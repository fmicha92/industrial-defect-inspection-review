---
title: "Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification"
aliases:
  - "WaPIRL"
paper_key: "doi:10.1109/tsm.2020.3038165"
paper_type: research
year: 2020
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Hyungu Kahng"
  - "Seoung Bum Kim"
status: processed
processed_at: 2026-05-22
topics:
  - "wafer bin map classification"
  - "self-supervised learning"
  - "contrastive learning"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[WaPIRL]]"
  - "[[Self-supervised learning]]"
model_family:
  - "convolutional neural network"
  - "contrastive learning"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[AU-PR]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Macro F1: arithmetic mean of class-wise F1 scores, reported for downstream classification comparisons."
  - "AUPRC: area under the precision-recall curve, reported in the appendix table."
  - "Accuracy: used in prose to describe absolute improvement under scarce labels."
baselines:
  - "supervised CNN classifiers"
  - "training from scratch"
code: "reported available: https://github.com/hgkahng/WaPIRL"
data: "[[WM-811K]]"
doi: "10.1109/TSM.2020.3038165"
arxiv: "not applicable"
url: "https://doi.org/10.1109/TSM.2020.3038165"
pdf: "paper-inbox/10_processed/Research/2020 - Kahng - Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification.pdf"
source_file: "paper-inbox/10_processed/Research/2020 - Kahng - Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Kahng - Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Kahng - Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "wafer-bin-map-classification"
  - "self-supervised-learning"
---

# Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification

## Summary

- The paper proposes self-supervised pretraining for wafer bin map defect pattern classification when labeled examples are scarce.
- It pretrains a CNN with noise-contrastive estimation on unlabeled wafer bin maps, then fine-tunes with available labeled data.
- The method is evaluated on the public WM-811K wafer bin map dataset, and code is reported on GitHub.

## Contribution

- Claimed: unlabeled wafer bin maps can provide useful visual representations before supervised fine-tuning.
- Claimed: self-supervised pretraining is especially helpful when clean labeled WBM samples are limited.
- Shown: experiments on WM-811K demonstrate improved classification behavior under label scarcity.

## Method

- The pretraining stage learns representations from unlabeled WBMs using noise-contrastive estimation.
- The network is then fine-tuned on labeled wafer map defect patterns.
- The framework is named WaPIRL in the reported code repository.

## Evidence

- Dataset: WM-811K.
- Code: https://github.com/hgkahng/WaPIRL.
- WM-811K contains 811,457 samples, 172,950 labeled samples across nine predefined classes, and 638,507 unlabeled samples.
- The dominant class accounts for roughly 85% of the dataset, so the paper uses batch-level resampling for supervised fine-tuning.
- The strongest reported low-label example is VGG16 WaPIRL with rotation augmentation, which yields a 20.1% absolute accuracy increase when fine-tuned on 1% of labeled samples.
- With 100% labels, WaPIRL still reports a 2% to 5% performance gap over fully supervised baselines.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[F1-score]] | Main downstream WBM classification comparison | Macro F1, arithmetic mean of class-wise F1 scores | Higher is better | yes | Reported across AlexNet, VGG16, ResNet-18, and ResNet-50 with 1%, 5%, 10%, 25%, 50%, and 100% labeled training data; exact table values are not preserved in the extracted text. |
| [[Accuracy]] | Prose comparison under label scarcity | Absolute classification accuracy improvement | Higher is better | no | VGG16 WaPIRL with rotation augmentation gives a 20.1% absolute accuracy increase with 1% labels; WaPIRL retains a 2%-5% gap with 100% labels. |
| [[AU-PR]] | Appendix classification comparison | Area under the precision-recall curve | Higher is better | no | Reported for the same encoder and labeled-data settings; exact values are not preserved in the extracted text. |

## Limitations

- Exact accuracy values are not available in the extracted abstract region used for this note.
- The method assumes abundant unlabeled wafer bin maps are available.
- Augmentation choice matters: cropping is generally strongest, rotation helps in low-data regimes, and cropping plus shifting can degrade classification performance.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[WaPIRL]], [[Self-supervised learning]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[F1-score]], [[AU-PR]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[WM-811K]] | Shares dataset | WaPIRL evaluates wafer bin map classification on WM-811K. |
| [[Self-supervised learning]] | Shares method | The paper uses self-supervised contrastive pretraining before supervised fine-tuning. |
| [[2022 - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning]] | Shares task | Both reduce the burden of labeled wafer defect pattern data. |

## Questions

- How does performance scale with the number of labeled wafer maps?
- Does the representation help with unseen or mixed defect patterns?
