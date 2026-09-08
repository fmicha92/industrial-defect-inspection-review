---
title: "YOLO-ACF"
aliases:
  - "YOLO adaptive complementary fusion"
  - "Adaptive Complementary Fusion YOLO"
tags: [method, model, object-detection, photovoltaic-inspection]
---

# YOLO-ACF

## Definition

YOLO-ACF is the photovoltaic-panel defect detector proposed in [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]]. It modifies YOLOv5s v6.0 with an Adaptive Complementary Fusion module that sequentially refines spatial and channel embeddings.

## Why It Matters

YOLO-ACF is designed to improve photovoltaic-panel defect detection while reducing detector size and inference time. On the selected [[PVEL-AD]] subset, the paper reports 92.6% mAP50, 62.1% mAP50-95, 6.1M parameters, 12.7 MB weights, 6.8 ms per image, and 147 FPS.

## Used In These Papers

- [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] proposes YOLO-ACF for photovoltaic panel defect detection and compares it with Faster R-CNN, RetinaNet, YOLOv3, YOLOv5, YOLOv6, and YOLOv8.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Surface defect detection]]
- [[mAP]]
- [[FPS]]
- [[YOLOv5]]
