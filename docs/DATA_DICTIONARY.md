# Data dictionary

## Vault notes

Each Markdown note may begin with YAML frontmatter. The exporter reads top-level scalar and list properties; nested mappings and body text remain available to human readers but are not flattened automatically.

Common fields are:

| Field | Meaning |
|---|---|
| `title` | Display title; filename is the fallback |
| `aliases` | Alternative names used for matching and navigation |
| `status` | Processing state, commonly `processed` for completed paper notes |
| `paper_key` | Stable local identifier such as DOI, arXiv ID, OpenAlex ID, or source hash |
| `paper_type` | Research, review, dataset, benchmark, systems, or other |
| `year`, `venue`, `authors` | Bibliographic metadata |
| `datasets`, `methods`, `tasks`, `domains`, `metrics` | Graph-aligned evidence descriptors |
| `availability`, `access` | Dataset availability and access conditions |
| `license` / `licenses` | Reported dataset license evidence; absence means unverified, not unrestricted |
| `url`, `doi`, `arxiv` | External identifiers or canonical landing pages |

Wikilinks use Obsidian syntax (`[[Target note]]`) and form the graph edges.

## Generated exports

### `nodes.csv`

One row per Markdown note. `node_id` is the extension-free path relative to the vault and is the stable repository identifier. `node_type` is the top-level vault folder.

### `edges.csv`

One deduplicated wikilink edge per source-target pair. Resolution follows path, filename, title, then alias precedence. If a promoted and an `Emerging *` note share a name, the promoted note is canonical. `resolution` is `resolved`, `ambiguous`, or `unresolved`; `target_id` is populated only for unambiguous matches.

### `dataset_registry.csv`

All dataset notes, including public, private, and availability-unspecified records. Folder placement supplies `availability_group`; frontmatter may supply more specific access and license evidence.

### `public_dataset_registry.csv`

The public subset of `dataset_registry.csv`. “Public” describes documented access, not permission to redistribute dataset files. `scope_screen` is an automated domain screen and is not a final review decision.

### `manufacturing_dataset_candidates.csv`

Public dataset notes that do not match a controlled set of clearly contextual domains (general computer vision, autonomous driving, document analysis, medical imaging, or natural-language processing). This is a broad manufacturing-scope pre-screen and requires manual confirmation.

### `paper_evidence.csv`

Bibliographic and graph-aligned fields for every paper note. Local PDF and preprocessing paths are intentionally excluded.

### `synthesis_impact_candidates.csv`

An automated pre-screen containing papers that both reference a public dataset note passing the manufacturing-scope pre-screen and contain explicit synthesis terminology in structured metadata or the note body. It supports screening but does not establish dataset scope, review eligibility, or performance evidence.

### `summary.json`

Snapshot metadata, counts, graph resolution statistics, and candidate-screen totals.

List-valued CSV cells use ` | ` as the separator. Values are de-wikilinked for interoperability while source notes preserve the original links.
