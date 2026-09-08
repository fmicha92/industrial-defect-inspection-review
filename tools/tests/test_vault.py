from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from inspection_evidence.vault import iter_notes, resolve_edges, split_frontmatter


class VaultTests(unittest.TestCase):
    def test_frontmatter_top_level_lists_and_wikilinks(self):
        metadata, body = split_frontmatter(
            '---\ntitle: "Example"\ndatasets:\n  - "[[MVTec AD]]"\nmetric_definitions:\n  AUC: "nested"\n---\n# Body\n'
        )
        self.assertEqual(metadata["title"], "Example")
        self.assertEqual(metadata["datasets"], ["[[MVTec AD]]"])
        self.assertEqual(metadata["metric_definitions"], [])
        self.assertIn("# Body", body)

    def test_edge_resolution_uses_aliases(self):
        with TemporaryDirectory() as directory:
            vault = Path(directory)
            (vault / "Datasets").mkdir()
            (vault / "Papers").mkdir()
            (vault / "Datasets" / "Dataset.md").write_text(
                '---\ntitle: "Canonical Dataset"\naliases:\n  - "Alias Dataset"\n---\n', encoding="utf-8"
            )
            (vault / "Papers" / "Paper.md").write_text(
                '---\ntitle: "Paper"\n---\nUses [[Alias Dataset]].\n', encoding="utf-8"
            )
            edges = resolve_edges(iter_notes(vault))
            self.assertEqual(len(edges), 1)
            self.assertEqual(edges[0].resolution, "resolved")
            self.assertEqual(edges[0].target_id, "Datasets/Dataset")


if __name__ == "__main__":
    unittest.main()

