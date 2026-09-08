---
title: "A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classification"
aliases:
  - "IncepViTH-Net for Solar Panel Fault Detection"
paper_key: "doi:10.1016/j.compeleceng.2025.110819"
paper_type: "research"
year: 2026
venue: "Computers and Electrical Engineering"
authors:
  - "Gangu Dharmaraju"
  - "Manoj Kumar Jena"
  - "Venkataramana Attada"
status: "processed"
topics:
  - "solar panel fault detection"
  - "solar panel fault classification"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PV Panel Defect Dataset]]"
methods:
  - "[[IncepViTH-Net]]"
  - "[[U-Net]]"
  - "[[Vision Transformer]]"
  - "[[Computer Vision Models]]"
model_family:
  - "[[Computer Vision Models]]"
  - "[[Transformers]]"
architectures:
  - "[[IncepViTH-Net]]"
  - "[[U-Net]]"
  - "[[Vision Transformer]]"
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
  - "[[Specificity]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + TN + FP + FN)"
  - "TPR: TP / (TP + FN)"
  - "TNR: TN / (TN + FP)"
baselines:
  - "SPF-Net"
  - "PV-YOLO"
  - "Coupled UDenseNet"
  - "RMVDM"
benchmarks:
  - "not reported"
code: "not reported"
data: "https://www.kaggle.com/datasets/pythonafroz/solar-panel-clean-and-faulty-images"
doi: "10.1016/j.compeleceng.2025.110819"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.compeleceng.2025.110819"
pdf: "paper-inbox/10_processed/Research/2026 - Dharmaraju - A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classif....pdf"
source_file: "paper-inbox/10_processed/Research/2026 - Dharmaraju - A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classif....pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2026 - Dharmaraju - A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classif....md"
extracted_text: "paper-inbox/90_processing/text/2026 - Dharmaraju - A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classif....txt"
related_papers:
  - "[[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]]"
  - "[[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]"
  - "[[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]]"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[IncepViTH-Net]]"
  - "[[U-Net]]"
  - "[[Vision Transformer]]"
related_datasets:
  - "[[PV Panel Defect Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "not reported"
processed_at: "2026-05-29"
---
# A Deep Learning Model with Inception Vision Transformer and Harmonic Fusion Network for Solar Panel Fault Detection and Classification

## Summary

The paper proposes [[IncepViTH-Net]], a hybrid model for solar panel fault detection and classification. The pipeline enhances panel images with pixel brightness correction, segments affected regions with [[U-Net]], extracts CNN, histogram, angular second moment, and inverse difference moment features, then fuses InceptionV3-style convolutional features with [[Vision Transformer]] outputs through harmonic analysis.

The reported experiment uses a Kaggle clean/faulty solar-panel subset represented here by [[PV Panel Defect Dataset]]. The proposed model reaches 96.988% accuracy, 97.988% TPR, and 96.577% TNR at K value 8, outperforming SPF-Net, PV-YOLO, Coupled UDenseNet, and RMVDM in the paper's comparison.

## Paper Type

Research paper. It introduces a new model architecture and reports comparative experiments on a public solar panel image dataset.

## Problem

The paper addresses automated [[Solar cell defect detection]] and [[Defect classification]] for photovoltaic panel surface conditions. It frames manual inspection, rule-based approaches, and conventional deep models as limited by scalability, lighting variability, small or subtle defects, labeled-data requirements, and limited ability to classify exact fault types.

## Contribution

- Proposes [[IncepViTH-Net]], combining InceptionV3-Net, [[Vision Transformer]], and harmonic fusion for solar panel fault detection and classification.
- Uses pixel brightness correction and [[U-Net]] segmentation before classification so the model focuses on affected panel regions.
- Evaluates clean and faulty panel classes including bird-drop, clean, dusty, electrical damage, physical damage, and snow-covered panels.

## Method

The method has five stages:

1. Solar panel images are acquired from a Kaggle clean/faulty solar-panel subset represented by [[PV Panel Defect Dataset]].
2. Pixel brightness correction converts and adjusts images to improve brightness and contrast.
3. [[U-Net]] segments affected solar panel regions from denoised images.
4. CNN features, histogram features, angular second moment, and inverse difference moment are extracted from segmented images.
5. [[IncepViTH-Net]] fuses an InceptionV3-Net branch and a [[Vision Transformer]] branch with harmonic analysis to produce classified labels.

The output classes are clean, dusty, bird drop, electric damage, snow-covered, and physical damage.

## Evidence

### Dataset

The paper reports 907 images from the Kaggle clean/faulty solar-panel subset:

| Class | Images |
|---|---:|
| Bird-drop | 199 |
| Clean | 202 |
| Dusty | 220 |
| Electrical damage | 98 |
| Physical damage | 66 |
| Snow-covered | 122 |

The dataset source is reported as Kaggle: https://www.kaggle.com/datasets/pythonafroz/solar-panel-clean-and-faulty-images.

### Experimental Setup

