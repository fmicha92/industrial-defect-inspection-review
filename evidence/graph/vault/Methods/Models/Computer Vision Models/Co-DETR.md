---
title: "Co-DETR"
aliases:
  - "Collaborative Hybrid Assignments Training for DETR"
  - "Co-DETR"
tags:
  - method
---
# Co-DETR

## Definition

Co-DETR is an object-detection model used as a validation baseline in [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]].

## Why It Matters

The PCB dataset paper uses Co-DETR to show that [[DsPCBSD+]] can train a high-performing detector and to quantify detection performance across small, medium, and large PCB surface defects.

## Used In These Papers

- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] trains Co-DETR on [[DsPCBSD+]] and reports AP50 0.848, AP75 0.490, and AP50:95 0.492.

## Related Concepts

- [[Object detection]]
- [[PCB defect detection]]
- [[Deep convolutional neural network]]
- [[DsPCBSD+]]
