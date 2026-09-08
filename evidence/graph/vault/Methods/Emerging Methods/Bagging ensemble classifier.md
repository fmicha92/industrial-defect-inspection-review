---
title: "Bagging ensemble classifier"
aliases:
  - "Bootstrap aggregating"
  - "Bagging"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Classical ML"
source_papers:
  - "[[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]]"
evidence_count: 1
---
# Bagging Ensemble Classifier

## Definition

Bagging ensemble classification trains multiple weak classifiers on random samples of the training data and combines their votes into a final prediction. Li et al. use 1,000 decision trees, each trained on a random 80% of the training data, for wafer-map defect classification.

## Why It Matters

The voting distribution gives a confidence score for each predicted defect type. In the wafer-map relabeling workflow, low-confidence samples are treated as questionable or unresolved rather than accepted as reliable labels.

## Used In These Papers

- [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] uses a 1,000-tree Bagging classifier to screen mislabeled [[WM-811K]] wafer maps and classify unlabeled maps above class-specific confidence thresholds.

## Related Concepts

- [[Semi-supervised learning]]
- [[Wafer map defect classification]]
- [[Self-organizing map]]
 - [[YOLOv5]]
+- [[Bagging ensemble classifier]]
