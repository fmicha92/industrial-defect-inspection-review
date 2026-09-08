---
title: "Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection"
aliases:
  - "Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection"
paper_key: "doi:10.1109/tcsvt.2024.3479887"
paper_type: research
year: 2025
venue: "IEEE Transactions on Circuits and Systems for Video Technology"
authors:
  - "Qiyu Chen"
  - "Huiyuan Luo"
  - "Han Gao"
  - "Chengkan Lv"
  - "Zhengtao Zhang"
status: processed
processed_at: 2026-05-23
topics:
  - "boundary-guided anomaly synthesis"
  - "feature-level anomaly synthesis"
  - "industrial anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MPDD]]"
methods:
  - "[[PBAS]]"
  - "[[Synthetic data generation]]"
model_family:
  - "not reported"
architectures:
  - "[[PBAS]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
  - "[[Average precision]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MPDD]]"
code: "reported will be available: https://github.com/cqylunlun/PBAS"
data: "not reported"
doi: "10.1109/tcsvt.2024.3479887"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2025 - Chen - Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[PBAS]]"
  - "[[Synthetic data generation]]"
related_datasets:
  []
related_tasks:
  - "[[Industrial anomaly detection]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2025 - Chen - Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Chen - Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Chen - Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection.txt"
artifact_status: "code reported planned available"
tags:
  - paper
---
# Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection

## Summary

The paper proposes Progressive Boundary Guided Anomaly Synthesis (PBAS) for industrial anomaly detection. The compact extraction reports feature-level anomaly synthesis without auxiliary textures and components including Approximate Boundary Learning.

## Paper Type

- Type: research.
- Why: The title, abstract, and contribution framing describe a research method or evaluation study for industrial defect or anomaly inspection.

## Problem

- Task: [[Industrial anomaly detection]]
- Setting: [[Multi-industry anomaly detection]]
- Inputs: industrial inspection imagery, wafer maps, masks, or text prompts when reported by the source.
- Outputs: defect labels, anomaly scores, segmentation masks, generated defect samples, benchmark annotations, or classification predictions depending on the paper objective.
- Motivation: improve automated quality inspection under scarce, imbalanced, or hard-to-label defect data.
- Assumptions: not fully reported in the compact extraction unless stated above.

## Contribution

- Claimed: Introduces progressive boundary-guided feature-level anomaly synthesis.

- Inferred: The paper is relevant to [[Industrial anomaly detection]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: The paper proposes Progressive Boundary Guided Anomaly Synthesis (PBAS) for industrial anomaly detection
- Architecture / algorithm: [[PBAS]], [[Synthetic data generation]], [[PBAS]]
- Objective / loss: not reported in the compact extraction.
- Optimization: not reported in the compact extraction.
- Training data: [[MVTec AD]], [[VisA]], [[MPDD]]
- Data pipeline: not fully reported in the compact extraction.
- Augmentation / synthesis: not reported
- Inference: not reported in the compact extraction.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[VisA]], [[MPDD]]
- Splits: not fully reported in the compact extraction.
- Baselines: not fully reported in the compact extraction.
- Used performance metrics: [[AU-ROC]], [[AU-PRO]], [[Average precision]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

- Shown: Exact datasets, metrics, and result values are not fully extracted.

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

- Model family: not reported
- Architecture: [[PBAS]]
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in the compact extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec AD]], [[VisA]], [[MPDD]]
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
- Used performance metrics: [[AU-ROC]], [[AU-PRO]], [[Average precision]]
- Primary metric: [[AU-ROC]]
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and Dice-style metrics unless the paper states otherwise; lower is better for FID and LPIPS.
- Baselines: not fully reported in the compact extraction.
- Benchmarks: [[MVTec AD]], [[VisA]], [[MPDD]]
- Statistical tests: not reported.
- Failure cases: not fully reported in the compact extraction.

## Dataset / Benchmark Details

- Source: [[MVTec AD]], [[VisA]], and [[MPDD]].
- Collection: MVTec AD is a 15-category industrial anomaly dataset; MPDD contains metal part images under varied camera conditions across six categories.
- Annotation: anomaly labels and pixel-level localization labels are used for anomaly detection/localization evaluation.
- Size: MVTec AD contains 5354 high-resolution industrial product images with more than 70 defect types; the training set has 3629 normal samples. MPDD contains 1346 metal-part images; the training set has 888 normal samples and the test set contains normal and abnormal samples.
- Splits: standard anomaly-detection training uses normal-only training samples; test sets contain normal and abnormal images.
- Modalities: 2D industrial product images.
- License: not reported in the extracted text.
- Leakage risks: PBAS synthesizes feature-level anomalies from normal training features without auxiliary texture datasets; no formal leakage audit is reported.
- Bias / coverage: MVTec AD spans many industrial categories; MPDD focuses on metal parts and varied camera conditions.
- Maintenance: not reported.

## Metal Dataset Extraction

- [[MPDD]]: Metal Parts Defect Detection dataset with 1346 images across six categories and 888 normal training samples; used as the metal-specific benchmark.
- [[MVTec AD]]: includes metal-relevant object categories such as metal nut and is used as a broad industrial anomaly benchmark.
- Synthesis: PBAS synthesizes feature-level anomalies in ray directions from normal feature centers, avoiding auxiliary texture datasets and pixel-level defect annotations during training.
- Evaluation: metrics include image-level AUROC/AP and pixel-level AUROC/AP/PRO. The paper reports MVTec AD average I-AUROC of 99.8%, P-AUROC of 98.6%, and P-PRO of 97.3%; on MPDD, PBAS reports average I-AUROC of 97.7% and improves P-AUROC/P-PRO over compared methods.

## Limitations

- Datasets, metrics, baselines, and full experimental settings are not fully reported in the compact extraction.

- Inferred: conclusions should be checked against the full experimental protocol, dataset splits, and baseline details before using the paper as strong evidence.

## Reproducibility

- Code: reported will be available: https://github.com/cqylunlun/PBAS
- Data: not reported
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: code reported planned available

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[PBAS]], [[Synthetic data generation]]
- Datasets: [[MVTec AD]], [[VisA]], [[MPDD]]
- Benchmarks: [[MVTec AD]], [[VisA]], [[MPDD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]], [[Average precision]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- not reported

### Shares Method

- [[PBAS]]: central to the paper method or comparison framing.
- [[Synthetic data generation]]: central to the paper method or comparison framing.

### Shares Task

- [[Industrial anomaly detection]]: task supported by the paper title, abstract, or evaluation description.

### Shares Metric

- not reported

### Application / Domain

- [[Multi-industry anomaly detection]]: application setting represented by the paper.

### Follow-up Reading

- not reported.

## Questions

- Which dataset splits, baselines, and implementation details are required before treating the reported gains as robust evidence?
- Are the synthetic samples evaluated for leakage, artifact overfitting, or distribution shift beyond the reported metrics?
