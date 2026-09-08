---
title: "GiPL"
aliases:
  - "Generative augmented iterative Pseudo-Labeling"
  - "GiPL-Grounding"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
evidence_count: 1
---
# GiPL

## Definition

GiPL is a two-branch cross-domain few-shot object detection framework that selects between iterative pseudo-label self-training and Qwen-based generative data augmentation depending on the target dataset.

## Why It Matters

The method separates two common few-shot detector failures: sparse support annotations in dense scenes and overfitting from low-resource target-domain samples.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] introduces GiPL and reports improvements on RUOD, CARPK, and CarDD under 1/5/10-shot settings.

## Related Concepts

- [[Cross-domain few-shot object detection]]
- [[Pseudo-labeling]]
- [[Qwen-Image generative augmentation]]
- [[Data augmentation]]
- [[GLIP]]
- [[GroundingDINO]]
