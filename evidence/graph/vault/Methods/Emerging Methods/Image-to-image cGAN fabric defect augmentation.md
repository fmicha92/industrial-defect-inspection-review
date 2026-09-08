---
title: "Image-to-image cGAN fabric defect augmentation"
aliases:
  - "conditional image-to-image translation cGAN for fabric defect augmentation"
  - "fabric defect cGAN augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]]"
evidence_count: 1
tags:
  - method
---

# Image-to-image cGAN fabric defect augmentation

## Definition

Image-to-image cGAN fabric defect augmentation generates synthetic defective fabric samples from a clean fabric image and a segmented defect mask. The mask conditions the generated defect type, size, shape, and location while the clean image provides the fabric texture.

## Why It Matters

Fabric defect datasets are often small and imbalanced. A mask-conditioned generator can create additional defect samples for underrepresented defect types without collecting more defective fabric from production.

## Used In These Papers

- [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]]: uses AITEX fabric images and masks to generate synthetic defects and train segmentation models with improved accuracy, recall, precision, and F1-score.

## Related Concepts

- [[GAN]]
- [[U-Net]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Textile defect detection]]
