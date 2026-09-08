---
title: "Ghost module"
aliases:
  - "GhostConv"
  - "Ghost convolution"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
  - "[[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]]"
  - "[[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]]"
evidence_count: 3
---
# Ghost Module

## Definition

Ghost module is a lightweight convolutional module that generates some feature maps with ordinary convolution and additional feature maps through cheaper linear operations.

## Why It Matters

It reduces computation and parameter cost in object detectors while attempting to preserve feature-map information.

## Used In These Papers

- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] replaces neck convolutions with Ghost modules to reduce YOLOv5s deployment cost.
- [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]] uses Ghost modules inside [[GSLU-Net]] to reduce computation while preserving feature maps for heat-sink defect segmentation.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] uses Ghost convolution inside [[GBH-YOLOv5]] to reduce inference time and parameters for PV panel defect detection.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses ghost convolution inside [[LGB-Net]] Conv-Blocks and [[TFLA-Net]] downsampling to reduce detector computation.

## Related Concepts

- [[YOLOv5]]
- [[MobileNet]]
- [[GSLU-Net]]
- [[GBH-YOLOv5]]
- [[IDD-Net]]
- [[LGB-Net]]
- [[TFLA-Net]]
