---
title: "LIME surrogate fidelity"
aliases:
  - "kernel-weighted surrogate fidelity"
  - "R2w"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# LIME Surrogate Fidelity

## Definition

LIME surrogate fidelity measures how well the local surrogate model approximates the black-box model response around the explained image. The source paper reports kernel-weighted `R2w` and weighted MSE.

## Direction

Higher `R2w` is better because it indicates the surrogate better matches local model behavior.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports LIME surrogate-fidelity statistics across Baseline CNN, VGG16, ResNet50, InceptionV3, and EfficientNetB0.

## Related Concepts

- [[LIME]]
- [[Shortcut learning]]
- [[Defect classification]]
