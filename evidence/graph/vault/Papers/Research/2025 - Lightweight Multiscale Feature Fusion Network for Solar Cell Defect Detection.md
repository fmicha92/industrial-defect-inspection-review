---
title: "A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection"
aliases:
  - "LMFF for Solar Cell Defect Detection"
paper_key: "doi:10.32604/cmc.2024.058063"
paper_type: "research"
year: 2025
venue: "Computers, Materials & Continua"
authors:
  - "Xiaoyun Chen"
  - "Lanyao Zhang"
  - "Xiaoling Chen"
  - "Yigang Cen"
  - "Linna Zhang"
  - "Fugui Zhang"
status: "processed"
topics:
  - "solar cell defect segmentation"
  - "lightweight segmentation networks"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[Dataset of Solar Cells Defect Segmentation]]"
  - "[[PVEL-AD]]"
methods:
  - "[[LMFF]]"
  - "[[Depthwise separable convolution]]"
  - "[[Segmentation Models]]"
  - "[[Computer Vision Models]]"
model_family:
  - "[[Segmentation Models]]"
  - "[[Computer Vision Models]]"
architectures:
  - "[[LMFF]]"
  - "[[U-Net]]"
metrics:
  - "[[IoU]]"
  - "[[mIoU]]"
  - "[[F1-score]]"
  - "[[Foreground pixel accuracy]]"
  - "[[Background pixel accuracy]]"
  - "[[Mean pixel accuracy]]"
  - "[[Inference time]]"
  - "[[FPS]]"
  - "[[GFLOPs]]"
  - "[[Parameter count]]"
primary_metric: "[[IoU]]"
metric_definitions:
  - "IoU: TP / (TP + FP + FN)"
  - "mIoU: average of foreground and background IoU terms"
  - "F1-score: 2TP / (2TP + FP + FN)"
  - "FPA: TP / (TP + FN)"
  - "BPA: TN / (TN + FP)"
  - "MPA: (FPA + BPA) / 2"
baselines:
  - "FCN"
  - "Deeplab-v3"
  - "U-Net"
  - "U2-Net"
benchmarks:
  - "SolarCells"
  - "SolarCells-S"
  - "PVEL-S"
code: "not reported"
data: "https://www.kaggle.com/datasets/xiaoyunchen666/dataset-of-solar-cells-defect-segmentation"
doi: "10.32604/cmc.2024.058063"
arxiv: "not reported"
url: "https://doi.org/10.32604/cmc.2024.058063"
pdf: "paper-inbox/10_processed/Research/2025 - Chen - A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2025 - Chen - A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Chen - A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Chen - A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection.txt"
related_papers:
  - "[[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]]"
  - "[[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]]"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[LMFF]]"
  - "[[Depthwise separable convolution]]"
  - "[[U-Net]]"
related_datasets:
  - "[[Dataset of Solar Cells Defect Segmentation]]"
  - "[[PVEL-AD]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "SolarCells"
  - "SolarCells-S"
  - "PVEL-S"
processed_at: "2026-05-29"
---
# A Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection

## Summary

The paper proposes [[LMFF]], a lightweight semantic segmentation network for defect localization in solar-cell electroluminescence images. LMFF uses [[Depthwise separable convolution]] in depthwise separable residual blocks to reduce parameters, fuses multi-scale feature maps with an MFF module, and uses a multi-scale attention module to improve small-defect segmentation.

The paper also introduces [[Dataset of Solar Cells Defect Segmentation]], a Kaggle-hosted release containing SolarCells, SolarCells-S, and PVEL-S. LMFF is evaluated on all three datasets and reports the best or strongest listed segmentation metrics against FCN, Deeplab-v3, [[U-Net]], and U2-Net, while keeping low parameter count and high throughput.

## Paper Type

Research paper. It introduces both a lightweight segmentation architecture and new solar-cell defect segmentation datasets with refined labels.

## Problem

