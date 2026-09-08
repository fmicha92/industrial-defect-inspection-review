---
title: "Principal Component Analysis"
aliases:
  - "PCA"
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
# Principal Component Analysis

## Definition

Principal Component Analysis transforms correlated input features into lower-dimensional uncorrelated components while preserving as much variance as possible.

## Why It Matters

PCA can make high-dimensional, sparse production data easier to cluster or visualize before downstream prediction.

## Used In These Papers

- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] uses PCA on binary feature-presence indicators before K-means process clustering.

## Related Concepts

- [[Classical ML]]
- [[K-means clustering]]
- [[Manufacturing failure prediction]]
