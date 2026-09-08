---
title: "Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses"
aliases:
  - "Interactive-engagement versus traditional methods"
  - "Hake 1998 interactive engagement"
paper_key: "hake1998interactive"
citation_key: "hake1998interactive"
paper_type: other
year: 1998
venue: "American Journal of Physics"
authors:
  - "Richard R. Hake"
status: processed
processed_at: 2026-06-30
topics:
  - "physics education research"
  - "introductory mechanics"
  - "pre-post assessment"
tasks:
  - "[[Pre-post diagnostic assessment]]"
domains:
  - "physics education"
methods:
  - "[[Interactive engagement]]"
metrics:
  - "[[Normalized gain]]"
primary_metric: "[[Normalized gain]]"
metric_definitions:
  - "Average normalized gain is the ratio of actual average gain to maximum possible average gain: (%<post> - %<pre>) / (100 - %<pre>)."
datasets:
  - "62 introductory mechanics courses"
dataset_sizes:
  - "6542 students for MD/FCI conceptual tests; 3259 students for the Mechanics Baseline subset."
baselines:
  - "traditional introductory physics instruction"
doi: "10.1119/1.18809"
url: "http://dx.doi.org/10.1119/1.18809"
pdf: "paper-inbox/10_processed/Other/1998 - Hake - Interactive-engagement versus traditional methods A six-thousand-student survey of mechanics test data for introductory physics courses.pdf"
code: "not applicable"
data: "survey data tabulated in a companion paper; full raw dataset not reported"
related_papers:
  - "[[2007 - Normalized Change]]"
related_concepts:
  - "[[Interactive engagement]]"
  - "[[Normalized gain]]"
related_methods:
  - "[[Interactive engagement]]"
related_tasks:
  - "[[Pre-post diagnostic assessment]]"
source_file: "paper-inbox/10_processed/Other/1998 - Hake - Interactive-engagement versus traditional methods A six-thousand-student survey of mechanics test data for introductory physics courses.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/1998 - Hake - Interactive-engagement versus traditional methods A six-thousand-student survey of mechanics test data for introductory physics courses.md"
extracted_text: "paper-inbox/90_processing/text/1998 - Hake - Interactive-engagement versus traditional methods A six-thousand-student survey of mechanics test data for introductory physics courses.txt"
artifact_status: "paper available; code not applicable; raw survey data not reported"
bibtex: |
  @article{hake1998interactive,
    title={Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses},
    author={Hake, Richard R},
    journal={American journal of Physics},
    volume={66},
    number={1},
    pages={64--74},
    year={1998},
    publisher={American Association of Physics Teachers}
  }
tags:
  - paper
---

# Interactive-engagement versus traditional methods

## Summary

- Hake surveys pre/post mechanics concept-test results from 62 introductory physics courses enrolling 6542 students.
- The paper defines average normalized gain, `<g>`, as a rough measure of course effectiveness in promoting conceptual understanding across groups with different pre-test scores.
- Traditional courses averaged `<g> = 0.23 +/- 0.04`, while interactive-engagement courses averaged `<g> = 0.48 +/- 0.14`; the paper argues the difference is unlikely to be explained by systematic error.
- The paper is a direct foundation for [[2007 - Normalized Change]], which critiques and modifies the normalized-gain statistic introduced and operationalized here.

## Paper Type

- Type: other.
- Why: The article is a physics education research survey and measurement paper, not an ML research paper, dataset paper, benchmark, review, or system.

## Problem

- Task: [[Pre-post diagnostic assessment]].
- Setting: Introductory mechanics courses in high schools, colleges, and universities.
- Inputs: Course-level pre-test and post-test scores from the Mechanics Diagnostic or Force Concept Inventory; Mechanics Baseline post-test scores where available.
- Outputs: Course-level average normalized gain and comparisons between traditional and interactive-engagement instruction.
- Motivation: Earlier physics education research suggested traditional instruction produced little conceptual change in Newtonian mechanics; the survey asks whether newer interactive-engagement methods improve outcomes.
- Assumptions: Average normalized gain can serve as a rough cross-course effectiveness measure when comparing courses with diverse initial knowledge states.

## Contribution

- Claimed: Interactive-engagement courses can increase mechanics-course effectiveness well beyond traditional instruction.
- Shown: 48 interactive-engagement courses achieved more than double the average normalized gain of 14 traditional courses in the survey.
- Inferred: Normalized gain became a central comparative statistic for later physics education measurement work, including the normalized change critique in [[2007 - Normalized Change]].

