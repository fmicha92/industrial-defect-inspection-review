#!/usr/bin/env python3
"""Collect OpenAlex citation counts for all Table 1 dataset rows.

The dataset registry table uses two provenance citation slots in each dataset
name cell: the first citation is the data host/source and the second citation is
the introducing or source paper. This script extracts the second citation key
for every Table 1 row, resolves it in ``library.bib``, queries OpenAlex, and
writes all-domain CSV/JSON outputs.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DOMAIN_RE = re.compile(r"\\multicolumn\{7\}\{@\{\}l\}\{\\textit\{(.+?)\}\}")
CITE_RE = re.compile(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
ENTRY_RE = re.compile(r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,\s]+)\s*,", re.M)
FIELD_RE = re.compile(r"(?P<field>\w+)\s*=\s*(?P<value>\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)", re.S)


def normalize_text(value: str) -> str:
    """Collapse simple LaTeX markup into stable CSV-friendly text."""
    value = value.replace(r"\&", "&")
    value = value.replace(r"\_", "_")
    value = value.replace(r"\,", " ")
    value = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"[{}]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_rows(table_text: str) -> list[dict[str, str]]:
    """Extract all dataset rows from the longtable registry."""
    rows: list[dict[str, str]] = []
    current_domain: str | None = None
    for raw_line in table_text.splitlines():
        line = raw_line.strip()
        domain_match = DOMAIN_RE.search(line)
        if domain_match:
            current_domain = normalize_text(domain_match.group(1))
            continue
        if not current_domain or "&" not in line or not line.endswith(r"\\"):
            continue
        cells = [cell.strip() for cell in line[:-2].split("&")]
        if len(cells) < 7:
            continue
        cites: list[str] = []
        for cite_match in CITE_RE.finditer(cells[0]):
            cites.extend(key.strip() for key in cite_match.group(1).split(",") if key.strip())
        dataset = normalize_text(CITE_RE.sub("", cells[0]).replace("~", " "))
        rows.append(
            {
                "domain_group": current_domain,
                "dataset": dataset,
                "domain": normalize_text(cells[2]),
                "task": normalize_text(cells[3]),
                "citation_keys": cites,
                "paper_key": cites[1] if len(cites) > 1 else "",
            }
        )
    return rows


def field_value(value: str) -> str:
    value = value.strip().rstrip(",")
    if value.startswith("{") and value.endswith("}"):
        value = value[1:-1]
    elif value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    return normalize_text(value)


def parse_bibtex(path: Path) -> dict[str, dict[str, str]]:
    """Parse enough BibTeX for key, title, year, DOI, and URL lookup fields."""
    text = path.read_text(encoding="utf-8")
    matches = list(ENTRY_RE.finditer(text))
    entries: dict[str, dict[str, str]] = {}
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end].rsplit("}", 1)[0]
        entry = {"entry_type": match.group("type")}
        for field_match in FIELD_RE.finditer(body):
            entry[field_match.group("field").lower()] = field_value(field_match.group("value"))
        entries[match.group("key")] = entry
    return entries


def request_json(url: str, mailto: str | None = None) -> dict:
    if mailto:
        separator = "&" if "?" in url else "?"
        url = f"{url}{separator}mailto={urllib.parse.quote(mailto)}"
    request = urllib.request.Request(url, headers={"User-Agent": "dataset-citation-overview/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def title_score(expected: str, observed: str) -> float:
    """Return a conservative token-overlap score for title-search fallbacks."""
    expected_words = set(re.findall(r"[a-z0-9]+", expected.lower()))
    observed_words = set(re.findall(r"[a-z0-9]+", observed.lower()))
    if not expected_words or not observed_words:
        return 0.0
    return len(expected_words & observed_words) / len(expected_words | observed_words)


def openalex_work(
    entry: dict[str, str], mailto: str | None = None, delay: float = 0.1, min_title_score: float = 0.55
) -> tuple[dict | None, str]:
    """Find an OpenAlex work by DOI, falling back to guarded title search."""
    doi = entry.get("doi", "").strip()
    if doi:
        doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        encoded = urllib.parse.quote(f"https://doi.org/{doi}", safe="")
        try:
            time.sleep(delay)
            return request_json(f"https://api.openalex.org/works/{encoded}", mailto), "doi"
        except urllib.error.HTTPError as exc:
            if exc.code not in {404, 403}:
                raise
    title = entry.get("title", "")
    if not title:
        return None, "missing-title"
    params = urllib.parse.urlencode({"search": title, "per-page": 5})
    time.sleep(delay)
    results = request_json(f"https://api.openalex.org/works?{params}", mailto).get("results", [])
    if not results:
        return None, "title-not-found"
    best = max(results, key=lambda item: title_score(title, item.get("display_name", "")))
    if title_score(title, best.get("display_name", "")) < min_title_score:
        return None, "low-confidence-title-search"
    return best, "title-search"


def summarize(rows: list[dict]) -> list[dict[str, object]]:
    """Aggregate total OpenAlex citation counts by Table 1 domain group."""
    summaries: list[dict[str, object]] = []
    by_domain: dict[str, list[int]] = {}
    for row in rows:
        if row.get("openalex_id"):
            by_domain.setdefault(row["domain_group"], []).append(int(row.get("total_citations") or 0))
    for domain, counts in by_domain.items():
        summaries.append(
            {
                "domain_group": domain,
                "n_matched_papers": len(counts),
                "total_citations": sum(counts),
                "mean_citations": round(statistics.mean(counts), 2) if counts else 0,
                "median_citations": round(statistics.median(counts), 2) if counts else 0,
                "min_citations": min(counts) if counts else 0,
                "max_citations": max(counts) if counts else 0,
            }
        )
    return summaries


def year_counts(counts_by_year: list[dict], start_year: int, end_year: int) -> dict[int, int]:
    """Normalize OpenAlex per-year counts into a complete requested year span."""
    counts = {int(item.get("year")): int(item.get("cited_by_count", 0)) for item in counts_by_year if item.get("year")}
    return {year: counts.get(year, 0) for year in range(start_year, end_year + 1)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--table", default="evidence/review/publication/tables/dataset_registry.tex")
    parser.add_argument("--bib", default="evidence/review/publication/manuscript/library.bib")
    parser.add_argument("--output-dir", default="evidence/review/publication/data/citation_counts")
    parser.add_argument("--mailto", default="", help="Optional email for OpenAlex polite pool.")
    parser.add_argument("--delay", type=float, default=0.1)
    parser.add_argument("--start-year", type=int, default=2020)
    parser.add_argument("--end-year", type=int, default=2025)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    table_path = project_root / args.table
    bib_path = project_root / args.bib
    output_dir = project_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.start_year > args.end_year:
        print("--start-year must be less than or equal to --end-year.", file=sys.stderr)
        return 2

    table_rows = split_rows(table_path.read_text(encoding="utf-8"))
    if not table_rows:
        print("No Table 1 dataset rows found.", file=sys.stderr)
        return 2

    bib_entries = parse_bibtex(bib_path)
    enriched_rows: list[dict] = []
    long_rows: list[dict[str, object]] = []
    wide_rows: list[dict[str, object]] = []
    errors: list[str] = []

    for table_row in table_rows:
        paper_key = table_row["paper_key"]
        if not paper_key:
            errors.append(f"{table_row['dataset']}: no second citation key")
            continue
        bib_entry = bib_entries.get(paper_key)
        if not bib_entry:
            errors.append(f"{table_row['dataset']}: BibTeX key not found: {paper_key}")
            continue
        try:
            work, match_method = openalex_work(bib_entry, args.mailto or None, args.delay)
        except Exception as exc:
            errors.append(f"{table_row['dataset']} ({paper_key}): OpenAlex lookup failed: {exc}")
            work = None
            match_method = "lookup-error"
        if work is None:
            errors.append(f"{table_row['dataset']} ({paper_key}): no confident OpenAlex match ({match_method})")
        counts_by_year = sorted((work or {}).get("counts_by_year", []), key=lambda item: item.get("year", 0))
        selected_year_counts = year_counts(counts_by_year, args.start_year, args.end_year) if work else {}
        latest = max(counts_by_year, key=lambda item: item.get("year", 0), default={})
        row = {
            **table_row,
            "citation_keys": ";".join(table_row["citation_keys"]),
            "paper_key": paper_key,
            "bib_title": bib_entry.get("title", ""),
            "bib_year": bib_entry.get("year", ""),
            "doi": bib_entry.get("doi", ""),
            "openalex_id": (work or {}).get("id", ""),
            "openalex_title": (work or {}).get("display_name", ""),
            "openalex_year": (work or {}).get("publication_year", ""),
            "total_citations": (work or {}).get("cited_by_count", ""),
            "latest_year": latest.get("year", ""),
            "latest_year_citations": latest.get("cited_by_count", ""),
            "openalex_match_method": match_method,
        }
        enriched_rows.append(row)
        wide_row = {
            "domain_group": row["domain_group"],
            "dataset": row["dataset"],
            "domain": row["domain"],
            "task": row["task"],
            "paper_key": paper_key,
            "bib_title": row["bib_title"],
            "bib_year": row["bib_year"],
            "doi": row["doi"],
            "openalex_id": row["openalex_id"],
            "openalex_match_method": row["openalex_match_method"],
        }
        for year in range(args.start_year, args.end_year + 1):
            wide_row[str(year)] = selected_year_counts.get(year, "") if work else ""
        wide_rows.append(wide_row)
        for count in counts_by_year:
            year = int(count.get("year", 0))
            if year < args.start_year or year > args.end_year:
                continue
            long_rows.append(
                {
                    "domain_group": row["domain_group"],
                    "dataset": row["dataset"],
                    "paper_key": paper_key,
                    "year": count.get("year", ""),
                    "cited_by_count": count.get("cited_by_count", 0),
                }
            )

    stats_rows = summarize(enriched_rows)
    stem = "all_domains"
    json_path = output_dir / f"dataset_citations_{stem}.json"
    summary_path = output_dir / f"dataset_citation_summary_{stem}.csv"
    yearly_path = output_dir / f"dataset_citation_counts_by_year_{stem}.csv"
    wide_yearly_path = output_dir / f"dataset_citation_counts_wide_{args.start_year}_{args.end_year}_{stem}.csv"
    stats_path = output_dir / f"dataset_citation_domain_stats_{stem}.csv"

    json_path.write_text(
        json.dumps({"rows": enriched_rows, "domain_statistics": stats_rows, "errors": errors}, indent=2),
        encoding="utf-8",
    )
    if enriched_rows:
        with summary_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(enriched_rows[0].keys()))
            writer.writeheader()
            writer.writerows(enriched_rows)
    with yearly_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["domain_group", "dataset", "paper_key", "year", "cited_by_count"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(long_rows)
    if wide_rows:
        with wide_yearly_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(wide_rows[0].keys()))
            writer.writeheader()
            writer.writerows(wide_rows)
    if stats_rows:
        with stats_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(stats_rows[0].keys()))
            writer.writeheader()
            writer.writerows(stats_rows)

    print(f"Wrote {json_path}")
    print(f"Wrote {summary_path}")
    print(f"Wrote {yearly_path}")
    print(f"Wrote {wide_yearly_path}")
    print(f"Wrote {stats_path}")
    if errors:
        print("Warnings:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
