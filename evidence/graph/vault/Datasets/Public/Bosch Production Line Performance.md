---
title: "Bosch Production Line Performance"
aliases:
  - "Bosch Production Line Performance"
  - "Bosch Production Line Performance dataset"
  - "Bosch assembly line fault detection dataset"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://www.kaggle.com/c/bosch-production-line-performance"
data_sources:
  - "Kaggle"
  - "Bosch"
access: "public Kaggle competition data; Kaggle account and competition rules may be required"
licenses:
  - "not reported"
modalities:
  - "tabular production-line measurements"
tasks:
  - "[[Manufacturing failure prediction]]"
metrics:
  - "[[Matthews correlation coefficient]]"
related_papers:
  - "[[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]]"
  - "https://openalex.org/W2583522268"
introduced_by: "not reported"
---
# Bosch Production Line Performance

## Definition

Bosch Production Line Performance is a Kaggle competition dataset for predicting internal production-line failures from anonymized measurements and tests recorded for parts as they move through Bosch assembly lines.

## Why It Matters

The dataset is a large, sparse, high-dimensional industrial machine-learning benchmark. It supports research on manufacturing quality control, failure prediction, feature selection, and robust supervised learning under heavy class imbalance.

## Dataset Details

- Host: Kaggle competition, "Bosch Production Line Performance".
- Competition subtitle: "Reduce manufacturing failures".
- Provider: Bosch.
- Task: predict which parts fail internal quality control.
- Target label: `Response`, where public descriptions report `0` for pass and `1` for fail.
- Instance identifier: each part has a unique `Id`.
- Data modality: tabular production-line measurements.
- Feature groups: numeric, categorical, and date/timestamp features.
- File groups reported for the competition: `train_numeric.csv`, `test_numeric.csv`, `train_categorical.csv`, `test_categorical.csv`, `train_date.csv`, `test_date.csv`, and `sample_submission.csv`.
- Feature naming convention: feature names encode production line, station, and feature number, such as `L3_S36_F3939`.
- Date-feature naming convention: date columns encode the measurement timestamp for corresponding station/feature fields, such as `L0_S0_D1`.
- Scale: public dataset descriptions report roughly 1.18 million parts and thousands of anonymized feature columns.
- Data challenge: public descriptions report high sparsity and a highly imbalanced failure label.
- Competition evaluation metric: Matthews correlation coefficient.
- Access: Kaggle competition page; a Kaggle account and competition rules acceptance may be required to download files.
- License: not reported in the extracted accessible page text.

## Used In These Papers

- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] uses the numerical Bosch production-line features for sparse, imbalanced binary failure prediction with process clustering and random forests.
- [Using big data to enhance the Bosch production line performance: A Kaggle challenge](https://openalex.org/W2583522268) describes a modeling approach for the Kaggle challenge and reports that the data records tests and measurements for components along an assembly line to predict internal failures.

## Source Anchors

- Hosting source: [Kaggle competition](https://www.kaggle.com/c/bosch-production-line-performance).
- Data page: [Kaggle data tab](https://www.kaggle.com/c/bosch-production-line-performance/data).
- Related paper: [Using big data to enhance the Bosch production line performance: A Kaggle challenge](https://openalex.org/W2583522268), DOI [10.1109/bigdata.2016.7840826](https://doi.org/10.1109/bigdata.2016.7840826).
- Related paper: [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]], DOI [10.1109/bigdata.2016.7840832](https://doi.org/10.1109/bigdata.2016.7840832).
- Introducing paper: not reported.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Manufacturing failure prediction]]
- [[Matthews correlation coefficient]]
