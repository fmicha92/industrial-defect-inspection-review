---
title: "Focal loss"
status: emerging
concept_type: method
candidate_parent: "Methods/Losses"
source_papers:
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
evidence_count: 1
---
# Focal Loss

## Definition

Focal loss is a classification loss used in [[DCN+]] to emphasize hard damage categories in car damage detection.

## Why It Matters

In [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]], focal loss improves the hard dent, scratch, and crack classes and boosts small-object AP.

## Used In These Papers

- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] uses focal loss with alpha 0.50 and gamma 2.0 in [[DCN+]].

## Related Concepts

- [[DCN+]]
- [[Car damage detection]]
- [[Average precision]]
