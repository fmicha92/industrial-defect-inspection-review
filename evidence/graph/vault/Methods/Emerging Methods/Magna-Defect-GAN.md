---
title: "Magna-Defect-GAN"
aliases:
  - "Magna-Defect-GAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks]]"
evidence_count: 1
tags:
  - emerging-method
---
# Magna-Defect-GAN

## Definition

Magna-Defect-GAN is a conditional mask-to-image GAN for synthesizing magnetic particle inspection defect images. It maps a defect mask, latent noise vector, and guide vector for background, defect thickness, and brightness to a realistic defect image.

## Why It Matters

It supports scarce-defect learning by generating controlled intraclass variation, including defect size, shape, position, thickness, brightness, and background. In its source paper, classifiers trained with both conventional augmentation and Magna-Defect-GAN samples outperform original-only and single-augmentation settings.

## Used In These Papers


- [[2023 - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks]] proposes Magna-Defect-GAN for line-scan magnetic particle inspection defect synthesis and reports better [[Inception Score]] and [[FID]] than [[Pix2Pix]] and [[CycleGAN]].

## Method Details

- Generator: U-Net-style conditional generator with mask projection and latent projection branches.
- Mask embedding: 32-dimensional embedding produced by seven stride-2 convolution layers.
- Latent input: 132-dimensional noise vector.
- Guide vector: three controls for background, thickness, and brightness.
- Discriminator: modified PatchGAN discriminator using 16 x 16 local patches.
- Losses: adversarial loss, L2 reconstruction loss, and VGG-based style loss.
- Training: average 200 epochs on a single Nvidia 12 GB Titan X GPU.

## Related Concepts

- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[GAN]]
- [[U-Net]]
- [[FID]]
- [[Inception Score]]
