#!/usr/bin/env python3
"""List or selectively extract a remote ZIP using HTTP byte ranges."""

from __future__ import annotations

import argparse
from collections import Counter
import io
import re
import shutil
import urllib.request
import zipfile
from pathlib import Path


class HTTPRangeFile(io.RawIOBase):
    def __init__(self, url: str, block_size: int = 2 * 1024 * 1024):
        self.url = url
        self.block_size = block_size
        request = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(request) as response:
            self.length = int(response.headers["Content-Length"])
        self.position = 0
        self.cache_start = -1
        self.cache = b""

    def readable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        return self.position

    def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        if whence == io.SEEK_SET:
            position = offset
        elif whence == io.SEEK_CUR:
            position = self.position + offset
        elif whence == io.SEEK_END:
            position = self.length + offset
        else:
            raise ValueError(f"Unsupported whence: {whence}")
        if position < 0:
            raise ValueError("Negative seek position")
        self.position = min(position, self.length)
        return self.position

    def read(self, size: int = -1) -> bytes:
        if self.position >= self.length:
            return b""
        if size is None or size < 0:
            size = self.length - self.position
        size = min(size, self.length - self.position)
        cache_end = self.cache_start + len(self.cache)
        if not (self.cache_start <= self.position and self.position + size <= cache_end):
            start = self.position
            end = min(self.length, start + max(size, self.block_size)) - 1
            request = urllib.request.Request(self.url, headers={"Range": f"bytes={start}-{end}"})
            with urllib.request.urlopen(request) as response:
                if response.status != 206:
                    raise OSError(f"Server ignored byte range: HTTP {response.status}")
                self.cache_start = start
                self.cache = response.read()
        relative = self.position - self.cache_start
        result = self.cache[relative : relative + size]
        self.position += len(result)
        return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--match", default=".*", help="Regular expression matched against ZIP paths")
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--group-depth", type=int, help="Count matches by the first N path components")
    parser.add_argument("--limit", type=int, help="Use only the first N matching entries")
    args = parser.parse_args()

    pattern = re.compile(args.match, re.IGNORECASE)
    with zipfile.ZipFile(HTTPRangeFile(args.url)) as archive:
        members = [item for item in archive.infolist() if pattern.search(item.filename)]
        if args.limit is not None:
            members = members[: args.limit]
        if args.group_depth:
            counts = Counter(
                "/".join(Path(item.filename).parts[: args.group_depth])
                for item in members
                if not item.is_dir()
            )
            for group, count in sorted(counts.items()):
                print(f"{count}\t{group}")
            return
        if args.destination is None:
            for item in members:
                print(f"{item.file_size}\t{item.compress_size}\t{item.filename}")
            return
        args.destination.mkdir(parents=True, exist_ok=True)
        for item in members:
            if item.is_dir():
                continue
            member_path = Path(item.filename)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise ValueError(f"Unsafe ZIP path: {item.filename}")
            output = args.destination / member_path
            output.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(item) as source, output.open("wb") as target:
                shutil.copyfileobj(source, target)
            print(output)


if __name__ == "__main__":
    main()
