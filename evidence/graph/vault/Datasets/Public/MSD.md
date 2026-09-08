---
title: "MSD"
aliases:
  - "Mobile Phone Screen Surface Defect Dataset"
  - "MSD smartphone screen defect dataset"
  - "Mobile phone screen Surface Defect dataset"
related_domain: "[[Glass inspection]]"
url: "https://github.com/jianzhang96/MSD"
data_sources:
  - "GitHub MSD repository"
  - "GitHub FDSNet repository"
introduced_by: "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
---
# MSD

## Definition

MSD is a public mobile phone screen surface-defect dataset introduced for pixel-level segmentation of oil, stain, and scratch defects. It is also used in later object-detection experiments on smartphone cover-glass defects.

## Why It Matters

The dataset supports [[Smartphone screen glass defect detection]] under reflective cover-glass conditions where low-contrast defects and background interference can cause false detections.

## Used In These Papers

- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] evaluates [[DY-YOLO]] on MSD and reports 99.3% mAP@0.5 and 70.9% mAP@0.5:0.95.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] introduces MSD and evaluates [[FDSNet]] for real-time defect segmentation, reporting 90.2% [[mIoU]] at 135.0 [[FPS]] on 1440 x 810 images.

## Dataset Details

- Domain: [[Glass inspection]].
- Task: [[Smartphone screen glass defect detection]].
- Images: 1200.
- Defect classes from the introducing paper: oil, stain, and scratch.
- Defect classes from the DY-YOLO paper: oil stains, scratches, and spots.
- Images per class: 400.
- Resolution: 1920 x 1080.
- Capture: artificially generated defects on glass cover plates captured with an industrial camera.
- Annotation: pixel-level LabelMe annotations.
- Split used by FDSNet: random train/validation/test = 6:2:2; images downsampled to 1440 x 810 during training and testing.
- Split used by DY-YOLO: training/validation = 8:2 after reallocating the original test set to validation.
- Dataset repository license: GPL-3.0.

## Source Anchors

- Dataset source: https://github.com/jianzhang96/MSD.
- Introducing-paper code/source repository: https://github.com/jianzhang96/fdsnet.
- Introducing paper: [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]].
- Later processed-paper source: [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]].

## Related Concepts

- [[Smartphone screen glass defect detection]]
- [[Glass inspection]]
- [[Surface defect detection]]
- [[Object detection]]
- [[Defect segmentation]]
- [[FDSNet]]
