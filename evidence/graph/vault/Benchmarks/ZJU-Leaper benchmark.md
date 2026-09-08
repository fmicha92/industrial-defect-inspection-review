---
title: "ZJU-Leaper benchmark"
aliases:
  - "ZJU-Leaper evaluation protocol"
  - "ZJU-Leaper fabric defect benchmark"
tags:
  - benchmark
  - dataset
  - textile-inspection
---

# ZJU-Leaper Benchmark

## Definition

ZJU-Leaper benchmark is the evaluation setup introduced with [[ZJU-Leaper]] for [[Textile defect detection]]. It defines five progressive task settings and evaluates inspection algorithms with pixel-level, region-level, and sample-level F1-style metrics.

## Why It Matters

The benchmark separates deployment regimes by annotation cost: normal-only training, a small amount of masked defect data, many labeled defect images, many bounding-box annotations, and many mask annotations. This makes it possible to compare methods under realistic fabric-inspection constraints instead of assuming abundant defective samples and dense labels.

## Used In These Papers

- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] introduces the benchmark, the evaluation protocol, and baseline experiments.

## Benchmark Protocol

- Dataset: [[ZJU-Leaper]].
- Tasks: [[Textile defect detection]], [[Defect segmentation]].
- Setting 1: normal samples only.
- Setting 2: small amount of defect data with mask annotation.
- Setting 3: large amount of defect data with image-label annotation.
- Setting 4: large amount of defect data with bounding-box annotation.
- Setting 5: large amount of defect data with mask annotation.
- Pixel-level metric: [[Dice score]].
- Region-level metrics: region precision, region recall, and region F1-score using IoU and area-ratio matching criteria.
- Sample-level metric: sample F1-score over defective versus normal image decisions.
- Baselines include sparse coding, convolutional auto-encoder, one-class SVM, transfer learning with U-Net, data augmentation with U-Net, weakly supervised U-Net variants, and fully supervised U-Net.

## Related Concepts

- [[ZJU-Leaper]]
- [[Textile defect detection]]
- [[Defect segmentation]]
- [[Textile and fiber inspection]]
- [[U-Net]]
- [[Data augmentation]]
- [[Transfer learning]]
- [[Weakly supervised learning]]
- [[IoU]]
- [[Dice score]]
