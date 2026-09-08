---
title: "FDSNet: An Accurate Real-Time Surface Defect Segmentation Network"
aliases:
  - "FDSNet"
paper_key: "doi:10.1109/icassp43922.2022.9747311"
doi: "10.1109/ICASSP43922.2022.9747311"
url: "https://doi.org/10.1109/ICASSP43922.2022.9747311"
pdf: "paper-inbox/10_processed/Research/2022 - Zhang - FDSNet An Accurate Real-Time Surface Defect Segmentation Network.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Zhang - FDSNet An Accurate Real-Time Surface Defect Segmentation Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Zhang - FDSNet An Accurate Real-Time Surface Defect Segmentation Network.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Zhang - FDSNet An Accurate Real-Time Surface Defect Segmentation Network.txt"
authors:
  - "Jian Zhang"
  - "Runwei Ding"
  - "Miaoju Ban"
  - "Tianyu Guo"
year: 2022
venue: "ICASSP 2022"
paper_type: research
status: processed
processed_at: 2026-06-04
topics:
  - surface defect segmentation
  - real-time semantic segmentation
tasks:
  - "[[Defect segmentation]]"
  - "[[Smartphone screen glass defect detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[MSD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[NEU-SEG]]"
methods:
  - "[[FDSNet]]"
  - "[[Global Context Upsampling]]"
  - "[[MobileNet]]"
architectures:
  - "[[FDSNet]]"
model_family:
  - "[[Segmentation Models]]"
metrics:
  - "[[mIoU]]"
  - "[[FPS]]"
primary_metric: "[[mIoU]]"
baselines:
  - "FCN-8s"
  - "PSPNet"
  - "DeepLabV3+"
  - "EMANet"
  - "U2-Net"
  - "DFANet A"
  - "ICNet"
  - "LEDNet"
  - "ENet"
  - "ESPNetV2"
  - "STDC-Seg"
  - "BiSeNet"
  - "Fast-SCNN"
code: "https://github.com/jianzhang96/fdsnet"
data: "https://github.com/jianzhang96/fdsnet"
related_papers:
  - "[[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
related_methods:
  - "[[FDSNet]]"
  - "[[Global Context Upsampling]]"
  - "[[MobileNet]]"
related_datasets:
  - "[[MSD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[NEU-SEG]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Smartphone screen glass defect detection]]"
---
# FDSNet: An Accurate Real-Time Surface Defect Segmentation Network

## Summary

Zhang et al. propose [[FDSNet]], a real-time surface-defect segmentation network built from a Fast-SCNN-style encoder-decoder architecture with training-only boundary and multi-label classification auxiliary tasks. The paper also introduces [[MSD]], a mobile-phone screen surface-defect segmentation dataset with 1,200 pixel-labeled images across oil, stain, and scratch defects.

The strongest reported result is on MSD: FDSNet reaches 90.2% [[mIoU]] at 135.0 [[FPS]] on 1440 x 810 images using one NVIDIA GTX 1080Ti GPU, and 88.7% mIoU at 275.9 FPS with TensorRT acceleration.

## Paper Type

Research paper. It proposes a segmentation model and introduces a dataset used to evaluate the model.

## Problem

Surface defect detection for industrial quality control needs accurate localization and real-time inference. The paper argues that existing detection-style methods do not meet fine-grained localization needs, while directly applying scene-parsing segmentation networks struggles with low contrast, local similarity between defect classes, boundary detail, dust, and lighting changes.

## Contribution

- Introduces [[FDSNet]], a lightweight real-time segmentation network for surface defects.
- Adds boundary detection and multi-label classification auxiliary tasks during training to improve boundary detail and semantic guidance without inference-time cost.
- Proposes [[Global Context Upsampling]] to fuse multi-scale features and capture long-range context.
- Introduces [[MSD]], a mobile phone screen surface-defect segmentation dataset with pixel-level labels.

## Method

FDSNet is based on Fast-SCNN and uses an encoder-decoder segmentation architecture. It replaces part of the high-level feature extractor with six MobileNetV3 blocks and uses channel attention from MobileNetV3 to improve contrast between defects and background.

The detail branch is supervised by a boundary detection auxiliary task. Boundary labels are generated from segmentation masks with a Laplacian operator followed by morphological dilation. The semantic branch is supervised by a multi-label classification auxiliary task derived from the unique class labels in each segmentation mask. These auxiliary heads are used only during training.

[[Global Context Upsampling]] uses skip-connected 1/8 and 1/16 encoder features, bilinear upsampling, group convolution, and global-context blocks to capture long-range dependency and recover more complete defect masks.

## Evidence

### Datasets

- [[MSD]]: 1,200 mobile phone screen images; three defect classes: oil, stain, and scratch; pixel-level LabelMe annotations; 1920 x 1080 source resolution; downsampled to 1440 x 810 during training and testing.
- [[Magnetic Tile Defects]]: 392 defect images and 952 non-defect images; five defect classes: uneven, fray, crack, blowhole, and break; image resolution ranges from 105 x 283 to 388 x 516.
- [[NEU-SEG]]: hot-rolled steel strip surface-defect segmentation dataset introduced by [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]; three surface-defect classes: inclusion, patches, and scratches; 200 x 200 images; 300 images per class in the source NEU defect database.