Solar cell defect detection in EL images is difficult because defect samples are scarce, defect locations and shapes are random, monocrystalline and polycrystalline cells have different texture backgrounds, and small defects can be missed by coarse detectors or heavy segmentation models.

## Contribution

- Introduces SolarCells, SolarCells-S, and PVEL-S as refined-label datasets for semantic segmentation of solar-cell defects.
- Proposes [[LMFF]], an end-to-end lightweight segmentation network with depthwise separable residual blocks.
- Adds multi-scale feature fusion and multi-scale attention to improve localization of small and irregular defects.
- Reports segmentation accuracy and efficiency against FCN, Deeplab-v3, [[U-Net]], and U2-Net.

## Method

LMFF contains a feature extraction network, multi-scale feature fusion module, and segmentation network. The feature extractor keeps the last three feature layers and discards the first layer to avoid redundant low-level detail and computation. The MFF module resizes, unfolds, averages, and concatenates these feature layers so the segmentation stage receives both shallow texture features and deeper semantic information.

The segmentation network uses a multi-scale attention module with multiple convolution-kernel sizes, spatial attention, and channel attention. The model is trained with a combined cross-entropy and Dice loss to address foreground/background imbalance in defect masks.

## Evidence

### Datasets

| Dataset | Source/material | Size and split | Notes |
|---|---|---|---|
| SolarCells | monocrystalline silicon-cell EL defect images collected from the web | 190 images, 152 train and 38 test | 448 x 448 resolution |
| SolarCells-S | monocrystalline EL defect images from a partner company | 36 original images, 28 train and 8 test; augmented to 144 train and 36 test | augmentation uses 180-degree rotation, mirroring, darkening, and brightening |
| PVEL-S | subset of [[PVEL-AD]] | 1200 polysilicon defect images, 960 train and 240 test | selected from PVEL-AD and pixel-level labeled |

### Implementation

| Setting | Value |
|---|---|
| Input resolution | 480 x 480 |
| Feature layer shapes | 64 x 120 x 120, 128 x 60 x 60, 256 x 30 x 30 |
| Multi-scale fusion feature | 448 x 60 x 60 |
| Optimizer | SGD |
| Learning rate | 0.01 |
| Momentum | 0.9 |
| Batch size | 8 |
| Loss weights | lambda_D = 1, lambda_C = 1 |
| Hardware | Intel Core i9-10900X CPU and NVIDIA GeForce RTX 3080 Ti |

### Performance Metrics

| Metric | Definition | Direction | Primary | Context |
|---|---|---|---|---|
| [[IoU]] | `TP / (TP + FP + FN)` | higher | yes | defect mask overlap |
| [[mIoU]] | average foreground/background IoU terms | higher | no | category-average segmentation overlap |
| [[F1-score]] | `2TP / (2TP + FP + FN)` | higher | no | balances missed and false defect pixels |
| [[Foreground pixel accuracy]] | `TP / (TP + FN)` | higher | no | foreground defect-pixel identification |
| [[Background pixel accuracy]] | `TN / (TN + FP)` | higher | no | background/non-defect-pixel identification |
| [[Mean pixel accuracy]] | `(FPA + BPA) / 2` | higher | no | average pixel accuracy |
| [[Inference time]] | milliseconds per image | lower | no | deployment efficiency |
| [[FPS]] | frames per second | higher | no | deployment throughput |
| [[GFLOPs]] | floating-point operations | lower | no | model complexity |
| [[Parameter count]] | trainable parameters | lower | no | model size |

### Reported Results

| Dataset | Method | IoU | mIoU | F1-score | FPA | BPA | MPA |
|---|---|---:|---:|---:|---:|---:|---:|
| SolarCells | LMFF | 68.5 | 82.9 | 81.3 | 87.8 | 98.1 | 93.0 |
| SolarCells-S | LMFF | 51.0 | 74.0 | 67.5 | 67.2 | 98.6 | 82.9 |
| PVEL-S | LMFF | 92.7 | 95.5 | 96.2 | 98.3 | 98.6 | 98.5 |

