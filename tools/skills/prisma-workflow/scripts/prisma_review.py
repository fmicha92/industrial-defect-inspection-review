#!/usr/bin/env python3
"""PRISMA-style review record tracker.

The script keeps a persistent record set and decision audit trail for systematic
or scoping reviews. It intentionally uses only the Python standard library so it
can run anywhere the paper vault scripts run.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


ROOT = Path(
    os.environ.get("INSPECTION_EVIDENCE_ROOT") or next(
        parent for parent in Path(__file__).resolve().parents
        if (parent / "tools" / "config" / "repository.json").is_file()
    )
).resolve()
DEFAULT_OUT_DIR = ROOT / "evidence" / "review" / "sessions"


SCREEN_UNSCREENED = "unscreened"
SCREEN_DUPLICATE = "duplicate"
SCREEN_EXCLUDED = "title_abstract_excluded"
SCREEN_INCLUDED = "title_abstract_included"

FT_NOT_SOUGHT = "not_sought"
FT_SOUGHT = "sought"
FT_RETRIEVED = "retrieved"
FT_NOT_RETRIEVED = "not_retrieved"

INCLUDE_UNDECIDED = "undecided"
INCLUDE_ASSESSED = "full_text_assessed"
INCLUDE_EXCLUDED = "excluded"
INCLUDE_INCLUDED = "included"


class PrismaError(RuntimeError):
    """Human-readable workflow error."""


@dataclass(frozen=True)
class DecisionUpdate:
    record_id: str
    action: str
    details: dict[str, Any]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(text: str, max_len: int = 72) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug[:max_len].strip("-") or "prisma-review")


def normalize_space(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalize_id(value: Any) -> str:
    return normalize_space(value).lower().replace("https://doi.org/", "").replace("doi:", "")


def normalize_title(value: Any) -> str:
    value = normalize_space(value).lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return normalize_space(value)


def stable_record_id(record: dict[str, Any]) -> str:
    for key in ("paper_id", "openalex_id", "doi", "arxiv_id", "id"):
        value = normalize_space(record.get(key))
        if value:
            if key == "openalex_id" and value.startswith("https://openalex.org/"):
                return value.rstrip("/").split("/")[-1]
            if key == "doi":
                return normalize_id(value)
            return value
    title = normalize_title(record.get("title"))
    year = normalize_space(record.get("year"))
    digest = hashlib.sha1(f"{title}|{year}".encode("utf-8")).hexdigest()[:12]
    return f"record-{digest}"


def maybe_openalex_id(record: dict[str, Any]) -> str:
    for key in ("paper_id", "openalex_id", "id"):
        value = normalize_space(record.get(key))
        if not value:
            continue
        if value.startswith("https://openalex.org/"):
            return value.rstrip("/").split("/")[-1]
        if re.fullmatch(r"W\d+", value):
            return value
    url = normalize_space(record.get("openalex_url"))
    if url.startswith("https://openalex.org/"):
        return url.rstrip("/").split("/")[-1]
    return ""


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [normalize_space(v) for v in value if normalize_space(v)]
    return [normalize_space(value)] if normalize_space(value) else []


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def append_decisions(session: Path, updates: list[DecisionUpdate]) -> None:
    if not updates:
        return
    path = session / "decisions.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        for update in updates:
            payload = {
                "timestamp": utc_now(),
                "record_id": update.record_id,
                "action": update.action,
                **update.details,
            }
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def load_session(session: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if not session.exists():
        raise PrismaError(f"Session does not exist: {session}")
    state_path = session / "state.json"
    records_path = session / "records.json"
    if not state_path.exists() or not records_path.exists():
        raise PrismaError(f"Missing state.json or records.json in {session}")
    return load_json(state_path), load_json(records_path)


def save_session(session: Path, state: dict[str, Any], records: list[dict[str, Any]]) -> None:
    state["updated_at"] = utc_now()
    save_json(session / "state.json", state)
    save_json(session / "records.json", records)


def add_event(state: dict[str, Any], action: str, **details: Any) -> None:
    state.setdefault("events", []).append({"timestamp": utc_now(), "action": action, **details})


def extract_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        raise PrismaError("Import JSON must be a list or an object containing records.")
    for key in ("candidates", "results", "records", "shortlist", "papers"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
    raise PrismaError("Could not find records in JSON; expected candidates, results, records, shortlist, or papers.")


def normalize_record(raw: dict[str, Any], source: str) -> dict[str, Any]:
    external_ids = raw.get("external_ids") if isinstance(raw.get("external_ids"), dict) else {}
    doi = raw.get("doi") or external_ids.get("doi")
    arxiv_id = raw.get("arxiv_id") or external_ids.get("arxiv")
    openalex_id = maybe_openalex_id(raw)
    record = {
        "record_id": stable_record_id({**raw, "doi": doi, "arxiv_id": arxiv_id, "openalex_id": openalex_id}),
        "title": normalize_space(raw.get("title")),
        "authors": as_list(raw.get("authors")),
        "year": raw.get("year") or raw.get("publication_year") or "",
        "venue": normalize_space(raw.get("venue") or raw.get("source") or raw.get("host_venue", "")),
        "doi": normalize_id(doi),
        "arxiv_id": normalize_space(arxiv_id),
        "openalex_id": openalex_id,
        "openalex_url": normalize_space(raw.get("openalex_url") or (f"https://openalex.org/{openalex_id}" if openalex_id else "")),
        "url": normalize_space(raw.get("landing_url") or raw.get("url") or raw.get("primary_location", "")),
        "pdf": normalize_space(raw.get("open_access_pdf") or raw.get("pdf") or ""),
        "abstract": normalize_space(raw.get("abstract")),
        "source": source,
        "screen_status": SCREEN_UNSCREENED,
        "screen_exclusion_reason": "",
        "full_text_status": FT_NOT_SOUGHT,
        "full_text_retrieval_reason": "",
        "include_status": INCLUDE_UNDECIDED,
        "full_text_exclusion_reason": "",
        "duplicate_of": "",
        "imported_at": utc_now(),
    }
    if not record["title"]:
        record["title"] = "not reported"
    return record


def parse_csv_ids(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def parse_key_values(values: list[str] | None, label: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for value in values or []:
        if "=" not in value:
            raise PrismaError(f"{label} entries must use ID=reason: {value}")
        key, reason = value.split("=", 1)
        key = key.strip()
        reason = reason.strip()
        if not key or not reason:
            raise PrismaError(f"{label} entries need both ID and reason: {value}")
        parsed[key] = reason
    return parsed


def candidate_keys(record: dict[str, Any]) -> list[str]:
    keys = [
        record.get("record_id"),
        record.get("doi"),
        record.get("arxiv_id"),
        record.get("openalex_id"),
        record.get("openalex_url"),
    ]
    return [normalize_id(k) for k in keys if normalize_id(k)]


def resolve_record(records: list[dict[str, Any]], token: str) -> dict[str, Any]:
    token_norm = normalize_id(token)
    exact = [record for record in records if token_norm in candidate_keys(record)]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise PrismaError(f"Ambiguous ID {token}; matched {len(exact)} records.")

    prefix = [
        record
        for record in records
        if any(key.startswith(token_norm) for key in candidate_keys(record)) or normalize_title(record.get("title")).startswith(normalize_title(token))
    ]
    if len(prefix) == 1:
        return prefix[0]
    if len(prefix) > 1:
        raise PrismaError(f"Ambiguous ID prefix {token}; matched {len(prefix)} records.")
    raise PrismaError(f"Could not resolve record ID: {token}")


def command_init(args: argparse.Namespace) -> None:
    out_dir = Path(args.out_dir) if args.out_dir else DEFAULT_OUT_DIR
    session = out_dir / slugify(args.question)
    if session.exists() and any(session.iterdir()):
        raise PrismaError(f"Session already exists: {session}")
    session.mkdir(parents=True, exist_ok=True)
    state = {
        "question": args.question,
        "slug": session.name,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "phase": "initialized",
        "events": [],
    }
    add_event(state, "init", question=args.question)
    save_json(session / "state.json", state)
    save_json(session / "records.json", [])
    (session / "decisions.jsonl").touch()
    print(json.dumps({"session": str(session), "slug": session.name}, indent=2))


def command_import_openalex(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    payload = load_json(Path(args.json_file))
    imported = [normalize_record(record, args.source) for record in extract_records(payload)]
    existing_ids = {record["record_id"] for record in records}
    added = []
    skipped = 0
    for record in imported:
        if record["record_id"] in existing_ids:
            skipped += 1
            continue
        existing_ids.add(record["record_id"])
        records.append(record)
        added.append(record)
    add_event(state, "import-openalex", source=args.source, added=len(added), skipped_existing=skipped)
    state["phase"] = "imported"
    save_session(session, state, records)
    append_decisions(session, [DecisionUpdate(r["record_id"], "imported", {"source": args.source}) for r in added])
    print(json.dumps({"added": len(added), "skipped_existing": skipped, "total_records": len(records)}, indent=2))


def dedup_key(record: dict[str, Any]) -> tuple[str, str] | None:
    for field in ("doi", "arxiv_id", "openalex_id"):
        value = normalize_id(record.get(field))
        if value:
            return field, value
    title = normalize_title(record.get("title"))
    if title and title != "not reported":
        return "title", title
    return None


def command_dedup(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    seen: dict[tuple[str, str], str] = {}
    updates: list[DecisionUpdate] = []
    duplicates = 0

    for record in records:
        if record["screen_status"] == SCREEN_DUPLICATE:
            continue
        key = dedup_key(record)
        if key and key in seen:
            record["screen_status"] = SCREEN_DUPLICATE
            record["duplicate_of"] = seen[key]
            duplicates += 1
            updates.append(DecisionUpdate(record["record_id"], "duplicate", {"duplicate_of": seen[key], "basis": key[0]}))
            continue
        if key:
            seen[key] = record["record_id"]

    active_titles = [(normalize_title(r.get("title")), r["record_id"]) for r in records if r["screen_status"] != SCREEN_DUPLICATE]
    for record in records:
        if record["screen_status"] == SCREEN_DUPLICATE:
            continue
        title = normalize_title(record.get("title"))
        if not title or title == "not reported":
            continue
        for other_title, other_id in active_titles:
            if other_id == record["record_id"] or other_id == record.get("duplicate_of"):
                continue
            if other_id > record["record_id"]:
                continue
            if SequenceMatcher(None, title, other_title).ratio() >= args.fuzzy_threshold:
                record["screen_status"] = SCREEN_DUPLICATE
                record["duplicate_of"] = other_id
                duplicates += 1
                updates.append(DecisionUpdate(record["record_id"], "duplicate", {"duplicate_of": other_id, "basis": "fuzzy_title"}))
                break

    add_event(state, "dedup", duplicates_marked=duplicates, fuzzy_threshold=args.fuzzy_threshold)
    state["phase"] = "deduplicated"
    save_session(session, state, records)
    append_decisions(session, updates)
    print(json.dumps({"duplicates_marked": duplicates, "total_records": len(records)}, indent=2))


def command_screen(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    include_ids = parse_csv_ids(args.include)
    exclude_map = parse_key_values(args.exclude, "--exclude")
    updates: list[DecisionUpdate] = []

    for token in include_ids:
        record = resolve_record(records, token)
        if record["screen_status"] == SCREEN_DUPLICATE:
            raise PrismaError(f"Cannot include duplicate record at screening: {token}")
        record["screen_status"] = SCREEN_INCLUDED
        record["full_text_status"] = FT_SOUGHT
        updates.append(DecisionUpdate(record["record_id"], "title_abstract_included", {}))

    for token, reason in exclude_map.items():
        record = resolve_record(records, token)
        if record["screen_status"] == SCREEN_DUPLICATE:
            raise PrismaError(f"Cannot exclude duplicate record as screened-out: {token}")
        record["screen_status"] = SCREEN_EXCLUDED
        record["screen_exclusion_reason"] = reason
        record["full_text_status"] = FT_NOT_SOUGHT
        record["include_status"] = INCLUDE_EXCLUDED
        updates.append(DecisionUpdate(record["record_id"], "title_abstract_excluded", {"reason": reason}))

    add_event(state, "screen", included=len(include_ids), excluded=len(exclude_map))
    state["phase"] = "screening"
    save_session(session, state, records)
    append_decisions(session, updates)
    print(json.dumps({"screen_included": len(include_ids), "screen_excluded": len(exclude_map)}, indent=2))


def command_fulltext(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    retrieved_ids = parse_csv_ids(args.retrieved)
    not_retrieved_map = parse_key_values(args.not_retrieved, "--not-retrieved")
    exclude_map = parse_key_values(args.exclude, "--exclude")
    updates: list[DecisionUpdate] = []

    for token in retrieved_ids:
        record = resolve_record(records, token)
        record["full_text_status"] = FT_RETRIEVED
        if record["include_status"] == INCLUDE_UNDECIDED:
            record["include_status"] = INCLUDE_ASSESSED
        updates.append(DecisionUpdate(record["record_id"], "full_text_retrieved", {}))

    for token, reason in not_retrieved_map.items():
        record = resolve_record(records, token)
        record["full_text_status"] = FT_NOT_RETRIEVED
        record["full_text_retrieval_reason"] = reason
        record["include_status"] = INCLUDE_EXCLUDED
        updates.append(DecisionUpdate(record["record_id"], "full_text_not_retrieved", {"reason": reason}))

    for token, reason in exclude_map.items():
        record = resolve_record(records, token)
        if record["full_text_status"] == FT_NOT_SOUGHT:
            record["full_text_status"] = FT_RETRIEVED
        record["include_status"] = INCLUDE_EXCLUDED
        record["full_text_exclusion_reason"] = reason
        updates.append(DecisionUpdate(record["record_id"], "full_text_excluded", {"reason": reason}))

    add_event(state, "fulltext", retrieved=len(retrieved_ids), not_retrieved=len(not_retrieved_map), excluded=len(exclude_map))
    state["phase"] = "eligibility"
    save_session(session, state, records)
    append_decisions(session, updates)
    print(json.dumps({"retrieved": len(retrieved_ids), "not_retrieved": len(not_retrieved_map), "full_text_excluded": len(exclude_map)}, indent=2))


def command_include(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    include_ids = parse_csv_ids(args.include)
    updates: list[DecisionUpdate] = []
    for token in include_ids:
        record = resolve_record(records, token)
        if record["screen_status"] in (SCREEN_DUPLICATE, SCREEN_EXCLUDED):
            raise PrismaError(f"Cannot include a duplicate or title/abstract-excluded record: {token}")
        record["include_status"] = INCLUDE_INCLUDED
        if record["full_text_status"] in (FT_NOT_SOUGHT, FT_SOUGHT):
            record["full_text_status"] = FT_RETRIEVED
        updates.append(DecisionUpdate(record["record_id"], "included", {}))
    add_event(state, "include", included=len(include_ids))
    state["phase"] = "included"
    save_session(session, state, records)
    append_decisions(session, updates)
    print(json.dumps({"included": len(include_ids)}, indent=2))


def compute_counts(records: list[dict[str, Any]]) -> dict[str, Any]:
    source_counts = Counter(record.get("source") or "not reported" for record in records)
    duplicate_count = sum(1 for r in records if r["screen_status"] == SCREEN_DUPLICATE)
    screened_count = sum(1 for r in records if r["screen_status"] != SCREEN_DUPLICATE)
    screen_excluded = [r for r in records if r["screen_status"] == SCREEN_EXCLUDED]
    sought = [r for r in records if r["screen_status"] == SCREEN_INCLUDED]
    not_retrieved = [r for r in records if r["full_text_status"] == FT_NOT_RETRIEVED]
    assessed = [r for r in records if r["full_text_status"] == FT_RETRIEVED and r["screen_status"] == SCREEN_INCLUDED]
    ft_excluded = [r for r in records if r["include_status"] == INCLUDE_EXCLUDED and r.get("full_text_exclusion_reason")]
    included = [r for r in records if r["include_status"] == INCLUDE_INCLUDED]
    return {
        "identified": len(records),
        "source_counts": source_counts,
        "duplicates": duplicate_count,
        "screened": screened_count,
        "screen_excluded": len(screen_excluded),
        "screen_exclusion_reasons": Counter(r.get("screen_exclusion_reason") or "not reported" for r in screen_excluded),
        "reports_sought": len(sought),
        "reports_not_retrieved": len(not_retrieved),
        "not_retrieved_reasons": Counter(r.get("full_text_retrieval_reason") or "not reported" for r in not_retrieved),
        "reports_assessed": len(assessed),
        "full_text_excluded": len(ft_excluded),
        "full_text_exclusion_reasons": Counter(r.get("full_text_exclusion_reason") or "not reported" for r in ft_excluded),
        "included": len(included),
    }


def counter_lines(counter: Counter[str]) -> list[str]:
    if not counter:
        return ["  - none"]
    return [f"  - {reason}: {count}" for reason, count in counter.most_common()]


def command_flow(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    counts = compute_counts(records)
    out = Path(args.out) if args.out else session / "flow.md"
    lines = [
        f"# PRISMA Flow: {state.get('question', 'not reported')}",
        "",
        "## Identification",
        f"- Records identified from databases/registers: {counts['identified']}",
        "- Source breakdown:",
        *[f"  - {source}: {count}" for source, count in counts["source_counts"].most_common()],
        f"- Duplicate records removed before screening: {counts['duplicates']}",
        "",
        "## Screening",
        f"- Records screened: {counts['screened']}",
        f"- Records excluded: {counts['screen_excluded']}",
        "- Title/abstract exclusion reasons:",
        *counter_lines(counts["screen_exclusion_reasons"]),
        "",
        "## Eligibility",
        f"- Reports sought for retrieval: {counts['reports_sought']}",
        f"- Reports not retrieved: {counts['reports_not_retrieved']}",
        "- Not-retrieved reasons:",
        *counter_lines(counts["not_retrieved_reasons"]),
        f"- Reports assessed for eligibility: {counts['reports_assessed']}",
        f"- Reports excluded after full-text assessment: {counts['full_text_excluded']}",
        "- Full-text exclusion reasons:",
        *counter_lines(counts["full_text_exclusion_reasons"]),
        "",
        "## Included",
        f"- Studies included in review: {counts['included']}",
        "",
        f"Generated: {utc_now()}",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    add_event(state, "flow", out=str(out))
    save_session(session, state, records)
    print(json.dumps({"flow": str(out), "included": counts["included"]}, indent=2))


CHECKLIST_ROWS = [
    ("Title", "1", "Identify the report as a systematic review."),
    ("Abstract", "2", "Provide a structured summary."),
    ("Rationale", "3", "Describe the rationale for the review."),
    ("Objectives", "4", "State the review objectives or questions."),
    ("Eligibility criteria", "5", "Specify inclusion and exclusion criteria."),
    ("Information sources", "6", "Specify databases, registers, websites, organizations, and dates searched."),
    ("Search strategy", "7", "Present full search strategies for all sources."),
    ("Selection process", "8", "Specify how records were screened and selected."),
    ("Data collection process", "9", "Specify how data were collected from reports."),
    ("Data items", "10a", "List all outcomes for which data were sought."),
    ("Data items", "10b", "List other variables for which data were sought."),
    ("Study risk of bias assessment", "11", "Specify methods for assessing risk of bias."),
    ("Effect measures", "12", "Specify effect measures for each outcome."),
    ("Synthesis methods", "13a", "Describe processes for deciding which studies were eligible for each synthesis."),
    ("Synthesis methods", "13b", "Describe data preparation for synthesis."),
    ("Synthesis methods", "13c", "Describe tabulation or visual display methods."),
    ("Synthesis methods", "13d", "Describe synthesis methods."),
    ("Synthesis methods", "13e", "Describe exploration of heterogeneity."),
    ("Synthesis methods", "13f", "Describe sensitivity analyses."),
    ("Reporting bias assessment", "14", "Describe methods for assessing reporting bias."),
    ("Certainty assessment", "15", "Describe methods for assessing certainty in evidence."),
    ("Study selection", "16a", "Report screening and inclusion results."),
    ("Study selection", "16b", "Cite studies that appeared to meet criteria but were excluded and explain why."),
    ("Study characteristics", "17", "Cite each included study and present characteristics."),
    ("Risk of bias in studies", "18", "Present risk-of-bias assessments."),
    ("Results of individual studies", "19", "Present results for all outcomes."),
    ("Results of syntheses", "20a", "Summarize characteristics and risk of bias for contributing studies."),
    ("Results of syntheses", "20b", "Present results of each synthesis."),
    ("Results of syntheses", "20c", "Present results of heterogeneity investigations."),
    ("Results of syntheses", "20d", "Present sensitivity analyses."),
    ("Reporting biases", "21", "Present assessments of reporting bias."),
    ("Certainty of evidence", "22", "Present certainty assessments."),
    ("Discussion", "23a", "Interpret results in context."),
    ("Discussion", "23b", "Discuss limitations of included evidence."),
    ("Discussion", "23c", "Discuss limitations of review processes."),
    ("Discussion", "23d", "Discuss implications for practice, policy, or research."),
    ("Registration and protocol", "24a", "Provide registration information."),
    ("Registration and protocol", "24b", "Indicate where the protocol can be accessed."),
    ("Registration and protocol", "24c", "Describe protocol amendments."),
    ("Support", "25", "Describe financial or non-financial support."),
    ("Competing interests", "26", "Declare competing interests."),
    ("Availability", "27", "Report availability of data, code, and materials."),
]


def command_checklist(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    out = Path(args.out) if args.out else session / "checklist.md"
    lines = [
        f"# PRISMA Checklist: {state.get('question', 'not reported')}",
        "",
        "| Section | Item | Checklist item | Location | Notes |",
        "|---|---:|---|---|---|",
    ]
    lines.extend(f"| {section} | {item} | {text} |  |  |" for section, item, text in CHECKLIST_ROWS)
    lines.extend(["", f"Generated: {utc_now()}"])
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    add_event(state, "checklist", out=str(out))
    save_session(session, state, records)
    print(json.dumps({"checklist": str(out), "items": len(CHECKLIST_ROWS)}, indent=2))


def command_status(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    counts = compute_counts(records)
    unscreened = sum(1 for r in records if r["screen_status"] == SCREEN_UNSCREENED)
    print(f"Question: {state.get('question', 'not reported')}")
    print(f"Phase: {state.get('phase', 'not reported')}")
    print(f"Records: {len(records)}")
    print(f"Duplicates: {counts['duplicates']}")
    print(f"Unscreened: {unscreened}")
    print(f"Title/abstract included: {counts['reports_sought']}")
    print(f"Reports assessed: {counts['reports_assessed']}")
    print(f"Included studies: {counts['included']}")
    if unscreened:
        print("Next: screen remaining records with `screen` and explicit include/exclude decisions.")
    elif counts["reports_sought"] and counts["reports_assessed"] < counts["reports_sought"]:
        print("Next: record full-text retrieval and eligibility with `fulltext`.")
    else:
        print("Next: run `flow` and fill the generated checklist locations.")


def command_export_csv(args: argparse.Namespace) -> None:
    session = Path(args.session)
    state, records = load_session(session)
    out = Path(args.out) if args.out else session / "records.csv"
    fields = [
        "record_id",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "arxiv_id",
        "openalex_id",
        "openalex_url",
        "url",
        "pdf",
        "source",
        "screen_status",
        "screen_exclusion_reason",
        "full_text_status",
        "full_text_retrieval_reason",
        "include_status",
        "full_text_exclusion_reason",
        "duplicate_of",
    ]
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = {field: record.get(field, "") for field in fields}
            row["authors"] = "; ".join(as_list(row["authors"]))
            writer.writerow(row)
    add_event(state, "export-csv", out=str(out))
    save_session(session, state, records)
    print(json.dumps({"csv": str(out), "records": len(records)}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track PRISMA review records and decisions.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create a PRISMA review session.")
    init.add_argument("question")
    init.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    init.set_defaults(func=command_init)

    imp = subparsers.add_parser("import-openalex", help="Import OpenAlex-style JSON records.")
    imp.add_argument("session")
    imp.add_argument("json_file")
    imp.add_argument("--source", default="OpenAlex")
    imp.set_defaults(func=command_import_openalex)

    dedup = subparsers.add_parser("dedup", help="Mark duplicate records.")
    dedup.add_argument("session")
    dedup.add_argument("--fuzzy-threshold", type=float, default=0.96)
    dedup.set_defaults(func=command_dedup)

    screen = subparsers.add_parser("screen", help="Record title/abstract screening decisions.")
    screen.add_argument("session")
    screen.add_argument("--include", help="Comma-separated record IDs to include.")
    screen.add_argument("--exclude", nargs="*", help="Record exclusions as ID=reason entries.")
    screen.set_defaults(func=command_screen)

    fulltext = subparsers.add_parser("fulltext", help="Record full-text retrieval and eligibility decisions.")
    fulltext.add_argument("session")
    fulltext.add_argument("--retrieved", help="Comma-separated record IDs retrieved for full-text review.")
    fulltext.add_argument("--not-retrieved", nargs="*", help="Retrieval failures as ID=reason entries.")
    fulltext.add_argument("--exclude", nargs="*", help="Full-text exclusions as ID=reason entries.")
    fulltext.set_defaults(func=command_fulltext)

    include = subparsers.add_parser("include", help="Mark studies included in the review.")
    include.add_argument("session")
    include.add_argument("--include", required=True, help="Comma-separated record IDs to include.")
    include.set_defaults(func=command_include)

    flow = subparsers.add_parser("flow", help="Write PRISMA flow counts to Markdown.")
    flow.add_argument("session")
    flow.add_argument("--out")
    flow.set_defaults(func=command_flow)

    checklist = subparsers.add_parser("checklist", help="Write a PRISMA checklist scaffold.")
    checklist.add_argument("session")
    checklist.add_argument("--out")
    checklist.set_defaults(func=command_checklist)

    status = subparsers.add_parser("status", help="Print session status and next action.")
    status.add_argument("session")
    status.set_defaults(func=command_status)

    export_csv = subparsers.add_parser("export-csv", help="Export records and decisions to CSV.")
    export_csv.add_argument("session")
    export_csv.add_argument("--out")
    export_csv.set_defaults(func=command_export_csv)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except PrismaError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
