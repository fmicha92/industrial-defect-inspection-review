---
title: "ALADA"
aliases:
  - "A Lite Automatic Data Augmentation"
  - "Lite automatic data augmentation"
tags:
  - method
  - data-augmentation
source_papers:
  - "[[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]]"
---
# ALADA

## Definition

ALADA is a lite automatic data augmentation framework for industrial defect detection. It uses a compact search space of 25 candidate augmentation operations and 5 magnitude levels, then jointly optimizes augmentation policy weights and detector parameters through a three-step bi-level optimization scheme.

## Why It Matters

ALADA avoids a separate retraining stage for searched policies and uses policy gradient sampling to handle non-differentiable augmentation operations. In the source paper, it improves mAP across Tianchi-TILE, GC10-DET, and NEU-DET with FRCNN and RetinaNet detectors.

## Used In These Papers

- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] - introduces ALADA and reports best mAP among compared augmentation methods on Tianchi-TILE, GC10-DET, and NEU-DET for both FRCNN and RetinaNet.

## Related Concepts

- [[Automatic data augmentation]]
- [[Policy gradient sampling]]
- [[Data augmentation]]
- [[Object detection]]
- [[Surface defect detection]]
