---
title: "Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations"
aliases:
  - "Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations"
paper_key: "sha256:e85d98e581cdcb0cf8dff2af80ab64f86fafa773198c8f1a9589e0c662040b60"
paper_type: research
year: 2022
venue: "PeerJ Computer Science"
authors:
  - "Alaa S. Al-Waisy"
  - "Dheyaa Ahmed Ibrahim"
  - "Dilovan Asaad Zebari"
  - "Shumoos Hammadi"
  - "Hussam Mohammed"
  - "Mazin Abed Mohammed"
  - "Robertas Damasevicius"
status: processed
processed_at: 2026-05-22
topics:
  - "electroluminescence images"
  - "deep feature representations"
  - "solar cell defect classification"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[ELPV Dataset]]"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Feature extraction]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "Inception-V3"
  - "ResNet50"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy, recall, precision, F1-score, and specificity are reported for binary and multiclass EL image classification."
baselines:
  - "Inception-V3 features"
  - "ResNet50 features"
benchmarks:
  - "[[ELPV Dataset]]"
code: "reported available: https://github.com/Dilovan1/Defective-solar-cell"
data: "reported available: https://github.com/zae-bayern/elpv-dataset"
doi: "10.7717/peerj-cs.992"
arxiv: "not reported"
url: "https://doi.org/10.7717/peerj-cs.992"
pdf: "paper-inbox/10_processed/Research/2022 - Al-Waisy - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations.pdf"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Feature extraction]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[ELPV Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[ELPV Dataset]]"
source_file: "paper-inbox/10_processed/Research/2022 - Al-Waisy - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Al-Waisy - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Al-Waisy - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations.txt"
artifact_status: "dataset and code reported available"
tags:
  - paper
---
# Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations

## Summary

Al-Waisy et al. propose a supervised EL-image classification system for detecting defective photovoltaic cells. The system extracts deep features from Inception-V3 and ResNet50, fuses the feature vectors with a Parallel Maximum Covariance feature-fusion method, applies dropout and data augmentation, and classifies solar cells in binary and four-class settings.

The evaluation uses [[ELPV Dataset]], a public collection of 2,624 solar-cell electroluminescence images from monocrystalline and polycrystalline PV modules. With data augmentation, the hybrid feature model reports 98.15% binary accuracy for functional versus defective cells and 95.35% multiclass accuracy for normal, mild, moderate, and severe cells.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a hybrid deep feature representation method for solar-cell defect classification.

## Problem

- Task: [[Solar cell defect detection]] and [[Defect classification]].
- Setting: electroluminescence inspection of photovoltaic modules.
- Inputs: 300 x 300 EL images of solar cells.
- Outputs: binary functional/defective labels and multiclass normal/mild/moderate/severe labels.
- Motivation: manual EL image inspection is slow, subjective, and requires expert knowledge.
- Assumptions: supervised labels are available; classes can be represented by deep feature extractors and fused features.

## Contribution

- Claimed: develops a fully automated supervised classification system for identifying solar-cell faults in EL images.
- Claimed: fuses Inception-V3 and ResNet50 feature representations into a more discriminative feature vector.
- Shown: data augmentation substantially improves performance over the same models without augmentation.
- Shown: the hybrid fused feature model outperforms individual Inception-V3 and ResNet50 features in binary and multiclass classification.

## Method

The method extracts features from Inception-V3 and ResNet50 and fuses them into a 4,096-dimensional vector using Parallel Maximum Covariance. A dropout layer with probability 0.5 is used before classification. The binary classifier uses sigmoid activation, while the multiclass classifier uses softmax activation.

Training uses pretrained Inception-V3 and ResNet50 weight configurations, then optimizes the current classification task with Adam. Data augmentation includes rotations by 90, 180, and 270 degrees, flips along x and y axes, Gaussian blur, and contrast changes.

## Evidence

### Dataset / Benchmark Setup

- Dataset: [[ELPV Dataset]].
- Size: 2,624 EL images from 44 PV modules.
- Module types: 18 monocrystalline and 26 polycrystalline modules.
- Image resolution: 300 x 300 pixels.
- Severity categories: no defect 0%, possibly normal 33%, possibly defective 66%, and defective 100%.
- Category counts: 1,508 no-defect, 295 possibly normal, 106 possibly defective, and 715 defective images.
- Binary class balance: 65% functional and 35% defective.
- Split: random 80% training and 20% testing.
- Training/test counts: 2,100 training and 524 testing images.

