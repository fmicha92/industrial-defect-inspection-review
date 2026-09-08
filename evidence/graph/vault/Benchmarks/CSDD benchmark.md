---
title: "CSDD benchmark"
aliases:
  - "CSDD detection benchmark"
  - "CSDD segmentation benchmark"
tags:
  - benchmark
  - dataset
  - metal-inspection
---

# CSDD Benchmark

## Definition

CSDD benchmark is the evaluation setup introduced with [[CSDD]] for casting surface defect detection and segmentation. The paper reports a 64/16/20 split, detection metrics based on AP and mAP, segmentation metrics based on IoU and mIoU, and GFLOPs for method complexity.

## Why It Matters

The benchmark gives a common testbed for [[Casting surface defect detection]] under high-resolution, complex-structure metal surface imagery with small and shape-varied defects.

## Used In These Papers

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] introduces the benchmark and reports detection and segmentation baselines.

## Benchmark Protocol

- Dataset: [[CSDD]].
- Tasks: [[Casting surface defect detection]], [[Defect segmentation]].
- Split: 1343 train, 335 validation, 422 test.
- Detection metrics: [[Average precision]], [[mAP]].
- Segmentation metrics: [[IoU]], [[mIoU]].
- Complexity metric: [[GFLOPs]].
- Best reported detection method in the paper: [[YOLOv5 with global attention and partial convolution]] at 71.1% mAP.
- Best reported segmentation method in the paper: [[U-Net]] at 54.29% mIoU.

## Related Concepts

- [[CSDD]]
- [[Metal inspection]]
- [[Surface defect detection]]
- [[GC10-DET]]
- [[NEU-DET]]
