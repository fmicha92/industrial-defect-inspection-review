---
title: "Mean Absolute Ranged Relative Error"
aliases:
  - "MARRE"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]"
evidence_count: 1
tags:
  - metric
  - emerging-taxonomy
---
# Mean Absolute Ranged Relative Error

## Definition

Mean Absolute Ranged Relative Error measures absolute forecast error relative to the observed range of the target time series. In [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]], lower MARRE indicates better target-parameter forecasting.

## Why It Matters

MARRE normalizes forecasting error by the target-series range, which helps compare welding-gun forecasting performance across different target scales.

## Used In These Papers

- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]] reports MARRE for every forecasting baseline; Temporal Fusion Transformer has the best reported mean MARRE at 5.3300.

## Related Concepts

- [[Welding gun fault prediction]]
- [[Mean Absolute Error]]
- [[Mean Absolute Percentage Error]]
- [[Mean Squared Error]]
