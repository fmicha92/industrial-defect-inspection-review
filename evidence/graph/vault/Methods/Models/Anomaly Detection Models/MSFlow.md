---
title: "MSFlow"
aliases:
  - "MSFlow"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---

# MSFlow

## Definition

MSFlow is a multiscale normalizing-flow framework with low-level feature pyramids, asymmetrical parallel flows, and a fusion flow for unsupervised anomaly detection and localization.

## Why It Matters

MSFlow targets anomaly size variation in normal-only inspection. On [[MVTec AD]], [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] reports 99.7% image-wise AUROC, 98.8% pixel-wise AUROC, and 97.1% PRO.

## Used In These Papers

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] introduces MSFlow with asymmetrical parallel flows, fusion flow, addition/multiplication aggregation, and mean top-3% image anomaly scoring.

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Unsupervised anomaly localization]]
- [[MVTec AD]]
- [[Magnetic Tile Defects]]
- [[AU-ROC]]
- [[AU-PRO]]

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.
