---
title: "Segmentation-decision network"
aliases:
  - "segmentation and decision network"
  - "two-stage segmentation decision network"
tags:
  - method
  - model
  - segmentation
---
# Segmentation-decision Network

## Definition

A segmentation-decision network is a two-stage visual inspection architecture in which a segmentation network predicts pixel-level defect evidence and a decision network uses segmentation features plus the segmentation output to classify whether the whole image is defective.

## Why It Matters

The design lets pixel-wise supervision shape defect features while still optimizing for the image-level decision required in industrial quality control.

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] proposes this architecture for [[KolektorSDD]], reaching 99.9% [[Average precision]] with zero false positives and one false negative.

## Related Concepts

- [[Segmentation Models]]
- [[Deep convolutional neural network]]
- [[Defect segmentation]]
- [[Defect classification]]
- [[Surface defect detection]]
- [[KolektorSDD]]
