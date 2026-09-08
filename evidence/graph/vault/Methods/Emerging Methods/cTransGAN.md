---
title: "cTransGAN"
aliases:
  - "conditional TransGAN"
  - "Conditional TransGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]]"
evidence_count: 1
tags:
  - emerging-method
---
# cTransGAN

## Definition

cTransGAN is the conditional TransGAN augmentation method proposed for PCB component and defect inspection. It conditions a TransGAN generator and discriminator on learned class embeddings so generated images belong to a desired PCB component or defect class.

## Why It Matters

It records a transformer-based GAN augmentation approach for small-object PCB inspection where limited training data reduces detector mAP.

## Used In These Papers

- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] proposes cTransGAN and uses it to augment detector training on a self-developed PCB component dataset and [[DeepPCB]].

## Related Concepts

- [[GAN]]
- [[Transformers]]
- [[Data augmentation]]
- [[Synthetic data generation]]
- [[PCB defect detection]]
