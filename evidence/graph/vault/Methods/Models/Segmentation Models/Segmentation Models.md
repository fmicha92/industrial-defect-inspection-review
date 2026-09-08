---
title: "Segmentation Models"
tags:
  - model-family
---

# Segmentation Models

Segmentation models assign labels to pixels, voxels, or regions. They are mainly used for defect masks, anomaly localization, and dense inspection outputs.

## Examples

- [[Segmentation-decision network]]
- [[U-Net]]
- [[PSPNet]]
- [[Unsupervised anomaly localization]]
- [[Defect segmentation]]
- [[FDSNet]]

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] proposes a [[Segmentation-decision network]] for image-level defect detection from pixel-wise masks.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] uses 3D CT voxel segmentation.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] uses U-Net-style image segmentation.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] and [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] evaluate anomaly localization as dense defect output.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] introduces [[LMFF]] as a lightweight solar-cell defect segmentation model.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] introduces [[FDSNet]] for real-time surface-defect segmentation.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] compares U-Net, PSPNet, and DeepLabv3+ on [[BenchmarkELimages]].
