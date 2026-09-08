---
title: "Mean Absolute Percentage Error"
aliases:
  - "MAPE"
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
# Mean Absolute Percentage Error

## Definition

Mean Absolute Percentage Error measures average absolute forecast error as a percentage of the actual value. In [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]], lower MAPE indicates better target-series forecasting.

## Why It Matters

MAPE lets the benchmark compare forecast errors relative to the magnitude of welding-gun target parameters.

## Used In These Papers

- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]] reports MAPE for every forecasting baseline; random forest has the best reported mean MAPE at 90.5216.

## Related Concepts

- [[Welding gun fault prediction]]
- [[Mean Absolute Error]]
- [[Mean Squared Error]]
- [[Mean Absolute Ranged Relative Error]]
