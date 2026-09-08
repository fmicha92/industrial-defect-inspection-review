---
title: "Learned generative synthesis"
aliases:
  - "ML-generated synthetic data"
  - "Model-generated synthetic data"
tags:
  - method
---

# Learned Generative Synthesis

## Definition

Learned generative synthesis creates synthetic data with trained models such as GANs, diffusion models, VAEs, or autoregressive generators.

## Typical Use

Useful when synthetic examples should match complex visual, textural, or distributional properties learned from real data.

## Related Concepts

- [[Synthetic data generation]]
- [[Hybrid generative-procedural synthesis]]
- [[Defect synthesis]]
- [[GAN]]
- [[Pix2Pix]]
- [[DCGAN]]
- [[PSGAN]]
- [[Generative Models]]
- [[Variational Autoencoder]]
- [[Diffusion models]]

## Used In These Papers

- [[2014 - Generative Adversarial Nets]] introduces adversarial learned synthesis from random noise through a generator trained against a discriminator.
- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] introduces diffusion-based learned synthesis by reversing a forward process that destroys data structure.
- [[2020 - Denoising Diffusion Probabilistic Models]] demonstrates high-quality image synthesis with denoising diffusion probabilistic models.
- [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] introduces CycleGAN for learned unpaired image-to-image translation.
- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] uses StyleGAN2-ADA as learned generative synthesis for structural adhesive defect augmentation.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses Con-GAN learned synthesis to generate defect images for recognition augmentation.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] evaluates learned generative synthesis for CMC microCT, EcoFAB root, and Rocks microCT images.
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] uses DDPM-generated defective glass bottle images to rebalance a small MVTec AD bottle classification set.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] introduces [[Defect-Gen]], a two-stage diffusion generator for paired defect images and masks under scarce defective data.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] combines [[DCGAN]], [[CycleGAN]], and [[PSGAN]] for synthetic defect and non-defect periodic texture generation.
- [[2022 - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables]] generates pseudo-anomalous samples from latent variables for anomaly detection on [[Magnetic Tile Defects]].
- [[2025 - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection]] uses [[DDPM-CSD]] to generate [[NEU-CLS]] steel defect images for classifier augmentation.
- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] uses LoRA-adapted Stable Diffusion to generate [[NEU-SEG]] segmentation training images.
- [[2026 - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks]] uses LoRA-adapted FLUX.2-dev to generate rare-class [[Magnetic Tile Defects]] images.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] uses [[Image-mask aligned diffusion synthesis]] to generate anomaly images with better mask correspondence and improve downstream segmentation.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses [[Qwen-Image generative augmentation]] to synthesize domain-aligned object-detection images and bounding boxes for RUOD and CarDD.
