---
title: "DCGAN"
aliases:
  - "Deep convolutional GAN"
tags:
  - concept
  - method
---

# DCGAN

## Definition

DCGAN is the GAN variant named in the paper notes for convolutional image synthesis. It is used for defect image generation in fiber layup inspection and aircraft engine inspection.

## Why It Matters

The papers use DCGAN when real defect imagery is scarce and additional synthetic samples are needed. The approach is promising for image augmentation, but the notes also record concerns about training instability, artifacts, and modality-specific transfer.

## Used In These Papers

- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] investigates conditional DCGAN with geometric transformations for AFP defect images.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] uses a customized DCGAN for synthetic aircraft engine defect images.
- [[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]] uses DCGAN to generate wafer bin map defect patterns for class-imbalanced [[WM-811K]] classification.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses DCGAN-style synthetic defect generation before CycleGAN super-resolution and golden-template generation.

## Related Concepts

- [[GAN]]
- [[Generative Models]]
- [[Learned generative synthesis]]
- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[Automated fiber placement inspection]]
