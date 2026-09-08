# Release checklist

## Identity and citation

- [ ] Confirm the repository URL and associated manuscript citation.
- [ ] Verify contributor names in `CITATION.cff` and `pyproject.toml`; resolve placeholder entities before an archival release.
- [ ] Confirm that archival identifiers refer to an actual release.

## Evidence and data

- [ ] Manually review every record promoted from the synthesis-impact candidate list into included evidence.
- [ ] Resolve or explicitly document missing dataset license and access evidence.
- [ ] Confirm the review protocol, search dates, screening decisions, and extraction forms.
- [ ] Ensure that no restricted full text, private dataset, credentials, or personal data is distributed.
- [ ] Verify the schema version and snapshot date in `tools/config/repository.json`.
- [ ] Check website claims against [DATA_PROVENANCE.md](../website/DATA_PROVENANCE.md) and [SCIENTIFIC_CONTENT_AUDIT.md](../website/SCIENTIFIC_CONTENT_AUDIT.md).

## Software and repository hygiene

- [ ] Run `make check` or the equivalent commands in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
- [ ] Confirm that the committed exports match the source graph without rewriting them.
- [ ] Review [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and vendor provenance.
- [ ] Confirm that private `workspace/` material and generated dependencies/build products are not tracked.
- [ ] Review Agent Skills and executable helpers before use.
- [ ] Confirm repository security settings and the reporting instructions in [SECURITY.md](../SECURITY.md).

## Website and GitHub Pages

- [ ] Install the pinned package manager and dependencies using the frozen lockfile.
- [ ] Run website linting, type checking, tests, and the production build.
- [ ] Run `pnpm check:pages` from `website/` to verify every generated route and its assets under the GitHub project path without an application fallback.
- [ ] Preview the production build and inspect navigation, graph selection, directed paths, filters, and downloads.
- [ ] Check direct nested links, page refreshes, Back/Forward navigation, query parameters, and existing hash bookmarks.
- [ ] Confirm that existing scientific values and identifiers are preserved.
- [ ] Select **GitHub Actions** as the Pages source.
- [ ] Confirm that [website-pages.yml](../.github/workflows/website-pages.yml) publishes `website/dist/`.
