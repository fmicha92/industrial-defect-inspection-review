---
title: "RGB Channel Fusion"
aliases:
  - "RGB channel fusion"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]]"
evidence_count: 1
tags:
  - method
  - emerging
---

# RGB Channel Fusion

## Definition

RGB Channel Fusion is a data-level fusion method that converts paired forward-lighting and backward-lighting images to grayscale, assigns them to red and green channels, and uses their mean grayscale image as the blue channel.

## Why It Matters

The aircraft canopy paper uses RGB Channel Fusion as a simple dual-modal baseline. It raises mAP50 from 92.8% for forward-only YOLOv8m and 79.0% for backward-only YOLOv8m to 97.9% on the composite dataset.

## Used In These Papers

- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] evaluates RGB Channel Fusion on ag_composite_obb with YOLOv8m as the detector backend.

## Related Concepts

- [[Dual-modal illumination for transparent material inspection]]
- [[ADMF-Net]]
- [[Aircraft glass canopy defect detection]]
