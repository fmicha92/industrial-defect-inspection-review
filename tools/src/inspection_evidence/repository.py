"""Repository discovery and configuration shared by the command-line tools."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CONFIG_PATH = Path("tools/config/repository.json")


def find_root(start: Path) -> Path:
    start = start.resolve()
    if start.is_file():
        start = start.parent
    for candidate in (start, *start.parents):
        if (candidate / CONFIG_PATH).is_file():
            return candidate
    raise FileNotFoundError(f"Could not find {CONFIG_PATH.as_posix()}; pass --root.")


def load_config(root: Path) -> dict[str, Any]:
    return json.loads((root / CONFIG_PATH).read_text(encoding="utf-8"))
