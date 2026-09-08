---
title: "JRGAN"
aliases:
  - "Jacobian Regularized Generative Adversarial Network"
  - "Jacobi regularized generative adversarial network"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Generative Models"
source_papers:
  - "[[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]]"
evidence_count: 1
tags:
  - method
---

# JRGAN

## Definition

JRGAN is a Jacobian-regularized auxiliary-classifier GAN for wafer-map sample generation. It adds Jacobian regularization to the generator and discriminator losses so generated samples and discriminator decisions are less sensitive to small input perturbations.

## Why It Matters

The method targets class imbalance in wafer defect datasets by generating minority-class wafer maps before training a [[ResNet-18]] classifier. In the source paper, JRGAN-balanced training improves MIR-WM811K accuracy from 95.14% to 97.24% and MixedWM38 accuracy from 94.19% in an imbalanced trial to 97.38%.

## Used In These Papers

- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] introduces JRGAN for [[WM-811K]] and [[MixedWM38]] wafer-map class-imbalance augmentation.

## Related Concepts

- [[GAN]]
- [[Data augmentation]]
- [[Synthetic data generation]]
- [[Wafer map defect classification]]
