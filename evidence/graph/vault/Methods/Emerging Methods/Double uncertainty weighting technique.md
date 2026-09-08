---
title: "Double uncertainty weighting technique"
aliases:
  - "DUW"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]]"
evidence_count: 1
---
# Double uncertainty weighting technique

## Definition

Double uncertainty weighting is a loss-weighting strategy for semi-supervised strip steel surface defect classification. The linked paper applies one weighting rule to labeled samples based on whether predictions match labels and another to unlabeled samples based on whether student and teacher predictions agree.

## Why It Matters

It increases the loss weight for uncertain or misclassified samples, encouraging the model to learn from harder labeled and unlabeled NEU-CLS examples.

## Used In These Papers

- [[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]] uses double uncertainty weighting for supervised and unsupervised losses in semi-supervised NEU-CLS classification.

## Related Concepts

- [[Semi-supervised learning]]
- [[Defect classification]]
- [[NEU-CLS]]
