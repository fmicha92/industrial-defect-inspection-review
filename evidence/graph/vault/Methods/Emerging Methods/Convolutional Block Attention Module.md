---
title: "Convolutional Block Attention Module"
aliases:
  - "CBAM"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]]"
  - "[[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]]"
evidence_count: 2
tags:
  - method
  - emerging
---

# Convolutional Block Attention Module

## Definition

Convolutional Block Attention Module is an attention module with channel and spatial attention branches. In Ding and Yang's YOLOv5_zc detector, it is embedded into the YOLOv5 backbone to refine feature maps for tiny mobile phone flat-glass defects.

## Why It Matters

CBAM helps vision models focus on meaningful channel and spatial information. In the glass-defect paper it improves small-target detection relative to the original YOLOv5 model; in the wafer-map paper it is added before pooling and classification to strengthen wafer defect-pattern representation.

## Used In These Papers

- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] uses CBAM as part of [[YOLOv5_zc]] for mobile phone flat-glass defect detection.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] uses CBAM inside [[WM-PeleeNet]] before final global average pooling and classification.

## Related Concepts

- [[YOLOv5_zc]]
- [[YOLOv5]]
- [[Object detection]]
- [[Smartphone screen glass defect detection]]
- [[WM-PeleeNet]]
- [[Wafer map defect classification]]
