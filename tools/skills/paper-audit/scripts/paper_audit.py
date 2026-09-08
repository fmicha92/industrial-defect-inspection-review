#!/usr/bin/env python3
"""Audit registry and shallow-extraction checks for Paper Vault paper notes."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(
    os.environ.get("INSPECTION_EVIDENCE_ROOT") or next(
        parent for parent in Path(__file__).resolve().parents
        if (parent / "tools" / "config" / "repository.json").is_file()
    )
).resolve()
VAULT_DIR = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_VAULT",
        PROJECT_ROOT / "evidence" / "graph" / "vault",
    )
).resolve()
DEFAULT_REGISTRY = PROJECT_ROOT / "evidence" / "review" / "audits" / "paper_registry.json"
PAPERS_DIR = VAULT_DIR / "Papers"

SHALLOW_PATTERNS = [
    "concise extraction",
    "not fully extracted",
    "not fully reported",
    "not fully reported in this concise extraction",
    "not reported in this concise extraction",
    "see extracted snippets below",
    "not fully extracted",
    "not fully reported",
]

GENERIC_PATTERNS = [
    "visual inspection imagery or wafer maps as described by the source paper",
    "defect labels, anomaly scores, defect masks, bounding boxes, generated samples, or benchmark artifacts depending on the paper objective",
    "standard metric names are recorded when present; exact definitions are not fully extracted",
    "related-paper mapping was not completed",
    "created or updated if missing",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def rel(path: Path) -> str:
    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": 1, "updated_at": None, "papers": {}}
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("schema_version", 1)
    data.setdefault("papers", {})
    return data


def save_registry(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now_iso()
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
    tmp.replace(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    return parse_simple_yaml(raw), body


def parse_simple_yaml(raw: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(clean_scalar(line[4:]))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
        else:
            data[key] = clean_scalar(value)
    return data


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def git_added_at(path: Path) -> tuple[str | None, str]:
    rel_path = rel(path)
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%aI", "--", rel_path],
            cwd=PROJECT_ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
    except OSError:
        result = None
    if result and result.returncode == 0:
        dates = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        if dates:
            return dates[-1], "git"
    stat = path.stat()
    ts = min(stat.st_ctime, stat.st_mtime)
    return datetime.fromtimestamp(ts, timezone.utc).replace(microsecond=0).isoformat(), "filesystem"


def paper_notes() -> list[Path]:
    return sorted(PAPERS_DIR.glob("*/*.md"))


def source_exists(value: Any) -> bool:
    if not isinstance(value, str) or not value or value == "not reported":
        return False
    return (PROJECT_ROOT / value).exists()


def count_listish(value: Any) -> int:
    if isinstance(value, list):
        return len([x for x in value if str(x).strip()])
    if isinstance(value, str) and value.strip() and value != "not reported":
        return 1
    return 0


def automated_flags(note_path: Path) -> list[dict[str, str]]:
    text = read_text(note_path)
    frontmatter, body = split_frontmatter(text)
    lower = text.lower()
    flags: list[dict[str, str]] = []

    for pattern in SHALLOW_PATTERNS:
        if pattern in lower:
            flags.append({"severity": "high", "code": "shallow-placeholder", "detail": pattern})

    for pattern in GENERIC_PATTERNS:
        if pattern.lower() in lower:
            flags.append({"severity": "medium", "code": "generic-boilerplate", "detail": pattern})

    not_reported = len(re.findall(r"\bnot reported\b", lower))
    source_available = source_exists(frontmatter.get("preprocessed_input")) or source_exists(frontmatter.get("extracted_text"))
    if source_available and not_reported >= 20:
        flags.append({
            "severity": "medium",
            "code": "many-not-reported",
            "detail": f"{not_reported} occurrences with source input available",
        })

    if not source_exists(frontmatter.get("preprocessed_input")) and not source_exists(frontmatter.get("extracted_text")):
        flags.append({
            "severity": "medium",
            "code": "missing-source-input",
            "detail": "preprocessed_input and extracted_text are missing or unresolved",
        })

    metrics_count = count_listish(frontmatter.get("metrics"))
    if metrics_count and "### Performance Metrics" not in body and "## Performance Metrics" not in body:
        flags.append({
            "severity": "medium",
            "code": "metrics-without-section",
            "detail": f"{metrics_count} metric(s) in frontmatter but no performance metrics section",
        })

    if "| Reported in source text |" in text or "| not reported |" in text:
        flags.append({
            "severity": "medium",
            "code": "placeholder-result-table",
            "detail": "result table appears to contain placeholder rows",
        })

    return flags


def entry_from_note(note_path: Path, existing: dict[str, Any] | None = None) -> dict[str, Any]:
    existing = existing or {}
    text = read_text(note_path)
    frontmatter, _ = split_frontmatter(text)
    added_at = existing.get("added_at")
    added_source = existing.get("added_source")
    if not added_at:
        added_at, added_source = git_added_at(note_path)

    entry = dict(existing)
    entry.update({
        "note_path": rel(note_path),
        "title": frontmatter.get("title") or note_path.stem,
        "paper_key": frontmatter.get("paper_key", "not reported"),
        "year": frontmatter.get("year", "not reported"),
        "paper_type": frontmatter.get("paper_type", note_path.parent.name.lower()),
        "source_file": frontmatter.get("source_file", "not reported"),
        "preprocessed_input": frontmatter.get("preprocessed_input", "not reported"),
        "extracted_text": frontmatter.get("extracted_text", "not reported"),
        "added_at": added_at,
        "added_source": added_source,
        "last_checked_at": now_iso(),
        "flags": automated_flags(note_path),
    })
    entry.setdefault("last_audited_at", None)
    entry.setdefault("audit_status", "never-audited")
    entry.setdefault("audit_history", [])
    entry.setdefault("last_linked_at", None)
    entry.setdefault("linked_notes", [])
    entry.setdefault("graph_audit_status", "not checked")
    return entry


def sync(args: argparse.Namespace) -> None:
    registry = load_registry(args.registry)
    papers = registry["papers"]
    seen: set[str] = set()
    for note in paper_notes():
        key = rel(note)
        seen.add(key)
        papers[key] = entry_from_note(note, papers.get(key))
    for key in list(papers):
        if key not in seen:
            papers[key]["missing"] = True
    save_registry(args.registry, registry)
    print(json.dumps({
        "registry": rel(args.registry),
        "paper_count": len(seen),
        "registered_count": len(papers),
    }, indent=2))


def year_sort(value: Any) -> int:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 9999


def queue_sort_key(item: dict[str, Any]) -> tuple[int, str, int, str]:
    last = item.get("last_audited_at")
    if not last:
        return (0, item.get("added_at") or "", year_sort(item.get("year")), item.get("note_path") or "")
    return (1, last, year_sort(item.get("year")), item.get("note_path") or "")


def queue(args: argparse.Namespace) -> None:
    registry = load_registry(args.registry)
    items = [v for v in registry.get("papers", {}).values() if not v.get("missing")]
    if args.with_flags:
        items = [item for item in items if item.get("flags")]
    items.sort(key=queue_sort_key)
    for item in items[: args.limit]:
        flag_summary = ",".join(sorted({f["code"] for f in item.get("flags", [])})) or "-"
        last = item.get("last_audited_at") or "never"
        print(f"{last}\t{item.get('added_at')}\t{item.get('audit_status')}\t{flag_summary}\t{item.get('note_path')}")


def check(args: argparse.Namespace) -> None:
    note = (PROJECT_ROOT / args.note).resolve()
    if not note.exists():
        raise SystemExit(f"note not found: {args.note}")
    entry = entry_from_note(note)
    print(json.dumps(entry, indent=2, sort_keys=True))


def mark(args: argparse.Namespace) -> None:
    registry = load_registry(args.registry)
    note = (PROJECT_ROOT / args.note).resolve()
    key = rel(note)
    if not note.exists():
        raise SystemExit(f"note not found: {args.note}")
    entry = entry_from_note(note, registry["papers"].get(key))
    if args.status == "fixed" and not args.graph_links_checked:
        raise SystemExit("--status fixed requires --graph-links-checked")
    linked_notes = [normalize_project_path(value) for value in args.linked_note]
    audit_event = {
        "audited_at": now_iso(),
        "status": args.status,
        "notes": args.notes,
        "graph_links_checked": args.graph_links_checked,
        "linked_notes": linked_notes,
        "graph_audit_status": args.graph_audit_status,
        "flags_at_audit": entry.get("flags", []),
    }
    entry["last_audited_at"] = audit_event["audited_at"]
    entry["audit_status"] = args.status
    entry["graph_audit_status"] = args.graph_audit_status
    if args.graph_links_checked:
        entry["last_linked_at"] = audit_event["audited_at"]
    if linked_notes:
        merged = sorted(set(entry.get("linked_notes", []) + linked_notes))
        entry["linked_notes"] = merged
    entry.setdefault("audit_history", []).append(audit_event)
    registry["papers"][key] = entry
    save_registry(args.registry, registry)
    print(json.dumps({"note_path": key, "audit_status": args.status, "last_audited_at": entry["last_audited_at"]}, indent=2))


def normalize_project_path(value: str) -> str:
    path = Path(value)
    if path.is_absolute():
        return rel(path)
    return path.as_posix()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    sub = parser.add_subparsers(dest="command", required=True)

    sync_parser = sub.add_parser("sync", help="sync paper notes into the audit registry")
    sync_parser.set_defaults(func=sync)

    queue_parser = sub.add_parser("queue", help="show papers in audit priority order")
    queue_parser.add_argument("--limit", type=int, default=20)
    queue_parser.add_argument("--with-flags", action="store_true", help="only show papers with automated flags")
    queue_parser.set_defaults(func=queue)

    check_parser = sub.add_parser("check", help="run automated checks for one note")
    check_parser.add_argument("note")
    check_parser.set_defaults(func=check)

    mark_parser = sub.add_parser("mark", help="mark a note after source-backed audit")
    mark_parser.add_argument("note")
    mark_parser.add_argument("--status", choices=["passed", "fixed", "needs-work"], required=True)
    mark_parser.add_argument("--notes", default="")
    mark_parser.add_argument("--graph-links-checked", action="store_true", help="confirm related graph notes were reviewed/refreshed")
    mark_parser.add_argument("--linked-note", action="append", default=[], help="related note updated or reviewed during relink pass")
    mark_parser.add_argument("--graph-audit-status", default="not run", help="graph audit result, e.g. passed, warnings, not run")
    mark_parser.set_defaults(func=mark)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not args.registry.is_absolute():
        args.registry = PROJECT_ROOT / args.registry
    args.func(args)


if __name__ == "__main__":
    main()
