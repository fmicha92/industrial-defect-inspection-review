---
title: "GLASS"
aliases:
  - "GLASS"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]]"
evidence_count: 1
tags:
  - emerging-method
---
# GLASS

## Definition

GLASS is a Global and Local Anomaly co-Synthesis Strategy for industrial anomaly detection and localization. It combines feature-level Global Anomaly Synthesis with Gaussian noise, gradient ascent, and truncated projection, plus image-level Local Anomaly Synthesis using Perlin/foreground masks and texture overlays.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label defect data in industrial visual inspection.

## Used In These Papers


- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] introduces GLASS and reports 99.9 image-level AUROC, 99.3 pixel-level AUROC, and 96.8 PRO on MVTec AD, plus strong weak-defect results on MAD-man and MAD-sys.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[AU-ROC]]
- [[AU-PRO]]
