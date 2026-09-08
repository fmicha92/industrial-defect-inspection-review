---
title: "DFMGAN"
aliases:
  - "DFMGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Generative Models"
source_papers:
  - "[[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]]"
evidence_count: 1
tags:
  - emerging-method
---
# DFMGAN

## Definition

DFMGAN is a few-shot defect image generator that trains a StyleGAN2 backbone on defect-free images, freezes that backbone, and trains defect-aware residual blocks plus a defect mapping network on limited defect images. It can generate defect images and masks by manipulating only defect-region features.

## Why It Matters

It provides a reusable model for generating realistic, diverse defect images when only a handful of labeled defect examples exist.

## Used In These Papers

- [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] introduces DFMGAN for MVTec AD few-shot defect image generation and downstream defect classification augmentation.

## Related Concepts

- [[Synthetic data generation]]
- [[Surface defect detection]]
- [[Defect-aware feature manipulation]]
- [[StyleGAN2]]
