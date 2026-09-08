---
title: "TMFFNet"
aliases:
  - "Temporal Multi-Feature Fusion Network"
  - "Thermal-Sequence Guided Dual-Branch Network"
tags:
  - concept
  - architecture
---
# TMFFNet

## Definition

TMFFNet is a dual-branch temporal network that processes three consecutive thermal frames to classify pharmaceutical bag sealing defects.

## Why It Matters

The architecture is designed for subtle thermal defects under severe class imbalance. One branch fuses global and local thermal features, while a channel-aware SE-Dense branch suppresses background noise such as wrinkles.

## Used In These Papers

- [[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]] proposes TMFFNet for thermal pharmaceutical bag sealing defect detection.

## Related Concepts

- [[Pharmaceutical bag sealing defect detection]]
- [[Pharmaceutical packaging inspection]]
- [[Class imbalance]]
- [[Ghost module]]
- [[ResNet50]]
- [[Data augmentation]]