### Training And Runtime

- Optimizer: Adam.
- Epochs: 300.
- Mini-batch size: 16.
- Learning rate: 0.01.
- Weight decay: 0.0005.
- Momentum: 0.95.
- Dense layer: 64 neurons for the first dense layer in the reported setup.
- Hardware: Windows 10 PC, Intel Core i7-4790 CPU, 32 GB RAM.
- Training time: 30-45 minutes for Inception-V3 and ResNet50 experiments.
- Test time: about 1.01 ms per image for Inception-V3 and 1.14 ms per image for ResNet50; the abstract reports less than 1 s per image for the full system.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---|---:|---|
| Binary classification with augmentation | [[ELPV Dataset]] / functional vs defective | [[Accuracy]] | higher | Inception-V3 94.44, ResNet50 95.91 | 98.15 | Hybrid fused features. |
| Binary F1 with augmentation | [[ELPV Dataset]] / functional vs defective | [[F1-score]] | higher | Inception-V3 94.46, ResNet50 95.94 | 98.14 | Hybrid fused features. |
| Multiclass classification with augmentation | [[ELPV Dataset]] / normal, mild, moderate, severe | [[Accuracy]] | higher | Inception-V3 87.67, ResNet50 91.60 | 95.35 | Hybrid fused features. |
| Multiclass F1 with augmentation | [[ELPV Dataset]] / normal, mild, moderate, severe | [[F1-score]] | higher | Inception-V3 86.75, ResNet50 91.58 | 95.25 | Hybrid fused features. |

### Binary Classification

| Method | Features | Augmentation | Accuracy | Recall | Precision | F1-score | Specificity |
|---|---:|---|---:|---:|---:|---:|---:|
| Inception-V3 | 2,048 | no | 47.41 | 44.44 | 47.24 | 45.80 | 50.37 |
| ResNet50 | 2,048 | no | 55.19 | 52.59 | 55.47 | 53.99 | 57.78 |
| Hybrid model | 4,096 | no | 60.00 | 60.74 | 59.85 | 60.29 | 59.26 |
| Inception-V3 | 2,048 | yes | 94.44 | 94.81 | 94.12 | 94.46 | 94.07 |
| ResNet50 | 2,048 | yes | 95.91 | 96.30 | 95.59 | 95.94 | 95.52 |
| Hybrid model | 4,096 | yes | 98.15 | 98.51 | 97.78 | 98.14 | 97.79 |

### Multiclass Classification

| Method | Features | Augmentation | Accuracy | Recall | Precision | F1-score | Specificity |
|---|---:|---|---:|---:|---:|---:|---:|
| Inception-V3 | 2,048 | no | 48.39 | 48.50 | 52.50 | 48.03 | 82.50 |
| ResNet50 | 2,048 | no | 52.68 | 52.75 | 55.50 | 52.51 | 84.00 |
| Hybrid model | 4,096 | no | 61.15 | 61.75 | 66.02 | 61.03 | 87.25 |
| Inception-V3 | 2,048 | yes | 87.67 | 87.01 | 87.05 | 86.75 | 95.75 |
| ResNet50 | 2,048 | yes | 91.60 | 91.61 | 91.55 | 91.58 | 91.52 |
| Hybrid model | 4,096 | yes | 95.35 | 95.50 | 95.53 | 95.25 | 98.50 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Accuracy]] | Binary and multiclass EL image classification | Percent correct | Higher is better | yes | 98.15% binary and 95.35% multiclass for the augmented hybrid model. |
| [[F1-score]] | Binary and multiclass EL image classification | Harmonic mean of precision and recall | Higher is better | secondary | 98.14% binary and 95.25% multiclass for the augmented hybrid model. |
| [[Precision]] | Binary and multiclass EL image classification | Positive prediction correctness | Higher is better | secondary | 97.78% binary and 95.53% multiclass for the augmented hybrid model. |
| [[Recall]] | Binary and multiclass EL image classification | Positive-class coverage | Higher is better | secondary | 98.51% binary and 95.50% multiclass for the augmented hybrid model. |

## ML / DL Extraction

### Task Formulation

- Input modality: electroluminescence images of solar cells.
- Output target: binary functional/defective labels and four severity labels.
- Supervision: supervised classification.
- Objective: classify defective solar cells automatically using fused deep feature representations.

