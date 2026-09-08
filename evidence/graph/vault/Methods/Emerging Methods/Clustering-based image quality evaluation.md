---
title: "Clustering-based image quality evaluation"
aliases:
  - "IQE module"
  - "image quality evaluation module"
status: emerging
concept_type: method
candidate_parent: "Methods/Deployment"
source_papers:
  - "[[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]]"
evidence_count: 1
---
# Clustering-Based Image Quality Evaluation

## Definition

Clustering-based image quality evaluation filters video frames by extracting HOG features, clustering frames with K-means, selecting high-quality clusters, and discarding frames closest to lower-quality clusters.

## Why It Matters

In rotating optical-glass videos, motion blur and out-of-focus frames can hurt defect detection. Filtering lower-quality frames improves final prediction quality in the reported OGD-DET experiments.

## Used In These Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] uses the IQE module before final defect detection and reports that adding IQE raises precision from 0.9050 to 0.9948 while preserving 1.0 recall.

## Related Concepts

- [[Video-based two-stage defect detection]]
- [[Optical glass defect detection]]
- [[Industrial visual inspection]]
