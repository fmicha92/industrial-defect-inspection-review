# Evidence toolkit

This directory contains the software and configuration supporting the review. Run the commands below from the repository root.

```bash
python tools/validate_repository.py
python tools/export_knowledge_graph.py --check
```

Both wrappers locate the package and repository without installation. Core validation and export checks are offline, dependency-free, and non-writing.

## Contents

| Path | Purpose |
|---|---|
| [src/inspection_evidence/](src/inspection_evidence/) | Python parser, exporter, validator, and CLI |
| [tests/](tests/) | Unit, integration, and repository-layout tests |
| [config/repository.json](config/repository.json) | Repository paths, snapshot date, and export settings |
| [export_knowledge_graph.py](export_knowledge_graph.py) | Exporter wrapper; `--check` verifies existing outputs without writing |
| [validate_repository.py](validate_repository.py) | Repository and evidence validation wrapper |
| [acquire/](acquire/) | Opt-in OpenAlex, Kaggle, Google Drive, and remote-archive helpers |
| [audit/](audit/) | Specialist raw-dataset inspection tools with optional dependencies |
| [graph/](graph/) | Manuscript graph-figure helper |
| [archive/](archive/) | Reference publication tools outside the supported checks |
| [skills/](skills/) | Project-authored review and evidence-processing skills |
| [vendor/](vendor/) | Attributed third-party skill snapshots |

## Tool boundaries

Acquisition, audit, and figure-generation tools have separate input, credential, network, and dependency requirements. They are not invoked by `make check` or the website build. Project and third-party skills are instructions and utilities, not automatically installed runtime dependencies.

Publication-facing defaults use `evidence/review/publication/`. Consult each helper's `--help` and source before invoking it. Do not acquire sources, modify evidence, or regenerate scientific outputs as part of ordinary verification.

See the [reproducibility guide](../docs/REPRODUCIBILITY.md) for environment setup, package installation, and supported commands.
