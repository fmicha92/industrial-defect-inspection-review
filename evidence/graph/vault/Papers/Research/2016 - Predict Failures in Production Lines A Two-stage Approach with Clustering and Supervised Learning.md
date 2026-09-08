---
title: "Predict Failures in Production Lines: A Two-stage Approach with Clustering and Supervised Learning"
aliases:
  - "Predict Failures in Production Lines"
  - "A Two-stage Approach with Clustering and Supervised Learning"
paper_key: "doi:10.1109/bigdata.2016.7840832"
paper_type: "research"
year: 2016
venue: "2016 IEEE International Conference on Big Data"
authors:
  - "Darui Zhang"
  - "Bin Xu"
  - "Jasmine Wood"
status: "processed"
topics:
  - "manufacturing failure prediction"
  - "quality control"
  - "sparse tabular data"
tasks:
  - "[[Manufacturing failure prediction]]"
datasets:
  - "[[Bosch Production Line Performance]]"
methods:
  - "[[Principal Component Analysis]]"
  - "[[K-means clustering]]"
  - "[[Random forest]]"
  - "[[Classical ML]]"
metrics:
  - "[[Matthews correlation coefficient]]"
  - "[[AU-ROC]]"
primary_metric: "[[Matthews correlation coefficient]]"
domains:
  - "[[Multi-industry anomaly detection]]"
related_datasets:
  - "[[Bosch Production Line Performance]]"
related_tasks:
  - "[[Manufacturing failure prediction]]"
related_methods:
  - "[[Principal Component Analysis]]"
  - "[[K-means clustering]]"
  - "[[Random forest]]"
url: "https://doi.org/10.1109/bigdata.2016.7840832"
doi: "10.1109/bigdata.2016.7840832"
source_file: "paper-inbox/10_processed/Research/2016 - Zhang - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2016 - Zhang - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning.md"
extracted_text: "paper-inbox/90_processing/text/2016 - Zhang - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning.txt"
processed_at: "2026-06-01"
---
# Predict Failures in Production Lines: A Two-stage Approach with Clustering and Supervised Learning

## Summary

Zhang, Xu, and Wood propose a two-stage approach for predicting failed products in the [[Bosch Production Line Performance]] Kaggle dataset. The method first clusters products into similar manufacturing-process groups using binary missingness patterns, [[Principal Component Analysis]], and [[K-means clustering]], then trains a supervised classifier separately inside each cluster. [[Random forest]] is selected as the final classifier because it gives the best trade-off between Matthews correlation coefficient, AUROC, and training time among the compared algorithms.

### Graph Hubs

- Tasks: [[Manufacturing failure prediction]]
- Datasets: [[Bosch Production Line Performance]]
- Methods: [[Principal Component Analysis]], [[K-means clustering]], [[Random forest]], [[Classical ML]]
- Metrics: [[Matthews correlation coefficient]], [[AU-ROC]]
- Domains: [[Multi-industry anomaly detection]]

## Paper Type

Research paper. The contribution is a modeling pipeline for sparse, imbalanced production-line failure prediction rather than a new dataset release.

## Problem

The paper studies binary prediction of failed products in a large anonymized production-line dataset. Each observation represents a product moving through a production line, and the target label indicates failure or pass. The dataset is difficult because it is large, highly imbalanced, sparse, anonymized, and lacks usable domain knowledge about station-level feature meaning.

## Contribution

- Converts feature missingness into process-pattern information and clusters products into six process groups.
- Deletes empty or constant features within each cluster to reduce sparsity and data size before supervised learning.
- Trains a separate classifier per cluster and reports the final two-stage random-forest performance on a held-out test set.

## Method

Only the numerical part of [[Bosch Production Line Performance]] is used. The paper excludes categorical data because it is more than 99% sparse and excludes time data because the labels of preceding data may not be available in a production-line setting.

The dataset is randomly shuffled and split into 50% training, 25% cross-validation, and 25% test. For clustering, every feature is converted to a binary indicator where `1` means a value is present and `0` means missing. PCA is applied to the 968 feature indicators; 95% of the variance is explained by 22 principal components, while two components are used for visualization. K-means is then used, and six clusters are chosen based on the inertia curve.

