---
title: "MVTec3D"
aliases:
  - "MVTec 3D"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://www.mvtec.com/research-teaching/datasets/mvtec-3d-ad"
data_sources: "MVTec"
introduced_by: "[[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]]"
related_papers:
  - "[[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]]"
availability: "public"
access: "downloadable from MVTec research dataset page"
licenses:
  - "CC BY-NC-SA 4.0"
---
# MVTec3D

## Definition

MVTec3D is a public industrial anomaly localization benchmark with 4147 high-resolution 3D scans from 10 object categories. Each sample provides 3D coordinate data and RGB values, with normal-only training and validation splits and pixel-precise anomaly annotations for anomalous test samples.

## Why It Matters

It extends MVTec-style industrial anomaly detection from RGB images into 3D inspection data. The introducing benchmark shows that voxel and depth-image baselines leave substantial room for improvement, especially when localization is evaluated with [[AU-PRO]] at low false-positive rates.

## Dataset Details

- Total scans: 4147.
- Categories: bagel, cable gland, carrot, cookie, dowel, foam, peach, potato, rope, and tire.
- Splits: 2656 training scans, 294 validation scans, 249 good test scans, and 948 anomalous test scans.
- Anomalies: 41 defect types and 1148 annotated regions.
- Modalities: `(x, y, z)` coordinate images, RGB values, point clouds, and ground-truth anomaly masks for anomalous test samples.
- Acquisition: Zivid One+ Medium structured-light 3D sensor with fixed per-category viewpoint and indirect diffuse lighting.
- Evaluation: localization uses [[AU-PRO]]; sample-level anomaly detection uses [[AU-ROC]].
- Availability: public download from https://www.mvtec.com/research-teaching/datasets/mvtec-3d-ad.
- License: CC BY-NC-SA 4.0; commercial use is not allowed under the MVTec terms.

## Used In These Papers



- [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]] contrasts with MVTec 3D as prior multimodal industrial anomaly-detection groundwork.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] introduces the dataset and reports initial 3D/depth anomaly-localization baselines.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] reports CDO results on MVTec3D and a 10.72% AU-PRO gain over 3D-ST.

## Source Anchors

- Hosting source: https://www.mvtec.com/research-teaching/datasets/mvtec-3d-ad.
- Introducing paper: [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]].
- Access terms: CC BY-NC-SA 4.0, noncommercial.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[MVTec AD]]
- [[Unsupervised anomaly localization]]
- [[Defect segmentation]]
- [[Industrial visual inspection]]

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.
- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] evaluates 3DSR on MVTec3D and reports 97.8 mean RGB+3D image AUROC, 99.5 pixel AUROC, 97.2 PRO, and 33 FPS.

- [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] supports multimodal anomaly detection, crossmodal mapping.
