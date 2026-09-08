---
title: "PreCaCycleGAN"
aliases:
  - "Perceptual Capsule CycleGAN"
  - "Perceptual Capsule Cyclic Generative Adversarial Network"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2023 - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation]]"
evidence_count: 1
tags:
  - method
---

# PreCaCycleGAN

## Definition

PreCaCycleGAN is a CycleGAN-derived industrial defect sample augmentation method. It combines a U-Net and DenseNet generator, perceptual loss, least-squares adversarial training, cyclic consistency, identity mapping loss, and a capsule-network discriminator to generate defect samples from defect-free images.

## Why It Matters

The method is designed for sparse and imbalanced industrial defect data, where generated samples can improve detector generalization without requiring large collections of real defect images.

## Used In These Papers

- [[2023 - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation]]: evaluates generated DAGM2007 defect samples with YOLOv5, SSD, and Faster R-CNN and reports broad detection gains over CycleGAN-TSS and Tree-CycleGAN.

## Related Concepts

- [[GAN]]
- [[Data augmentation]]
- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[DAGM2007]]
