---
title: "Simulation-based data augmentation"
aliases:
  - "Simulated training data"
tags:
  - concept
  - method
---

# Simulation-based data augmentation

## Definition

Simulation-based data augmentation generates synthetic training samples from a modeled inspection process or object rather than from purely image-space transformations. Simulation provides labels for CT volumes, adhesive bead images, and rendered industrial surface defects.

## Why It Matters

Simulation can produce labeled examples when real defects are scarce or difficult to annotate. Its main risk is fidelity: if the simulated sensor, geometry, material, or defect distribution misses key real-world factors, performance can drop on real data.

## Used In These Papers

- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] trains on realistically simulated CT scans with precise voxel labels.
- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] generates 4000 CoppeliaSim adhesive inspection images with YOLO-format bounding annotations and uses them to augment a 124-image real dataset.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] renders synthetic turbocharger housing defects with PBR and domain randomization.

## Related Concepts

- [[Synthetic data generation]]
- [[Hybrid generative-procedural synthesis]]
- [[Domain gap]]
- [[Physically based rendering]]
- [[Domain randomization]]
