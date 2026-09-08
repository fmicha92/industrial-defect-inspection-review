---
title: "HSS-IAD: A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset"
aliases:
  - "HSS-IAD: A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset"
paper_key: "doi:10.1109/icme59968.2025.11208914"
paper_type: dataset
year: 2025
venue: "ICME"
authors:
  - "Qingsong Wang"
  - "Shengyang Gao"
  - "Wenqiang Zhang"
status: processed
processed_at: 2026-05-22
topics:
  - "heterogeneous same-sort anomaly detection"
  - "dataset"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[HSS-IAD]]"
methods:
  - "[[Unsupervised learning]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures: []
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[HSS-IAD]]"
code: "not reported"
data: "reported available: https://github.com/Qiqigeww/HSS-IAD-Dataset"
doi: "10.1109/icme59968.2025.11208914"
arxiv: "9968.2025"
url: "not reported"
pdf: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Unsupervised learning]]"
  - "[[Unsupervised anomaly detection]]"
related_datasets:
  - "[[HSS-IAD]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
related_benchmarks: []
source_file: "paper-inbox/00_incoming/HSS-IAD_A_Heterogeneous_Same-Sort_Industrial_Anomaly_Detection_Dataset.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Wang - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Wang - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset.txt"
artifact_status: "dataset reported available"
tags:
  - paper
---
# HSS-IAD: A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset

## Summary

- Multi-class Unsupervised Anomaly Detection algorithms (MUAD) are receiving increasing attention due to their relatively low deployment costs and improved training efficiency.
- However, the real-world effectiveness of MUAD methods is questioned due to limitations in current Industrial Anomaly Detection (IAD) datasets.

## Paper Type

- Type: dataset.
- Why: Classified from the title, abstract, and contribution framing in the preprocessed paper text.

## Problem

- Task: [[Industrial anomaly detection]]
- Setting: [[Metal inspection]]
- Inputs: industrial inspection images or derived visual representations as described by the source paper.
- Outputs: defect labels, anomaly scores, defect masks, bounding boxes, generated samples, or benchmark artifacts depending on the paper objective.
- Motivation: improve automated quality inspection for industrial products.
- Assumptions: not fully reported in this concise extraction.

## Contribution

- Claimed: Multi-class Unsupervised Anomaly Detection algorithms (MUAD) are receiving increasing attention due to their relatively low deployment costs and improved training efficiency.
- Shown: Multi-class Unsupervised Anomaly Detection algorithms (MUAD) are receiving increasing attention due to their relatively low deployment costs and improved training efficiency. However, the real-world effectiveness of MUAD methods is questioned due to limitations in current Industrial Anomaly Detection (IAD) datasets. These datasets contain numerous classes that are unlikely to be produced by the same factory and fail to cover multiple structures or appearances. Additionally, the defects do not reflect real-world characteristics. Therefore, we introduce the Heterogeneous Same-Sort Industrial Anomaly Detection (HSSIAD) dataset, which contains 8,580 images of metallic-like industrial parts and precise anomaly annotations. These parts exhibit variations in structure and appearance, with subtle defects that closely resemble the base materials. We also provide foreground images for synthetic anomaly generation. Finally, we evaluate popular IAD methods on this dataset under multi-class and classseparated settings, demonstrating its potential to bridge the gap between existing datasets and real factory conditions. The dataset is available at https://github.com/Qiqigeww/HSS-IAD-Dataset.
- Inferred: The work is relevant to [[Industrial anomaly detection]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: Multi-class Unsupervised Anomaly Detection algorithms (MUAD) are receiving increasing attention due to their relatively low deployment costs and improved training efficiency.
- Architecture / algorithm: [[Unsupervised learning]], [[Unsupervised anomaly detection]]
- Objective / loss: not reported in this concise extraction.
- Optimization: not reported in this concise extraction.
- Training data: [[HSS-IAD]]
- Data pipeline: not reported in this concise extraction.
- Augmentation / synthesis: not reported
- Inference: not reported in this concise extraction.
- Complexity / deployment constraints: not reported in this concise extraction.

## ML / DL Extraction

### Task Formulation

- Input modality: visual inspection imagery or wafer maps as described by the source paper.
- Output target: defect/anomaly detection, localization, segmentation, classification, generation, or benchmark labels.
- Supervision: Unsupervised learning
- Objective: not reported in this concise extraction.

### Model And Training

- Model family: [[Unsupervised anomaly detection]]
- Architecture: not fully reported in this concise extraction.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in this concise extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[HSS-IAD]]
- Data source: HSS-IAD dataset reported by the paper
- Dataset size: not reported in this concise extraction.
- Labels / annotations: defect labels, masks, bounding boxes, or benchmark labels when reported by the paper.
- Splits: not reported in this concise extraction.
- Preprocessing: not reported.
- Augmentation: not reported
- Synthetic data: not reported
- Leakage checks: not reported.
- License: not reported in this concise extraction.

