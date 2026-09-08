# Scientific content audit

## Audit rule

Every scientific statement and plotted value on the website must be traceable to a checked-in asset beneath **public/data/** or **public/downloads/**. The interface may improve navigation and presentation; it must not extend the review with a new evaluation.

All paths in this document are relative to **website/**.

## Approved scope statements

| Website statement | Website evidence | Presentation constraint |
|---|---|---|
| 61 public datasets across seven manufacturing-domain groups | public/data/datasets.json and public/data/meta.json | Describe the curated registry, not every graph dataset node |
| 92 non-exclusive dataset-task assignments | public/data/task-coverage.json | A multi-task dataset may contribute to multiple task columns; 92 is not a dataset count |
| 39 dataset-level evaluations from 37 unique publications | public/data/evidence.json | Keep evidence-entry and publication counts distinct |
| Evidence identifiers E01–E39 | public/data/evidence.json | Use the identifier as the stable cross-reference |
| Median normalized change 0.43; Q1–Q3 0.20–0.66; mean 0.45; sample SD 0.29 | public/data/evidence.json | Present as supplied review statistics; do not recalculate them |
| All 39 representative normalized-change values are positive | public/data/evidence.json | Pair with the retained-positive-evidence caveat; never call this a success rate |
| 896 graph notes and 8,926 resolved directed wikilinks dated 2026-08-27 | public/data/graph.bundle.json and public/data/meta.json | Treat the graph as a navigation layer, not a quantitative evidence ranking |

The seven registry groups are semiconductor and electronics, solar cells and photovoltaic modules, metals, textiles, glass, automotive components, and multi-industry anomaly benchmarks.

## View-to-asset traceability

| Website view | Checked-in assets | Allowed interaction |
|---|---|---|
| Dataset registry | public/data/datasets.json | Search, filter, compare supplied fields, and follow documented links |
| Domain/task coverage | public/data/task-coverage.json and public/data/datasets.json | Filter, focus, tooltip, and accessible table; no new coverage score |
| Baseline-versus-after scatter | public/data/evidence.json | Focus by EID, filter by supplied categories, and show the no-change diagonal |
| Normalized-change distribution | public/data/evidence.json | Inspect supplied representative values; no fitted model, confidence band, or dynamic summary |
| Normalized change by synthesis family | public/data/evidence.json | Group by supplied family; no winner claim |
| Synthesis-family-by-domain matrix | public/data/evidence.json | Filter the corresponding records; cell counts describe evaluations, not effect strength |
| Citation trajectories | public/data/citation-trends.json | Inspect supplied yearly values; blanks remain missing |
| Evidence graph | public/data/graph.bundle.json | Search, filter, select, and trace directed paths; no importance or causality calculation |

Every visual mark must expose the evidence identifier or dataset record that produced it. Charts and the graph provide text or table alternatives for inspection without relying solely on visual position.

## Evidence-record audit

The published evidence bundle contains:

- 39 unique evidence identifiers, E01–E39;
- 39 dataset-level evaluation records;
- 37 unique publications;
- one representative metric comparison per evidence record.

Methods and comparators for the representative comparisons are available in the detailed record view and the downloadable **public/data/evidence.json** bundle.

Each record keeps dataset, task, annotation, synthesis setup, comparator, model information, metric, baseline, after value, and normalized change together where those fields are supplied.

Some publications contribute more than one dataset-level entry. Those records must remain separate rather than being deduplicated by publication.

## Normalized-change interpretation

Normalized change is a supplied, direction-aware representation for bounded metrics. It does not make accuracy, F1, AP, mAP, IoU, mIoU, AUROC, classification, detection, segmentation, localization, and anomaly-detection outcomes scientifically interchangeable.

Display precision has a presentation role:

- precise evidence fields retain the supplied higher-precision value;
- table and chart labels may use the supplied display precision;
- neither representation may be recreated from rounded baseline and after values.

The interface must not dynamically recompute means, medians, quartiles, uncertainty intervals, or significance statistics after filtering.

## Required interpretation notice

The evidence views must keep an equivalent of this interpretation readily available:

The collection retains positive, interpretable published comparisons and therefore does not estimate how often synthesis succeeds in industrial inspection overall. The 39 entries combine different datasets, tasks, metrics, models, annotation levels, and comparator designs; some publications contribute more than one dataset-level entry. Normalized change supports a consistent display scale but does not make the underlying tasks or metrics equivalent. Public-dataset findings do not by themselves establish transfer to factory deployment.

Additional constraints:

- the records do not share a common sampling design, uncertainty estimate, test-set size, or repeated-trial structure;
- comparator quality and intervention scope vary;
- multiple metrics from one publication must not give that publication extra analytic weight;
- some hybrid results combine synthesis with other pipeline changes;
- citation counts describe publication visibility, not dataset use, benchmark quality, or synthesis relevance;
- blank citation values mean missing data, not zero.

## Labels and mappings

Use the exact labels and supplied compact categories carried by the website bundles.

Do not derive:

- a primary task from a multi-task label;
- a primary synthesis family from punctuation or keywords;
- a dataset-to-evidence relationship from name similarity;
- a publication title, DOI, or URL from an unmatched citation key;
- an inclusion decision from a candidate flag.

Links between records require a stable identifier or an explicitly supplied mapping. Subsets, aliases, selected classes, and multi-dataset entries remain distinct unless the website data provides the relationship directly.

## Graph interpretation

Graph layout, degree, direction, and neighborhood size support exploration only. A directed wikilink is not necessarily a citation, endorsement, causal relation, performance dependency, or quality judgment.

The website may highlight:

- the selected record;
- directly connected records;
- incoming and outgoing directions;
- pinned records;
- a shortest directed wikilink path.

It must not present graph centrality, clusters, or layout position as scientific findings.

## Prohibited claims

The website must not present:

- a globally best dataset, model, metric, or synthesis family;
- a ranking by normalized change across heterogeneous tasks;
- a synthesis success rate inferred from the retained positive entries;
- dynamic scientific summaries for a filtered subset;
- new effect-size calculations;
- new evidence-strength, reproducibility, readiness, or quality scores;
- graph centrality or communities as evidence;
- candidate records as included evaluations;
- missing citation values as zero;
- a publicly accessible dataset as freely redistributable without license evidence.

## Release checklist

Before publication, verify:

- all 61 dataset records are present exactly once;
- E01–E39 are present exactly once in the evidence bundle and all 39 rows appear in the unfiltered evidence table;
- the normalized-change distribution is directly visible without expanding a disclosure;
- downloads contain JSON and CSV reference files, not LaTeX sources;
- the evidence bundle still reports 37 unique publications;
- numeric values and category labels match the checked-in assets;
- every visual mark links to a record;
- secondary metrics do not enter representative charts;
- graph candidate flags remain distinct from review inclusion;
- missing citation values remain missing;
- external URLs are sanitized;
- keyboard access, visible focus, reduced motion, and table alternatives remain functional;
- clean routes, query-bearing links, legacy bookmarks, and assets work beneath the GitHub project path;
- no credentials, machine-specific paths, private notes, publication full text, or dataset archives are published;
- unresolved citation and license information remains explicitly unresolved.
