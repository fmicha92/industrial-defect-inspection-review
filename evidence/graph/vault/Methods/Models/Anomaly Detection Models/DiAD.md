---
title: "DiAD"
aliases:
  - "DiAD"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---

# DiAD

## Definition

DiAD is a diffusion-based anomaly detection framework for multi-class anomaly detection. It combines pixel-space autoencoding, a Semantic-Guided latent network connected to a Stable Diffusion denoising network, Spatial-aware Feature Fusion, and feature-space anomaly maps from a pretrained extractor.

## Why It Matters

The linked paper uses this method as a central mechanism for industrial defect detection, anomaly detection, anomaly localization, or data-efficient inspection.

## Used In These Papers

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] introduces DiAD and reports 97.2 AUROC-cls, 96.8 AUROC-seg, and 90.7 PRO on multi-class MVTec AD.

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Diffusion models]]
- [[ResNet50]]
- [[MVTec AD]]
- [[VisA]]

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.
