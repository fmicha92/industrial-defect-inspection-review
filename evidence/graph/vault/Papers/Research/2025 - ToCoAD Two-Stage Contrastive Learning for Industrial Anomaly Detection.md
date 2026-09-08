---
title: "ToCoAD: Two-Stage Contrastive Learning for Industrial Anomaly Detection"
aliases:
  - "ToCoAD: Two-Stage Contrastive Learning for Industrial Anomaly Detection"
  - "ToCoAD"
paper_key: "doi:10.1109/tim.2025.3545987"
paper_type: research
year: 2025
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Yun Liang"
  - "Zhiguang Hu"
  - "Junjie Huang"
  - "Donglin Di"
  - "Anyang Su"
  - "Lei Fan"
status: processed
processed_at: 2026-06-12
topics:
  - "two-stage contrastive anomaly detection"
  - "negative-guided contrastive learning"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[BTAD]]"
methods:
  - "[[ToCoAD]]"
  - "[[Defect synthesis]]"
  - "[[Contrastive learning]]"
model_family:
  - "contrastive anomaly detector"
architectures:
  - "WideResNet50"
  - "inverse WideResNet50 discriminative network"
losses:
  - "contrastive loss"
  - "focal loss"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "PatchCore"
  - "PaDiM"
  - "CFLOW"
  - "DRAEM"
  - "FastFlow"
  - "PyramidFlow"
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[BTAD]]"
evaluation_protocol: "image-level and pixel-level AUROC on MVTec AD and VisA; pixel-level AUROC on BTAD"
doi: "10.1109/tim.2025.3545987"
url: "https://doi.org/10.1109/TIM.2025.3545987"
pdf: "paper-inbox/10_processed/Research/2025 - Liang - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection.pdf"
code: "not reported"
data: "not reported"
related_methods:
  - "[[ToCoAD]]"
  - "[[Defect synthesis]]"
  - "[[Contrastive learning]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[BTAD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
concept_notes_created_or_updated:
  - "[[ToCoAD]]"
source_file: "paper-inbox/10_processed/Research/2025 - Liang - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Liang - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Liang - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection.txt"
artifact_status: "not reported"
tags:
  - paper
---

# ToCoAD: Two-Stage Contrastive Learning for Industrial Anomaly Detection

## Summary

ToCoAD fine-tunes industrial anomaly features in two stages. Stage I trains a discriminative network on synthetic anomalies. Stage II freezes that network as a negative feature guide and fine-tunes the feature extractor with bootstrap contrastive learning, reducing the domain gap between ImageNet-pretrained features and industrial images. The paper reports 99.10% image-level and 98.21% pixel-level AUROC on [[MVTec AD]], 95.35% image-level and 98.43% pixel-level AUROC on [[VisA]], and 97.70% pixel-level AUROC on [[BTAD]].

## Paper Type

- Type: research.
- Why: It proposes a two-stage training strategy and evaluates it on industrial anomaly detection benchmarks.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: unsupervised industrial anomaly detection with only normal training images.
- Inputs: industrial inspection images.
- Outputs: image-level anomaly scores and pixel-level anomaly heatmaps.
- Motivation: frozen pretrained feature extractors can fail on industrial anomaly domains due to covariate shift and task mismatch.
- Assumptions: synthetic anomalies can train a discriminative network that later provides useful negative guidance for feature adaptation.

## Contribution

- Claimed: introduces a two-stage training strategy to bridge domain gaps between pretrained and target industrial features.
- Claimed: introduces negative-guided contrastive learning (NCL) for fine-tuning the feature extractor.
- Shown: competitive AUROC on MVTec AD, VisA, and BTAD.

## Method

