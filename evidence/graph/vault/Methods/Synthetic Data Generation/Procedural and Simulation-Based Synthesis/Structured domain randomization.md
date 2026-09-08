---
title: "Structured domain randomization"
aliases:
  - "SDR"
tags:
  - method
---

# Structured domain randomization

## Definition

Structured domain randomization is a context-aware variant of [[Domain randomization]] that places objects according to scene structure rather than uniformly at random.

## Why It Matters

For object detection, context can matter when targets are small, occluded, or truncated. Structured domain randomization preserves procedural variability while making object placement consistent with the scene.

## Used In These Papers

- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] introduces SDR for synthetic vehicle detection data and reports stronger KITTI detection performance than ordinary domain randomization and other synthetic datasets.

## Related Concepts

- [[Procedural and simulation-based synthesis]]
- [[Domain randomization]]
- [[Synthetic data generation]]
- [[Domain gap]]
- [[Rule-based data synthesis]]
