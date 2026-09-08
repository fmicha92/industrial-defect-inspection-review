---
title: "Defect-aware feature manipulation"
aliases:
  - "Defect-aware feature manipulation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]]"
evidence_count: 1
tags:
  - emerging-method
---
# Defect-aware feature manipulation

## Definition

Defect-aware feature manipulation modifies only defect-region features in a generative model rather than transferring an entire image distribution. In [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]], defect-aware residual blocks generate masks and add residual defect features inside masked regions of a frozen StyleGAN2 backbone.

## Why It Matters

It captures a reusable approach for few-shot defect generation where the non-defect object appearance should remain realistic and only localized defect regions should change.

## Used In These Papers


- [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] introduces defect-aware residual blocks that produce masks and manipulate StyleGAN2 features inside defect regions.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[DFMGAN]]
- [[StyleGAN2]]
