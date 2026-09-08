---
title: "AnomalyDiffusion"
aliases:
  - "AnomalyDiffusion"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]]"
evidence_count: 1
tags:
  - emerging-method
---
# AnomalyDiffusion

## Definition

AnomalyDiffusion is a few-shot diffusion-based anomaly generation method that produces anomalous image-mask pairs. It uses Spatial Anomaly Embedding to separate anomaly appearance from mask-derived location information and Adaptive Attention Re-weighting to improve generated anomaly-mask alignment.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label defect data in industrial visual inspection.

## Used In These Papers


- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] introduces AnomalyDiffusion and reports downstream MVTec AD localization at 99.1 pixel AUROC, 81.4 AP, and 76.3 F1-max using generated data.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Diffusion models]]
- [[MVTec AD]]
