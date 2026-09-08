---
title: "Residual network"
aliases:
  - "ResNet"
  - "Residual neural network"
  - "residual learning framework"
tags:
  - method
  - model
---
# Residual Network

## Definition

A residual network learns residual functions with shortcut connections, typically optimizing a block output as `F(x) + x` rather than learning an unreferenced mapping directly.

## Why It Matters

Residual learning addresses the degradation problem in deep networks: deeper plain networks can have higher training error, while residual counterparts can optimize better and gain accuracy from depth.

## Used In These Papers

- [[2016 - Deep Residual Learning for Image Recognition]] introduces residual learning and evaluates ResNets from 18 to 152 layers on ImageNet, CIFAR-10, and detection/segmentation tasks.

## Related Concepts

- [[Computer Vision Models]]
- [[ResNet-18]]
- [[ResNet50]]
- [[Image classification]]
- [[Object detection]]

