# Knowledge graph

`vault/` is the canonical Obsidian-compatible Markdown graph. `schema/` documents its expected top-level properties, and `exports/` contains deterministic analysis snapshots.

Open `vault/` directly as an Obsidian vault if desired. The committed `.obsidian` settings are limited to portable configuration; per-user workspace state is ignored.

Do not edit CSV or JSON exports by hand. Change source notes, then run `make export` from the repository root.

