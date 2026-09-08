---
title: "Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data"
aliases:
  - "Benchmark for welding gun fault prediction with multivariate time series data"
paper_key: "doi:10.1038/s41597-024-02914-z)/producer(itext"
paper_type: "dataset"
year: 2024
venue: "Scientific Data"
authors:
  - "Xiaoye Wang"
  - "Changsheng Zhang"
  - "Tao Wang"
status: "processed"
topics:
  - "resistance spot welding"
  - "predictive maintenance"
  - "multivariate time series forecasting"
tasks:
  - "[[Welding gun fault prediction]]"
datasets:
  - "[[RSW gun fault prediction benchmark dataset]]"
methods:
  - "[[Classical ML]]"
  - "[[Neural Networks]]"
  - "[[Transformers]]"
metrics:
  - "[[Mean Absolute Error]]"
  - "[[Mean Absolute Percentage Error]]"
  - "[[Mean Absolute Ranged Relative Error]]"
  - "[[Mean Squared Error]]"
  - "[[Accuracy]]"
  - "[[Recall]]"
primary_metric: "[[Mean Absolute Error]]"
domains:
  - "[[Automotive manufacturing]]"
related_domains:
  - "[[Smart manufacturing]]"
related_datasets:
  - "[[RSW gun fault prediction benchmark dataset]]"
related_tasks:
  - "[[Welding gun fault prediction]]"
related_methods:
  - "[[Classical ML]]"
  - "[[Neural Networks]]"
  - "[[Transformers]]"
url: "https://doi.org/10.1038/s41597-024-02914-z"
doi: "10.1038/s41597-024-02914-z"
data: "https://zenodo.org/records/7655193"
code: "https://zenodo.org/record/7655025"
source_file: "paper-inbox/10_processed/Dataset/2024 - Wang - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Wang - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Wang - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data.txt"
processed_at: "2026-06-01"
---
# Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data

## Summary

Wang, Zhang, and Wang introduce an open benchmark dataset for resistance spot welding gun fault prediction in automotive body-shop production. The dataset contains 80 multivariate time series from real production welding guns, with 72 series for training and 8 for testing, each sampled at 1 Hz over 604800 timestamps. Each timestamp includes 19 welding-gun parameters plus an error code, and the published data intentionally retains missing values and outliers to preserve real industrial imperfections.

### Graph Hubs

- Tasks: [[Welding gun fault prediction]]
- Datasets: [[RSW gun fault prediction benchmark dataset]]
- Methods: [[Classical ML]], [[Neural Networks]], [[Transformers]]
- Metrics: [[Mean Absolute Error]], [[Mean Absolute Percentage Error]], [[Mean Absolute Ranged Relative Error]], [[Mean Squared Error]], [[Accuracy]], [[Recall]]
- Domains: [[Automotive manufacturing]], [[Smart manufacturing]]

## Paper Type

Dataset paper. The core contribution is the release and technical validation of [[RSW gun fault prediction benchmark dataset]], plus baseline forecasting and fault-prediction experiments for the associated task.

## Problem

Resistance spot welding guns can stop automotive manufacturing lines when their servo-pneumatic control system fails. The paper frames the task as using historical welding control, sensor, and status time series to predict future welding-gun faults before they interrupt production.

The target classes are:

- E001: counterbalance timeout.
- E002: electrode broke.
- E003: unwanted movement.
- E004: drift.
- E000: normal state.

## Contribution

- Releases an open multivariate time-series benchmark from 80 production RSW guns collected in the Body-Shop of BMW Brilliance Automotive Ltd.
- Defines welding gun fault prediction as a two-stage task: forecast target welding parameters over a 60-second prediction range, then diagnose the resulting state with rule-based or learned working-state logic.
- Benchmarks multiple global forecasting methods on the dataset and reports both forecasting-error metrics and downstream state-classification results.

## Dataset

[[RSW gun fault prediction benchmark dataset]] contains:

- 72 training time series and 8 testing time series.
- 604800 samples per time series at 1 sample per second.
- 20 dimensions per timestamp: 19 welding-gun variables and one error code.
- CSV files grouped by error code and gun id.
- Missing values and outliers retained in the released files.
- Data collected from welding guns that worked continuously for more than 7 days and ended with a welding error.

The 19 machine parameters are electrode cap offset, electrode force, electrode position, force build-up, balance pressure, friction, maximum aperture, maximum electrode force, start friction, US2, welding point count, position count, setpoints for counterbalance pressure, electrode force, electrode position, sheet thickness, velocity, force build-up, and offset value in robot.

## Method

The data construction pipeline collects real-time welding data from welding controllers, PLCs, an IoT gateway, and a cloud database. Raw data are resampled to 1 Hz, then missing-rate and outlier handling is applied for internal filtering. The released dataset keeps the imperfections so fault-prediction methods can be evaluated under realistic industrial time-series conditions.

The benchmark uses a two-stage strategy:

1. Forecast the target series in the prediction range from the conditioning range.
2. Map the forecast target series to a welding-gun state using welding-gun diagnosis logic.

