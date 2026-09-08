---
title: "Smartphone screen glass defect detection"
aliases:
  - "Touch screen glass defect detection"
  - "Screen glass defect detection"
related_domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
related_datasets:
  - "[[SSGD]]"
  - "[[MSD]]"
  - "[[Mobile Phone Flat Glass Defect Dataset]]"
related_benchmarks:
  - "[[SSGD benchmark]]"
tags:
  - task
  - glass-inspection
---

# Smartphone Screen Glass Defect Detection

## Definition

Smartphone screen glass defect detection localizes defects on touch-screen glass panels during manufacturing quality inspection. In [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]], the task uses bounding boxes for crack, broken, spot, scratch, light-leakage, blot, and broken-membrane defects.

## Why It Matters

Screen glass quality affects smartphone display performance, service life, and user acceptance. Automated detection can reduce manual inspection labor and judgment errors, but high-resolution images and small or elongated defects make the task challenging.

## Used In These Papers

- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] introduces [[MSD]] for pixel-level segmentation of oil, stain, and scratch defects on mobile phone screens.
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] introduces [[SSGD]] and benchmarks CNN and Transformer object detectors.
- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] proposes [[DY-YOLO]] for real-time smartphone cover-glass defect detection on [[MSD]] and [[SSGD]].
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] proposes [[YOLOv5_zc]] for bright spot, scratch, dust, and stain detection on mobile phone flat glass.
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] proposes [[CE-SGNet]] for small, low-contrast smartphone screen defects on [[SSGD]].

## Related Concepts

- [[SSGD]]
- [[SSGD benchmark]]
- [[Glass inspection]]
- [[Semiconductor and electronics]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
- [[Average precision]]
- [[DY-YOLO]]
- [[MSD]]
- [[YOLOv5_zc]]
- [[Mobile Phone Flat Glass Defect Dataset]]
- [[CE-SGNet]]
