---
title: "ADMF-Net"
aliases:
  - "Attention-based Dual-Branch Modal Fusion Network"
tags:
  - method
  - model
  - object-detection
model_family:
  - "[[YOLOv8]]"
related_methods:
  - "[[Dual-modal illumination for transparent material inspection]]"
  - "[[RGB Channel Fusion]]"
source_papers:
  - "[[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]]"
---

# ADMF-Net

## Definition

ADMF-Net is an attention-based dual-branch modal fusion network for aircraft glass canopy defect detection. It uses two CSPDarknet-like backbones to extract features from forward-lighting and backward-lighting images, fuses features with attention-based multimodal fusion modules, and predicts oriented bounding boxes.

## Why It Matters

Transparent-material defects can appear differently under different illumination directions. ADMF-Net uses feature-level fusion so forward-lighting and backward-lighting views can complement each other during defect detection.

## Used In These Papers

- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] reports ADMF-Net at 98.4% mAP50 and 66.9% mAP50-95 on ag_dual_obb.

## Related Concepts

- [[Aircraft glass canopy defect detection]]
- [[AGDD]]
- [[YOLOv8]]
- [[mAP@0.50]]
- [[mAP]]
