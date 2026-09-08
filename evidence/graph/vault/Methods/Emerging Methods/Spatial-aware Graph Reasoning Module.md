---
title: "Spatial-aware Graph Reasoning Module"
aliases:
  - "SGRM"
  - "Spatial-aware Graph Attention Network"
  - "SGAT"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]]"
evidence_count: 1
tags:
  - method
  - emerging
---

# Spatial-Aware Graph Reasoning Module

## Definition

Spatial-aware Graph Reasoning Module builds a region-to-region graph from region proposals and updates node features with spatial-aware graph attention. It encodes spatial relationships between proposed defect regions before final classification and localization.

## Why It Matters

The CE-SGNet paper argues that independent region proposals contain limited information for small or incomplete defects. SGRM propagates contextual and spatial information among regions and improves localization by strengthening related defect-region features.

## Used In These Papers

- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] combines SGRM with ARFAM in [[CE-SGNet]], improving SSGD-LB101 AP from 20.3 to 24.0 over the Faster R-CNN baseline.

## Related Concepts

- [[CE-SGNet]]
- [[Object detection]]
- [[Smartphone screen glass defect detection]]
- [[Average precision]]
