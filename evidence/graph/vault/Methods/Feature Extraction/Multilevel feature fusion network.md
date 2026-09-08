---
title: "Multilevel feature fusion network"
aliases:
  - "MFN"
  - "multilevel-feature fusion network"
  - "multi-level feature fusion network"
tags:
  - method
  - feature-extraction
---

# Multilevel Feature Fusion Network

## Definition

Multilevel feature fusion network is a feature-fusion module introduced in [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]. It takes feature maps from multiple ResNet stages, normalizes their scale and dimensionality, and concatenates them into a multilevel representation for defect proposal generation.

## Why It Matters

Steel surface defect localization depends on small spatial details that can be filtered out in deep CNN layers. MFN preserves lower-level location cues while retaining higher-level semantic features, improving proposal quality for [[NEU-DET]] detection.

## Used In These Papers

- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] uses MFN inside [[Defect Detection Network]] and attributes DDN's mAP gain over Faster R-CNN to higher-quality region proposals from multilevel features.

## Related Concepts

- [[Defect Detection Network]]
- [[ResNet50]]
- [[Faster R-CNN]]
- [[Object detection]]
- [[Metallic surface defect detection]]
- [[NEU-DET]]
