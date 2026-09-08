# Repository quality report

Snapshot date: 2026-08-27  
Repository-readiness verification: 2026-08-28

## Automated status

The supported repository validation passes. The snapshot contains:

| Check | Result |
|---|---:|
| Markdown notes | 896 |
| Paper notes | 226 |
| Substantive dataset notes | 157 |
| Public dataset notes | 85 |
| Public manufacturing-scope candidates | 76 |
| Private dataset notes | 2 |
| Availability-unspecified dataset notes | 70 |
| Unique wikilink edges | 8,926 |
| Resolved edges | 8,926 |
| Ambiguous or unresolved edges | 0 |
| Automated synthesis-impact candidates | 142 |

All custom project skills pass the Agent Skill quick validator, the legacy graph audit reports zero errors and warnings, the vault taxonomy audit reports zero errors and warnings, generated exports are synchronized, and the dependency-free unit suite passes.

All 10 tracked third-party Agent Skill snapshots are covered by the machine-readable provenance manifest. License-unverified local copies remain outside the public tree through `.gitignore`.

## Known metadata gaps

- 49 public dataset notes lack verified license evidence.
- 67 public dataset notes lack a normalized `access` detail field.
- The 76 manufacturing-scope dataset candidates and 142 synthesis-impact candidates are automated pre-screen results and require manual scope, eligibility, and outcome verification.
- `CITATION.cff` uses the entity “Repository contributors” until the final contributor list is supplied.

These are release warnings rather than concealed defaults: missing license evidence never means unrestricted reuse, and missing access detail never changes a dataset's source-note evidence.

## Duplicate display titles

Three intentional or transitional title collisions remain while all links resolve deterministically:

- `Mean Absolute Error` exists as an emerging and a promoted metric; the promoted metric is canonical for unqualified links.
- `Normalized Change` exists as a metric note and as a source-paper note.
- `Open Stamped Parts Dataset` exists as a dataset note and as its dataset paper note.

## Public-release hygiene

No raw paper PDFs, dataset archives, files larger than 50 MiB, or machine-specific absolute paths occur in the public tree. Per-user Obsidian state and license-unverified Agent Skill copies are excluded by `.gitignore`.
