---
title: "Cross-domain few-shot object detection"
aliases:
  - "CD-FSOD"
  - "cross-domain FSOD"
tags:
  - task
---
# Cross-Domain Few-Shot Object Detection

## Definition

Cross-domain few-shot object detection adapts an object detector to a target domain with only a few labeled examples per novel class, while the target distribution differs from the source or pretraining distribution.

## Why It Matters

The task combines localization, classification, domain shift, and scarce annotation. Sparse support labels can make true unannotated objects look like false positives, and limited target-domain images can cause overfitting during detector fine-tuning.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] evaluates GiPL on RUOD, CARPK, and CarDD under 1/5/10-shot settings and reports gains from pseudo-labeling and Qwen-based generative augmentation.

## Related Concepts

- [[Object detection]]
- [[Few-shot zero-shot learning]]
- [[Domain gap]]
- [[Pseudo-labeling]]
- [[Data augmentation]]
- [[Learned generative synthesis]]
