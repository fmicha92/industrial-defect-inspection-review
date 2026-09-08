---
title: "K-means clustering"
aliases:
  - "K-means"
  - "K-means algorithm"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Classical ML"
source_papers:
  - "[[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]]"
evidence_count: 1
tags:
  - method
  - emerging-taxonomy
---
# K-means Clustering

## Definition

K-means clustering partitions observations into a fixed number of clusters by iteratively assigning observations to the nearest centroid and updating centroids until convergence.

## Why It Matters

K-means can separate products or process traces into groups with similar measurement patterns before fitting specialized classifiers.

## Used In These Papers

- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] uses K-means to divide Bosch production-line records into six process groups.

## Related Concepts

- [[Principal Component Analysis]]
- [[Classical ML]]
- [[Manufacturing failure prediction]]
