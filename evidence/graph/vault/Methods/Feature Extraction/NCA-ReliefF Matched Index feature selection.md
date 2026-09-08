---
title: "NCA-ReliefF Matched Index feature selection"
aliases:
  - "NRMI"
  - "NCA-ReliefF Matched Index"
status: stable
concept_type: method
source_papers:
  - "[[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]]"
evidence_count: 1
tags:
  - method
---
# NCA-ReliefF Matched Index feature selection

## Definition

NCA-ReliefF Matched Index feature selection is a feature-selection procedure that ranks deep features with Neighborhood Component Analysis and ReliefF, then selects feature indexes that match across the top-ranked features from both methods.

## Why It Matters

The method reduces the number of deep PAR-CNN features before SVM classification. In the source paper, it selects 100 features for binary steel defect classification and 66 features for multi-class classification, improving accuracy over unselected PAR-CNN features and NCA-only or ReliefF-only selection.

## Used In These Papers

- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] introduces NRMI for feature selection on 500 deep features extracted from [[Parallel attention-residual CNN]].

## Related Concepts

- [[Feature extraction]]
- [[Parallel attention-residual CNN]]
- [[Support vector machine]]
- [[Defect classification]]
