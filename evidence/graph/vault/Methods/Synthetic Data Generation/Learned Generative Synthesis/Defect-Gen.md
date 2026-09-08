---
title: "Defect-Gen"
aliases:
  - "Defect Gen"
  - "two-stage diffusion-based defect generator"
tags:
  - method
  - synthetic-data-generation
---

# Defect-Gen

## Definition

Defect-Gen is a two-stage diffusion-based generator for creating paired defective images and masks from limited defective examples. It concatenates images and one-hot defect masks channel-wise so generated samples include both visual defects and corresponding labels.

## Why It Matters

Defect inspection datasets often have few defective samples. Defect-Gen addresses this by combining a large-receptive-field diffusion model for global structure with a small-receptive-field model for local patch diversity, aiming to avoid memorizing scarce training examples while preserving realistic product structure.

## Used In These Papers

- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] introduces Defect-Gen and reports that its synthetic samples improve mIoU for segmentation models on Defect Spectrum subsets.

## Related Concepts

- [[Defect Spectrum]]
- [[Synthetic data generation]]
- [[Learned generative synthesis]]
- [[Data augmentation]]
- [[FID]]
- [[LPIPS]]
