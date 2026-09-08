---
title: "GLIP"
aliases:
  - "Grounded Language-Image Pre-training"
tags:
  - model
---
# GLIP

## Definition

GLIP is an open-set object detection model that reformulates detection as phrase grounding through vision-language alignment.

## Why It Matters

The GiPL paper uses GLIP-L with a Swin-L backbone for dense CARPK vehicle scenes, where iterative pseudo-labeling recovers unlabeled vehicle instances.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses GLIP for CARPK and reports that pseudo-labeling improves CARPK mAP@0.50 over zero-shot and vanilla fine-tuning.

## Related Concepts

- [[Object detection]]
- [[Cross-domain few-shot object detection]]
- [[Vision-language object detection]]
- [[Pseudo-labeling]]
