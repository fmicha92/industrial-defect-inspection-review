# Local workspace policy

Use an optional `workspace/` directory at the repository root for private processing material. The entire directory is excluded by [.gitignore](../.gitignore) and is not required for graph validation or website builds.

Suitable local-only content includes lawfully obtained paper PDFs, extracted full text, dataset downloads, temporary extraction manifests, and license-unverified skill copies. Keep these materials out of the public graph, review outputs, website assets, and Git history.

- Do not force-add ignored material.
- Keep credentials out of source files and generated artifacts.
- Confirm provenance, redistribution rights, and personal-data handling before publishing any material.
- Place only approved third-party skill snapshots in [tools/vendor/agent-skills/](../tools/vendor/agent-skills/), with the required license and provenance records.
- Keep local provenance fields out of public exports as specified in the [data dictionary](DATA_DICTIONARY.md).

`website/public/downloads/` contains approved, versioned reference tables and is part of the repository. It is not a location for private downloads.
