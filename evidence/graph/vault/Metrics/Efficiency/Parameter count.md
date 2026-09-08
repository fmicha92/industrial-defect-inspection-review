---
title: "Parameter count"
aliases:
  - "parameters"
  - "model parameters"
  - "Param"
tags:
  - metric
  - efficiency
concept_type: metric
---
# Parameter Count

## Definition

Parameter count measures the number of model parameters. It is used as an efficiency and deployability metric for neural inspection models.

## Direction

Lower is usually better when model compactness is the comparison target, but the interpretation depends on accuracy and deployment constraints.

## Used In These Papers

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports LMFF with 1.18M parameters.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] reports [[WM-PeleeNet]] with 0.169M parameters in Table 7 and 173.643 KB of parameters in the abstract.

## Related Metrics

- [[GFLOPs]]
- [[Inference time]]
- [[FPS]]
- [[Efficiency metrics]]
