---
title: "FB-IoU"
aliases:
  - "Foreground-background IoU"
  - "Foreground-background Intersection over Union"
tags:
  - metric
  - segmentation
direction: "higher is better"
unit: "IoU score"
source_papers:
  - "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
---

# FB-IoU

## Definition

FB-IoU averages foreground IoU and background IoU for binary segmentation. In [[2023 - Few-shot semantic segmentation for industrial defect recognition]], it ignores the object class and evaluates foreground/background segmentation quality.

## Direction

Higher is better.

## Used In These Papers

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] reports FB-IoU for 1-shot and 5-shot Industrial-5i defect segmentation and ablation experiments.

## Related Metrics

- [[IoU]]
- [[mIoU]]
- [[Segmentation metrics]]
