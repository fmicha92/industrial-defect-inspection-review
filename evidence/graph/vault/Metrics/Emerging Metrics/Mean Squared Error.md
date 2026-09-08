---
title: "Mean Squared Error"
aliases:
  - "MSE"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]"
  - "[[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]]"
evidence_count: 2
tags:
  - metric
  - emerging-taxonomy
---
# Mean Squared Error

## Definition

Mean Squared Error measures average squared point-forecast error between two time series of equal length. In [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]], lower MSE indicates better target-series forecasting and is also used as the training loss.

## Why It Matters

MSE penalizes larger target-forecasting errors more heavily than absolute-error measures, making it useful for identifying methods with large deviations on welding-gun target parameters.

## Used In These Papers

- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]] trains forecasting models with MSE loss and reports MSE as a benchmark metric; random forest has the best reported mean MSE at 0.0958.
- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] uses MSE as both a training loss and an I-V curve fit metric.

## Related Concepts

- [[Welding gun fault prediction]]
- [[Mean Absolute Error]]
- [[Mean Absolute Percentage Error]]
- [[Mean Absolute Ranged Relative Error]]