### Evaluation Setup

- Train/validation/test split: 6:2:2 randomly for all three datasets.
- Optimizer: Adam.
- Learning-rate policy: poly schedule.
- Initial learning rate: 1e-4.
- Weight decay: 1e-5.
- Augmentation: scale 0.5 to 2.0, 450 x 450 crop, and flipping.
- Batch size: 8 for MSD and 16 for the other datasets.
- Epochs: 150.
- Hardware/software: NVIDIA GTX 1080Ti, CUDA 11.1, PyTorch 1.9.

### Results

| Dataset | Metric | FDSNet result | Speed | Context |
|---|---:|---:|---:|---|
| [[MSD]] | [[mIoU]] | 90.2% | 135.0 [[FPS]] | Best accuracy and speed in Table 1. |
| [[MSD]] with TensorRT | [[mIoU]] | 88.7% | 275.9 [[FPS]] | TensorRT acceleration reported in text. |
| [[Magnetic Tile Defects]] | [[mIoU]] | 63.9% | 181.5 [[FPS]] | Average image resolution 320 x 320. |
| [[NEU-SEG]] | [[mIoU]] | 78.8% | 186.1 [[FPS]] | Input size 200 x 200. |

### Ablation Results On MSD

| Variant | mIoU |
|---|---:|
| Baseline | 89.08 |
| GCU only | 89.95 |
| Multi-label classification only | 89.57 |
| Boundary detection only | 89.49 |
| GCU + boundary detection | 89.96 |
| GCU + multi-label classification | 90.15 |
| GCU + multi-label classification + boundary detection + V3 blocks | 90.20 |

### MSD Per-Class Results

| Class | Fast-SCNN | FDSNet |
|---|---:|---:|
| oil | 95.12 | 95.50 |
| stain | 81.90 | 84.63 |
| scratch | 79.39 | 80.75 |
| mIoU | 89.08 | 90.20 |

## ML/DL Extraction

- Task formulation: multi-class pixel-level semantic segmentation of surface defects.
- Inputs: industrial surface images; MSD images are collected at 1920 x 1080 and downsampled to 1440 x 810 for training and testing.
- Outputs: semantic segmentation masks; auxiliary boundary and multi-label predictions during training.
- Architecture: Fast-SCNN-style encoder-decoder with MobileNetV3 blocks, channel attention, [[Global Context Upsampling]], and training-only auxiliary heads.
- Losses: segmentation loss plus binary cross-entropy for boundary detection and multi-label classification; auxiliary weights w1 = w2 = 0.5.
- Data pipeline: random scale, crop, and flip augmentation.
- Evaluation protocol: random 6:2:2 train/validation/test split across MSD, Magnetic Tile Defects, and NEU-SEG.
- Metrics: [[mIoU]], [[FPS]], parameter count.
- Compute: one NVIDIA GTX 1080Ti GPU; TensorRT also used for an accelerated MSD result.
- Artifacts: dataset and code are reported available at https://github.com/jianzhang96/fdsnet.

## Limitations

- The MSD defects are made by the authors; the paper does not report whether the defect-generation process matches natural production defect distributions.
- The paper reports random splits but does not report repeated-run variance or statistical significance.
- The available text does not report a license for the dataset or code.
- The auxiliary supervision uses labels derived from segmentation masks, so the approach still depends on pixel-level annotations.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Smartphone screen glass defect detection]]
- Methods: [[FDSNet]], [[Global Context Upsampling]], [[MobileNet]]
- Datasets: [[MSD]], [[Magnetic Tile Defects]], [[NEU-SEG]]
- Domains: [[Glass inspection]], [[Metal inspection]]
- Metrics: [[mIoU]], [[FPS]]

### Shares Dataset

- [[MSD]]: introduced by this paper for pixel-level mobile phone screen surface-defect segmentation and later used for object-detection experiments.
- [[Magnetic Tile Defects]]: used as a surface-defect segmentation benchmark.
- [[NEU-SEG]]: used as a steel-strip surface-defect segmentation benchmark introduced by the PGA-Net paper.

### Shares Task

- [[Defect segmentation]]: FDSNet predicts pixel-level defect masks.
- [[Smartphone screen glass defect detection]]: MSD is a smartphone screen surface-defect dataset.

### Shares Method

- [[FDSNet]]: central model proposed by the paper.
- [[Global Context Upsampling]]: central upsampling and context module proposed by the paper.
- [[MobileNet]]: MobileNetV3 blocks are used to reduce high-level feature extraction cost and add channel attention.

### Shares Metric

- [[mIoU]]: primary segmentation metric.
- [[FPS]]: throughput metric for real-time inspection.

### Application/Domain

- [[Glass inspection]]: MSD covers mobile-phone screen surface defects.

### Follow-up Reading

- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]]: later evaluates object detection on [[MSD]] and [[SSGD]], providing a different task framing for the same dataset name.

## Questions

- What license and download structure are provided in the GitHub repository?
- Are the author-made MSD defects representative of production defects on mobile phone screens?
- How stable are the random split results across multiple seeds?
