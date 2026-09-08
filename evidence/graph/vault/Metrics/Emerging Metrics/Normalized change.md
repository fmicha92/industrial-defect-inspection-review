---
title: "Normalized change"
aliases:
  - "normalized change"
  - "c"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2007 - Normalized Change]]"
evidence_count: 1
tags:
  - metric
  - emerging-taxonomy
---

# Normalized change

## Definition

Normalized change measures change between a pre-test and post-test score by normalizing improvements against the maximum possible gain and declines against the maximum possible loss. In [[2007 - Normalized Change]], `c = (post - pre) / (100 - pre)` when `post > pre`, `c = (post - pre) / pre` when `post < pre`, and `c = 0` when the scores are equal except for matched 0% or 100% cases.

## Why It Matters

The metric keeps score changes in a -1 to +1 range and avoids normalized gain's asymmetric behavior when post-test scores decline. It also permits group summaries by averaging individual normalized changes when matched pre/post data are available.

## Used In These Papers

- [[2007 - Normalized Change]] introduces normalized change for physics education diagnostic assessments and recommends reporting the average of individual normalized changes with a conservative standard error.

## Related Concepts

- [[Pre-post diagnostic assessment]]
- [[Metrics]]
