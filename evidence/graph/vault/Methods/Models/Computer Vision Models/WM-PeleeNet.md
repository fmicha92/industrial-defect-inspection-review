---
title: "WM-PeleeNet"
aliases:
  - "Wafer Map PeleeNet"
  - "WM PeleeNet"
tags:
  - method
  - model
---

# WM-PeleeNet

## Definition

WM-PeleeNet is a lightweight convolutional wafer-map classifier derived from PeleeNet. Yu et al. prune the PeleeNet structure for wafer defect-pattern recognition and add [[Convolutional Block Attention Module]] before global average pooling and classification.

## Why It Matters

The model is designed for semiconductor wafer-map inspection where classification accuracy, low parameter count, low FLOPs, and CPU inference speed all matter for deployment.

## Used In These Papers

- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] proposes WM-PeleeNet and reports 93.6% accuracy on [[WM-811K]], 97.5% on [[MixedWM38]], 0.169M parameters, 0.316 GFLOPs, and 22.99 s for 1000 wafer maps.

## Related Concepts

- [[Wafer map defect classification]]
- [[Deep convolutional neural network]]
- [[Convolutional Block Attention Module]]
- [[Parameter count]]
- [[GFLOPs]]
- [[Inference time]]
