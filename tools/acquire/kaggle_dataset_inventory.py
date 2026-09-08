#!/usr/bin/env python3
"""List every file exposed by Kaggle's public dataset inventory API."""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request


API_ROOT = "https://www.kaggle.com/api/v1/datasets/list"


def inventory(dataset_ref: str) -> list[dict[str, object]]:
    owner, slug = dataset_ref.split("/", 1)
    endpoint = f"{API_ROOT}/{urllib.parse.quote(owner)}/{urllib.parse.quote(slug)}"
    page_token: str | None = None
    files: dict[str, dict[str, object]] = {}

    while True:
        parameters = {"pageSize": 200}
        if page_token:
            parameters["pageToken"] = page_token
        query = urllib.parse.urlencode(parameters)
        url = f"{endpoint}?{query}" if query else endpoint
        request = urllib.request.Request(url, headers={"User-Agent": "dataset-gap-audit/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.load(response)

        error = payload.get("errorMessage")
        if error:
            raise RuntimeError(error)
        for item in payload.get("datasetFiles", []):
            name = item.get("name")
            if isinstance(name, str):
                files[name] = {
                    "name": name,
                    "bytes": item.get("totalBytes"),
                    "created": item.get("creationDate"),
                }

        page_token = payload.get("nextPageToken")
        if not page_token:
            break

    return [files[name] for name in sorted(files)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_ref", help="Kaggle reference in owner/slug form")
    args = parser.parse_args()
    print(json.dumps(inventory(args.dataset_ref), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
