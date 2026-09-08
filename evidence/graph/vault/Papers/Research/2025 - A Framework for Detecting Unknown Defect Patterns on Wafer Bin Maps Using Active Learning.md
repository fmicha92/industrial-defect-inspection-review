---
title: "A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning"
aliases:
  - "A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning"
paper_key: "sha256:5cc0a2064e59e599d27b39d848d0aac34e7f85c2fb70a3bb552a0a71a95b62e5"
paper_type: research
year: 2025
venue: "not reported"
authors:
  - "Shin"
status: processed
processed_at: 2026-05-21
topics:
  - industrial defect detection
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[Taiwan company 21-defect wafer map dataset]]"
methods:
  - "[[Active learning]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Precision]]"
benchmarks:
  - "[[Taiwan company 21-defect wafer map dataset]]"
code: "not reported"
data: "not reported"
doi: "not reported"
arxiv: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[Active learning]]"
  - "[[Deep convolutional neural network]]"
related_datasets:
  - "[[Taiwan company 21-defect wafer map dataset]]"
related_tasks:
  - "[[Wafer map defect classification]]"
source_file: "paper-inbox/10_processed/Research/2025 - Shin - A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Shin - A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Shin - A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning.txt"
artifact_status: "not reported"
tags:
  - paper
---

# A Framework for Detecting Unknown Defect Patterns on Wafer Bin Maps Using Active Learning

## Summary

- Presents a framework for detecting unknown defect patterns on wafer bin maps using active learning.
- Connects active learning to wafer map defect classification when unknown patterns appear.
- Extends the wafer-map graph beyond fixed known-pattern classification.

## Paper Type

- Type: research.
- Why: Classified from the extracted title, abstract/keywords, and contribution framing in the preprocessed paper text.

## Problem

- Task: [[Wafer map defect classification]]
- Setting: industrial defect detection / inspection.
- Inputs: images or process-monitoring data as described by the source paper.
- Outputs: defect labels, defect locations, unknown-pattern flags, review taxonomy, or dataset/benchmark artifacts depending on paper type.
- Motivation: improve automated quality inspection for industrial products.
- Assumptions: not fully reported in this concise pass.

## Contribution

- Claimed: Presents a framework for detecting unknown defect patterns on wafer bin maps using active learning.
- Shown: The title identifies unknown defect-pattern detection on wafer bin maps using active learning.
- Inferred: This paper strengthens the vault's coverage of [[Wafer map defect classification]].

## Method

- Core idea: Presents a framework for detecting unknown defect patterns on wafer bin maps using active learning.
- Architecture / algorithm: [[Active learning]], [[Deep convolutional neural network]]
- Objective / loss: not reported in this concise pass.
- Optimization: not reported in this concise pass.
- Training data: [[Taiwan company 21-defect wafer map dataset]]
- Data pipeline: not reported in this concise pass.
- Augmentation / synthesis: recorded when named in the title or graph hubs.
- Inference: not reported in this concise pass.
- Complexity / deployment constraints: not reported in this concise pass.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial imagery or monitoring data as reported by the paper.
- Output target: defect class, defect region, anomaly flag, or review synthesis.
- Supervision: not reported in this concise pass.
- Objective: Presents a framework for detecting unknown defect patterns on wafer bin maps using active learning.

### Model And Training

- Model family: [[Active learning]], [[Deep convolutional neural network]]
- Architecture: not fully reported in this concise pass.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[Taiwan company 21-defect wafer map dataset]]
- Data source: The title identifies unknown defect-pattern detection on wafer bin maps using active learning.
- Dataset size: not reported in this concise pass.
- Labels / annotations: not reported in this concise pass.
- Splits: not reported in this concise pass.
- Preprocessing: not reported in this concise pass.
- Augmentation: not reported unless named in the summary.
- Synthetic data: not reported unless named in the summary.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: not reported in this concise pass.
- Used performance metrics: [[Precision]], [[Recall]]
- Primary metric: [[Precision]]
- Metric definitions: not reported in this concise pass.
- Metric direction / units: use linked metric notes when available.
- Baselines: not reported in this concise pass.
- Benchmarks: [[Taiwan company 21-defect wafer map dataset]]
- Statistical tests: not reported.
- Failure cases: not reported in this concise pass.

## Evidence

### Experimental Setup

- Datasets: [[Taiwan company 21-defect wafer map dataset]]
- Splits: not reported in this concise pass.
- Baselines: not reported in this concise pass.
- Used performance metrics: [[Precision]], [[Recall]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Contribution summary | [[Wafer map defect classification]] | [[Precision]], [[Recall]] | not reported | not reported | not reported | The title identifies unknown defect-pattern detection on wafer bin maps using active learning. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Precision]], [[Recall]] | paper evaluation or review synthesis | see linked notes when available | not reported | not reported | not reported in this concise pass |

### Ablations

- not reported in this concise pass.

## Dataset / Benchmark Details

- Source: The title identifies unknown defect-pattern detection on wafer bin maps using active learning.
- Collection: not reported in this concise pass.
- Annotation: not reported in this concise pass.
- Size: not reported in this concise pass.
- Splits: not reported in this concise pass.
- Modalities: industrial images or monitoring data as reported by the paper.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: not reported.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not reported in this concise pass.
- Taxonomy: not reported in this concise pass.
- Major themes: [[Wafer map defect classification]]; [[Active learning]], [[Deep convolutional neural network]].
- Gaps: not reported in this concise pass.

## Limitations

- Stated: not reported in this concise pass.
- Inferred: No DOI was extracted; identifier is the source-file SHA-256.

## Reproducibility

- Code: not reported.
- Data: [[Taiwan company 21-defect wafer map dataset]]
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: not reported.
- Artifact status: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[Active learning]], [[Deep convolutional neural network]]
- Datasets: [[Taiwan company 21-defect wafer map dataset]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Precision]], [[Recall]]

### Builds On

- [[Active learning]], [[Deep convolutional neural network]]: method family or named architecture linked from the paper's title, abstract, or keywords.

### Contrasts With

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]: related industrial defect detection context, but with different dataset/task scope unless this paper is a review.

### Shares Dataset

- [[Taiwan company 21-defect wafer map dataset]]

### Shares Task

- [[Wafer map defect classification]]

### Shares Method

- [[Active learning]], [[Deep convolutional neural network]]

### Shares Metric

- [[Precision]], [[Recall]]

### Application / Domain

- [[Semiconductor and electronics]]

### Follow-Up Reading

- [[Surface defect detection]]

## Questions

- Revisit the full analysis input for exact dataset sizes, split details, and result values.
- Verify artifact availability if this paper is later used as a benchmark anchor.
