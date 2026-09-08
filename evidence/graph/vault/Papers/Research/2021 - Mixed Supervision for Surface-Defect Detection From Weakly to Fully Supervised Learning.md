---
title: "Mixed Supervision for Surface-Defect Detection: From Weakly to Fully Supervised Learning"
aliases:
  - "Mixed Supervision for Surface-Defect Detection"
paper_key: "arxiv:2104.06064"
paper_type: research
year: 2021
venue: "arXiv"
authors:
  - "Jakob Bozic"
  - "Domen Tabernik"
  - "Danijel Skocaj"
status: processed
processed_at: 2026-05-22
topics:
  - "mixed supervision"
  - "surface defect detection"
  - "weak labels"
tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Metal inspection]]"
datasets:
  - "[[DAGM]]"
  - "[[KolektorSDD]]"
  - "[[KolektorSDD2]]"
  - "[[Severstal Steel Defect Dataset]]"
methods:
  - "[[Weakly supervised learning]]"
  - "[[Supervised learning]]"
  - "[[Deep convolutional neural network]]"
  - "mixed supervision"
  - "dynamically balanced loss"
  - "gradient-flow adjustment"
  - "distance-transform loss weighting"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "segmentation sub-network"
  - "classification sub-network"
optimizers:
  - "[[Stochastic gradient descent]]"
metrics:
  - "[[Average precision]]"
  - "[[AU-ROC]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  AP: "Area under the precision-recall curve; higher is better and used as the main per-image classification metric."
  AUC: "Area under the ROC curve; higher is better and reported for DAGM comparison."
  F1: "F1-measure; higher is better and reported for DAGM comparison."
  CA: "Classification accuracy; higher is better and reported for DAGM comparison."
baselines:
  - "f-AnoGAN"
  - "Uninformed Students"
  - "Staar"
  - "CADN"
  - "Kim et al."
  - "Racki et al."
  - "Weimer et al."
  - "Lin et al."
  - "Wang et al."
  - "Huang et al."
  - "Liu et al."
benchmarks:
  - "[[DAGM]]"
  - "[[KolektorSDD]]"
  - "[[KolektorSDD2]]"
  - "[[Severstal Steel Defect Dataset]]"
code: "https://github.com/vicoslab/mixed-segdec-net-comind2021"
data: "https://www.vicos.si/Downloads/KolektorSDD2"
doi: "not reported"
arxiv: "2104.06064"
url: "https://arxiv.org/abs/2104.06064"
pdf: "paper-inbox/10_processed/Research/2021 - Bozic - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Bozic - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Bozic - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Bozic - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning.txt"
artifact_status: "code and KolektorSDD2 dataset URL reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Weakly supervised learning]]"
  - "[[Supervised learning]]"
  - "[[Deep convolutional neural network]]"
  - "[[Stochastic gradient descent]]"
related_datasets:
  - "[[DAGM]]"
  - "[[KolektorSDD]]"
  - "[[KolektorSDD2]]"
  - "[[Severstal Steel Defect Dataset]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
tags:
  - paper
---
# Mixed Supervision for Surface-Defect Detection: From Weakly to Fully Supervised Learning

## Summary

- The paper proposes a deep-learning architecture for industrial surface-defect detection that can train from weak image-level labels, full pixel-level masks, or a mixture of both.
- The architecture has a segmentation sub-network and a classification sub-network trained end to end; the classification target is the main industrial decision of whether an inspected item is defective.
- The paper evaluates on [[DAGM]], [[KolektorSDD]], [[KolektorSDD2]], and [[Severstal Steel Defect Dataset]], and reports that a small number of pixel-level masks added to weak labels often approaches fully supervised performance.

## Paper Type

Research paper. It introduces a model, training losses, a mixed-supervision protocol, a new dataset, and experimental comparisons against unsupervised, weakly supervised, and fully supervised defect-detection methods.

## Problem

- Task: per-image defect detection/classification, with segmentation used during training and as an auxiliary output.
- Setting: industrial surface-defect inspection where defective samples are rare and pixel-level labels are expensive or ambiguous.
- Inputs: industrial inspection images with image-level labels, optional pixel-level masks, and optional coarse region annotations.
- Outputs: image-level defect probability and segmentation map.
- Motivation: reduce annotation cost while retaining the performance benefits of fully supervised segmentation masks.

