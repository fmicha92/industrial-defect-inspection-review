---
title: "IoU"
aliases:
  - "Intersection over union"
  - "intersection over union"
tags:
  - metric
  - segmentation
---

# IoU

## Definition

Intersection over union measures overlap between a predicted region or mask and a reference region or mask. It is used for CT defect segmentation evaluation.

## Direction

Higher is better.

## Used In These Papers


- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] reports mIoU and [[FB-IoU]] for binary defect segmentation on [[Industrial-5i]].
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] uses intersection over union as the primary metric for CT defect segmentation.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] uses IoU as part of the region-level matching criterion for fabric defect regions.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] uses IoU and mIoU for defect segmentation evaluation on [[CSDD benchmark]].
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports IoU on SolarCells, SolarCells-S, and PVEL-S, with LMFF reaching 68.5%, 51.0%, and 92.7%.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] uses IoU-derived median class scores to compare solar-cell EL segmentation masks on [[BenchmarkELimages]].
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] defines IoU for predicted and ground-truth defect masks and uses mIoU over defective regions as the primary result metric.
- [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]] uses IoU for anomaly segmentation overlap and reports 0.399 average IoU on [[MVTec AD]] and 0.231 IoU on [[Bottle-Cap Dataset]].

## Related Metrics

- [[Segmentation metrics]]
- [[Probability of detection]]
- [[mIoU]]
- [[FB-IoU]]
- [[ZJU-Leaper benchmark]]
