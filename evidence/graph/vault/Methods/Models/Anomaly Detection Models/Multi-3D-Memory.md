---
title: "Multi-3D-Memory"
aliases:
  - "Multi-3D-Memory"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]]"
evidence_count: 1
tags:
  - method
---

# Multi-3D-Memory

## Definition

Multi-3D-Memory is an unsupervised multimodal industrial anomaly detection method for RGB images and 3D point clouds. It uses patch-wise contrastive feature fusion, separate RGB/3D/fused memory banks, and decision-layer fusion for image-level anomaly detection and segmentation.

## Why It Matters

Directly concatenating RGB and point-cloud features can disturb the modalities. Multi-3D-Memory preserves single-modality evidence while still learning feature interaction, which improves reported MVTec-3D AD detection and segmentation performance.

## Used In These Papers

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] proposes Multi-3D-Memory and reports 0.945 mean I-AUROC and 0.964 mean AUPRO on [[MVTec3D]] in the RGB + 3D setting.

## Method Details

- RGB branch: DINO-pretrained ViT-B/8 patch features.
- 3D branch: ShapeNet-pretrained Point Transformer features.
- Alignment: Point Feature Alignment maps point features back to the RGB-aligned 2D plane.
- Fusion: Unsupervised Feature Fusion uses patch-wise contrastive loss.
- Memory banks: separate RGB, 3D, and fused-feature memory banks.
- Decision layer: combines memory-bank anomaly scores and segmentation maps.

## Related Concepts

- [[MVTec3D]]
- [[Unsupervised anomaly detection]]
- [[Vision Transformer]]
- [[AU-PRO]]

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.