## Contribution

- Proposes a mixed-supervision surface-defect detector that jointly trains segmentation and classification sub-networks from image-level and pixel-level labels.
- Introduces dynamically balanced loss, gradient-flow adjustment, and distance-transform weighting for coarse or uncertain pixel-level labels.
- Introduces [[KolektorSDD2]], a real-world industrial dataset with 3335 images, fine-grained segmentation masks, and a public download URL.
- Shows that mixed supervision can reach high detection performance with only a small fraction of positive samples fully annotated.

## Method

- The segmentation sub-network learns from pixel-level masks when they are available.
- The classification sub-network learns from image-level labels and uses segmentation features and pooled segmentation outputs.
- The total loss combines segmentation and classification cross-entropy: segmentation is weighted by lambda, gamma, and pixel-label availability; classification is weighted by the complementary factor and delta.
- Gamma disables segmentation learning only for positive images without pixel-level masks. Negative images still supervise the segmentation output as all-zero masks.
- Dynamically balanced loss gradually shifts training emphasis from segmentation to classification across epochs.
- Gradient-flow adjustment stops classification gradients from modifying the segmentation sub-network through the segmentation feature and pooling shortcuts.
- Distance-transform weighting gives more weight to central pixels in positive regions and less to uncertain defect boundaries.

## ML/DL Extraction

### Architecture

| Part | Source-backed detail |
|---|---|
| Segmentation sub-network | Convolutional and max-pooling blocks produce segmentation features and segmentation map. |
| Classification sub-network | Receives segmentation features and segmentation map, applies pooling/convolution, then predicts image-level defect probability. |
| Losses | Cross-entropy segmentation loss and cross-entropy classification loss, combined for weak, mixed, and full supervision. |
| Label handling | Weak labels are image-level; full labels are pixel-level; mixed supervision uses image-level labels for all images and pixel-level labels for a subset of anomalous images. |

### Training Details

| Dataset | Reported training setup |
|---|---|
| [[DAGM]] | 70 epochs, learning rate 0.05, batch size 1, delta 1, positive-pixel weight 10, p = 1, 7 x 7 mask dilation. |
| [[KolektorSDD]] | 50 epochs for mixed/full runs, learning rate 1, batch size 1, delta 0.01, positive-pixel weight 1, p = 2; weak-only run uses delta 1 and learning rate 0.01. |
| [[KolektorSDD2]] | 50 epochs, learning rate 0.01, batch size 1, delta 1, positive-pixel weight 3, p = 2, 15 x 15 mask dilation. |
| [[Severstal Steel Defect Dataset]] | Positive training subset varied across 300, 750, 1500, and 3000; epochs 90, 80, 60, and 40 respectively; learning rate 0.1, batch size 10, delta 0.1, positive-pixel weight 1, p = 2. |

## Data

| Dataset | Source-backed details |
|---|---|
| [[DAGM]] | Grayscale images of 10 computer-generated surfaces with scratches or spots; each surface is a binary classification problem; annotations are ellipse-like regions. |
| [[KolektorSDD]] | Real-world grayscale production-item images with visible surface cracks; evaluated with three-fold cross-validation. |
| [[KolektorSDD2]] | Color images from a controlled industrial inspection setup, about 230 x 630 pixels; train split has 2085 negative and 246 positive samples; test split has 894 negative and 110 positive samples; defects have fine-grained masks and vary from small scratches and spots to large surface imperfections. |
| [[Severstal Steel Defect Dataset]] | 12,568 grayscale images in four classes; the evaluation uses all negative images and positive images from the most common defect class, class 3. |

## Evidence

### Performance Metrics

| Metric | Direction | Evaluation context |
|---|---|---|
| [[Average precision]] | Higher is better | Main per-image classification metric for KolektorSDD, KolektorSDD2, Severstal Steel, and many DAGM results. |
| [[AU-ROC]] | Higher is better | DAGM comparison table. |
| [[F1-score]] | Higher is better | DAGM comparison table. |
| [[Accuracy]] | Higher is better | DAGM classification accuracy and mean accuracy comparison. |

### Main Results

