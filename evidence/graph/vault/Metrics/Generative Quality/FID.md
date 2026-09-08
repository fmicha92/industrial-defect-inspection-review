---
title: "FID"
aliases:
  - "Frechet Inception Distance"
  - "Frechet Inception Distance"
tags:
  - metric
  - generative-quality
---

# FID

## Definition

FID measures similarity between generated and reference image distributions. It is used as a generative-quality metric for defect synthesis.

## Direction

Lower is better.

## Used In These Papers

- [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] uses FID to compare generated defect images from ProGAN, CycleGAN, ablated DG-GAN variants, and the final DG-GAN model.
- [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] uses FID to evaluate generated pseudo defect image quality; lower values indicate generated and real defect image distributions are closer.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses FID to evaluate Con-GAN generated NEU-CLS defect images under limited samples.
- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] reports FID for defect generation across MVTec AD, MTD, and SDI categories; the paper cautions that low FID may hide overfitting on small datasets.

- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] reports FID values for Defect-GAN and comparison synthesis methods.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] reports FID for generated defect-free, crack, and finger-interruption EL images.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] uses FID for GC10-DET and NEU-CLS generated surface defect image quality and notes that FID can miss disappearing defect regions.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] uses FID to compare real and generated image distributions for CMC, EcoFAB, and Rocks datasets.
- [[2020 - Defect Image Sample Generation With GAN for Improving Defect Recognition]] uses FID to evaluate generated commutator cylinder defect images and states that SDGAN has the lowest FID for all defects except thread-line.
- [[2020 - Denoising Diffusion Probabilistic Models]] reports CIFAR-10 FID 3.17 for its best unconditional diffusion model and LSUN 256x256 FID values for church and bedroom samples.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses FID to evaluate Defect-Gen fidelity while selecting receptive-field and switch-timestep settings.
- [[2025 - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection]] uses FID to compare DDPM-CSD, DDPM, StableSDG, and GAN baselines for [[NEU-CLS]] defect generation.
- [[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]] reports FID for fabric enhancement quality and obtains 69.433 with the proposed OurSR method on TILDA.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] reports FID 162.01 for generated polyp images, compared with ArSDM at 361.55.

## Related Metrics

- [[Generative quality metrics]]
- [[GAN-Train GAN-Test]]
- [[SSIM]]
- [[LPIPS]]
- [[CLIPScore]]
