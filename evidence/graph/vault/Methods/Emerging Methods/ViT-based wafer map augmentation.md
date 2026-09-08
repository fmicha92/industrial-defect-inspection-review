---
title: "ViT-based wafer map augmentation"
aliases:
  - "ViT-based wafer map augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]]"
evidence_count: 1
tags:
  - emerging-method
---
# ViT-based wafer map augmentation

## Definition

ViT-based wafer map augmentation uses Vision Transformer multi-head self-attention matrices to generate heatmap-like wafer defect maps for data augmentation. In the source paper, attention scores are averaged by row, rearranged into square maps, resized if needed, and added to training data before VGG16 wafer-map classification.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label defect data in industrial visual inspection.

## Used In These Papers


- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] uses ViT attention heatmaps to augment minority [[WM-811K]] wafer-map classes and reports improved Donut and Scratch recall plus higher accuracy than CycleGAN under equalized training sizes.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Vision Transformer]]
- [[Wafer map defect classification]]
- [[WM-811K]]
