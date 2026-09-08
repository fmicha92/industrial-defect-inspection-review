---
title: "Global Context Anomaly Detection"
aliases:
  - "GCAD"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
evidence_count: 1
---
# Global Context Anomaly Detection

## Definition

Global Context Anomaly Detection is a two-branch unsupervised anomaly localization method. A local branch detects novel local structures through feature-regression errors, while a global bottleneck branch detects violations of long-range logical constraints through discrepancies between globally consistent encodings and high-capacity regression outputs.

## Why It Matters

The method is designed for benchmarks that include both [[Structural anomalies]] and [[Logical anomalies]]. On [[MVTec LOCO AD]], the source paper reports the best mean localization score among the evaluated baselines, with balanced structural and logical anomaly performance.

## Used In These Papers

- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] proposes GCAD and reports mean sPRO AUC 0.701 on [[MVTec LOCO AD]], compared with 0.626 for Student-Teacher and 0.451 for SPADE.

## Related Concepts

- [[Unsupervised anomaly localization]]
- [[Unsupervised anomaly detection]]
- [[Logical anomalies]]
- [[Structural anomalies]]
- [[Area Under Saturated Per-Region Overlap]]
