---
title: "Defect synthesis"
aliases:
  - "Synthetic defect generation"
  - "Synthetic anomalies"
tags:
  - concept
  - method
---

# Defect synthesis

## Definition

Defect synthesis is the generation of artificial defects or anomalies for training, augmentation, or anomaly-localization objectives. It includes GAN-generated surface defects, simulated adhesive defects, procedural 3D defect tools, CT defect simulation, and random anomaly perturbations.

## Why It Matters

Defects are often rare, expensive, or unsafe to collect at scale. Synthetic defects help build training sets and labels, but the generated defects must match the important visual or geometric properties of real defects enough to improve real-world inspection.

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] synthesizes local defects by cutting and pasting normal image patches.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] creates synthetic pasted-patch anomalies at attention-selected salient regions.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] synthesizes pseudo-anomalies with Simplex noise for contrastive distillation.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] uses attention-guided synthetic perturbations for multimodal RGBD anomaly training.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] compares and selects multiple anomaly simulation methods for reconstruction-based detection.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] creates realistic synthetic defects using MVTec AD anomaly sources and foreground-aware placement.
- [[2023 - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples]] generates object-aware and texture-aware synthetic anomalies through patch extraction, augmentation, and paste.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] uses [[PatchAnomaly]] to create local synthetic defects for supervised anomaly localization from normal-only training images.
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] evaluates multiple pseudo-anomaly insertion methods and introduces [[Affine anomaly insertion]].
- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] trains its first-stage discriminative network on synthetic anomalies before contrastive feature adaptation.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] uses [[Image-mask aligned diffusion synthesis]] to generate anomaly image-mask training pairs.


- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] focuses directly on high-fidelity controllable defect synthesis.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] creates 3D blowhole defects with procedural tools and rendering.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] uses synthetic abnormal inputs to shape discrepancy distributions.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] uses synthetic defects in unsupervised textured surface inspection.
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] synthesizes PV faults including damage, cracks, snail trails, dust, delamination, and hotspots.

## Related Concepts

- [[Synthetic data generation]]
- [[Learned generative synthesis]]
- [[Procedural and simulation-based synthesis]]
- [[Hybrid generative-procedural synthesis]]
- [[GAN]]
- [[Domain gap]]
- [[Procedural generation]]

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.