| Setting | Value |
|---|---|
| Tooling | Python |
| Epochs | 80 |
| Optimizer | Adam |
| Learning rate | 0.01 |
| beta1 | 0.9 |
| beta2 | 0.9999 |
| epsilon | 0.00001 |
| Batch size | 32 |
| Dropout | 0.2 |
| Kernel size | 3 x 3 |
| Activation | softmax |
| Loss | categorical cross-entropy |

### Performance Metrics

| Metric | Task context | Definition | Direction | Primary | Reported value |
|---|---|---|---|---|---|
| [[Accuracy]] | solar panel fault classification | `(TP + TN) / (TP + TN + FP + FN)` | higher | yes | 96.988% at K value 8 |
| [[Recall]] | reported as TPR | `TP / (TP + FN)` | higher | no | 97.988% at K value 8 |
| [[Specificity]] | reported as TNR | `TN / (TN + FP)` | higher | no | 96.577% at K value 8 |

### Comparative Results

| Setting | Metric | SPF-Net | PV-YOLO | Coupled UDenseNet | RMVDM | IncepViTH-Net |
|---|---|---:|---:|---:|---:|---:|
| 90% learning data | Accuracy | 86.889 | 87.988 | 89.988 | 92.988 | 96.777 |
| 90% learning data | TPR | 87.990 | 89.999 | 91.999 | 94.999 | 97.479 |
| 90% learning data | TNR | 85.879 | 86.555 | 88.999 | 93.999 | 96.010 |
| K value 8 | Accuracy | 87.888 | 89.998 | 92.888 | 94.657 | 96.988 |
| K value 8 | TPR | 90.988 | 92.888 | 94.988 | 95.888 | 97.988 |
| K value 8 | TNR | 90.880 | 91.988 | 93.988 | 94.677 | 96.577 |
| Few-shot samples 100 | Accuracy | 85.877 | 87.888 | 90.990 | 93.898 | 96.179 |
| Few-shot samples 100 | TPR | 87.988 | 89.999 | 91.999 | 94.545 | 96.889 |
| Few-shot samples 100 | TNR | 83.099 | 88.988 | 90.880 | 93.879 | 95.768 |

## ML/DL Extraction

- Task formulation: six-class solar panel condition classification, with preprocessing and fault-region segmentation before classification.
- Inputs: RGB solar panel images from a Kaggle clean/faulty solar-panel subset represented by [[PV Panel Defect Dataset]].
- Outputs: one of six panel labels: clean, dusty, bird drop, electric damage, snow-covered, or physical damage.
- Architecture: pixel brightness correction, [[U-Net]] segmentation, handcrafted/statistical feature extraction, InceptionV3-Net branch, [[Vision Transformer]] branch, harmonic fusion layer.
- Loss: categorical cross-entropy.
- Optimizer: Adam.
- Training recipe: 80 epochs, batch size 32, learning rate 0.01, dropout 0.2.
- Evaluation protocol: comparisons are reported by learning data percentage, K value, and few-shot sample setting; exact train/test split is not reported.
- Artifacts: dataset is public; code is not reported.

## Limitations

- The paper reports minor misclassifications for extremely small or occluded fault regions.
- It proposes future work on real-time solar farm monitoring, environmental factors, edge-suitable lightweight models, federated learning, data-efficient transformers, higher-resolution imaging, and multimodal data.
- Exact train/test split construction is not reported beyond the learning-data and few-shot descriptions.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[IncepViTH-Net]], [[U-Net]], [[Vision Transformer]], [[Computer Vision Models]]
- Datasets: [[PV Panel Defect Dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]], [[Recall]], [[Specificity]]

### Shares Dataset

- [[PV Panel Defect Dataset]]: the paper evaluates on a clean/faulty solar-panel subset and reports class counts for the six panel-condition classes.

### Shares Task

- [[Solar cell defect detection]]: the paper detects faulty photovoltaic panel conditions.
- [[Defect classification]]: the final output is a six-class panel condition label.

### Shares Method

- [[IncepViTH-Net]]: the paper introduces this hybrid architecture.
- [[U-Net]]: used to segment affected panel regions before feature extraction and classification.
- [[Vision Transformer]]: one branch of the proposed classifier.
- [[Computer Vision Models]]: the paper combines convolutional, transformer, and image-processing components.

### Shares Metric

- [[Accuracy]]: primary classification metric.
- [[Recall]]: reported as TPR.
- [[Specificity]]: reported as TNR.

### Application/Domain

- [[Solar cells and photovoltaic]]: panel-level PV fault inspection and classification.

### Follow-up Reading

- [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]]: related photovoltaic panel defect detection work using a YOLO-style detector.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]: related photovoltaic cell defect classification work with deep feature fusion.
- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]]: related solar cell defect classification using deep feature representations.

## Questions

- What exact train/test split and random seeds were used for the 907-image dataset?
- Is the model implementation or trained weights available outside the article?
- How well does the reported result transfer to field imagery under different camera angles, weather, panel models, and solar farm conditions?
