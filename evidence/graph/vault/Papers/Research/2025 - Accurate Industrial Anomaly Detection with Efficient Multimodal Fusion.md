---
title: "Accurate industrial anomaly detection with efficient multimodal fusion"
aliases:
  - "Accurate industrial anomaly detection with efficient multimodal fusion"
paper_key: "sha256:a76bb886db3f736d8103741a70ca452a56a538f66d6ecede310c80e809d4dc2f"
paper_type: research
year: 2025
venue: "Array"
authors:
  - "Dinh-Cuong Hoang"
  - "Phan Xuan Tan"
  - "Anh-Nhat Nguyen"
  - "Ta Huu Anh Duong"
  - "Tuan-Minh Huynh"
  - "Duc-Manh Nguyen"
  - "Minh-Duc Cao"
  - "Duc-Huy Ngo"
  - "Thu-Uyen Nguyen"
  - "Khanh-Toan Phan"
  - "Minh-Quang Do"
  - "Xuan-Tung Dinh"
  - "Van-Hiep Duong"
  - "Ngoc-Anh Hoang"
  - "Van-Thiep Nguyen"
status: processed
processed_at: 2026-06-12
topics:
  - "multimodal industrial anomaly detection"
  - "RGBD fusion"
  - "attention-guided synthetic perturbation"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
methods:
  - "[[Synthetic data generation]]"
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
model_family:
  - "[[ResNet50]]"
architectures:
  - "[[ResNet50]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
baselines:
  - "RGB-only anomaly detection methods"
  - "RGBD fusion methods"
  - "Unmodulated Gaussian perturbation"
  - "No modality dropout"
code: "not reported"
data: "uses MVTec AD, VisA, and a RealSense D435i RGBD dataset"
doi: "10.1016/j.array.2025.100512"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.array.2025.100512"
pdf: "paper-inbox/10_processed/Research/2025 - Hoang - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion.pdf"
related_methods:
  - "[[Synthetic data generation]]"
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2025 - Hoang - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Hoang - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Hoang - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Accurate industrial anomaly detection with efficient multimodal fusion

## Summary

The paper proposes an efficient RGBD industrial anomaly detection framework with modality-specific feature enhancement, hierarchical multimodal fusion, an anomalous feature generator, and modality-dropout augmentation. It evaluates on [[MVTec AD]], [[VisA]], and a newly collected RealSense D435i RGBD dataset, reporting 99.6% image-level AUROC and 99.0% pixel-level AUROC on MVTec AD, plus 99.0% pixel-level AUROC on VisA.

## Paper Type

- Type: research.
- Why: It proposes a multimodal anomaly detection architecture and reports benchmark, robustness, efficiency, and ablation results.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: RGBD industrial anomaly detection, including estimated depth for RGB-only public benchmarks.
- Inputs: RGB images and depth maps, with depth estimated for MVTec AD and VisA using Depth Anything.
- Outputs: image-level anomaly scores and pixel-level anomaly maps.
- Motivation: RGB-only methods miss geometric defects, while RGBD fusion can be expensive or brittle when modalities are missing.
- Assumptions: attention-guided synthetic perturbations and modality dropout can improve robust multimodal anomaly localization.

## Contribution

- Claimed: Introduces modality-specific feature enhancement and hierarchical multimodal fusion for efficient RGBD industrial anomaly detection.
- Claimed: Uses curriculum-based training with synthetic anomaly perturbations and modality dropout.
- Shown: Improves pixel-level AUROC and AUPRO on MVTec AD and VisA while running at 45 FPS.

## Method

