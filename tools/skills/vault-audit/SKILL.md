---
name: vault-audit
description: Audit this Obsidian research vault for structural health issues, taxonomy drift, stale folders, missing index links, and broad wiki hygiene before or after paper graph changes.
---

# Vault Audit

Use this skill when checking the Obsidian vault structure itself, especially
after moving taxonomy folders, adding graph notes, or changing paper-processing
rules.

## Quick Start

Run from the project root:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py
```

For machine-readable output:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py --json
```

Run only the taxonomy checks:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py --check taxonomy
```

Run only the dataset-domain checks:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py --check dataset-domains
```

Print vault statistics:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py --check stats
```

Refresh the in-vault statistics note:

```bash
python tools/export_knowledge_graph.py
```

The legacy `--check stats --write-stats` flag delegates to the same canonical exporter for compatibility.

Machine-readable statistics:

```bash
python3 tools/skills/vault-audit/scripts/vault_audit.py --check stats --json
```

## What It Checks

- Parent-scoped emerging folders exist:
  `Concepts/Emerging Concepts`, `Methods/Emerging Methods`,
  `Metrics/Emerging Metrics`, `Domains/Emerging Domains`, and
  `Learning Paradigms/Emerging Learning Paradigms`.
- Legacy top-level `Emerging *` folders are absent.
- Each emerging folder has a matching index note.
- Each emerging folder index links to its child notes.
- Top-level vault folders stay within the expected project taxonomy.
- Dataset notes use exactly one `domain` or `related_domain` association.
- Datasets do not appear under multiple domain notes; if they span multiple
  domains, they are associated only with `[[Multi-Industry Anomaly Detection]]`.
- Vault statistics: processed papers, paper notes, total notes, total wikilinks,
  unique wikilinks, unique wikilink targets, resolved/unresolved targets,
  embeds, orphan notes, duplicate note names, and useful folder/type/status
  breakdowns.

## Statistics Note

The canonical in-vault place for refreshed statistics is:

```text
evidence/graph/vault/Bases/Vault Statistics.md
```

The note is generated from committed vault Markdown by the canonical graph exporter. The optional private paper-intake manifest is deliberately excluded from public snapshot counts. Regenerate it after paper-processing batches, graph repairs, or taxonomy moves.

## Related Audits

Use the paper graph audit for paper-note connectivity:

```bash
python3 tools/skills/paper-processing/scripts/graph_audit.py
```

For nontrivial findings, write reports outside the Obsidian vault under
`evidence/review/audits/vault/`.
