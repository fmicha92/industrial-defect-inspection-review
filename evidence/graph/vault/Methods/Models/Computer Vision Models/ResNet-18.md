---
title: "ResNet-18"
aliases:
  - "ResNet18"
  - "18-layer ResNet"
tags:
  - model
---
# ResNet-18

## Definition

ResNet-18 is an 18-layer residual convolutional neural network used as an image feature extractor or classifier. In [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]], it is the backbone for self-supervised anomaly localization, and feature stages C2, C3, and C4 provide dense maps for anomaly scoring.

## Why It Matters

Residual CNN backbones provide reusable multi-scale image features for industrial visual inspection and anomaly localization.

## Used In These Papers

- [[2016 - Deep Residual Learning for Image Recognition]] evaluates 18-layer residual networks on ImageNet.
- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] trains ResNet-18 from scratch on MVTec AD normal images and uses its feature maps for regression-error and uncertainty scoring.
- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] uses ResNet-18 as a deep feature extractor for the hybrid CNN + SVM model and the XGBoost feature pipeline.

## Related Concepts

- [[Computer Vision Models]]
- [[Residual network]]
- [[ResNet50]]
- [[Industrial anomaly detection]]
- [[Dynamic Local Augmentation]]
- [[Support vector machine]]