- Core idea: train a shared-backbone RGBD fusion model with synthetic perturbations and a discriminator so fused RGB/depth features separate normal from anomalous patterns.
- Architecture / algorithm: shared ResNet-50 backbone, modality-specific feature enhancement blocks, hierarchical multimodal fusion modules, anomalous feature generator, and discriminator.
- Objective / loss: discriminator-based anomaly scoring with generated synthetic anomaly features; exact loss details are partially reported in extracted equations but not fully reconstructed.
- Training data: MVTec AD, VisA, and a RealSense D435i RGBD dataset.
- Data pipeline: RGB inputs resized; public RGB datasets are paired with estimated depth from Depth Anything.
- Augmentation / synthesis: attention-guided synthetic perturbations modulated by attention maps; modality-dropout augmentation for missing-modality robustness.
- Inference: RGBD anomaly maps at real-time speed; also evaluated under RGB-only and depth-only settings.
- Complexity / deployment constraints: reports 45 FPS on 480 x 480 RGBD inputs.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[VisA]], and a RealSense D435i RGBD dataset.
- Splits: not fully reported in extracted text; MVTec AD and VisA follow public benchmark protocols.
- Baselines: RGB-only and RGBD anomaly detection baselines, plus ablations without MSFE, without attention modulation, without dropout, and without isolation-stage training.
- Used performance metrics: image-level AUROC, pixel-level AUROC, AUPRO, FPS.
- Compute: not fully reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| MVTec AD benchmark | MVTec AD localization | P-AUROC / AUPRO (%) | higher | 98.6 / 80.5 | 99.0 / 82.6 | Source identifies Hyun et al. at 98.6 P-AUROC and Costanzino et al. at 80.5 AUPRO as prior strong baselines. |
| VisA benchmark | VisA localization | P-AUROC / AUPRO (%) | higher | 98.4 / about 78-79 | 99.0 / 80.5 | Source says RGBD distillation baselines report no higher than 98.4 P-AUROC and AUPRO around 78-79. |
| Attention-guided perturbation vs no attention modulation | Average ablation | P-AUROC / AUPRO (%) | higher | 95.3 / 76.6 | 98.2 / 81.1 | Both use sigma=0.02; attention modulation is the isolated change. |
| Full model vs no MSFE | Average ablation | P-AUROC / AUPRO (%) | higher | 94.0 / 74.5 | 98.2 / 81.1 | Shows contribution of modality-specific enhancement. |
| Full training vs no isolation stage | Average ablation | P-AUROC / AUPRO (%) | higher | 93.9 / 69.6 | 98.2 / 81.1 | Curriculum isolation stage ablation. |
| Modality dropout vs no dropout | Average ablation | P-AUROC / AUPRO (%) | higher | 95.6 / 72.4 | 98.2 / 81.1 | Moderate 20% dropout is the reported default. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection | I-AUROC percent | higher | yes | Reported for MVTec AD, VisA, and RGBD dataset. |
| [[AU-ROC]] | Pixel-level anomaly localization | P-AUROC percent | higher | yes | Main localization metric. |
| [[AU-PRO]] | Region-level localization | AUPRO percent | higher | no | Integrated PRO, typically up to FPR 0.1. |
| FPS | Inference efficiency | frames per second | higher | no | Full model reports 45 FPS. |

### Ablations

- Attention-guided perturbation at sigma=0.02 improves over unmodulated Gaussian perturbation at the same sigma.
- MSFE, hierarchical fusion, two-stage training, and 20% modality dropout all improve the average results.
- Shared ResNet50 is nearly as accurate as a separate-backbone variant while being more deployable.

## ML / DL Extraction

### Data

- Datasets: [[MVTec AD]], [[VisA]], and RealSense D435i RGBD dataset.
- Data source: public RGB industrial datasets plus depth estimated by Depth Anything for MVTec AD and VisA.
- Dataset size: source says the RealSense dataset has 20,000 RGBD images; MVTec AD and VisA sizes are described but exact split numbers are not fully needed for the method result.
- Labels / annotations: image-level and pixel-level anomaly labels/masks for MVTec AD and VisA; RGBD dataset also has anomaly segmentations.
- Preprocessing: MVTec AD and VisA RGB images are resized; depth maps generated for public RGB datasets.
- Augmentation: modality dropout and synthetic perturbations.
- Synthetic data: attention-guided perturbations create synthetic anomalous features/images for training.
- Leakage checks: not reported.

### Evaluation

- Protocol: benchmark comparisons and ablations across MVTec AD, VisA, and the RGBD dataset.
- Baselines: multiple RGB-only and RGBD methods; extracted table columns are partially fragmented, so only source-explicit aggregate comparisons are recorded above.
- Statistical tests: not reported.
- Failure cases: estimated depth introduces noise and causes performance drops compared with real depth.

## Limitations

- Stated: performance decreases when depth is estimated or degraded.
- Inferred: MVTec AD and VisA are RGB datasets, so RGBD conclusions on them depend on depth-estimation quality rather than captured depth.

## Reproducibility

- Code: not reported.
- Data: public MVTec AD and VisA; RealSense dataset availability not reported in extracted text.
- Hyperparameters: attention-guided perturbation sigma=0.02 and 20% modality dropout are reported as defaults.
- Random seeds: not reported.
- Environment: not fully reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Synthetic data generation]], [[Defect synthesis]], [[Data augmentation]], [[ResNet50]]
- Datasets: [[MVTec AD]], [[VisA]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Shares Dataset

- [[MVTec AD]] and [[VisA]]: public industrial anomaly benchmarks.

### Shares Method

- [[Synthetic data generation]], [[Defect synthesis]], and [[Data augmentation]]: synthetic perturbations and modality dropout are core training components.
- [[ResNet50]]: shared backbone.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]].

### Shares Metric

- [[AU-ROC]] and [[AU-PRO]].

## Questions

- Is the RealSense D435i RGBD dataset public, and under what license?
- Are the MVTec AD and VisA depth-estimation preprocessing scripts released?
