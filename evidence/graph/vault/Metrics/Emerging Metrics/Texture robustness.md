---
title: "Texture robustness"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Anomaly Detection"
source_papers:
  - "[[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]]"
evidence_count: 1
tags:
  - emerging-metric
---

# Texture Robustness

## Definition

Texture robustness measures consistency of anomaly-detection performance across fabric texture categories. In [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]], it is computed as average AUC across texture categories such as plain, twill, jacquard, denim, and patterned fabrics.

## Direction

Higher is better.

## Used In These Papers

- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] reports 92% texture robustness for STDAN.

## Related Concepts

- [[AU-ROC]]
- [[Anomaly detection metrics]]
- [[STDAN]]
- [[Textile defect detection]]
