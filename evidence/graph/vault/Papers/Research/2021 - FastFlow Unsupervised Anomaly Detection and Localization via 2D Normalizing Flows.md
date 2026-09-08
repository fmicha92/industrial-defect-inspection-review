---
title: "FastFlow: Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows"
aliases:
  - "FastFlow"
paper_key: "arxiv:2111.07677"
paper_type: research
year: 2021
venue: "arXiv"
authors:
  - "Jiawei Yu"
  - "Ye Zheng"
  - "Xiang Wang"
  - "Wei Li"
  - "Yushuang Wu"
  - "Rui Zhao"
  - "Liwei Wu"
status: processed
processed_at: 2026-05-22
topics:
  - "unsupervised anomaly detection"
  - "anomaly localization"
  - "normalizing flows"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[FastFlow]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
model_family:
  - "normalizing flows"
  - "convolutional neural network"
  - "vision transformer feature extractor"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  AU-ROC: "Higher is better; reported at image level for anomaly detection and pixel level for anomaly localization."
baselines:
  - "PatchCore"
  - "PaDiM"
  - "CFlow-AD"
  - "DifferNet"
  - "SPADE"
  - "PatchSVDD"
  - "CutPaste"
  - "VT-ADL"
code: "not reported"
data: "[[MVTec AD]]"
doi: "not reported"
arxiv: "2111.07677"
url: "https://arxiv.org/abs/2111.07677"
pdf: "paper-inbox/10_processed/Research/2021 - Yu - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Yu - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Yu - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Yu - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows.txt"
artifact_status: "processed"
tags:
  - "paper"
  - "unsupervised-anomaly-detection"
  - "anomaly-localization"
---

# FastFlow: Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows

## Summary

- The paper proposes FastFlow, a 2D normalizing-flow module for unsupervised anomaly detection and pixel localization from pretrained visual features.
- FastFlow keeps feature maps in two-dimensional form instead of flattening patches, which preserves spatial relationships and supports image-level inference.
- Experiments on MVTec AD report 99.4% anomaly-detection AUC with high inference efficiency.
- The method is evaluated on [[MVTec AD]], BTAD, and CIFAR-10, with MVTec AD as the main industrial anomaly-detection benchmark.

## Contribution

- Claimed: 2D normalizing flows with fully convolutional subnetworks model local and global feature distributions for anomaly detection and localization.
- Shown: FastFlow is evaluated with CNN and transformer feature extractors on MVTec AD and reports 99.4% detection AUC.
- Inferred: The method is most useful when only normal training images are available and a compact density estimator is needed on top of fixed features.

## Method

- A pretrained feature extractor produces visual feature maps.
- FastFlow transforms feature maps into a tractable base distribution and uses likelihood-derived scores at inference time.
- The architecture avoids sliding-window patch inference by processing whole feature maps end to end.
- Vision transformer backbones use one selected feature layer; ResNet backbones use the last layer of the first three blocks and average the resulting flow outputs.
- The flow subnet uses 2D convolutional affine coupling layers; the paper selects alternating 3 x 3 and 1 x 1 flow steps for DeiT, CaiT, and Wide-ResNet50-2, and 3 x 3-only flow steps for ResNet18.
- FastFlow is trained only on normal images and upsamples the summed 2D likelihood map to the input image resolution for pixel-level anomaly localization.

## Training And Implementation

| Item | Source-backed detail |
|---|---|
| Feature extractors | CaiT-M48-distilled, DeiT-base-distilled, ResNet18, and Wide-ResNet50-2, initialized from ImageNet and frozen. |
| Flow depth | 20 flow steps for CaiT and DeiT; 8 flow steps for ResNet18 and Wide-ResNet50-2. |
| Optimizer | Adam, learning rate 1e-3, weight decay 1e-5. |
| Schedule | 500 epochs, batch size 32. |
| Input sizes | CaiT 448, DeiT 384, ResNet18 256, Wide-ResNet50-2 256. |
| Hardware for complexity analysis | Intel Xeon E5-2680 V4 at 2.4 GHz and NVIDIA GeForce GTX 1080Ti. |

