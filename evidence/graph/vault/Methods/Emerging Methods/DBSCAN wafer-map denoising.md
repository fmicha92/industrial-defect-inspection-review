---
title: "DBSCAN wafer-map denoising"
aliases:
  - "DBSCAN denoising"
  - "density-based wafer-map denoising"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]]"
evidence_count: 1
---
# DBSCAN Wafer-Map Denoising

## Definition

DBSCAN wafer-map denoising uses density-based clustering to keep clustered failed-die patterns and discard randomly distributed failed dies before feature extraction.

## Why It Matters

Removing random defects helps the downstream wafer-map classifier focus on systematic spatial defect patterns rather than noise.

## Used In These Papers

- [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] applies DBSCAN during preprocessing of [[WM-811K]] wafer maps before geometric, statistical, and Radon-transform feature extraction.

## Related Concepts

- [[Wafer map defect classification]]
- [[Self-organizing map]]
- [[Semi-supervised learning]]
