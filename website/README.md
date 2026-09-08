# Industrial Inspection Evidence Explorer

The **website** directory contains the static companion site for “Synthetic Data for Machine Learning in Industrial Visual Defect Inspection: A Review Centered on Public Datasets.”

The site helps readers move between public manufacturing datasets, synthesis-supported evaluations, downstream tasks, model families, metrics, comparator conditions, and the linked evidence graph. It is an evidence-navigation interface, not a model leaderboard or a new scientific evaluation.

All paths in this document are relative to **website/** unless they are explicitly identified as repository-level files.

## Scientific scope

The checked-in website assets present:

- 61 public-dataset records across seven manufacturing-domain groups;
- 92 non-exclusive dataset-to-task assignments;
- 39 dataset-level synthesis evaluations, E01–E39, from 37 unique publications;
- a graph snapshot containing 896 notes, including 226 paper notes, and 8,926 resolved directed wikilinks dated 2026-08-27.

The dataset registry, evidence collection, and graph are related but distinct scopes. A graph record is not automatically an included review record. Candidate flags remain navigation aids that require manual confirmation.

The website does not generate experiments, metrics, effect sizes, rankings, quality scores, significance tests, or scientific conclusions. Existing values and interpretations are displayed as supplied by the checked-in assets.

## Exploring the evidence

- **Explorer:** start with the full graph, search records, inspect incoming and outgoing connections, pin records, and trace a shortest directed wikilink path. Choose a local neighborhood to focus on one record. The table provides a keyboard-accessible alternative to the canvas.
- **Datasets:** inspect domain/task coverage and citation trends, search and filter the complete registry, compare up to three datasets, and open linked graph records.
- **Evidence:** inspect all 39 comparisons on one page, filter the records, and select chart points to inspect their study context. The normalized-change distribution and supplied family summaries are directly visible and remain based on the complete retained set.
- **Review logic:** navigate the research questions, evaluation framework, normalized-change definition, limitations, recommendations, and reference downloads.

Dataset and evidence filters are retained in the URL. Cross-links preserve the distinction between complete datasets, documented subsets, and multi-dataset comparisons.

## Website contents

| Path | Purpose |
|---|---|
| src/ | React pages, components, chart logic, graph interaction, data loading, and shared styles |
| public/data/ | Versioned JSON bundles used by the interface |
| public/downloads/ | Existing CSV reference tables offered through the download panel |
| public/.nojekyll | Prevents GitHub Pages from applying Jekyll processing |
| scripts/ | Static page generation, deployment checks, and optional data-maintenance utilities |
| package.json | Commands and direct dependency declarations |
| pnpm-lock.yaml | Reproducible dependency resolution |
| vite.config.ts | Project-path production configuration and static route generation |
| DATA_PROVENANCE.md | Inventory and handling rules for website data |
| SCIENTIFIC_CONTENT_AUDIT.md | Claim-to-asset traceability and interpretation constraints |
| THIRD_PARTY_NOTICES.md | Dependency and content notices |

## Local development

Requirements:

- Node.js 22;
- pnpm 11.19.0.

From the repository root:

    cd website
    npm install --global pnpm@11.19.0
    pnpm install --frozen-lockfile
    pnpm dev

The development server binds to 127.0.0.1.

## Verification

Run the complete check sequence from **website/**:

    pnpm lint
    pnpm typecheck
    pnpm test
    pnpm build
    pnpm check:pages
    pnpm preview

The production output is written to **dist/**. That directory is generated and should not replace the maintained website source.

The production preview uses `/industrial-defect-inspection-review/`, matching GitHub Pages. Open the project-path URL printed by `pnpm preview`. Development with `pnpm dev` uses `/`.

`pnpm check:pages` serves the built files under the repository path without an application fallback. It checks all four routes, query-bearing links, directory redirects, scripts, styles, lazy graph assets, and downloads. It also checks that public files match the committed inputs and that no LaTeX source files are published.

Verification should preserve these invariants:

- all 61 dataset records and E01–E39 are present exactly once;
- the unfiltered evidence table shows all 39 records without pagination;
- the normalized-change distribution is visible without expanding a section;
- a fresh Explorer route opens the full graph, while explicit local links preserve their scope;
- no LaTeX source files are present in public/ or dist/;
- all graph edges reference existing nodes;
- supplied numeric values and identifiers remain unchanged;
- missing citation values remain missing rather than becoming zero;
- candidate records are not presented as included evidence;
- normalized change and other scientific results are not recomputed;
- external URLs are sanitized before use;
- no credentials, machine-specific paths, private notes, dataset archives, or publication full text enter the public build.

## Checked-in data

The application reads its scientific content from **public/data/**. CSV reference tables in **public/downloads/** and the registry and evidence JSON bundles are available for download. LaTeX source files are not served by the website. Normal development and GitHub Pages builds use these committed files directly.

The central interpretation rule is to preserve the condition around every reported result. Dataset, task, annotation, synthesis setup, model, metric, and comparator remain visible together. Normalized change supports consistent display of bounded, positively oriented metrics but does not make different tasks or metrics equivalent.

See [DATA_PROVENANCE.md](DATA_PROVENANCE.md) and [SCIENTIFIC_CONTENT_AUDIT.md](SCIENTIFIC_CONTENT_AUDIT.md) for the website-level data contract.

### Optional data maintenance

`pnpm prepare:data` is a separate maintenance command, not a prerequisite for running or building the site. It reads existing source material and writes the website bundles and reference downloads. Do not run it as part of ordinary verification or use it to generate new scientific evaluations.

By default, it expects the repository's `evidence/graph/exports/` and the following inputs under the repository-level `evidence/review/publication/` directory:

| Directory | Required files |
|---|---|
| tables/ | dataset_registry.tex, synthesis_impact_longtable.tex, dataset_source_citation_trends.tex |
| data/ | synthesis_impact_normalized_change.csv, table3_baseline_after_synthesis.csv, dataset_citation_counts_wide_2020_2025_all_domains.csv |
| figures/ | fig_dataset_task_coverage_matrix_final.tex |
| manuscript/ | library.bib |

Only some publication inputs are included in the repository; the website does not bundle LaTeX source files. If any required input is unavailable, the command reports the missing files before reading source content or writing output. The committed website assets remain sufficient for all standard checks and GitHub Pages builds.

## GitHub Pages

The repository-level workflow **.github/workflows/website-pages.yml**:

1. installs the pinned package manager;
2. installs dependencies from the lockfile;
3. runs linting, type checking, and tests;
4. builds the website, including an `index.html` for every route;
5. verifies the static routes and public assets;
6. uploads **website/dist** as the GitHub Pages artifact.

The production base and browser router use `/industrial-defect-inspection-review/`. The public site is available at:

    https://fmicha92.github.io/industrial-defect-inspection-review/

The build produces `index.html`, `datasets/index.html`, `evidence/index.html`, and `review/index.html`. Each entry loads the interactive application, so the clean `/datasets/`, `/evidence/`, and `/review/` URLs support direct visits and refreshes on GitHub Pages without a rewrite rule or a custom 404 redirect. Scripts, lazy chunks, data, and downloads use the same repository base path.

Filters, selected records, and shared graph state use normal query parameters. Existing `#/` bookmarks are recognized on startup and converted to their clean equivalent, preserving their query values. The deployed artifact is the contents of **website/dist**, not the unbuilt source directory; the public URL has no `/website/` suffix.

In the repository settings, select **Pages → Build and deployment → Source: GitHub Actions**. Pushes to **main** that change the website or its Pages workflow trigger deployment automatically. The workflow may also be started manually from the Actions tab.

## Citation and reuse

Use the repository’s **CITATION.cff** and release metadata when citing the project. Do not infer a DOI, archived-release URL, or contributor list that is not present there.

Repository code, documentation, graph material, third-party software, bibliographic metadata, and linked dataset records may have different license conditions. Public access to a dataset does not imply permission to redistribute its files. Review the repository license files and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before reuse.
