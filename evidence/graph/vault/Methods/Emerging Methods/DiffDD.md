---
title: "DiffDD"
aliases:
  - "DiffDD"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]]"
evidence_count: 1
tags:
  - emerging-method
---
# DiffDD

## Definition

DiffDD is a diffusion-based surface defect segmentation framework that combines a PvTv2 feature backbone, conditional image prior, feature guidance, semantic restoration, and a denoising diffusion model to reconstruct binary defect masks from inspection images.

## Why It Matters

It adapts diffusion models from unconstrained image generation to pixel-level defect segmentation, avoiding a separate postprocessing step for mask extraction while preserving image-mask semantic correspondence.

## Used In These Papers


- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] introduces DiffDD and reports mAP/AUROC of 87.75/97.68 on NEU-SEG, 68.41/95.21 on Magnetic Tile, 78.90/95.44 on KolektorSDD2, and 73.24/90.45 on DAGM2007.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Diffusion models]]
- [[Defect segmentation]]
