---
title: "PatchAnomaly"
aliases:
  - "Patch-wise anomaly augmentation"
  - "Patch-wise augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Procedural and Simulation-Based Synthesis"
source_papers:
  - "[[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]]"
evidence_count: 1
tags:
  - method
---

# PatchAnomaly

## Definition

PatchAnomaly is a patch-wise pseudo-defect generation method for unsupervised visual anomaly detection. It selects multiple local patches from a normal image, subdivides and transforms them with self-supervised tasks such as rotation, jigsaw, and context inpainting, blends them back into the image, and records the augmented patch boxes as surrogate supervision.

## Why It Matters

The method turns anomaly detection with only normal training images into a supervised localization problem by producing anomaly-like images with labels. Its design preserves most normal image content while perturbing local regions, matching the paper's claim that industrial anomalies are often subtle and fine-grained.

## Used In These Papers

- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] uses PatchAnomaly to train a reconstruction-detection model on synthetic local defects and reports 98.4/97.0 image-/pixel-level AUROC on [[MVTec AD]] and 95.5/97.4 on [[BTAD]].

## Related Concepts

- [[Defect synthesis]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Self-supervised learning]]

