---
title: "LGB-Net"
aliases:
  - "Local-Global Backbone Feature Extraction Network"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
evidence_count: 1
---
# LGB-Net

## Definition

LGB-Net is the local-global backbone in [[IDD-Net]]. It combines convolutional blocks and lightweight Transformer blocks so the detector can model local surface texture and longer-range feature context.

## Why It Matters

The IDD-Net ablations report that replacing the YOLOv5s backbone with LGB-Net improves mAP and recall on steel and aluminium surface defect data.

## Used In These Papers

- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses LGB-Net as the backbone for IDD-Net, with Conv-Block plus TransformerBlock stages and ghost convolution.

## Related Concepts

- [[IDD-Net]]
- [[Ghost module]]
- [[YOLOv5]]
- [[Object detection]]