| Dataset | Supervision setting | Key result |
|---|---|---|
| [[DAGM]] | Weak labels only, N = 0 | Average AP 74.0 in the comparison table and over 90% AP for 6 classes in the class-wise analysis. |
| [[DAGM]] | Mixed supervision, N = 5 | Average AP 91.5; 100% detection rate on 8 classes. |
| [[DAGM]] | Mixed supervision, N = 15 | 100% AP, AUC, F1, classification accuracy, and mean accuracy. |
| [[DAGM]] | Full supervision | 100% reported for the tabled metrics. |
| [[KolektorSDD]] | Weak labels only | AP 93.4. |
| [[KolektorSDD]] | Mixed supervision, N = 5 | AP 99.1 with fewer than 15% of positive images pixel-annotated. |
| [[KolektorSDD]] | Full supervision | 100% detection rate. |
| [[KolektorSDD2]] | Weak labels only | AP 73.3. |
| [[KolektorSDD2]] | Mixed supervision, N = 16 | AP 83.2. |
| [[KolektorSDD2]] | Full supervision | AP 95.4. |
| [[Severstal Steel Defect Dataset]] | Weak labels only | AP ranges from 90.3 to 94.1 as positive image count increases from 300 to 3000. |
| [[Severstal Steel Defect Dataset]] | Mixed/full supervision | AP 95.37 for a mixed-supervision setting and 100% detection rate for full supervision. |

### Ablation Results

| Component | Source-backed finding |
|---|---|
| Dynamically balanced loss | Improves fully supervised AP by 1.08 points on DAGM, 0.23 on KolektorSDD, and 1.68 on Severstal Steel; also improves mixed supervision. |
| Gradient-flow adjustment | Prevents unstable segmentation features from disrupting classification learning and improves robustness. |
| Distance-transform weighting | Raises fully supervised Severstal AP from 98.24% to 98.74% and enables 100% detection rate with 25% fully annotated data in mixed supervision on the reported datasets. |

## Reproducibility

- Code: https://github.com/vicoslab/mixed-segdec-net-comind2021
- KolektorSDD2 data: https://www.vicos.si/Downloads/KolektorSDD2
- Framework: PyTorch.
- Optimizer: [[Stochastic gradient descent]] without momentum and without weight decay.
- Hardware: single NVIDIA RTX2080Ti for reported speed and training-time measurements.
- Inference speeds: 57 FPS on DAGM 512 x 512 images, 23 FPS on KolektorSDD 512 x 1408 images, 85 FPS on KolektorSDD2 232 x 640 images, and 36 FPS on Severstal 1600 x 256 images.
- Training times: 35 minutes for DAGM, 32 minutes for one KolektorSDD fold, 15 minutes for KolektorSDD2, and 460 minutes for Severstal Steel with Nall = 3000.

## Limitations

- The primary objective is image-level defect detection; segmentation is used to improve training and is not the main decision target.
- The Severstal evaluation uses only the most common positive defect class rather than all defect classes.
- The paper reports that some Severstal defects are ambiguous and may not be properly annotated.
- Distance-transform weighting and mask dilation introduce task-specific choices for handling uncertain defect boundaries.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Defect segmentation]]
- Learning paradigms: [[Weakly supervised learning]], [[Supervised learning]]
- Methods: [[Deep convolutional neural network]]
- Optimizers: [[Stochastic gradient descent]]
- Datasets: [[DAGM]], [[KolektorSDD]], [[KolektorSDD2]], [[Severstal Steel Defect Dataset]]
- Metrics: [[Average precision]], [[AU-ROC]], [[F1-score]], [[Accuracy]]
- Domains: [[Multi-industry anomaly detection]], [[Metal inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - The MVTec Anomaly Detection Dataset]] | Contrasts with | MVTec AD emphasizes unsupervised anomaly segmentation benchmarks; this paper focuses on mixed image-level and pixel-level supervision for industrial defect detection. |
| [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] | Contrasts with | FastFlow trains on normal samples only; this paper explicitly uses weak and full labels when available. |

## Questions

- How would the method compare against newer foundation-model or transformer-based defect detectors under the same mixed-supervision protocol?
- How sensitive are the results to mask dilation size and distance-transform weighting on datasets with fuzzy boundaries?
