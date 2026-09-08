---
title: "AnomalyControl: Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis"
aliases:
  - "AnomalyControl: Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis"
paper_key: "doi:10.48550/arxiv.2412.06510"
paper_type: research
year: 2025
venue: "arXiv"
authors:
  - "Shidan He"
  - "Lei Liu"
  - "Xiujun Shu"
  - "Bo Wang"
  - "Yuanhao Feng"
  - "Shen Zhao"
status: processed
processed_at: 2026-05-23
topics:
  - "controllable anomaly synthesis"
  - "cross-modal semantic features"
  - "industrial anomaly generation"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[MPDD]]"
methods:
  - "[[AnomalyControl]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "[[AnomalyControl]]"
metrics:
  - "[[Inception Score]]"
  - "[[LPIPS]]"
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[MVTec AD]]"
  - "[[MPDD]]"
code: "reported available: https://github.com/DaniellaHe/AnomalyControl"
data: "not reported"
doi: "10.48550/arxiv.2412.06510"
arxiv: "2412.06510"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2025 - He - AnomalyControl Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[AnomalyControl]]"
  - "[[Synthetic data generation]]"
related_datasets:
  []
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2025 - He - AnomalyControl Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - He - AnomalyControl Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis.md"
extracted_text: "paper-inbox/90_processing/text/2025 - He - AnomalyControl Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# AnomalyControl: Learning Cross-modal Semantic Features for Controllable Anomaly Synthesis

## Summary

The paper proposes AnomalyControl for controllable anomaly synthesis by learning cross-modal semantic features. The compact extraction identifies the method and controllable synthesis framing, but not full dataset or metric details.

## Paper Type

- Type: research.
- Why: The title, abstract, and contribution framing describe a research method or evaluation study for industrial defect or anomaly inspection.

## Problem

- Task: [[Industrial anomaly detection]], [[Defect segmentation]]
- Setting: [[Multi-industry anomaly detection]]
- Inputs: industrial inspection imagery, wafer maps, masks, or text prompts when reported by the source.
- Outputs: defect labels, anomaly scores, segmentation masks, generated defect samples, benchmark annotations, or classification predictions depending on the paper objective.
- Motivation: improve automated quality inspection under scarce, imbalanced, or hard-to-label defect data.
- Assumptions: not fully reported in the compact extraction unless stated above.

## Contribution

- Claimed: Learns cross-modal semantic features for controllable anomaly synthesis.

- Inferred: The paper is relevant to [[Industrial anomaly detection]], [[Defect segmentation]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: The paper proposes AnomalyControl for controllable anomaly synthesis by learning cross-modal semantic features
- Architecture / algorithm: [[AnomalyControl]], [[Synthetic data generation]], [[AnomalyControl]]
- Objective / loss: not reported in the compact extraction.
- Optimization: not reported in the compact extraction.
- Training data: [[MVTec AD]], [[MPDD]]
- Data pipeline: not fully reported in the compact extraction.
- Augmentation / synthesis: not reported
- Inference: not reported in the compact extraction.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[MPDD]]
- Splits: not fully reported in the compact extraction.
- Baselines: not fully reported in the compact extraction.
- Used performance metrics: [[Inception Score]], [[LPIPS]], [[AU-ROC]], [[Average precision]], [[F1-score]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

- Shown: Exact datasets, metrics, and numerical results are not fully extracted.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| not reported | not reported | not reported | not reported | not reported | not reported |

## ML / DL Extraction

### Task Formulation

- Input modality: industrial visual inspection imagery, wafer maps, generated samples, masks, or multimodal prompts when reported.
- Output target: anomaly detection, localization, segmentation, classification, generation, or benchmark labels.
- Supervision: not fully reported in the compact extraction.
- Objective: not reported in the compact extraction.

### Model And Training

- Model family: [[Generative Models]]
- Architecture: [[AnomalyControl]]
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in the compact extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec AD]], [[MPDD]]
- Data source: not fully reported in the compact extraction.
- Dataset size: not fully reported in the compact extraction.
- Labels / annotations: defect labels, masks, bounding boxes, wafer-map classes, text captions, or benchmark labels when reported.
- Splits: not fully reported in the compact extraction.
- Preprocessing: not reported.
- Augmentation: not reported
- Synthetic data: reported when synthesis or augmentation is part of the method.
- Leakage checks: not reported.
- License: not reported in the compact extraction.

### Evaluation

- Protocol: not fully reported in the compact extraction.
- Used performance metrics: [[Inception Score]], [[LPIPS]], [[AU-ROC]], [[Average precision]], [[F1-score]]
- Primary metric: [[Inception Score]]
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and Dice-style metrics unless the paper states otherwise; lower is better for FID and LPIPS.
- Baselines: not fully reported in the compact extraction.
- Benchmarks: [[MVTec AD]], [[MPDD]]
- Statistical tests: not reported.
- Failure cases: not fully reported in the compact extraction.

## Dataset / Benchmark Details

- Source: not fully reported in the compact extraction.
- Collection: not fully reported in the compact extraction.
- Annotation: not fully reported in the compact extraction.
- Size: not fully reported in the compact extraction.
- Splits: not fully reported in the compact extraction.
- Modalities: visual inspection imagery, wafer maps, generated defects, masks, or captions when reported.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: not fully reported in the compact extraction.
- Maintenance: not reported.

## Limitations

- Dataset, evaluation protocol, and artifact details are not fully reported in the compact extraction.

- Inferred: conclusions should be checked against the full experimental protocol, dataset splits, and baseline details before using the paper as strong evidence.

## Reproducibility

- Code: reported available: https://github.com/DaniellaHe/AnomalyControl
- Data: not reported
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: code reported available

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[AnomalyControl]], [[Synthetic data generation]]
- Datasets: [[MVTec AD]], [[MPDD]]
- Benchmarks: [[MVTec AD]], [[MPDD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Inception Score]], [[LPIPS]], [[AU-ROC]], [[Average precision]], [[F1-score]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- not reported

### Shares Method

- [[AnomalyControl]]: central to the paper method or comparison framing.
- [[Synthetic data generation]]: central to the paper method or comparison framing.

### Shares Task

- [[Industrial anomaly detection]]: task supported by the paper title, abstract, or evaluation description.
- [[Defect segmentation]]: task supported by the paper title, abstract, or evaluation description.

### Shares Metric

- not reported

### Application / Domain

- [[Multi-industry anomaly detection]]: application setting represented by the paper.

### Follow-up Reading

- not reported.

## Questions

- Which dataset splits, baselines, and implementation details are required before treating the reported gains as robust evidence?
- Are the synthetic samples evaluated for leakage, artifact overfitting, or distribution shift beyond the reported metrics?
