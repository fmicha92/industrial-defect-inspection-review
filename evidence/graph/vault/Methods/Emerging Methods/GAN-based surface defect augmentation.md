---
title: "GAN-based surface defect augmentation"
aliases:
  - "GAN-based surface defect augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]]"
  - "[[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]]"
  - "[[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]]"
evidence_count: 3
tags:
  - emerging-method
---
# GAN-based surface defect augmentation

## Definition

GAN-based surface defect augmentation uses generative adversarial networks to synthesize additional industrial defect images for classifier or detector training. Linked papers use the pattern for steel surface defect classification and structural adhesive defect object detection.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label defect data in industrial visual inspection.

## Used In These Papers


- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] proposes a dual-discriminator GAN regularization method for limited-data surface defect image generation.
- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] uses StyleGAN2-ADA generated adhesive defect images to augment YOLOv4-Tiny object-detection training.
- [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] uses GAN-based augmentation on NEU-CLS and reports DCGAN-augmented CNN accuracy of 95.78% versus 90.28% for classic augmentation.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[GAN]]
- [[DCGAN]]
- [[NEU-CLS]]
- [[Structural Adhesive Defects Dataset]]
