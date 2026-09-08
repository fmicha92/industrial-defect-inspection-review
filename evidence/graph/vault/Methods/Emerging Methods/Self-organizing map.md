---
title: "Self-organizing map"
aliases:
  - "SOM"
  - "self-organized map"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Classical ML"
source_papers:
  - "[[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]]"
evidence_count: 1
---
# Self-Organizing Map

## Definition

A self-organizing map maps high-dimensional feature vectors onto a two-dimensional lattice while preserving neighborhood structure. Li et al. use SOM clustering to group wafer maps that cannot be confidently assigned to an existing defect type.

## Why It Matters

SOM clustering supports discovery of undefined wafer-map defect patterns. In the wafer-map relabeling workflow, SOM clusters are separated with U-matrix wall finding and then reviewed to add or merge defect labels.

## Used In These Papers

- [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] uses SOM on unresolved [[WM-811K]] wafer maps to define additional defect labels such as Half-random, Center+Local, and Edge-ring+Local.

## Related Concepts

- [[Wafer map defect classification]]
- [[Bagging ensemble classifier]]
- [[Pseudo-labeling]]
