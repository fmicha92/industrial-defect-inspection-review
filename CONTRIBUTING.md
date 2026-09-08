# Contributing

Contributions should preserve the evidence graph's traceability and the distinction between source evidence, reviewer judgment, and generated outputs.

1. Create or edit source notes in `evidence/graph/vault/`; do not hand-edit generated files in `evidence/graph/exports/`.
2. Keep literature-dependent claims tied to a source note, DOI, paper key, or canonical dataset URL.
3. Do not commit paper PDFs, extracted full text, dataset archives, credentials, or private data.
4. Use repository-relative paths. Machine-specific paths such as `/home/...`, `/Users/...`, or drive-letter paths fail validation.
5. Run `make check` to validate the repository, compare committed exports without rewriting them, and run the tests. Use `make export` only for intentional export generation.
6. Keep schemas, the data dictionary, and tests consistent with one another. Follow the [repository map](docs/REPOSITORY_MAP.md) for path conventions.
7. Treat automated synthesis-paper classification as screening assistance, not a final eligibility decision.

Website work belongs in `website/`. Use the pinned package manager and frozen lockfile, then run linting, type checking, tests, and the production build as described in the [website guide](website/README.md). Scientific values, evidence identifiers, and attribution must remain traceable to the checked-in assets.

Private material belongs in the ignored `workspace/`; see the [local-workspace policy](docs/LOCAL_WORKSPACE.md). Manuscript-facing material belongs in `evidence/review/publication/`.

For new Agent Skills, keep `SKILL.md` concise, put detailed material in `references/`, place repeatable code in `scripts/`, and include `agents/openai.yaml` for user-facing metadata.
