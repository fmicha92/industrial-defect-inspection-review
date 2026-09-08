---
title: "Mean Absolute Error"
aliases:
  - "MAE"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]"
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
  - "[[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]]"
evidence_count: 3
tags:
  - metric
  - emerging-taxonomy
---
# Mean Absolute Error

## Definition

Mean Absolute Error measures average absolute error between predicted and reference values. In [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]], lower MAE indicates better target-parameter forecasting; in [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]], lower MAE indicates better salient-object foreground maps.

## Why It Matters

MAE gives the benchmark a direct scale-sensitive error measure for forecasted welding-gun target parameters.

## Used In These Papers

- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]] reports MAE for multiple multivariate time-series forecasting methods; Temporal Fusion Transformer has the best reported mean MAE at 0.2099.
- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] reports PoolNet and SGL-KRN tied at MAE 0.071 on [[CarDD benchmark]], while noting that MAE is sensitive to object size.
- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] uses MAE as both a training loss and an I-V curve fit metric.

## Related Concepts

- [[Welding gun fault prediction]]
- [[Mean Squared Error]]
- [[Mean Absolute Percentage Error]]
- [[Mean Absolute Ranged Relative Error]]
- [[CarDD benchmark]]
