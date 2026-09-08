---
title: "Natural Synthetic Anomalies"
aliases:
  - "Natural Synthetic Anomalies"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]]"
evidence_count: 1
tags:
  - emerging-method
---
# Natural Synthetic Anomalies

## Definition

Natural Synthetic Anomalies is a self-supervised synthetic anomaly task that blends resized patches from normal images with Poisson image editing, then trains an end-to-end model to localize the generated anomaly mask.

## Why It Matters

NSA supports normal-only anomaly detection and localization without ImageNet pretraining or external texture datasets, and it reports strong MVTec AD image-level and pixel-level AUROC.

## Used In These Papers


- [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] uses [[Natural Synthetic Anomalies]] for self-supervised anomaly detection, synthetic anomalies.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[MVTec AD]]
- [[rCXR]]
- [[AU-ROC]]
