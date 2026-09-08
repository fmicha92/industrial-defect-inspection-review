---
title: "LPIPS"
tags:
  - metric
concept_type: metric
---
# LPIPS

## Definition

LPIPS is recorded as a generative-quality or perceptual-distance metric when a linked paper reports it. Exact implementation details are `not reported` unless provided by the source paper.

## Used In These Papers

- [[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]] reports LPIPS for fabric image enhancement quality and obtains 0.357 with the proposed OurSR method on TILDA.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] reports LPIPS 0.698 for generated polyp images, compared with ArSDM at 0.869.

- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] uses LPIPS with nearest-neighbor analysis and classifier performance to diagnose synthetic-sample similarity and potential overfitting.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] reports mean IC-LPIPS 0.33 on MVTec AD and 0.33 on MVTec LOCO for generated anomaly diversity.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] uses LPIPS for paired scientific image editing and variation evaluations.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses LPIPS to reason about Defect-Gen sample diversity under similar FID.

## Related Concepts

- [[Generative quality metrics]]
- [[SSIM]]
- [[FID]]
- [[CLIPScore]]
