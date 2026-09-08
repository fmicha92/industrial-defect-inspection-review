---
title: "Weakly supervised learning"
tags:
  - learning-paradigm
---

# Weakly Supervised Learning

## Definition

Weakly supervised learning uses imperfect supervision, such as noisy labels, image-level labels, coarse annotations, or heuristic labels.

## Typical Use

Useful when precise labels such as pixel masks or bounding boxes are too expensive to collect.

## Vault Relevance

Relevant to inspection workflows where defect presence may be known but exact location, extent, or class may be incomplete.

## Used In These Papers

- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2011 - Non-parametric Texture Defect Detection Using Weibull Features]] evaluates on weakly labeled DAGM2007 texture defects, where labels are ellipses rather than exact pixel-wise masks.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] performs periodic-texture defect segmentation using image-level labels rather than region-level labels for model training.