### Model And Training

- Model family: [[Deep convolutional neural network]] feature extraction.
- Architecture: Inception-V3 and ResNet50 feature extractors followed by feature fusion and dense classification layers.
- Feature dimensions: 2,048 from Inception-V3, 2,048 from ResNet50, 4,096 after fusion.
- Pretraining: pretrained Inception-V3 and ResNet50 weights are used as initialization.
- Regularization: dropout probability 0.5.
- Augmentation: rotations, flips, Gaussian blur, and contrast changes.
- Optimizer: Adam.
- Hyperparameters: 300 epochs, mini-batch 16, learning rate 0.01, weight decay 0.0005, momentum 0.95.
- Compute: CPU workstation reported; GPU not reported.

### Data

- Dataset: [[ELPV Dataset]].
- Data source: monocrystalline and polycrystalline PV module EL images.
- Labels / annotations: defect-severity labels at 0%, 33%, 66%, and 100%.
- Splits: 80% train and 20% test.
- Leakage checks: random split is reported, but module-level leakage checks are not reported.
- License: dataset images are described as CC BY NC SA 4.0 in figure captions; paper text reports data availability on GitHub.

### Evaluation

- Protocol: compare Inception-V3, ResNet50, and fused hybrid features with and without augmentation for binary and multiclass classification.
- Baselines: individual Inception-V3 features and individual ResNet50 features.
- Statistical tests: not reported.
- Failure cases: mild and severe cell images can be confused; defects similar to normal-cell texture remain challenging.

## Dataset / Benchmark Details

- Source: `https://github.com/zae-bayern/elpv-dataset`.
- Collection: high-resolution EL images extracted from PV modules.
- Size: 2,624 images.
- Classes: normal, mild, moderate, severe; binary grouping functional vs defective.
- Modalities: electroluminescence images.
- Maintenance: public GitHub dataset.

## Limitations

- EL images contain noise that requires further investigation and noise reduction while preserving texture information.
- The model should be trained and tested on more data from different environments.
- Similar texture between normal and defective cells remains challenging.
- Random train/test split is reported, but the source does not report module-level split controls or uncertainty estimates.

## Reproducibility

- Code: reported available at `https://github.com/Dilovan1/Defective-solar-cell`.
- Data: reported available at `https://github.com/zae-bayern/elpv-dataset`.
- Hyperparameters: optimizer, epochs, batch size, learning rate, weight decay, momentum, and dropout are reported.
- Random seeds: not reported.
- Environment: Windows 10, Intel Core i7-4790 CPU, 32 GB RAM.
- Checkpoints / models: not reported.
- Exact preprocessing: 300 x 300 EL images; augmentation transforms are reported.
- Artifact status: dataset and code reported available.

## Systems Details

- Hardware / software stack: Windows 10 PC with Intel Core i7-4790 CPU and 32 GB RAM.
- Latency: abstract reports less than 1 s per image; model-specific test times are about 1.01 ms and 1.14 ms for Inception-V3 and ResNet50 feature paths.
- Training time: 30-45 minutes for Inception-V3 and ResNet50 experiments.
- Deployment assumptions: image-level EL inspection with labeled training data.
- Failure modes: class overlap between normal, mild, moderate, and severe defect appearances.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[Deep convolutional neural network]], [[Feature extraction]], [[Data augmentation]]
- Datasets: [[ELPV Dataset]]
- Benchmarks: [[ELPV Dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]], [[F1-score]], [[Precision]], [[Recall]]
- Concepts: [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[Dataset of Solar Cells Defect Segmentation]] | Shares domain | Both use solar-cell defect imagery, but this paper performs image-level classification while the dataset note supports segmentation labels. |
| [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] | Shares domain and task family | Both address solar-cell defect analysis, but SIGAN focuses on segmentation augmentation while this paper focuses on fused-feature classification. |

### Connection Rationale

- [[ELPV Dataset]] is the source dataset and benchmark.
- [[Solar cells and photovoltaic]] is the domain supported by the EL/PV module setting.
- [[Accuracy]] is the primary reported metric; F1-score, precision, recall, and specificity provide supporting evaluation.

## Questions

- Does the random 80/20 split separate images by PV module, or can cells from the same module appear in both train and test?
- How robust is the fused-feature model on EL datasets from different acquisition environments?
- Would image enhancement or noise reduction improve mild/moderate defect separation?
