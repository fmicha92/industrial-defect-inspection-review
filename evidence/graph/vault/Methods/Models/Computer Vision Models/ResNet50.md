---
title: "ResNet50"
aliases:
  - "ResNet-50"
tags:
  - method
  - model
---
# ResNet50

## Definition

ResNet50 is a 50-layer residual convolutional neural network commonly used as an image classifier or pretrained feature extractor.

## Why It Matters

ResNet50 provides transferable visual features for small industrial inspection datasets where training a deep CNN from scratch is impractical.

## Used In These Papers

- [[2016 - Deep Residual Learning for Image Recognition]] defines bottleneck residual architectures including 50-layer and deeper ResNets.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses ImageNet-pretrained ResNet-50 as the feature extractor for [[IndustrialNet]].
- [[2023 - Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning]] uses pretrained ResNet50 embeddings with SVM for bangle defect classification.
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] evaluates ResNet50V2 as the strongest augmented glass bottle classifier, improving accuracy from 0.78 to 0.93.
- [[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]] evaluates ResNet50 for SolarDK classification and as a DeepLabV3+ segmentation backbone.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] uses ImageNet-pretrained ResNet50 as the strongest DDN backbone, reporting 82.3 mAP on [[NEU-DET]].
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] uses ResNet50 as the default pretrained feature extractor for DiAD anomaly maps and reports the strongest image-level AUROC among tested extractors.

## Related Concepts

- [[Transfer learning]]
- [[Residual network]]
- [[Industrial visual inspection]]
- [[IndustrialNet]]
- [[SolarDK]]
