---
title: "GAN"
aliases:
  - "Generative adversarial network"
  - "Generative adversarial networks"
tags:
  - concept
  - method
---

# GAN

## Definition

[[2014 - Generative Adversarial Nets]] introduced GANs as a generative modeling framework in which a generator learns to synthesize samples while a discriminator learns to distinguish generated samples from real data. The method is trained as an adversarial game, with the generator improving by making the discriminator fail.

## Why It Matters

GAN-based methods can create diverse defect appearances without manually collecting every defect class. The original paper also records practical limits that recur in later applications: no explicit density representation, discriminator-generator synchronization problems, and collapse risk when generation loses diversity.

## Used In These Papers






- [[2014 - Generative Adversarial Nets]] introduced the GAN concept and the adversarial generator-discriminator training framework.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] supports wafer map defect classification, class imbalance.
- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] supports PCB component inspection, generative augmentation.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] supports class imbalance, wafer map defect classification.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] proposes Defect-GAN for spatially and categorically controlled defect generation.
- [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] uses adversarial training to refine simulator images while preserving labels.
- [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] introduces CycleGAN for unpaired image-to-image translation.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] uses Cyclic-GAN refinement for synthetic industrial object images.
- [[2018 - RenderGAN Generating Realistic Labeled Data]] combines a 3D model with GAN-learned augmentations.
- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] uses StyleGAN2-ADA to generate structural adhesive defect images for object-detection data augmentation.
- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] studies conditional DCGAN for laser line scan defect images.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] uses DCGAN for synthetic image generation and Pix2Pix GAN for deblurring.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] compares DCGAN and StyleGAN against diffusion and text-to-image systems on scientific image datasets.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reviews GAN synthesis, GAN scoring, AnoGAN, and CycleGAN plus U-Net hybrids for visual defect detection.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reviews GANs for unsupervised defect detection, synthetic defect generation, and small-sample anomaly detection.

## Related Concepts

- [[Generative Models]]
- [[Learned generative synthesis]]
- [[DCGAN]]
- [[Pix2Pix]]
- [[CycleGAN]]
- [[SimGAN]]
- [[RenderGAN]]
- [[Defect synthesis]]
- [[Synthetic data generation]]
- [[Scientific image generation]]
- [[Parzen window log-likelihood]]

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] supports wafer map defect recognition, class imbalance.
