---
title: "Contrastive regularization loss"
aliases:
  - "Contrastive regularization"
  - "Soft-nearest-neighbor regularization"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]]"
evidence_count: 1
tags:
  - method
  - emerging-taxonomy
---

# Contrastive Regularization Loss

## Definition

Contrastive regularization loss is used in [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] as an added training objective for supervised OK/nOK classification. The paper adds a soft-nearest-neighbor loss term on feature embeddings before the final classifier to the standard cross-entropy loss.

## Why It Matters

The regularizer encourages samples from the same OK/nOK class to move closer in embedding space and samples from different classes to move apart. In the gearbox component benchmark, this is intended to reduce component-specific shortcuts and improve generalization under [[Distribution shift]].

## Used In These Papers

- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] applies the loss to ResNet-50 and reports improved mean [[F1-score]], especially on the component-category split S4.

## Related Concepts

- [[Deep convolutional neural network]]
- [[Defect classification]]
- [[Distribution shift]]
- [[F1-score]]
