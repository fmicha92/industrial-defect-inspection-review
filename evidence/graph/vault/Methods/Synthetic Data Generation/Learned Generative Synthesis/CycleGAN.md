---
title: "CycleGAN"
aliases:
  - "Cycle-consistent adversarial networks"
  - "Cycle-consistent GAN"
tags:
  - method
---

# CycleGAN

## Definition

CycleGAN learns unpaired image-to-image translation between two image domains using adversarial losses plus cycle-consistency losses that encourage translation into the other domain and back to reconstruct the original image.

## Why It Matters

CycleGAN enables domain translation when paired examples are unavailable. In synthetic-data workflows it can translate simulated or procedurally rendered images toward a real-image domain, but the method itself is learned generative synthesis rather than a simulator.

## Used In These Papers

- [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] introduces CycleGAN and evaluates it on unpaired translation tasks including maps/photos, labels/photos, object transfiguration, season transfer, style transfer, and photo enhancement.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] uses a Cyclic-GAN model to refine rendered industrial object images toward real images.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] uses CycleGAN as the benchmark wafer-map augmentation generator and reports lower accuracy than ViT augmentation at equalized class training sizes.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses CycleGAN for defect super-resolution and golden-template generation in weakly supervised periodic-texture defect segmentation.

## Related Concepts

- [[Learned generative synthesis]]
- [[Hybrid generative-procedural synthesis]]
- [[GAN]]
- [[Pix2Pix]]
- [[Domain gap]]
