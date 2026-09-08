---
title: "Normalized change"
aliases:
  - "Normalized Change"
paper_key: "marx2007normalized"
citation_key: "marx2007normalized"
paper_type: other
year: 2007
venue: "American Journal of Physics"
authors:
  - "Jeffrey D. Marx"
  - "Karen Cummings"
status: processed
processed_at: 2026-06-30
topics:
  - "physics education research"
  - "pre-post assessment"
tasks:
  - "[[Pre-post diagnostic assessment]]"
domains:
  - "physics education"
methods:
  - "[[Normalized change]]"
metrics:
  - "[[Normalized change]]"
primary_metric: "[[Normalized change]]"
metric_definitions:
  - "For post > pre, c = (post - pre) / (100 - pre); for post < pre, c = (post - pre) / pre; for equal scores, c = 0 except matched 0% or 100% cases, which are dropped."
baselines:
  - "[[Normalized gain]]"
doi: "10.1119/1.2372468"
url: "http://dx.doi.org/10.1119/1.2372468"
pdf: "paper-inbox/10_processed/Other/2007 - Marx - Normalized change.pdf"
code: "not applicable"
data: "not reported"
related_concepts:
  - "[[Normalized change]]"
  - "[[Normalized gain]]"
related_methods:
  - "[[Normalized change]]"
related_tasks:
  - "[[Pre-post diagnostic assessment]]"
related_papers:
  - "[[1998 - Interactive-engagement versus Traditional Methods]]"
source_file: "paper-inbox/10_processed/Other/2007 - Marx - Normalized change.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2007 - Marx - Normalized change.md"
extracted_text: "paper-inbox/90_processing/text/2007 - Marx - Normalized change.txt"
artifact_status: "paper available; code not applicable; data not reported"
bibtex: |
  @article{marx2007normalized,
    title={Normalized change},
    author={Marx, Jeffrey D and Cummings, Karen},
    journal={American Journal of Physics},
    volume={75},
    number={1},
    pages={87--91},
    year={2007},
    publisher={AIP Publishing}
  }
tags:
  - paper
---

# Normalized change

## Summary

- Marx and Cummings propose normalized change, `c`, for measuring changes between pre-test and post-test diagnostic scores in physics education.
- The paper argues that the commonly used normalized gain has low-test-score bias, asymmetric negative ranges, and undefined cases for perfect pre-test scores.
- The proposed statistic measures gains relative to maximum possible gain and losses relative to maximum possible loss, yielding values from -1 to +1 except for matched 0% or 100% cases that are removed.

## Paper Type

- Type: other.
- Why: The article is a physics education research methods paper about score-change measurement, not an ML paper, dataset paper, benchmark, review, or system.

## Problem

- Task: [[Pre-post diagnostic assessment]].
- Setting: Conceptual diagnostic exams administered before and after instruction.
- Inputs: Matched pre-test and post-test scores expressed as percentages.
- Outputs: A normalized score-change statistic for individuals and groups.
- Motivation: Normalized gain is widely used but behaves poorly when post-test scores decrease or when pre-test scores are 100%.
- Assumptions: Pre-test and post-test scores are matched at the student level when averaging individual normalized changes.

## Contribution

- Claimed: Normalized change provides a more robust and descriptive measurement than normalized gain for pre/post diagnostic score changes.
- Shown: The paper derives a piecewise statistic, gives numerical examples, compares it against normalized gain, and proposes uncertainty and plotting practices for comparing class-level averages.
- Inferred: The statistic is mainly useful when score decreases, ceiling cases, or individual-level matched data make normalized gain hard to interpret.

## Method

- Core idea: Treat improvement and decline symmetrically by normalizing gains by maximum possible gain and losses by maximum possible loss.
- Formula:
  - If `post > pre`: `c = (post - pre) / (100 - pre)`.
  - If `post < pre`: `c = (post - pre) / pre`.
  - If `post = pre`: `c = 0`, except matched `0` or `100` scores are dropped.
- Group statistic: Compute each student's `c` and report the average normalized change, `c_ave`.
- Uncertainty: Use the standard deviation of individual `c` scores as a coarse spread measure and `sem_c = sigma_c / sqrt(N)` as a conservative uncertainty for the mean.
- Visualization: Plot `c_ave` against average pre-test score, with uncertainty bars, rather than directly adapting the Hake plot.

## ML / DL Extraction

### Task Formulation

- Input modality: Numeric pre-test and post-test scores.
- Output target: Normalized score-change value.
- Supervision: not applicable.
- Objective: Characterize conceptual learning change while avoiding normalized-gain pathologies.

### Model And Training

- Model family: not applicable.
- Architecture: not applicable.
- Parameters: not applicable.
- Pretraining: not applicable.
- Fine-tuning: not applicable.
- Losses: not applicable.
- Optimizer: not applicable.
- Hyperparameters: not applicable.
- Seeds: not applicable.
- Training compute: not applicable.

### Data

- Datasets: illustrative pre-test/post-test score table with 20 examinees.
- Data source: constructed example in the paper; prior physics education diagnostic contexts are discussed.
- Dataset size: 20 examinees in the illustrative table.
- Labels / annotations: not applicable.
- Splits: not applicable.
- Preprocessing: remove matched 0%/0% and 100%/100% cases from normalized-change calculation.
- Augmentation: not applicable.
- Synthetic data: not applicable.
- Leakage checks: not applicable.
- License: not reported.

