---
title: "EID-GAN"
aliases:
  - "EID-GAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]]"
evidence_count: 1
tags:
  - emerging-method
---
# EID-GAN

## Definition

EID-GAN is a GAN-based augmentation method for extremely imbalanced industrial defect data where the outlier occupies only a tiny part of a defective image. It adds an outlier norm penalty to the generator loss so generated negative samples include visible defect regions rather than only normal-looking image content.

## Why It Matters

It is relevant when ordinary GANs, SMOTE, or geometric augmentation increase sample counts but fail to synthesize the small defect feature that a detector must learn.

## Used In These Papers


- [[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]] introduces EID-GAN for tiny-outlier synthesis on Fabric, Piston, and DAGM imbalanced defect datasets.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[GAN]]
