---
title: "TFLA-Net"
aliases:
  - "TLFA-Net"
  - "Three-Layer Feature Aggregation Network"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
evidence_count: 1
---
# TFLA-Net

## Definition

TFLA-Net is the three-layer feature aggregation network used in [[IDD-Net]]. The paper also spells the acronym as TLFA-Net in several places; both refer to the feature aggregation neck that transfers adjacent multi-scale features into the detector.

## Why It Matters

The module is designed to preserve useful detail while aggregating hierarchical backbone features for small industrial defect detection.

## Used In These Papers

- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates TFLA-Net against YOLOv5s PANet, Bi-FPN, and NAS-FPN variants on the PCB surface defect dataset.

## Related Concepts

- [[IDD-Net]]
- [[Multi-scale feature fusion]]
- [[YOLOv5]]
- [[Object detection]]