LMFF reports 5.66 ms inference time, 176.6 FPS, 6.51 GFLOPs, and 1.18M parameters. Compared with U-Net, LMFF is slightly slower by inference time in the paper's table but uses far fewer operations and parameters.

### Ablations

- Replacing conventional residual blocks with depthwise separable residual blocks slightly reduces IoU/mIoU but improves efficiency: 5.66 ms versus 6.71 ms, 176.60 FPS versus 148.07 FPS, 6.51 GFLOPs versus 41.62 GFLOPs, and 1.18M versus 7.04M parameters.
- The MFF module improves most reported metrics by combining shallow texture information and deeper semantic features.
- The MSA module further improves segmentation by adding spatial and channel attention over multi-scale branches.
- Combining cross-entropy loss and Dice loss performs better than using either loss alone.

## ML/DL Extraction

- Task formulation: pixel-level defect segmentation for solar-cell EL images.
- Inputs: electroluminescence images of monocrystalline and polycrystalline solar cells.
- Outputs: segmentation masks for defective regions.
- Architecture: feature extraction network, MFF module, DSR block, MSA module, upsampled segmentation output.
- Losses: cross-entropy loss plus Dice loss.
- Optimization: SGD, learning rate 0.01, momentum 0.9, batch size 8.
- Baselines: FCN, Deeplab-v3, [[U-Net]], and U2-Net.
- Artifacts: dataset is public on Kaggle; code is not reported.

## Limitations

- SolarCells-S remains small even after augmentation, and the paper notes that small training datasets can degrade localization performance.
- The model needs validation in more scenarios and optimization for actual production requirements.
- Deployment on production hardware/software systems is left for future work.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect segmentation]]
- Methods: [[LMFF]], [[Depthwise separable convolution]], [[Segmentation Models]], [[Computer Vision Models]]
- Datasets: [[Dataset of Solar Cells Defect Segmentation]], [[PVEL-AD]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[IoU]], [[mIoU]], [[F1-score]], [[Foreground pixel accuracy]], [[Background pixel accuracy]], [[Mean pixel accuracy]], [[Inference time]], [[FPS]], [[GFLOPs]], [[Parameter count]]

### Shares Dataset

- [[Dataset of Solar Cells Defect Segmentation]]: the paper introduces SolarCells, SolarCells-S, and PVEL-S and links the Kaggle release.
- [[PVEL-AD]]: PVEL-S is selected from PVEL-AD and given pixel-level labels.

### Shares Task

- [[Solar cell defect detection]]: defect localization on photovoltaic cell EL imagery.
- [[Defect segmentation]]: the method predicts pixel-level defect regions.

### Shares Method

- [[LMFF]]: introduced as the paper's lightweight segmentation architecture.
- [[Depthwise separable convolution]]: used inside depthwise separable residual blocks to lower computation and parameters.
- [[U-Net]]: used as a segmentation baseline and prior related architecture.

### Shares Metric

- [[IoU]], [[mIoU]], [[F1-score]], [[Foreground pixel accuracy]], [[Background pixel accuracy]], and [[Mean pixel accuracy]] measure segmentation quality.
- [[Inference time]], [[FPS]], [[GFLOPs]], and [[Parameter count]] measure deployment efficiency and model size.

### Application/Domain

- [[Solar cells and photovoltaic]]: EL inspection of monocrystalline and polycrystalline solar cells.

### Follow-up Reading

- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] introduces the larger source dataset for PVEL-S.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] is related solar-cell segmentation and augmentation work.

## Questions

- Are the SolarCells and SolarCells-S image files fully redistributable beyond Kaggle access?
- What exact code implementation, data preprocessing, and random seeds were used?
- How does LMFF perform on production-line deployment hardware and mixed cell batches beyond the reported datasets?
