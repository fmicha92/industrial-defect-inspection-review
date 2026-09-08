---
title: "CAGen"
aliases:
  - "CAGen"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - CAGEN Controllable Anomaly Generator Using Diffusion Model]]"
evidence_count: 1
tags:
  - emerging-method
---
# CAGen

## Definition

CAGen is a two-stage controllable anomaly generator for industrial anomaly detection. It fine-tunes Stable Diffusion v1.5 with [[ControlNet]] so a binary mask controls anomaly location and a text prompt controls anomaly style, then fuses generated anomalous features with normal-image features before decoding the final anomalous image.

## Why It Matters

It creates synthetic anomalous images with both spatial labels and prompt-controlled anomaly styles, which lets anomaly localization models train with more realistic generated defects than simple cut-and-paste augmentation.

## Used In These Papers


- [[2024 - CAGEN Controllable Anomaly Generator Using Diffusion Model]] introduces CAGen and reports mean MVTec AD localization AUROC/AP improving from DRAEM's 97.3/68.4 to 97.7/71.5.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Diffusion models]]
- [[ControlNet]]
