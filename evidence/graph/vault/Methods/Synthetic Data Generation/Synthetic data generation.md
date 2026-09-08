---
title: Synthetic data generation
aliases:
  - Synthetic training data
  - Synthetic image generation
  - Data synthesis
tags:
  - method
---

# Synthetic data generation

## Definition

Synthetic data generation is a method family for creating artificial training, validation, or evaluation examples instead of relying only on collected real-world samples. Across the papers, synthetic data is generated through learned generators, simulation, procedural rendering, CT simulation, geometric augmentation, rule-based perturbation, or random anomaly synthesis.

## Why It Matters

The common motivation is defect scarcity: industrial defects are rare, expensive to collect, and hard to label. Synthetic data can provide labels automatically or expand small datasets, but the papers repeatedly surface the same risk: synthetic examples must transfer to real inspection conditions.

## Method Families

- [[Learned generative synthesis]]: model-generated data from trained generators such as GANs, diffusion models, VAEs, and image-to-image translation systems.
- [[Procedural and simulation-based synthesis]]: explicit rules, rendering, physics, simulators, domain randomization, or other controlled non-learned generators.
- [[Hybrid generative-procedural synthesis]]: systems that combine learned generators with procedural, rule-based, rendering, simulation, or physics-driven components.
- [[Rule-based data synthesis]]: explicit templates, constraints, perturbation policies, or generation rules for synthetic examples and labels.
- [[Defect synthesis]]: synthetic defect or anomaly generation for inspection, segmentation, detection, localization, or data augmentation.

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] uses local pasted patches as synthetic irregularities for self-supervised anomaly representation learning.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] uses transformer attention maps to guide synthetic patch anomalies in salient image regions.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] uses Simplex-noise pseudo-anomalies to train a contrastive reverse-distillation anomaly detector.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] uses attention-guided synthetic perturbations as training anomalies for RGBD industrial anomaly detection.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] uses class-selective anomaly simulation, including near-distribution anomaly augmentation, for reconstruction-based anomaly detection.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] uses realistic synthetic anomaly images generated from MVTec AD anomaly sources to train defect-map prediction.







- [[2014 - Generative Adversarial Nets]] introduces GANs as learned generative models that synthesize samples from random noise through an adversarially trained generator.
- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] introduces diffusion probabilistic models that synthesize samples by reversing a learned diffusion trajectory.
- [[2020 - Denoising Diffusion Probabilistic Models]] demonstrates diffusion-based image synthesis on CIFAR-10, CelebA-HQ, and LSUN.
- [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] refines simulator images with SimGAN while preserving synthetic labels.
- [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] introduces CycleGAN for unpaired image-to-image translation.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] mixes domain-randomized rendered images with Cyclic-GAN refined synthetic images.
- [[2018 - RenderGAN Generating Realistic Labeled Data]] combines a 3D marker model with learned GAN augmentations for labeled synthetic marker data.
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] generates context-aware synthetic road scenes for vehicle detection.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] introduces [[G2LGAN]], a global-to-local GAN strategy for synthetic minority-class wafer-map generation.
- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] supports PCB component inspection, generative augmentation.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] introduces [[JRGAN]] to generate wafer defect samples for imbalanced MIR-WM811K and [[MixedWM38]] training sets.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] generates synthetic defect and non-defect periodic texture images using DCGAN, CycleGAN, PatchMatch, and PSGAN to improve weakly supervised defect segmentation.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] trains on realistically simulated CT scans with precise voxel labels.
- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] uses GAN-based defect synthesis to improve downstream classification.
- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] generates synthetic adhesive inspection images and YOLO-format annotations.
- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] generates structural adhesive defect images with StyleGAN2-ADA to augment YOLOv4-Tiny object detection.
- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] studies DCGAN and geometric augmentation for AFP inspection images.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses procedural 3D defects, PBR, and domain randomization.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] includes DCGAN-based synthetic image generation.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] uses synthetic defects during unsupervised training.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] uses synthetic abnormal inputs generated by random perturbation.
- [[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]] evaluates synthetic scientific images as potential augmentation, simulation, and hypothesis-generation artifacts.
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] generates PV fault masks with an MLLM and composites them into real UAV thermal panel images for object detector training.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses [[Defect-Gen]] to generate synthetic defect image-mask pairs that improve mIoU on Defect Spectrum subsets.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] combines feature-level global anomaly synthesis and image-level local anomaly synthesis for industrial anomaly detection.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] generates 1,000 anomalous image-mask pairs per MVTec AD anomaly category for downstream localization, detection, and classification.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] generates 1,000 anomalous images per category with text, mask, and texture conditioning for downstream anomaly localization, detection, and classification.

## Related Concepts

- [[Domain gap]]
- [[Simulation-based data augmentation]]
- [[Procedural generation]]
- [[Rule-based data synthesis]]
- [[Defect synthesis]]
- [[Learned generative synthesis]]
- [[Procedural and simulation-based synthesis]]
- [[Hybrid generative-procedural synthesis]]
- [[SimGAN]]
- [[RenderGAN]]
- [[CycleGAN]]
- [[PSGAN]]
- [[Structured domain randomization]]
- [[GAN]]
- [[Scientific image generation]]
