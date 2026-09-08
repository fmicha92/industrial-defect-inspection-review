---
title: "Mean pixel accuracy"
aliases:
  - "MPA"
tags:
  - metric
  - segmentation
concept_type: metric
---
# Mean Pixel Accuracy

## Definition

Mean pixel accuracy averages foreground and background pixel accuracy. In the linked solar-cell segmentation paper, it is defined as `(FPA + BPA) / 2`.

## Direction

Higher is better.

## Used In These Papers

- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] uses mean pixel accuracy alongside [[mIoU]] for surface defect segmentation evaluation; exact table values were not recoverable from the extracted text.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports MPA for SolarCells, SolarCells-S, and PVEL-S defect segmentation.

## Related Metrics

- [[Foreground pixel accuracy]]
- [[Background pixel accuracy]]
- [[IoU]]
- [[mIoU]]
- [[F1-score]]
- [[Segmentation metrics]]
