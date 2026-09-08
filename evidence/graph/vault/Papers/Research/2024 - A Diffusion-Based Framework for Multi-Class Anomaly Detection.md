---
title: "A Diffusion-Based Framework for Multi-Class Anomaly Detection"
aliases:
  - "DiAD"
  - "Diffusion-based Anomaly Detection"
paper_key: "sha256:796caba20b23ed4f2d9a60134a075e87c742cbaffc0592f84fb2966a6a977073"
paper_type: research
year: 2024
venue: "AAAI 2024"
authors:
  - "Haoyang He"
  - "Jiangning Zhang"
  - "Hongxu Chen"
  - "Xuhai Chen"
  - "Zhishan Li"
  - "Xu Chen"
  - "Yabiao Wang"
  - "Chengjie Wang"
  - "Lei Xie"
status: processed
processed_at: 2026-05-22
audited_at: 2026-06-11
topics:
  - "multi-class anomaly detection"
  - "diffusion models"
  - "reconstruction-based anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
methods:
  - "[[DiAD]]"
  - "[[Diffusion models]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[ResNet50]]"
model_family:
  - "diffusion model"
  - "autoencoder"
  - "pretrained feature extractor"
optimizers:
  - "[[Adam]]"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUROC-cls/AP-cls/F1max-cls: image-level anomaly detection metrics; higher is better"
  - "AUROC-seg/AP-seg/F1max-seg/PRO: pixel-level anomaly localization metrics; higher is better"
baselines:
  - "DDPM"
  - "LDM"
  - "DRAEM"
  - "PaDiM"
  - "RD4AD"
  - "UniAD"
  - "reconstruction-based methods"
  - "embedding-based methods"
code: "https://lewandofskee.github.io/projects/diad"
data: "[[MVTec AD]], [[VisA]]"
doi: "10.1609/aaai.v38i8.28690"
arxiv: "not reported"
url: "https://doi.org/10.1609/aaai.v38i8.28690"
pdf: "paper-inbox/10_processed/Research/2024 - He - A Diffusion-Based Framework for Multi-Class Anomaly Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - He - A Diffusion-Based Framework for Multi-Class Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - He - A Diffusion-Based Framework for Multi-Class Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - He - A Diffusion-Based Framework for Multi-Class Anomaly Detection.txt"
artifact_status: "project page and code URL reported"
tags:
  - "paper"
  - "multi-class-anomaly-detection"
  - "diffusion-models"
---

# A Diffusion-Based Framework for Multi-Class Anomaly Detection

## Summary

DiAD is a diffusion-based reconstruction framework for multi-class anomaly detection. It combines a pixel-space autoencoder, a latent-space Semantic-Guided network connected to Stable Diffusion denoising, Spatial-aware Feature Fusion, and feature-space anomaly maps from a pretrained extractor. The paper evaluates a single multi-class model on MVTec AD and VisA and reports state-of-the-art results against both non-diffusion and diffusion baselines.

## Paper Type

- Type: research.
- Why: The paper proposes a new anomaly detection framework and evaluates it experimentally on established benchmarks.

## Problem

- Task: [[Industrial anomaly detection]] and pixel-level [[Defect segmentation]].
- Setting: unsupervised multi-class anomaly detection, where one model must handle multiple object and texture categories.
- Motivation: one-class-per-category anomaly detectors require increasing storage and training time as category count grows; direct DDPM and LDM reconstruction can lose category identity or semantic structure in the multi-class setting.

## Contribution

- Claimed: DiAD is a diffusion-based framework designed for multi-class anomaly detection rather than single-class reconstruction.
- Claimed: the Semantic-Guided network preserves input semantics while reconstructing anomalous regions.
- Claimed: Spatial-aware Feature Fusion integrates multi-scale features to improve reconstruction across small texture anomalies and large object defects.
- Shown: on multi-class MVTec AD, DiAD reports 97.2/99.0/96.5 for AUROC-cls/AP-cls/F1max-cls and 96.8/52.6/55.5 for AUROC-seg/AP-seg/F1max-seg.

## Method

- Pixel space: a pretrained autoencoder encodes the input into a latent representation and decodes the denoised latent representation back to the reconstructed image.
- Latent space: a Semantic-Guided network connects to the Stable Diffusion denoising network to reconstruct abnormal regions while preserving semantic information from the input image.
- Feature space: input and reconstructed images are passed through the same pretrained feature extractor; multi-scale feature differences produce anomaly maps.
- Spatial-aware Feature Fusion: fuses higher-scale semantic features into lower-scale features so the method can handle both texture anomalies and larger object defects.
- Normalization/activation: the paper reports improved results using instance normalization and SiLU rather than batch normalization and ReLU.

