#!/usr/bin/env python3
"""Inventory publicly shared Google Drive folders without downloading their contents."""

from __future__ import annotations

import argparse
import codecs
import json
import re
import urllib.request
from collections.abc import Iterator


FOLDER_MIME = "application/vnd.google-apps.folder"
IVD_PATTERN = re.compile(r"window\['_DRIVE_ivd'\]\s*=\s*'(.*?)';", re.DOTALL)


def fetch_children(folder_id: str) -> list[dict[str, str]]:
    url = f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response:
        html = response.read().decode("utf-8", errors="replace")
    match = IVD_PATTERN.search(html)
    if not match:
        raise RuntimeError(f"No public folder inventory found for {folder_id}")
    escaped = match.group(1).replace(r"\/", "/")
    decoded = codecs.decode(escaped, "unicode_escape")
    data = json.loads(decoded)
    entries: dict[str, dict[str, str]] = {}
    for value in walk(data):
        if not isinstance(value, list) or len(value) < 4:
            continue
        file_id, parents, name, mime = value[:4]
        if not (
            isinstance(file_id, str)
            and isinstance(parents, list)
            and folder_id in parents
            and isinstance(name, str)
            and isinstance(mime, str)
        ):
            continue
        entries[file_id] = {"id": file_id, "name": name, "mime": mime}
    return sorted(entries.values(), key=lambda item: (item["mime"] != FOLDER_MIME, item["name"]))


def walk(value: object) -> Iterator[object]:
    yield value
    if isinstance(value, list):
        for item in value:
            yield from walk(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk(item)


def inventory(folder_id: str, recursive: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pending = [(folder_id, "")]
    visited: set[str] = set()
    while pending:
        current_id, prefix = pending.pop(0)
        if current_id in visited:
            continue
        visited.add(current_id)
        for item in fetch_children(current_id):
            path = f"{prefix}/{item['name']}".lstrip("/")
            row = {**item, "path": path}
            rows.append(row)
            if recursive and item["mime"] == FOLDER_MIME:
                pending.append((item["id"], path))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_id")
    parser.add_argument("--recursive", action="store_true")
    args = parser.parse_args()
    print(json.dumps(inventory(args.folder_id, args.recursive), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
