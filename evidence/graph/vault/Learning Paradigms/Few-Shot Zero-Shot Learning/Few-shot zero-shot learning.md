---
title: "Few-shot / zero-shot learning"
aliases:
  - "Few-shot learning"
  - "Zero-shot learning"
tags:
  - learning-paradigm
---

# Few-Shot / Zero-Shot Learning

## Definition

Few-shot learning aims to generalize from very few labeled examples. Zero-shot learning aims to recognize or solve tasks without task-specific labeled examples.

## Typical Use

Useful for rare classes, new defect types, open-vocabulary recognition, and rapid adaptation.

## Vault Relevance

Relevant to industrial inspection because new defect modes may appear before enough labeled examples exist for conventional supervised training.

## Used In These Papers

- [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] trains DFMGAN's defect modules from only a handful of MVTec AD defect images while using more defect-free images for the StyleGAN2 backbone.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] evaluates k-shot defect segmentation using K normal support images and unseen product categories.
