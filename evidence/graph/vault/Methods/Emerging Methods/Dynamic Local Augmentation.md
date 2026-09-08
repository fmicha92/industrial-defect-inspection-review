---
title: "Dynamic Local Augmentation"
aliases:
  - "Dynamic Local Augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]]"
evidence_count: 1
tags:
  - emerging-method
---
# Dynamic Local Augmentation

## Definition

Dynamic Local Augmentation generates local pseudo-abnormal image regions by applying hard local transformations such as rotation, ColorJitter, local permutation, and grayscale conversion, then weighting each transformed region by how much it differs from the original region. [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] uses this weighted local augmentation as a negative sample generator for self-supervised pixel-level anomaly localization.

## Why It Matters

Normal-only anomaly detection has no real defects during training. Dynamic local augmentation creates harder, location-sensitive pseudo-defects without treating every local transformation as equally useful, which the source paper reports is important because static local augmentation can generate ineffective abnormal samples and reduce MVTec AD AUROC.

## Used In These Papers


- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] uses [[Dynamic Local Augmentation]] for self-supervised anomaly detection, dynamic local augmentation.

## Related Concepts

- [[Data augmentation]]
- [[Self-supervised learning]]
- [[Industrial anomaly detection]]
- [[Regression-error anomaly scoring]]
- [[Monte Carlo dropout uncertainty scoring]]
