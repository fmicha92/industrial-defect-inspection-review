---
title: "Unsupervised anomaly localization"
tags:
  - concept
  - method
---

# Unsupervised anomaly localization

## Definition

Unsupervised anomaly localization identifies where anomalies occur while avoiding dependence on real labeled anomaly samples during training. In the paper notes, it is evaluated with pixel- or region-level metrics such as AU-ROC and AU-PRO.

## Why It Matters

Localization is more useful than image-level anomaly flags for inspection workflows, but labels are expensive. The linked papers address this by learning normal feature structure, reconstruction behavior, or discrepancy distributions.

## Used In These Papers



- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] supports 3D anomaly detection, industrial visual inspection.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] directly targets unsupervised image anomaly localization with collaborative discrepancy optimization.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] localizes textured surface defects through memory features and reconstruction.

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Unsupervised learning]]
- [[Anomaly Detection Models]]
- [[Defect segmentation]]
- [[Synthetic data generation]]
- [[MVTec AD]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.
