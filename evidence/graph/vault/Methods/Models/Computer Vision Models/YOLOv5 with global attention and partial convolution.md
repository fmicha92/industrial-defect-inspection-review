---
title: "YOLOv5 with global attention and partial convolution"
aliases:
  - "YOLOv5-GAM-PConv"
  - "CSDD proposed detector"
tags:
  - method
  - model
  - object-detection
---

# YOLOv5 With Global Attention And Partial Convolution

## Definition

YOLOv5 with global attention and partial convolution is the detector proposed in [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]. It adds a global attention mechanism before SPPF and replaces two C3 modules in the YOLOv5 backbone with P3 modules that use partial convolution.

## Why It Matters

The method is designed to improve [[Casting surface defect detection]] on small, complex, and shape-varied casting surface defects while keeping model complexity near the YOLOv5 baseline.

## Used In These Papers

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] reports 71.1% mAP on [[CSDD]], compared with 69.5% for YOLOv5.

## Reported Evidence

- Base YOLOv5: 69.5% mAP and 15.8 GFLOPs.
- Base + GAM: 70.0% mAP and 17.2 GFLOPs.
- Base + PConv: 70.6% mAP and 14.6 GFLOPs.
- Base + GAM + PConv: 71.1% mAP and 16.2 GFLOPs.

## Related Concepts

- [[YOLOv5]]
- [[CSDD benchmark]]
- [[Average precision]]
- [[mAP]]
- [[GFLOPs]]
