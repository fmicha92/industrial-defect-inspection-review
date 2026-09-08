---
title: "Mask R-CNN"
aliases:
  - "Mask RCNN"
tags:
  - method
  - model
  - segmentation
  - object-detection
source_papers:
  - "[[2021 - Industrial Machine Tool Component Surface Defect Dataset]]"
related_methods:
  - "[[Faster R-CNN]]"
related_tasks:
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
---

# Mask R-CNN

## Definition

Mask R-CNN is a two-stage instance-segmentation model that extends region-based object detection with a pixel-level mask prediction branch.

## Why It Matters

In [[2021 - Industrial Machine Tool Component Surface Defect Dataset]], Mask R-CNN provides the baseline model for detecting and segmenting pitting on [[BSData]].

## Used In These Papers

- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] uses Mask R-CNN with a COCO-pretrained Inception-ResNet-v2 backbone and reports mIoU 0.316 on [[BSData]].

## Related Concepts

- [[Faster R-CNN]]
- [[Object detection]]
- [[Defect segmentation]]
- [[mIoU]]
- [[BSData]]
