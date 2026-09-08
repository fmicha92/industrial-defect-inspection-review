---
title: "GFLOPs"
aliases:
  - "giga floating point operations"
tags:
  - metric
  - efficiency
---

# GFLOPs

## Definition

GFLOPs quantifies the number of floating-point operations required for a single forward pass. In the processed CSDD paper, it is used as a model-complexity metric for detection and segmentation methods.

## Direction

Lower is better when comparing model complexity.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] reports 7.9 GFLOPs for [[YOLO-AL]] on [[APDDD]].
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] reports GFLOPs for detection and segmentation baselines on [[CSDD benchmark]].
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] reports GFLOPs for CNN and Transformer object detectors on [[SSGD benchmark]].
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] reports [[CE-SGNet]] at 347.27 GFLOPs.

## Related Metrics

- [[Efficiency metrics]]
- [[Inference time]]
- [[FPS]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports LMFF complexity as 6.51 GFLOPs.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] reports [[WM-PeleeNet]] at 0.316 GFLOPs / 316.194M FLOPs.
