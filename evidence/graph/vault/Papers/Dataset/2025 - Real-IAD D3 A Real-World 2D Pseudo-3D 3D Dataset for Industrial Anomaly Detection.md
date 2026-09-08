---
title: "Real-IAD D3: A Real-World 2D/Pseudo-3D/3D Dataset for Industrial Anomaly Detection"
aliases:
  - "Real-IAD D3"
  - "Real-IAD D³"
paper_key: "sha256:f88f5bc6bb3b92ec6e8e59324f5b7bc31c71be8d3c4c1adc43ad437be0a1aac6"
paper_type: dataset
year: 2025
venue: "CVPR"
authors:
  - "Wenbing Zhu"
  - "Lidong Wang"
  - "Ziqing Zhou"
  - "Chengjie Wang"
  - "Yurui Pan"
  - "Ruoyi Zhang"
  - "Zhuhao Chen"
  - "Linjie Cheng"
  - "Bin-Bin Gao"
  - "Jiangning Zhang"
  - "Zhenye Gan"
  - "Yuxie Wang"
  - "Yulong Chen"
  - "Shuguang Qian"
  - "Mingmin Chi"
  - "Bo Peng"
  - "Lizhuang Ma"
status: processed
processed_at: 2026-05-22
topics:
  - multimodal industrial anomaly detection
  - 2D pseudo-3D 3D inspection
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Real-IAD D3]]"
  - "[[Real-IAD]]"
  - "[[MVTec3D]]"
methods:
  - "[[Photometric stereo]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "not reported"
code: "https://realiad4ad.github.io/Real-IAD_D3"
data: "Real-IAD D3 dataset reported as publicly accessible for research purposes"
doi: "not reported"
arxiv: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Photometric stereo]]"
related_datasets:
  - "[[Real-IAD D3]]"
  - "[[Real-IAD]]"
  - "[[MVTec3D]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/10_processed/2025 - Zhu - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Zhu - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Zhu - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection.txt"
artifact_status: "manual correction after false duplicate grouping"
tags:
  - paper
---

# Real-IAD D3: A Real-World 2D/Pseudo-3D/3D Dataset for Industrial Anomaly Detection

## Summary

- The increasing complexity of industrial anomaly detection (IAD) has positioned multimodal detection methods as a focal area of machine vision research. However, dedicated multimodal datasets speciﬁcally tailored for IAD remain limited. Pioneering datasets like MVTec 3D have laid essential groundwork in multimodal IAD by incorporating RGB+3D data, but still face challenges in bridging the gap with real industrial environments due to limitations in scale and resolution. To address these challenges, we introduce Real-IAD D³, a high-precision multimodal dataset that uniquely incorporates an additional pseudo3D modality generated through photometric stereo, alongside high-resolution RGB images and micrometer-level 3D point clouds. Real-IAD D³ features ﬁner defects, diverse anomalies, and greater scale across 20 categories, providing a challenging benchmark for multimodal IAD Additionally, we introduce an effective approach that integrates RGB, point cloud, and pseudo-3D depth information to leverage the complementary strengths of each modality, enhancing detection performance. Our experiments highlight the importance of these modalities in boosting detection robustness and overall IAD performance. The dataset and code are publicly accessible for research purposes at https://realiad4ad.github.io/Real-IAD D3.

## Paper Type

- Type: dataset.
- Why: The paper introduces Real-IAD D3 as a multimodal industrial anomaly detection dataset and benchmark.

## Problem

- Task: [[Industrial anomaly detection]]
- Setting: multimodal industrial visual inspection.
- Inputs: RGB images, pseudo-3D depth generated through [[Photometric stereo]], and 3D point clouds.
- Outputs: anomaly detection and localization results.
- Motivation: multimodal IAD datasets tailored to real industrial environments remain limited.
- Assumptions: not fully reported in this concise extraction.

## Contribution

- Claimed: The paper introduces [[Real-IAD D3]], a high-precision multimodal IAD dataset with RGB, pseudo-3D, and 3D modalities.
- Shown: The abstract reports finer defects, diverse anomalies, 20 categories, and experiments integrating RGB, point-cloud, and pseudo-3D depth information.
- Inferred: The dataset extends the Real-IAD line toward multimodal anomaly detection.

## Method

- Core idea: combine RGB, point-cloud, and pseudo-3D depth information for multimodal IAD.
- Architecture / algorithm: not fully reported in this concise extraction.
- Objective / loss: not reported.
- Optimization: not reported.
- Training data: [[Real-IAD D3]]
- Data pipeline: pseudo-3D modality generated through [[Photometric stereo]].
- Augmentation / synthesis: not reported.
- Inference: multimodal anomaly detection/localization.
- Complexity / deployment constraints: not reported.

## Evidence

- Dataset: [[Real-IAD D3]] covers 20 categories and includes RGB, pseudo-3D, and 3D point-cloud data according to the abstract.
- Metrics: [[AU-ROC]] and [[AU-PRO]] are recorded as likely anomaly-detection metrics, but exact reported values were not extracted in this concise pass.
- Baselines: not fully reported in this concise extraction.

## Limitations

- Stated: not fully reported in this concise extraction.
- Inferred: claims should be checked against full dataset protocol, categories, splits, and baseline tables before use as strong comparative evidence.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[Photometric stereo]], [[Unsupervised anomaly detection]]
- Datasets: [[Real-IAD D3]], [[Real-IAD]], [[MVTec3D]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] | Builds on | Real-IAD D3 extends the Real-IAD dataset direction to RGB, pseudo-3D, and 3D modalities. |
| [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] | Contrasts with | The abstract positions MVTec 3D as prior multimodal IAD groundwork and argues for larger, more realistic multimodal data. |

## Questions

- What are the exact train/test splits, category counts, and metric values for each modality combination?
- Which baseline methods are strongest in the full experimental tables?
