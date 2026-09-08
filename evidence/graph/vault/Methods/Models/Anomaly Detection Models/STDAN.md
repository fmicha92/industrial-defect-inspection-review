---
title: "STDAN"
aliases:
  - "Self-Supervised Texture-Decomposition and Defect Amplification Network"
  - "Texture Conditioned GAN Based Self Supervised Framework"
tags:
  - model
  - anomaly-detection
---

# STDAN

## Definition

STDAN is a self-supervised fabric anomaly-detection framework introduced in [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]]. It decomposes encoded fabric features into normal texture bases and residual anomaly cues, then amplifies residual features in latent space to train a contrastive anomaly-aware representation.

## Why It Matters

The method targets fabric inspection settings where defect labels are scarce, pixel-level annotations are expensive, and normal texture variation can be mistaken for defects. Its feature-level amplification is designed to avoid unrealistic pixel-level synthetic defects while increasing sensitivity to weak anomalies.

## Used In These Papers

- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] proposes STDAN and evaluates it on [[FabricSpotDefect]], [[FD_Dataset]], and [[Lusitano]].

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Self-supervised learning]]
- [[GAN]]
- [[Anomaly Detection Models]]
- [[Textile defect detection]]
- [[Defect segmentation]]
