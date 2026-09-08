---
title: "Depthwise separable convolution"
tags:
  - method
---

# Depthwise Separable Convolution

## Definition

Depthwise separable convolution is used in the processed wafer-map paper as a lightweight convolution strategy to reduce model parameters and computation.

## Why It Matters

It enables wafer-map classification models intended for high-volume testing and low-cost embedded platforms.

## Used In These Papers

- [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] uses depthwise separable convolutions in DMC1 and DMC2.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] uses depthwise separable convolution inside depthwise separable residual blocks to reduce LMFF computation and parameters.

## Related Concepts

- [[MobileNet]]
- [[Wafer map defect classification]]
- [[LMFF]]
