---
title: "LMFF"
aliases:
  - "Lightweight Multiscale Feature Fusion Network"
  - "Lightweight Multi-scale Feature Fusion Network"
tags:
  - method
  - model
concept_type: method
candidate_parent: "Methods/Models/Segmentation Models"
source_papers:
  - "[[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]]"
evidence_count: 1
---
# LMFF

## Definition

LMFF is a lightweight segmentation network for solar-cell defect localization in electroluminescence images. It combines depthwise separable residual blocks, multi-scale feature fusion, and multi-scale attention to segment small and irregular defect regions.

## Why It Matters

The source paper reports that LMFF improves [[IoU]], [[mIoU]], and [[F1-score]] over FCN, Deeplab-v3, [[U-Net]], and U2-Net on SolarCells, SolarCells-S, and PVEL-S while keeping low [[GFLOPs]] and [[Parameter count]].

## Used In These Papers

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] introduces LMFF for solar-cell defect segmentation.

## Related Concepts

- [[Segmentation Models]]
- [[Depthwise separable convolution]]
- [[Solar cell defect detection]]
- [[Defect segmentation]]
- [[Dataset of Solar Cells Defect Segmentation]]
