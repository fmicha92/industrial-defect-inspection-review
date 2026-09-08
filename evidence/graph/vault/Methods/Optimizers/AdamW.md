---
title: "AdamW"
aliases:
  - "AdamW optimizer"
tags:
  - optimizer
---

# AdamW

## Definition

AdamW is an Adam-family optimizer that decouples weight decay from the adaptive gradient update.

## Why It Matters

It is commonly used for training deep neural network modules, especially transformer-based models and feature-fusion layers.

## Used In These Papers

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] uses AdamW to train the Unsupervised Feature Fusion module with learning rate 0.003, cosine warm-up over 250 steps, batch size 256, and best results under 750 training steps.

## Related Concepts

- [[Adam]]
- [[Vision Transformer]]
- [[Unsupervised anomaly detection]]
