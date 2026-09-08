---
title: "A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization"
aliases:
  - "GLASS"
paper_key: "arxiv:2407.09359"
paper_type: research
year: 2024
venue: "arXiv"
authors:
  - "Qiyu Chen"
  - "Huiyuan Luo"
  - "Chengkan Lv"
  - "Zhengtao Zhang"
status: processed
processed_at: 2026-05-23
audited_at: 2026-06-11
topics:
  - "gradient ascent anomaly synthesis"
  - "industrial anomaly detection"
  - "weak defect detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MPDD]]"
  - "[[Woven fabric defect dataset]]"
methods:
  - "[[GLASS]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
  - "WideResNet50"
  - "[[Adam]]"
losses:
  - "BCE loss"
  - "Focal loss"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "Image-level AUROC: anomaly detection discrimination; higher is better"
  - "Pixel-level AUROC: anomaly localization discrimination; higher is better"
  - "Pixel-level PRO: per-region overlap localization score; higher is better"
baselines:
  - "DSR"
  - "PatchCore"
  - "BGAD"
  - "RD++"
  - "SimpleNet"
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MPDD]]"
  - "[[Woven fabric defect dataset]]"
code: "https://github.com/cqylunlun/GLASS"
data: "dataset reported available with code"
doi: "not reported"
arxiv: "2407.09359"
url: "https://arxiv.org/abs/2407.09359"
pdf: "paper-inbox/10_processed/Research/2024 - Chen - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization.pdf"
related_methods:
  - "[[GLASS]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MPDD]]"
  - "[[Woven fabric defect dataset]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Chen - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Chen - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Chen - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization.txt"
artifact_status: "code and dataset reported available"
tags:
  - paper
---
# A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization

## Summary

The paper proposes GLASS, a Global and Local Anomaly co-Synthesis Strategy for unsupervised industrial anomaly detection and localization. GLASS combines feature-level Global Anomaly Synthesis (GAS), which uses Gaussian noise guided by gradient ascent and truncated projection, with image-level Local Anomaly Synthesis (LAS), which overlays augmented DTD textures through Perlin and foreground masks. The paper reports state-of-the-art results on MVTec AD, VisA, MPDD, and a woven fabric defect dataset, with particular gains on weak defects.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a new anomaly synthesis and detection framework.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: unsupervised industrial inspection where defect samples and pixel labels are scarce.
- Motivation: image-level synthesis provides detailed textures but limited diversity and realism, while feature-level synthesis is efficient but lacks controllable synthesis directions for near-in-distribution weak defects.

## Contribution

- Claimed: GLASS synthesizes broader anomaly coverage at both feature and image levels.
- Claimed: GAS uses gradient ascent and truncated projection to synthesize controllable near-in-distribution anomalies for weak defect detection.
- Claimed: LAS supplies stronger local texture anomalies far from normal samples.
- Shown: GLASS-j reports 99.9 image-level AUROC, 99.3 pixel-level AUROC, and 96.8 PRO on MVTec AD.

## Method

- Normal branch: frozen feature extractor and trainable feature adaptor produce adapted normal features.
- GAS branch: creates global anomaly features by adding Gaussian noise to normal features, following the gradient ascent direction of the GAS loss, and constraining the result with truncated projection.
- LAS branch: creates local anomaly images using Perlin masks, foreground masks, DTD textures, random augmentations, and transparency-controlled overlay fusion.
- Discriminator: single-hidden-layer MLP with Sigmoid outputs anomaly confidence for each feature point.
- Losses: BCE for normal features, BCE for GAS features, Focal loss for LAS features, and OHEM on the LAS loss.
- Inference: only the normal branch is used; the discriminator output is resized and smoothed for pixel-level anomaly localization, and the image-level anomaly score is the maximum point value.

## ML / DL Extraction

