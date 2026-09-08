"""Read the repository's Obsidian-compatible Markdown evidence graph."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
WHOLE_WIKILINK_RE = re.compile(r"^\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]$")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
            return str(parsed)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def dewiki(value: Any) -> str:
    """Return the visible/canonical text of one whole-value wikilink."""

    text = _unquote(str(value or "")).strip()
    match = WHOLE_WIKILINK_RE.match(text)
    if match:
        return (match.group(2) or match.group(1)).strip()
    return text


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]") and not value.startswith("[["):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(part.strip()) for part in inner.split(",") if part.strip()]
    return _unquote(value)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse the top-level YAML subset used by the vault.

    Nested mappings and block scalars are intentionally left unexpanded; exports
    consume only top-level scalar and list fields.
    """

    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    body = text[body_start:]

    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(parse_scalar(line[4:]))
            continue
        if line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        parsed = parse_scalar(value)
        data[current_key] = [] if parsed == "" and value.strip() == "" else parsed
    return data, body


def as_strings(value: Any, *, dewikify: bool = True) -> list[str]:
    if value is None:
        return []
    values = value if isinstance(value, list) else [value]
    cleaned: list[str] = []
    for item in values:
        text = dewiki(item) if dewikify else str(item).strip()
        if text and text.lower() not in {"none", "null", "not reported", "not applicable"}:
            cleaned.append(text)
    return cleaned


def scalar(value: Any, *, dewikify: bool = True) -> str:
    values = as_strings(value, dewikify=dewikify)
    return values[0] if values else ""


@dataclass(frozen=True)
class Note:
    path: Path
    relative_path: str
    node_id: str
    node_type: str
    title: str
    metadata: dict[str, Any]
    body: str

    @property
    def aliases(self) -> list[str]:
        return as_strings(self.metadata.get("aliases"))


@dataclass(frozen=True)
class Edge:
    source_id: str
    target_id: str
    target_title: str
    resolution: str


def load_note(path: Path, vault: Path) -> Note:
    text = path.read_text(encoding="utf-8", errors="replace")
    metadata, body = split_frontmatter(text)
    relative = path.relative_to(vault).as_posix()
    node_id = relative[:-3] if relative.endswith(".md") else relative
    parts = Path(relative).parts
    node_type = parts[0] if len(parts) > 1 else "root"
    title = scalar(metadata.get("title")) or path.stem
    return Note(path, relative, node_id, node_type, title, metadata, body)


def iter_notes(vault: Path) -> list[Note]:
    notes = []
    for path in sorted(vault.rglob("*.md"), key=lambda item: item.as_posix().casefold()):
        relative_parts = path.relative_to(vault).parts
        if any(part.startswith(".") for part in relative_parts):
            continue
        notes.append(load_note(path, vault))
    return notes


def wikilink_targets(text: str) -> list[str]:
    return [match.strip() for match in WIKILINK_RE.findall(text) if match.strip()]


def _add_name(index: dict[str, set[str]], name: str, node_id: str) -> None:
    key = name.strip().removesuffix(".md").casefold()
    if key:
        index.setdefault(key, set()).add(node_id)


def _name_indices(notes: Iterable[Note]) -> tuple[dict[str, set[str]], ...]:
    """Build precedence-ordered indices matching Obsidian's filename-first behavior."""

    paths: dict[str, set[str]] = {}
    filenames: dict[str, set[str]] = {}
    titles: dict[str, set[str]] = {}
    aliases: dict[str, set[str]] = {}
    for note in notes:
        _add_name(paths, note.node_id, note.node_id)
        _add_name(filenames, Path(note.node_id).name, note.node_id)
        _add_name(titles, note.title, note.node_id)
        for alias in note.aliases:
            _add_name(aliases, alias, note.node_id)
    return paths, filenames, titles, aliases


def resolve_edges(notes: list[Note]) -> list[Edge]:
    indices = _name_indices(notes)
    rows: set[tuple[str, str, str, str]] = set()
    for note in notes:
        text = note.path.read_text(encoding="utf-8", errors="replace")
        for raw_target in wikilink_targets(text):
            target = raw_target.strip().removesuffix(".md")
            candidates: set[str] = set()
            for index in indices:
                candidates = index.get(target.casefold(), set())
                if candidates:
                    break
            if len(candidates) > 1:
                promoted = {
                    candidate
                    for candidate in candidates
                    if not any(
                        part.casefold().startswith("emerging ")
                        for part in Path(candidate).parts
                    )
                }
                if len(promoted) == 1:
                    candidates = promoted
            if len(candidates) == 1:
                target_id = next(iter(candidates))
                resolution = "resolved"
            elif candidates:
                target_id = ""
                resolution = "ambiguous"
            else:
                target_id = ""
                resolution = "unresolved"
            rows.add((note.node_id, target_id, Path(target).name, resolution))
    return [Edge(*row) for row in sorted(rows, key=lambda item: tuple(part.casefold() for part in item))]


def duplicate_titles(notes: list[Note]) -> dict[str, list[str]]:
    by_title: dict[str, list[str]] = {}
    for note in notes:
        by_title.setdefault(note.title.casefold(), []).append(note.node_id)
    return {
        title: sorted(paths)
        for title, paths in by_title.items()
        if len(paths) > 1
    }
