---
title: "Domain randomization"
tags:
  - concept
  - method
---

# Domain randomization

## Definition

Domain randomization varies synthetic scene parameters so a model sees many possible appearances during training. In the paper notes, randomized parameters include defect position, orientation, size, shape, illumination, camera pose, texture roughness, base color, and normal maps.

## Why It Matters

The goal is to narrow the synthetic-to-real domain gap by forcing the model to learn robust features rather than overfit one rendered appearance. It is especially relevant when the final deployment data are scarce or variable.

## Used In These Papers

- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses domain randomization across defects, illumination, camera, and texture for turbocharger housing inspection.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] randomizes lights, object and floor colors/textures, and camera position for industrial electric parts.
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] extends domain randomization with context-aware object placement and scene structure.

## Related Concepts

- [[Synthetic data generation]]
- [[Hybrid generative-procedural synthesis]]
- [[Structured domain randomization]]
- [[Domain gap]]
- [[Physically based rendering]]
- [[Procedural generation]]
