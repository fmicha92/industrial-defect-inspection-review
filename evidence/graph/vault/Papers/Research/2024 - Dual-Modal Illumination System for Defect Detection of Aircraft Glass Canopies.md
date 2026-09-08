---
title: "Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies"
aliases:
  - "Dual-Modal Illumination System"
paper_key: "sha256:d679f1fb776c738a80641d578aa97bf43a6e89fa6d9aa1d256ab8be12720091f"
paper_type: research
year: 2024
venue: "Sensors"
authors:
  - "Zijian Li"
  - "Yong Yao"
  - "Runyuan Wen"
  - "Qiyang Liu"
status: processed
processed_at: 2026-06-03
topics:
  - "aircraft glass canopy defect detection"
  - "dual-modal illumination"
  - "image fusion"
  - "oriented bounding boxes"
tasks:
  - "[[Aircraft glass canopy defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[AGDD]]"
methods:
  - "[[Dual-modal illumination for transparent material inspection]]"
  - "[[ADMF-Net]]"
  - "[[RGB Channel Fusion]]"
  - "[[YOLOv8]]"
model_family:
  - "[[YOLOv8]]"
architectures:
  - "[[ADMF-Net]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[mAP]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP50: mean average precision at IoU 0.5."
  - "mAP50-95: mean average precision averaged across IoU thresholds from 0.5 to 0.95 in 0.05 steps."
baselines:
  - "YOLOv8m forward-only"
  - "YOLOv8m backward-only"
  - "RGB Channel Fusion"
benchmarks:
  - "[[AGDD]]"
code: "https://github.com/core128/AGDD"
data: "https://github.com/core128/AGDD"
doi: "10.3390/s24206717"
url: "https://doi.org/10.3390/s24206717"
pdf: "paper-inbox/10_processed/Research/2024 - Li - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Oriented bounding boxes]]"
related_methods:
  - "[[Dual-modal illumination for transparent material inspection]]"
  - "[[ADMF-Net]]"
  - "[[RGB Channel Fusion]]"
related_datasets:
  - "[[AGDD]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Aircraft glass canopy defect detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Li - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Li - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies.txt"
---

# Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies

## Summary

Li, Yao, Wen, and Liu propose a dual-modal illumination inspection system for aircraft glass canopy defects. The system captures paired forward-lighting and backward-lighting images, introduces the public AGDD dataset, and evaluates data-level and feature-level fusion methods for oriented defect detection.

## Paper Type

Research paper with dataset and systems components. It introduces an acquisition platform, dataset, and detection model.

## Problem

Aircraft glass canopies, windshields, and windows require strong mechanical and optical quality. Defects such as cracks, scratches, pits, contusions, and spots can interfere with pilot visibility and create safety risks. A single lighting condition can miss or confuse transparent-material defects because defect visibility depends on lighting direction.

## Contribution

- Builds a prototype dual-modal illumination acquisition platform using forward and backward lighting.
- Introduces [[AGDD]], a public aircraft glass canopy defect dataset with paired illumination images and OBB annotations.
- Proposes [[RGB Channel Fusion]] as a data-level fusion baseline and [[ADMF-Net]] as a feature-level dual-branch fusion detector.

## Method

The acquisition platform uses a digital microscope, flexible arm holder, backlight panel, and ring light source. The microscope uses a 20 mm focal length during acquisition with approximately 400x magnification. Forward lighting uses eight ring-shaped LED lights around the camera lens, while backward lighting uses a 30 cm x 42 cm backlight panel with 500 nit brightness and 6500 K color temperature.

ADMF-Net uses two CSPDarknet-like backbones, one for forward-lighting images and one for backward-lighting images. Attention-based multimodal feature fusion modules are inserted at P3 and P4, while the P5 features are concatenated into a fusion-based SPPF module. Detection layers use an OBB head to predict rotated boxes.

## Evidence

Dataset construction:

- Raw collection: 438 images from 219 defect points, captured under two lighting methods.
- Final dataset: ag_dual_obb, with 1752 defect points and 4784 defect objects.
- Split: 1576 training image pairs and 176 test image pairs, a 9:1 split.
- Defect classes: contusion, scratches, crack, and spot.
- Annotation: oriented bounding boxes, assisted by Segment Anything pre-labeling and manual adjustment.
- Public repository: https://github.com/core128/AGDD.

Main results:

| Dataset / method | Model | mAP50 | mAP50-95 |
|---|---|---:|---:|
| forward_only | YOLOv8m | 0.928 | 0.641 |
| backward_only | YOLOv8m | 0.790 | 0.538 |
| ag_composite_obb | RGB Channel Fusion | 0.979 | 0.691 |
| ag_dual_obb | ADMF-Net | 0.984 | 0.669 |

Per-class ADMF-Net AP50/AP50-95 values are 0.995/0.686 for contusion, 0.954/0.520 for scratches, 0.995/0.714 for crack, and 0.993/0.756 for spot. Removing the attention mechanism leaves mAP50 almost stable at 0.983 but reduces mAP50-95 to 0.639.

## ML/DL Extraction

- Task formulation: four-class oriented object detection on transparent aircraft glass canopy defects.
- Inputs: spatially aligned forward-lighting and backward-lighting image pairs.
- Architecture: ADMF-Net with two YOLOv8-style CSPDarknet-like backbones, AMFF modules, FSPPF, and OBB detection heads.
- Training environment: Python 3.10.14, PyTorch 2.2.2, CUDA 11.8, Ultralytics 8.2.2.
- Hardware: AMD Ryzen 7 7800X3D, 48 GB memory, NVIDIA GeForce RTX 4080 16 GB VRAM.
- Training setup: 300 epochs, batch size 16, 640 x 640 image size, Mosaic-4 augmentation, SGD, learning rate 0.01, momentum 0.937, weight decay 0.0005.
- Metrics: precision, recall, AP, mAP50, and mAP50-95.

## Limitations

- The paper states that exploring specific multi-modal detection networks remains worthwhile.
- The dataset is specific to aircraft glass canopy samples and four reported defect categories.
- The extracted text does not report inference speed or model size.

## Connections

### Graph Hubs

- Tasks: [[Aircraft glass canopy defect detection]], [[Object detection]]
- Methods: [[Dual-modal illumination for transparent material inspection]], [[ADMF-Net]], [[RGB Channel Fusion]], [[YOLOv8]]
- Datasets: [[AGDD]]
- Domains: [[Glass inspection]]
- Metrics: [[mAP@0.50]], [[mAP]], [[Precision]], [[Recall]]

### Relationship Rationale

- Shares task: [[Aircraft glass canopy defect detection]] because the paper introduces the acquisition system, dataset, and detector for that task.
- Shares dataset: [[AGDD]] is introduced by the paper.
- Shares method: [[Dual-modal illumination for transparent material inspection]] is the inspection setup used to acquire paired images.
- Shares method: [[ADMF-Net]] is the proposed feature-level fusion detector.
- Shares method: [[RGB Channel Fusion]] is the proposed data-level fusion baseline.
- Application/domain: [[Glass inspection]] because aircraft canopies are transparent glass components.

## Questions

- How well does the dual-modal approach transfer to windshields, architectural glass, or other transparent materials with different defect morphologies?
- What inference speed and model-size tradeoffs does ADMF-Net impose compared with single-branch YOLOv8m?
