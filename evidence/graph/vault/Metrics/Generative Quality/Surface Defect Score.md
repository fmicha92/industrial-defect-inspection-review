---
title: "Surface Defect Score"
aliases:
  - "SDS"
tags:
  - metric
  - generative-quality
---
# Surface Defect Score

## Definition

Surface Defect Score is a generated-image quality metric proposed for surface defect synthesis. It trains a ResNet18 classifier to distinguish real from fake defect images, then converts the fake-image classification accuracy into a similarity score.

## Direction

Higher is better.

## Used In These Papers

- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] proposes SDS because FID can remain strong even when generated surface defect regions disappear.

## Related Metrics

- [[FID]]
- [[Generative quality metrics]]
