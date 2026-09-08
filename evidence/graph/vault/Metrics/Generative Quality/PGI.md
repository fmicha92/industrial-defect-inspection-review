---
title: "PGI"
aliases:
  - "Polymorphic Generative Index"
  - "polymorphic generative index"
tags:
  - metric
  - generative-quality
---
# PGI

## Definition

PGI is the polymorphic generative index proposed for evaluating wafer bin map augmentation models. It compares generated wafer maps with original class patterns and is computed per defect pattern.

## Direction

Higher is better.

## Used In These Papers

- [[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]] proposes PGI to compare DCGAN-based and CAE-based wafer map augmentation without relying on ImageNet-pretrained metrics.

## Notes

- The paper states PGI is limited when the number of original examples is extremely small, such as the one-sample donut class in the selected WM-811K subset.
- PGI depends on the classifier used to calculate it, so comparisons should use the same classifier structure.

## Related Metrics

- [[Accuracy]]
- [[FID]]
- [[Generative quality metrics]]
