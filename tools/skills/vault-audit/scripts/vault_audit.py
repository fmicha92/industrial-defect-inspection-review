#!/usr/bin/env python3
"""Audit broad Obsidian vault structure for this project."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(
    os.environ.get("INSPECTION_EVIDENCE_ROOT") or next(
        parent for parent in Path(__file__).resolve().parents
        if (parent / "tools" / "config" / "repository.json").is_file()
    )
).resolve()
sys.path.insert(0, str(ROOT / "tools" / "src"))

from inspection_evidence.exporter import export_repository  # noqa: E402

VAULT = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_VAULT",
        ROOT / "evidence" / "graph" / "vault",
    )
).resolve()
LINK_RE = re.compile(r"\[\[([^\]|#]+)")
EMBED_RE = re.compile(r"!\[\[([^\]|#]+)")
STATS_NOTE = VAULT / "Bases" / "Vault Statistics.md"
MANIFEST = ROOT / "workspace" / "paper-inbox" / "90_processing" / "manifest.json"
MULTI_INDUSTRY_DOMAIN = "Multi-Industry Anomaly Detection"
DATASET_DOMAIN_KEYS = ("domain", "related_domain")
PLURAL_DATASET_DOMAIN_KEYS = ("domains", "related_domains")

EXPECTED_TOP_LEVEL = {
    ".obsidian",
    "Bases",
    "Benchmarks",
    "Canvases",
    "Concepts",
    "Datasets",
    "Domains",
    "Learning Paradigms",
    "Methods",
    "Metrics",
    "Papers",
    "Tasks",
}

EMERGING_FOLDERS = {
    "Concepts/Emerging Concepts",
    "Methods/Emerging Methods",
    "Metrics/Emerging Metrics",
    "Domains/Emerging Domains",
    "Learning Paradigms/Emerging Learning Paradigms",
}

LEGACY_EMERGING_FOLDERS = {
    "Emerging Concepts",
    "Emerging Methods",
    "Emerging Metrics",
    "Emerging Domains",
    "Emerging Learning Paradigms",
}


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    path: str
    message: str


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def links_in(path: Path) -> set[str]:
    return set(LINK_RE.findall(path.read_text(encoding="utf-8")))


def frontmatter_raw(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    return text[3:end]


def values_for_yaml_key(raw: str, key: str) -> list[str]:
    values: list[str] = []
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith(" ") and line.split(":", 1)[0].strip() == key and ":" in line:
            value = line.split(":", 1)[1].strip()
            if value:
                values.append(value)
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                values.append(lines[i][4:].strip())
                i += 1
            continue
        i += 1
    return values


def clean_yaml_scalar(value: str) -> str:
    value = value.strip().strip(",")
    if value in {"", "[]"}:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1].strip()
    return value


def frontmatter_scalar(raw: str, key: str) -> str:
    values = values_for_yaml_key(raw, key)
    return clean_yaml_scalar(values[0]) if values else ""


def markdown_files(include_virtual: Path | None = None) -> list[Path]:
    files = sorted(VAULT.rglob("*.md")) if VAULT.exists() else []
    if include_virtual and include_virtual not in files:
        files.append(include_virtual)
    return sorted(files)


def top_level_for(path: Path) -> str:
    try:
        rel_path = path.relative_to(VAULT)
    except ValueError:
        return "outside-vault"
    return rel_path.parts[0] if rel_path.parts else "."


def manifest_processed_count() -> int:
    if not MANIFEST.exists():
        return 0
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    papers = data.get("papers", {})
    return sum(1 for paper in papers.values() if paper.get("status") == "processed")


def collect_stats(include_virtual_note: bool = False) -> dict[str, object]:
    files = markdown_files(STATS_NOTE if include_virtual_note else None)
    note_names = {path.stem for path in files}
    duplicate_note_names = sum(count > 1 for count in Counter(path.stem for path in files).values())

    link_occurrences: list[tuple[Path, str]] = []
    embed_count = 0
    notes_with_outlinks: set[Path] = set()
    incoming_counts: Counter[str] = Counter()

    for path in files:
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        targets = LINK_RE.findall(text)
        embeds = EMBED_RE.findall(text)
        embed_count += len(embeds)
        if targets:
            notes_with_outlinks.add(path)
        for target in targets:
            link_occurrences.append((path, target))
            incoming_counts[target] += 1

    unique_targets = {target for _, target in link_occurrences}
    unique_wikilinks = {(path.relative_to(VAULT).as_posix(), target) for path, target in link_occurrences}
    resolved_targets = unique_targets & note_names
    unresolved_targets = unique_targets - note_names
    orphan_notes = [
        path
        for path in files
        if path.stem not in incoming_counts and top_level_for(path) != "Bases"
    ]

    paper_paths = sorted((VAULT / "Papers").rglob("*.md")) if (VAULT / "Papers").exists() else []
    paper_type_counts: Counter[str] = Counter()
    paper_status_counts: Counter[str] = Counter()
    processed_paper_notes = 0
    for path in paper_paths:
        raw_fm = frontmatter_raw(path.read_text(encoding="utf-8"))
        paper_type = frontmatter_scalar(raw_fm, "paper_type") or path.parent.name.lower()
        status = frontmatter_scalar(raw_fm, "status") or "not reported"
        paper_type_counts[paper_type] += 1
        paper_status_counts[status] += 1
        if status == "processed":
            processed_paper_notes += 1

    dataset_root = VAULT / "Datasets"
    dataset_availability_counts: Counter[str] = Counter()
    if dataset_root.exists():
        for path in sorted(dataset_root.rglob("*.md")):
            if path.parent == dataset_root:
                dataset_availability_counts["root"] += 1
            else:
                dataset_availability_counts[path.parent.name] += 1

    return {
        "generated_at": now_utc(),
        "vault": rel(VAULT),
        "total_vault_notes": len(files),
        "total_paper_notes": len(paper_paths),
        "total_papers_processed": processed_paper_notes,
        "total_papers_processed_in_manifest": manifest_processed_count(),
        "total_links": len(link_occurrences),
        "total_unique_wikilinks": len(unique_wikilinks),
        "total_unique_links": len(unique_targets),
        "resolved_unique_links": len(resolved_targets),
        "unresolved_unique_links": len(unresolved_targets),
        "total_embeds": embed_count,
        "notes_with_outgoing_links": len(notes_with_outlinks),
        "orphan_notes_excluding_bases": len(orphan_notes),
        "duplicate_note_names": duplicate_note_names,
        "notes_by_top_level": dict(sorted(Counter(top_level_for(path) for path in files).items())),
        "paper_notes_by_type": dict(sorted(paper_type_counts.items())),
        "paper_notes_by_status": dict(sorted(paper_status_counts.items())),
        "dataset_notes_by_availability": dict(sorted(dataset_availability_counts.items())),
    }


def markdown_table(rows: dict[str, int]) -> str:
    if not rows:
        return "| Item | Count |\n|---|---|\n"
    lines = ["| Item | Count |", "|---|---:|"]
    lines.extend(f"| {key} | {value} |" for key, value in rows.items())
    return "\n".join(lines) + "\n"


def format_stats_markdown(stats: dict[str, object]) -> str:
    core_rows = {
        "Total papers processed": stats["total_papers_processed"],
        "Total paper notes": stats["total_paper_notes"],
        "Manifest processed papers": stats["total_papers_processed_in_manifest"],
        "Total vault notes": stats["total_vault_notes"],
        "Total wikilinks": stats["total_links"],
        "Total unique wikilinks": stats["total_unique_wikilinks"],
        "Total unique wikilink targets": stats["total_unique_links"],
        "Resolved unique targets": stats["resolved_unique_links"],
        "Unresolved unique targets": stats["unresolved_unique_links"],
        "Total embeds": stats["total_embeds"],
        "Notes with outgoing links": stats["notes_with_outgoing_links"],
        "Orphan notes excluding Bases": stats["orphan_notes_excluding_bases"],
        "Duplicate note names": stats["duplicate_note_names"],
    }

    return "\n".join(
        [
            "---",
            "title: Vault Statistics",
            "tags:",
            "  - vault/statistics",
            f"updated_at: {stats['generated_at']}",
            "source_script: tools/skills/vault-audit/scripts/vault_audit.py",
            "---",
            "",
            "# Vault Statistics",
            "",
            f"Updated: {stats['generated_at']}",
            "",
            "## Core Counts",
            "",
            markdown_table(core_rows).rstrip(),
            "",
            "## Notes By Top-Level Folder",
            "",
            markdown_table(stats["notes_by_top_level"]).rstrip(),
            "",
            "## Paper Notes By Type",
            "",
            markdown_table(stats["paper_notes_by_type"]).rstrip(),
            "",
            "## Paper Notes By Status",
            "",
            markdown_table(stats["paper_notes_by_status"]).rstrip(),
            "",
            "## Dataset Notes By Availability",
            "",
            markdown_table(stats["dataset_notes_by_availability"]).rstrip(),
            "",
            "## Definitions",
            "",
            "- Total papers processed counts paper notes under `evidence/graph/vault/Papers/` whose frontmatter `status` is `processed`.",
            "- Manifest processed papers counts records in the optional local `workspace/paper-inbox/90_processing/manifest.json` whose status is `processed`.",
            "- Total wikilinks counts every Obsidian wikilink occurrence in vault markdown files.",
            "- Total unique wikilinks deduplicates repeated links from the same source note to the same target.",
            "- Total unique wikilink targets deduplicates link targets by note name, ignoring aliases, headings, and block IDs.",
            "- Unresolved unique targets are wikilink targets that do not match any current markdown note basename.",
            "",
        ]
    )


def write_stats_note(stats: dict[str, object]) -> Path:
    STATS_NOTE.parent.mkdir(parents=True, exist_ok=True)
    STATS_NOTE.write_text(format_stats_markdown(stats), encoding="utf-8")
    return STATS_NOTE


def print_stats_text(stats: dict[str, object]) -> None:
    print(f"vault {stats['vault']}")
    for key in (
        "total_papers_processed",
        "total_paper_notes",
        "total_papers_processed_in_manifest",
        "total_vault_notes",
        "total_links",
        "total_unique_wikilinks",
        "total_unique_links",
        "resolved_unique_links",
        "unresolved_unique_links",
        "total_embeds",
        "notes_with_outgoing_links",
        "orphan_notes_excluding_bases",
        "duplicate_note_names",
    ):
        print(f"{key} {stats[key]}")


def link_targets_from_values(values: list[str]) -> set[str]:
    targets: set[str] = set()
    for value in values:
        links = LINK_RE.findall(value)
        if links:
            targets.update(links)
            continue
        if value.startswith("[") and value.endswith("]"):
            parts = [part.strip() for part in value[1:-1].split(",")]
        else:
            parts = [value]
        for part in parts:
            scalar = clean_yaml_scalar(part)
            if scalar and scalar.lower() not in {"not reported", "not applicable", "none"}:
                targets.add(scalar)
    return targets


def dataset_domain_targets(raw_frontmatter: str) -> set[str]:
    values: list[str] = []
    for key in DATASET_DOMAIN_KEYS:
        values.extend(values_for_yaml_key(raw_frontmatter, key))
    return link_targets_from_values(values)


def plural_dataset_domain_targets(raw_frontmatter: str) -> set[str]:
    values: list[str] = []
    for key in PLURAL_DATASET_DOMAIN_KEYS:
        values.extend(values_for_yaml_key(raw_frontmatter, key))
    return link_targets_from_values(values)


def section_text(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    tail = text[match.end():]
    next_heading = re.search(r"^## ", tail, re.MULTILINE)
    return tail if not next_heading else tail[:next_heading.start()]


def audit_taxonomy() -> list[Finding]:
    findings: list[Finding] = []

    if not VAULT.exists():
        return [
            Finding(
                level="error",
                check="vault_exists",
                path=rel(VAULT),
                message="vault folder is missing",
            )
        ]

    top_level = {path.name for path in VAULT.iterdir() if path.is_dir()}
    for name in sorted(top_level - EXPECTED_TOP_LEVEL):
        findings.append(
            Finding(
                level="warn",
                check="unexpected_top_level_folder",
                path=rel(VAULT / name),
                message="top-level folder is outside the expected project taxonomy",
            )
        )

    for folder in sorted(LEGACY_EMERGING_FOLDERS):
        path = VAULT / folder
        if path.exists():
            findings.append(
                Finding(
                    level="error",
                    check="legacy_emerging_folder",
                    path=rel(path),
                    message="legacy top-level emerging folder should be moved under its parent taxonomy folder",
                )
            )

    for folder in sorted(EMERGING_FOLDERS):
        path = VAULT / folder
        if not path.exists():
            findings.append(
                Finding(
                    level="error",
                    check="missing_emerging_folder",
                    path=rel(path),
                    message="parent-scoped emerging folder is missing",
                )
            )
            continue

        index_path = path / f"{path.name}.md"
        if not index_path.exists():
            findings.append(
                Finding(
                    level="warn",
                    check="missing_emerging_index",
                    path=rel(index_path),
                    message="emerging folder should have a same-name index note",
                )
            )
            continue

        index_links = links_in(index_path)
        for child in sorted(path.glob("*.md")):
            if child == index_path:
                continue
            if child.stem not in index_links:
                findings.append(
                    Finding(
                        level="warn",
                        check="emerging_index_missing_child",
                        path=rel(child),
                        message=f"{rel(index_path)} does not link to [[{child.stem}]]",
                    )
                )

    return findings


def audit_dataset_domains() -> list[Finding]:
    findings: list[Finding] = []
    dataset_paths = sorted((VAULT / "Datasets").rglob("*.md")) if (VAULT / "Datasets").exists() else []
    dataset_frontmatter_domains: dict[str, set[str]] = {}

    for path in dataset_paths:
        raw_fm = frontmatter_raw(path.read_text(encoding="utf-8"))
        singular_targets = dataset_domain_targets(raw_fm)
        plural_targets = plural_dataset_domain_targets(raw_fm)
        all_targets = singular_targets | plural_targets
        dataset_frontmatter_domains[path.stem] = all_targets

        if plural_targets:
            findings.append(
                Finding(
                    level="error",
                    check="dataset_plural_domain_field",
                    path=rel(path),
                    message="dataset note uses plural domain field(s); use one domain or related_domain value",
                )
            )
        if len(all_targets) > 1:
            findings.append(
                Finding(
                    level="error",
                    check="dataset_multiple_domains",
                    path=rel(path),
                    message=(
                        f"dataset has multiple domain associations {sorted(all_targets)}; "
                        f"use only [[{MULTI_INDUSTRY_DOMAIN}]] when more than one domain is supported"
                    ),
                )
            )

    dataset_names = {path.stem for path in dataset_paths}
    dataset_to_domain_notes: dict[str, set[str]] = {}
    domain_paths = sorted((VAULT / "Domains").rglob("*.md")) if (VAULT / "Domains").exists() else []
    for path in domain_paths:
        related_datasets = section_text(path.read_text(encoding="utf-8"), "Related Datasets")
        if not related_datasets:
            continue
        for target in LINK_RE.findall(related_datasets):
            if target in dataset_names:
                dataset_to_domain_notes.setdefault(target, set()).add(path.stem)

    for dataset, domains in sorted(dataset_to_domain_notes.items()):
        if len(domains) > 1:
            findings.append(
                Finding(
                    level="error",
                    check="dataset_in_multiple_domain_notes",
                    path=f"evidence/graph/vault/Domains/*/Related Datasets",
                    message=(
                        f"[[{dataset}]] appears under multiple domain notes {sorted(domains)}; "
                        f"use one domain, or only [[{MULTI_INDUSTRY_DOMAIN}]] for multi-domain datasets"
                    ),
                )
            )

    for dataset, frontmatter_domains in sorted(dataset_frontmatter_domains.items()):
        reciprocal_domains = dataset_to_domain_notes.get(dataset, set())
        combined = frontmatter_domains | reciprocal_domains
        if len(combined) > 1:
            findings.append(
                Finding(
                    level="error",
                    check="dataset_domain_mismatch",
                    path=f"evidence/graph/vault/Datasets/**/{dataset}.md",
                    message=(
                        f"frontmatter and reciprocal domain notes disagree {sorted(combined)}; "
                        "keep exactly one domain association"
                    ),
                )
            )

    return findings


def audit_all() -> list[Finding]:
    return audit_taxonomy() + audit_dataset_domains()


def run_check(check: str) -> list[Finding]:
    if check == "taxonomy":
        return audit_taxonomy()
    if check == "dataset-domains":
        return audit_dataset_domains()
    return audit_all()


def print_text(findings: list[Finding]) -> None:
    errors = [finding for finding in findings if finding.level == "error"]
    warnings = [finding for finding in findings if finding.level == "warn"]

    print(f"vault {rel(VAULT)}")
    print(f"taxonomy_errors {len(errors)}")
    for finding in errors:
        print(f"ERROR {finding.check} {finding.path}: {finding.message}")
    print(f"taxonomy_warnings {len(warnings)}")
    for finding in warnings:
        print(f"WARN {finding.check} {finding.path}: {finding.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit broad Obsidian vault structure.")
    parser.add_argument(
        "--check",
        choices=("all", "taxonomy", "dataset-domains", "stats"),
        default="all",
        help="Audit code path to run.",
    )
    parser.add_argument("--json", action="store_true", help="Print findings as JSON.")
    parser.add_argument(
        "--write-stats",
        action="store_true",
        help=f"Refresh {rel(STATS_NOTE)} with current vault statistics.",
    )
    args = parser.parse_args()

    if args.check == "stats":
        stats = collect_stats(include_virtual_note=args.write_stats)
        if args.write_stats:
            export_repository(ROOT)
            stats = collect_stats()
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            print_stats_text(stats)
            if args.write_stats:
                print(f"wrote {rel(STATS_NOTE)}")
        return 0

    findings = run_check(args.check)
    if args.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        print_text(findings)

    return 1 if any(finding.level == "error" for finding in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
