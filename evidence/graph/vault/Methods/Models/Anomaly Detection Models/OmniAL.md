---
title: "OmniAL"
aliases:
  - "OmniAL"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]]"
evidence_count: 1
tags:
  - method
---

# OmniAL

## Definition

OmniAL is a unified CNN framework for unsupervised anomaly localization with one model across multiple classes. It trains on panel-guided synthetic anomalies, reconstructs anomaly-free images with DCSA-equipped encoder-decoder blocks, and localizes defects by comparing the input with reconstructed normal and JND maps through DiffNeck.

## Why It Matters

OmniAL directly addresses the performance drop that reconstruction/localization methods can suffer when moving from one model per class to a single model for many industrial categories. On MVTec AD, the unified model reports 97.2 image AUROC, 98.3 pixel AUROC, and 73.4 pixel AP.

## Used In These Papers

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] introduces OmniAL for unified unsupervised anomaly localization on [[MVTec AD]] and [[VisA]].

## Related Concepts

- [[Unsupervised anomaly localization]]
- [[Defect synthesis]]
- [[MVTec AD]]
- [[VisA]]
- [[AU-ROC]]
- [[Average precision]]
- [[SSIM]]
- [[Adam]]
