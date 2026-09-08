---
title: "YOLOv6-L6"
aliases:
  - "YOLOv6-L6"
  - "YOLOv6"
tags:
  - method
---
# YOLOv6-L6

## Definition

YOLOv6-L6 is an object-detection model used as a validation baseline in [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]].

## Why It Matters

The PCB dataset paper uses YOLOv6-L6 to validate [[DsPCBSD+]] in a one-stage detector setting and to compare detector performance against Co-DETR on the same PCB surface-defect labels.

## Used In These Papers

- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] trains YOLOv6-L6 on [[DsPCBSD+]] and reports AP50 0.851, AP75 0.525, and AP50:95 0.514.

## Related Concepts

- [[Object detection]]
- [[PCB defect detection]]
- [[Deep convolutional neural network]]
- [[DsPCBSD+]]
