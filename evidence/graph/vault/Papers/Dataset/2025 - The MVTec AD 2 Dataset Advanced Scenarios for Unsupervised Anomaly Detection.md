---
title: "The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection"
aliases:
  - "The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection"
paper_key: "sha256:bf9df9d7f71e2775647952b36cdea2431f48e33ec20aa254fca82029791479a9"
paper_type: dataset
year: 2025
venue: "not reported"
authors:
  - "Heckler-Kram"
status: processed
processed_at: 2026-05-21
topics:
  - industrial defect detection
tasks:
  - "[[Unsupervised anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD 2]]"
  - "[[MVTec AD]]"
methods:
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
benchmarks:
  - "[[MVTec AD 2]]"
  - "[[MVTec AD]]"
code: "not reported"
data: "reported available: https://www.mvtec.com/company/research/datasets/mvtec-ad-2"
doi: "not reported"
arxiv: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[Unsupervised anomaly detection]]"
related_datasets:
  - "[[MVTec AD 2]]"
  - "[[MVTec AD]]"
related_tasks:
  - "[[Unsupervised anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/2025 - Heckler-Kram - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Heckler-Kram - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Heckler-Kram - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection.txt"
artifact_status: "dataset and benchmark server reported available"
tags:
  - paper
---

# The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection

## Summary

- Introduces MVTec AD 2 for advanced scenarios in unsupervised anomaly detection.
- The extracted abstract frames the dataset as responding to performance saturation on existing anomaly detection datasets.
- Extends the MVTec anomaly-detection dataset family in the vault.

## Paper Type

- Type: dataset.
- Why: Classified from the extracted title, abstract/keywords, and contribution framing in the preprocessed paper text.

## Problem

- Task: [[Unsupervised anomaly detection]], [[Defect segmentation]]
- Setting: industrial defect detection / inspection.
- Inputs: images or process-monitoring data as described by the source paper.
- Outputs: defect labels, defect locations, unknown-pattern flags, review taxonomy, or dataset/benchmark artifacts depending on paper type.
- Motivation: improve automated quality inspection for industrial products.
- Assumptions: not fully reported in this concise pass.

## Contribution

- Claimed: Introduces MVTec AD 2 for advanced scenarios in unsupervised anomaly detection.
- Shown: The extracted abstract states that performance on existing anomaly detection datasets motivates advanced scenarios; index terms include anomaly detection, datasets, benchmarks, and evaluation.
- Inferred: This paper strengthens the vault's coverage of [[Unsupervised anomaly detection]], [[Defect segmentation]].

## Method

- Core idea: Introduces MVTec AD 2 for advanced scenarios in unsupervised anomaly detection.
- Architecture / algorithm: [[Unsupervised anomaly detection]]
- Objective / loss: not reported in this concise pass.
- Optimization: not reported in this concise pass.
- Training data: [[MVTec AD 2]], [[MVTec AD]]
- Data pipeline: not reported in this concise pass.
- Augmentation / synthesis: recorded when named in the title or graph hubs.
- Inference: not reported in this concise pass.
- Complexity / deployment constraints: not reported in this concise pass.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial imagery or monitoring data as reported by the paper.
- Output target: defect class, defect region, anomaly flag, or review synthesis.
- Supervision: not reported in this concise pass.
- Objective: Introduces MVTec AD 2 for advanced scenarios in unsupervised anomaly detection.

### Model And Training

- Model family: [[Unsupervised anomaly detection]]
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

- Datasets: [[MVTec AD 2]], [[MVTec AD]]
- Data source: The extracted abstract states that performance on existing anomaly detection datasets motivates advanced scenarios; index terms include anomaly detection, datasets, benchmarks, and evaluation.
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
- Used performance metrics: [[AU-ROC]], [[AU-PRO]]
- Primary metric: [[AU-ROC]]
- Metric definitions: not reported in this concise pass.
- Metric direction / units: use linked metric notes when available.
- Baselines: not reported in this concise pass.
- Benchmarks: [[MVTec AD 2]], [[MVTec AD]]
- Statistical tests: not reported.
- Failure cases: not reported in this concise pass.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD 2]], [[MVTec AD]]
- Splits: not reported in this concise pass.
- Baselines: not reported in this concise pass.
- Used performance metrics: [[AU-ROC]], [[AU-PRO]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Contribution summary | [[Unsupervised anomaly detection]], [[Defect segmentation]] | [[AU-ROC]], [[AU-PRO]] | not reported | not reported | not reported | The extracted abstract states that performance on existing anomaly detection datasets motivates advanced scenarios; index terms include anomaly detection, datasets, benchmarks, and evaluation. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]], [[AU-PRO]] | paper evaluation or review synthesis | see linked notes when available | not reported | not reported | not reported in this concise pass |

### Ablations

- not reported in this concise pass.

## Dataset / Benchmark Details

- Source: The extracted abstract states that performance on existing anomaly detection datasets motivates advanced scenarios; index terms include anomaly detection, datasets, benchmarks, and evaluation.
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
- Major themes: [[Unsupervised anomaly detection]], [[Defect segmentation]]; [[Unsupervised anomaly detection]].
- Gaps: not reported in this concise pass.

## Limitations

- Stated: not reported in this concise pass.
- Inferred: No DOI was extracted; identifier is the source-file SHA-256.

## Reproducibility

- Code: not reported.
- Data: [[MVTec AD 2]], [[MVTec AD]]
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: dataset and benchmark server reported available.
- Exact preprocessing: not reported.
- Artifact status: dataset and benchmark server reported available.

## Connections

### Graph Hubs

- Tasks: [[Unsupervised anomaly detection]], [[Defect segmentation]]
- Methods: [[Unsupervised anomaly detection]]
- Datasets: [[MVTec AD 2]], [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Builds On

- [[Unsupervised anomaly detection]]: method family or named architecture linked from the paper's title, abstract, or keywords.

### Contrasts With

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]: related industrial defect detection context, but with different dataset/task scope unless this paper is a review.

### Shares Dataset

- [[MVTec AD 2]], [[MVTec AD]]

### Shares Task

- [[Unsupervised anomaly detection]], [[Defect segmentation]]

### Shares Method

- [[Unsupervised anomaly detection]]

### Shares Metric

- [[AU-ROC]], [[AU-PRO]]

### Application / Domain

- [[Multi-industry anomaly detection]]

### Follow-Up Reading

- [[Surface defect detection]]

## Questions

- Revisit the full analysis input for exact dataset sizes, split details, and result values.
- Verify artifact availability if this paper is later used as a benchmark anchor.
