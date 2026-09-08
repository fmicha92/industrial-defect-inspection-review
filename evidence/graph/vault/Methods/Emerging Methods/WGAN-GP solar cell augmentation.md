---
title: "WGAN-GP solar cell augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2024 - Improved Hybrid Solar Cell Defect Detection Using GANs and Weighted Classification]]"
evidence_count: 1
tags:
  - emerging-method
---
# WGAN-GP solar cell augmentation

## Definition

WGAN-GP solar cell augmentation uses Wasserstein GAN with gradient penalty to generate synthetic defective electroluminescence images for binary photovoltaic cell defect classification.

## Why It Matters

It addresses limited and imbalanced defective solar-cell data while avoiding some GAN training instability through gradient penalty.

## Used In These Papers

- [[2024 - Improved Hybrid Solar Cell Defect Detection Using GANs and Weighted Classification]] uses WGAN-GP generated images and reports 94.11% accuracy, 96.70% recall, and 95.71% F-score on ELPV.

## Related Concepts

- [[GAN]]
- [[Data augmentation]]
- [[Synthetic data generation]]
- [[Solar cell defect detection]]
