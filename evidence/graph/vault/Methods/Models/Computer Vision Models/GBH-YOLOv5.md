---
title: "GBH-YOLOv5"
aliases:
  - "Ghost convolution with BottleneckCSP and tiny target prediction head YOLOv5"
tags:
  - method
  - model
  - object-detection
model_family:
  - "[[YOLOv5]]"
related_methods:
  - "[[YOLOv5]]"
  - "[[Ghost module]]"
related_tasks:
  - "[[PV panel fault detection]]"
related_datasets:
  - "[[PV-Multi-Defect]]"
source_papers:
  - "[[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]]"
---
# GBH-YOLOv5

## Definition

GBH-YOLOv5 is a YOLOv5s-based photovoltaic panel defect detector that combines BottleneckCSP, an added tiny-target prediction head, and Ghost convolution.

## Why It Matters

The model targets small and visually similar surface defects on PV panels. In the introducing paper, BottleneckCSP improves multiscale feature extraction, the extra prediction head improves tiny target detection, and Ghost convolution reduces layers, parameters, and average per-image elapsed time relative to the same model without Ghost convolution.

## Used In These Papers

- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] reports 97.8% mAP, 96.4% precision, and 93.3% recall on [[PV-Multi-Defect]].

## Architecture Notes

- Base model: [[YOLOv5]]s.
- Replaces the C3 residual module with BottleneckCSP.
- Adds a fourth prediction head for tiny target detection.
- Uses [[Ghost module|Ghost convolution]] instead of conventional convolution.
- Uses FPN and PAN structures for feature classification.
- Uses CIoU loss for bounding boxes and NMS for multiple or fuzzy targets.

## Related Concepts

- [[YOLOv5]]
- [[Ghost module]]
- [[Object detection]]
- [[PV panel fault detection]]
- [[mAP]]
