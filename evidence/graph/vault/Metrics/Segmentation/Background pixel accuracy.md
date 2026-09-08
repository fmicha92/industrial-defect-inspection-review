---
title: "Background pixel accuracy"
aliases:
  - "BPA"
tags:
  - metric
  - segmentation
concept_type: metric
---
# Background Pixel Accuracy

## Definition

Background pixel accuracy measures the share of true non-defect pixels correctly predicted as background. In the linked solar-cell segmentation paper, it is defined as `TN / (TN + FP)`.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports BPA for SolarCells, SolarCells-S, and PVEL-S defect segmentation.

## Related Metrics

- [[IoU]]
- [[mIoU]]
- [[F1-score]]
- [[Foreground pixel accuracy]]
- [[Mean pixel accuracy]]
- [[Segmentation metrics]]
