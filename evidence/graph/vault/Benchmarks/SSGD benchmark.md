---
title: "SSGD benchmark"
aliases:
  - "Smartphone screen glass defect detection benchmark"
related_domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
related_datasets:
  - "[[SSGD]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
tags:
  - benchmark
  - dataset
  - glass-inspection
---

# SSGD Benchmark

## Definition

SSGD benchmark is the object-detection evaluation protocol introduced with [[SSGD]]. It evaluates mainstream CNN- and Transformer-based object detectors on smartphone screen glass defects across two workstation-derived dataset parts.

## Why It Matters

The benchmark exposes high-resolution industrial inspection challenges: small and elongated defects, imbalanced categories, and a speed-accuracy trade-off for production-line use.

## Used In These Papers

- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] introduces the benchmark and reports AP, AP50, AP75, small/medium/large AP, FLOPs, parameters, and FPS.

## Benchmark Protocol

- Dataset: [[SSGD]].
- Task: [[Smartphone screen glass defect detection]].
- Defect categories: crack, broken, spot, scratch, light-leakage, blot, and broken-membrane.
- Dataset parts: Part I and Part II correspond to two capture workstations.
- Evaluation: 5-fold cross-validation; results averaged over the five folds.
- CNN detectors: Faster R-CNN, Cascade R-CNN, RetinaNet, FCOS, ATSS, GFL, YOLOv5-m, and YOLOX-m.
- Transformer detectors: Swin-T, PVT-S, ScalableViT-S, and UniFormer-Sh14 under Faster R-CNN.
- Metrics: [[Average precision]], [[mAP@0.50]], AP75, APS, APM, APL, [[GFLOPs]], and [[FPS]].
- Training: most experiments use MMDetection; YOLOv5 and YOLOX follow official repositories.

## Reported Results

| Method / Setting | Split | AP | AP50 | AP75 | FPS | Notes |
|---|---|---:|---:|---:|---:|---|
| ATSS | Part I | 22.3 | 46.1 | 18.5 | 24.2 | Best AP among ResNet-50-based models on Part I. |
| YOLOv5-m | Part II | 27.8 | 52.4 | 25.0 | 59.5 | Highest Part II AP in Table 1 and fastest listed model. |
| ATSS | Part II | 27.6 | 52.8 | 26.4 | 24.2 | Best AP50 and AP75 among ResNet-50-based methods in Table 1. |
| ScalableViT-S + Faster R-CNN | Part I | 21.2 | 46.4 | 15.1 | 10.9 | Best Transformer AP on Part I in Table 2. |
| Swin-T + Faster R-CNN | Part II | 27.0 | 52.4 | 24.5 | 18.1 | Best Transformer AP on Part II in Table 2. |

## Related Concepts

- [[SSGD]]
- [[Smartphone screen glass defect detection]]
- [[Glass inspection]]
- [[Industrial visual inspection]]
- [[Average precision]]
- [[mAP@0.50]]
- [[GFLOPs]]
- [[FPS]]
