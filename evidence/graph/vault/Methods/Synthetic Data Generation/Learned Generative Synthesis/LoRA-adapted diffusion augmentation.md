---
title: "LoRA-adapted diffusion augmentation"
aliases:
  - "LoRA diffusion augmentation"
  - "LoRA-adapted text-to-image augmentation"
tags:
  - method
---
# LoRA-adapted Diffusion Augmentation

## Definition

LoRA-adapted diffusion augmentation fine-tunes a pretrained diffusion generator with low-rank adaptation on a small defect-image set, then uses generated images as additional training samples for downstream vision models.

## Why It Matters

It supports synthetic-data generation when defect samples are scarce and full diffusion fine-tuning would be expensive.

## Used In These Papers

- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] fine-tunes Stable Diffusion with LoRA and augments [[NEU-SEG]] segmentation training.
- [[2026 - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks]] uses LoRA-adapted FLUX.2-dev to generate rare-class examples for [[Magnetic Tile Defects]] classification.

## Related Concepts

- [[Diffusion models]]
- [[Learned generative synthesis]]
- [[Data augmentation]]
