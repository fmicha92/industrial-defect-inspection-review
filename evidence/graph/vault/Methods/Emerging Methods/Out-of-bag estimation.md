---
title: "Out-of-bag estimation"
aliases:
  - "OOB estimation"
  - "out-of-bag error"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Classical ML"
source_papers:
  - "[[2001 - Random Forests]]"
evidence_count: 1
---
# Out-of-Bag Estimation

## Definition

Out-of-bag estimation evaluates each training example using only trees for which that example was left out of the bootstrap sample.

## Why It Matters

Breiman uses out-of-bag estimates to monitor random forest error, tree strength, correlation, and variable importance without a separate validation set.

## Used In These Papers

- [[2001 - Random Forests]] uses out-of-bag estimates to select the number of random features, estimate generalization error, and compute variable importance.

## Related Concepts

- [[Random forest]]
- [[Decision tree]]

