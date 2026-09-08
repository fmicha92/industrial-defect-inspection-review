# Reproducibility

## Evidence checks

The core workflow uses Python 3.10 or newer and only the standard library. Run these commands from the repository root; they check the committed evidence without rewriting it.

With GNU Make and a POSIX shell:

```bash
make check
```

Equivalent POSIX commands:

```bash
PYTHONPATH=tools/src python -m inspection_evidence.cli validate
PYTHONPATH=tools/src python -m inspection_evidence.cli export --check
PYTHONPATH=tools/src python -m unittest discover -s tools/tests -v
```

PowerShell:

```powershell
$env:PYTHONPATH = "tools/src"
python -m inspection_evidence.cli validate
python -m inspection_evidence.cli export --check
python -m unittest discover -s tools/tests -v
```

The wrappers `python tools/validate_repository.py` and `python tools/export_knowledge_graph.py --check` also locate the package and repository without installation.

Validation checks source hygiene, note links, metadata, required directories, and vendor provenance. It excludes local environments, caches, and website build dependencies. Review the [quality report](QUALITY_REPORT.md) for evidence warnings that require human judgment.

## Python environment

[environment.yml](../environment.yml) records a minimal Conda environment. Source-tree execution above needs no package installation or network access.

For an installed command, use `python -m pip install --no-deps -e .`, then `inspection-evidence validate` or `inspection-evidence export --check`. Installation requires the build tools declared in [pyproject.toml](../pyproject.toml); pip may download them if they are not available.

The CLI finds [tools/config/repository.json](../tools/config/repository.json) by searching upward from the working directory, or accepts an explicit `--root` before the subcommand.

## Intentional export generation

`make export` regenerates graph exports and `evidence/graph/vault/Bases/Vault Statistics.md`. Use it only when these outputs are intended to be written. `make reproduce` runs export generation, validation, and tests. `make export-check` performs an in-memory comparison without writing files.

Determinism is supported by:

- stable repository-relative paths and identifiers;
- sorted source files and output rows;
- UTF-8 CSV files with LF endings and explicit headers;
- a snapshot date supplied by configuration rather than execution time;
- public exports that omit local preprocessing paths and note bodies.

## Website

Use Node.js 22 and pnpm 11.19.0. From the repository root:

```bash
cd website
pnpm install --frozen-lockfile
pnpm lint
pnpm typecheck
pnpm test
pnpm build
pnpm preview
```

Dependency installation may require network access. After installation, `make website-check` from the repository root runs linting, type checking, tests, and the production build with GNU Make.

The site builds from committed JSON bundles and reference tables in [website/public/](../website/public/). It does not require the manuscript or acquisition tools. The [GitHub Pages workflow](../.github/workflows/website-pages.yml) publishes the generated `website/dist/` artifact using the repository's Actions-based Pages setting.

The optional `pnpm prepare:data` maintenance command has separate source-input requirements and is not part of development, verification, or Pages builds. See the [website guide](../website/README.md).

## Optional tools and source-material boundary

[Acquisition and audit helpers](../tools/README.md) may require credentials, network access, optional scientific libraries, or lawfully obtained datasets. [Archived publication tools](../tools/archive/README.md) require inputs that are not included and are outside the supported build.

[evidence/review/publication/](../evidence/review/publication/) contains guidance, not a compilable manuscript. LaTeX compilation requires actual manuscript and bibliography files.

The public repository reproduces the curated graph exports and builds the site from its existing results. It does not redistribute full-text sources or reproduce new scientific evaluations. Private PDFs, extracted text, and dataset downloads belong in the ignored workspace described in [LOCAL_WORKSPACE.md](LOCAL_WORKSPACE.md).
