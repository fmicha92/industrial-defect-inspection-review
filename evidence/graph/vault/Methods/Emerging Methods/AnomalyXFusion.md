---
title: "AnomalyXFusion"
aliases:
  - "AnomalyXFusion"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]]"
evidence_count: 1
tags:
  - emerging-method
---
# AnomalyXFusion

## Definition

AnomalyXFusion is a multi-modal diffusion-based anomaly synthesis method for industrial inspection. It combines text anomaly descriptions, anomaly masks, and masked anomaly texture images through Multi-modal In-Fusion, then adjusts the fused condition by diffusion timestep through Dynamic Dif-Fusion.

## Why It Matters

It supports controllable anomaly generation when real defects are scarce. The method is especially relevant for logical anomalies, where text can state missing, wrong-count, misplaced, or wrong-color object relationships that are not fully specified by masks alone.

## Used In These Papers


- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] introduces AnomalyXFusion with semantic, location, and texture conditioning, reporting MVTec AD mean IS 1.82, IC-LPIPS 0.33, localization AUC-P 99.3, and anomaly classification accuracy 74.70%.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Diffusion models]]
- [[MVTec Caption]]
