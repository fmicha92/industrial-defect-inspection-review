---
title: "RD4AD"
aliases:
  - "Reverse Distillation from One-Class Embedding for Anomaly Detection"
  - "Reverse Distillation for Anomaly Detection"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]"
evidence_count: 1
tags:
  - method
  - anomaly-detection
---

# RD4AD

## Definition

RD4AD is an unsupervised anomaly detection method using a pre-trained teacher encoder, a trainable one-class bottleneck embedding module, and a student decoder. The Lusitano paper describes it as using reverse distillation and multi-scale similarity maps to detect anomalies from low similarity between encoder and decoder feature vectors.

## Why It Matters

The method is suitable for one-class industrial inspection because it can train on normal samples and detect deviations at inference time without requiring labeled examples for every possible defect type.

## Used In These Papers

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] evaluates RD4AD on [[Lusitano]] and reports it outperforming [[DBFAD]] on AU-ROC/AUC and mAP.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] builds on reverse-distillation-style teacher-student anomaly detection and adds synthetic-anomaly contrastive training.

## Related Concepts

- [[Anomaly Detection Models]]
- [[Unsupervised anomaly detection]]
- [[Industrial anomaly detection]]
- [[Lusitano benchmark]]
- [[AU-ROC]]
- [[mAP]]