- Core idea: use synthetic anomalies to train a discriminative network, then use that network to guide contrastive fine-tuning of the feature extractor.
- Architecture / algorithm: anomaly generator G, feature extractor F, discriminative network D, contrastive learning network, and memory bank M.
- Objective / loss: discriminative loss and contrastive loss; focal loss performs best in the reported loss ablation.
- Optimization: not reported.
- Training data: normal images from MVTec AD, VisA, and BTAD; synthetic anomalies from CutPaste, Perlin noise, or random patch generators.
- Data pipeline: generate pseudo anomalies, train D, fine-tune F with NCL, compress features into a memory bank with coreset subsampling, then use feature distances for localization.
- Augmentation / synthesis: CutPaste, random seamless patches, and Perlin noise are compared; Perlin noise gives the best MVTec AD AUROC.
- Inference: extract patch features, compare against memory-bank features, and produce anomaly maps.
- Complexity / deployment constraints: two separate training stages extend training time; memory-bank matching can slow inference as stored features increase.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[VisA]], [[BTAD]].
- Dataset details: MVTec AD has 15 categories with 3629 training and 1725 test images; VisA contains 12 subsets; BTAD has three industrial products with image sizes from 600 x 600 to 1600 x 1600.
- Feature extractor: ImageNet-pretrained WideResNet50; inverse WideResNet50 discriminative network.
- Baselines: PatchCore, PaDiM, CFLOW, DRAEM, FastFlow, PyramidFlow, FAPM, and other anomaly detection methods.
- Used performance metrics: image-level and pixel-level AUROC.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| ToCoAD | MVTec AD | image-level AUROC | higher | source baseline value not reported | 99.10% | Reported final result. |
| ToCoAD | MVTec AD | pixel-level AUROC | higher | source baseline value not reported | 98.21% | Reported final result. |
| ToCoAD | VisA | image-level AUROC | higher | source baseline value not reported | 95.35% | Perlin-noise generator setting. |
| ToCoAD | VisA | pixel-level AUROC | higher | source baseline value not reported | 98.43% | Perlin-noise generator setting. |
| ToCoAD | BTAD | pixel-level AUROC | higher | source baseline value not reported | 97.70% | Average over three categories. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level anomaly detection | area under ROC curve, percent | higher | yes | Reported on MVTec AD and VisA. |
| [[AU-ROC]] | pixel-level anomaly localization | area under ROC curve, percent | higher | yes | Reported on MVTec AD, VisA, and BTAD. |

### Ablations

- Hierarchy-level ablation: features from layers 3 and 4 worked best for contrastive learning.
- Two-stage ablation: NCL without discriminative negative guidance performed poorly; combining DNP and NCL improved pixel-level localization.
- Loss ablation: focal loss outperformed cross-entropy; alpha = 0.5 and gamma = 2 gave 98.82% image-level and 98.13% pixel-level AUROC.
- Anomaly generator ablation: Perlin noise achieved the best 99.10% image-level and 98.21% pixel-level AUROC on MVTec AD.
- Feature extractor ablation: WideResNet50 performed best; WideResNet101 was comparable but more resource-intensive, and ResNet50 declined slightly.

## Dataset / Benchmark Details

- [[MVTec AD]]: 15 industrial categories, 3629 training and 1725 test images.
- [[VisA]]: 12 subsets across object and PCB-style categories.
- [[BTAD]]: three industrial products, 600 x 600 to 1600 x 1600 images.
- License: not reported.

## Limitations

- Stated: two training sessions increase training time.
- Stated: inference depends on memory-bank feature matching and can slow down as stored features increase.
- Stated: heatmaps can show subtle background interference.

## Reproducibility

- Code: not reported.
- Data: public benchmarks named.
- Hyperparameters: focal loss alpha/gamma and hierarchy choices are reported in ablations; full training recipe is partly reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[ToCoAD]], [[Defect synthesis]], [[Contrastive learning]]
- Datasets: [[MVTec AD]], [[VisA]], [[BTAD]]
- Benchmarks: [[MVTec AD]], [[VisA]], [[BTAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Shares Dataset

- [[MVTec AD]], [[VisA]], and [[BTAD]] are the main evaluation benchmarks.

### Shares Method

- [[ToCoAD]]: central method.
- [[Defect synthesis]]: synthetic anomalies train the discriminative network.
- [[Contrastive learning]]: negative-guided contrastive learning adapts the feature extractor.

### Follow-Up Reading

- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] is cited in ToCoAD and is another synthetic-anomaly method from overlapping authors.

## Questions

- How does ToCoAD compare to newer foundation-model feature extractors that reduce ImageNet-domain mismatch?
- Can the memory-bank stage be compressed enough for real-time industrial deployment?
