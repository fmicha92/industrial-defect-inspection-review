---
title: "Pseudo-labeling"
aliases:
  - "pseudo-label generation"
  - "pseudo-labeled data"
status: emerging
concept_type: method
candidate_parent: "Learning Paradigms/Semi-Supervised Learning"
source_papers:
  - "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
  - "[[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]]"
  - "[[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]]"
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
evidence_count: 4
---
# Pseudo-Labeling

## Definition

Pseudo-labeling uses a model trained on labeled data to assign tentative labels to unlabeled samples, then reuses sufficiently confident predictions as additional training labels.

## Why It Matters

Industrial defect datasets often have few labeled defect images. Pseudo-labeling can expand training data when manual annotation is expensive.

## Used In These Papers

- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] trains YOLOv5s on labeled automotive-glass images and uses confidence-filtered predictions to create pseudo-labels for unlabeled images.
- [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] uses confidence-thresholded ensemble predictions to assign labels to unlabeled [[WM-811K]] wafer maps before clustering unresolved maps.
- [[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]] uses pseudo-label supervision with perturbation consistency to exploit unlabeled industrial defect images for segmentation.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses iterative pseudo-labeling on CARPK to recover unlabeled vehicle instances in sparse few-shot support images.

## Related Concepts

- [[Semi-supervised learning]]
- [[YOLOv5]]
- [[Bagging ensemble classifier]]
- [[Cross-domain few-shot object detection]]
- [[GLIP]]
