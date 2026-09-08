---
title: "Global Context Upsampling"
aliases:
  - "GCU"
  - "GCU module"
tags:
  - method
related_methods:
  - "[[FDSNet]]"
  - "[[Multi-scale feature fusion]]"
source_papers:
  - "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
---
# Global Context Upsampling

## Definition

Global Context Upsampling is the FDSNet upsampling module proposed in [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]. It gradually upsamples high-level features, fuses 1/8 and 1/16 encoder features through skip connections, and inserts global-context blocks to capture long-range dependency from multi-scale features.

## Why It Matters

Surface defects can have locally similar appearances across classes and incomplete predicted regions. The paper reports that GCU improves MSD test-set mIoU from 89.08 to 89.95 in ablation, and visual examples show more continuous oil and scratch predictions than the Fast-SCNN baseline.

## Used In These Papers

- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] uses Global Context Upsampling inside [[FDSNet]] for real-time surface-defect segmentation.

## Related Concepts

- [[FDSNet]]
- [[Multi-scale feature fusion]]
- [[Defect segmentation]]
- [[Surface defect detection]]
