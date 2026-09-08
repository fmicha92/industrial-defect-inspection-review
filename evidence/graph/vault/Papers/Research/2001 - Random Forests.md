---
title: "Random Forests"
paper_key: "sha256:3ad0f6182280e8c0f763527be85d41bce08f6e4d1de3f8c674098f0de31138ce"
paper_type: "research"
year: 2001
venue: "Machine Learning"
authors:
  - "Leo Breiman"
status: "processed"
topics:
  - "ensemble learning"
  - "classification"
  - "regression"
tasks:
  - "[[Defect classification]]"
datasets:
  - "[[UCI classification benchmarks]]"
methods:
  - "[[Random forest]]"
  - "[[Decision tree]]"
  - "[[Out-of-bag estimation]]"
metrics:
  - "[[Error rate]]"
  - "[[Mean Squared Error]]"
primary_metric: "[[Error rate]]"
code: "not reported"
data: "not reported"
source_file: "paper-inbox/10_processed/Research/2001 - Breiman - Random Forests.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2001 - Breiman - Random Forests.md"
extracted_text: "paper-inbox/90_processing/text/2001 - Breiman - Random Forests.txt"
related_methods:
  - "[[Random forest]]"
  - "[[Decision tree]]"
  - "[[Out-of-bag estimation]]"
related_datasets:
  - "[[UCI classification benchmarks]]"
---
# Random Forests

## Summary

Breiman formalizes [[Random forest|random forests]] as ensembles of tree predictors where each tree depends on an independently sampled random vector. The paper proves that classification forest generalization error converges as the number of trees grows, analyzes the trade-off between tree strength and inter-tree correlation, introduces out-of-bag monitoring, and evaluates random-feature forests for classification and regression.

## Paper Type

Research paper introducing and analyzing a classical machine learning algorithm.

## Problem

Tree ensembles can improve prediction accuracy, but the field needed a clear account of how randomized tree construction affects generalization, how to estimate error internally, and how random forests compare with boosting and single trees across classification and regression.

## Contribution

- Defines random forests as collections of tree-structured classifiers driven by independent identically distributed random vectors.
- Shows that forest generalization error converges almost surely as the number of trees increases.
- Derives an upper-bound view based on individual-tree strength and correlation.
- Uses [[Out-of-bag estimation]] to monitor error, strength, correlation, and variable importance.
- Evaluates random input selection and random linear-combination feature selection against Adaboost and one-tree baselines.

## Method

The paper studies forests grown from randomized tree construction. Forest-RI selects a random subset of input features at each node before finding the best split. Forest-RC generates random linear combinations of inputs and searches those for splits. Trees vote for the most popular class in classification; regression forests average tree outputs.

## Evidence

| Evaluation | Dataset group | Metric | Reported finding |
|---|---|---|---|
| Forest-RI classification | [[UCI classification benchmarks]] plus larger and synthetic datasets | [[Error rate]] | Random input selection compares favorably with Adaboost and substantially improves over one tree in Table 2. |
| Compute comparison | Zip-code dataset | runtime | Forest-RI with one random feature takes 4.0 minutes for 100 trees on a 250 MHz Macintosh, compared with almost three hours for Adaboost. |
| Noise robustness | 9 smaller datasets | error increase under 5% label noise | Adaboost deteriorates markedly, while random forest procedures generally show small changes. |
| High-dimensional synthetic task | 1000 inputs, 1000 training examples, 4000 test examples | [[Error rate]] | Forest-RI reports 3.0% and Forest-RC 2.8% test error, not far above the stated Bayes error rate of 1.0%. |
| Variable importance | Diabetes and votes datasets | OOB misclassification increase | Permuting variables in out-of-bag cases provides a variable-importance measure. |
| Regression forests | regression datasets | [[Mean Squared Error]] | Random-feature forests improve over bagging in the reported regression table, though results against adaptive bagging are mixed. |

## ML/DL Extraction

- Task formulation: supervised classification and regression.
- Model family: ensemble of randomized decision trees.
- Objective/loss: split criteria and tree-growing details are not fully extracted in the available source; voting and averaging are central.
- Training recipe: classification experiments often use 100 random-forest trees; Adaboost comparisons use 50 trees in many settings.
- Evaluation protocol: repeated random 10% holdouts for smaller datasets, fixed train/test splits for larger datasets, synthetic repeated runs, out-of-bag estimates for internal monitoring.
- Compute: random input selection can be much faster than all-variable tree construction when feature count is large.
- Artifacts: code not reported.

## Limitations

- The paper's empirical tables span many datasets, but the source does not provide modern cross-validation or uncertainty reporting.
- The Adaboost-as-random-forest claim is explicitly framed as a conjecture.
- Individual dataset provenance and licensing are not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]]
- Methods: [[Random forest]], [[Decision tree]], [[Out-of-bag estimation]]
- Datasets: [[UCI classification benchmarks]]
- Domains: [[General computer vision]]
- Metrics: [[Error rate]], [[Mean Squared Error]]

| Link | Relation | Rationale |
|---|---|---|
| [[Decision tree]] | Builds on | Each forest member is a tree-structured classifier or regressor. |
| [[Out-of-bag estimation]] | Shares method | OOB estimates drive error monitoring, feature count selection, and variable importance. |
| [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] | Follow-up use | That manufacturing paper uses random forest as its final classifier and feature-importance tool. |

## Questions

- How would the original strength/correlation diagnostics compare with modern random forest implementations?
- Which random forest results are sensitive to tree-growing and pruning choices not fully detailed in the extracted source?