## Method

- Core idea: Compare course-level pre/post conceptual test changes using average normalized gain rather than raw gain or post-test score alone.
- Survey source: Hake solicited pre/post FCI data and post-test Mechanics Baseline data through talks, meetings, and email lists beginning in 1992.
- Course classification:
  - Traditional courses used little or no interactive engagement and relied mainly on passive lectures, recipe labs, and algorithmic exams.
  - Interactive-engagement courses used methods intended to promote conceptual understanding through heads-on and usually hands-on activities with immediate feedback from peers or instructors.
- Primary statistic: `<g> = (%<post> - %<pre>) / (100 - %<pre>)`.
- Grouping: Courses were categorized as high-g (`<g> >= 0.7`), medium-g (`0.7 > <g> >= 0.3`), or low-g (`<g> < 0.3`).

## ML / DL Extraction

### Task Formulation

- Input modality: Numeric pre-test and post-test scores from mechanics diagnostic tests.
- Output target: Average normalized gain for a course.
- Supervision: not applicable.
- Objective: Estimate course effectiveness in promoting conceptual mechanics understanding.

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

- Datasets: 62 introductory mechanics courses using the Halloun-Hestenes Mechanics Diagnostic or Force Concept Inventory; 30-course Mechanics Baseline subset.
- Data source: Published accounts, unpublished classroom results, private communications, and survey questionnaire responses.
- Dataset size: 6542 students in the MD/FCI survey; 3259 students in the Mechanics Baseline subset.
- Labels / annotations: Courses were classified as traditional or interactive-engagement according to reported instructional methods.
- Splits: 14 traditional courses and 48 interactive-engagement courses for the conceptual-test analysis.
- Preprocessing: Course-level average normalized gain was computed from average pre-test and post-test scores.
- Augmentation: not applicable.
- Synthetic data: not applicable.
- Leakage checks: The paper discusses possible test-question leakage and reports suspect data were excluded when identified.
- License: not reported.

### Evaluation

- Protocol: Compare normalized-gain distributions for traditional and interactive-engagement courses; examine Mechanics Baseline post-test scores against FCI post-test scores for the subset with both tests.
- Used performance metrics: [[Normalized gain]], FCI/MD pre-test and post-test scores, Mechanics Baseline post-test score.
- Primary metric: [[Normalized gain]].
- Metric definitions: Average normalized gain is actual average gain divided by maximum possible average gain.
- Metric direction / units: Higher normalized gain indicates larger conceptual test improvement; values are dimensionless.
- Baselines: Traditional introductory mechanics instruction.
- Benchmarks: Force Concept Inventory, Mechanics Diagnostic, and Mechanics Baseline tests.
- Statistical tests: The paper uses course-group averages, standard deviations, correlations, and systematic-error analysis.
- Failure cases: Low-g interactive-engagement courses are discussed as likely implementation failures rather than evidence that all interactive-engagement methods are ineffective.

## Evidence

### Experimental Setup

- Datasets: 62 courses with MD/FCI data; 30 courses with Mechanics Baseline data.
- Splits: 14 traditional courses with 2084 students; 48 interactive-engagement courses with 4458 students.
- Baselines: Traditional courses.
- Used performance metrics: Average normalized gain, FCI/MD average scores, Mechanics Baseline average scores.
- Compute: not applicable.
- Hardware: not applicable.
- Training time: not applicable.
- Inference cost: not applicable.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Traditional courses stayed in the low-g region | 14 traditional courses, N = 2084 | [[Normalized gain]] | higher is better | not applicable | 0.23 +/- 0.04 | All traditional course points fell in the low-g region. |
| Interactive-engagement courses averaged higher gains | 48 IE courses, N = 4458 | [[Normalized gain]] | higher is better | 0.23 +/- 0.04 | 0.48 +/- 0.14 | The IE average was about 2.1 times the traditional average. |
| No surveyed course reached high-g | 62 courses | [[Normalized gain]] region | higher is better | high-g threshold 0.7 | no points in high-g region | The paper treats this as evidence that IE methods still needed improvement. |
| Mechanics Baseline and FCI post-test scores were strongly related | 30-course subset, N = 3259 | correlation coefficient | stronger positive relation supports consistency | not applicable | r = 0.91 | The paper argues problem-solving performance was not sacrificed by conceptual emphasis. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Normalized gain]] | Course-level conceptual mechanics improvement | `(%<post> - %<pre>) / (100 - %<pre>)` | higher is better | yes | The paper uses it as a rough effectiveness measure across diverse initial pre-test scores. |
| FCI/MD score | Conceptual mechanics understanding | Percent correct on concept inventories | higher is better | no | Used for pre/post conceptual testing. |
| Mechanics Baseline score | Mechanics problem solving | Percent correct on MB post-test | higher is better | no | Used for the subset where MB data were available. |

