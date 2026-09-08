---
title: "CE-SGNet"
aliases:
  - "Context-Enhanced Network with Spatial-Aware Graph"
  - "CE-SG defect detection network"
tags:
  - method
  - model
  - object-detection
model_family:
  - "[[Faster R-CNN]]"
related_methods:
  - "[[Adaptive Receptive Field Attention Module]]"
  - "[[Spatial-aware Graph Reasoning Module]]"
source_papers:
  - "[[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]]"
---

# CE-SGNet

## Definition

CE-SGNet is a two-stage defect detector for smartphone screen defect detection. It uses Faster R-CNN with FPN as the baseline, adds an Adaptive Receptive Field Attention Module after feature fusion, and applies a Spatial-aware Graph Reasoning Module to enhance region proposal features before classification and localization.

## Why It Matters

The method targets small, low-contrast, irregular smartphone screen defects. The paper reports that CE-SGNet improves AP and AP50 over the Faster R-CNN baseline on SSGD-LB101 and outperforms compared CNN, YOLO, and Transformer detectors on most SSGD metrics.

## Used In These Papers

- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] reports 24.0 AP / 51.2 AP50 on SSGD-LB101, 22.7 AP / 48.1 AP50 on SSGD-LB201, and 53.8 AP / 97.0 AP50 on the PCB generalization dataset.

## Related Concepts

- [[Smartphone screen glass defect detection]]
- [[SSGD]]
- [[DeepPCB]]
- [[Average precision]]
- [[FPS]]
