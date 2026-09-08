---
title: "GAN-Train GAN-Test"
aliases:
  - "GAN-Train"
  - "GAN-Test"
tags:
  - metric
  - generative-quality
---

# GAN-Train GAN-Test

## Definition

GAN-Train and GAN-Test are paired evaluation protocols for generated image sets. In GAN-Train, a classifier is trained on generated images and evaluated on real or comparison images; in GAN-Test, the classifier is trained on real or comparison images and evaluated on generated images. [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] uses the pair to assess generated image diversity and realism.

## Direction

Higher classification rates are generally better, but the two directions must be interpreted jointly because GAN-Train emphasizes generated-image diversity and GAN-Test emphasizes generated-image realism.

## Used In These Papers

- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] uses GAN-Train and GAN-Test as the primary generative evaluation protocol.

## Related Metrics

- [[FID]]
- [[Generative quality metrics]]
