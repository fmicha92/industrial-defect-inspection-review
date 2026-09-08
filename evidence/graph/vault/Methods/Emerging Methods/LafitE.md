---
title: "LafitE"
aliases:
  - "Latent Diffusion Model with Feature Editing"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Generative Models/Diffusion models"
source_papers:
  - "[[2023 - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---
# LafitE

## Definition

LafitE is a latent feature-space diffusion method for unsupervised multi-class anomaly detection. It reconstructs pretrained patch features with a diffusion model and uses memory-bank feature editing to replace query patches with weighted normal-neighbor features before denoising.

## Why It Matters

The method improves normal-only anomaly detection and localization on [[MPDD]] and MVTec AD, especially under non-homogeneous metal-part backgrounds.

## Used In These Papers

- [[2023 - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection]] uses LafitE for unsupervised anomaly detection and localization on [[MPDD]] and MVTec AD.

## Related Concepts

- [[Diffusion models]]
- [[Industrial anomaly detection]]
- [[MPDD]]
