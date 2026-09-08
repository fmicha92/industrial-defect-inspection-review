---
title: "YOLOv5_zc"
aliases:
  - "YOLOv5-zc"
  - "Improved YOLOv5 with CBAM and data augmentation"
tags:
  - method
  - model
  - object-detection
model_family:
  - "[[YOLOv5]]"
related_methods:
  - "[[YOLOv5]]"
  - "[[Convolutional Block Attention Module]]"
  - "[[Poisson defect image augmentation]]"
source_papers:
  - "[[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]]"
---

# YOLOv5_zc

## Definition

YOLOv5_zc is the improved YOLOv5 detector evaluated for mobile phone flat-glass defect detection by Ding and Yang. It combines YOLOv5 with a Convolutional Block Attention Module, an added small-target detection layer, and generated training samples from segmented defect fusion.

## Why It Matters

The paper targets tiny glass defects such as dust and bright spots, where the original YOLOv5 can miss small targets or localize them poorly. YOLOv5_zc improves validation-set MAP, precision, recall, and missed-detection behavior relative to the original YOLOv5 in the reported ablation.

## Used In These Papers

- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] reports 98.36% MAP, 98.68% precision, 98.72% recall, and 65 FPS for YOLOv5_zc on the validation set, with 98.75% average correct detection on the testing set.

## Related Concepts

- [[YOLOv5]]
- [[Object detection]]
- [[Smartphone screen glass defect detection]]
- [[mAP]]
- [[Average precision]]
