"""Generate public, deterministic exports from the Markdown evidence graph."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from .repository import load_config
from .vault import Note, as_strings, duplicate_titles, iter_notes, resolve_edges, scalar, wikilink_targets


SYNTHESIS_RE = re.compile(
    r"\bsynthe(?:sis|tic)|\bgenerative?\b|\bgenerat(?:ed|ion)\b|\bgan\b|"
    r"diffusion|simulat(?:ion|ed)|procedural|cutpaste|copy[- ]?paste|"
    r"(?:defect|anomaly|pseudo[- ]?anomaly) insertion",
    re.IGNORECASE,
)

CONTEXTUAL_DOMAINS = {
    "autonomous driving",
    "document analysis",
    "general computer vision",
    "medical imaging",
    "natural language processing",
}


def _join(value: Any, separator: str) -> str:
    return separator.join(dict.fromkeys(as_strings(value)))


def _csv_text(rows: list[dict[str, Any]], fields: list[str]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def _availability(note: Note) -> str:
    parts = Path(note.relative_path).parts
    if len(parts) >= 2 and parts[0] == "Datasets":
        group = parts[1].lower()
        if group == "public":
            return "public"
        if group == "private":
            return "private"
        if group == "availability unspecified":
            return "unspecified"
    explicit = scalar(note.metadata.get("availability")).lower()
    return explicit or "not reported"


def _dataset_rows(notes: list[Note], separator: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for note in notes:
        if note.node_type != "Datasets" or note.relative_path == "Datasets/Dataset Source Links.md":
            continue
        metadata = note.metadata
        licenses = as_strings(metadata.get("licenses")) or as_strings(metadata.get("license"))
        domains = (
            as_strings(metadata.get("related_domain"))
            or as_strings(metadata.get("domain"))
            or as_strings(metadata.get("related_domains"))
            or as_strings(metadata.get("domains"))
        )
        contextual_domains = sorted(
            {domain for domain in domains if domain.casefold() in CONTEXTUAL_DOMAINS},
            key=str.casefold,
        )
        scope_screen = "contextual" if contextual_domains else "manufacturing candidate"
        scope_reason = (
            "Automated exclusion-domain match: " + separator.join(contextual_domains)
            if contextual_domains
            else "No automated non-manufacturing domain exclusion matched; manual scope confirmation required."
        )
        rows.append({
            "dataset_id": note.node_id,
            "title": note.title,
            "aliases": separator.join(note.aliases),
            "availability": _availability(note),
            "availability_detail": scalar(metadata.get("availability"), dewikify=False),
            "availability_group": Path(note.relative_path).parts[1] if len(Path(note.relative_path).parts) > 2 else "root",
            "domain": separator.join(domains),
            "scope_screen": scope_screen,
            "scope_reason": scope_reason,
            "url": scalar(metadata.get("url"), dewikify=False),
            "access": scalar(metadata.get("access"), dewikify=False),
            "license_evidence": separator.join(licenses),
            "data_sources": _join(metadata.get("data_sources"), separator),
            "introduced_by": scalar(metadata.get("introduced_by")),
            "related_papers": _join(metadata.get("related_papers"), separator),
            "source_note": note.relative_path,
        })
    return sorted(rows, key=lambda row: row["dataset_id"].casefold())


def _public_dataset_lookup(
    dataset_rows: list[dict[str, str]], separator: str, *, manufacturing_only: bool = False
) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for row in dataset_rows:
        if row["availability"] != "public":
            continue
        if manufacturing_only and row["scope_screen"] != "manufacturing candidate":
            continue
        lookup[row["title"].casefold()] = row["title"]
        for alias in row["aliases"].split(separator):
            if alias.strip():
                lookup[alias.strip().casefold()] = row["title"]
    return lookup


def _synthesis_families(text: str) -> list[str]:
    lower = text.lower()
    families: list[str] = []
    if "diffusion" in lower:
        families.append("diffusion-based generation")
    if re.search(r"\bgan\b|generative adversarial", lower):
        families.append("GAN-based generation")
    if "simulation" in lower or "simulated" in lower:
        families.append("simulation")
    if "procedural" in lower:
        families.append("procedural synthesis")
    if re.search(r"cutpaste|copy[- ]?paste|(?:defect|anomaly) insertion|rule-based", lower):
        families.append("rule-based insertion")
    if not families and SYNTHESIS_RE.search(text):
        families.append("other generative synthesis")
    return families


def _paper_rows(
    notes: list[Note], dataset_rows: list[dict[str, str]], separator: str
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    public_lookup = _public_dataset_lookup(dataset_rows, separator)
    manufacturing_lookup = _public_dataset_lookup(
        dataset_rows, separator, manufacturing_only=True
    )
    rows: list[dict[str, str]] = []
    candidates: list[dict[str, str]] = []
    for note in notes:
        if note.node_type != "Papers":
            continue
        metadata = note.metadata
        datasets = as_strings(metadata.get("datasets")) or as_strings(metadata.get("related_datasets"))
        public_datasets = sorted(
            {public_lookup[item.casefold()] for item in datasets if item.casefold() in public_lookup},
            key=str.casefold,
        )
        manufacturing_datasets = sorted(
            {
                manufacturing_lookup[item.casefold()]
                for item in datasets
                if item.casefold() in manufacturing_lookup
            },
            key=str.casefold,
        )
        structured_parts = [note.title]
        for key in ("topics", "methods", "architectures", "related_methods"):
            structured_parts.extend(as_strings(metadata.get(key)))
        structured_text = " ".join(structured_parts)
        structured_match = SYNTHESIS_RE.search(structured_text)
        body_match = SYNTHESIS_RE.search(note.body)
        is_candidate = bool(manufacturing_datasets and (structured_match or body_match))
        match_location = "structured metadata" if structured_match else ("note body" if body_match else "none")
        family_text = structured_text if structured_match else note.body
        families = _synthesis_families(family_text) if is_candidate else []
        row = {
            "paper_id": scalar(metadata.get("paper_key"), dewikify=False) or note.node_id,
            "title": note.title,
            "year": scalar(metadata.get("year"), dewikify=False),
            "paper_type": scalar(metadata.get("paper_type"), dewikify=False),
            "venue": scalar(metadata.get("venue"), dewikify=False),
            "authors": _join(metadata.get("authors"), separator),
            "doi": scalar(metadata.get("doi"), dewikify=False),
            "arxiv": scalar(metadata.get("arxiv"), dewikify=False),
            "url": scalar(metadata.get("url"), dewikify=False),
            "status": scalar(metadata.get("status"), dewikify=False),
            "datasets": separator.join(datasets),
            "public_datasets": separator.join(public_datasets),
            "manufacturing_dataset_candidates": separator.join(manufacturing_datasets),
            "methods": _join(metadata.get("methods"), separator),
            "tasks": _join(metadata.get("tasks"), separator),
            "domains": _join(metadata.get("domains"), separator),
            "metrics": _join(metadata.get("metrics"), separator),
            "synthesis_candidate": "yes" if is_candidate else "no",
            "candidate_match_location": match_location,
            "synthesis_families": separator.join(families),
            "source_note": note.relative_path,
        }
        rows.append(row)
        if is_candidate:
            candidates.append({
                **row,
                "eligibility_status": "manual confirmation required",
                "dataset_scope_status": "automated manufacturing-scope screen; manual confirmation required",
                "candidate_reason": (
                    "References public dataset note(s) passing the automated manufacturing-scope screen "
                    f"and matches explicit synthesis terminology in {match_location}."
                ),
            })
    key = lambda row: (row["year"], row["title"].casefold(), row["source_note"].casefold())
    return sorted(rows, key=key), sorted(candidates, key=key)


def _node_rows(notes: list[Note], separator: str) -> list[dict[str, str]]:
    rows = []
    for note in notes:
        metadata = note.metadata
        rows.append({
            "node_id": note.node_id,
            "node_type": note.node_type,
            "title": note.title,
            "aliases": separator.join(note.aliases),
            "status": scalar(metadata.get("status"), dewikify=False),
            "year": scalar(metadata.get("year"), dewikify=False),
            "paper_type": scalar(metadata.get("paper_type"), dewikify=False),
            "availability": _availability(note) if note.node_type == "Datasets" else "",
            "paper_key": scalar(metadata.get("paper_key"), dewikify=False),
            "doi": scalar(metadata.get("doi"), dewikify=False),
            "url": scalar(metadata.get("url"), dewikify=False),
            "source_note": note.relative_path,
        })
    return sorted(rows, key=lambda row: row["node_id"].casefold())


def _vault_hash(notes: list[Note]) -> str:
    digest = hashlib.sha256()
    for note in sorted(notes, key=lambda item: item.relative_path.casefold()):
        digest.update(note.relative_path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(note.path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def statistics_markdown(notes: list[Note], snapshot_date: str) -> str:
    edges = resolve_edges(notes)
    links_total = sum(len(wikilink_targets(note.path.read_text(encoding="utf-8", errors="replace"))) for note in notes)
    by_folder = Counter(note.node_type for note in notes)
    paper_types = Counter(scalar(note.metadata.get("paper_type"), dewikify=False) or "not reported" for note in notes if note.node_type == "Papers")
    paper_status = Counter(scalar(note.metadata.get("status"), dewikify=False) or "not reported" for note in notes if note.node_type == "Papers")
    availability = Counter(_availability(note) for note in notes if note.node_type == "Datasets" and note.relative_path != "Datasets/Dataset Source Links.md")
    resolved = Counter(edge.resolution for edge in edges)
    duplicates = duplicate_titles(notes)

    lines = [
        "---",
        'title: "Vault Statistics"',
        "tags:",
        "  - vault/statistics",
        f'updated_at: "{snapshot_date}"',
        'source_script: "src/inspection_evidence/exporter.py"',
        "---",
        "",
        "# Vault Statistics",
        "",
        f"Snapshot: {snapshot_date}",
        "",
        "## Core Counts",
        "",
        "| Item | Count |",
        "|---|---:|",
        f"| Total vault notes | {len(notes)} |",
        f"| Total paper notes | {by_folder.get('Papers', 0)} |",
        f"| Total dataset notes | {by_folder.get('Datasets', 0)} |",
        f"| Wikilink occurrences | {links_total} |",
        f"| Unique source-target links | {len(edges)} |",
        f"| Resolved links | {resolved.get('resolved', 0)} |",
        f"| Ambiguous links | {resolved.get('ambiguous', 0)} |",
        f"| Unresolved links | {resolved.get('unresolved', 0)} |",
        f"| Duplicate display titles | {len(duplicates)} |",
        "",
        "## Notes By Top-Level Folder",
        "",
        "| Folder | Count |",
        "|---|---:|",
    ]
    lines.extend(f"| {name} | {count} |" for name, count in sorted(by_folder.items(), key=lambda item: item[0].casefold()))
    lines.extend(["", "## Paper Notes By Type", "", "| Type | Count |", "|---|---:|"])
    lines.extend(f"| {name} | {count} |" for name, count in sorted(paper_types.items()))
    lines.extend(["", "## Paper Notes By Status", "", "| Status | Count |", "|---|---:|"])
    lines.extend(f"| {name} | {count} |" for name, count in sorted(paper_status.items()))
    lines.extend(["", "## Dataset Notes By Availability", "", "| Availability | Count |", "|---|---:|"])
    lines.extend(f"| {name} | {count} |" for name, count in sorted(availability.items()))
    lines.extend([
        "",
        "## Definitions",
        "",
        "- Counts are computed from committed Markdown notes only.",
        "- The private paper-processing manifest and full-text workspace are not distributed, so no manifest count is reported.",
        "- A resolved link maps unambiguously to a note title, filename, path, or alias.",
        "- Dataset availability is inferred from explicit metadata first and folder placement second.",
        "",
    ])
    return "\n".join(lines)


NODE_FIELDS = ["node_id", "node_type", "title", "aliases", "status", "year", "paper_type", "availability", "paper_key", "doi", "url", "source_note"]
EDGE_FIELDS = ["source_id", "target_id", "target_title", "resolution", "relationship"]
DATASET_FIELDS = ["dataset_id", "title", "aliases", "availability", "availability_detail", "availability_group", "domain", "scope_screen", "scope_reason", "url", "access", "license_evidence", "data_sources", "introduced_by", "related_papers", "source_note"]
PAPER_FIELDS = ["paper_id", "title", "year", "paper_type", "venue", "authors", "doi", "arxiv", "url", "status", "datasets", "public_datasets", "manufacturing_dataset_candidates", "methods", "tasks", "domains", "metrics", "synthesis_candidate", "candidate_match_location", "synthesis_families", "source_note"]
CANDIDATE_FIELDS = PAPER_FIELDS + ["eligibility_status", "dataset_scope_status", "candidate_reason"]


def build_exports(root: Path) -> tuple[dict[str, str], str]:
    config = load_config(root)
    vault = root / config["paths"]["vault"]
    separator = config["export"]["list_separator"]
    snapshot_date = config["snapshot_date"]
    notes = iter_notes(vault)
    edges = resolve_edges(notes)
    datasets = _dataset_rows(notes, separator)
    papers, candidates = _paper_rows(notes, datasets, separator)
    nodes = _node_rows(notes, separator)
    edge_rows = [
        {
            "source_id": edge.source_id,
            "target_id": edge.target_id,
            "target_title": edge.target_title,
            "resolution": edge.resolution,
            "relationship": "wikilink",
        }
        for edge in edges
    ]
    public_datasets = [row for row in datasets if row["availability"] == "public"]
    manufacturing_datasets = [
        row
        for row in public_datasets
        if row["scope_screen"] == "manufacturing candidate"
    ]
    resolution = Counter(edge.resolution for edge in edges)
    summary = {
        "repository_schema_version": config["repository_schema_version"],
        "snapshot_date": snapshot_date,
        "vault_sha256": _vault_hash(notes),
        "counts": {
            "notes": len(notes),
            "papers": len(papers),
            "datasets": len(datasets),
            "public_datasets": len(public_datasets),
            "public_manufacturing_dataset_candidates": len(manufacturing_datasets),
            "synthesis_impact_candidates": len(candidates),
            "unique_wikilink_edges": len(edges),
            "resolved_edges": resolution.get("resolved", 0),
            "ambiguous_edges": resolution.get("ambiguous", 0),
            "unresolved_edges": resolution.get("unresolved", 0),
            "duplicate_titles": len(duplicate_titles(notes)),
        },
        "interpretation": {
            "synthesis_impact_candidates": "Automated pre-screen only; manual eligibility confirmation required.",
            "public_dataset": "Documented public access does not imply permission to redistribute dataset files.",
        },
    }
    files = {
        "nodes.csv": _csv_text(nodes, NODE_FIELDS),
        "edges.csv": _csv_text(edge_rows, EDGE_FIELDS),
        "dataset_registry.csv": _csv_text(datasets, DATASET_FIELDS),
        "public_dataset_registry.csv": _csv_text(public_datasets, DATASET_FIELDS),
        "manufacturing_dataset_candidates.csv": _csv_text(manufacturing_datasets, DATASET_FIELDS),
        "paper_evidence.csv": _csv_text(papers, PAPER_FIELDS),
        "synthesis_impact_candidates.csv": _csv_text(candidates, CANDIDATE_FIELDS),
        "summary.json": json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
    }
    stats = statistics_markdown(notes, snapshot_date)
    return files, stats


def export_repository(root: Path, *, check: bool = False) -> list[str]:
    root = root.resolve()
    config = load_config(root)
    output_dir = root / config["paths"]["exports"]
    stats_path = root / config["paths"]["vault"] / "Bases" / "Vault Statistics.md"
    files, stats = build_exports(root)
    differences: list[str] = []
    if check:
        if not stats_path.exists() or stats_path.read_text(encoding="utf-8") != stats:
            differences.append(str(stats_path.relative_to(root)))
        for name, content in files.items():
            path = output_dir / name
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                differences.append(str(path.relative_to(root)))
        return differences

    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(stats, encoding="utf-8")
    # Rebuild after updating the source statistics note so hashes match the snapshot.
    files, _ = build_exports(root)
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (output_dir / name).write_text(content, encoding="utf-8", newline="")
    return []
