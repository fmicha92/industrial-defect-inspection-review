---
title: "RealNet: A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection"
aliases:
  - "RealNet: A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection"
paper_key: "arxiv:2403.05897"
paper_type: research
year: 2024
venue: "arXiv"
authors:
  - "Ximiao Zhang"
  - "Xiuzhuang Zhou"
  - "Min Xu"
status: processed
processed_at: 2026-05-23
topics:
  - "realistic anomaly synthesis"
  - "feature selection"
  - "industrial anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[MPDD]]"
  - "[[BTAD]]"
  - "[[VisA]]"
methods:
  - "[[RealNet]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "[[RealNet]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[MVTec AD]]"
  - "[[MPDD]]"
  - "[[BTAD]]"
  - "[[VisA]]"
code: "reported available: https://github.com/cnulab/RealNet"
data: "reported available, URL not captured"
doi: "not reported"
arxiv: "2403.05897"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2024 - Zhang - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[RealNet]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[MPDD]]"
  - "[[BTAD]]"
  - "[[VisA]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2024 - Zhang - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Zhang - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Zhang - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# RealNet: A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection

## Summary

The paper proposes RealNet, combining Strength-controllable Diffusion Anomaly Synthesis with adaptive feature selection for industrial anomaly detection. The compact extraction reports evaluations on MVTec AD, MPDD, BTAD, and VisA using image AUROC, pixel AUROC, and PRO.

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

- Claimed: Introduces Strength-controllable Diffusion Anomaly Synthesis for realistic synthetic anomalies.
- Claimed: Uses adaptive feature selection for anomaly detection and localization.

- Inferred: The paper is relevant to [[Industrial anomaly detection]], [[Defect segmentation]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: The paper proposes RealNet, combining Strength-controllable Diffusion Anomaly Synthesis with adaptive feature selection for industrial anomaly detection
- Architecture / algorithm: [[RealNet]], [[Diffusion models]], [[Synthetic data generation]], [[RealNet]]
- Objective / loss: not reported in the compact extraction.
- Optimization: not reported in the compact extraction.
- Training data: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
- Data pipeline: not fully reported in the compact extraction.
- Augmentation / synthesis: [[Diffusion models]]
- Inference: not reported in the compact extraction.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
- Splits: not fully reported in the compact extraction.
- Baselines: not fully reported in the compact extraction.
- Used performance metrics: [[AU-ROC]], [[AU-PRO]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

- Shown: Evaluated with image AUROC, pixel AUROC, and PRO; exact values are not fully extracted.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | [[Industrial anomaly detection]], [[Defect segmentation]] | not fully extracted | higher | yes | recorded from compact extraction |
| [[AU-PRO]] | [[Industrial anomaly detection]], [[Defect segmentation]] | not fully extracted | higher | not reported | recorded from compact extraction |

## ML / DL Extraction

### Task Formulation

- Input modality: industrial visual inspection imagery, wafer maps, generated samples, masks, or multimodal prompts when reported.
- Output target: anomaly detection, localization, segmentation, classification, generation, or benchmark labels.
- Supervision: not fully reported in the compact extraction.
- Objective: not reported in the compact extraction.

### Model And Training

- Model family: [[Diffusion models]], [[Generative Models]]
- Architecture: [[RealNet]]
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in the compact extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
- Data source: not fully reported in the compact extraction.
- Dataset size: not fully reported in the compact extraction.
- Labels / annotations: defect labels, masks, bounding boxes, wafer-map classes, text captions, or benchmark labels when reported.
- Splits: not fully reported in the compact extraction.
- Preprocessing: not reported.
- Augmentation: [[Diffusion models]]
- Synthetic data: reported when synthesis or augmentation is part of the method.
- Leakage checks: not reported.
- License: not reported in the compact extraction.

### Evaluation

- Protocol: not fully reported in the compact extraction.
- Used performance metrics: [[AU-ROC]], [[AU-PRO]]
- Primary metric: [[AU-ROC]]
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and Dice-style metrics unless the paper states otherwise; lower is better for FID and LPIPS.
- Baselines: not fully reported in the compact extraction.
- Benchmarks: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
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

- The compact extraction does not include full result tables or artifact URL details.

- Inferred: conclusions should be checked against the full experimental protocol, dataset splits, and baseline details before using the paper as strong evidence.

## Reproducibility

- Code: reported available, URL not captured
- Data: reported available, URL not captured
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: code/data/models reported available

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[RealNet]], [[Diffusion models]], [[Synthetic data generation]]
- Datasets: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
- Benchmarks: [[MVTec AD]], [[MPDD]], [[BTAD]], [[VisA]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[MVTec AD]]: evaluated, trained, or benchmarked in the paper when reported.
- [[MPDD]]: evaluated, trained, or benchmarked in the paper when reported.
- [[BTAD]]: evaluated, trained, or benchmarked in the paper when reported.
- [[VisA]]: evaluated, trained, or benchmarked in the paper when reported.

### Shares Method

- [[RealNet]]: central to the paper method or comparison framing.
- [[Diffusion models]]: central to the paper method or comparison framing.
- [[Synthetic data generation]]: central to the paper method or comparison framing.

### Shares Task

- [[Industrial anomaly detection]]: task supported by the paper title, abstract, or evaluation description.
- [[Defect segmentation]]: task supported by the paper title, abstract, or evaluation description.

### Shares Metric

- [[AU-ROC]]: used as an evaluation metric in the compact extraction.
- [[AU-PRO]]: used as an evaluation metric in the compact extraction.

### Application / Domain

- [[Multi-industry anomaly detection]]: application setting represented by the paper.

### Follow-up Reading

- not reported.

## Questions

- Which dataset splits, baselines, and implementation details are required before treating the reported gains as robust evidence?
- Are the synthetic samples evaluated for leakage, artifact overfitting, or distribution shift beyond the reported metrics?
