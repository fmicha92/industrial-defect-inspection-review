---
title: "Super-resolution data augmentation"
aliases:
  - "Blind super-resolution augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]]"
evidence_count: 1
tags:
  - method
---

# Super-resolution data augmentation

## Definition

Super-resolution data augmentation uses image super-resolution to enhance existing training images before training a downstream detector or segmenter. In fabric defect detection, the method can preserve texture detail while increasing the useful quality of scarce defect samples.

## Why It Matters

The 2025 fabric data augmentation paper reports that an improved Real-ESRGAN variant with Poisson degradation noise and a localized blur discriminative loss improved downstream YOLOv5n fabric defect detection on DAGM2007.

## Used In These Papers

- [[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]] augments [[DAGM2007]] and reports YOLOv5n gains of +7.4% precision, +1.0% recall, and +2.5% mAP.

## Related Concepts

- [[Data augmentation]]
- [[Textile defect detection]]
- [[Defect synthesis]]

