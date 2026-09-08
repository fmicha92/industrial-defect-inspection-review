---
title: "DAGM"
aliases:
  []
availability: "not reported"
status: stable
concept_type: dataset
related_domain: "[[Multi-industry anomaly detection]]"
url: "not reported"
data_sources: "not reported"
introduced_by: "not reported"
---
# DAGM

## Definition

DAGM is recorded in the processed FMR-Net note as an evaluation dataset for textured surface defect inspection. Availability: `not reported`.

## Why It Matters

It connects FMR-Net to textured surface defect detection evaluation.

## Used In These Papers

- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] uses this dataset as reported in the processed paper note.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] evaluates weak, mixed, and fully supervised surface-defect detection on DAGM.
- [[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]] uses DAGM category 1 as a public general imbalanced comparison dataset, reporting 150 negative grayscale images of size 1 x 512 x 512.

## Dataset Details

- Images: grayscale images of 10 computer-generated surfaces.
- Defects: scratches or spots.
- Task framing: each surface is treated as a binary classification problem.
- Annotation form reported by the mixed-supervision paper: ellipse regions.

## Source Anchors

- Hosting source: not reported.
- Introducing paper: not reported.

## Related Concepts

- [[Multi-industry anomaly detection]]
- Smart manufacturing
- [[Surface defect detection]]
- [[Unsupervised anomaly detection]]
