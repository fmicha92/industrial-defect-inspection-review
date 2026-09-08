---
title: "Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation"
aliases:
  - "Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation"
  - "SACD"
paper_key: "sha256:5e1a13b560b2ef7395ad4a7a37d67e4a81bd73a9b94dc27a00d290e0e6406161"
paper_type: research
year: 2025
venue: "Sensors"
authors:
  - "Junxian Li"
  - "Mingxing Li"
  - "Shucheng Huang"
  - "Gang Wang"
status: processed
processed_at: 2026-06-12
topics:
  - "synthetic anomaly contrastive distillation"
  - "Simplex noise anomaly synthesis"
  - "teacher-student anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[RD4AD]]"
architectures:
  - "[[RD4AD]]"
  - "[[ResNet50]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
baselines:
  - "Uninformed Students"
  - "MKD"
  - "Patch-SVDD"
  - "SPADE"
  - "PaDiM"
  - "CutPaste"
  - "RIAD"
  - "RD4AD"
  - "MaMiNet"
  - "MMR"
  - "AEKD"
  - "MSFR"
benchmarks:
  - "[[MVTec AD]]"
code: "not reported"
data: "uses MVTec AD and BTAD"
doi: "10.3390/s25123721"
arxiv: "not reported"
url: "https://doi.org/10.3390/s25123721"
pdf: "paper-inbox/10_processed/Research/2025 - Li - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation.pdf"
related_methods:
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[RD4AD]]"
related_datasets:
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2025 - Li - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Li - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Li - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation

## Summary

The paper proposes Synthetic-Anomaly Contrastive Distillation (SACD), a teacher-student industrial anomaly detection method that adds a synthetic-anomaly branch to reverse distillation. Synthetic anomalies are generated from normal images using Simplex noise, and FeaCali modules are trained to remove anomalous patterns from the student branch. On [[MVTec AD]], SACD reports 99.3% image-level AUROC, 98.3% pixel-level AUROC, and 94.8% PRO.

## Paper Type

- Type: research.
- Why: It proposes a new anomaly detection/localization model and reports quantitative comparisons and ablations.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: normal-only industrial anomaly detection with synthetic pseudo-anomaly exposure during training.
- Inputs: industrial images resized to 256 x 256.
- Outputs: image-level anomaly scores and pixel-level anomaly score maps.
- Motivation: ordinary reverse distillation can reconstruct or align features in ways that weaken anomaly contrast.
- Assumptions: normal and anomalous patterns share basic feature components, so synthetic anomaly confrontation can teach the student to refine abnormal features away.

## Contribution

- Claimed: Adds a Siamese synthetic-anomaly branch to reverse distillation.
- Claimed: Introduces FeaCali modules that enhance normal features and suppress synthetic abnormal patterns.
- Shown: Simplex-noise synthesis outperforms CutPaste and Gaussian-noise synthesis in the paper's ablation.

## Method