- Backbone: WideResNet50 by default; features from level2 and level3 are merged.
- Neighborhood size: 3.
- Image preprocessing: resized and center-cropped to 288 x 288.
- LAS transparency: beta sampled from `N(0.5, 0.1^2)` and truncated to `[0.2, 0.8]`.
- GAS noise: Gaussian noise sampled from `N(0, 0.015^2)`.
- GLASS-m: manifold hypothesis with `r1 = 1`, `r2 = 2`.
- GLASS-h: hypersphere hypothesis.
- GLASS-j: hybrid strategy selected by image-level spectrogram analysis.
- Optimizer: Adam, with learning rates 0.0001 for the feature adaptor and 0.0002 for the discriminator.
- Training: 640 epochs, batch size 8.
- Hardware: NVIDIA Tesla A800 GPU and Intel Xeon Gold 6346 CPU at 3.10 GHz.

## Evidence

### Benchmark Results

| Dataset | GLASS variant | Image AUROC | Pixel AUROC | Pixel PRO |
|---|---|---:|---:|---:|
| [[MVTec AD]] | GLASS-j | 99.9 | 99.3 | 96.8 |
| [[VisA]] | GLASS-j | 98.8 | 98.8 | 92.8 |
| [[MPDD]] | GLASS-j | 99.6 | 99.4 | 98.2 |
| [[Woven fabric defect dataset]] | GLASS-j | 100.0 | 98.9 | 94.9 |
| Average over four datasets | GLASS-j | 99.6 | 99.1 | 95.7 |

### Weak Defect Results

| Test set | GLASS image AUROC | GLASS pixel AUROC | GLASS PRO | Notes |
|---|---:|---:|---:|---|
| MAD-man | 99.6 | 99.3 | 97.5 | weak MVTec AD samples manually selected by five people |
| MAD-sys | 95.6 | 93.3 | 80.3 | synthetic weak defects from MVTec AD textures |
| Average | 97.6 | 96.3 | 88.9 | higher than all listed baselines |

### Ablation

- LAS alone: 98.2 / 95.4 / 88.0 on MVTec AD.
- GAS with Gaussian noise only: 99.4 / 98.1 / 91.8 on MVTec AD.
- GAS with Gaussian noise plus gradient ascent: 99.5 / 98.9 / 94.7 on MVTec AD.
- GAS with Gaussian noise, gradient ascent, and truncated projection: 99.6 / 99.0 / 95.9 on MVTec AD.
- LAS plus full GAS: 99.7 / 99.1 / 96.4 on MVTec AD.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level detection and pixel-level localization | area under ROC curve | higher | yes | reported for all benchmark datasets |
| [[AU-PRO]] | pixel-level anomaly localization | per-region overlap score | higher | no | reported as PRO in tables |

## Dataset / Benchmark Details

- Public benchmarks: MVTec AD, VisA, and MPDD.
- WFDD: woven fabric defect detection dataset constructed for industrial settings with 3,860 normal and 241 anomaly samples.
- MAD-man: weak-defect test set manually selected from MVTec AD by five individuals.
- MAD-sys: synthetic weak-defect test set from five MVTec AD texture categories with beta values `{0.1, 0.3, 0.5, 0.7}`.

## Limitations

- The paper states that GLASS mainly focuses on localizing structural anomalies in industrial scenarios.
- Logical anomalies are not extensively explored.
- Future work includes applying GLASS to logical anomaly detection and anomaly synthesis without auxiliary texture datasets.

## Reproducibility

- Code and dataset: https://github.com/cqylunlun/GLASS.
- Hardware: NVIDIA Tesla A800 GPU and Intel Xeon Gold 6346 CPU.
- Training: 640 epochs, batch size 8, Adam.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[GLASS]], [[Synthetic data generation]], [[Data augmentation]], [[Adam]]
- Datasets: [[MVTec AD]], [[VisA]], [[MPDD]], [[Woven fabric defect dataset]]
- Domains: [[Multi-industry anomaly detection]], [[Textile and fiber inspection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Relationship Notes

- Shares method: [[GLASS]] synthesizes anomalies through feature-level GAS and image-level LAS.
- Shares datasets: [[MVTec AD]], [[VisA]], [[MPDD]], and [[Woven fabric defect dataset]].
- Shares task: [[Industrial anomaly detection]] and weak-defect localization.
- Application/domain: [[Multi-industry anomaly detection]] and [[Textile and fiber inspection]].

## Questions

- How does GLASS behave on logical anomaly benchmarks where defects are not local texture or structure changes?
- Can LAS be redesigned to remove the dependency on auxiliary texture datasets?
