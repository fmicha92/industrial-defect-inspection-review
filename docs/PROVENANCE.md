# Provenance model

The repository preserves four distinct provenance layers:

1. **External sources** — papers, dataset landing pages, repositories, and archival records identified by DOI, paper key, URL, or wikilink.
2. **Curated notes** — human- and agent-assisted Markdown extractions in [evidence/graph/vault/](../evidence/graph/vault/).
3. **Review decisions** — explicit eligibility and extraction judgments in [evidence/review/](../evidence/review/).
4. **Generated artifacts** — graph exports and publication-facing products derived from the preceding layers.

Frontmatter is a discovery and linkage layer, not proof by itself. A factual claim should remain traceable to the corresponding note and, where necessary, the underlying source. Conflicts must be represented explicitly rather than silently resolved.

The website's checked-in bundles have their own [data-provenance contract](../website/DATA_PROVENANCE.md) and [scientific-content audit](../website/SCIENTIFIC_CONTENT_AUDIT.md). Its evidence collection is distinct from automated graph candidate lists.

[Publication reference scripts](../tools/archive/legacy-publication-scripts/) require inputs that are not included. They are neither evidence sources nor part of the supported build.

Third-party skill attribution is recorded in [tools/vendor/agent-skills/provenance.json](../tools/vendor/agent-skills/provenance.json) and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