- Core idea: train a normal branch and synthetic anomaly branch against a teacher model, using contrastive losses to increase teacher-student discrepancy on abnormal regions while preserving normal consistency.
- Architecture / algorithm: WideResNet50 teacher, student reverse-distillation model, multi-scale refinement module, and FeaCali bottleneck modules.
- Objective / loss: dual-objective loss combining cross-model feature alignment and intra-model component coordination; equilibrium coefficient alpha defaults to 0.2.
- Optimization: Adam with beta=(0.5, 0.999), learning rate 0.001, batch size 16, 200 epochs.
- Training data: [[MVTec AD]] and BTAD normal samples.
- Data pipeline: one-class-per-category training; images resized to 256 x 256.
- Augmentation / synthesis: half of each batch is used for pseudo-anomaly synthesis; Simplex noise generates variable-shaped pseudo-anomaly regions, with lambda controlling anomaly intensity.
- Inference: anomaly score maps are smoothed with a Gaussian filter with sigma=4.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]] and BTAD.
- Splits: category-wise anomaly detection using normal training samples and normal/anomalous test sets.
- Baselines: Uninformed Students, MKD, Patch-SVDD, SPADE, PaDiM, CutPaste, RIAD, RD4AD, MaMiNet, MMR, AEKD, MSFR.
- Used performance metrics: image-level AUROC, pixel-level AUROC, and PRO.
- Hardware: not reported in the extracted text.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| SACD vs AEKD complexity/performance | MVTec AD image-level detection | AUROC (%) | higher | 98.9 | 99.3 | SACD depth L=2 also has lower latency than AEKD, 3.85 ms vs 4.64 ms. |
| Simplex synthesis vs CutPaste synthesis | MVTec AD detection/localization | image AUROC / pixel AUROC / PRO (%) | higher | 99.1 / 97.9 / 94.2 | 99.3 / 98.3 / 94.8 | Same SACD framework, synthesis mode changed. |
| Simplex synthesis vs Gaussian noise synthesis | MVTec AD detection/localization | image AUROC / pixel AUROC / PRO (%) | higher | 99.0 / 98.0 / 94.4 | 99.3 / 98.3 / 94.8 | Simplex noise is described as more natural-looking. |
| WideResNet50 teacher vs ResNet50 teacher | MVTec AD detection/localization | image AUROC / pixel AUROC / PRO (%) | higher | 99.0 / 98.0 / 94.4 | 99.3 / 98.3 / 94.8 | Pretrained-model ablation. |
| WideResNet50 teacher vs ResNet18 teacher | MVTec AD detection/localization | image AUROC / pixel AUROC / PRO (%) | higher | 98.4 / 97.6 / 94.0 | 99.3 / 98.3 / 94.8 | Pretrained-model ablation. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection | Percent AUROC | higher | yes | Main detection metric. |
| [[AU-ROC]] | Pixel-level anomaly localization | Percent pixel-wise AUROC | higher | yes | Localization metric. |
| [[AU-PRO]] | Region-level localization | Percent PRO | higher | no | Measures overlap and recovery of connected anomaly components. |

### Ablations

- FeaCali depth L=2 is identified as the accuracy-efficiency point: 158.90M parameters, 39.67G FLOPs, 3.85 ms latency, and 99.3% image AUROC.
- Simplex-noise synthesis outperforms CutPaste and Gaussian-noise synthesis.
- Alpha=0.2 is the best reported loss-balance setting.
- WideResNet50 outperforms ResNet18 and ResNet50 as the teacher.

## ML / DL Extraction

### Data

- Datasets: [[MVTec AD]] and BTAD.
- Dataset size: MVTec AD has 15 sub-datasets, 5354 images, and 1725 test images in the source description.
- Labels / annotations: MVTec AD provides defect types and ground-truth anomaly masks for test sets.
- Preprocessing: resize to 256 x 256.
- Augmentation: source explicitly says no ordinary data augmentation is applied; pseudo-anomaly synthesis is used.
- Synthetic data: Simplex noise regions are blended into normal images; lambda default is 0.4, and half of each batch is synthesized.
- Leakage checks: not reported.

### Evaluation

- Protocol: one class at a time, following prior work.
- Statistical tests: not reported.
- Failure cases: not fully reported in the extracted text.

## Limitations

- Stated: future work aims to investigate more natural and physically consistent anomaly synthesis methods.
- Inferred: Simplex noise may still be a crude proxy for physical industrial defects.

## Reproducibility

- Code: not reported.
- Data: MVTec AD public; BTAD external benchmark.
- Hyperparameters: lambda 0.4 by default, alpha 0.2, Simplex octaves=3, persistence=0.5, frequency=32.0, Adam lr=0.001, batch size 16, 200 epochs.
- Random seeds: not reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Defect synthesis]], [[Synthetic data generation]], [[RD4AD]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Shares Dataset

- [[MVTec AD]]: main reported industrial benchmark.

### Shares Method

- [[Defect synthesis]] and [[Synthetic data generation]]: Simplex-noise pseudo-anomaly generation is central to the method.
- [[RD4AD]]: SACD modifies reverse-distillation-style teacher-student anomaly detection.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]].

### Shares Metric

- [[AU-ROC]] and [[AU-PRO]].

## Questions

- Does the paper release code for the FeaCali implementation and Simplex-noise synthesis?
- How does SACD perform on VisA or MVTec AD 2 under the same synthetic-anomaly protocol?
