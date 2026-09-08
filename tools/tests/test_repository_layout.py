import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from inspection_evidence.cli import find_root
from inspection_evidence.repository import load_config
from inspection_evidence.validator import _public_files, validate_repository


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def make_repository(root: Path) -> None:
    files = {
        ".gitignore": "workspace/\n",
        "README.md": "# Test repository\n",
        "LICENSE": "Test license\n",
        "CITATION.cff": "title: Test repository\n",
        "CONTRIBUTING.md": "# Contributing\n",
        "SECURITY.md": "# Security\n",
        "THIRD_PARTY_NOTICES.md": "# Notices\n",
        "docs/LOCAL_WORKSPACE.md": "# Local workspace\n",
        "docs/licenses/MIT.txt": "Test license\n",
        "docs/licenses/CC-BY-4.0.md": "Test license\n",
        ".github/workflows/validate.yml": "name: Test validation\n",
        "tools/vendor/agent-skills/PROVENANCE.md": "# Provenance\n",
        "tools/vendor/agent-skills/example/SKILL.md": "# Vendor example\n",
        "tools/skills/example/SKILL.md": "---\nname: example\ndescription: Test skill\n---\n",
        "evidence/graph/schema/note.json": "{}\n",
    }
    for relative, content in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for relative in (
        "evidence/graph/vault", "evidence/graph/exports", "evidence/review/protocol",
        "evidence/review/publication", "tools/archive", "tools/src/inspection_evidence",
        "tools/tests", "website/src/pages", "tools/config",
    ):
        (root / relative).mkdir(parents=True, exist_ok=True)
    (root / "tools/config/repository.json").write_text(json.dumps({
        "repository_schema_version": "1.0.0",
        "snapshot_date": "2026-01-01",
        "paths": {
            "vault": "evidence/graph/vault", "exports": "evidence/graph/exports",
            "review": "evidence/review", "publication": "evidence/review/publication",
            "workspace": "workspace",
        },
        "export": {"list_separator": " | ", "include_note_body": False},
    }), encoding="utf-8")
    (root / "tools/vendor/agent-skills/provenance.json").write_text(json.dumps({
        "sources": [{"id": "example", "repository": "https://example.org/skills", "license": "MIT", "skills": ["example"]}],
    }), encoding="utf-8")


class RepositoryLayoutTests(unittest.TestCase):
    def test_root_discovery_from_nested_publication_and_website(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "tools/config").mkdir(parents=True)
            (root / "tools/config/repository.json").write_text("{}", encoding="utf-8")
            for relative in (
                "evidence/review/publication/manuscript", "website/src/pages",
                "tools/src/inspection_evidence", "tools/tests", "tools/skills/example/scripts",
            ):
                nested = root / relative
                nested.mkdir(parents=True)
                self.assertEqual(find_root(nested), root)
            self.assertEqual(find_root(root / "tools/config/repository.json"), root)
            self.assertEqual(load_config(root), {})

    def test_root_discovery_requires_repository_marker(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(FileNotFoundError, "tools/config/repository.json"):
                find_root(root)

    def test_validates_consolidated_layout_and_vendor_coverage(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            make_repository(root)
            report = validate_repository(root)
            self.assertTrue(report.ok, report.errors)
            self.assertEqual(report.metrics["vendored_skills"], 1)
            self.assertEqual(report.metrics["vendored_skills_with_provenance"], 1)
            (root / "tools/skills").rename(root / "other-skills")
            report = validate_repository(root)
            self.assertIn("missing required path: tools/skills", report.errors)

    def test_rejects_missing_configured_evidence_path(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            make_repository(root)
            config = load_config(root)
            config["paths"]["vault"] = "evidence/missing-vault"
            (root / "tools/config/repository.json").write_text(json.dumps(config), encoding="utf-8")
            report = validate_repository(root)
            self.assertFalse(report.ok)
            self.assertTrue(any("configured vault" in error for error in report.errors))

    def test_wrappers_use_repository_paths_from_nested_working_directory(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            make_repository(root)
            shutil.copytree(
                REPOSITORY_ROOT / "tools/src/inspection_evidence",
                root / "tools/src/inspection_evidence",
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            for name in ("validate_repository.py", "export_knowledge_graph.py"):
                shutil.copy2(REPOSITORY_ROOT / "tools" / name, root / "tools" / name)
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            environment.pop("PYTHONPATH", None)
            validation = subprocess.run(
                [sys.executable, "-B", str(root / "tools/validate_repository.py")],
                cwd=root / "website/src/pages", env=environment,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(validation.returncode, 0, validation.stdout + validation.stderr)
            self.assertIn("Repository validation: PASS", validation.stdout)
            before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            export = subprocess.run(
                [sys.executable, "-B", str(root / "tools/export_knowledge_graph.py"), "--check"],
                cwd=root / "website/src/pages", env=environment,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(export.returncode, 1, export.stdout + export.stderr)
            self.assertIn("evidence/graph/exports/nodes.csv", export.stderr.replace("\\", "/"))
            after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(before, after, "The export --check wrapper must not write files")

    def test_public_scan_covers_sources_without_build_or_local_files(self):
        public = {
            "README.md",
            "docs/LOCAL_WORKSPACE.md",
            "evidence/review/publication/data/README.md",
            "tools/archive/legacy-publication-scripts/example.py",
            "tools/vendor/agent-skills/example/SKILL.md",
            "website/public/downloads/evidence.csv",
            "website/src/App.tsx",
            "node_modules/example/package.json",
        }
        excluded = {
            ".git/config",
            "workspace/unlicensed-agent-skills/example/SKILL.md",
            ".venv/lib/example.py",
            "tools/src/__pycache__/example.pyc",
            "tools/src/example.egg-info/PKG-INFO",
            "website/node_modules/example/package.json",
            "website/dist/assets/example.js",
            "website/coverage/report.json",
        }
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in public | excluded:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("test fixture\n", encoding="utf-8")
            observed = {path.relative_to(root).as_posix() for path in _public_files(root)}
            self.assertEqual(observed, public)


if __name__ == "__main__":
    unittest.main()