### Ablations

- not applicable.

## Dataset / Benchmark Details

- Source: Course-level results collected from published reports, unpublished reports, private communications, and survey responses.
- Collection: Data were solicited beginning in 1992 through talks, meetings, and e-mail postings.
- Annotation: Courses were labeled traditional or interactive-engagement based on reported instructional methods.
- Size: 62 courses and 6542 students for MD/FCI; 30 courses and 3259 students for Mechanics Baseline.
- Splits: 14 traditional and 48 interactive-engagement courses.
- Modalities: Numeric assessment scores and course metadata.
- License: not reported.
- Leakage risks: The paper discusses teaching to the test and test-question leakage as possible systematic errors; it reports one suspect leakage case was removed from the survey.
- Bias / coverage: The paper states data solicitation tended to pre-select unusually strong courses and was not intended to estimate average introductory mechanics effectiveness.
- Maintenance: not applicable.

## Review / Survey Details

- Scope: Introductory mechanics courses using MD/FCI pre/post testing and, where available, Mechanics Baseline testing.
- Inclusion criteria: Quantitative pre/post-test results known to the author in time for inclusion; courses with `N > 20` were plotted to improve reliability, with some smaller homogeneous sections included in weighted averages.
- Taxonomy: Traditional instruction versus interactive engagement; low-, medium-, and high-g normalized-gain regions.
- Major themes: Interactive engagement, peer discussion, conceptual testing, implementation quality, physics education research, and systematic measurement.
- Gaps: The paper calls for standardized administration practices, improved tests, independent classroom observation, and broader anonymous sampling.

## Limitations

- Stated: The survey does not estimate average introductory mechanics effectiveness because data solicitation pre-selected reported results.
- Stated: Course-level systematic errors may include question ambiguities, teaching to the test, test leakage, mechanics time allocation, student motivation, and Hawthorne or John Henry effects.
- Stated: Some interactive-engagement courses still produced low normalized gains, likely due to implementation problems.
- Stated: Normalized gain is described as a rough effectiveness measure, not a complete causal model of learning.
- Inferred: The average normalized-gain statistic compresses individual student score changes and does not directly handle score declines or ceiling cases, which motivates later work in [[2007 - Normalized Change]].

## Reproducibility

- Code: not applicable.
- Data: Course data are described as tabulated and referenced in a companion paper; raw data are not reported in this article.
- Hyperparameters: not applicable.
- Random seeds: not applicable.
- Environment: not applicable.
- Checkpoints / models: not applicable.
- Exact preprocessing: Compute course-level average normalized gain from average pre-test and post-test percentages.
- Artifact status: Paper available; reusable raw dataset not reported.

## Connections

### Graph Hubs

- Tasks: [[Pre-post diagnostic assessment]]
- Methods: [[Interactive engagement]]
- Metrics: [[Normalized gain]]
- Datasets: 62 introductory mechanics courses
- Domains: physics education

### Builds on

- Halloun-Hestenes mechanics diagnostic work - the survey uses MD/FCI tests introduced in earlier physics education research.

### Supports

- [[2007 - Normalized Change]] - Hake's average normalized gain is the measurement foundation that Marx and Cummings later modify to address decline, asymmetry, and ceiling-score cases.

### Shares metric

- [[Normalized gain]] - the paper defines and operationalizes average normalized gain for course-level pre/post comparisons.

### Shares method

- [[Interactive engagement]] - the survey compares courses using interactive-engagement instruction against traditional lecture-centered courses.

### Shares task

- [[Pre-post diagnostic assessment]] - the survey interprets pre/post mechanics diagnostic tests as evidence about instructional effectiveness.

## Questions

- How sensitive are Hake's course comparisons to reanalysis with individual-level normalized change rather than course-level average normalized gain?
- Which implementation factors most strongly separate medium-g and low-g interactive-engagement courses?
