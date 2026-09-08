---
title: "Deformable convolution"
aliases:
  - "deformable convolutional unit"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]]"
evidence_count: 1
tags:
  - emerging-method
---

# Deformable Convolution

## Definition

Deformable convolution augments standard convolution with learned spatial offsets, allowing the sampling grid to shift toward informative image regions rather than staying fixed.

## Why It Matters

For mixed-type wafer-map defects, deformable sampling can focus on defect dies and suppress normal or noisy areas, helping distinguish overlapping or rotated defect patterns.

## Used In These Papers

- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] uses deformable convolution in DC-Net for mixed-type wafer defect recognition.

## Related Concepts

- [[DC-Net]]
- [[Deep convolutional neural network]]
- [[Wafer map defect classification]]
