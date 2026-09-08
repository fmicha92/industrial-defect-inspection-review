---
title: "Diversified controllable defect synthesis"
aliases:
  - "Diversified controllable defect synthesis"
  - "DCDGANc"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]]"
evidence_count: 1
tags:
  - emerging-method
---
# Diversified controllable defect synthesis

## Definition

Diversified controllable defect synthesis generates defect content with controllable classes and diverse styles, then composites generated defects onto normal backgrounds to create labeled inspection samples. In [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]], DCDGANc uses class constant maps and OD-SPADE to generate multi-class defect contents from extracted defect regions.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label defect data when segmentation models need pixel-level synthetic defects rather than image-level augmentation alone.

## Used In These Papers


- [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]] introduces DCDGANc for controllable multi-class defect-content generation, improved Poisson blending, and pixel-mask synthetic data augmentation.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Poisson defect image augmentation]]
