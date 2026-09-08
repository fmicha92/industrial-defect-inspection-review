---
title: "Diffusion models"
aliases:
  - "Diffusion models"
status: promoted
concept_type: method
candidate_parent: "Methods/Models/Generative Models"
source_papers:
  - "[[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]]"
  - "[[2020 - Denoising Diffusion Probabilistic Models]]"
  - "[[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]]"
  - "[[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]]"
  - "[[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]]"
  - "[[2025 - Enhancing Glass Defect Detection with Diffusion Models]]"
evidence_count: 6
tags:
  - method
---

# Diffusion models

## Definition

Diffusion models are generative models that define a forward process which gradually destroys data structure with noise and a learned reverse process which denoises from a tractable noise distribution back to data. [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] introduced this diffusion probabilistic modeling idea; [[2020 - Denoising Diffusion Probabilistic Models]] made the approach practical and prominent for high-quality image synthesis.

## Why It Matters

Diffusion models provide a flexible learned generative synthesis route with tractable training objectives, explicit denoising dynamics, and strong image-generation quality. Later anomaly, scientific-image, and defect-synthesis papers use the family as a central image-generation or reconstruction mechanism.

## Used In These Papers

- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] introduces diffusion probabilistic models by learning the reverse of a forward diffusion chain that maps data to noise.
- [[2020 - Denoising Diffusion Probabilistic Models]] shows high-quality image synthesis with diffusion models, connects the method to denoising score matching, and reports CIFAR-10 FID 3.17.
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] uses diffusion denoising for multi-class anomaly reconstruction and reports that direct DDPM/LDM baselines suffer category or semantic reconstruction failures.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] uses latent diffusion priors for few-shot anomaly image-mask generation and introduces spatial anomaly embeddings plus attention re-weighting.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] uses diffusion for text-, mask-, and texture-conditioned anomaly synthesis through Multi-modal In-Fusion and Dynamic Dif-Fusion.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] evaluates diffusion-based image editing and variation systems for scientific image synthesis.
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] trains a U-Net-based DDPM on defective MVTec AD bottle images and uses generated defects for glass classification augmentation.

## Related Concepts

- [[DiAD]]
- [[Unsupervised anomaly detection]]
- [[Scientific image generation]]
- [[Generative Models]]
- [[Learned generative synthesis]]
- [[Generative modeling]]
