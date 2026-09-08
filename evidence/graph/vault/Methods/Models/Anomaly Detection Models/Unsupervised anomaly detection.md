---
title: "Unsupervised anomaly detection"
tags:
  - concept
  - method
---

# Unsupervised anomaly detection

## Definition

Unsupervised anomaly detection learns normal patterns and detects deviations without requiring real labeled defect samples for training. In the paper notes, it is used for textured surface inspection and industrial anomaly localization.

## Why It Matters

Many industrial settings lack enough labeled defects to train supervised models. Unsupervised methods reduce this requirement, but their reliability depends on how well normal patterns are modeled and how synthetic or inferred anomalies are used during training.

## Used In These Papers









- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] benchmarks CFlow, DRAEM, DSR, EfficientAD, PaDiM, and Patchcore on [[AutoVI]] using normal-only training images and defective test images.
- [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] supports benchmarking, self-supervised anomaly detection.
- [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] supports metal part defect detection, complex industrial conditions.
- [[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]] supports heterogeneous same-sort anomaly detection, dataset.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] benchmarks PatchCore, PaDiM, CFlow, SimpleNet, DeSTSeg, RD, UniAD, and SoftPatch under standard and noisy unsupervised IAD settings.
- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] supports self-supervised pre-training, industrial anomaly dataset.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] supports 3D anomaly detection, industrial visual inspection.
- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] evaluates normal-only fabric anomaly detection on [[Lusitano]].
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] uses a normal feature memory bank and reconstruction for unsupervised textured defect inspection.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] uses expert-apprentice discrepancy optimization with synthetic abnormal inputs.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] trains [[STDAN]] with defect-free fabric images, feature-level defect amplification, and contrastive learning for anomaly detection and localization.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reviews unsupervised anomaly detection as a way to reduce image labeling and pixel-annotation costs in AOI.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reviews PatchCore, PaDiM, SPADE, autoencoder, GAN, and normal-only settings for industrial surface-defect detection.

## Related Concepts

- [[Unsupervised anomaly localization]]
- [[Unsupervised learning]]
- [[Anomaly Detection Models]]
- [[Defect segmentation]]
- [[MVTec AD]]
- [[Synthetic data generation]]
- [[Lusitano]]
- [[Lusitano benchmark]]
- [[Patch-based anomaly detection]]
- [[STDAN]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, frequency decoupling.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.

- [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] supports multimodal anomaly detection, crossmodal mapping.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.
