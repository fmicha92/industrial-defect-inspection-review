---
title: "Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification: Yield Enhancement"
aliases:
  - "Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification"
paper_key: "sha256:e6d97def995c62d0b1f55a748532dc460faeb718f73f36f24325368063932a24"
paper_type: research
year: 2020
venue: "31st Annual SEMI Advanced Semiconductor Manufacturing Conference"
authors:
  - "YongSung Ji"
  - "Jee-Hyong Lee"
status: processed
processed_at: 2026-06-11
topics:
  - "wafer map defect classification"
  - "GAN augmentation"
  - "CNN"
  - "yield enhancement"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[DCGAN wafer map augmentation]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
metrics:
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
baselines:
  - "CNN trained on original dataset DS0"
  - "classic augmentation dataset DS2"
doi: "10.1109/ASMC49169.2020.9185193"
openalex: "W3083472197"
url: "https://doi.org/10.1109/ASMC49169.2020.9185193"
data: "[[WM-811K]]"
code: "not reported"
related_methods:
  - "[[DCGAN wafer map augmentation]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
source_file: "paper-inbox/10_processed/Research/2020 - Ji - Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification Yield Enhancement.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Ji - Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification Yield Enhancement.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Ji - Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification Yield Enhancement.txt"
artifact_status: "code not reported"
tags:
  - paper
---
# Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification: Yield Enhancement

## Summary

The paper uses GAN-generated wafer maps to improve a CNN classifier on an imbalanced [[WM-811K]] subset. It compares the original dataset, GAN-generated augmentation, conventional augmentation, and combined augmentation variants. The best reported setting improves CNN accuracy from 97.0% on the original dataset to 98.3% using targeted GAN augmentation for weak classes.

## Paper Type

- Type: research.
- Why: The paper proposes a GAN-based augmentation workflow and evaluates CNN classification accuracy across dataset variants.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: semiconductor wafer maps with scarce minority defect classes.
- Motivation: CNN classifier performance degrades for defect classes with few training examples, especially scratch in this paper.

## Contribution

- Claimed: GAN-generated wafer maps supplement scarce classes and improve CNN wafer-map classification.
- Shown: GAN augmentation improves total accuracy from 97.0% to 98.0%, outperforms classic augmentation at 97.5%, and reaches 98.3% when targeted to low-accuracy classes.

## Method

- Dataset preprocessing: convert wafer maps to 64 x 64 images, white for fail chips and black for pass/other chips; remove unclear, unlabeled, and extreme-resolution maps.
- Classifier: CNN with three convolutional layers, max-pooling, ReLU, a 256-node fully connected layer, and softmax output.
- Training: 100 epochs, learning rate 0.001, batch size 64.
- GAN augmentation: DCGAN-style generator produces additional maps for scarce classes.
- Classic augmentation baseline: left/right inversion, top/bottom inversion, and rotation.

## Data

- Dataset: [[WM-811K]].
- Processed subset: 8,560 wafer maps across 10 classes.
- Train/test totals: 7,560 training and 1,000 test maps.
- Classes: None, Location, Edge Location, Center, Edge Ring, Scratch, Random, Near Full, Donut, and Horizontal Stripe.
- Low-data classes: Location, Edge Location, Center, Scratch, Random, Near Full, and Donut.

## Evidence

### Baseline vs Augmentation

| Dataset variant | Training samples | Test samples | Accuracy |
|---|---:|---:|---:|
| DS0 original dataset | 7,560 | 1,000 | 97.0% |
| DS1 DCGAN generated maps added | 8,960 | 1,000 | 98.0% |
| DS2 classic augmentation | 8,960 | 1,000 | 97.5% |
| DS3 classic augmentation used before GAN generation | 8,960 | 1,000 | 98.2% |
| DS4 targeted GAN addition for low-accuracy classes | 8,160 | 1,000 | 98.3% |

### Per-Class Improvement Example

| Class | DS0 accuracy | DS4 accuracy | Delta |
|---|---:|---:|---:|
| Scratch | 71.7% | 88.3% | +16.6 |
| Location | 93.3% | 96.7% | +3.4 |
| None | 99.2% | 100.0% | +0.8 |

## ML / DL Extraction

- Task formulation: 10-class wafer map classification.
- Model: CNN classifier.
- Synthetic data: GAN-generated wafer map images.
- Evaluation protocol: fixed 1,000-sample test set across DS0-DS4.
- Metric: [[Accuracy]].
- Code: not reported.

## Limitations

- The paper reports accuracy only; precision, recall, and F-score are not reported.
- GAN architecture details are high level in the extracted text.
- The experiment uses a selected/preprocessed subset of WM-811K, not the full labeled corpus.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Defect classification]]
- Methods: [[DCGAN wafer map augmentation]], [[GAN]], [[Data augmentation]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]]

### Relationship Notes

- Shares dataset: [[WM-811K]].
- Shares task: [[Wafer map defect classification]].
- Shares method: [[DCGAN wafer map augmentation]], [[GAN]], and [[Data augmentation]].
- Application/domain: [[Semiconductor and electronics]].

## Questions

- How were GAN outputs filtered or quality-controlled before insertion?
- Would targeted GAN augmentation still dominate if per-class recall or macro-F1 were used instead of overall accuracy?
- Are the exact train/test files or random splits available?
