---
title: "YOLOv8"
aliases:
  - "YOLO v8"
tags:
  - concept
  - architecture
---
# YOLOv8

## Definition

YOLOv8 is a real-time object detection architecture family used as a baseline or foundation for industrial defect detection models.

## Why It Matters

The DY-YOLO paper uses YOLOv8 as the base detector because it balances accuracy, inference speed, training stability, and deployment maturity for smartphone cover-glass defect detection.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] builds [[YOLO-AL]] on YOLOv8n for aluminum profile surface defect detection on [[APDDD]].
- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] builds [[DY-YOLO]] on YOLOv8 for smartphone screen surface defect detection.
- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] uses YOLOv8m as a single-modal baseline and uses YOLOv8-style backbones in [[ADMF-Net]].
- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] reports YOLOv8-l as the best MSDD detector at 0.854 mAP50, while YOLOv8-m is described as nearly as accurate and faster.

## Related Concepts

- [[Object detection]]
- [[Computer Vision Models]]
- [[YOLO-AL]]
- [[DY-YOLO]]
- [[ADMF-Net]]