### Evaluation

- Protocol: not fully reported in this concise extraction.
- Used performance metrics: [[AU-ROC]]
- Primary metric: not reported
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for the listed accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and FPS metrics unless the paper states otherwise.
- Baselines: not reported in this concise extraction.
- Benchmarks: [[HSS-IAD]]
- Statistical tests: not reported.
- Failure cases: not reported in this concise extraction.

## Evidence

### Experimental Setup

- Datasets: [[HSS-IAD]]
- Splits: not reported in this concise extraction.
- Baselines: not reported in this concise extraction.
- Used performance metrics: [[AU-ROC]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Reported in source text | [[HSS-IAD]] / [[Industrial anomaly detection]] | AU-ROC | higher | not reported | not fully extracted | See extracted snippets below. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | [[Industrial anomaly detection]] | not fully extracted | higher | not reported | not reported |

Metric-related source snippets:
- ETECTION TASK IS MORE CHALLENGING . Datasets MVTec-AD [4] VisA [16] Real-IAD [5] BTAD [17] MPDD [15] HSS-IAD Metric↑ I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO Embedding-based SimpleNet DeSTSeg 89.2 95.3 86.5 64.8 88.9 87.2 81.4 6
- MORE CHALLENGING . Datasets MVTec-AD [4] VisA [16] Real-IAD [5] BTAD [17] MPDD [15] HSS-IAD Metric↑ I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO Embedding-based SimpleNet DeSTSeg 89.2 95.3 86.5 64.8 88.9 87.2 81.4 67.4 82.3 57.2 39
- G . Datasets MVTec-AD [4] VisA [16] Real-IAD [5] BTAD [17] MPDD [15] HSS-IAD Metric↑ I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO Embedding-based SimpleNet DeSTSeg 89.2 95.3 86.5 64.8 88.9 87.2 81.4 67.4 82.3 57.2 39.0 40.6 93.5 94.
- ec-AD [4] VisA [16] Real-IAD [5] BTAD [17] MPDD [15] HSS-IAD Metric↑ I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO I-AUROC P-AUPRO Embedding-based SimpleNet DeSTSeg 89.2 95.3 86.5 64.8 88.9 87.2 81.4 67.4 82.3 57.2 39.0 40.6 93.5 94.0 69.6 72.9 92.6

### Ablations

- not reported in this concise extraction.

## Dataset / Benchmark Details

- Source: HSS-IAD dataset reported by the paper
- Collection: not fully reported in this concise extraction.
- Annotation: not fully reported in this concise extraction.
- Size: not fully reported in this concise extraction.
- Splits: not reported in this concise extraction.
- Modalities: visual inspection imagery or wafer maps as described by the paper.
- License: not reported in this concise extraction.
- Leakage risks: not reported.
- Bias / coverage: not fully reported in this concise extraction.
- Maintenance: not reported.

## Limitations

- Stated: not fully reported in this concise extraction.
- Inferred: conclusions should be checked against the full experimental protocol, dataset split, and baseline details before using this paper as strong evidence.

## Reproducibility

- Code: not reported
- Data: HSS-IAD dataset reported by the paper
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: dataset reported available.
- Exact preprocessing: not reported.
- Artifact status: dataset reported available.

## Systems Details

- Hardware / software stack: not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: not reported.
- Deployment assumptions: not reported.
- Cost: not reported.
- Failure modes: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[Unsupervised learning]], [[Unsupervised anomaly detection]]
- Datasets: [[HSS-IAD]]
- Benchmarks: [[HSS-IAD]]
- Domains: [[Metal inspection]]
- Metrics: [[AU-ROC]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| not reported | Follow-up reading | Related-paper mapping was not completed in this concise extraction. |

### Backlinks Updated

- Important linked task, dataset, method, metric, and domain notes were updated when available.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[HSS-IAD]] | Created or updated if missing | Paper title and abstract |

## Questions

- Which baselines, splits, and ablations are most important for comparing this paper against adjacent work?
- Are code, data, or trained models available beyond what was captured in the concise extraction?
