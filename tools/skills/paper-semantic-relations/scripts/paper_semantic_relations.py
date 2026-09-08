#!/usr/bin/env python3
"""Find vault-aware new paper candidates via OpenAlex.

The script reads Obsidian paper notes, builds a lightweight semantic profile for
a keyword, runs bounded OpenAlex searches through the local scholar-search
helper, and filters out papers already present in the vault.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(
    os.environ.get("INSPECTION_EVIDENCE_ROOT") or next(
        parent for parent in Path(__file__).resolve().parents
        if (parent / "tools" / "config" / "repository.json").is_file()
    )
).resolve()
OBSIDIAN_ROOT = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_VAULT",
        PROJECT_ROOT / "evidence" / "graph" / "vault",
    )
).resolve()
PAPERS_ROOT = OBSIDIAN_ROOT / "Papers"
SCHOLAR_SEARCH_CANDIDATES = (
    PROJECT_ROOT / "tools" / "vendor" / "agent-skills" / "scholar-search" / "scripts",
    PROJECT_ROOT / "tools" / "skills" / "scholar-search" / "scripts",
)
SCHOLAR_SEARCH_DIR = next(
    (path for path in SCHOLAR_SEARCH_CANDIDATES if path.is_dir()),
    SCHOLAR_SEARCH_CANDIDATES[0],
)
sys.path.insert(0, str(SCHOLAR_SEARCH_DIR))

try:
    import scholar_search
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(f"error: could not import scholar_search.py: {exc}") from exc

GRAPH_FIELDS = [
    "datasets",
    "tasks",
    "domains",
    "methods",
    "metrics",
    "model_family",
    "architectures",
    "baselines",
    "benchmarks",
    "related_concepts",
    "related_methods",
    "related_datasets",
    "related_tasks",
    "related_benchmarks",
]

RELATION_TERMS = {
    "dataset": ["dataset", "benchmark"],
    "method": ["method", "approach"],
    "task": ["task", "detection", "classification", "segmentation"],
    "domain": ["domain", "application"],
    "metric": ["metric", "evaluation"],
    "concept": ["concept"],
    "auto": [],
}


def norm_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def norm_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def title_words(value: str) -> set[str]:
    return {word for word in norm_text(value).split() if len(word) > 2}


def strip_year_prefix(value: str) -> str:
    return re.sub(r"^\s*(?:19|20)\d{2}\s*[-:]\s*", "", value).strip()


def clean_scalar(value: str) -> str:
    value = value.strip()
    if value in {"[]", "{}"}:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def dewiki(value: str) -> str:
    value = clean_scalar(value)
    match = re.fullmatch(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", value)
    if match:
        return (match.group(2) or match.group(1)).strip()
    return value


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    lines = text[4:end].splitlines()
    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(dewiki(raw[4:]))
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            parts = [p.strip() for p in value[1:-1].split(",") if p.strip()]
            data[key] = [dewiki(p) for p in parts]
        else:
            data[key] = dewiki(value)
    return data


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if str(v).strip()]
    value = str(value).strip()
    return [value] if value and value != "not reported" else []


def load_papers() -> list[dict[str, Any]]:
    papers: list[dict[str, Any]] = []
    for path in sorted(PAPERS_ROOT.rglob("*.md")):
        meta = parse_frontmatter(path)
        title = str(meta.get("title") or path.stem)
        aliases = listify(meta.get("aliases"))
        title_variants = [title, path.stem, strip_year_prefix(path.stem), *aliases]
        title_variants = [variant for variant in title_variants if variant and variant != "not reported"]
        papers.append({
            "path": str(path.relative_to(PROJECT_ROOT)),
            "title": title,
            "norm_title": norm_title(title),
            "title_variants": title_variants,
            "norm_title_variants": {norm_title(variant) for variant in title_variants if norm_title(variant)},
            "doi": clean_id(meta.get("doi")),
            "arxiv": clean_arxiv(meta.get("arxiv")),
            "openalex": clean_openalex(meta.get("openalex") or meta.get("openalex_id")),
            "meta": meta,
        })
    return papers


def clean_id(value: Any) -> str:
    if value is None:
        return ""
    value = str(value).strip().lower()
    if value in {"", "not reported", "none", "null"}:
        return ""
    return value.removeprefix("https://doi.org/").removeprefix("doi:")


def clean_arxiv(value: Any) -> str:
    value = clean_id(value)
    value = value.removeprefix("https://arxiv.org/abs/")
    value = value.removeprefix("arxiv:")
    return re.sub(r"v\d+$", "", value)


def clean_openalex(value: Any) -> str:
    value = clean_id(value)
    return value.removeprefix("https://openalex.org/")


def load_graph_notes() -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
    skip = {PAPERS_ROOT.resolve(), (OBSIDIAN_ROOT / ".obsidian").resolve()}
    for path in sorted(OBSIDIAN_ROOT.rglob("*.md")):
        if any(path.resolve().is_relative_to(s) for s in skip):
            continue
        meta = parse_frontmatter(path)
        aliases = listify(meta.get("aliases"))
        title = str(meta.get("title") or path.stem)
        notes.append({
            "path": str(path.relative_to(PROJECT_ROOT)),
            "title": title,
            "aliases": aliases,
            "folder": str(path.parent.relative_to(OBSIDIAN_ROOT)),
        })
    return notes


def match_score(keyword: str, values: list[str]) -> int:
    nk = norm_text(keyword)
    if not nk:
        return 0
    score = 0
    for value in values:
        nv = norm_text(value)
        if nv == nk:
            score = max(score, 4)
        elif nk in nv or nv in nk:
            score = max(score, 3)
        elif set(nk.split()) & set(nv.split()):
            score = max(score, 1)
    return score


def paper_matches_keyword(paper: dict[str, Any], keyword: str, graph_names: set[str]) -> bool:
    meta = paper["meta"]
    values = [paper["title"]]
    for field in GRAPH_FIELDS:
        values.extend(listify(meta.get(field)))
    names = {norm_text(v) for v in values}
    if any(norm_text(name) in names for name in graph_names):
        return True
    return match_score(keyword, values) >= 3


def build_profile(keyword: str, relation: str) -> dict[str, Any]:
    papers = load_papers()
    graph_notes = load_graph_notes()
    matches = []
    for note in graph_notes:
        score = match_score(keyword, [note["title"], *note["aliases"]])
        if score:
            matches.append({**note, "match_score": score})
    matches.sort(key=lambda n: (-n["match_score"], n["folder"], n["title"]))
    graph_names = {norm_text(n["title"]) for n in matches}
    linked = [p for p in papers if paper_matches_keyword(p, keyword, graph_names)]

    co: dict[str, Counter[str]] = {field: Counter() for field in GRAPH_FIELDS}
    for paper in linked:
        meta = paper["meta"]
        for field in GRAPH_FIELDS:
            for value in listify(meta.get(field)):
                if match_score(keyword, [value]) < 4:
                    co[field][value] += 1

    return {
        "keyword": keyword,
        "relation": relation,
        "matching_graph_notes": matches[:20],
        "existing_papers": [
            {
                "title": p["title"],
                "path": p["path"],
                "doi": p["doi"],
                "arxiv": p["arxiv"],
                "openalex": p["openalex"],
            }
            for p in linked
        ],
        "co_occurring_terms": {
            field: [{"term": term, "count": count} for term, count in counter.most_common(10)]
            for field, counter in co.items()
            if counter
        },
        "known_counts": {
            "papers_total": len(papers),
            "papers_linked_to_keyword": len(linked),
            "matching_graph_notes": len(matches),
        },
    }


def build_queries(profile: dict[str, Any], limit: int) -> list[str]:
    keyword = profile["keyword"]
    relation = profile["relation"]
    queries: list[str] = [keyword]
    for term in RELATION_TERMS.get(relation, []):
        queries.append(f"{keyword} {term}")
    for note in profile["matching_graph_notes"][:3]:
        if note["title"].lower() != keyword.lower():
            queries.append(note["title"])
        for alias in note.get("aliases", [])[:2]:
            queries.append(alias)
    priority_fields = ["tasks", "methods", "domains", "metrics", "datasets"]
    for field in priority_fields:
        for item in profile["co_occurring_terms"].get(field, [])[:2]:
            term = item["term"]
            if norm_text(term) != norm_text(keyword):
                queries.append(f"{keyword} {term}")
    deduped: list[str] = []
    seen: set[str] = set()
    for query in queries:
        key = norm_text(query)
        if key and key not in seen:
            seen.add(key)
            deduped.append(query)
    return deduped[:limit]


def result_existing_reason(result: dict[str, Any], papers: list[dict[str, Any]]) -> str:
    doi = clean_id(result.get("doi"))
    arxiv = clean_arxiv(result.get("arxiv_id"))
    openalex = clean_openalex(result.get("paper_id") or result.get("openalex_id"))
    raw_title = str(result.get("title") or "")
    title = norm_title(raw_title)
    title_word_set = title_words(raw_title)
    for paper in papers:
        if doi and paper["doi"] == doi:
            return f"doi match: {paper['path']}"
        if arxiv and paper["arxiv"] == arxiv:
            return f"arxiv match: {paper['path']}"
        if openalex and paper["openalex"] == openalex:
            return f"openalex match: {paper['path']}"
        if title and title in paper["norm_title_variants"]:
            return f"title match: {paper['path']}"
        for variant in paper["title_variants"]:
            variant_norm = norm_title(variant)
            if not title or not variant_norm:
                continue
            ratio = difflib.SequenceMatcher(None, title, variant_norm).ratio()
            if ratio >= 0.94:
                return f"fuzzy title match ({ratio:.2f}): {paper['path']}"
            variant_words = title_words(variant)
            if len(title_word_set) >= 6 and len(variant_words) >= 6:
                overlap = len(title_word_set & variant_words) / min(len(title_word_set), len(variant_words))
                if overlap >= 0.90:
                    return f"title word overlap ({overlap:.2f}): {paper['path']}"
    return ""


def relevance_score(result: dict[str, Any], keyword: str, profile: dict[str, Any]) -> tuple[int, list[str]]:
    haystack = " ".join([
        str(result.get("title") or ""),
        str(result.get("abstract") or ""),
        " ".join(result.get("concepts") or []),
    ])
    hay = norm_text(haystack)
    reasons: list[str] = []
    score = 0
    if norm_text(keyword) in hay:
        score += 5
        reasons.append("keyword appears in title/abstract/topics")
    relation = profile["relation"]
    for term in RELATION_TERMS.get(relation, []):
        if norm_text(term) in hay:
            score += 2
            reasons.append(f"relation term: {term}")
            break
    for field, items in profile["co_occurring_terms"].items():
        for item in items[:5]:
            term = item["term"]
            if norm_text(term) in hay and norm_text(term) != norm_text(keyword):
                score += 1
                reasons.append(f"vault co-term: {term}")
                break
    return score, reasons[:5]


def run_search(profile: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    papers = load_papers()
    queries = build_queries(profile, args.query_limit)
    seen_results: set[str] = set()
    candidates: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []

    filters = scholar_search.build_filters(
        args.year, args.venue, args.concepts, args.min_citations, args.open_access
    )
    for query in queries:
        url = scholar_search.build_search_url(query, args.limit, filters, scholar_search.DEFAULT_SELECT)
        status, payload = scholar_search._http_get_json(url)
        if status != 200 or payload is None:
            raise SystemExit(f"error: search failed for {query!r} (HTTP {status})")
        for raw in payload.get("results") or []:
            result = scholar_search.normalize_work(raw)
            key = (
                clean_openalex(result.get("paper_id"))
                or clean_id(result.get("doi"))
                or clean_arxiv(result.get("arxiv_id"))
                or norm_title(result.get("title") or "")
            )
            if not key or key in seen_results:
                continue
            seen_results.add(key)
            existing = result_existing_reason(result, papers)
            if existing:
                excluded.append({
                    "title": result.get("title"),
                    "year": result.get("year"),
                    "reason": existing,
                    "query": query,
                })
                continue
            score, reasons = relevance_score(result, profile["keyword"], profile)
            if score < args.min_score:
                continue
            candidates.append({
                "score": score,
                "why": reasons,
                "query": query,
                **result,
            })

    candidates.sort(key=lambda r: (-(r.get("score") or 0), -(r.get("citation_count") or 0), -(r.get("year") or 0)))
    return {
        "profile": profile,
        "queries": queries,
        "candidate_count": len(candidates),
        "candidates": candidates[: args.max_candidates],
        "excluded_existing_count": len(excluded),
        "excluded_existing": excluded[:50],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Find new papers related to vault semantics.")
    sub = parser.add_subparsers(dest="command", required=True)

    profile_parser = sub.add_parser("profile", help="Show vault context for a keyword.")
    profile_parser.add_argument("keyword")
    profile_parser.add_argument("--relation", choices=sorted(RELATION_TERMS), default="auto")

    search_parser = sub.add_parser("search", help="Search OpenAlex and exclude existing vault papers.")
    search_parser.add_argument("keyword")
    search_parser.add_argument("--relation", choices=sorted(RELATION_TERMS), default="auto")
    search_parser.add_argument("--limit", type=int, default=25, help="OpenAlex results per query.")
    search_parser.add_argument("--query-limit", type=int, default=8, help="Max expanded queries.")
    search_parser.add_argument("--max-candidates", type=int, default=40)
    search_parser.add_argument("--min-score", type=int, default=3)
    search_parser.add_argument("--year", default="2020-", help="Year range, e.g. 2022-2026, 2024, or 2020- (default 2020-).")
    search_parser.add_argument("--venue")
    search_parser.add_argument("--concepts")
    search_parser.add_argument("--min-citations", type=int, default=25, help="Minimum cited-by count (default 25).")
    search_parser.add_argument("--open-access", action="store_true")

    args = parser.parse_args()
    profile = build_profile(args.keyword, args.relation)
    if args.command == "profile":
        print(json.dumps(profile, indent=2, ensure_ascii=False))
        return 0
    print(json.dumps(run_search(profile, args), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
