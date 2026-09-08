---
title: "Defect Detection Network"
aliases:
  - "DDN"
  - "defect detection network"
tags:
  - method
  - model
  - object-detection
---

# Defect Detection Network

## Definition

Defect Detection Network is an end-to-end steel surface defect detector introduced with [[NEU-DET]]. It combines a ResNet backbone, [[Multilevel feature fusion network]], an RPN proposal stage, ROI pooling, and classification/localization heads.

## Why It Matters

DDN demonstrates how region-proposal object detection can be adapted to metal surface inspection when defect localization, multiple defects, and overlapping defects matter more than image-level classification alone.

## Used In These Papers

- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] introduces DDN and reports 82.3 mAP on [[NEU-DET]] with a ResNet50 backbone.

## Related Concepts

- [[Multilevel feature fusion network]]
- [[Faster R-CNN]]
- [[ResNet50]]
- [[Object detection]]
- [[Metallic surface defect detection]]
- [[NEU-DET]]
- [[mAP]]
