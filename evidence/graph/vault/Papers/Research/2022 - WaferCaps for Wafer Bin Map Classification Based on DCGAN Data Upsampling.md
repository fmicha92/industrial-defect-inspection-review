---
title: "An Improved Capsule Network (WaferCaps) for Wafer Bin Map Classification Based on DCGAN Data Upsampling"
aliases:
  - "WaferCaps"
paper_key: "doi:10.1109/tsm.2021.3134625"
paper_type: research
year: 2022
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Abd Al Rahman M. Abu Ebayyeh"
  - "Sebelan Danishvar"
  - "Alireza Mousavi"
status: processed
processed_at: 2026-06-11
topics:
  - "wafer bin map classification"
  - "DCGAN data upsampling"
  - "capsule networks"
  - "class imbalance"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[WaferCaps]]"
  - "[[DCGAN wafer map augmentation]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
baselines:
  - "Original CapsNet"
  - "CNN"
  - "MLP"
doi: "10.1109/TSM.2021.3134625"
url: "https://doi.org/10.1109/TSM.2021.3134625"
data: "[[WM-811K]]"
code: "not reported"
related_methods:
  - "[[WaferCaps]]"
  - "[[DCGAN wafer map augmentation]]"
  - "[[DCGAN]]"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
source_file: "paper-inbox/10_processed/Research/2022 - Abu Ebayyeh - An Improved Capsule Network (WaferCaps) for Wafer Bin Map Classification Based on DCGAN Data Upsampling.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Abu Ebayyeh - An Improved Capsule Network (WaferCaps) for Wafer Bin Map Classification Based on DCGAN Data Upsampling.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Abu Ebayyeh - An Improved Capsule Network (WaferCaps) for Wafer Bin Map Classification Based on DCGAN Data Upsampling.txt"
artifact_status: "code not reported"
tags:
  - paper
---
# An Improved Capsule Network (WaferCaps) for Wafer Bin Map Classification Based on DCGAN Data Upsampling

## Summary

The paper proposes [[WaferCaps]], a capsule-network classifier for wafer bin maps, and pairs it with [[DCGAN wafer map augmentation]] to upsample imbalanced [[WM-811K]] defect classes. The key result is a large test-accuracy gain when WaferCaps is trained on a mixed dataset of original and DCGAN-generated wafer maps instead of original data only.

## Paper Type

- Type: research.
- Why: The paper proposes a model architecture and a synthetic data upsampling workflow, then evaluates classification performance.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: class-imbalanced wafer bin maps from [[WM-811K]].
- Motivation: minority wafer defect patterns have too few labeled examples for reliable deep learning.

## Contribution

- Claimed: DCGAN upsampling can balance wafer-map defect classes and improve classifier accuracy.
- Claimed: WaferCaps adapts capsule networks to 64 x 64 wafer maps through added convolutional layers, dropout, larger kernels, and a modified input size.
- Shown: WaferCaps test accuracy improves from 78.2% with original data only to 91.41% with mixed original + DCGAN data.

## Method

- Synthetic data: one DCGAN per defect class generates 64 x 64 wafer maps from a 100-dimensional Gaussian vector.
- Post-processing: generated maps are filtered using Pearson correlation coefficient threshold 0.92; about 50% of DCGAN outputs are accepted.
- Scratch class exception: DCGAN failed to generate scratch patterns well, so the authors isolate scratch patterns and rotate them to create additional samples.
- Class balancing: each of eight defect classes is upsampled to 10,000 samples including originals.
- Classifier: [[WaferCaps]], a capsule network with 64 x 64 input, three convolutional layers, dropout, 15 x 15 kernels, PrimaryCaps, and DigitCaps.

## Data

- Dataset: [[WM-811K]] labeled and patterned wafer bin maps.
- Classes: center, donut, edge-loc, edge-ring, loc, near-full, scratch, and random.
- Original dataset: 17,804 training maps, 4,333 validation maps, and 2,165 test maps.
- Mixed dataset: 63,200 training maps and 15,600 validation maps; the same original test set is used for comparison.

## Evidence

### Baseline vs Synthetic Data

| Model / setting | Baseline result | Result after DCGAN upsampling | Metric | Delta |
|---|---:|---:|---|---:|
| WaferCaps on original vs mixed data | 78.2 | 91.41 | test accuracy | +13.21 |
| WaferCaps original dataset | 99.89 / 88.92 / 78.2 | not applicable | train / validation / test accuracy | not applicable |
| WaferCaps mixed dataset | not applicable | 99.59 / 97.53 / 91.41 | train / validation / test accuracy | not applicable |

### Architecture Ablations

| Change | Test accuracy |
|---|---:|
| Original CapsNet image size 28 x 28 | 80.6 |
| Image size 64 x 64 | 82.9 |
| + dropout | 84.5 |
| + two convolutional layers | 85.8 |
| + three convolutional layers | 88.4 |
| Kernel size 15 x 15 | 91.4 |

## ML / DL Extraction

- Task formulation: eight-class wafer bin map defect classification.
- Input: 64 x 64 grayscale wafer maps.
- Model: [[WaferCaps]] capsule network.
- Generator: [[DCGAN]] with generator/discriminator adversarial training.
- Losses: BCE for DCGAN discriminator; capsule margin loss for WaferCaps.
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], and [[F1-score]].
- Code: not reported.

## Limitations

- DCGAN did not generate scratch defects well; scratch required a separate pattern-isolation and rotation workaround.
- Synthetic data quality depends on Pearson filtering and manual threshold choice.
- Future work: optimize DCGAN for scratch patterns and optimize per-class WaferCaps classification.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Defect classification]]
- Methods: [[WaferCaps]], [[DCGAN wafer map augmentation]], [[DCGAN]], [[Data augmentation]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Relationship Notes

- Shares dataset: [[WM-811K]].
- Shares task: [[Wafer map defect classification]].
- Shares method: [[DCGAN wafer map augmentation]], [[DCGAN]], and [[Data augmentation]].
- Application/domain: [[Semiconductor and electronics]].

## Questions

- How do CNN, MLP, and original CapsNet exact test scores compare in Tables VI and VII where OCR did not preserve the numeric table cells?
- Does Pearson filtering remove diversity from generated wafer maps?
- Can one generator model handle all classes without the scratch-class special case?
