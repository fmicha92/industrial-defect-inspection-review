---
title: "YOLO-AL"
aliases:
  - "You Only Look Once-Aluminum"
tags:
  - concept
  - architecture
source_papers:
  - "[[2025 - You Only Look Once-Aluminum]]"
---
# YOLO-AL

## Definition

YOLO-AL is a YOLOv8n-based object detector for aluminum surface defects. It combines C2f-US backbone changes, CPMSCA attention, an ODE-RepGFPN neck, and Focaler-WIoU loss.

## Why It Matters

The model is designed for [[Metallic surface defect detection]] where aluminum defects can be small, low-resolution, strip-like, and imbalanced across classes.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] introduces YOLO-AL and evaluates it on [[APDDD]].

## Related Concepts

- [[YOLOv8]]
- [[Object detection]]
- [[APDDD]]
- [[Metal inspection]]
- [[mAP@0.50]]
- [[FPS]]
