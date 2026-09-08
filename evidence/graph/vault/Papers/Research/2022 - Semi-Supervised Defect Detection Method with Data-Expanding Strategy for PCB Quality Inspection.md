---
title: "Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection"
aliases:
  - "DE-SSD"
  - "BA-SSL"
paper_key: "sha256:ca9e95ebbc8cb226052e5460e58fff6abd97366c2d621aa507003e040c800220"
paper_type: research
year: 2022
venue: "Sensors"
authors:
  - "Yusen Wan"
  - "Liang Gao"
  - "Xinyu Li"
  - "Yiping Gao"
status: processed
processed_at: 2026-05-22
topics:
  - PCB defect detection
  - semi-supervised learning
  - data expansion
  - pseudo-labeling
tasks:
  - "[[PCB defect detection]]"
domains:
  - "[[Semiconductor and electronics]]"
application_area: "Printed circuit board quality inspection"
datasets:
  - "[[DeepPCB]]"
  - "[[HRIPCB]]"
dataset_sizes:
  - "DeepPCB: 1,500 samples; 1,000 train and 500 test"
  - "PKU-PCB: 1,386 PCB samples; processed into about 3,000 negative image patches"
  - "DE-SSD experiment uses 1,500 selected PKU-PCB-derived negative samples"
splits:
  - "Semi-supervised DeepPCB labels: 50, 100, or 200 labeled samples; remaining training samples used as unlabeled data"
  - "Fully supervised DeepPCB setting: all 1,000 training samples plus 1,500 negative samples"
modalities:
  - PCB image
  - bounding box annotation
methods:
  - "[[DE-SSD]]"
  - "[[Semi-supervised learning]]"
  - "[[Data augmentation]]"
  - "[[YOLOv5]]"
  - "[[Pseudo-labeling]]"
model_family:
  - single-stage object detector
  - semi-supervised detector
architectures:
  - "YOLOv5x"
losses:
  - "cross-entropy loss for classification scores"
  - "complete intersection over union loss for bounding boxes"
training_regime: "Train YOLOv5x first on labeled target and auxiliary negative samples, then add unlabeled DeepPCB samples batch by batch with dynamic-threshold pseudo labels, then train on a stable labeled/unlabeled mixture."
augmentation:
  - "YOLOv5 mosaic augmentation"
  - "PKU-PCB clipping, grayscale conversion, mean blur, unsharp masking, binarization, erosion, and dilation to create target-like negative samples"
synthetic_data: "PKU-PCB is described as a synthetic PCB defect detection dataset; DE-SSD processes auxiliary PKU-PCB images into negative samples rather than generating defects."
metrics:
  - "[[mAP]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "mAP: average precision across recalls, following the DeepPCB literature"
  - "precision: proportion of true defects among detected defects"
  - "recall: proportion of true defects that are detected"
baselines:
  - "SSDfull"
  - "SSDsemi"
  - "YOLOv5"
  - "I.P."
  - "RDDN"
  - "YOLOv1"
  - "Faster-RCNN"
benchmarks:
  - "[[DeepPCB]]"
evaluation_protocol: "Compare DE-SSD against semi-supervised and fully supervised PCB defect detectors on DeepPCB using 50/100/200 labeled-sample semi-supervised settings and a 1,000-sample fully supervised setting."
parameters: "YOLOv5x with 87.7M parameters and 284 layers"
compute: "server with two Nvidia RTX2080Ti GPUs"
hardware: "two Nvidia RTX2080Ti GPUs"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.3390/s22207971"
pdf: "paper-inbox/10_processed/Research/2022 - Wan - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection.pdf"
code: "not reported"
data: "[[DeepPCB]] and [[HRIPCB|PKU-PCB]] auxiliary dataset"
doi: "10.3390/s22207971"
arxiv: "not applicable"
related_papers:
  - "[[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[DE-SSD]]"
  - "[[Semi-supervised learning]]"
  - "[[Data augmentation]]"
  - "[[YOLOv5]]"
  - "[[Pseudo-labeling]]"
related_datasets:
  - "[[DeepPCB]]"
  - "[[HRIPCB]]"
related_tasks:
  - "[[PCB defect detection]]"
related_benchmarks:
  - "[[DeepPCB]]"
source_file: "paper-inbox/10_processed/Research/2022 - Wan - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Wan - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Wan - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection.txt"
artifact_status: "processed"
tags:
  - paper
  - pcb-defect-detection
  - semi-supervised-learning
