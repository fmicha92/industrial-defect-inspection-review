---
title: "Inference time"
aliases:
  - "average inference time"
tags:
  - metric
  - efficiency
---

# Inference Time

## Definition

Inference time measures how long a model takes to process an input at evaluation or deployment time.

## Direction

Lower is better when latency matters.

## Used In These Papers

- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] reports average inference time for FMR-Net and multilevel detection.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] reports about 2.31 ms per image for the ResNet18 PCB recognition network.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports LMFF inference time as 5.66 ms per image.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] reports [[WM-PeleeNet]] classifies 1000 wafer maps in 22.99 seconds on CPU.

## Related Metrics

- [[Detection time]]
- [[FPS]]
- [[Efficiency metrics]]
