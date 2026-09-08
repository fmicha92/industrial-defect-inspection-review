# Website data provenance

## Purpose and scope

This document inventories the versioned data files contained in **website/public/** and defines how the website may present them.

The website publishes existing review records and graph metadata. It does not create new scientific data or evaluations. Filters, searches, tooltips, tables, and chart interactions expose the supplied records without changing their meaning.

All paths below are relative to **website/**.

## Runtime data assets

| Asset | Website use |
|---|---|
| public/data/datasets.json | Public-dataset records, domains, tasks, annotations, modalities, resolution, sample composition, bibliography, and registry summary |
| public/data/task-coverage.json | Supplied domain-by-task assignments and totals |
| public/data/citation-trends.json | Supplied 2020–2025 citation series and missing-value semantics |
| public/data/evidence.json | E01–E39 evidence details, supplied summary values, and interpretation text |
| public/data/graph.bundle.json | Graph nodes, directed edges, type counts, snapshot metadata, and candidate flags |
| public/data/meta.json | Website title, authorship display, snapshot labels, and headline counts |
| public/data/provenance.json | Publication-time fingerprints, recorded transformations, validated invariants, and generated-data policy |

These JSON files are committed website inputs. The production build bundles the application around them but does not regenerate their scientific values.

## Download assets

The website provides these checked-in reference files:

| Asset | Contents |
|---|---|
| public/data/datasets.json | Public-dataset records and descriptions |
| public/data/evidence.json | Representative evidence records, methods, and comparators |
| public/downloads/synthesis_impact_normalized_change.csv | Supplied precise representative values and normalized change |
| public/downloads/table3_baseline_after_synthesis.csv | Supplied plotting values and categories |
| public/downloads/dataset_citation_counts_wide_2020_2025_all_domains.csv | Supplied yearly citation series |

The download copies support inspection and traceability. Their inclusion does not change copyright, attribution, or dataset-redistribution conditions.

## Published snapshot

The checked-in bundles report:

| Collection | Published website state |
|---|---:|
| Public-dataset records | 61 |
| Manufacturing-domain groups | 7 |
| Non-exclusive task assignments | 92 |
| Dataset-level evidence entries | 39 |
| Unique publications represented by evidence entries | 37 |
| Graph notes | 896 |
| Graph paper notes | 226 |
| Resolved directed wikilinks | 8,926 |
| Graph snapshot date | 2026-08-27 |
| Graph schema version | 1.0.0 |

Task assignments are non-exclusive: one dataset may support multiple tasks. Evidence entries are dataset-level records, so one publication may contribute more than one entry.

## Evidence-value contract

Each evidence record keeps the following context together:

- evidence identifier;
- publication identifier;
- dataset and manufacturing domain;
- task and annotation;
- synthesis family and setup;
- comparator;
- model or architecture where supplied;
- representative metric, baseline, after value, and normalized change.

The detailed record view and **public/data/evidence.json** expose the supplied methods and comparators for each representative comparison. The website serves JSON and CSV reference files, not LaTeX source files.

The website displays the supplied baseline, after, and normalized-change values. It does not recompute normalized change from rounded display numbers. Supplied categories remain authoritative for grouping; the interface does not infer a primary category from free text.

E01–E39 are stable public cross-references. Dataset names or metric labels are not substitutes for those identifiers.

## Permitted presentation operations

The website may:

- load and validate the shape of checked-in JSON;
- filter and sort records without altering them;
- search titles, aliases, and stable identifiers;
- group records using supplied categories;
- count records currently visible in an interface view;
- render the supplied values as charts, tables, cards, and graph elements;
- preserve a selected view in the URL;
- provide the checked-in reference files for download.

Visible-record counts are navigation aids, not new scientific summary statistics.

## Prohibited derivations

The website must not:

- recalculate normalized change or substitute a newly rounded value;
- pool incompatible metrics;
- calculate new means, medians, quartiles, confidence intervals, regressions, significance tests, effect sizes, or rankings;
- create evidence-strength, reproducibility, readiness, or quality scores;
- infer scientific importance from graph degree, centrality, or layout;
- turn an automated candidate flag into an inclusion decision;
- interpret a missing citation value as zero;
- treat public access as a redistribution license.

## Graph semantics

Every graph edge represents a directed wikilink between two website graph records. It is not automatically:

- a bibliographic citation;
- a causal relation;
- a performance dependency;
- an endorsement;
- a quality judgment.

The graph bundle reports zero ambiguous and zero unresolved edges for the published snapshot. Candidate flags are explicitly described as requiring manual confirmation.

## Missing values and access metadata

Missing metadata remain missing. In particular:

- blank citation values are not converted to zero;
- missing license evidence does not imply unrestricted reuse;
- a documented public-access link does not authorize redistribution of dataset files;
- unresolved bibliographic or citation metadata are not invented.

## Build and publication integrity

The normal production command is:

    pnpm build

It reads the checked-in website source and public assets, type-checks the application, and writes **dist/**. The repository’s Pages workflow uploads that generated directory.

Before publication, verify:

- all expected JSON and CSV download files are present;
- no LaTeX source files occur in public/ or dist/;
- all 61 datasets and E01–E39 occur once;
- identifiers and numeric lexemes remain unchanged;
- every graph edge endpoint exists;
- URLs use permitted protocols;
- candidate and included records remain visibly distinct;
- the build contains no credentials, machine-specific paths, private note bodies, publication full text, or dataset archives.
