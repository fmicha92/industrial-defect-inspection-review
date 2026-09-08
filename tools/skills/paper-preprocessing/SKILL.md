---
name: paper-preprocessing
description: Use this project-local skill when ingesting, deduplicating, preprocessing, analyzing, or marking research papers in the Paper Vault. It keeps raw inputs and processing artifacts outside evidence/graph/vault/, uses the paper intake script, and ensures Codex analyzes preprocessed analysis inputs instead of raw PDFs whenever possible.
---

# Paper Preprocessing

Use this skill for paper intake and processing in this project. Keep `evidence/graph/vault/`
for Obsidian-only files. All raw paper intake and intermediate processing state
belongs outside `evidence/graph/vault/`.

Dataset host pages such as Kaggle, GitHub, IEEE DataPort, Zenodo, Hugging Face,
or institutional repositories do not need to be placed in `workspace/paper-inbox/` unless
the user downloads source files for local analysis. When the task is only to add
or update a dataset graph note from a web source, use `paper-processing`'s
dataset web source workflow and record the canonical host URL in the dataset
note, plus the most relevant paper that introduces the dataset when one exists.

## Folders

- `workspace/paper-inbox/` - all paper intake files, archive folders, and preprocessing state.
- `workspace/paper-inbox/00_incoming/` - raw incoming PDFs, papers, and metadata files to scan.
- `workspace/paper-inbox/10_processed/` - original source files after an Obsidian note is created,
  sorted into `Research/`, `Dataset/`, `Review/`, `Benchmark/`, `Systems/`, or `Other/`.
- `workspace/paper-inbox/20_duplicates/` - re-added source files already known as processed.
- `workspace/paper-inbox/30_failed/` - source files set aside after failed intake when needed.
- `workspace/paper-inbox/90_processing/manifest.json` - persistent registry of known papers.
- `workspace/paper-inbox/90_processing/text/` - clean extracted full text.
- `workspace/paper-inbox/90_processing/analysis-inputs/` - compact Codex-ready markdown inputs.
- `workspace/paper-inbox/90_processing/logs/` - processing logs when needed.
- `evidence/graph/vault/` - final Obsidian notes, bases, canvases, and vault config only.

## Default Workflow

Run commands from the project root:

```bash
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py scan
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py preprocess
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py list --status preprocessed
```

Place new PDFs and source files in `workspace/paper-inbox/00_incoming/`. Analyze files from
`workspace/paper-inbox/90_processing/analysis-inputs/`, not the raw PDF, unless
preprocessing failed or the user explicitly asks for raw PDF analysis.

The analysis input is a compact reading source, not a summary to skim. After
preprocessing, the paper-processing step must read the analysis input thoroughly
and create the most complete paper note supported by that input. Do not mark a
paper processed from title/abstract snippets, generic metadata, or a shallow
template.

After creating the final Obsidian note, mark the paper processed:

```bash
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py mark-processed <paper-key> \
  --year 2024 \
  --author "First Author" \
  --title "Exact Paper Title" \
  --note "evidence/graph/vault/Papers/Research/Exact Note.md"
```

Use `--year`, `--author`, and `--title` only with values extracted from the
actual paper or explicit paper metadata. This moves source files still in
`workspace/paper-inbox/00_incoming/` to `workspace/paper-inbox/10_processed/<paper-type>/` and
renames the source plus preprocessing artifacts to `year - author - title`.
The paper type is inferred from the `--note` path under `evidence/graph/vault/Papers/`;
pass `--paper-type research|dataset|review|benchmark|systems|other` only when
there is no note path to infer from. Long filenames are truncated to a safe
length. If filename fields are missing, the script falls back to the paper key
instead of inventing values. Use `--no-archive` only if the source file must stay
in place.

Only run `mark-processed` after a final note satisfies the paper-processing
completion standard: the available source has been read beyond the abstract,
source-supported datasets/methods/metrics/results/limitations have been
captured, and the graph links have been checked. Triage or concise notes should
remain unprocessed until upgraded.

To organize existing flat processed archives after changing the folder policy:

```bash
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py organize-processed --dry-run
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py organize-processed
```

## Duplicate Handling

`scan` identifies known papers by normalized DOI, arXiv ID, OpenAlex ID, or exact
SHA-256 hash. If a known paper appears in `workspace/paper-inbox/00_incoming/` again later, keep
the existing manifest record and preserve `status: processed` when already
processed. Already-processed duplicates are moved to `workspace/paper-inbox/20_duplicates/`
by default.

Use this to inspect a single file without changing the manifest:

```bash
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py check-file workspace/paper-inbox/00_incoming/example.pdf
```

## Preprocessing Rules

`preprocess` extracts text and builds a smaller analysis input:

- PDFs use local `pdftotext`.
- Text-like files are read directly.
- Clean full text goes to `workspace/paper-inbox/90_processing/text/`.
- Codex analysis markdown goes to `workspace/paper-inbox/90_processing/analysis-inputs/`.
- Trailing `References`, `Bibliography`, `Appendix`, and similar sections are
  removed from the analysis input when detected.
- Token estimates and artifact paths are written back to `manifest.json`.
- After `mark-processed`, preprocessing artifact filenames are renamed to match
  the processed source filename when paper metadata was supplied.

If preprocessing fails, report the failure from the manifest and decide whether
to install a better extractor, use another source file, or analyze the raw paper.
Failed source files are moved to `workspace/paper-inbox/30_failed/` by default; use
`--no-archive-failed` only when you want to retry the same file in place.

Preprocessing results are not stored under `workspace/paper-inbox/00_incoming/`: extracted full
text goes to `workspace/paper-inbox/90_processing/text/`, compact analysis markdown
goes to `workspace/paper-inbox/90_processing/analysis-inputs/`, and the manifest
records both paths.

## Status Commands

```bash
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py status
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py list --status queued
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py list --status preprocessed
python3 tools/skills/paper-preprocessing/scripts/paper_intake.py list --status processed
```

## Hard Rules

- Do not put raw PDFs, extracted text, digests, or processing logs under
  `evidence/graph/vault/`.
- Do not archive or mirror large hosted datasets in the vault. Link to the host
  page from the dataset note; only place downloaded files in `workspace/paper-inbox/` when
  local analysis is explicitly needed.
- Do not carry intake or preprocessing language into final Obsidian note prose.
  Keep source paths and processing status in metadata fields; summaries,
  definitions, evidence, and limitations should describe the paper itself.
- Do not fabricate identifiers, metadata, extracted text, or processing status.
- Do not invent filename metadata. `year`, `author`, and `title` used for
  renaming must come from the actual paper or explicit paper metadata.
- Prefer preprocessing before Codex analysis to reduce token use and make repeat
  analysis deterministic.
- Never treat preprocessing completion as paper-note completion. A preprocessed
  paper still requires a thorough paper-processing pass before it can be marked
  processed.
- Keep the manifest as the source of truth for whether a paper is known,
  preprocessed, or processed.
