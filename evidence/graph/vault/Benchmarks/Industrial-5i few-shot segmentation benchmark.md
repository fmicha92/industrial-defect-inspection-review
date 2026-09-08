---
title: "Industrial-5i few-shot segmentation benchmark"
aliases:
  - "Industrial-5i benchmark"
tags:
  - benchmark
dataset: "[[Industrial-5i]]"
tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
metrics:
  - "[[mIoU]]"
  - "[[FB-IoU]]"
introduced_by: "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
related_domain: "[[Multi-industry anomaly detection]]"
---

# Industrial-5i few-shot segmentation benchmark

## Definition

The Industrial-5i few-shot segmentation benchmark evaluates binary defect-mask prediction on held-out industrial product categories from [[Industrial-5i]]. Episodes use K normal support images and one abnormal query image.

## Protocol

- Dataset: [[Industrial-5i]].
- Products: 20 product categories arranged in four folds of five products each.
- Cross-validation: one fold is held out for testing while the other product categories are used for training.
- Test sampling: [[2023 - Few-shot semantic segmentation for industrial defect recognition]] reports 1000 randomly sampled episodes for each test fold.
- Metrics: [[mIoU]] and [[FB-IoU]].

## Reported Results

| Method | 1-shot mean mIoU | 1-shot FB-IoU | 5-shot mean mIoU | 5-shot FB-IoU |
|---|---:|---:|---:|---:|
| FSS-1000 | 9.81 | 51.52 | 11.51 | 52.06 |
| MMNet | 21.73 | 56.51 | 24.84 | 57.75 |
| MSNet | 24.16 | 57.16 | 24.13 | 57.46 |
| HSNet | 27.44 | 59.58 | 28.40 | 59.85 |
| [[IndustrialNet]] | 36.36 | 67.26 | 38.24 | 68.31 |

## Used In These Papers

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] introduces the benchmark and reports baseline, support-shot, and distance-ablation results.

## Related Concepts

- [[Industrial-5i]]
- [[IndustrialNet]]
- [[Few-shot anomaly detection]]
- [[Defect segmentation]]
- [[Multi-industry anomaly detection]]
