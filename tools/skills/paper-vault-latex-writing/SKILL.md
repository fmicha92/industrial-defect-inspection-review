---
name: paper-vault-latex-writing
description: Draft or revise the associated dataset-centered manufacturing visual-inspection manuscript from curated vault and review evidence, working section by section with claim-local citations and a user feedback checkpoint before major edits.
metadata:
  short-description: Write the manuscript from curated graph evidence
---

# Paper Vault LaTeX Writing

## Scope

Use this project skill for manuscript work connecting:

- evidence vault: `evidence/graph/vault/`
- review decisions and extractions: `evidence/review/`
- manuscript source: `evidence/review/publication/manuscript/`
- publication tables/data: `evidence/review/publication/tables/` and `evidence/review/publication/data/`

If no real `.tex` file or bibliography exists under `evidence/review/publication/manuscript/`, stop and ask which manuscript source should be added; do not fabricate a paper scaffold as if it were the submitted manuscript.

## Controlling story

This is a dataset-centered evidence review of image-based visual defect inspection in industrial manufacturing. Public manufacturing datasets are the organizing backbone. The research-paper layer includes only studies that use an overviewed public dataset, apply explicit data synthesis, and report a downstream ML inspection outcome.

The controlling claim is:

> Public datasets, data-synthesis methods, and ML inspection models should be evaluated together: synthesis should be compared by measurable downstream benefit, and ML methods should be interpreted under clearly specified dataset, task, annotation, domain, metric, split, and baseline conditions.

Primary questions are:

1. Which public image datasets are available, and how do they differ by domain, task, modality, annotation, access, and synthesis-evaluation suitability?
2. Which synthesis approaches are best supported by downstream inspection evidence on those datasets?
3. Which downstream ML models are best supported when trained or evaluated with that synthesis support?

## Workflow

1. **Agree on one unit of work.** Select a section, subsection, table, paragraph, or claim set.
2. **Inspect the manuscript and neighboring sections.** Check the abstract-to-outlook story and the citation commands already in use.
3. **Read review outputs first.** Use manually confirmed extraction tables where available; automated candidates are not final evidence.
4. **Search the vault.** Use `rg` for dataset names, methods, metrics, tasks, and paper titles; read the relevant notes and follow material wikilinks.
5. **Build an evidence map.** For every proposed claim, identify the source note, paper key/DOI, intended BibTeX key, evidence strength, and exact local claim supported.
6. **Surface gaps and conflicts.** Do not write unsupported claims as facts. Specify the missing source or dataset-method-task combination that needs verification.
7. **Present the outline and ask for acceptance.** Wait before substantial framing or prose changes. Tiny mechanical corrections may proceed directly.
8. **Draft in full scientific paragraphs.** Keep transitions and the paper's central argument coherent.
9. **Cite locally.** Confirm every key in the actual bibliography. Use the manuscript's established citation package; for `natbib`, prefer `\citep{...}` and `\citet{...}`.
10. **Edit narrowly and verify.** Preserve unrelated user changes, re-read the section, run citation/path checks, and compile only through the repository's documented manuscript workflow.
11. **Close the loop.** Report edited files, evidence notes used, unresolved gaps, and the next decision.

## Citation and claim rules

- Do not cite from memory or invent BibTeX keys.
- Cite dataset properties, access, synthesis methods, downstream results, baselines, limitations, and research gaps next to the exact claim they support.
- Prefer 1--3 representative citations per sentence. Move exhaustive support into a table rather than dumping citations at paragraph ends.
- Keep classification, detection, segmentation, and anomaly-detection results distinct.
- Interpret improvements relative to the real-only baseline and comparable evaluation conditions.
- When heterogeneous evidence cannot support a single best method, state conditional conclusions and the reason.

## Quality bar

Write for an applied computer-science/manufacturing journal such as the *Journal of Intelligent Manufacturing*. The registry must be systematic and traceable, the review protocol reproducible, the synthesis comparisons conditional on actual downstream evidence, and limitations about private data, domain shift, annotation quality, reproducibility, and synthetic-to-real transfer explicit.
