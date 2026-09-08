---
title: "Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data"
paper_key: "doi:10.1109/ent47717.2019.9030550"
paper_type: research
year: 2019
venue: "IEEE conference paper"
authors:
  - "Kudrov Maksim"
  - "Bukharov Kirill"
  - "Zakharov Eduard"
  - "Grishin Nikita"
  - "Bazzaev Aleksandr"
  - "Lozhkina Arina"
  - "Semenkin Vladislav"
  - "Makhotkin Daniil"
  - "Krivoshein Nikolay"
status: processed
processed_at: 2026-05-20
topics:
  - wafer map defect classification
  - small data
  - synthetic wafer maps
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Parametric wafer map synthesis]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: class-wise or final-test classification correctness on WM-811K."
  - "Precision, recall, and F1-score: per-pattern classification metrics for ResNet-50 at Rls = 0.05."
doi: "10.1109/ent47717.2019.9030550"
url: "https://doi.org/10.1109/ent47717.2019.9030550"
related_papers:
  - "[[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]]"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
related_methods:
  - "[[Parametric wafer map synthesis]]"
  - "[[Deep convolutional neural network]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2019 - Kudrov - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data.md"
extracted_text: "paper-inbox/90_processing/text/2019 - Kudrov - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data.txt"
pdf: "paper-inbox/10_processed/Research/2019 - Kudrov - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data.pdf"
source_file: "paper-inbox/10_processed/Research/2019 - Kudrov - Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data.pdf"
tags:
  - paper
  - wafer-map
  - small-data
---

# Classification of Wafer Maps Defect Based on Deep Learning Methods With Small Amount of Data

## Summary

- Proposes a DCNN-based wafer map defect classifier trained with a composite dataset of synthetic wafer maps plus a small number of experimental examples.
- Uses pretraining on synthetic data before training/validation on the composite dataset.
- Validates on [[WM-811K]] and reports ResNet-50 reaching 87.8% accuracy at the selected labeled-to-synthetic ratio.

## Paper Type

Research paper focused on learning under limited labeled experimental data.

## Contribution

- Claimed: A composite dataset can compensate for small experimental labeled wafer-map data.
- Shown: Synthetic wafer-map patterns are generated from parametric descriptions and regularized to visually approximate experimental examples.
- Shown: Pretraining on synthetic data improves resulting accuracy by 1% to 4% depending on architecture.

## Method

The method creates synthetic defect patterns from manufacturing pattern descriptions, mixes them with a small experimental set, pretrains DCNNs on synthetic data, and compares VGG, ResNet, and MobileNet architectures using WM-811K for final testing.

## Evidence

| Evidence | Reported detail |
|---|---|
| Experimental data amount | About 20 examples in the abstract; later 10 to 120 examples per class are discussed |
| Final benchmark | WM-811K |
| Best reported model | ResNet-50 |
| Best reported accuracy | 87.8% on WM-811K at Rls = 0.05 |
| Metrics | Accuracy, recall, precision, F1-score |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Accuracy]] | Final wafer-map defect classification on [[WM-811K]] | Fraction correct | Higher is better | yes | With pretraining at Rls = 0.05: VGG19 0.8481, ResNet34 0.8539, ResNet50 0.8784, MobileNetV2 0.8191. Without pretraining: VGG19 0.8326, ResNet34 0.8274, ResNet50 0.8625, MobileNetV2 0.7822. |
| [[Accuracy]] | ResNet-50 class-wise results on [[WM-811K]] | Per-pattern accuracy | Higher is better | no | Center 0.9131, Donut 0.9328, Loc 0.7170, Scratch 0.7421, Edge-Ring 0.9601, Edge-Loc 0.8273. |
| [[Precision]] | ResNet-50 class-wise results on [[WM-811K]] | Per-pattern precision | Higher is better | no | Center 0.7837, Donut 0.8287, Loc 0.7380, Scratch 0.4677, Edge-Ring 0.9878, Edge-Loc 0.7296. |
| [[Recall]] | ResNet-50 class-wise results on [[WM-811K]] | Per-pattern recall | Higher is better | no | Center 0.9236, Donut 0.8589, Loc 0.6078, Scratch 0.8635, Edge-Ring 0.9412, Edge-Loc 0.7491. |
| [[F1-score]] | ResNet-50 class-wise results on [[WM-811K]] | Per-pattern F1 score | Higher is better | no | Center 0.8479, Donut 0.8436, Loc 0.6667, Scratch 0.6068, Edge-Ring 0.9639, Edge-Loc 0.7401. |

### Efficiency

| Model | Throughput |
|---|---:|
| VGG19 | 49.2 images/sec |
| ResNet34 | 84.1 images/sec |
| ResNet50 | 58.4 images/sec |
| MobileNetV2 | 66.8 images/sec |

## Limitations

- The synthetic generation is tuned to described wafer defect classes and may not cover undefined or mixed defect types.
- The paper treats WM-811K as the isolated final test, but the training data are partly synthetic and partly small experimental data, so production transfer is not fully established.
- Scratch and Loc classes remain comparatively weak for ResNet-50 at Rls = 0.05, with 0.4677 precision for Scratch and 0.6078 recall for Loc.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Datasets: [[WM-811K]]
- Methods: [[Parametric wafer map synthesis]], [[Deep convolutional neural network]], [[Synthetic data generation]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]
- Domains: [[Semiconductor and electronics]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] | Builds on dataset | Uses WM-811K, introduced by Wu et al., as the open final test set. |
| [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] | Shares task | Both classify wafer maps with deep models and address limited or imbalanced data, but Tsai and Lee use autoencoder-decoder augmentation and lightweight CNNs. |

## Questions

- How were the roughly 20 experimental examples selected?
- Does the synthetic generator cover multi-pattern wafer maps?
