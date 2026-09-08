---
title: "DBFAD"
aliases:
  - "Distillation-Based Fabric Anomaly Detection"
  - "Distillation-based fabric anomaly detection"
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

# DBFAD

## Definition

DBFAD is a distillation-based fabric anomaly detection method for texture defect inspection. The Lusitano paper describes it as using residue reverse distillation and a teacher-student architecture to detect fabric defects without defective samples during training.

## Why It Matters

The method directly targets fabric textures under one-class anomaly detection, where collecting all possible defect types is impractical.

## Used In These Papers

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] evaluates DBFAD on [[Lusitano]] across training subsets from 1k to 32k normal images.

## Related Concepts

- [[Anomaly Detection Models]]
- [[Unsupervised anomaly detection]]
- [[Textile defect detection]]
- [[Lusitano benchmark]]
- [[AU-ROC]]
- [[mAP]]
