---
title: "A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation"
paper_key: "doi:10.1109/tsm.2020.3013004"
paper_type: research
year: 2020
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Tsung-Han Tsai"
  - "Yu-Chen Lee"
status: processed
processed_at: 2026-05-20
topics:
  - wafer map classification
  - data augmentation
  - lightweight neural networks
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
  - "[[Taiwan company 21-defect wafer map dataset]]"
methods:
  - "[[MobileNet]]"
  - "[[Depthwise separable convolution]]"
  - "[[Autoencoder-decoder data augmentation]]"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[FPS]]"
  - "[[G-mean]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: test classification accuracy for the wafer-map classifier."
  - "F1-score: reported for WM-811K because the None class makes accuracy overestimate performance."
  - "G-mean: reported for WM-811K as another imbalance-aware classification metric."
  - "FPS: inference throughput on Jetson Nano for 64 x 64 wafer-map sequences."
doi: "10.1109/TSM.2020.3013004"
url: "https://doi.org/10.1109/TSM.2020.3013004"
related_papers:
  - "[[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]]"
related_datasets:
  - "[[WM-811K]]"
  - "[[Taiwan company 21-defect wafer map dataset]]"
related_tasks:
  - "[[Wafer map defect classification]]"
related_methods:
  - "[[MobileNet]]"
  - "[[Depthwise separable convolution]]"
  - "[[Autoencoder-decoder data augmentation]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Tsai - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Tsai - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation.txt"
pdf: "paper-inbox/10_processed/Research/2020 - Tsai - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation.pdf"
source_file: "paper-inbox/10_processed/Research/2020 - Tsai - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation.pdf"
tags:
  - paper
  - wafer-map
  - data-augmentation
---

# A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation

## Summary

- Proposes lightweight wafer-map classifiers based on depthwise separable convolutions and MobileNet-style architectures.
- Uses CNN encoder-decoder augmentation to generate additional wafer maps while filtering generated outputs by hash similarity.
- Reports accuracy improvements from 93.95% to 97.01% on WM-811K and from 87.04% or 87.4% to 95.09% on the 21-defect dataset.

## Paper Type

Research paper. It contributes a lightweight neural architecture and data augmentation workflow.

## Contribution

- Claimed: Lightweight CNNs can reduce parameters and computation while improving wafer-map classification accuracy through augmentation.
- Shown: The paper uses [[WM-811K]] and a Taiwan company 21-defect wafer-map dataset.
- Shown: It reports 5 FPS inference on Jetson Nano for 64 x 64 input sequences.

## Method

The method trains DMC1 and DMC2 classifiers using depthwise separable convolutions, MobileNetV1/V2 ideas, and inverted residual blocks. A CNN autoencoder-decoder generates augmented wafer maps, and generated samples are kept only when hash similarity falls between 70% and 95%.

## Evidence

| Evidence | Reported detail |
|---|---|
| WM-811K result | 97.01% accuracy with augmentation, 93.95% without |
| 21-defect result | 95.09% accuracy after augmentation |
| Efficiency | Parameters reduced by 30% and 95% on the two datasets |
| Embedded deployment | 5 FPS on Jetson Nano for 64 x 64 resolution |
| Reported imbalance issue | WM-811K accuracy can be overestimated because the None class is large |

### Performance Metrics

| Metric | Dataset / model | Direction | Primary? | Reported values |
|---|---|---|---|---|
| [[Accuracy]] | [[WM-811K]] / DMC1 | Higher is better | yes | 93.95% without augmentation; 97.01% with autoencoder-decoder augmentation. |
| [[Accuracy]] | [[Taiwan company 21-defect wafer map dataset]] / DMC2 | Higher is better | yes | 87.4% before augmentation; 95.09% after augmentation. |
| [[F1-score]] | [[WM-811K]] / DMC1 | Higher is better | no | 80.66%. |
| [[G-mean]] | [[WM-811K]] / DMC1 | Higher is better | no | 81.71%. |
| [[FPS]] | Jetson Nano embedded inference | Higher is better | no | 5 FPS for 64 x 64 input sequences. |

### Efficiency

| Dataset / model | Reported efficiency change |
|---|---|
| [[WM-811K]] / DMC1 | Parameter count reduced by about 30%; calculations reduced by about 75%. |
| [[Taiwan company 21-defect wafer map dataset]] / DMC2 | Parameter count reduced by about 95%; multiply-accumulation operations reduced by about 25%. |

## Limitations

- The 21-defect dataset is built with a Taiwan company; public availability is not reported in the extracted text.
- Accuracy is partially skewed by the high proportion of None labels in WM-811K, which the paper notes.
- The autoencoder-decoder filter keeps generated maps only when hash similarity to the input lies between 70% and 95%, leaving robustness to other defect distributions unresolved.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Datasets: [[WM-811K]], [[Taiwan company 21-defect wafer map dataset]]
- Methods: [[MobileNet]], [[Depthwise separable convolution]], [[Autoencoder-decoder data augmentation]]
- Metrics: [[Accuracy]], [[F1-score]], [[G-mean]], [[FPS]]
- Domains: [[Semiconductor and electronics]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] | Dataset source | Uses WM-811K, introduced by Wu et al. |
| [[2019 - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data]] | Shares task | Both address wafer-map classification with limited or imbalanced data, using different synthetic/augmentation strategies. |
| [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] | Shares dataset | Both use WM-811K and discuss class imbalance/labeling issues. |

## Questions

- Are the DMC1/DMC2 implementations available?
- How robust is the 70%-95% hash similarity filter across new defect classes?
