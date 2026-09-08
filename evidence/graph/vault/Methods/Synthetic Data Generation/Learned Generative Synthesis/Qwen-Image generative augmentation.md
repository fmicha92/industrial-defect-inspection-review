---
title: "Qwen-Image generative augmentation"
aliases:
  - "Qwen-Image-2.0-pro augmentation"
  - "LVLM-based generative data augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
evidence_count: 1
---
# Qwen-Image Generative Augmentation

## Definition

Qwen-Image generative augmentation uses Qwen-Image-2.0-pro to create domain-aligned object-detection training images and corresponding bounding boxes from few-shot support images and prompts.

## Why It Matters

In GiPL, generated images expand scarce RUOD and CarDD support sets while preserving target-domain style, background, and object characteristics.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses Qwen-Image-2.0-pro to synthesize semantically consistent multi-object images for RUOD and CarDD, improving mAP@0.50 in all listed 1/5/10-shot augmentation ablations.

## Related Concepts

- [[Learned generative synthesis]]
- [[Data augmentation]]
- [[Cross-domain few-shot object detection]]
- [[Object detection]]
- [[GroundingDINO]]
