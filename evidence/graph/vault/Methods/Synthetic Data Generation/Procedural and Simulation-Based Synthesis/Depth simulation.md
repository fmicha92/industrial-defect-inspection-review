---
title: "Depth simulation"
aliases:
  - "Depth simulation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Procedural and Simulation-Based Synthesis"
source_papers:
  - "[[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]]"
evidence_count: 1
tags:
  - method
---

# Depth simulation

## Definition

Depth simulation is a procedural synthetic data method for generating industrial-like depth maps. In [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]], a Perlin noise map is normalized, scaled by a sampled `alpha`, and translated by a sampled `beta` to model local depth variation and average object-distance changes.

## Why It Matters

It supplies large synthetic depth supervision when real industrial RGB+3D anomaly datasets are too small to train depth-specific representations directly.

## Used In These Papers

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] uses Perlin-plus-affine simulated depth maps to pretrain DADA; removing Perlin drops MVTec3D RGB+3D image AUROC from 97.8 to 90.0, and removing affine scaling/translation drops it to 94.8.

## Related Concepts

- [[Simulation-based data augmentation]]
- [[MVTec3D]]
- [[3DSR]]
- [[Eyecandies]]
