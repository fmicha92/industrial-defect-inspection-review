---
title: "Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets"
paper_key: "doi:10.1109/tsm.2014.2364237"
paper_type: dataset
year: 2015
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Ming-Ju Wu"
  - "Jyh-Shing R. Jang"
  - "Jui-Long Chen"
status: processed
processed_at: 2026-05-20
topics:
  - wafer map failure pattern recognition
  - wafer map similarity ranking
  - large-scale wafer map dataset
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Wafer map similarity ranking]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[Rotation and scale invariant wafer map features]]"
metrics:
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
doi: "10.1109/TSM.2014.2364237"
url: "https://doi.org/10.1109/TSM.2014.2364237"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
  - "[[Wafer map similarity ranking]]"
related_methods:
  - "[[Rotation and scale invariant wafer map features]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2015 - Wu - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets.md"
extracted_text: "paper-inbox/90_processing/text/2015 - Wu - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets.txt"
pdf: "paper-inbox/10_processed/2015 - Wu - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets.pdf"
source_file: "paper-inbox/10_processed/2015 - Wu - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets.pdf"
tags:
  - paper
  - dataset
  - wafer-map
---

# Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets

## Summary

- Introduces [[WM-811K]], reported as 811,457 real-world wafer maps and the largest publicly accessible wafer-map dataset at the time.
- Proposes compact rotation- and scale-invariant wafer-map features for failure pattern recognition and similarity ranking.
- Reports 94.63% overall accuracy for the two-stage WMFPR system on the test set.

## Paper Type

Dataset paper with a feature-based recognition and retrieval method.

## Contribution

- Claimed: The proposed features make large-scale wafer map failure pattern recognition and similarity ranking effective and efficient.
- Shown: WM-811K contains wafer maps from 46,293 lots, with approximately 20% manually labeled by domain experts.
- Shown: The feature set includes Radon-based and geometry-based attributes, computed with and without noise reduction.
- Shown: The WMFPR system reaches 94.63% overall accuracy on the 118,595-wafer test set, while WMSR retrieves the top-100 similar wafer maps from 811,457 wafer maps in 2.5 s.

## Method

The system extracts reduced wafer-map representations from Radon, regional, statistical, and linear features. A two-stage SVM first decides Pattern versus Nonpattern, then identifies the failure pattern type. Similarity ranking retrieves related wafer maps using feature similarity and salient region similarity.

## Evidence

| Evidence | Reported detail |
|---|---|
| Dataset size | 811,457 wafer maps |
| Source | Real-world fabrication; 46,293 lots |
| Labeled portion | Approximately 20% manually labeled |
| Classes | Center, Donut, Edge-local, Edge-ring, Local, Near-full, Random, Scratch, Nonpattern |
| Reported WMFPR accuracy | 94.63% overall accuracy |

## Performance Metrics

| Metric | Task | Dataset / split | Direction | Reported value | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | [[Wafer map defect classification]] | [[WM-811K]] test set of 118,595 labeled wafer maps | Higher is better | 94.63% overall accuracy | Reported for the combined two-stage WMFPR system. |
| Top-100 retrieval time | [[Wafer map similarity ranking]] | [[WM-811K]] full set of 811,457 wafer maps | Lower is better | 2.5 s | Reported for retrieving the top-100 similar wafer maps when feature vectors are already available. |
| Online classification time | [[Wafer map defect classification]] | Per wafer map | Lower is better | 0.0742 s per wafer | Feature extraction takes 0.0737 s and SVM prediction takes 0.0005 s per wafer. |

## Limitations

- The method uses hand-engineered features and SVMs, so it may not adapt to undefined patterns as directly as later semi-supervised methods.
- The extracted text does not provide dataset licensing beyond the public dataset URL.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Wafer map similarity ranking]]
- Datasets: [[WM-811K]]
- Methods: [[Rotation and scale invariant wafer map features]]
- Metrics: [[Accuracy]]
- Domains: [[Semiconductor and electronics]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2019 - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data]] | Dataset source | Uses WM-811K for final testing of DCNN classifiers trained with synthetic and small experimental data. |
| [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] | Dataset source | Uses WM-811K as the open wafer-map dataset. |
| [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] | Dataset source | Uses labeled and unlabeled WM-811K wafer maps for semi-supervised relabeling and recognition. |

## Questions

- Should WM-811K be represented as both dataset and benchmark notes later?
- Which later wafer-map papers improve on the 94.63% feature/SVM baseline under comparable splits?
