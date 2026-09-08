---
title: "mIoU"
aliases:
  - "mean Intersection over Union"
  - "mean IoU"
tags:
  - metric
  - segmentation
---

# mIoU

## Definition

mIoU is the mean Intersection over Union across defect types or classes. In the CSDD paper, it averages IoU values across scratches, spots, and rusts for defect segmentation.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] uses mIoU as the primary segmentation metric for [[CSDD benchmark]].
- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] reports 82.15% mIoU for [[PGA-Net]] on [[NEU-SEG]].
- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] reports mIoU 0.316 for a Mask R-CNN baseline on [[BSData]].
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] reports mean mIoU on [[Industrial-5i few-shot segmentation benchmark]], including 36.36 for 1-shot and 38.24 for 5-shot IndustrialNet.
- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] uses mIoU to compare [[F-labelImg]] annotations with manual labelImg annotations.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports mIoU on SolarCells, SolarCells-S, and PVEL-S, with LMFF reaching 82.9%, 74.0%, and 95.5%.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] reports 90.2% mIoU for [[FDSNet]] on [[MSD]], 63.9% on [[Magnetic Tile Defects]], and 78.8% on [[NEU-SEG]].
- [[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]] uses mIoU for solar-panel localization masks on [[SolarDK benchmark]].
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] reports median IoU for selected classes on [[BenchmarkELimages]], with DeepLabV3+ custom weights reaching 0.28 average mIoU across cracks, inactive areas, and gridline defects.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses mIoU as the primary semantic defect segmentation metric on Defect Spectrum subsets and reports synthetic-data improvements up to 9.85 points.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] reports mIoU for private semiconductor and [[TILDA]] periodic-texture defect segmentation, with the best private weakly supervised setting reaching 82.33%.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] uses mIoU for downstream anomaly segmentation and reports improvements over AnomalyDiffusion on MVTec AD, Real-IAD, and Floor Dirty.

## Related Metrics

- [[IoU]]
- [[FB-IoU]]
- [[Segmentation metrics]]
