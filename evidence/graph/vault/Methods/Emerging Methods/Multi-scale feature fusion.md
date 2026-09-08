---
title: "Multi-scale feature fusion"
aliases:
  - "M-SFF"
  - "multi-scale feature-fusion module"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
evidence_count: 2
---
# Multi-Scale Feature Fusion

## Definition

Multi-scale feature fusion combines feature maps from different network depths so a detector can use both spatial location information from shallow layers and semantic information from deeper layers.

## Why It Matters

Small and varied industrial defects can require both localization detail and semantic context. In the automotive-glass YOLOv5 paper, M-SFF improved mAP and recall with little additional computation.

## Used In These Papers

- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] adds M-SFF with coordinate attention to the MobileNetV3/Ghost YOLOv5s variant.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] adds an MSF module before the detector heads to combine feature channel attention and learnable weighted feature fusion for multi-scale industrial defects.

## Related Concepts

- [[YOLOv5]]
- [[Ghost module]]
- [[IDD-Net]]
