---
title: "YOLO-DSC"
aliases:
  - "YOLO with distribution shifting convolution"
tags:
  - model
---
# YOLO-DSC

## Definition

YOLO-DSC is a YOLOv8n-derived steel surface defect detector that uses distribution shifting convolution in the feature-fusion network to reduce parameter count and computation.

## Why It Matters

It targets real-time steel surface defect detection on constrained hardware while preserving detection accuracy after diffusion-based data augmentation.

## Used In These Papers

- [[2024 - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation]] reports YOLO-DSC at 0.809 mAP@0.5 on [[NEU-DET]] with fewer parameters and lower GFlops than YOLOv8n.

## Related Concepts

- [[YOLOv8]]
- [[mAP@0.50]]
- [[NEU-DET]]