The benchmark compares linear regression, Bayesian ridge regression, random forest regression, LightGBM, RNN, LSTM, GRU, N-BEATS, TCN, and Temporal Fusion Transformer. Local forecasting models and univariate-only statistical methods are excluded because the task uses many welding-gun series, multivariate target parameters, and past-observed covariates.

## Evidence

The benchmark setup uses 32-bit data, zero-mean/unit-variance normalization, KNN imputation for missing values in benchmark training, a 60-second lead time, input chunk length 20, MSE loss, 100 epochs, and batch size 32. Tests are reported on an Intel i7-8700 CPU, NVIDIA GeForce GTX 1080, and 16 GB RAM.

Forecasting benchmark means:

| Method | MAE | MAPE | MARRE | MSE |
|---|---:|---:|---:|---:|
| Bayesian ridge | 0.6047 | 174.0001 | 15.3520 | 0.7032 |
| Linear regression | 0.5431 | 255.9767 | 13.7886 | 0.5156 |
| Random forest | 0.2203 | 90.5216 | 5.5921 | 0.0958 |
| N-BEATS | 0.3041 | 214.3311 | 7.7203 | 0.1671 |
| LightGBM | 0.3174 | 148.2126 | 8.0568 | 0.2055 |
| RNN | 0.4008 | 164.0906 | 10.1751 | 0.2403 |
| LSTM | 0.8479 | 598.6380 | 21.5250 | 1.3111 |
| GRU | 0.6668 | 604.9237 | 16.9287 | 1.0064 |
| TCN | 0.9413 | 219.2912 | 23.8958 | 1.7227 |
| TFT | 0.2099 | 181.1341 | 5.3300 | 0.1047 |

Random forest is best by MAPE and MSE. Temporal Fusion Transformer is best by MAE and MARRE. The paper reports that no method dominates across all instances and error types.

Downstream working-state classification from forecasted data reaches 68.62% average accuracy, recall 0.4431 for normal state, recall 0.7431 for error state, and low recall for each individual error type: E01 0.3578, E02 0.1945, E03 0.2385, and E04 0.1843. The paper treats these results as unsatisfactory for predictive-maintenance advice because they produce too many false alarms and do not distinguish error kind accurately enough.

## ML/DL Extraction

- Task formulation: multivariate time-series forecasting followed by welding-gun state diagnosis.
- Inputs: historical welding-gun control, cylinder, status, electrode-monitoring, and gun-information parameters.
- Outputs: forecast target parameters, then normal/error or specific error class.
- Forecast targets: electrode force for E02 and balance pressure for E01, E03, and E04.
- Covariates: other components of the welding time series.
- Training: 100 epochs, batch size 32, MSE loss, input chunk length 20.
- Data preprocessing for benchmark models: normalization to zero mean and unit variance, KNN imputation.
- Metrics: [[Mean Absolute Error]], [[Mean Absolute Percentage Error]], [[Mean Absolute Ranged Relative Error]], [[Mean Squared Error]], [[Accuracy]], and [[Recall]].
- Artifacts: dataset and benchmark code are available on Zenodo.

## Limitations

- Missing values and outliers are common because of sensor faults, IoT network failures, transmission latency, cap dressing, and cap changing.
- The 1 Hz sampling rate cannot characterize an individual welding process that lasts hundreds of milliseconds.
- The downstream fault-prediction result is not strong enough for reliable predictive-maintenance advice in the reported setup.
- Individual error-type recall is low, indicating that forecasted target parameters are not accurate enough to separate fault types.

## Connections

### Shares Dataset

- [[RSW gun fault prediction benchmark dataset]] is introduced and validated by this paper.

### Shares Task

- [[Welding gun fault prediction]] is the primary task defined around forecasting future welding-gun parameters and predicting future fault states.

### Shares Method

- [[Classical ML]] covers the linear, Bayesian ridge, random forest, and LightGBM benchmark family.
- [[Neural Networks]] covers RNN, LSTM, GRU, N-BEATS, and TCN forecasting baselines.
- [[Transformers]] covers Temporal Fusion Transformer, the best method by MAE and MARRE in the reported benchmark.

### Shares Metric

- [[Mean Absolute Error]], [[Mean Absolute Percentage Error]], [[Mean Absolute Ranged Relative Error]], and [[Mean Squared Error]] evaluate target-series forecasting.
- [[Accuracy]] and [[Recall]] evaluate downstream normal/error and error-type classification.

### Application/Domain

- [[Automotive manufacturing]] is the production setting because the dataset comes from automotive body-shop resistance spot welding.
- [[Smart manufacturing]] is relevant because the data are collected through an IoT production-data pipeline for predictive maintenance.

## Source Anchors

- Paper DOI: [10.1038/s41597-024-02914-z](https://doi.org/10.1038/s41597-024-02914-z)
- Dataset: [https://zenodo.org/records/7655193](https://zenodo.org/records/7655193)
- Benchmark code: [https://zenodo.org/record/7655025](https://zenodo.org/record/7655025)

## Questions

- Does the Zenodo record include additional metadata that identifies exact production stations or only anonymized gun ids?
- Can the downstream classifier be improved by training directly on fault-state labels rather than only forecasted target parameters?
