#!/usr/bin/env python3
"""Manage paper intake outside the public Obsidian vault.

The script scans workspace/paper-inbox/00_incoming/, records stable identifiers
in workspace/paper-inbox/90_processing/manifest.json, and keeps processed
status when a known paper appears in the inbox again later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def find_project_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (
            (candidate / "tools" / "config" / "repository.json").is_file()
            or (
                (candidate / "tools" / "skills").is_dir()
                and (candidate / "evidence" / "graph" / "vault").is_dir()
            )
        ):
            return candidate
    return Path.cwd().resolve()


PROJECT_ROOT = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_ROOT",
        find_project_root(Path(__file__).resolve()),
    )
).resolve()
VAULT_DIR = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_VAULT",
        PROJECT_ROOT / "evidence" / "graph" / "vault",
    )
).resolve()
DEFAULT_INBOX_DIR = Path(
    os.environ.get(
        "INSPECTION_EVIDENCE_INBOX",
        PROJECT_ROOT / "workspace" / "paper-inbox",
    )
).resolve()
DEFAULT_INPUT_DIR = DEFAULT_INBOX_DIR / "00_incoming"
DEFAULT_PROCESSED_DIR = DEFAULT_INBOX_DIR / "10_processed"
DEFAULT_DUPLICATE_DIR = DEFAULT_INBOX_DIR / "20_duplicates"
DEFAULT_FAILED_DIR = DEFAULT_INBOX_DIR / "30_failed"
DEFAULT_PROCESSING_DIR = DEFAULT_INBOX_DIR / "90_processing"
DEFAULT_MANIFEST = DEFAULT_PROCESSING_DIR / "manifest.json"
DEFAULT_TEXT_DIR = DEFAULT_PROCESSING_DIR / "text"
DEFAULT_ANALYSIS_DIR = DEFAULT_PROCESSING_DIR / "analysis-inputs"
DEFAULT_SUFFIXES = (".pdf", ".md", ".txt", ".bib", ".ris", ".json")
DEFAULT_ARCHIVE_NAMES = {"10_processed", "20_duplicates", "30_failed", "90_processing"}
PROCESSED_TYPE_DIRS = {
    "research": "Research",
    "dataset": "Dataset",
    "review": "Review",
    "benchmark": "Benchmark",
    "systems": "Systems",
    "system": "Systems",
    "other": "Other",
}
MANIFEST_VERSION = 1
MAX_FILENAME_STEM_LENGTH = 150
MAX_AUTHOR_STEM_LENGTH = 48
MIN_TITLE_STEM_LENGTH = 24

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
ARXIV_RE = re.compile(
    r"(?:arxiv[:\s]*)?(\d{4}\.\d{4,5})(?:v\d+)?",
    re.IGNORECASE,
)
OPENALEX_RE = re.compile(r"\bW\d{7,}\b", re.IGNORECASE)
REFERENCE_HEADING_RE = re.compile(
    r"(?im)^\s*(references|bibliography|works cited|acknowledg(e)?ments|appendix|supplementary material)\s*$"
)
SECTION_HEADING_RE = re.compile(r"(?m)^\s*(\d+(\.\d+)*\s+)?[A-Z][A-Za-z0-9 ,:;()/\-]{2,80}\s*$")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def relpath(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "version": MANIFEST_VERSION,
            "updated_at": None,
            "papers": {},
            "file_index": {},
        }
    with path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    manifest.setdefault("version", MANIFEST_VERSION)
    manifest.setdefault("updated_at", None)
    manifest.setdefault("papers", {})
    manifest.setdefault("file_index", {})
    return manifest


def save_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    manifest["updated_at"] = utc_now()
    with path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sample_text(path: Path, max_bytes: int = 2 * 1024 * 1024) -> str:
    with path.open("rb") as handle:
        data = handle.read(max_bytes)
    return data.decode("utf-8", errors="ignore")


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def estimate_tokens(text: str) -> int:
    # A practical planning estimate for English technical prose.
    return max(1, round(len(text) / 4))


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return slug[:120] or "paper"


def safe_filename_part(value: str) -> str:
    part = re.sub(r"[\\/:*?\"<>|]+", " ", value)
    part = re.sub(r"\s+", " ", part).strip(" .")
    return part or "not reported"


def truncate_filename_part(value: str, max_length: int) -> tuple[str, bool]:
    if len(value) <= max_length:
        return value, False
    if max_length <= 3:
        return value[:max_length].rstrip(" .-"), True
    return value[: max_length - 3].rstrip(" .-") + "...", True


def path_from_record(path_value: str) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def normalized_paper_type(value: str | None) -> str:
    if not value:
        return "Other"
    key = str(value).strip().lower()
    return PROCESSED_TYPE_DIRS.get(key, "Other")


def paper_type_from_note_path(path_value: str | None) -> str | None:
    if not path_value:
        return None
    parts = Path(path_value).parts
    for index, part in enumerate(parts[:-1]):
        if part == "Papers":
            if Path(parts[index + 1]).suffix:
                return None
            return normalized_paper_type(parts[index + 1])
    return None


def normalized_match_value(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def current_note_type_for_paper(paper: dict[str, Any]) -> str | None:
    metadata = paper.get("metadata", {})
    candidates = [
        str(metadata.get("title") or ""),
        str(paper.get("canonical_filename") or ""),
    ]
    wanted = {normalized_match_value(value) for value in candidates if value}
    if not wanted:
        return None

    papers_root = VAULT_DIR / "Papers"
    if not papers_root.exists():
        return None
    for note in papers_root.glob("*/*.md"):
        note_key = normalized_match_value(note.stem)
        if any(key and (key in note_key or note_key in key) for key in wanted):
            return paper_type_from_note_path(relpath(note))
    return None


def inferred_paper_type(paper: dict[str, Any], explicit_type: str | None = None) -> str:
    if explicit_type:
        return normalized_paper_type(explicit_type)

    for output in paper.get("processed_outputs", []):
        paper_type = paper_type_from_note_path(str(output))
        if paper_type:
            return paper_type

    paper_type = current_note_type_for_paper(paper)
    if paper_type:
        return paper_type

    metadata = paper.get("metadata", {})
    for field in ("paper_type", "type"):
        paper_type = normalized_paper_type(metadata.get(field))
        if paper_type != "Other":
            return paper_type

    return "Other"


def clean_doi(raw: str) -> str:
    return raw.strip().rstrip(".,;)]}>").lower()


def extract_identifiers(path: Path) -> dict[str, str]:
    haystack = f"{path.name}\n{sample_text(path)}"
    identifiers: dict[str, str] = {}

    doi_match = DOI_RE.search(haystack)
    if doi_match:
        identifiers["doi"] = clean_doi(doi_match.group(0))

    arxiv_match = ARXIV_RE.search(haystack)
    if arxiv_match:
        identifiers["arxiv"] = arxiv_match.group(1).lower()

    openalex_match = OPENALEX_RE.search(haystack)
    if openalex_match:
        identifiers["openalex"] = openalex_match.group(0).upper()

    return identifiers


def identifier_keys(identifiers: dict[str, str], sha256: str | None = None) -> list[str]:
    keys: list[str] = []
    for name in ("doi", "arxiv", "openalex"):
        value = identifiers.get(name)
        if value:
            keys.append(f"{name}:{value}")
    if sha256:
        keys.append(f"sha256:{sha256}")
    return keys


def build_indexes(manifest: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    identifier_index: dict[str, str] = {}
    file_index: dict[str, str] = dict(manifest.get("file_index", {}))

    for canonical_key, paper in manifest.get("papers", {}).items():
        for key in identifier_keys(paper.get("identifiers", {})):
            identifier_index[key] = canonical_key
        for item in paper.get("files", []):
            sha = item.get("sha256")
            if sha:
                file_index[f"sha256:{sha}"] = canonical_key
            path = item.get("path")
            if path:
                file_index[f"path:{path}"] = canonical_key

    return identifier_index, file_index


def find_input_files(input_dir: Path, suffixes: tuple[str, ...]) -> list[Path]:
    if not input_dir.exists():
        return []
    files: list[Path] = []
    for path in input_dir.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(input_dir).parts
        if any(part.startswith(".") for part in relative_parts):
            continue
        if relative_parts and relative_parts[0] in DEFAULT_ARCHIVE_NAMES:
            continue
        if path.suffix.lower() in suffixes:
            files.append(path)
    return sorted(files)


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def unique_destination(path: Path) -> Path:
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 2
    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def canonical_filename_stem(metadata: dict[str, Any], fallback: str) -> tuple[str, list[str]]:
    warnings: list[str] = []
    year = str(metadata.get("year") or "").strip()
    author = str(metadata.get("author") or metadata.get("first_author") or "").strip()
    title = str(metadata.get("title") or "").strip()

    if year and author and title:
        year_part, year_truncated = truncate_filename_part(safe_filename_part(year), 12)
        author_part, author_truncated = truncate_filename_part(
            safe_filename_part(author),
            MAX_AUTHOR_STEM_LENGTH,
        )
        title_budget = MAX_FILENAME_STEM_LENGTH - len(year_part) - len(author_part) - len(" - ") * 2
        if title_budget < MIN_TITLE_STEM_LENGTH:
            author_budget = max(12, MAX_FILENAME_STEM_LENGTH - len(year_part) - MIN_TITLE_STEM_LENGTH - len(" - ") * 2)
            author_part, author_truncated = truncate_filename_part(safe_filename_part(author), author_budget)
            title_budget = MAX_FILENAME_STEM_LENGTH - len(year_part) - len(author_part) - len(" - ") * 2
        title_part, title_truncated = truncate_filename_part(safe_filename_part(title), title_budget)
        stem = " - ".join((year_part, author_part, title_part))
        if len(stem) > MAX_FILENAME_STEM_LENGTH:
            stem, stem_truncated = truncate_filename_part(stem, MAX_FILENAME_STEM_LENGTH)
            title_truncated = title_truncated or stem_truncated
        if year_truncated or author_truncated or title_truncated:
            warnings.append(
                f"Canonical filename was truncated to stay under {MAX_FILENAME_STEM_LENGTH} characters."
            )
        return stem, warnings

    missing = [name for name, value in (("year", year), ("author", author), ("title", title)) if not value]
    warnings.append(
        "Missing metadata for canonical filename: "
        + ", ".join(missing)
        + ". Used paper key fallback instead of inventing values."
    )
    stem, truncated = truncate_filename_part(safe_filename_part(fallback.replace(":", " ")), MAX_FILENAME_STEM_LENGTH)
    if truncated:
        warnings.append(
            f"Fallback filename was truncated to stay under {MAX_FILENAME_STEM_LENGTH} characters."
        )
    return stem, warnings


def move_file_record_to_archive(
    manifest: dict[str, Any],
    paper_key: str,
    file_record: dict[str, Any],
    archive_dir: Path,
    archive_status: str,
    now: str,
    destination_stem: str | None = None,
) -> dict[str, str] | None:
    old_path_value = file_record.get("path")
    if not old_path_value:
        return None

    source = path_from_record(old_path_value)
    if not source.exists() or not source.is_file():
        return None

    archive_dir.mkdir(parents=True, exist_ok=True)
    destination_name = f"{destination_stem}{source.suffix}" if destination_stem else source.name
    destination = unique_destination(archive_dir / destination_name)
    shutil.move(str(source), str(destination))

    new_path = relpath(destination)
    file_record.setdefault("original_path", old_path_value)
    file_record["path"] = new_path
    file_record["archived_at"] = now
    file_record["archive_status"] = archive_status
    file_record["last_seen"] = now

    manifest.setdefault("file_index", {})[f"path:{new_path}"] = paper_key
    manifest["file_index"].pop(f"path:{old_path_value}", None)
    sha = file_record.get("sha256")
    if sha:
        manifest["file_index"][f"sha256:{sha}"] = paper_key

    return {"from": old_path_value, "to": new_path, "archive_status": archive_status}


def archive_inbox_files(
    manifest: dict[str, Any],
    paper_key: str,
    input_dir: Path,
    archive_dir: Path,
    archive_status: str,
    now: str,
    destination_stem: str | None = None,
) -> list[dict[str, str]]:
    paper = manifest["papers"][paper_key]
    moves: list[dict[str, str]] = []
    for file_record in paper.get("files", []):
        path_value = file_record.get("path")
        if not path_value:
            continue
        source = path_from_record(path_value)
        if not source.exists() or not source.is_file():
            continue
        if not is_under(source, input_dir):
            continue
        if source.parent.resolve() == archive_dir.resolve():
            continue
        if source.resolve().relative_to(input_dir.resolve()).parts[0] in DEFAULT_ARCHIVE_NAMES:
            continue
        moved = move_file_record_to_archive(
            manifest,
            paper_key,
            file_record,
            archive_dir,
            archive_status,
            now,
            destination_stem,
        )
        if moved:
            moves.append(moved)
    return moves


def resolve_key(
    manifest: dict[str, Any],
    identifiers: dict[str, str],
    sha256: str | None = None,
    path: str | None = None,
) -> str | None:
    identifier_index, file_index = build_indexes(manifest)

    for key in identifier_keys(identifiers, sha256):
        if key in identifier_index:
            return identifier_index[key]
        if key in file_index:
            return file_index[key]
    if path and f"path:{path}" in file_index:
        return file_index[f"path:{path}"]
    return None


def canonical_key_for(identifiers: dict[str, str], sha256: str) -> str:
    keys = identifier_keys(identifiers, sha256)
    return keys[0]


def merge_file_record(files: list[dict[str, Any]], path: str, sha256: str, now: str) -> bool:
    for item in files:
        if item.get("sha256") == sha256 and item.get("path") != path and item.get("archive_status"):
            continue
        if item.get("sha256") == sha256 or item.get("path") == path:
            item["path"] = path
            item["sha256"] = sha256
            item["last_seen"] = now
            item["seen_count"] = int(item.get("seen_count", 0)) + 1
            return False

    files.append(
        {
            "path": path,
            "sha256": sha256,
            "first_seen": now,
            "last_seen": now,
            "seen_count": 1,
        }
    )
    return True


def scan(args: argparse.Namespace) -> int:
    input_dir = Path(args.input_dir).resolve()
    duplicate_dir = Path(args.duplicate_dir).resolve()
    manifest_path = Path(args.manifest).resolve()
    suffixes = tuple(s.lower() if s.startswith(".") else f".{s.lower()}" for s in args.suffix)
    manifest = load_manifest(manifest_path)
    now = utc_now()

    summary = {
        "input_dir": relpath(input_dir),
        "manifest": relpath(manifest_path),
        "scanned": 0,
        "new_papers": 0,
        "known_papers": 0,
        "known_processed": 0,
        "new_file_instances": 0,
        "exact_repeats": 0,
        "archived_duplicates": 0,
        "duplicate_archive_dir": relpath(duplicate_dir),
    }

    papers = manifest.setdefault("papers", {})
    manifest.setdefault("file_index", {})

    for path in find_input_files(input_dir, suffixes):
        summary["scanned"] += 1
        relative = relpath(path)
        sha = sha256_file(path)
        identifiers = extract_identifiers(path)
        key = resolve_key(manifest, identifiers, sha, relative)

        if key is None:
            key = canonical_key_for(identifiers, sha)
            papers[key] = {
                "canonical_key": key,
                "status": "queued",
                "first_seen": now,
                "last_seen": now,
                "seen_count": 0,
                "identifiers": {},
                "files": [],
                "processed_outputs": [],
            }
            summary["new_papers"] += 1
        else:
            summary["known_papers"] += 1

        paper = papers[key]
        paper["last_seen"] = now
        paper["seen_count"] = int(paper.get("seen_count", 0)) + 1
        paper.setdefault("identifiers", {}).update(identifiers)
        paper.setdefault("files", [])
        paper.setdefault("processed_outputs", [])

        new_instance = merge_file_record(paper["files"], relative, sha, now)
        if new_instance:
            summary["new_file_instances"] += 1
        else:
            summary["exact_repeats"] += 1

        if paper.get("status") == "processed":
            summary["known_processed"] += 1

        for index_key in identifier_keys(paper.get("identifiers", {}), sha):
            manifest["file_index"][index_key] = key
        manifest["file_index"][f"path:{relative}"] = key

        if args.archive_duplicates and paper.get("status") == "processed":
            for file_record in paper["files"]:
                if file_record.get("path") != relative:
                    continue
                moved = move_file_record_to_archive(
                    manifest,
                    key,
                    file_record,
                    duplicate_dir,
                    "duplicate",
                    now,
                )
                if moved:
                    summary["archived_duplicates"] += 1
                break

    save_manifest(manifest_path, manifest)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def status(args: argparse.Namespace) -> int:
    manifest = load_manifest(Path(args.manifest).resolve())
    counts: dict[str, int] = {}
    preprocessing_counts: dict[str, int] = {}
    for paper in manifest.get("papers", {}).values():
        state = paper.get("status", "unknown")
        counts[state] = counts.get(state, 0) + 1
        preprocessing_state = paper.get("preprocessing", {}).get("status", "not_started")
        preprocessing_counts[preprocessing_state] = preprocessing_counts.get(preprocessing_state, 0) + 1
    payload = {
        "manifest": relpath(Path(args.manifest).resolve()),
        "updated_at": manifest.get("updated_at"),
        "paper_count": len(manifest.get("papers", {})),
        "preprocessing_counts": preprocessing_counts,
        "status_counts": counts,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def list_papers(args: argparse.Namespace) -> int:
    manifest = load_manifest(Path(args.manifest).resolve())
    rows = []
    for key, paper in sorted(manifest.get("papers", {}).items()):
        if args.status and paper.get("status") != args.status:
            continue
        rows.append(
            {
                "key": key,
                "status": paper.get("status", "unknown"),
                "first_seen": paper.get("first_seen"),
                "last_seen": paper.get("last_seen"),
                "seen_count": paper.get("seen_count", 0),
                "identifiers": paper.get("identifiers", {}),
                "metadata": paper.get("metadata", {}),
                "canonical_filename": paper.get("canonical_filename"),
                "files": [item.get("path") for item in paper.get("files", [])],
                "preprocessing": paper.get("preprocessing", {}),
                "processed_outputs": paper.get("processed_outputs", []),
            }
        )

    if args.json:
        print(json.dumps(rows, indent=2, sort_keys=True))
        return 0

    if not rows:
        print("No papers matched.")
        return 0

    for row in rows:
        identifiers = ", ".join(f"{k}={v}" for k, v in row["identifiers"].items()) or "no external id"
        preprocessing_state = row["preprocessing"].get("status", "not_started")
        print(
            f"{row['key']}  [{row['status']}]  preprocess={preprocessing_state}  "
            f"seen={row['seen_count']}  {identifiers}"
        )
    return 0


def rename_path(path_value: str, destination_stem: str) -> dict[str, str] | None:
    source = path_from_record(path_value)
    if not source.exists() or not source.is_file():
        return None
    destination = unique_destination(source.with_name(f"{destination_stem}{source.suffix}"))
    if destination == source:
        return None
    source.rename(destination)
    return {"from": path_value, "to": relpath(destination)}


def replace_output_path(outputs: list[Any], old_path: str, new_path: str) -> None:
    for index, output in enumerate(outputs):
        if output == old_path:
            outputs[index] = new_path


def rename_preprocessing_artifacts(paper: dict[str, Any], destination_stem: str) -> list[dict[str, str]]:
    preprocessing = paper.get("preprocessing", {})
    outputs = paper.setdefault("processed_outputs", [])
    renamed: list[dict[str, str]] = []

    for field in ("full_text", "analysis_input"):
        old_path = preprocessing.get(field)
        if not old_path:
            continue
        moved = rename_path(old_path, destination_stem)
        if not moved:
            continue
        preprocessing[field] = moved["to"]
        replace_output_path(outputs, moved["from"], moved["to"])
        moved["artifact"] = field
        renamed.append(moved)

    return renamed


def mark_processed(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = load_manifest(manifest_path)
    input_dir = Path(args.input_dir).resolve()
    processed_dir = Path(args.processed_dir).resolve()

    key = args.paper_key
    if key not in manifest.get("papers", {}):
        found = resolve_key(manifest, identifiers_from_key(key))
        if found:
            key = found

    papers = manifest.get("papers", {})
    if key not in papers:
        print(f"Paper key not found: {args.paper_key}", file=sys.stderr)
        return 2

    paper = papers[key]
    metadata = paper.setdefault("metadata", {})
    for field in ("year", "author", "title"):
        value = getattr(args, field)
        if value:
            metadata[field] = value
    destination_stem, naming_warnings = canonical_filename_stem(metadata, key)

    paper["status"] = "processed"
    paper["processed_at"] = utc_now()
    paper["canonical_filename"] = destination_stem
    outputs = paper.setdefault("processed_outputs", [])
    for output in args.output:
        outputs.append(relpath(Path(output)))
    if args.note:
        outputs.append(args.note)
    paper_type = inferred_paper_type(paper, args.paper_type)
    metadata["paper_type"] = paper_type.lower()
    archive_dir = processed_dir / paper_type

    archived_sources: list[dict[str, str]] = []
    if not args.no_archive:
        archived_sources = archive_inbox_files(
            manifest,
            key,
            input_dir,
            archive_dir,
            "processed",
            paper["processed_at"],
            destination_stem,
        )

    renamed_artifacts = rename_preprocessing_artifacts(paper, destination_stem)

    save_manifest(manifest_path, manifest)
    print(
        json.dumps(
            {
                "paper_key": key,
                "status": "processed",
                "paper_type": paper_type,
                "canonical_filename": destination_stem,
                "processed_archive_dir": relpath(archive_dir),
                "archived_sources": archived_sources,
                "renamed_artifacts": renamed_artifacts,
                "warnings": naming_warnings,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def organize_processed(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    processed_dir = Path(args.processed_dir).resolve()
    manifest = load_manifest(manifest_path)
    now = utc_now()
    moves: list[dict[str, str]] = []

    for key, paper in sorted(manifest.get("papers", {}).items()):
        if paper.get("status") != "processed":
            continue
        paper_type = inferred_paper_type(paper)
        paper.setdefault("metadata", {})["paper_type"] = paper_type.lower()
        target_dir = processed_dir / paper_type
        for file_record in paper.get("files", []):
            path_value = file_record.get("path")
            if not path_value:
                continue
            source = path_from_record(path_value)
            if not source.exists() or not source.is_file():
                continue
            if not is_under(source, processed_dir):
                continue
            if source.parent.resolve() == target_dir.resolve():
                continue
            if args.dry_run:
                moves.append(
                    {
                        "from": path_value,
                        "to": relpath(target_dir / source.name),
                        "archive_status": "processed",
                        "paper_type": paper_type,
                    }
                )
                continue
            moved = move_file_record_to_archive(
                manifest,
                key,
                file_record,
                target_dir,
                "processed",
                now,
            )
            if moved:
                moved["paper_type"] = paper_type
                moves.append(moved)

    if not args.dry_run:
        save_manifest(manifest_path, manifest)

    payload = {
        "processed_dir": relpath(processed_dir),
        "moved_count": len(moves),
        "moves": moves,
        "dry_run": args.dry_run,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def identifiers_from_key(key: str) -> dict[str, str]:
    if ":" not in key:
        return {}
    name, value = key.split(":", 1)
    if name in {"doi", "arxiv", "openalex"}:
        return {name: value}
    return {}


def resolve_manifest_key(manifest: dict[str, Any], paper_key: str) -> str | None:
    if paper_key in manifest.get("papers", {}):
        return paper_key
    return resolve_key(manifest, identifiers_from_key(paper_key))


def first_existing_source_file(paper: dict[str, Any]) -> Path | None:
    for item in paper.get("files", []):
        path_value = item.get("path")
        if not path_value:
            continue
        path = path_from_record(path_value)
        if path.exists() and path.is_file():
            return path
    return None


def extract_pdf_text(path: Path) -> tuple[str, str]:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("PDF extraction requires pdftotext, but it is not installed.")

    command = [pdftotext, "-enc", "UTF-8", "-nopgbrk", str(path), "-"]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        message = result.stderr.strip() or "pdftotext failed without an error message."
        raise RuntimeError(message)
    return result.stdout, "pdftotext"


def extract_source_text(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf_text(path)
    if suffix in {".md", ".txt", ".bib", ".ris", ".json"}:
        return read_text_file(path), "text"
    raise RuntimeError(f"Unsupported source file type: {suffix}")


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\x0c", "\n\n")
    text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def strip_low_value_tail(text: str) -> tuple[str, str | None]:
    match = REFERENCE_HEADING_RE.search(text)
    if not match:
        return text, None
    trimmed = text[: match.start()].rstrip() + "\n"
    return trimmed, match.group(1).lower()


def section_outline(text: str, limit: int = 30) -> list[str]:
    headings: list[str] = []
    for match in SECTION_HEADING_RE.finditer(text):
        heading = " ".join(match.group(0).split())
        lower = heading.lower()
        if len(heading) < 4 or lower in {"abstract", "keywords"}:
            continue
        if heading not in headings:
            headings.append(heading)
        if len(headings) >= limit:
            break
    return headings


def build_analysis_input(
    paper_key: str,
    paper: dict[str, Any],
    source_file: Path,
    full_text: str,
) -> tuple[str, dict[str, Any]]:
    analysis_text, removed_tail = strip_low_value_tail(full_text)
    full_tokens = estimate_tokens(full_text)
    analysis_tokens = estimate_tokens(analysis_text)
    savings = max(0, full_tokens - analysis_tokens)
    savings_percent = round((savings / full_tokens) * 100, 1) if full_tokens else 0.0

    identifiers = paper.get("identifiers", {})
    metadata = {
        "paper_key": paper_key,
        "source_file": relpath(source_file),
        "identifiers": identifiers,
        "full_text_tokens_est": full_tokens,
        "analysis_input_tokens_est": analysis_tokens,
        "token_savings_vs_full_text_est": savings,
        "token_savings_percent_est": savings_percent,
        "removed_tail_from_heading": removed_tail,
        "section_outline": section_outline(analysis_text),
    }

    frontmatter = [
        "---",
        f"paper_key: {json.dumps(paper_key)}",
        f"source_file: {json.dumps(relpath(source_file))}",
        f"full_text_tokens_est: {full_tokens}",
        f"analysis_input_tokens_est: {analysis_tokens}",
        f"token_savings_percent_est: {savings_percent}",
        "---",
        "",
        "# Codex Analysis Input",
        "",
        "## Metadata",
        "",
        "```json",
        json.dumps(metadata, indent=2, sort_keys=True),
        "```",
        "",
        "## Text",
        "",
        analysis_text.rstrip(),
        "",
    ]
    return "\n".join(frontmatter), metadata


def preprocess_one(
    manifest: dict[str, Any],
    paper_key: str,
    text_dir: Path,
    analysis_dir: Path,
    force: bool,
) -> dict[str, Any]:
    paper = manifest["papers"][paper_key]
    existing = paper.get("preprocessing", {})
    if existing.get("status") == "ready" and not force:
        return {
            "paper_key": paper_key,
            "status": "skipped",
            "reason": "already preprocessed",
            "analysis_input": existing.get("analysis_input"),
        }

    source_file = first_existing_source_file(paper)
    if not source_file:
        paper["preprocessing"] = {
            "status": "failed",
            "failed_at": utc_now(),
            "error": "No source file exists for this paper.",
        }
        return {"paper_key": paper_key, "status": "failed", "error": paper["preprocessing"]["error"]}

    raw_text, extractor = extract_source_text(source_file)
    full_text = clean_text(raw_text)
    slug = safe_slug(paper_key)
    text_path = text_dir / f"{slug}.txt"
    analysis_path = analysis_dir / f"{slug}.md"

    text_dir.mkdir(parents=True, exist_ok=True)
    analysis_dir.mkdir(parents=True, exist_ok=True)
    text_path.write_text(full_text, encoding="utf-8")
    analysis_input, metadata = build_analysis_input(paper_key, paper, source_file, full_text)
    analysis_path.write_text(analysis_input, encoding="utf-8")

    paper["preprocessing"] = {
        "status": "ready",
        "extracted_at": utc_now(),
        "extractor": extractor,
        "source_file": relpath(source_file),
        "full_text": relpath(text_path),
        "analysis_input": relpath(analysis_path),
        **{key: value for key, value in metadata.items() if key.endswith("_est") or key.endswith("_percent_est")},
        "removed_tail_from_heading": metadata["removed_tail_from_heading"],
    }
    if paper.get("status") == "queued":
        paper["status"] = "preprocessed"

    outputs = paper.setdefault("processed_outputs", [])
    for output_path in (relpath(text_path), relpath(analysis_path)):
        if output_path not in outputs:
            outputs.append(output_path)

    return {
        "paper_key": paper_key,
        "status": "ready",
        "source_file": relpath(source_file),
        "full_text": relpath(text_path),
        "analysis_input": relpath(analysis_path),
        "full_text_tokens_est": metadata["full_text_tokens_est"],
        "analysis_input_tokens_est": metadata["analysis_input_tokens_est"],
        "token_savings_percent_est": metadata["token_savings_percent_est"],
    }


def preprocess(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = load_manifest(manifest_path)
    text_dir = Path(args.text_dir).resolve()
    analysis_dir = Path(args.analysis_dir).resolve()
    input_dir = Path(args.input_dir).resolve()
    failed_dir = Path(args.failed_dir).resolve()
    papers = manifest.get("papers", {})

    if args.paper_key:
        resolved = resolve_manifest_key(manifest, args.paper_key)
        if not resolved:
            print(f"Paper key not found: {args.paper_key}", file=sys.stderr)
            return 2
        keys = [resolved]
    else:
        keys = [
            key
            for key, paper in sorted(papers.items())
            if args.all or paper.get("status") in {"queued", "preprocessed", "processing"}
        ]

    results: list[dict[str, Any]] = []
    for key in keys:
        try:
            result = preprocess_one(manifest, key, text_dir, analysis_dir, args.force)
            if result.get("status") == "failed" and args.archive_failed:
                result["archived_sources"] = archive_inbox_files(
                    manifest,
                    key,
                    input_dir,
                    failed_dir,
                    "failed",
                    papers[key].get("preprocessing", {}).get("failed_at", utc_now()),
                )
            results.append(result)
        except Exception as exc:  # noqa: BLE001 - reports per-paper extraction failures.
            failed_at = utc_now()
            papers[key]["preprocessing"] = {
                "status": "failed",
                "failed_at": failed_at,
                "error": str(exc),
            }
            result = {"paper_key": key, "status": "failed", "error": str(exc)}
            if args.archive_failed:
                result["archived_sources"] = archive_inbox_files(
                    manifest,
                    key,
                    input_dir,
                    failed_dir,
                    "failed",
                    failed_at,
                )
            results.append(result)

    save_manifest(manifest_path, manifest)
    print(json.dumps({"processed": len(results), "results": results}, indent=2, sort_keys=True))
    return 0


def check_file(args: argparse.Namespace) -> int:
    manifest = load_manifest(Path(args.manifest).resolve())
    path = Path(args.file).resolve()
    relative = relpath(path)
    sha = sha256_file(path)
    identifiers = extract_identifiers(path)
    key = resolve_key(manifest, identifiers, sha, relative)
    payload: dict[str, Any] = {
        "file": relative,
        "sha256": sha,
        "identifiers": identifiers,
        "known": key is not None,
        "paper_key": key,
    }
    if key:
        payload["status"] = manifest.get("papers", {}).get(key, {}).get("status", "unknown")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        default=str(DEFAULT_MANIFEST),
        help="Manifest path. Defaults to workspace/paper-inbox/90_processing/manifest.json.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan workspace/paper-inbox/00_incoming and update the manifest.",
    )
    scan_parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    scan_parser.add_argument("--duplicate-dir", default=str(DEFAULT_DUPLICATE_DIR))
    scan_parser.add_argument(
        "--no-archive-duplicates",
        action="store_false",
        dest="archive_duplicates",
        help="Leave re-added already-processed source files in the inbox.",
    )
    scan_parser.add_argument("--suffix", action="append", default=list(DEFAULT_SUFFIXES))
    scan_parser.set_defaults(archive_duplicates=True)
    scan_parser.set_defaults(func=scan)

    status_parser = subparsers.add_parser("status", help="Show manifest status counts.")
    status_parser.set_defaults(func=status)

    list_parser = subparsers.add_parser("list", help="List known papers.")
    list_parser.add_argument(
        "--status",
        choices=("queued", "preprocessed", "processing", "processed", "skipped"),
    )
    list_parser.add_argument("--json", action="store_true")
    list_parser.set_defaults(func=list_papers)

    preprocess_parser = subparsers.add_parser(
        "preprocess",
        help="Extract text and create compact Codex analysis inputs.",
    )
    preprocess_parser.add_argument("paper_key", nargs="?", help="Paper key to preprocess.")
    preprocess_parser.add_argument(
        "--all",
        action="store_true",
        help="Preprocess every known paper instead of queued/preprocessing papers only.",
    )
    preprocess_parser.add_argument("--force", action="store_true", help="Rebuild existing artifacts.")
    preprocess_parser.add_argument("--text-dir", default=str(DEFAULT_TEXT_DIR))
    preprocess_parser.add_argument("--analysis-dir", default=str(DEFAULT_ANALYSIS_DIR))
    preprocess_parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    preprocess_parser.add_argument("--failed-dir", default=str(DEFAULT_FAILED_DIR))
    preprocess_parser.add_argument(
        "--no-archive-failed",
        action="store_false",
        dest="archive_failed",
        help="Leave source files in place when preprocessing fails.",
    )
    preprocess_parser.set_defaults(archive_failed=True)
    preprocess_parser.set_defaults(func=preprocess)

    mark_parser = subparsers.add_parser("mark-processed", help="Mark a known paper as processed.")
    mark_parser.add_argument("paper_key")
    mark_parser.add_argument("--note", help="Obsidian note path or other note reference.")
    mark_parser.add_argument("--output", action="append", default=[], help="Produced output path.")
    mark_parser.add_argument("--year", help="Publication year from the paper/source metadata.")
    mark_parser.add_argument("--author", help="First author or canonical author label from the paper.")
    mark_parser.add_argument("--title", help="Paper title from the paper/source metadata.")
    mark_parser.add_argument(
        "--paper-type",
        choices=("research", "dataset", "review", "benchmark", "systems", "other"),
        help="Paper type for archiving under workspace/paper-inbox/10_processed/<Type>/. Inferred from --note when omitted.",
    )
    mark_parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    mark_parser.add_argument("--processed-dir", default=str(DEFAULT_PROCESSED_DIR))
    mark_parser.add_argument(
        "--no-archive",
        action="store_true",
        help="Mark processed without moving source files into workspace/paper-inbox/10_processed/.",
    )
    mark_parser.set_defaults(func=mark_processed)

    organize_parser = subparsers.add_parser(
        "organize-processed",
        help="Move existing processed source files into workspace/paper-inbox/10_processed/<Type>/ subfolders.",
    )
    organize_parser.add_argument("--processed-dir", default=str(DEFAULT_PROCESSED_DIR))
    organize_parser.add_argument("--dry-run", action="store_true")
    organize_parser.set_defaults(func=organize_processed)

    check_parser = subparsers.add_parser("check-file", help="Check whether a file is already known.")
    check_parser.add_argument("file")
    check_parser.set_defaults(func=check_file)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
