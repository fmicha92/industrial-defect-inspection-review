---
title: "Dice score"
tags:
  - metric
concept_type: metric
---
# Dice score

## Definition

Dice score is a segmentation-overlap metric. [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] defines it as `2 * |X intersect Y| / (|X| + |Y|)`, where `X` is the predicted pixel set and `Y` is the ground-truth pixel set.

## Used In These Papers

- [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] reports Dice score for steel defect segmentation.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] uses Dice/F1pix as the preferred pixel-level metric for imbalanced fabric defect masks.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reports Dice coefficient examples for pixel-level AOI segmentation and recommends Dice/MeanIoU over accuracy-only comparisons.

## Related Concepts

- [[Segmentation metrics]]
- [[ZJU-Leaper benchmark]]
