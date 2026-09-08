---
title: "Parallel attention-residual CNN"
aliases:
  - "PAR-CNN"
  - "Parallel Attention Residual-Convolutional Neural Network"
status: stable
concept_type: method
source_papers:
  - "[[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]]"
evidence_count: 1
tags:
  - method
  - model
---
# Parallel attention-residual CNN

## Definition

Parallel attention-residual CNN is a convolutional feature extractor that trains residual blocks and an attention structure in parallel, then uses the resulting deep features for steel surface defect classification.

## Why It Matters

The architecture is designed to improve classification features for [[Metal inspection]] while keeping residual depth bounded by hardware limits. In the source paper, PAR-CNN features outperform the same architecture's softmax classifier when passed to [[Support vector machine]], and improve further after [[NCA-ReliefF Matched Index feature selection]].

## Used In These Papers

- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] proposes PAR-CNN for extracting 500 deep features from Severstal steel surface images.

## Related Concepts

- [[Computer Vision Models]]
- [[Deep convolutional neural network]]
- [[Residual network]]
- [[Defect classification]]
- [[NCA-ReliefF Matched Index feature selection]]
