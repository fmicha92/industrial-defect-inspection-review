---
title: "FEGAN"
aliases:
  - "FEGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]]"
evidence_count: 1
tags:
  - emerging-method
---
# FEGAN

## Definition

FEGAN is a normal-only industrial anomaly detection and localization method introduced in [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]]. It combines a VGG19-based feature extraction network with an improved GAN and scores anomalies from both deep feature residuals and image-space reconstruction residuals.

## Why It Matters

FEGAN targets industrial inspection settings where abnormal samples are scarce or difficult to label. On [[MVTec AD]], it reports 0.978 image-level AUC-ROC, 0.982 pixel-level AUC-ROC, and 0.399 IoU; on [[Bottle-Cap Dataset]], it reports 0.956 image-level AUC-ROC, 0.979 pixel-level AUC-ROC, and 0.231 IoU.

## Used In These Papers


- [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]] introduces [[FEGAN]] with a Feature Extraction Network, Improved GAN, Multi-scale Self-Enhancement, and a combined feature/image anomaly score.

## Related Concepts

- [[Industrial anomaly detection]]
- [[Defect segmentation]]
- [[Feature extraction]]
- [[GAN]]
- [[MVTec AD]]
- [[Bottle-Cap Dataset]]
