---
title: "Glass container defect detection"
aliases:
  - "Glass container quality control"
  - "Transparent material inspection"
related_domains:
  - "[[Glass inspection]]"
related_datasets:
  - "[[MVEP]]"
tags:
  - task
  - glass-inspection
---
# Glass Container Defect Detection

## Definition

Glass container defect detection localizes and grades surface defects on glass containers for industrial quality control. [[MVEP]] uses multi-view images, object-level bounding boxes, and ordinal severity labels for erasure-type surface degradation defects.

## Why It Matters

Transparent materials introduce specular reflections, refractions, and view-dependent visual effects that can make single-view inspection unreliable. Multi-view inspection supports more robust defect detection and severity assessment.

## Used In These Papers

- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] classifies MVTec AD bottle images as defective or non-defective and uses DDPM-generated defective samples to reduce class imbalance.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates object detection on [[BBMP]], a glass-bottle bottom mold point production-line dataset.

## Related Concepts

- [[MVEP]]
- [[BBMP]]
- [[Glass inspection]]
- [[Defect classification]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