---
# Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection

## Summary

- Wan et al. propose DE-SSD, a semi-supervised PCB defect detector that combines YOLOv5x, batch-adding semi-supervised learning, dynamic-threshold pseudo-labeling, and auxiliary-dataset data expansion.
- The method uses [[DeepPCB]] as the target dataset and processes [[HRIPCB|PKU-PCB]] into negative samples that reduce the proportion and disturbance of unlabeled samples.
- On DeepPCB, YOLOv5 + DE-SSD reports 98.4% mAP with only 50 labeled samples and 98.7% mAP with 1,000 labeled samples, improving over YOLOv5 and prior PCB detection methods.

## Paper Type

- Type: research.
- Why: The paper proposes a semi-supervised detection method, evaluates it against PCB defect detection baselines, and reports component ablations.

## Problem

- Task: [[PCB defect detection]] with bounding boxes and defect classes.
- Setting: PCB manufacturing inspection where labels are costly and many samples may be unlabeled.
- Inputs: DeepPCB defect images, unlabeled DeepPCB samples, and PKU-PCB auxiliary images processed into negative samples.
- Outputs: PCB defect bounding boxes and class predictions.
- Motivation: Deep learning PCB detectors require many labeled samples, but small labeled sets and large unlabeled sets can disturb semi-supervised training.
- Assumptions: Auxiliary PCB samples can be transformed to look similar enough to target DeepPCB samples to serve as negative samples; pseudo labels can be selected with dynamic thresholds.

## Contribution

- Claimed: BA-SSL reduces unlabeled-sample disturbance by adding unlabeled data in batches and selecting pseudo labels with a dynamic threshold.
- Claimed: The DE strategy expands target training data with transformed auxiliary negative samples from another PCB dataset.
- Shown: DE-SSD reaches mAP 98.4%, 98.6%, and 98.7% with 50, 100, and 200 labeled DeepPCB samples and improves precision/recall over YOLOv5.

## Method

- Core idea: Combine a YOLOv5x detector with a semi-supervised training schedule and auxiliary negative samples to reduce the disruptive effect of unlabeled data in few-label PCB defect detection.
- Architecture / algorithm: YOLOv5x detector with input, backbone, neck, and prediction components; BA-SSL framework; DE auxiliary negative-sample generation.
- Objective / loss: YOLOv5 uses cross-entropy loss for classification scores and complete intersection over union loss for bounding boxes.
- Optimization: SGD with initial learning rate 1e-3, weight decay 0.0005, and batch size 16.
- Training data: DeepPCB target data and PKU-PCB auxiliary negative samples.
- Data pipeline: Train on labeled target and auxiliary negative samples; generate online pseudo labels for unlabeled samples; add unlabeled batches gradually; train on a stable labeled/unlabeled mixture.
- Augmentation / synthesis: YOLOv5 mosaic augmentation; PKU-PCB images are clipped, filtered, sharpened, binarized, and smoothed to match DeepPCB-like negative samples.
- Inference: YOLOv5x predicts bounding boxes and classes for PCB defects.
- Complexity / deployment constraints: Requires developing a DE strategy tailored to the auxiliary dataset and training a large YOLOv5x model; inference cost is not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: PCB images.
- Output target: Bounding boxes and defect class labels for open, short, mouse bite, spur, spurious copper, pinhole, or related PCB defects.
- Supervision: Semi-supervised object detection with limited labeled data, unlabeled data, and auxiliary negative samples.
- Objective: Close the performance gap between few labeled samples and abundant labeled samples.

### Model And Training

- Model family: Single-stage object detection.
- Architecture: YOLOv5x with 87.7M parameters and 284 layers.
- Parameters: 87.7M.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: Cross-entropy classification loss and CIOU bounding-box loss.
- Optimizer: SGD.
- Hyperparameters: initial learning rate 1e-3, weight decay 0.0005, batch size 16; first and third semi-supervised stages last 400 epochs; second-stage stable-unlabeled interval lasts 120 epochs.
- Seeds: not reported.
- Training compute: two Nvidia RTX2080Ti GPUs.

### Data

