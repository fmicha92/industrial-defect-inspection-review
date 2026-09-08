---
title: "NEU-DET"
aliases:
  - "Northeastern University surface defect dataset"
related_domain: "[[Metal inspection]]"
url: "https://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm"
data_sources:
  - "Northeastern University surface defect database"
introduced_by: "[[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]"
related_papers:
  - "[[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]"
  - "[[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]"
  - "[[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]]"
---
# NEU-DET

## Definition

NEU-DET is a hot-rolled steel strip surface defect detection dataset introduced by [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]. It upgrades [[NEU-CLS]] with XML bounding-box annotations for six defect classes: crazing, inclusion, patches, pitted surface, rolled-in scale, and scratches.

## Why It Matters

It provides the bounding-box annotations needed to train and evaluate steel surface defect detectors, including [[Defect Detection Network]], EDDN, MSFT-YOLO, and other object-detection models.

## Used In These Papers

- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] introduces NEU-DET by adding XML bounding-box annotations to the earlier NEU surface defect classification dataset.
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] compares EDDN and detector baselines on NEU-DET and GC10-DET.
- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] evaluates automatic data augmentation on NEU-DET and reports ALADA mAP of 78.48 with FRCNN and 76.34 with RetinaNet.
- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] evaluates MSFT-YOLO on NEU-DET's six hot-rolled steel strip defect classes.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates IDD-Net on NEU steel surface defects after reported graphic fixes and a 6:2:2 train/validation/test split, reporting 79.66% [[mAP@0.50]] and 43.6% [[mAP@0.50-0.95]].
- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]] evaluates SA-DSSD on NEU-DET and reports 74.88 [[mAP]].
- [[2024 - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation]] uses DDIM augmentation and [[YOLO-DSC]] on NEU-DET, improving mAP@0.5 from 0.748 to 0.809.
- [[2024 - NHD-YOLO Improved YOLOv8 Using Optimized Neck and Head]] uses NEU-DET for surface defect object detection and reports NHD-YOLOs AP improvement from 38.5 to 39.6 over YOLOv8s.
- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] uses three NEU-DET labels, expands them with random cropping, flipping, rotation, and SA-GAN, and reports YOLOv11 with SA-GAN at 85.1% mAP@0.5.

## Source Anchors

- Hosting source: https://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm.
- Mirror/source pointer: the NEU faculty page was identified through indexed paper and search evidence; the page did not return successfully during the 2026-06-05 audit.
- Introducing paper: [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]].
- Dataset details from introducing paper: 1,800 grayscale images, 300 per class, six hot-rolled steel strip defect classes, and nearly 5,000 XML bounding-box annotations.
- Usage paper: [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] compares detector baselines on NEU-DET and GC10-DET.
- Popular usage paper: [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] evaluates MSFT-YOLO on NEU-DET.

## Related Concepts

- [[Metallic surface defect detection]]
- [[Metal inspection]]
- [[GC10-DET]]
- [[NEU-DET benchmark]]
- [[Defect Detection Network]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.
