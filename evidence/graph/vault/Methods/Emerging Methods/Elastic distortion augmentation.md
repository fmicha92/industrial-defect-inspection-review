---
title: "Elastic distortion augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2003 - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis]]"
evidence_count: 1
tags:
  - method
---

# Elastic Distortion Augmentation

## Definition

Elastic distortion augmentation warps images using smoothed random displacement fields, producing local deformations that mimic handwriting variation in the cited MNIST experiments.

## Why It Matters

The Simard et al. paper reports that elastic distortions improve MNIST error more than affine distortions for both multilayer perceptrons and convolutional networks.

## Used In These Papers

- [[2003 - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis]] uses elastic distortions with a simple CNN and reports 0.4% MNIST test error.

## Related Concepts

- [[Data augmentation]]
- [[Handwritten digit recognition]]
- [[MNIST]]
