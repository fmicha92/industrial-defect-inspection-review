#!/usr/bin/env python3
"""Stable wrapper for the knowledge-graph exporter."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "src"))

from inspection_evidence.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main(["--root", str(ROOT), "export", *sys.argv[1:]]))
