---
title: "PGA-Net"
aliases:
  - "Pyramid Feature Fusion and Global Context Attention Network"
tags:
  - method
  - model
status: "stable"
concept_type: "method"
source_papers:
  - "[[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]"
related_methods:
  - "[[Segmentation Models]]"
  - "[[VGG-16]]"
related_tasks:
  - "[[Defect segmentation]]"
related_datasets:
  - "[[NEU-SEG]]"
related_metrics:
  - "[[mIoU]]"
---
# PGA-Net

## Definition

PGA-Net is a CNN-based surface defect segmentation model that combines VGG-16 multilevel feature extraction, pyramid feature fusion, global context attention, boundary refinement, and deep supervision for pixel-wise defect prediction.

## Why It Matters

The model was proposed for industrial surface defect detection settings where low contrast, intraclass variation, interclass similarity, and boundary precision make direct segmentation difficult. On [[NEU-SEG]], the introducing paper reports 82.15% [[mIoU]].

## Used In These Papers

- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] introduces PGA-Net and evaluates it on [[NEU-SEG]], DAGM 2007, MT defect, and Road defect datasets.

## Related Concepts

- [[Segmentation Models]]
- [[VGG-16]]
- [[Defect segmentation]]
- [[NEU-SEG]]
- [[mIoU]]
