---
title: "Procedural generation"
aliases:
  - "Procedural synthetic data generation"
tags:
  - concept
  - method
---

# Procedural generation

## Definition

Procedural generation creates data through parameterized rules rather than manual collection alone. In these notes, it is used for generating defect geometry, textures, render settings, and synthetic inspection images.

## Why It Matters

Procedural generation can scale synthetic datasets and automatically produce labels, but the generated parameter ranges need to reflect meaningful inspection variation. Otherwise the generated data may look diverse without improving real-world inspection.

## Used In These Papers

- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] is the central local example, using 3D defect tools, procedural textures, PBR, and domain randomization.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] notes that extending simulated CT generation to other manufacturing processes requires new procedural mesh generation and defect types.

## Related Concepts

- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[Domain randomization]]
- [[Physically based rendering]]
