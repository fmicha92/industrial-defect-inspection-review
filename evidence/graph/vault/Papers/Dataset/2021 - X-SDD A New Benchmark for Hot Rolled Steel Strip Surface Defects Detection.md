---
title: "X-SDD: A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection"
aliases:
  - "X-SDD: A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection"
paper_key: "doi:10.3390/sym13040706"
paper_type: dataset
year: 2021
venue: "Symmetry"
authors:
  - "Xinglong Feng"
  - "Xianwen Gao"
  - "Ling Luo"
affiliations:
  - "Northeastern University"
status: processed
processed_at: 2026-06-11
topics:
  - "hot rolled steel strip defect classification"
  - "surface defect dataset"
  - "RepVGG"
tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[X-SDD]]"
  - "[[NEU-CLS]]"
methods:
  - "[[RepVGG+SA]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[RepVGG+SA]]"
optimizers:
  - "[[Adam]]"
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Macro-recall, macro-precision, and macro-F1 are computed by averaging per-class binary recall, precision, and F1 across seven classes."
baselines:
  - "EspNet-v2"
  - "GhostNet"
  - "ShuffleNet"
  - "SqueezeNet"
  - "Xception"
  - "VGG16"
  - "ResNet50"
  - "ResNet101"
  - "ResNet152"
  - "RepVGG_B1g2"
  - "RepVGG_B3g4"
benchmarks:
  - "[[X-SDD]]"
code: "https://github.com/Fighter20092392/X-SDD-A-New-benchmark"
data: "https://github.com/Fighter20092392/X-SDD-A-New-benchmark"
doi: "10.3390/sym13040706"
url: "https://doi.org/10.3390/sym13040706"
pdf: "paper-inbox/10_processed/Dataset/2021 - Feng - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection.pdf"
related_papers:
  - "[[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]"
  - "[[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]]"
related_methods:
  - "[[RepVGG+SA]]"
related_datasets:
  - "[[X-SDD]]"
  - "[[NEU-CLS]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
related_benchmarks:
  - "[[X-SDD]]"
source_file: "paper-inbox/10_processed/Dataset/2021 - Feng - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Feng - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Feng - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection.txt"
artifact_status: "data and code repository reported"
tags:
  - paper
---
# X-SDD: A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection

## Summary

The paper introduces [[X-SDD]], a 1,360-image hot-rolled steel strip surface defect classification dataset with seven classes and pronounced class imbalance. It evaluates multiple CNN classifiers on X-SDD and proposes [[RepVGG+SA]], a RepVGG_B3g4 classifier with spatial attention, which reports the best overall classification metrics in the paper's experiments.

## Paper Type

- Type: dataset paper.
- Why: The main contribution is the release and benchmarking of X-SDD, with classifier experiments used to validate the dataset and provide baselines.

## Problem

- Task: [[Defect classification]] for hot-rolled steel strip surface defects.
- Setting: [[Metal inspection]] in a steel-strip production environment.
- Inputs: 128 x 128 three-channel JPG defect images.
- Outputs: one of seven hot-rolled steel strip defect classes.
- Motivation: existing industrial inspection systems classify some uncommon strip defects inaccurately, while public hot-rolled steel defect datasets are limited.
- Assumption: a dataset with more defect types and realistic class imbalance better reflects production defect classification than a balanced six-class benchmark alone.

## Contribution

- Introduces [[X-SDD]], a hot-rolled strip steel surface defect dataset with seven defect types and 1,360 images.
- Benchmarks multiple CNN classifiers on X-SDD, including EspNet-v2, GhostNet, ShuffleNet, SqueezeNet, Xception, VGG16, ResNet variants, and RepVGG variants.
- Proposes RepVGG_B3g4 with spatial attention, reporting 95.10% accuracy, 93.92% macro-recall, 95.16% macro-precision, and 93.25% macro-F1.

## Method

- Dataset construction: images were collected from a hot-rolled steel strip production field using a surface inspection setup similar to the machine-vision system described in the paper.
- X-SDD images: 128 x 128 pixels, three-channel JPG.
- Classifier: RepVGG_B3g4 plus a spatial attention module.
- Spatial attention: average pooling and max pooling across channels are concatenated, passed through a 7 x 7 convolution, and activated with sigmoid to form a spatial attention map.
- Training setup: images resized to 224 x 224; batch size 10; 100 epochs; learning rate 0.0001; Adam optimizer; PyTorch on Anaconda.
- Hardware: single NVIDIA RTX2080S GPU, Intel Core i7-9700 CPU, 16 GB RAM, Windows 10.

## Evidence

### Experimental Setup

- Dataset: [[X-SDD]].
- Split: 70% training and 30% testing, reported as 952 train images and 408 test images.
- Baselines: EspNet-v2, GhostNet, ShuffleNet, SqueezeNet, Xception, VGG16, ResNet50, ResNet101, ResNet152, RepVGG_B1g2, and RepVGG_B3g4.
- Metrics: [[Accuracy]], macro-[[Recall]], macro-[[Precision]], and macro-[[F1-score]].

### Main Results