After clustering, all-missing and constant features are removed inside each cluster, removing 15.8% of the total dataset. Remaining missing values are filled with the special value `-1` because missingness is process-related rather than random. The supervised stage compares logistic regression, naive Bayes, decision tree, random forest, and gradient boosting families, then uses random forest classifiers for the final cluster-specific models. Feature selection keeps features until 95% cumulative random-forest feature importance is reached.

## Dataset

[[Bosch Production Line Performance]] is described with:

- 968 numerical features.
- 1,183,747 observations.
- 0.58% failed products.
- 78.5% missing values.
- Binary label: `1` for failure and `0` for pass.
- Feature naming convention `L#_S##_F####`, encoding production line, station, and feature number.

## Evidence

The paper reports six clusters:

| Cluster | Samples | Features after cluster filtering |
|---:|---:|---:|
| 0 | 230831 | 813 |
| 1 | 177562 | 882 |
| 2 | 88781 | 692 |
| 3 | 65106 | 874 |
| 4 | 17756 | 737 |
| 5 | 11837 | 697 |

Final random-forest results:

| Cluster | Max depth | Min samples leaf | MCC | AUROC |
|---:|---:|---:|---:|---:|
| 0 | 25 | 6 | 0.169 | 0.665 |
| 1 | 25 | 6 | 0.308 | 0.736 |
| 2 | 20 | 8 | 0.148 | 0.664 |
| 3 | 5 | 6 | 0.145 | 0.672 |
| 4 | 20 | 8 | 0.184 | 0.606 |
| 5 | 20 | 5 | 0.179 | 0.568 |
| Total | not applicable | not applicable | 0.211 | 0.692 |

Each random-forest classifier uses 100 estimators. MCC thresholds are optimized on the cross-validation set.

## ML/DL Extraction

- Task formulation: binary classification of production-line product failure.
- Inputs: anonymized numerical production-line features.
- Output: pass/fail product label.
- Preprocessing: missingness binarization for process clustering; PCA; K-means; cluster-local feature deletion; remaining missing values set to `-1`.
- Models compared: logistic regression, naive Bayes, decision tree, random forest, and gradient boosting.
- Final model: cluster-specific random-forest classifiers.
- Evaluation: [[Matthews correlation coefficient]], [[AU-ROC]], and training time.
- Artifact availability: data hosted by Kaggle; code is not reported.

## Limitations

- The paper uses only numerical features; categorical and time features are explicitly outside scope.
- The features are anonymized, so station-level interpretation is limited to feature naming and importance patterns.
- The total MCC of 0.211 and AUROC of 0.692 indicate useful but limited failure-prediction performance.
- Future work is needed for classifier optimization and use of categorical and timestamp data.

## Connections

### Shares Dataset

- [[Bosch Production Line Performance]] is the dataset used for the production-line failure prediction experiments.

### Shares Task

- [[Manufacturing failure prediction]] is the binary pass/fail task studied in the paper.

### Shares Method

- [[Principal Component Analysis]] reduces binary missingness indicators before process clustering.
- [[K-means clustering]] separates products into six process groups.
- [[Random forest]] is the final supervised classifier and the source of feature-importance-based feature selection.

### Shares Metric

- [[Matthews correlation coefficient]] is the primary metric because the failure label is highly imbalanced.
- [[AU-ROC]] is used as an additional robustness metric.

### Application/Domain

- [[Multi-industry anomaly detection]] is the graph-facing domain because the dataset is an anonymized production-line failure benchmark rather than a source-specific visual inspection domain.

## Source Anchors

- Paper DOI: [10.1109/bigdata.2016.7840832](https://doi.org/10.1109/bigdata.2016.7840832)
- Dataset host: [Bosch Production Line Performance](https://www.kaggle.com/c/bosch-production-line-performance)

## Questions

- How much performance is left on the table by excluding timestamp and categorical features?
- Which stations correspond to the high-importance anonymized features in the random-forest models?
