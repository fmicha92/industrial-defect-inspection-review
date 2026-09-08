---
title: "MDGAN"
aliases:
  - "MDGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2022 - Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures]]"
evidence_count: 1
tags:
  - emerging-method
---
# MDGAN

## Definition

MDGAN is a mask-guided defect generation adversarial network for industrial defect images with non-uniform structures. It takes Gaussian noise, a pseudo-normal background, and a binary mask, then generates a defect image whose mask supplies pixel-level annotation.

## Why It Matters

MDGAN preserves normal backgrounds while independently controlling defect shape and texture, which makes its generated images useful for downstream defect segmentation training.

## Used In These Papers


- [[2022 - Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures]] uses [[MDGAN]] for mask-guided defect generation, non-uniform structures.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[CycleGAN]]
- [[U-Net]]
- [[FID]]
- [[SSIM]]
