---
title: "Regression-error anomaly scoring"
aliases:
  - "Feature-map regression error"
  - "Regression error anomaly score"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]]"
evidence_count: 1
tags:
  - emerging-method
---
# Regression-Error Anomaly Scoring

## Definition

Regression-error anomaly scoring compares a test image's feature maps with the average feature maps from normal training images. In [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]], differences from ResNet stages C2, C3, and C4 are upsampled to 224 x 224 and averaged per pixel.

## Why It Matters

The score converts normal-only dense representations into a localization signal: pixels whose feature values deviate from the normal training average receive higher anomaly scores.

## Used In These Papers

- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] uses regression error as one part of the final pixel-level anomaly score.

## Related Concepts

- [[Dynamic Local Augmentation]]
- [[Monte Carlo dropout uncertainty scoring]]
- [[Industrial anomaly detection]]
- [[AU-ROC]]
