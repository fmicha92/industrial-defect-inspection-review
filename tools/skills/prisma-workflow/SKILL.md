---
name: prisma-workflow
description: Track PRISMA-style literature-review records, deduplication, title-and-abstract screening, full-text retrieval, eligibility decisions, flow counts, and machine-readable exports in this repository.
---

# PRISMA Workflow

Use this skill when the evidence review needs an auditable screening ledger. It records decisions; it does not decide eligibility automatically.

## Workflow

Run from the repository root:

```bash
python tools/skills/prisma-workflow/scripts/prisma_review.py init \
  "Which synthesis-supported inspection studies use the registered public datasets?" \
  --out-dir evidence/review/sessions

python tools/skills/prisma-workflow/scripts/prisma_review.py import-openalex \
  evidence/review/sessions/<session-directory> search-results.json \
  --source openalex

python tools/skills/prisma-workflow/scripts/prisma_review.py dedup \
  evidence/review/sessions/<session-directory>

python tools/skills/prisma-workflow/scripts/prisma_review.py screen \
  evidence/review/sessions/<session-directory> \
  --include ID1,ID2 \
  --exclude ID3="No explicit data synthesis"

python tools/skills/prisma-workflow/scripts/prisma_review.py fulltext \
  evidence/review/sessions/<session-directory> \
  --retrieved ID1,ID2 \
  --exclude ID2="No downstream inspection evaluation"

python tools/skills/prisma-workflow/scripts/prisma_review.py include \
  evidence/review/sessions/<session-directory> --include ID1

python tools/skills/prisma-workflow/scripts/prisma_review.py flow \
  evidence/review/sessions/<session-directory>

python tools/skills/prisma-workflow/scripts/prisma_review.py checklist \
  evidence/review/sessions/<session-directory>

python tools/skills/prisma-workflow/scripts/prisma_review.py export-csv \
  evidence/review/sessions/<session-directory>
```

## Session layout

Each session under `evidence/review/sessions/<slug>/` contains persistent state, normalized records, a decision log, and exports. Keep IDs stable and retain exclusion reasons.

## Decision rules

- Deduplicate before screening; preserve the canonical record and `duplicate_of` link.
- Apply the criteria in `evidence/review/protocol/eligibility_criteria.md` consistently.
- Use one primary exclusion reason at each stage.
- Treat `evidence/graph/exports/synthesis_impact_candidates.csv` as a discovery aid, not an inclusion list.
- Record full-text retrieval failures separately from eligibility exclusions.
- Do not overwrite prior decisions without leaving an audit-trail event.
- Export flow counts only after checking that record-state combinations are internally consistent.
