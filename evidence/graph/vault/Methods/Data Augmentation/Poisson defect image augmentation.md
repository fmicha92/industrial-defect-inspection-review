---
title: "Poisson defect image augmentation"
aliases:
  - "segmented defect fusion"
  - "Poisson image editing defect augmentation"
tags:
  - method
  - data-augmentation
related_methods:
  - "[[Data augmentation]]"
source_papers:
  - "[[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]]"
  - "[[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]]"
---

# Poisson Defect Image Augmentation

## Definition

Poisson defect image augmentation creates additional defect-detection training samples by extracting defect regions, generating masks, and fusing the defects into clean background images with Poisson image editing.

## Why It Matters

For tiny mobile phone flat-glass defects, random cropping or Mosaic-style augmentation can clip defects or damage labels. The Ding and Yang paper uses segmentation and image fusion to preserve complete defects while automatically outputting class labels and bounding-box position information.

## Used In These Papers

- [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]] uses improved Poisson blending to composite DCDGANc-generated defect contents into normal industrial backgrounds while preserving defect content and producing refined masks.
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] applies Butterworth frequency-domain filtering, one-dimensional maximum entropy segmentation, defect-mask extraction, and Poisson image editing to generate augmented training samples for [[YOLOv5_zc]].
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] uses Poisson image blending to composite generated PV fault masks into real UAV thermal panel backgrounds.

## Related Concepts

- [[Data augmentation]]
- [[Synthetic data generation]]
- [[Smartphone screen glass defect detection]]
- [[Surface defect detection]]
