---
title: "DY-YOLO"
aliases:
  - "Dynamic YOLO for smartphone screen surface defect detection"
tags:
  - concept
  - architecture
---
# DY-YOLO

## Definition

DY-YOLO is a YOLOv8-based object detector that adds Dynamic-C2f, Dynamic-LSKA, HSF-BPAN, and DySample to improve smartphone cover-glass defect detection under reflective backgrounds and large defect-scale variation.

## Why It Matters

The model targets real-time production-line inspection where defects range from small scratches to large broken regions and the detector must preserve speed while reducing false detections from glass reflections.

## Used In These Papers

- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] proposes DY-YOLO and evaluates it on [[MSD]] and [[SSGD]].

## Related Concepts

- [[YOLOv8]]
- [[Object detection]]
- [[Smartphone screen glass defect detection]]
- [[Glass inspection]]
- [[Surface defect detection]]
