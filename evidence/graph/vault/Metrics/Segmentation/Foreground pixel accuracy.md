---
title: "Foreground pixel accuracy"
aliases:
  - "FPA"
tags:
  - metric
  - segmentation
concept_type: metric
---
# Foreground Pixel Accuracy

## Definition

Foreground pixel accuracy measures the share of true defect pixels correctly predicted as foreground. In the linked solar-cell segmentation paper, it is defined as `TP / (TP + FN)`.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports FPA for SolarCells, SolarCells-S, and PVEL-S defect segmentation.

## Related Metrics

- [[IoU]]
- [[mIoU]]
- [[F1-score]]
- [[Background pixel accuracy]]
- [[Mean pixel accuracy]]
- [[Segmentation metrics]]
