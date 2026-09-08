---
name: paper-processing
description: Process scientific papers or dataset host pages into evidence-rich, graph-linked Obsidian notes for this manufacturing visual-inspection repository. Use when extracting structured paper evidence, creating or repairing notes, updating taxonomy links, or checking graph completeness.
---

# Paper Processing

Use this skill to turn a scientific source into a traceable note in `evidence/graph/vault/`. Extract what the source reports, distinguish it from interpretation, and keep the graph connected to existing datasets, methods, tasks, metrics, domains, concepts, and benchmarks.

Read `references/PROCESSING_GUIDE.md` for the full field-by-field policy and `references/PAPER_NOTE_TEMPLATE.md` when creating a paper note.

## Canonical paths

- Vault: `evidence/graph/vault/`
- Paper notes: `evidence/graph/vault/Papers/<Type>/`
- Dataset notes: `evidence/graph/vault/Datasets/<Availability>/`
- Optional local sources: `workspace/paper-inbox/` (Git-ignored)
- Public source URLs: record directly in note frontmatter and source anchors

## Workflow

1. **Identify the source.** Confirm title, authors, year, venue, DOI/arXiv/OpenAlex identifier, and document type from the source rather than memory.
2. **Read the best lawful source available.** Prefer the preprocessed analysis input for local papers. For dataset host pages, inspect the canonical host and the introducing paper when available.
3. **Inventory existing graph nodes.** Search before creating a dataset, method, task, domain, metric, concept, benchmark, or paper note. Reuse canonical titles and aliases.
4. **Extract structured evidence.** Capture datasets, tasks, domains, methods, model families, architectures, baselines, metrics, split/protocol details, key results, limitations, code/data artifacts, and source identifiers when reported.
5. **Separate evidence levels.** Label claims as reported/claimed, shown by an experiment, or reviewer inference. Do not convert an inference into a reported result.
6. **Write the paper note.** Use the template and complete prose/tables where they improve traceability. Use `not reported` for checked but absent details; do not invent metadata.
7. **Link the graph.** Add frontmatter wikilinks and concise reciprocal backlinks in the relevant graph notes. Preserve the one-domain invariant for each dataset.
8. **Run audits.** Execute `python tools/skills/paper-processing/scripts/graph_audit.py` and, for substantial paper repairs, the `paper-audit` workflow.
9. **Mark completion only after verification.** A processed note must reflect a full source read beyond title/abstract metadata and have its graph links checked.

## Evidence integrity

- Do not use model memory as evidence.
- Do not cite a dataset property from a downstream paper when a primary dataset source is available without making the provenance explicit.
- Keep classification, detection, segmentation, and anomaly-detection outcomes distinct.
- Preserve the real-only baseline, metric definition, task, split, annotation level, and dataset condition for any claimed synthesis benefit.
- Do not treat visual realism metrics alone as downstream inspection evidence.
- Never infer public availability or redistribution permission from the existence of a URL.
- If sources conflict, record the conflict and source-specific values instead of silently choosing one.

## Dataset web sources

For a dataset host page without a local PDF:

1. verify the canonical landing page and access status;
2. locate the introducing paper or archival record when one exists;
3. extract only properties supported by the inspected sources;
4. record license/access evidence separately from general availability;
5. add related papers only when the relationship is source-supported; and
6. route out-of-scope contextual datasets clearly rather than presenting them as final manufacturing-registry entries.

## Graph rules

- Search with `rg` before creating a new node.
- Use one canonical note per concept and add aliases for variants.
- Dataset notes use exactly one `domain` or `related_domain` value. Multi-domain datasets route to `[[Multi-Industry Anomaly Detection]]`.
- New methods or concepts with weak support belong in the appropriate `Emerging *` folder until repeated evidence justifies promotion.
- Reciprocal backlinks should state the relationship, not merely repeat a title.
- Run the graph audit after any batch that changes multiple relations.

## Batch processing

Treat a batch as repeated complete single-paper workflows. Do not create shallow notes to increase throughput. After each paper, finish source extraction, note creation, reciprocal linking, and validation before proceeding.

## Completion report

Report:

- source and note path;
- identifiers and source state used;
- datasets, methods, tasks, metrics, and key downstream evidence added;
- graph notes created or updated;
- unresolved evidence gaps or source conflicts; and
- audit result.

Do not claim the note is complete when a required source was unavailable or only abstract-level evidence was inspected.
