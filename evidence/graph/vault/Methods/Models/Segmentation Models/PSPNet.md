---
title: "PSPNet"
aliases:
  - "Pyramid Scene Parsing Network"
tags:
  - method
  - model
---
# PSPNet

## Definition

PSPNet is a semantic segmentation architecture that uses pyramid pooling to combine contextual information at multiple spatial scales before producing dense pixel-level predictions.

## Why It Matters

Pyramid pooling can help segmentation models reason about larger scene context, but the BenchmarkELimages paper found that PSPNet was not the strongest model for small, narrow EL defects when compared with DeepLabv3+ using custom class weights.

## Used In These Papers

- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] evaluates PSPNet as one of four fully supervised semantic segmentation architectures on [[BenchmarkELimages]].

## Related Concepts

- [[Segmentation Models]]
- [[Defect segmentation]]
- [[Solar cell defect detection]]
- [[mIoU]]
- [[DeepLabV3+]]
- [[U-Net]]
