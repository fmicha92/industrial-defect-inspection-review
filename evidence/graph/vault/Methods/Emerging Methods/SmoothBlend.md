---
title: "SmoothBlend"
aliases:
  - "SmoothBlend"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]]"
evidence_count: 1
tags:
  - emerging-method
---
# SmoothBlend

## Definition

SmoothBlend is a local augmentation used by SPot-the-Difference pre-training. It creates a subtle local perturbation by color-jittering a patch cut from the same image, pasting it at a random location, and blending it with a Gaussian-blurred alpha mask.

## Why It Matters

The perturbation supplies local negatives for anomaly-oriented self-supervised pre-training, encouraging features to remain sensitive to small surface or structural differences rather than only global semantics.

## Used In These Papers

- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] uses SmoothBlend to generate local spot-the-difference negatives for SPD regularization.

## Related Concepts

- [[Data augmentation]]
- [[Self-supervised learning]]
- [[Industrial anomaly detection]]
- [[Defect segmentation]]
