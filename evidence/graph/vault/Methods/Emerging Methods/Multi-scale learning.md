---
title: "Multi-scale learning"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
evidence_count: 1
---
# Multi-Scale Learning

## Definition

Multi-scale learning trains a vision model with resized inputs at multiple scales so the model sees a wider distribution of object sizes.

## Why It Matters

In [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]], [[DCN+]] uses multi-scale resizing to improve damage detection under scale variation, especially for hard car-damage categories.

## Used In These Papers

- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] randomly resizes training-image height in the range 640 to 1200 while keeping width at 1333.

## Related Concepts

- [[DCN+]]
- [[Car damage detection]]
- [[Average precision]]
