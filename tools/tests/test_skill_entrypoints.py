"""Offline checks for project-skill entry points and repository path defaults."""

import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "paper-audit/scripts/paper_audit.py": {
        "PROJECT_ROOT": ".",
        "VAULT_DIR": "evidence/graph/vault",
        "DEFAULT_REGISTRY": "evidence/review/audits/paper_registry.json",
    },
    "paper-preprocessing/scripts/paper_intake.py": {
        "PROJECT_ROOT": ".",
        "VAULT_DIR": "evidence/graph/vault",
    },
    "paper-processing/scripts/graph_audit.py": {
        "ROOT": ".",
        "VAULT": "evidence/graph/vault",
    },
    "paper-semantic-relations/scripts/paper_semantic_relations.py": {
        "PROJECT_ROOT": ".",
        "OBSIDIAN_ROOT": "evidence/graph/vault",
        "PAPERS_ROOT": "evidence/graph/vault/Papers",
        "SCHOLAR_SEARCH_DIR": "tools/vendor/agent-skills/scholar-search/scripts",
    },
    "prisma-workflow/scripts/prisma_review.py": {
        "ROOT": ".",
        "DEFAULT_OUT_DIR": "evidence/review/sessions",
    },
    "vault-audit/scripts/vault_audit.py": {
        "ROOT": ".",
        "VAULT": "evidence/graph/vault",
        "STATS_NOTE": "evidence/graph/vault/Bases/Vault Statistics.md",
    },
}

READ_DEFAULTS = """
import json
from pathlib import Path
import runpy
import sys

namespace = runpy.run_path(sys.argv[1], run_name="skill_path_regression")
names = json.loads(sys.argv[2])
print(json.dumps({name: str(Path(namespace[name]).resolve()) for name in names}))
"""


class SkillEntrypointTests(unittest.TestCase):
    @staticmethod
    def child_environment():
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        for name in ("INSPECTION_EVIDENCE_ROOT", "INSPECTION_EVIDENCE_VAULT", "PYTHONPATH"):
            environment.pop(name, None)
        return environment

    def test_help_works_outside_repository_without_running_a_skill(self):
        with TemporaryDirectory() as directory:
            working_directory = Path(directory)
            for relative in SKILLS:
                with self.subTest(skill=relative):
                    result = subprocess.run(
                        [sys.executable, "-B", str(REPOSITORY_ROOT / "tools/skills" / relative), "--help"],
                        cwd=working_directory,
                        env=self.child_environment(),
                        capture_output=True, text=True, check=False, timeout=20,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("usage:", result.stdout.lower())
                    self.assertEqual(list(working_directory.iterdir()), [])

    def test_imported_defaults_resolve_to_repository_evidence(self):
        with TemporaryDirectory() as directory:
            working_directory = Path(directory)
            for relative, expected_paths in SKILLS.items():
                with self.subTest(skill=relative):
                    result = subprocess.run(
                        [sys.executable, "-B", "-c", READ_DEFAULTS,
                         str(REPOSITORY_ROOT / "tools/skills" / relative),
                         json.dumps(list(expected_paths))],
                        cwd=working_directory,
                        env=self.child_environment(),
                        capture_output=True, text=True, check=False, timeout=20,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    observed = json.loads(result.stdout)
                    self.assertEqual(
                        {name: Path(value) for name, value in observed.items()},
                        {name: (REPOSITORY_ROOT / value).resolve()
                         for name, value in expected_paths.items()},
                    )
                    self.assertEqual(list(working_directory.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