- Datasets: [[DeepPCB]] and [[HRIPCB|PKU-PCB]].
- Data source: DeepPCB is the target dataset; PKU-PCB is an auxiliary synthetic PCB defect dataset from Peking University.
- Dataset size: DeepPCB has 1,500 samples with 1,000 train and 500 test; PKU-PCB has 1,386 samples and can generate about 3,000 alternative patches, from which 1,500 negative samples are selected.
- Labels / annotations: DeepPCB samples include PCB defect bounding boxes and classes; PKU-PCB-derived patches are used as negative samples.
- Splits: 50, 100, or 200 labeled DeepPCB samples for semi-supervised experiments; remaining target training samples are unlabeled; all 1,000 DeepPCB training samples are used in the fully supervised setting.
- Preprocessing: DeepPCB images are binary 640 x 640 samples; PKU-PCB images are clipped to 640 x 640, converted to grayscale, mean-filtered, sharpened, binarized, eroded, and dilated.
- Augmentation: YOLOv5 mosaic augmentation and DE processing.
- Synthetic data: PKU-PCB is described as synthetic; DE-SSD does not synthesize new target defects.
- Leakage checks: not reported.
- License: Sensors article is CC BY; dataset license is not reported in the analysis input.

### Evaluation

- Protocol: Semi-supervised comparison at 50/100/200 labeled samples and fully supervised comparison at 1,000 labeled samples.
- Used performance metrics: [[mAP]], [[Precision]], [[Recall]].
- Primary metric: [[mAP]].
- Metric definitions: Precision is true defects among detected defects; recall is true defects detected; mAP averages precision over different recalls.
- Metric direction / units: percentage, higher is better.
- Baselines: SSDfull, SSDsemi, YOLOv5, I.P., YOLOv1, RDDN, Faster-RCNN.
- Benchmarks: [[DeepPCB]].
- Statistical tests: not reported.
- Failure cases: DE strategy alone can reduce YOLOv5 accuracy when very few defect samples are available; BA-SSL alone cannot handle too many unlabeled samples.

## Evidence

### Experimental Setup

- Datasets: [[DeepPCB]] and [[HRIPCB|PKU-PCB]].
- Splits: DeepPCB 1,000 train/500 test; 50/100/200 labeled-sample semi-supervised settings; 1,000-sample fully supervised setting.
- Baselines: SSDfull, SSDsemi, YOLOv5, I.P., YOLOv1, RDDN, Faster-RCNN.
- Used performance metrics: [[mAP]], [[Precision]], [[Recall]].
- Compute: two Nvidia RTX2080Ti GPUs.
- Hardware: two Nvidia RTX2080Ti GPUs.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| DE-SSD improves YOLOv5 with 50 labels | [[DeepPCB]] / PCB defect detection | mAP | higher | 93.7% | 98.4% | Precision 97.2%, recall 96.6% |
| DE-SSD improves YOLOv5 with 100 labels | [[DeepPCB]] / PCB defect detection | mAP | higher | 95.4% | 98.6% | Precision 97.8%, recall 96.4% |
| DE-SSD improves YOLOv5 with 200 labels | [[DeepPCB]] / PCB defect detection | mAP | higher | 96.8% | 98.7% | Precision 98.1%, recall 96.8% |
| DE-SSD improves YOLOv5 with 1,000 labels | [[DeepPCB]] / PCB defect detection | mAP | higher | 98.4% | 98.7% | Fully supervised comparison |
| DE-SSD exceeds SSDsemi with 50 labels | [[DeepPCB]] / PCB defect detection | mAP | higher | 89.3% | 98.4% | Semi-supervised comparison |
| DE-SSD exceeds Faster-RCNN in full setting | [[DeepPCB]] / PCB defect detection | mAP | higher | 97.6% | 98.7% | Fully supervised comparison |
| DE-SSD exceeds RDDN in full setting | [[DeepPCB]] / PCB defect detection | mAP | higher | 96.9% | 98.7% | Fully supervised comparison |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | PCB defect detection | Average of precisions with different recalls | higher | yes | Main DeepPCB comparison metric |
| [[Precision]] | PCB defect detection | True defects among detected defects | higher | no | Reflects false-positive/misclassification cost |
| [[Recall]] | PCB defect detection | True defects that are detected | higher | no | Reflects missed-defect cost |

### Ablations

