---
title: "Procedural and simulation-based synthesis"
aliases:
  - "Rule-based synthetic data"
  - "Simulation-based synthetic data"
tags:
  - method
---

# Procedural and Simulation-Based Synthesis

## Definition

Procedural and simulation-based synthesis creates synthetic data from explicit rules, parameterized generators, rendering pipelines, physics models, or controlled simulators.

## Typical Use

Useful when the generation process should be controllable, interpretable, physically constrained, or able to produce labels automatically.

## Used In These Papers

- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] procedurally generates context-aware road scenes and labels for vehicle detection.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] uses physics simulation, ray tracing, and domain randomization before applying GAN refinement.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] uses [[PatchAnomaly]] to create local patch-level pseudo defects and surrogate labels from normal MVTec AD and BTAD images.
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] introduces [[Affine anomaly insertion]] as a source-based/source-free pseudo-anomaly insertion family for segmentation training.
- [[2025 - Simulation of semiconductor wafer dicing induced faults on chips]] introduces [[Spline-based wafer dicing fault synthesis]] for generating labeled semiconductor wafer/chip imagery and composite training data.

## Related Concepts

- [[Synthetic data generation]]
- [[Hybrid generative-procedural synthesis]]
- [[Structured domain randomization]]
- [[Rule-based data synthesis]]
- [[Defect synthesis]]
- [[Procedural generation]]
- [[Physically based rendering]]
- [[Domain randomization]]
- [[Spline-based wafer dicing fault synthesis]]
