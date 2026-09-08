# Repository map

The repository has four primary directories: evidence, tools, documentation, and the website.

```text
.
├── evidence/
│   ├── graph/
│   │   ├── vault/                  # canonical Markdown/Obsidian evidence
│   │   ├── schema/                 # note contracts and controlled vocabulary
│   │   └── exports/                # deterministic CSV/JSON snapshots
│   └── review/
│       ├── protocol/               # scope, eligibility, and search documentation
│       ├── screening/              # decision-ledger guidance
│       ├── extraction/             # extraction guidance
│       ├── templates/              # screening and extraction forms
│       └── publication/            # manuscript, table, figure, and data guidance
├── tools/
│   ├── src/inspection_evidence/    # Python parser, exporter, and validator
│   ├── tests/                      # Python and repository-layout tests
│   ├── config/                     # paths, schema version, and snapshot settings
│   ├── acquire/                    # opt-in source-acquisition helpers
│   ├── audit/                      # specialist dataset-audit tools
│   ├── graph/                      # graph-figure helper
│   ├── archive/                    # reference publication tools
│   ├── skills/                     # project-authored Agent Skills
│   └── vendor/agent-skills/         # attributed third-party snapshots
├── docs/
│   └── licenses/                   # complete license texts
├── website/
│   ├── src/                        # pages, graph, charts, and tests
│   ├── public/data/                # scientific JSON bundles
│   ├── public/downloads/           # reference tables
│   └── scripts/                    # optional website data-maintenance utilities
└── .github/workflows/              # validation and GitHub Pages
```

The root retains conventional project entry points: `README.md`, `pyproject.toml`, `Makefile`, `environment.yml`, `CITATION.cff`, and contribution, security, and license notices.

## Evidence and publication boundaries

- [evidence/graph/vault/](../evidence/graph/vault/) is the source of truth for graph notes. The exporter derives [evidence/graph/exports/](../evidence/graph/exports/) from this vault.
- [evidence/review/](../evidence/review/) holds review rules and human decisions. Automated candidate flags do not establish inclusion.
- [evidence/review/publication/](../evidence/review/publication/) contains guidance for manuscript-facing material, not a second evidence database or a compilable manuscript.
- [website/public/](../website/public/) contains the scientific content needed to build the site. These assets remain distinct from the broader graph exports.
- [tools/archive/](../tools/archive/) contains tools with additional input requirements; they are not invoked by supported checks or website builds.
- [tools/vendor/agent-skills/](../tools/vendor/agent-skills/) retains third-party attribution separately from [project-authored skills](../tools/skills/).

## Naming conventions

Organizational directories use lowercase names and hyphens for multiword names. Python packages, modules, and established tabular field names follow their language or data-format conventions. Conventional filenames such as `README.md`, `LICENSE`, and `SKILL.md` retain their expected casing.

Names inside the evidence vault are scientific record titles and stable wikilink targets. Their casing, spacing, and hierarchy form part of the evidence identifiers and should not be normalized as ordinary directory names. Vendored filenames and internal relationships retain their upstream conventions.

## Paths and local material

[tools/config/repository.json](../tools/config/repository.json) defines the toolkit's repository-relative paths. The CLI searches for this marker when invoked from a nested directory. Run documented commands from the repository root unless a guide states otherwise.

`workspace/` is an optional, ignored directory for private material, not part of the public source tree. Website dependencies and build output are local artifacts in `website/node_modules/` and `website/dist/`. See [LOCAL_WORKSPACE.md](LOCAL_WORKSPACE.md) and [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
