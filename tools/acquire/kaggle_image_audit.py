#!/usr/bin/env python3
"""Audit image dimensions through Kaggle's anonymous per-file API."""

from __future__ import annotations

import argparse
import io
import json
import sys
import time
import urllib.error
import urllib.request
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath

from PIL import Image

from kaggle_dataset_inventory import inventory


DOWNLOAD_API = "https://api.kaggle.com/v1/datasets.DatasetApiService/DownloadDataset"
IMAGE_SUFFIXES = {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}


def image_size(dataset_ref: str, file_name: str) -> tuple[int, int]:
    owner, slug = dataset_ref.split("/", 1)
    body = json.dumps(
        {"ownerSlug": owner, "datasetSlug": slug, "fileName": file_name}
    ).encode()
    request = urllib.request.Request(
        DOWNLOAD_API, data=body, headers={"Content-Type": "application/json"}
    )
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                content = response.read()
            if content.startswith(b"PK"):
                archive = zipfile.ZipFile(io.BytesIO(content))
                content = archive.read(archive.namelist()[0])
            with Image.open(io.BytesIO(content)) as image:
                return image.size
        except (OSError, urllib.error.URLError, zipfile.BadZipFile):
            if attempt == 1:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_ref", help="Kaggle reference in owner/slug form")
    parser.add_argument("--contains", help="Only audit paths containing this text")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    files = [
        item["name"]
        for item in inventory(args.dataset_ref)
        if PurePosixPath(str(item["name"])).suffix.lower() in IMAGE_SUFFIXES
        and (not args.contains or args.contains in str(item["name"]))
    ]
    dimensions: Counter[str] = Counter()
    by_parent: dict[str, Counter[str]] = defaultdict(Counter)
    errors: dict[str, str] = {}

    def render() -> str:
        result = {
            "dataset_ref": args.dataset_ref,
            "filter": args.contains,
            "files": len(files),
            "audited": sum(dimensions.values()),
            "dimensions": dict(sorted(dimensions.items())),
            "by_parent": {
                parent: dict(sorted(counts.items()))
                for parent, counts in sorted(by_parent.items())
            },
            "errors": errors,
        }
        return json.dumps(result, indent=2, sort_keys=True)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(image_size, args.dataset_ref, name): name for name in files}
        for index, future in enumerate(as_completed(futures), 1):
            name = futures[future]
            try:
                width, height = future.result()
                key = f"{width}x{height}"
                dimensions[key] += 1
                by_parent[str(PurePosixPath(name).parent)][key] += 1
            except Exception as error:  # Keep the audit running and expose every failure.
                errors[name] = repr(error)
            if index % 100 == 0:
                print(f"audited {index}/{len(files)}", file=sys.stderr, flush=True)
                if args.output:
                    args.output.parent.mkdir(parents=True, exist_ok=True)
                    args.output.write_text(render() + "\n", encoding="utf-8")

    rendered = render()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