- Removing batch-adding reduces mAP from 98.4%, 98.6%, and 98.7% to 97.8%, 98.1%, and 98.5% for 50, 100, and 200 labeled samples.
- YOLOv5 + BA-SSL improves over YOLOv5 alone, reaching 95.8%, 96.6%, and 97.3% mAP for 50, 100, and 200 labeled samples.
- YOLOv5 + DE alone reports 90.5%, 93.5%, and 96.2% mAP for 50, 100, and 200 labeled samples, showing that DE alone can disturb training when few defect samples are labeled.
- DE-SSD combines BA-SSL and DE to outperform either component alone in the reported ablation table.

## Dataset / Benchmark Details

- Source: DeepPCB target dataset and PKU-PCB auxiliary dataset.
- Collection: DeepPCB samples are collected by a linear-scan CCD and cut into 640 x 640 binary sub-images; PKU-PCB is collected as RGB whole-PCB images with manually added defects.
- Annotation: DeepPCB includes bounding boxes and classes; PKU-PCB-derived clips are selected as defect-free negative samples for this method.
- Size: DeepPCB has 1,500 samples; PKU-PCB has 1,386 PCB samples.
- Splits: DeepPCB 1,000 train and 500 test; labeled subsets of 50/100/200 for semi-supervised experiments.
- Modalities: PCB images.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: DeepPCB and PKU-PCB differ in background, color/binary representation, image width, defect counts, and one defect category; DE preprocessing reduces but may not eliminate this domain difference.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: DE-SSD requires researchers to design a DE strategy for the auxiliary dataset; pseudo-label noise disturbs training; the selected PCB datasets include only seven defect types and omit other types such as dotted and line defects.
- Inferred: Code availability, random seeds, inference speed, and exact train/test sampling reproducibility are not reported in the analysis input.

## Reproducibility

- Code: not reported.
- Data: DeepPCB and PKU-PCB are used.
- Hyperparameters: YOLOv5x, optimizer settings, stage lengths, batch size, and DE preprocessing are reported.
- Random seeds: not reported.
- Environment: Linux 3.10.0-862.el7.x86_64, Python 3.7.11, PyTorch 1.10.2, Torchvision 0.11.3, NumPy 1.21.5.
- Checkpoints / models: not reported.
- Exact preprocessing: PKU-PCB clipping, mean blur, unsharp masking, binarization, erosion, and dilation are described.
- Artifact status: Local PDF archived as processed; code not reported.

## Systems Details

- Hardware / software stack: two Nvidia RTX2080Ti GPUs; Linux, Python, PyTorch, Torchvision, NumPy.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: Semi-supervised stage length increases as unlabeled batches are added; runtime is not measured.
- Deployment assumptions: Requires target labeled/unlabeled PCB data and an auxiliary PCB dataset that can be transformed into target-like negative samples.
- Cost: not reported.
- Failure modes: Too many unlabeled samples can disturb BA-SSL; DE alone can hurt when labeled defect samples are too few.

## Connections

### Graph Hubs

- Tasks: [[PCB defect detection]]
- Methods: [[DE-SSD]], [[Semi-supervised learning]], [[Data augmentation]], [[YOLOv5]], [[Pseudo-labeling]]
- Datasets: [[DeepPCB]], [[HRIPCB]]
- Benchmarks: [[DeepPCB]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[mAP]], [[Precision]], [[Recall]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[DeepPCB]] | Target dataset | DE-SSD evaluates PCB defect detection on DeepPCB. |
| [[HRIPCB|PKU-PCB]] | Auxiliary dataset | DE-SSD processes PKU-PCB into negative samples for data expansion. |
| [[Semi-supervised learning]] | Method family | The method trains with labeled and unlabeled samples via pseudo labels. |
| [[YOLOv5]] | Base detector | DE-SSD uses YOLOv5x as its detector and baseline. |
| [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] | Dataset link | DeepPCB is the target benchmark introduced by prior PCB defect detection work. |

### Backlinks Updated

- [[DeepPCB]] links this paper as a semi-supervised PCB defect detection benchmark.
- [[HRIPCB]] links this paper as an auxiliary data-expansion dataset under the PKU-PCB alias.
- [[DE-SSD]] links this paper as its source method.
- [[Semiconductor and electronics]] links this paper as a PCB inspection study.
- [[mAP]], [[Precision]], and [[Recall]] link this paper for reported detection metrics.

## Questions

- How robust is DE-SSD when the auxiliary PCB dataset differs more strongly from the target dataset?
- How much pseudo-label noise remains after the dynamic-threshold strategy?
- Can the DE strategy be generalized automatically instead of hand-designed per auxiliary dataset?
