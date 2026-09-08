---
title: "Patch-based anomaly detection"
aliases:
  - "Patch-based methods"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]]"
evidence_count: 1
tags:
  - method
  - emerging-taxonomy
---
# Patch-Based Anomaly Detection

## Definition

Patch-based anomaly detection breaks images into local patches and compares patch representations against normal training patches or patch-position distributions.

## Why It Matters

Patch-based methods can perform well when defects are local and visually different from nominal patches, but they can struggle with logical defects that require global spatial reasoning.

## Used In These Papers

- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] benchmarks PaDiM and Patchcore as patch-based methods; Patchcore gives the best mean AutoVI AUROC and AUsPRO, but the paper reports that local patch representations struggle with logical defects and very small defects in complex scenes.

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
