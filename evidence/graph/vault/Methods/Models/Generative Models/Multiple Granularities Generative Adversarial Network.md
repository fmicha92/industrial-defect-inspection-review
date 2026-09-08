---
title: "Multiple Granularities Generative Adversarial Network"
aliases:
  - "Multiple Granularities Generative Adversarial Network"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Generative Models"
source_papers:
  - "[[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]]"
evidence_count: 1
tags:
  - method
---

# Multiple Granularities Generative Adversarial Network

## Definition

Multiple Granularities Generative Adversarial Network (MGGAN) is a GAN architecture for wafer map generation and class-imbalance mitigation. It uses ResNet101 as an auxiliary feature extractor, feeds multigranularity features into the generator, and uses feature matching between generator and discriminator features to stabilize adversarial training.

## Why It Matters

The source paper reports that MGGAN-enhanced data raises ResNet101 wafer-map recognition accuracy to 93.43% on the WM-811K experiment setting, while random-noise-only or label-vector conditioning performs worse. The method is a concrete example of data-level class-imbalance handling for wafer map defect classification.

## Used In These Papers

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] introduces MGGAN with ResNet101 multigranularity features, feature matching, and a lightweight discriminator for [[WM-811K]] class-imbalance augmentation.

## Related Concepts

- [[GAN]]
- [[Data augmentation]]
- [[WM-811K]]

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] supports wafer map defect recognition, class imbalance.
