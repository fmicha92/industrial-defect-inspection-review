---
title: "GT-CutMix"
aliases:
  - "Ground-truth CutMix"
  - "GT CutMix"
tags:
  - method
---
# GT-CutMix

## Definition

GT-CutMix is a defect-detection data augmentation method that samples annotated defect regions and inserts them into same-class steel surface images while preserving bounding-box labels.

## Why It Matters

It targets class imbalance and sparse defect appearances in strip-steel object detection by increasing labeled defect instances without treating background patches as defects.

## Used In These Papers

- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]] applies GT-CutMix to X-SDD and reports higher mAP for several detector baselines.

## Related Concepts

- [[Data augmentation]]
- [[Metallic surface defect detection]]
- [[mAP]]
