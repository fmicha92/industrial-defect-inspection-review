---
name: paper-semantic-relations
description: Find new scientific papers related to existing Obsidian vault concepts, datasets, methods, tasks, domains, or keywords while excluding papers already present in the vault. Use when the user asks for more papers like the current graph, papers using a specific dataset, follow-up candidates, or literature expansion grounded in vault metadata.
---

# Paper Semantic Relations

Use this skill to discover new papers from the current Obsidian research graph.
The workflow starts from vault evidence, builds a search profile, queries
OpenAlex, and excludes papers already represented in `evidence/graph/vault/Papers/`.

## Workflow

Run commands from the project root.

### 1. Profile the vault term

```bash
python3 tools/skills/paper-semantic-relations/scripts/paper_semantic_relations.py profile "MVTec AD" --relation dataset
```

Use `--relation` to state the intended meaning when known:
`dataset`, `method`, `task`, `domain`, `metric`, `concept`, or `auto`.

The profile reports matching graph notes, existing papers linked to the term,
co-occurring datasets/tasks/methods/domains/metrics, and already-known IDs.

### 2. Search for new candidates

```bash
python3 tools/skills/paper-semantic-relations/scripts/paper_semantic_relations.py search "MVTec AD" \
  --relation dataset --year 2020- --limit 40 --min-citations 25 --open-access
```

The search output is JSON with:

- `profile` - vault matches and relation context.
- `queries` - OpenAlex queries generated from the keyword plus vault context.
- `candidates` - deduplicated papers not already present in `evidence/graph/vault/Papers/`.
- `excluded_existing` - matches removed because they were already in the vault.

For requests asking for **new** papers, recommendations, additions, or vault
expansion, this search helper is mandatory. Do not present final suggestions
from raw `scholar-search` output until they have passed this vault-aware
exclusion step.

### 3. Screen before processing

Present a compact table sorted by relevance score, then citations:

```text
score | citations | year | venue | title | OpenAlex | why it matches | IDs
```

For every candidate suggestion, include a Markdown hyperlink to OpenAlex when
possible. Prefer the `openalex_url` field; if it is missing but `paper_id` is an
OpenAlex work ID, link to `https://openalex.org/<paper_id>`. If no OpenAlex ID
is available, write `not available`.

Unless the user explicitly asks for older or lower-citation papers, candidate
suggestions must be from 2020 or newer and have at least 25 citations.

Keep only papers whose title, abstract, venue, or metadata directly supports the
requested relation. For example, if the user asks for papers using dataset X,
do not include papers that merely cite a similarly named method unless the
abstract or metadata shows dataset use.

Before showing the final table, verify that every row came from `candidates`,
not `excluded_existing`. If you manually merge in results from another search,
run the same duplicate screen against existing paper notes first.

### 4. Hand off selected papers

For papers the user wants to add:

1. Prefer `open_access_pdf` when available; otherwise use `landing_url`.
2. Place source files in `workspace/paper-inbox/00_incoming/`.
3. Use `paper-preprocessing` and `paper-processing` for final Obsidian notes.

For dataset hosts the user wants to add:

1. Use the canonical host URL, such as Kaggle, GitHub, IEEE DataPort, Zenodo,
   Hugging Face, or an institutional repository.
2. Do not place the host page in `workspace/paper-inbox/` unless downloading files for
   local analysis is explicitly needed.
3. Use `paper-processing`'s dataset web source workflow to create or update the
   dataset note. The note must include the host URL in frontmatter and body
   prose. It must also link the most relevant paper that introduces the dataset
   when one exists, using an internal paper note when available and an external
   paper URL otherwise.

## Query Strategy

The helper builds several bounded queries:

- exact keyword
- keyword plus relation word, such as `dataset` or `benchmark`
- keyword plus high-signal co-occurring tasks, methods, domains, or metrics
- matching graph-note aliases when available

Keep query expansion conservative. More candidates are useful only if they can
still be screened against the relation requested by the user.

## Exclusion Rules

Treat a result as already known if any of these match an existing paper note:

- DOI
- arXiv ID
- OpenAlex work ID
- normalized title
- normalized paper-note filename or alias
- high-confidence fuzzy title match

Do not fabricate missing IDs. If metadata is absent, rely on title and alias
matching. If a candidate is a fuzzy near-match to an existing note, exclude it
or explicitly label it as a possible duplicate rather than presenting it as new.

## Hard Rules

- Ground expansion in current vault files and OpenAlex result metadata.
- Never claim a suggestion is new unless it passed duplicate exclusion against
  `evidence/graph/vault/Papers/` by DOI, arXiv ID, OpenAlex ID, title, filename, alias, and
  fuzzy title match.
- Default new-paper suggestions to 2020+ and 25+ citations unless the user
  specifies a different year or citation threshold.
- Do not claim a candidate uses a dataset, method, or task unless its metadata
  supports that relation.
- Do not add papers to the vault from search results alone; process them through
  `paper-preprocessing` and `paper-processing`.
- If the relation is ambiguous, run `profile` first and ask the user which
  sense they mean before a broad search.
- Preserve the distinction between "semantically related", "uses the same
  dataset", "shares task", "shares method", and "follow-up citation".
