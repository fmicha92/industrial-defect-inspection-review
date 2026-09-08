---
title: "AU-PRO"
aliases:
  - "Area under per-region overlap"
tags:
  - metric
  - anomaly-detection
---

# AU-PRO

## Definition

AU-PRO measures area under the per-region overlap curve for anomaly localization evaluation. PRO averages the relative overlap between a thresholded prediction and each connected ground-truth anomaly component, so small and large defect regions contribute by region rather than by total pixel count alone.

## Direction

Higher is better.

## Evaluation Notes

- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] recommends integrating AU-PRO only up to low false-positive rates, no larger than 0.3, because anomalous regions are small relative to the image area.
- High integration limits can make methods look close to solved while allowing practically unacceptable numbers of false-positive pixels.

## Used In These Papers

- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] reports 94.8 PRO on MVTec AD with Simplex-noise pseudo-anomaly synthesis.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] reports AUPRO on MVTec AD and VisA, including 82.6 on MVTec AD and 80.5 on VisA.




- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] uses AU-PRO as the primary anomaly-localization benchmark metric for 3D and depth-image baselines.
- [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]] uses anomaly-localization evaluation context.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] reports P-AUPRO/P-PRO for Real-IAD pixel-level localization, including mean P-AUPRO 90.0 for single-view and 86.3 for multi-view UIAD settings.
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] reports PRO for anomaly localization, including 90.7 on MVTec AD and 75.2 on VisA.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] reports pixel-level PRO for GLASS, including 96.8 on MVTec AD and 98.2 on MPDD for GLASS-j.
- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] uses AU-PRO as the primary metric and reports gains on MVTec2D, MVTec3D, and automotive plastic parts.

## Related Metrics

- [[AU-ROC]]
- [[Anomaly detection metrics]]

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.
- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] reports 97.1% PRO on [[MVTec AD]] for region-wise anomaly localization.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.

- [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] supports multimodal anomaly detection, crossmodal mapping.
