---
title: "MixedWM38"
aliases:
  - "MixedWM38 wafer map dataset"
related_domain: "[[Semiconductor and electronics]]"
url: "https://github.com/Junliangwangdhu/WaferMap"
data_sources:
  - "GitHub"
  - "Kaggle"
  - "Google Drive"
  - "Baidu Pan"
introduced_by: "[[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]]"
---

# MixedWM38

## Definition

MixedWM38 is a wafer-map defect pattern dataset with 38 classes for mixed-type defect pattern recognition.

## Why It Matters

It supports multi-label wafer-map defect classification where several basic defect patterns can be present on the same wafer map.

## Dataset Details

- Size: 38,000 wafer maps.
- Classes: one normal type, eight single-defect types, 13 two-defect mixed types, 12 three-defect mixed types, and four four-defect mixed types.
- Samples per class: 1,000.
- Split used by the introducing paper: 80% training and 20% validation per category.
- Source: reported as based on 38 frequently occurring mixed-type defect patterns from a real semiconductor wafer manufacturing system, with simulation used where some mixed-type patterns had insufficient samples.
- Availability: public dataset; the GitHub repository states the dataset is public for researchers, students, and related-field users, and provides GitHub, Kaggle, Google Drive, and Baidu download sources.
- License: not reported.

## Used In These Papers

- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] introduces MixedWM38 and evaluates [[DC-Net]] on it.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] evaluates [[WM-PeleeNet]] on MixedWM38 and reports 97.5% average accuracy.
- [[2025 - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps]] uses MixedWM38 for single, mixed, and overlapped wafer-map defect identification with YOLO-style detection and U-Net segmentation.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] uses MixedWM38 with an artificially imbalanced training trial and reports 97.38% accuracy after [[JRGAN]] balancing.

## Source Anchors

- Hosting source: https://github.com/Junliangwangdhu/WaferMap.
- Additional download sources: [Kaggle](https://www.kaggle.com/co1d7era/mixedtype-wafer-defect-datasets), [Google Drive](https://drive.google.com/file/d/1M59pX-lPqL9APBIbp2AKQRTvngeUK8Va/view?usp=sharing), and [Baidu Pan](https://pan.baidu.com/s/1vOVzqByiE3VlhSZgvnGv7w).
- Introducing paper: [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]].

## Related Concepts

- [[Wafer map defect classification]]
- [[Semiconductor and electronics]]
- [[DC-Net]]
