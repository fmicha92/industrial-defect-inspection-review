---
title: "3DSR"
aliases:
  - "3DSR"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]]"
evidence_count: 1
tags:
  - method
---

# 3DSR

## Definition

3DSR is a 3D surface anomaly detection method that uses a Depth-Aware Discrete Autoencoder, simulated industrial depth pretraining, and dual subspace reprojection to produce anomaly segmentation masks from RGB+depth inputs.

## Why It Matters

It replaces slow point-cloud-heavy feature extraction with an efficient depth-image representation. [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] reports 97.8 mean image AUROC, 97.2 mean PRO, and 33 FPS on MVTec3D RGB+3D evaluation.

## Used In These Papers

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] introduces 3DSR and reports it outperforming M3DM in MVTec3D RGB+3D mean image AUROC (97.8 vs 94.5), mean PRO (97.2 vs 96.4), and speed (33 FPS vs 0.6 FPS).

## Related Concepts

- [[MVTec3D]]
- [[Simulation-based data augmentation]]
- [[Depth simulation]]
- [[AU-PRO]]
- [[FPS]]
