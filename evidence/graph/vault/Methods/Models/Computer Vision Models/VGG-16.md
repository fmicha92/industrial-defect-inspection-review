---
title: "VGG-16"
aliases:
  - "VGG16"
  - "VGG-16 network"
tags:
  - method
  - model
status: "stable"
concept_type: "method"
source_papers:
  - "[[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]"
related_methods:
  - "[[Computer Vision Models]]"
  - "[[Segmentation Models]]"
related_tasks:
  - "[[Defect segmentation]]"
---
# VGG-16

## Definition

VGG-16 is a convolutional neural network architecture used as a pretrained feature extractor in computer vision models. In the PGA-Net paper, VGG-16 pretrained on ImageNet provides the feature extraction module for multilevel surface-defect segmentation features.

## Why It Matters

As a backbone, VGG-16 supplies low-level and high-level feature maps that can be reused by segmentation heads, feature fusion modules, and defect inspection models.

## Used In These Papers

- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] uses pretrained VGG-16 as the feature extraction module before pyramid feature fusion.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] uses VGG16 as the wafer-map classifier for evaluating ViT and CycleGAN augmentation on [[WM-811K]].

## Related Concepts

- [[Computer Vision Models]]
- [[Segmentation Models]]
- [[Defect segmentation]]