### Evaluation

- Protocol: Analytical comparison of normalized gain and normalized change across score combinations, plus an illustrative table.
- Used performance metrics: [[Normalized change]], normalized gain, standard deviation of `c`, standard error of the mean for `c`.
- Primary metric: [[Normalized change]].
- Metric definitions: `c` normalizes improvement by remaining possible gain and decline by possible loss.
- Metric direction / units: Ranges from -1 to +1; higher values indicate more positive change.
- Baselines: Normalized gain `g = (post - pre) / (100 - pre)` and normalized gain of class averages.
- Benchmarks: not applicable.
- Statistical tests: The paper cautions that `c` values need not be normally distributed and does not prescribe normality-based tests.
- Failure cases: Matched 0%/0% and 100%/100% scores are excluded because the assessment cannot measure change for those cases.

## Evidence

### Experimental Setup

- Datasets: An illustrative table of 20 pre-test/post-test pairs.
- Splits: not applicable.
- Baselines: Normalized gain.
- Used performance metrics: `g`, `c`, `c_ave`, normalized change of averages, standard deviation of `c`, and `sem_c`.
- Compute: not applicable.
- Hardware: not applicable.
- Training time: not applicable.
- Inference cost: not applicable.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---|---|---|
| Normalized change avoids low pre-test score bias | Pre/post diagnostic scores | `c` range | higher is better for learning gain | normalized gain ranges from negative infinity to +1 | `c` ranges from -1 to +1 | The paper shows equal minimum possible `c` across pre-test values. |
| Average individual normalized change is preferred | 20-examinee illustrative table | `c_ave` | higher is better for learning gain | normalized change of averages = 0.19 | `c_ave` = 0.24 | The paper argues individual averaging better reflects matched score changes. |
| Spread and uncertainty can be reported | 20-examinee illustrative table | `sigma_c`, `sem_c` | lower uncertainty is better | not reported | `sigma_c` = 0.48, `sem_c` = 0.11 | The paper treats these as conservative descriptive statistics, not normal-distribution claims. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Normalized change]] | Pre/post diagnostic score change | Piecewise ratio of actual gain or loss to possible gain or loss | higher values indicate more positive change | yes | Ranges from -1 to +1 except excluded matched 0% or 100% cases. |
| Normalized gain | Baseline comparison | `(post - pre) / (100 - pre)` | higher values indicate more positive gain | no | Can be undefined or less than -1 when post-test performance declines. |
| Standard error of the mean for `c` | Uncertainty of `c_ave` | `sigma_c / sqrt(N)` | lower means less uncertainty | no | Presented as conservative because `c` values need not be normally distributed. |

### Ablations

- not applicable.

## Dataset / Benchmark Details

- Source: Illustrative pre/post score table in the paper.
- Collection: not reported.
- Annotation: not applicable.
- Size: 20 examinees in the illustrative example.
- Splits: not applicable.
- Modalities: numeric test scores.
- License: not reported.
- Leakage risks: not applicable.
- Bias / coverage: The paper states the example was chosen to highlight differences between methods, not to mimic typical administrations.
- Maintenance: not applicable.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Divisions between low, medium, and high `c_ave` regions are arbitrary and vary by diagnostic instrument.
- Stated: Individual `c` values need not be normally distributed, so common tests for differences between means may be difficult to interpret.
- Stated: Standard deviation of `c` is a coarse depiction of spread and should not be interpreted as a normal-distribution interval.
- Inferred: The proposal relies on matched individual pre/post scores when reporting `c_ave`.

## Reproducibility

- Code: not applicable; Appendix A gives a spreadsheet formula.
- Data: not reported beyond the illustrative table.
- Hyperparameters: not applicable.
- Random seeds: not applicable.
- Environment: spreadsheet calculation is described for Excel.
- Checkpoints / models: not applicable.
- Exact preprocessing: Drop matched 0%/0% and 100%/100% cases before averaging normalized changes.
- Artifact status: Paper available; reusable data/code artifacts not reported.

## Connections

### Graph Hubs

- Tasks: [[Pre-post diagnostic assessment]]
- Methods: [[Normalized change]]
- Metrics: [[Normalized change]]
- Datasets: not applicable
- Domains: physics education

### Shares metric

- [[Normalized change]] - the paper introduces this score-change metric and recommends it as the primary statistic for pre/post diagnostic assessments.
- [[Normalized gain]] - the paper modifies Hake's normalized-gain formulation by treating score increases and decreases with separate denominators.

### Shares task

- [[Pre-post diagnostic assessment]] - the statistic is designed for interpreting matched pre-test and post-test diagnostic exam scores.

### Contrasts with

- [[Normalized gain]] - the paper argues normalized gain has low pre-test score bias, asymmetric negative values, and undefined ceiling-score cases.

### Builds on

- [[1998 - Interactive-engagement versus Traditional Methods]] - the normalized change paper starts from the normalized gain statistic popularized by Hake's mechanics-course survey.

## Questions

- How often does normalized change materially alter conclusions in large empirical physics education datasets compared with normalized gain?
- Which nonparametric or resampling procedures are best suited for comparing `c_ave` values across instructional groups?
