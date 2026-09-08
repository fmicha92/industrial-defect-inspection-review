---
title: "FastFlow"
aliases:
  - "FastFlow"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]]"
evidence_count: 1
tags:
  - method
---

# FastFlow

## Definition

FastFlow is a 2D normalizing-flow module that estimates normal feature likelihoods from frozen CNN or vision-transformer feature maps for unsupervised anomaly detection and localization. It keeps feature maps in two-dimensional form instead of flattening them, then uses low likelihood as the anomaly signal.

## Why It Matters

It is designed to avoid sliding-window patch inference while preserving spatial relationships needed for pixel-level localization. On MVTec AD, the source paper reports 99.4 image-level AUROC and 98.5 pixel-level AUROC with faster inference than PatchCore and CFlow under the tested backbones.

## Used In These Papers

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] uses FastFlow as a central method or method component.

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Unsupervised anomaly localization]]
- [[MVTec AD]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.
