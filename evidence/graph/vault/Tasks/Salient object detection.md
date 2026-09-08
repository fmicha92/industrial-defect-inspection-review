---
title: "Salient object detection"
aliases:
  - "SOD"
tags:
  - task
---
# Salient Object Detection

## Definition

Salient object detection identifies foreground regions of interest without assigning fine-grained class labels.

## Why It Matters

For car damage assessment, salient object detection can localize irregular damage boundaries without requiring the model to distinguish visually similar classes such as dent, scratch, and crack.

## Used In These Papers

- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] evaluates CSNet, U2-Net, PoolNet, and SGL-KRN on [[CarDD benchmark]] using binary maps derived from instance-segmentation annotations.

## Related Concepts

- [[CarDD]]
- [[Car damage detection]]
- [[Defect segmentation]]
- [[F-measure]]
- [[S-measure]]