## Evidence

### Performance Metrics

| Metric | Direction | Evaluation context | Reported values |
|---|---|---|---|
| [[AU-ROC]] | Higher is better | [[MVTec AD]] image-level anomaly detection and pixel-level localization | Best FastFlow result is 99.4 image-level AUC and 98.5 pixel-level AUC. |
| [[AU-ROC]] | Higher is better | BTAD pixel-level localization | Mean pixel-level AUC is 0.97. |
| [[AU-ROC]] | Higher is better | CIFAR-10 anomaly detection | Mean AUC is 66.7. |

### MVTec AD Results

| Method | Mean image-level AUC | Mean pixel-level AUC |
|---|---:|---:|
| PatchSVDD | 92.1 | 95.7 |
| SPADE | 96.2 | 96.5 |
| DifferNet | 94.9 | pixel-level value absent from the comparison table |
| PaDiM | 97.9 | 97.5 |
| CutPaste | 97.1 | 96.0 |
| PatchCore | 99.1 | 98.1 |
| CFlow | 98.3 | 98.6 |
| FastFlow | 99.4 | 98.5 |

### Efficiency Results

| Backbone + method | FPS | Additional time | Additional parameters | Image AUC | Pixel AUC |
|---|---:|---:|---:|---:|---:|
| CaiT + PatchCore | 2.39 | 107 ms | 0 M | 97.9 | 96.5 |
| CaiT + CFlow | 2.76 | 42 ms | 10.5 M | 97.7 | 96.2 |
| CaiT + FastFlow | 3.08 | 9 ms | 14.8 M | 99.4 | 98.5 |
| DeiT + FastFlow | 30.14 | 8 ms | 14.8 M | 98.7 | 98.1 |
| ResNet18 + FastFlow | 30.8 | 27 ms | 4.9 M | 97.9 | 97.2 |
| Wide-ResNet50-2 + FastFlow | 21.8 | 34 ms | 41.3 M | 99.3 | 98.1 |

### Additional Evaluations

- On BTAD, FastFlow reports category pixel-level AUC values of 0.95, 0.96, and 0.99, with mean 0.97.
- On CIFAR-10 one-vs-rest anomaly detection, FastFlow reports mean AUC 66.7, above OCGAN at 65.6 and DSVDD at 64.8 in the reported table.
- On a non-aligned disturbed MVTec AD test set built with random zoom, rotation, and translation, CaiT-based FastFlow reports 99.2 image-level AUC and 98.1 pixel-level AUC.

## Limitations

- The strongest industrial evidence is [[MVTec AD]]; BTAD is smaller, and CIFAR-10 is a semantic anomaly-detection setting rather than industrial inspection.
- The approach depends on pretrained feature quality and normal-only training coverage.
- Bad cases include missed small or unobvious anomalies, false detections in background hair or dirt, and label ambiguity where the model marks regions that appear abnormal but are not labeled.
- Some MVTec AD categories are unsuitable for aggressive flipping or rotation augmentation; the paper explicitly notes transistor as an example.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[FastFlow]], [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Shares dataset | FastFlow evaluates unsupervised anomaly detection and localization on this benchmark. |
| [[Unsupervised anomaly detection]] | Shares method | The method models normal training features and scores deviations at inference. |
| [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] | Shares task | Both address normal-only industrial anomaly localization, but FastFlow uses flow likelihoods while CDO optimizes feature discrepancy distributions. |
| [[AU-ROC]] | Shares metric | FastFlow reports image-level and pixel-level AUROC across MVTec AD, BTAD, CIFAR-10, and perturbed MVTec AD evaluations. |

## Questions

- How much of the reported performance comes from the feature extractor versus the flow estimator?
- Does the 2D flow remain efficient on high-resolution industrial images beyond MVTec AD?