| Model | Accuracy | Macro-recall | Macro-precision | Macro-F1 |
|---|---:|---:|---:|---:|
| EspNet-v2 | 89.95% | 84.19% | 88.28% | 84.28% |
| GhostNet | 88.72% | 87.87% | 86.93% | 87.07% |
| ShuffleNet | 87.50% | 85.84% | 84.83% | 84.68% |
| SqueezeNet | 91.42% | 83.21% | 90.36% | 84.15% |
| Xception | 90.44% | 87.39% | 89.41% | 88.25% |
| VGG16 | 92.65% | 90.46% | 91.70% | 90.92% |
| ResNet50 | 93.87% | 89.41% | 93.45% | 90.02% |
| ResNet101 | 87.01% | 88.30% | 88.18% | 87.05% |
| ResNet152 | 92.16% | 89.41% | 91.41% | 89.92% |
| RepVGG_B1g2 | 88.97% | 82.04% | 90.79% | 81.58% |
| RepVGG_B3g4 | 91.67% | 85.28% | 88.46% | 84.94% |
| RepVGG_B3g4+SA | 95.10% | 93.92% | 95.16% | 93.25% |

### Per-Class RepVGG+SA Results

| Defect class | Correct | Error | Total | Accuracy |
|---|---:|---:|---:|---:|
| Oxide scale of plate system | 15 | 4 | 19 | 78.95% |
| Red iron sheet | 112 | 7 | 119 | 94.12% |
| Scratches | 39 | 1 | 40 | 97.50% |
| Inclusion | 60 | 1 | 61 | 98.36% |
| Finishing roll printing | 71 | 0 | 71 | 100% |
| Iron sheet ash | 31 | 6 | 37 | 83.78% |
| Oxide scale of temperature system | 60 | 1 | 61 | 98.36% |
| Total | 388 | 20 | 408 | 95.10% |

### Model Complexity

- RepVGG_B3g4+SA: 83.825 M parameters and 17.892 G MACs.
- EspNet-v2 comparison: 0.627 M parameters and 0.090 G MACs.
- The paper identifies RepVGG+SA as accurate but computationally costly.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB hot-rolled steel strip defect image.
- Output target: seven-class defect label.
- Supervision: supervised image classification.
- Objective: not reported.

### Model And Training

- Model family: CNN classifier.
- Architecture: RepVGG_B3g4 with spatial attention.
- Optimizer: [[Adam]].
- Learning rate: 0.0001.
- Batch size: 10.
- Epochs: 100.
- Image size: 224 x 224 after resizing.
- Hardware: NVIDIA RTX2080S, Intel Core i7-9700, 16 GB RAM.
- Environment: Windows 10, PyTorch, Anaconda.
- Seeds: not reported.

### Data

- Dataset: [[X-SDD]].
- Dataset size: 1,360 images.
- Classes: inclusion, red iron sheet, iron sheet ash, scratches, oxide scale of plate system, finishing roll printing, oxide scale of temperature system.
- Split: 952 train, 408 test.
- License: not reported in the paper.
- Availability: the paper reports a data URL at https://github.com/Fighter20092392/X-SDD-A-New-benchmark.

### Evaluation

- Protocol: compare multiple CNN classifiers on the same X-SDD train/test split.
- Primary metric: accuracy.
- Secondary metrics: macro-recall, macro-precision, macro-F1.
- Statistical tests: not reported.
- Failure cases: oxide scale of plate system has the lowest class accuracy, attributed to small sample count and similarity to inclusion.

## Dataset / Benchmark Details

- X-SDD contains seven hot-rolled strip steel defect categories.
- Class imbalance is intentional and reflects different defect frequencies in production; the largest class has more than six times the samples of the smallest class.
- Compared with [[NEU-CLS]], X-SDD has one additional class and several defect types that NEU-CLS does not contain.
- The paper frames X-SDD as a supplement to NEU-CLS rather than a replacement.

## Limitations

- The proposed RepVGG+SA model is computationally heavy: 83.825 M parameters and 17.892 G MACs.
- Oxide scale of plate system is difficult for the model, with 78.95% class accuracy.
- The paper does not report random seeds, repeated-run statistics, confidence intervals, or a separate validation set.
- Dataset license is not reported in the paper.

## Reproducibility

- Data/code URL: https://github.com/Fighter20092392/X-SDD-A-New-benchmark.
- Hyperparameters: batch size 10, 100 epochs, learning rate 0.0001, Adam optimizer, 224 x 224 image size.
- Random seeds: not reported.
- Environment: Windows 10, PyTorch, Anaconda.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Metallic surface defect detection]]
- Methods: [[RepVGG+SA]]
- Datasets: [[X-SDD]], [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]], [[Recall]], [[Precision]], [[F1-score]]

### Builds On

- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]: introduces [[NEU-CLS]], the six-class steel strip defect dataset used as the main comparison point.

### Shares Dataset

- [[X-SDD]]: introduced and benchmarked by this paper.
- [[NEU-CLS]]: compared as the existing six-class steel strip defect dataset.

### Shares Method

- [[RepVGG+SA]]: proposed classifier combining RepVGG_B3g4 with spatial attention.

### Shares Task

- [[Defect classification]]: seven-class image-level defect recognition.
- [[Metallic surface defect detection]]: hot-rolled strip steel surface defect classification.

### Shares Metric

- [[Accuracy]]: RepVGG+SA reports 95.10% test accuracy.
- [[Recall]]: RepVGG+SA reports 93.92% macro-recall.
- [[Precision]]: RepVGG+SA reports 95.16% macro-precision.
- [[F1-score]]: RepVGG+SA reports 93.25% macro-F1.

### Application / Domain

- [[Metal inspection]]: the dataset and task are hot-rolled steel strip surface inspection.

### Follow-up Reading

- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]]: uses X-SDD in later bounding-box detection and augmentation experiments.

## Questions

- What exact labeling workflow and quality-control procedure were used for X-SDD class labels?
- Are the GitHub and Kaggle releases identical, or does one include additional detection annotations?
- How stable are the reported classifier rankings across repeated random splits?
