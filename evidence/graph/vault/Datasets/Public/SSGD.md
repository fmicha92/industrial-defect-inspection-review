---
title: "SSGD"
aliases:
  - "Smartphone Screen Glass Dataset"
  - "Smartphone screen glass defect dataset"
related_domain: "[[Glass inspection]]"
url: "https://github.com/VincentHancoder/SSGD"
data_sources:
  - "GitHub"
  - "Baidu"
  - "Tsinghua Cloud"
licenses:
  - "Apache-2.0 repository license"
  - "academic purposes only dataset usage"
introduced_by: "[[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]"
---
# SSGD

## Definition

SSGD, the Smartphone Screen Glass Dataset, is a public object-detection dataset introduced by [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]. It contains high-resolution smartphone touch-screen glass images with bounding-box annotations for seven defect categories.

## Why It Matters

SSGD supports [[Smartphone screen glass defect detection]] in a manufacturing setting where defects can be small, elongated, or category-imbalanced. The benchmark results show that high-resolution screen-glass inspection remains difficult for both CNN and Transformer object detectors.

## Used In These Papers

- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] introduces SSGD and benchmarks CNN- and Transformer-based object detectors.
- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] evaluates [[DY-YOLO]] on SSGD with an 8:2 train/validation split.
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] evaluates [[CE-SGNet]] on the SSGD LB101 and LB201 subsets with a 4:1 train/test split.

## Dataset Details

- Domain: [[Glass inspection]].
- Task: [[Smartphone screen glass defect detection]].
- Images: 2504.
- Annotated defects: 3914.
- Resolution: 1500 x 1000 pixels.
- Annotation type: bounding boxes in XML files.
- Annotation tool: LabelMe.
- Defect categories: crack, broken, spot, scratch, light-leakage, blot, and broken-membrane.
- Capture setup: industrial line-scan camera on calibrated fixed workstations with black background decoration.
- Parts: Part I has 1258 images; Part II has 1246 images.
- Repository: https://github.com/VincentHancoder/SSGD.
- Download mirrors: Baidu and Tsinghua Cloud links are listed in the repository README.
- Usage: academic purposes only.
- Recommended evaluation: 5-fold cross-validation.
- Repository license: Apache-2.0.

## Source Anchors

- Hosting source: https://github.com/VincentHancoder/SSGD.
- Download source: https://cloud.tsinghua.edu.cn/f/720250d21e1b4887abf7/?dl=1.
- Introducing paper: [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]].

## Related Concepts

- [[SSGD benchmark]]
- [[CE-SGNet]]
- [[Smartphone screen glass defect detection]]
- [[Glass inspection]]
- [[Semiconductor and electronics]]
- [[Industrial visual inspection]]
- [[Average precision]]
- [[mAP@0.50]]
- [[FPS]]
- [[GFLOPs]]
- [[DY-YOLO]]
