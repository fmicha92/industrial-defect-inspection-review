---
title: "MMD"
aliases:
  - "maximum mean discrepancy"
tags:
  - metric
  - generative-quality
---
# MMD

## Definition

MMD measures the distance between two distributions using a kernel mean embedding. In the Con-GAN paper, it is computed on Inception-v3 image features to compare generated defect images with real defect images.

## Direction

Lower is better.

## Used In These Papers

- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses MMD with FID to evaluate generated NEU-CLS defect-image quality and reports lower average MMD for Con-GAN than compared GANs.

## Related Metrics

- [[FID]]
- [[Generative quality metrics]]
