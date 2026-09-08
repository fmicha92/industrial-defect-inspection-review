---
title: "Classical ML"
tags:
  - model-family
---

# Classical ML

## Scope

Classical ML covers non-deep-learning algorithms that are often strong baselines for tabular data, small or medium datasets, interpretable systems, and production settings where reliability matters.

## Common Models

- Linear models: linear regression, logistic regression
- Tree models: decision trees, random forests
- Boosting: [[XGBoost]], LightGBM, CatBoost
- Margin / instance methods: support vector machines, k-nearest neighbors
- Probabilistic methods: Naive Bayes, Gaussian processes

## Current Vault Links

- not reported in the processed paper graph as a central model family yet

## Used In These Papers

- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]] supports fabric inspection, public benchmark.
- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]] benchmarks linear regression, Bayesian ridge regression, random forest regression, and LightGBM for welding-gun target-parameter forecasting.
- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] uses PCA, K-means, and random forests for sparse Bosch production-line failure prediction.
- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] compares SVM, Random Forest, GridSearch Random Forest, and XGBoost against CNN-based PV panel classifiers.
