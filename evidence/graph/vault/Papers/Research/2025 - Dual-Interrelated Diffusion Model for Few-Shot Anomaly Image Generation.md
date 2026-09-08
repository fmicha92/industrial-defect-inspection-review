---
title: "Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation"
aliases:
  - "Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation"
paper_key: "arxiv:2408.13509"
paper_type: research
year: 2025
venue: "arXiv"
authors:
  - "Ying Jin"
  - "Jinlong Peng"
  - "Qingdong He"
  - "Teng Hu"
  - "Jiafu Wu"
  - "Hao Chen"
  - "Haoxuan Wang"
  - "Wenbing Zhu"
  - "Mingmin Chi"
  - "Jun Liu"
  - "Yabiao Wang"
status: processed
processed_at: 2026-05-23
topics:
  - "few-shot anomaly generation"
  - "dual diffusion models"
  - "industrial anomaly synthesis"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[DualAnoDiff]]"
  - "[[Diffusion models]]"
  - "[[Few-shot zero-shot learning]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "[[DualAnoDiff]]"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
  - "[[Inception Score]]"
  - "[[LPIPS]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[MVTec AD]]"
code: "reported available: https://github.com/yinyjin/DualAnoDiff"
data: "not reported"
doi: "not reported"
arxiv: "2408.13509"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2025 - Jin - Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[DualAnoDiff]]"
  - "[[Diffusion models]]"
  - "[[Few-shot zero-shot learning]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[MVTec AD]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2025 - Jin - Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Jin - Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Jin - Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation

## Summary

The paper proposes DualAnoDiff, a dual-interrelated diffusion model for few-shot anomaly image generation. The extracted text describes coupled diffusion models for whole-image and anomaly-part generation and reports a public code URL.

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

- Claimed: Uses dual diffusion models to coordinate whole-image and anomaly-part synthesis.
- Claimed: Targets few-shot industrial anomaly image generation.

- Inferred: The paper is relevant to [[Industrial anomaly detection]], [[Defect segmentation]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: The paper proposes DualAnoDiff, a dual-interrelated diffusion model for few-shot anomaly image generation
- Architecture / algorithm: [[DualAnoDiff]], [[Diffusion models]], [[Few-shot zero-shot learning]], [[Synthetic data generation]], [[DualAnoDiff]]
- Objective / loss: not reported in the compact extraction.
- Optimization: not reported in the compact extraction.
- Training data: [[MVTec AD]]
- Data pipeline: not fully reported in the compact extraction.
- Augmentation / synthesis: [[Diffusion models]]
- Inference: not reported in the compact extraction.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]]
- Splits: not fully reported in the compact extraction.
- Baselines: not fully reported in the compact extraction.
- Used performance metrics: [[AU-ROC]], [[Average precision]], [[F1-score]], [[Accuracy]], [[Inception Score]], [[LPIPS]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

- Shown: Evaluation metrics and exact numerical results are not fully extracted.

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

- Model family: [[Diffusion models]], [[Generative Models]]
- Architecture: [[DualAnoDiff]]
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in the compact extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec AD]]
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
- Used performance metrics: [[AU-ROC]], [[Average precision]], [[F1-score]], [[Accuracy]], [[Inception Score]], [[LPIPS]]
- Primary metric: [[AU-ROC]]
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and Dice-style metrics unless the paper states otherwise; lower is better for FID and LPIPS.
- Baselines: not fully reported in the compact extraction.
- Benchmarks: [[MVTec AD]]
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

- The compact extraction does not fully report datasets beyond MVTec AD, metrics, or baseline details.

- Inferred: conclusions should be checked against the full experimental protocol, dataset splits, and baseline details before using the paper as strong evidence.

## Reproducibility

- Code: https://github.com/yinyjin/DualAnoDiff
- Data: not reported
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: code reported

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[DualAnoDiff]], [[Diffusion models]], [[Few-shot zero-shot learning]], [[Synthetic data generation]]
- Datasets: [[MVTec AD]]
- Benchmarks: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]], [[F1-score]], [[Accuracy]], [[Inception Score]], [[LPIPS]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[MVTec AD]]: evaluated, trained, or benchmarked in the paper when reported.

### Shares Method

- [[DualAnoDiff]]: central to the paper method or comparison framing.
- [[Diffusion models]]: central to the paper method or comparison framing.
- [[Few-shot zero-shot learning]]: central to the paper method or comparison framing.
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
