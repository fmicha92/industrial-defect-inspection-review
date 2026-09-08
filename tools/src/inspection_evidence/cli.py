"""Command-line interface for the evidence repository."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .exporter import export_repository
from .repository import find_root
from .validator import format_report, validate_repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="inspection-evidence")
    parser.add_argument("--root", type=Path, help="Repository root (auto-detected by default).")
    subparsers = parser.add_subparsers(dest="command", required=True)
    export = subparsers.add_parser("export", help="Generate graph exports and vault statistics.")
    export.add_argument("--check", action="store_true", help="Fail if committed outputs are stale.")
    subparsers.add_parser("validate", help="Validate repository structure and graph integrity.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve() if args.root else find_root(Path.cwd())
    except FileNotFoundError as exc:
        parser.error(str(exc))
    if args.command == "export":
        differences = export_repository(root, check=args.check)
        if differences:
            print("Generated artifacts are stale or missing:", file=sys.stderr)
            for path in differences:
                print(f"  - {path}", file=sys.stderr)
            return 1
        print("Exports are current." if args.check else "Exports generated successfully.")
        return 0
    report = validate_repository(root)
    print(format_report(report))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
