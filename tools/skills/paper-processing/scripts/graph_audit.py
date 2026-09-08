#!/usr/bin/env python3
"""Audit Obsidian paper graph connectivity for this vault."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


ROOT = Path(
    os.environ.get("INSPECTION_EVIDENCE_ROOT") or next(
        parent for parent in Path(__file__).resolve().parents
        if (parent / "tools" / "config" / "repository.json").is_file()
    )
).resolve()
VAULT = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_VAULT",
        ROOT / "evidence" / "graph" / "vault",
    )
).resolve()


LINK_RE = re.compile(r"\[\[([^\]|#]+)")
MULTI_INDUSTRY_DOMAIN = "Multi-Industry Anomaly Detection"
DATASET_DOMAIN_KEYS = ("domain", "related_domain")
PLURAL_DATASET_DOMAIN_KEYS = ("domains", "related_domains")

EMERGING_FOLDERS = (
    "Concepts/Emerging Concepts",
    "Methods/Emerging Methods",
    "Metrics/Emerging Metrics",
    "Domains/Emerging Domains",
    "Learning Paradigms/Emerging Learning Paradigms",
)

def frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}

    data: dict[str, object] = {}
    current: str | None = None
    for raw in text[3:end].splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  - ") and current:
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(raw[4:].strip().strip('"'))
            continue
        if ":" not in raw or raw.startswith(" "):
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        current = key
        if value in {"", "[]"}:
            data[key] = [] if value == "[]" else ""
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [] if not inner else [v.strip().strip('"') for v in inner.split(",")]
        else:
            data[key] = value.strip('"')
    return data


def frontmatter_raw(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    return text[3:end]


def nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, list):
        return any(nonempty(v) for v in value)
    text = str(value).strip().lower()
    return bool(text and text not in {"[]", "not reported", "not applicable", "none"})


def links_in(path: Path) -> list[str]:
    return LINK_RE.findall(path.read_text(encoding="utf-8"))


def section_text(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    tail = text[match.end():]
    next_heading = re.search(r"^## ", tail, re.MULTILINE)
    return tail if not next_heading else tail[:next_heading.start()]


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


def graph_hub_value(text: str, name: str) -> bool:
    start = text.find("### Graph Hubs")
    if start == -1:
        return False
    tail = text[start:]
    next_section = tail.find("\n### ", len("### Graph Hubs"))
    block = tail if next_section == -1 else tail[:next_section]
    match = re.search(rf"^- {re.escape(name)}:\s*(.+)$", block, re.MULTILINE)
    return bool(match and match.group(1).strip() and match.group(1).strip() != "not reported")


def audit(strict: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    notes = sorted(VAULT.rglob("*.md"))
    note_names = {p.stem for p in notes}

    for path in notes:
        for target in links_in(path):
            if target not in note_names:
                errors.append(f"missing wikilink target [[{target}]] in {path.relative_to(ROOT)}")

    paper_paths = sorted((VAULT / "Papers").rglob("*.md")) if (VAULT / "Papers").exists() else []
    for path in paper_paths:
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        rel = path.relative_to(ROOT)

        if not nonempty(fm.get("tasks")):
            warnings.append(f"{rel}: no task links in frontmatter")
        if not any(nonempty(fm.get(k)) for k in ("methods", "model_family", "architectures")):
            warnings.append(f"{rel}: no method/model links in frontmatter")
        if not any(nonempty(fm.get(k)) for k in ("datasets", "domains")):
            warnings.append(f"{rel}: no dataset or domain links in frontmatter")
        if "Used performance metrics:" in text and not nonempty(fm.get("metrics")):
            warnings.append(f"{rel}: metrics discussed but no metric links in frontmatter")

        for hub in ("Tasks", "Methods", "Datasets", "Domains"):
            if not graph_hub_value(text, hub):
                warnings.append(f"{rel}: Graph Hubs missing {hub}")
        if nonempty(fm.get("metrics")) and not graph_hub_value(text, "Metrics"):
            warnings.append(f"{rel}: metrics frontmatter exists but Graph Hubs missing Metrics")

    dataset_paths = sorted((VAULT / "Datasets").rglob("*.md")) if (VAULT / "Datasets").exists() else []
    dataset_frontmatter_domains: dict[str, set[str]] = {}
    for path in dataset_paths:
        text = path.read_text(encoding="utf-8")
        raw_fm = frontmatter_raw(text)
        rel = path.relative_to(ROOT)
        singular_targets = dataset_domain_targets(raw_fm)
        plural_targets = plural_dataset_domain_targets(raw_fm)
        all_targets = singular_targets | plural_targets
        dataset_frontmatter_domains[path.stem] = all_targets

        if plural_targets:
            errors.append(
                f"{rel}: uses plural domain field(s); use one domain or related_domain value"
            )
        if len(all_targets) > 1:
            errors.append(
                f"{rel}: has multiple domain associations {sorted(all_targets)}; "
                f"use only [[{MULTI_INDUSTRY_DOMAIN}]] when more than one domain is supported"
            )
        if MULTI_INDUSTRY_DOMAIN in all_targets and len(all_targets) > 1:
            errors.append(
                f"{rel}: mixes [[{MULTI_INDUSTRY_DOMAIN}]] with narrower domains"
            )

    dataset_names = {path.stem for path in dataset_paths}
    dataset_to_domain_notes: dict[str, set[str]] = {}
    domain_paths = sorted((VAULT / "Domains").rglob("*.md")) if (VAULT / "Domains").exists() else []
    for path in domain_paths:
        text = path.read_text(encoding="utf-8")
        related_datasets = section_text(text, "Related Datasets")
        if not related_datasets:
            continue
        for target in LINK_RE.findall(related_datasets):
            if target in dataset_names:
                dataset_to_domain_notes.setdefault(target, set()).add(path.stem)

    for dataset, domains in sorted(dataset_to_domain_notes.items()):
        if len(domains) > 1:
            errors.append(
                f"dataset [[{dataset}]] appears in multiple domain Related Datasets sections "
                f"{sorted(domains)}; use one domain, or only [[{MULTI_INDUSTRY_DOMAIN}]] "
                "for multi-domain datasets"
            )

    for dataset, frontmatter_domains in sorted(dataset_frontmatter_domains.items()):
        reciprocal_domains = dataset_to_domain_notes.get(dataset, set())
        combined = frontmatter_domains | reciprocal_domains
        if len(combined) > 1:
            errors.append(
                f"dataset [[{dataset}]] has inconsistent frontmatter/reciprocal domains "
                f"{sorted(combined)}; keep exactly one domain association"
            )

    for folder_name in EMERGING_FOLDERS:
        folder = VAULT / folder_name
        if not folder.exists():
            continue
        index_name = folder.name
        index_path = folder / f"{index_name}.md"
        index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
        for path in sorted(folder.glob("*.md")):
            if path == index_path:
                continue
            text = path.read_text(encoding="utf-8")
            fm = frontmatter(text)
            rel = path.relative_to(ROOT)
            for key in ("status", "concept_type", "candidate_parent", "source_papers", "evidence_count"):
                if not nonempty(fm.get(key)):
                    warnings.append(f"{rel}: missing emerging frontmatter field {key}")
            if "## Used In These Papers" not in text:
                warnings.append(f"{rel}: missing Used In These Papers section")
            if "## Related Concepts" not in text:
                warnings.append(f"{rel}: missing Related Concepts section")
            if f"[[{path.stem}]]" not in index_text:
                warnings.append(f"{rel}: not linked from {index_path.relative_to(ROOT)}")
            if not links_in(path):
                warnings.append(f"{rel}: no wikilinks")

    print(f"markdown_files {len(notes)}")
    print(f"paper_notes {len(paper_paths)}")
    print(f"errors {len(errors)}")
    for item in errors:
        print(f"ERROR {item}")
    print(f"warnings {len(warnings)}")
    for item in warnings:
        print(f"WARN {item}")

    if errors or (strict and warnings):
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Obsidian paper graph connectivity.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero when warnings are present.")
    args = parser.parse_args()
    return audit(strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
