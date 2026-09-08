---
title: "DC-Net"
aliases:
  - "Deformable convolutional network"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]]"
evidence_count: 1
tags:
  - emerging-method
---

# DC-Net

## Definition

DC-Net is a deformable convolutional network for mixed-type wafer defect pattern recognition. It uses deformable convolutional units to sample relevant defect regions and a multi-label output layer to decode mixed defects into basic wafer defect patterns.

## Why It Matters

Mixed wafer-map defects can overlap, rotate, or partially obscure one another. DC-Net targets this by learning sampling offsets and decomposing mixed labels into simpler component defects.

## Used In These Papers

- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] reports 93.2% average accuracy on [[MixedWM38]].

## Related Concepts

- [[Deformable convolution]]
- [[Wafer map defect classification]]
- [[Deep convolutional neural network]]
