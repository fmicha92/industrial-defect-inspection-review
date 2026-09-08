---
title: "U-Net"
aliases:
  - "3D U-Net"
tags:
  - concept
  - architecture
---

# U-Net

## Definition

U-Net is an encoder-decoder segmentation architecture family used in the paper notes for defect localization. The notes include both a 3D U-Net-like CT segmentation network and customized U-Net models for aircraft engine defect segmentation.

## Why It Matters

U-Net-style architectures are useful when the inspection task needs dense pixel or voxel output. They also make label scarcity more severe, which is why the linked papers pair them with simulated CT labels or synthetic image generation.

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] compares a modified U-Net baseline against the proposed [[Segmentation-decision network]] on [[KolektorSDD]].

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses a U-Net-like decoder in [[IndustrialNet]] for binary defect-mask prediction.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] uses a U-Net-like 3D encoder-decoder for high-recall CT defect segmentation.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] trains customized U-Net models with several losses for compressor blade defect segmentation.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] uses U-Net variants for transfer-learning, data-augmentation, weakly supervised, and fully supervised fabric defect segmentation baselines.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] reports U-Net as the best listed segmentation baseline on [[CSDD benchmark]].
- [[2020 - Surface Defect Saliency of Magnetic Tile]] uses U-Net inside [[MCuePush U-Net]] for magnetic-tile surface-defect saliency on [[Magnetic Tile Defects]].
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] uses U-Net to segment affected solar panel regions before feature extraction and classification.
- [[2020 - Denoising Diffusion Probabilistic Models]] uses a U-Net backbone for image denoising in the reverse diffusion process.
- [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]] adapts U-Net into [[GSLU-Net]] for lightweight heat-sink scratch and stain segmentation.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] evaluates two U-Net implementations on [[BenchmarkELimages]].
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reviews U-Net and U-Net-inspired methods as core pixel-level defect segmentation approaches.

## Related Concepts

- [[Segmentation Models]]
- [[Neural Networks]]
- [[Computer Vision Models]]
- [[Defect segmentation]]
- [[Synthetic data generation]]
- [[Simulation-based data augmentation]]
- [[CSDD benchmark]]
- [[ZJU-Leaper benchmark]]
- [[Solar cell defect detection]]
- [[IncepViTH-Net]]
- [[GSLU-Net]]
- [[IndustrialNet]]
- [[MCuePush U-Net]]
- [[Magnetic Tile Defects]]
