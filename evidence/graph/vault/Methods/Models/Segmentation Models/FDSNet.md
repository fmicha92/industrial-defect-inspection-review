---
title: "FDSNet"
aliases:
  - "Fast surface Defect Segmentation Network"
  - "FDSNet"
tags:
  - model
  - segmentation
related_methods:
  - "[[Global Context Upsampling]]"
  - "[[MobileNet]]"
related_tasks:
  - "[[Defect segmentation]]"
source_papers:
  - "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
---
# FDSNet

## Definition

FDSNet is a real-time surface-defect semantic segmentation network proposed in [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]. It uses a Fast-SCNN-style encoder-decoder architecture, MobileNetV3 blocks, [[Global Context Upsampling]], and training-only boundary detection and multi-label classification auxiliary tasks.

## Why It Matters

The model targets industrial inspection settings where pixel-level defect masks and high throughput are both required. On [[MSD]], the paper reports 90.2% [[mIoU]] at 135.0 [[FPS]] on one NVIDIA GTX 1080Ti, and 88.7% mIoU at 275.9 FPS with TensorRT.

## Used In These Papers

- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] proposes FDSNet and evaluates it on [[MSD]], [[Magnetic Tile Defects]], and [[NEU-SEG]].

## Related Concepts

- [[Global Context Upsampling]]
- [[Defect segmentation]]
- [[Segmentation Models]]
- [[MobileNet]]
- [[mIoU]]
- [[FPS]]
