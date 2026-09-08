---
name: paper-audit
description: Use when auditing one or more existing Obsidian paper notes for extraction completeness against their preprocessed source inputs, maintaining an audit registry, prioritizing unaudited or oldest-audited papers, and repairing shallow or placeholder paper notes.
---

# Paper Audit

Use this skill to catch shallow paper notes that were marked processed without a
thorough read of their source. The audit checks note quality; it does not
replace `paper-processing` for repairs.

## Registry

The audit registry lives outside the vault:

```text
evidence/review/audits/paper_registry.json
```

Each entry tracks:

- `note_path` - paper note under `evidence/graph/vault/Papers/`
- `title`, `paper_key`, `year`, `paper_type`
- `source_file`, `preprocessed_input`, `extracted_text`
- `added_at`, `added_source`
- `last_audited_at`, `audit_status`, `audit_history`
- `last_linked_at`, `linked_notes`, `graph_audit_status`
- latest automated `flags`

## Commands

Run from the project root.

```bash
# Add/update all paper notes in the registry
python3 tools/skills/paper-audit/scripts/paper_audit.py sync

# Show next papers to audit; never-audited first, then oldest audit
python3 tools/skills/paper-audit/scripts/paper_audit.py queue --limit 20

# Run automated shallow-extraction checks for one note
python3 tools/skills/paper-audit/scripts/paper_audit.py check "evidence/graph/vault/Papers/Research/Example.md"

# Mark a human/agent audit result after reading the source and repairing if needed
python3 tools/skills/paper-audit/scripts/paper_audit.py mark "evidence/graph/vault/Papers/Research/Example.md" \
  --status fixed --graph-links-checked \
  --linked-note "evidence/graph/vault/Datasets/Public/Example Dataset.md" \
  --notes "Re-read source; added missing dataset split and metrics."
```

## Audit Workflow

1. Run `sync` before auditing.
2. Run `queue`; start with the first unaudited paper.
3. Run `check <note>` to identify automated warning signs.
4. Read the note and its `preprocessed_input` or `extracted_text` thoroughly.
   Treat that preprocessed paper state as the source of truth for extracted
   facts.
5. Compare the note against the preprocessed source for missing datasets,
   methods, metrics, results, limitations, artifacts, and graph links.
6. If the paper note is updated, immediately do a graph relink pass:
   inventory existing nodes, add or correct frontmatter links, update the
   `Connections` section, create or route missing graph notes, and update
   reciprocal backlinks in related dataset, task, method, domain, metric,
   benchmark, and important paper notes.
7. Check every affected dataset note for the dataset-domain invariant: exactly
   one `domain` or `related_domain` value, no plural domain fields, and no
   duplicate reciprocal entries across multiple domain notes. If the dataset
   spans more than one industry, material class, application area, or sensor/use
   context, route it only to `[[Multi-Industry Anomaly Detection]]`.
8. Run `graph_audit.py` after repairs and resolve missing links and
   dataset-domain errors.
9. Mark the audit and record graph-link evidence:
   - `passed` - source read; no repairs needed
   - `fixed` - source read; note repaired
   - `needs-work` - blocker remains; explain in `--notes`

## Batch Audits

When asked to audit more than one paper, such as "audit the next 20 papers",
treat the request as repeated single-paper audits, not a bulk triage pass.

For each paper, finish the complete workflow before starting the next one:

1. Take the next queued paper.
2. Run `check <note>`.
3. Thoroughly read the full `preprocessed_input`; if missing, use
   `extracted_text`. Do not skim only the abstract, snippets, or flagged lines.
4. Update the paper note only with facts extracted from the preprocessed source
   state: missing datasets, methods, metrics, results, limitations, artifacts,
   and reproducibility details.
5. Refresh graph connections and reciprocal backlinks for affected dataset,
   task, method, domain, metric, benchmark, artifact, and important paper notes.
   Dataset notes must keep exactly one domain association; multi-domain datasets
   must be associated only with `[[Multi-Industry Anomaly Detection]]`.
6. Run `graph_audit.py` and resolve missing links and dataset-domain issues
   introduced or exposed by the audit.
7. Mark that paper `passed`, `fixed`, or `needs-work` with linked-note evidence.

Only then continue to the next queued paper. If a blocker appears for one paper,
mark it `needs-work` with the blocker and continue with the remaining requested
papers unless the blocker affects the whole batch.

## Audit Reporting

After each audit response, briefly report the number of files changed for that
paper audit. Keep this to numbers, such as `Files changed: 4`.

Also report files and connections added:

- `Files changed: N`
- `Files added: N`
- `Connections added: N`

When auditing multiple papers, list each audited paper in chat as its own short
paragraph. For each paper, include:

- paper title or note name
- key points of what was checked or changed
- `Files changed: N`
- `Files added: N`
- `Connections added: N`

## Automated Flags

Treat these as triage signals, not final judgment:

- shallow placeholder phrases: `concise extraction`, `not fully extracted`,
  `not fully reported`, `see extracted snippets below`
- generic boilerplate in result or method sections
- many `not reported` values despite an available source input
- missing or nonexistent `preprocessed_input` / `extracted_text`
- metrics listed without a populated performance-metrics section

## Hard Rules

- Do not mark a paper `passed` or `fixed` without reading the source input
  beyond the abstract.
- Extract data from `preprocessed_input`, `extracted_text`, and explicit paper
  metadata only. Do not fill missing datasets, methods, metrics, claims,
  results, limitations, artifacts, or links from memory, general knowledge,
  likely field norms, or model training data.
- Do not audit multiple papers by sampling or summarizing the queue. Each paper
  must be read, repaired, graph-checked, and marked individually.
- Do not trust registry status over evidence in the note and source.
- Do not use automated flags alone to rewrite facts. Repairs must be grounded in
  the actual paper/source text.
- Do not mark a repaired paper `fixed` unless related graph notes were reviewed
  and linked again. Paper-note content changes must propagate to the existing
  vault graph where source-supported.
- Never mark triage notes as audited final paper notes.
- Keep audit reports and registry files under `evidence/review/audits/`, not `evidence/graph/vault/`.
