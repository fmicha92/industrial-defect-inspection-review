---
title: "MobileNet"
aliases:
  - "MobileNetV1"
  - "MobileNetV2"
tags:
  - method
  - model
---

# MobileNet

## Definition

MobileNet is used in the processed wafer map paper as a lightweight convolutional model family built around depthwise separable convolutions and inverted residual blocks.

## Why It Matters

It supports lower-parameter wafer-map classification for high-volume semiconductor testing workflows and embedded deployment.

## Used In These Papers

- [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] trains MobileNetV1 and MobileNetV2-style models for WM-811K and a 21-defect wafer-map dataset.
- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] benchmarks MobileNetV3-S for gearbox component OK/nOK classification.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] replaces part of the Fast-SCNN high-level feature extractor with MobileNetV3 blocks inside [[FDSNet]].
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] evaluates MobileNetV2 for glass bottle defect classification, improving recall from 0.60 to 0.6744 with DDPM augmentation.
- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] uses MobileNetV3 transfer learning as the Keras CNN baseline for PV panel defect classification.

## Related Concepts

- [[Depthwise separable convolution]]
- [[Wafer map defect classification]]
- [[Defect classification]]
