---
title: "SEODI"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Segmentation Models"
source_papers:
  - "[[2025 - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps]]"
evidence_count: 1
tags:
  - emerging-method
---
# SEODI

## Definition

SEODI is a segmentation-enhanced wafer-map defect identification framework that combines YOLO-style detection with [[U-Net]] segmentation for single, mixed, and overlapped defect patterns.

## Why It Matters

It treats overlapped wafer-map defects as a localization and segmentation problem rather than only a multi-label classification problem.

## Used In These Papers

- [[2025 - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps]] introduces SEODI and reports 89.3% overlapped type recognition accuracy and 89% mAP localization.

## Related Concepts

- [[YOLOv7]]
- [[U-Net]]
- [[Wafer map defect classification]]
- [[Defect segmentation]]