## ML / DL Extraction

### Model And Training

- Feature extractor: [[ResNet50]] is used by default; layers f2, f3, and f4 are used for anomaly score calculation.
- Preprocessing: MVTec AD and VisA images are resized to 256 x 256.
- Training: 1,000 epochs, batch size 12.
- Optimizer: [[Adam]] with learning rate 1e-5.
- Hardware: one NVIDIA Tesla V100 32GB.
- Inference: DDIM sampler with 10 steps by default; initial denoising timestep T is set from 1,000.
- Anomaly score: the image anomaly score is the maximum value of the averaged pooled anomaly localization score after 8 rounds of global average pooling with size 8 x 8.

### Data

- [[MVTec AD]]: 5,354 high-resolution images across 10 object and 5 texture categories; 3,629 anomaly-free training images and 1,725 test images with normal and abnormal samples.
- [[VisA]]: 10,821 high-resolution images, including 9,621 normal images and 1,200 anomaly images with 78 anomaly types across 12 subsets.

## Evidence

### Main Results

| Dataset | Level | Metrics | DiAD result |
|---|---|---|---|
| [[MVTec AD]] | image-level detection | AUROC-cls / AP-cls / F1max-cls | 97.2 / 99.0 / 96.5 |
| [[MVTec AD]] | pixel-level localization | AUROC-seg / AP-seg / F1max-seg | 96.8 / 52.6 / 55.5 |
| [[MVTec AD]] | pixel-level localization | PRO | 90.7 |
| [[VisA]] | image-level detection | AUROC-cls / AP-cls / F1max-cls | 86.8 / 88.3 / 85.1 |
| [[VisA]] | pixel-level localization | AUROC-seg / AP-seg / F1max-seg / PRO | 96.0 / 26.1 / 33.0 / 75.2 |

### Ablations

- Architecture: SD-only reaches 79.3 AUROC-cls and 89.5 AUROC-seg; the full method reaches 97.2 AUROC-cls and 96.8 AUROC-seg.
- Feature extractor: ResNet50 gives the best anomaly classification result among the tested backbones; WideResNet101 gives the best segmentation PRO.
- Diffusion timestep: performance declines when forward diffusion steps are below 600 because anomaly reconstruction is insufficient.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level detection and pixel-level localization | area under ROC curve | higher | yes | MVTec AD 97.2 AUROC-cls and 96.8 AUROC-seg; VisA 86.8 AUROC-cls and 96.0 AUROC-seg |
| [[Average precision]] | image-level detection and pixel-level localization | AP under precision-recall ranking | higher | no | MVTec AD 99.0 AP-cls and 52.6 AP-seg; VisA 88.3 AP-cls and 26.1 AP-seg |
| [[F1-score]] | image-level detection and pixel-level localization | maximum F1 over thresholds | higher | no | MVTec AD 96.5 F1max-cls and 55.5 F1max-seg; VisA 85.1 F1max-cls and 33.0 F1max-seg |
| [[AU-PRO]] | anomaly localization | per-region overlap area | higher | no | MVTec AD PRO 90.7; VisA PRO 75.2 |

## Limitations

- The paper states that DiAD can be susceptible to background impurities, causing localization and classification errors.
- Future work proposed by the paper includes improving background anti-interference, adding multimodal assistance, and using larger models to improve reconstruction.
- End-to-end inference latency is not reported.

## Reproducibility

- Code: https://lewandofskee.github.io/projects/diad.
- Hardware: one NVIDIA Tesla V100 32GB.
- Training recipe: 1,000 epochs, batch size 12, Adam, learning rate 1e-5.
- Preprocessing: resize images to 256 x 256.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[DiAD]], [[Diffusion models]], [[Unsupervised anomaly detection]]
- Feature extractor / optimizer: [[ResNet50]], [[Adam]]
- Datasets: [[MVTec AD]], [[VisA]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]], [[F1-score]], [[AU-PRO]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Shares dataset | DiAD reports multi-class anomaly detection and localization on MVTec AD. |
| [[VisA]] | Shares dataset | DiAD evaluates the framework on VisA. |
| [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] | Shares task | Both target multi-class anomaly detection; DiAD uses diffusion-guided reconstruction while OmniAL uses CNN reconstruction/localization. |
| [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] | Shares task | Both are reconstruction-centered anomaly detection methods; OCR-GAN focuses on frequency reconstruction while DiAD uses diffusion-guided reconstruction. |

## Questions

- How stable is DiAD when the input category is outside Stable Diffusion pretraining priors?
- What inference cost is introduced by the diffusion-denoising connection?
