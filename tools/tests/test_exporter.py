import csv
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from inspection_evidence.exporter import export_repository


class ExporterTests(unittest.TestCase):
    def test_public_dataset_synthesis_candidate_export(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            vault = root / "evidence" / "graph" / "vault"
            (vault / "Bases").mkdir(parents=True)
            (vault / "Datasets" / "Public").mkdir(parents=True)
            (vault / "Papers" / "Research").mkdir(parents=True)
            (root / "tools" / "config").mkdir(parents=True)
            (root / "tools" / "config" / "repository.json").write_text(json.dumps({
                "repository_schema_version": "1.0.0",
                "snapshot_date": "2026-01-01",
                "paths": {"vault": "evidence/graph/vault", "exports": "evidence/graph/exports"},
                "export": {"list_separator": " | ", "include_note_body": False, "candidate_screen_is_authoritative": False},
            }), encoding="utf-8")
            (vault / "Bases" / "Vault Statistics.md").write_text('---\ntitle: "Vault Statistics"\n---\n', encoding="utf-8")
            (vault / "Datasets" / "Public" / "Example.md").write_text(
                '---\ntitle: "Example Dataset"\nurl: "https://example.org"\navailability: "public"\n---\n', encoding="utf-8"
            )
            (vault / "Papers" / "Research" / "Paper.md").write_text(
                '---\ntitle: "Diffusion synthesis for inspection"\npaper_key: "example:1"\npaper_type: research\nyear: 2025\nstatus: processed\ndatasets:\n  - "[[Example Dataset]]"\nmethods:\n  - "Diffusion models"\n---\nUses [[Example Dataset]].\n', encoding="utf-8"
            )
            export_repository(root)
            text = (root / "evidence" / "graph" / "exports" / "synthesis_impact_candidates.csv").read_text(encoding="utf-8")
            rows = list(csv.DictReader(io.StringIO(text)))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["public_datasets"], "Example Dataset")
            self.assertEqual(rows[0]["eligibility_status"], "manual confirmation required")
            self.assertEqual(export_repository(root, check=True), [])


if __name__ == "__main__":
    unittest.main()
