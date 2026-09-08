---
title: "Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF"
aliases:
  - "YOLO-ACF"
  - "Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF"
paper_key: "doi:10.1038/s41598-024-75772-9"
paper_type: research
year: 2024
venue: "Scientific Reports"
authors:
  - "Wenwen Pan"
  - "Xiaofei Sun"
  - "Yilun Wang"
  - "Yang Cao"
  - "Yizheng Lang"
  - "Yunsheng Qian"
status: processed
processed_at: 2026-07-09
topics:
  - industrial defect detection
  - photovoltaic inspection
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PVEL-AD]]"
methods:
  - "[[YOLO-ACF]]"
  - "[[YOLOv5]]"
model_family:
  - "[[Deep convolutional neural network]]"
  - "[[YOLOv5]]"
architectures:
  - "[[YOLO-ACF]]"
losses:
  - "CIoU box loss"
  - "BCEWithLogits confidence loss"
  - "BCEWithLogits classification loss"
optimizers:
  - "SGD"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Average precision]]"
  - "[[mAP]]"
  - "[[FPS]]"
primary_metric: "[[mAP]]"
baselines:
  - "Faster R-CNN"
  - "RetinaNet"
  - "YOLOv3"
  - "[[YOLOv5]]"
  - "YOLOv6"
  - "[[YOLOv8]]"
benchmarks:
  - "[[PVEL-AD benchmark]]"
code: "not reported"
data: "https://github.com/binyisu/PVEL-AD"
doi: "10.1038/s41598-024-75772-9"
arxiv: "not reported"
url: "https://doi.org/10.1038/s41598-024-75772-9"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[YOLO-ACF]]"
  - "[[YOLOv5]]"
  - "[[YOLOv8]]"
related_datasets:
  - "[[PVEL-AD]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "[[PVEL-AD benchmark]]"
source_file: "paper-inbox/10_processed/Research/2024 - Pan - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Pan - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Pan - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF.txt"
artifact_status: "dataset available; code not reported"
tags:
  - paper
---

# Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF

## Summary

Pan et al. propose [[YOLO-ACF]], a YOLOv5s v6.0 detector for photovoltaic-panel electroluminescence defect detection. The method replaces the C3 module with an adaptive complementary fusion module that sequentially refines spatial and channel embeddings to improve detection while reducing parameters, weight size, and inference time.

On a selected [[PVEL-AD]] subset of 4,488 near-infrared electroluminescence images, YOLO-ACF reports 84.5% precision, 92.3% recall, 92.6% mAP50, 62.1% mAP50-95, 6.1M parameters, 14.2G FLOPs, 12.7 MB weights, 6.8 ms per image, and 147 FPS. Relative to YOLOv8, the paper reports higher recall, mAP50, and mAP50-95; relative to YOLOv5, it reports fewer parameters, smaller weights, lower latency, and higher FPS.

## Paper Type

- Type: research.
- Why: The paper introduces a modified detector architecture, evaluates it on photovoltaic-panel defect detection, and compares it against detector baselines and ablations.

## Problem

- Task: [[Solar cell defect detection]] and [[Surface defect detection]] in photovoltaic-panel electroluminescence images.
- Setting: automated quality inspection of photovoltaic panels where defect features can be similar to complex background patterns.
- Inputs: near-infrared electroluminescence images.
- Outputs: bounding boxes and defect-class predictions for selected photovoltaic defect categories.
- Motivation: reduce missed detections and false alarms while keeping the detector lightweight enough for practical inspection workflows.
- Defect classes used: crack, finger interruption, black core, thick line, star crack, corner, horizontal dislocation, vertical dislocation, and short circuit.

## Contribution

- Introduces the Adaptive Complementary Fusion (ACF) module for sequential spatial and channel feature refinement.
- Integrates ACF into YOLOv5s v6.0 to build [[YOLO-ACF]] for photovoltaic-panel defect detection.
- Reports that a single ACF module gives a better performance/efficiency balance than two ACF modules and outperforms the tested detector baselines on several accuracy and speed metrics.

## Method

### Architecture

- Baseline: YOLOv5s v6.0.
- Input: Mosaic data augmentation and 640 x 640 training images.
- Backbone: Conv2d + BN2d + SiLU blocks, C3/CSP-derived components, and the ACF module.
- Neck: fuses shallow features from the backbone with deeper semantic features.
- Head: predicts bounding boxes and classes.

### Adaptive Complementary Fusion

- Spatial adaptive fusion uses Group Normalization scaling factors to weight spatial embedding information, separates strong and weak embeddings with a sigmoid gate threshold of 0.5, and cross-fuses the resulting branches.
- Channel adaptive fusion uses grouped convolution with group number 2, pointwise convolution, a cheap 1 x 1 convolution branch, global average pooling, and softmax weighting to combine channel-refined embeddings.
- The paper's stated design goal is to reduce redundant embedding information while retaining representative spatial and channel cues.

### Objective And Training

- Box regression: CIoU loss.
- Confidence and classification: BCEWithLogitsLoss.
- Optimizer: SGD.
- Training settings: batch size 16, 100 epochs, input image size 640 x 640, initial learning rate 0.001, momentum 0.937, weight decay 0.0005.
- Hardware: Intel Xeon CPU E5-2678 v3 and NVIDIA GeForce GTX 1080 Ti.

## ML / DL Extraction

### Task Formulation

- Input modality: photovoltaic-panel electroluminescence images.
- Output target: defect bounding boxes and defect classes.
- Supervision: supervised object detection with labeled defect instances.
- Evaluation focus: detection performance, model complexity, and inference speed.

### Model And Training

- Model family: YOLO-style one-stage detector based on [[YOLOv5]].
- Architecture: YOLOv5s v6.0 with Adaptive Complementary Fusion.
- Parameters: 6.1M for YOLO-ACF.
- FLOPs: 14.2G for YOLO-ACF.
- Weight size: 12.7 MB for YOLO-ACF.
- Pretraining: not reported.
- Random seeds: not reported.
- Training time: not reported.

### Data

- Dataset: [[PVEL-AD]], released by Hebei University of Technology and Beihang University.
- Public source: https://github.com/binyisu/PVEL-AD.
- Images used: 4,488 selected near-infrared electroluminescence images from the publicly accessible portion.
- Original public portion described by the paper: 4,500 images with one normal class and twelve defect types.
- Experimental selection: nine defect classes plus normal, omitting classes with insufficient samples.
- Split: 8:1:1 train/validation/test by image count.
- Instance counts:
  - Crack: 969 train, 184 validation, 101 test, 1,254 total.
  - Finger: 2,158 train, 513 validation, 285 test, 2,956 total.
  - Black_core: 923 train, 16 validation, 88 test, 1,027 total.
  - Thick_line: 862 train, 20 validation, 99 test, 981 total.
  - Star_crack: 61 train, 58 validation, 16 test, 135 total.
  - Corner: 7 train, 0 validation, 2 test, 9 total.
  - Horizontal_dislocation: 723 train, 6 validation, 69 test, 798 total.
  - Vertical_dislocation: 112 train, 8 validation, 17 test, 137 total.
  - Short_circuit: 428 train, 6 validation, 58 test, 492 total.
- License: not reported.
- Leakage checks: not reported.

### Evaluation

- Metrics: precision, recall, mAP50, mAP50-95, parameters, FLOPs, weight size, inference time per image, and FPS.
- Primary reported detector quality metrics: mAP50 and mAP50-95.
- Baselines: Faster R-CNN, RetinaNet, YOLOv3, YOLOv5, YOLOv6, and YOLOv8.
- Statistical tests: not reported.

## Evidence

### Main Results

| Method | P (%) | R (%) | mAP50 (%) | mAP50-95 (%) | Params (M) | FLOPs (G) | Weight (MB) | Time (ms) | FPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RetinaNet | 69.7 | 58.8 | 91.3 | 58.7 | 10.4 | 68.2 | 289.0 | 37.4 | 27 |
| YOLOv3 | 53.1 | 72.4 | 60.5 | 26.9 | 8.7 | 12.9 | 17.5 | 7.3 | 136 |
| YOLOv5 | 81.7 | 86.8 | 89.1 | 60.4 | 7.0 | 15.9 | 14.5 | 7.1 | 140 |
| YOLOv6 | 67.6 | 77.1 | 75.7 | 51.7 | 16.3 | 44.0 | 32.9 | 9.1 | 110 |
| YOLOv8 | 87.0 | 87.1 | 91.8 | 59.8 | 11.1 | 28.5 | 22.5 | 8.5 | 117 |
| YOLO-ACF | 84.5 | 92.3 | 92.6 | 62.1 | 6.1 | 14.2 | 12.7 | 6.8 | 147 |
| Faster R-CNN | 31.9 | 26.4 | 76.6 | 51.3 | 14.0 | 14.1 | 315.2 | 30.2 | 33 |

- Relative to YOLOv8, YOLO-ACF improves recall by 5.2 percentage points, mAP50 by 0.8 percentage points, and mAP50-95 by 2.3 percentage points.
- Relative to YOLOv5, YOLO-ACF reduces parameters by 12.9%, weight size by 12.4%, and time per image by 4.2%, while increasing FPS by 5%.
- Confusion-matrix comparisons report higher accuracy for crack (84% vs 80%), thick_line (83% vs 77%), and black_core (100% vs 99%) compared with YOLOv8.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Precision]] | defect detection | percentage of predicted detections that are correct | higher is better | no | YOLO-ACF: 84.5% |
| [[Recall]] | defect detection | percentage of ground-truth instances detected | higher is better | no | YOLO-ACF: 92.3% |
| [[mAP]] | object detection | mAP50 and mAP50-95 percentages | higher is better | yes | YOLO-ACF: 92.6% mAP50, 62.1% mAP50-95 |
| [[FPS]] | inference speed | frames per second | higher is better | no | YOLO-ACF: 147 FPS |

### Ablations

| Setting | P (%) | R (%) | mAP50 (%) | mAP50-95 (%) | Params (M) | FLOPs (G) | Weight (MB) | Time (ms) | FPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Without attention | 81.7 | 86.8 | 89.1 | 60.4 | 7.0 | 15.9 | 14.5 | 7.1 | 140 |
| C3ACF | 89.0 | 92.3 | 92.7 | 62.4 | 7.3 | 15.2 | 15.0 | 9.4 | 106 |
| ACF | 84.5 | 92.3 | 92.6 | 62.1 | 6.1 | 14.2 | 12.7 | 6.8 | 147 |

| ACF count | P (%) | R (%) | mAP50 (%) | mAP50-95 (%) |
|---|---:|---:|---:|---:|
| Without | 81.7 | 86.8 | 89.1 | 60.4 |
| ACF | 84.5 | 92.3 | 92.6 | 62.1 |
| 2*ACF | 87.0 | 74.0 | 80.0 | 51.6 |

| Box loss | P (%) | R (%) | mAP50 (%) | mAP50-95 (%) |
|---|---:|---:|---:|---:|
| DIoU | 78.5 | 88.1 | 87.5 | 60.6 |
| FCIoU | 87.0 | 90.9 | 91.5 | 60.2 |
| CIoU | 84.5 | 92.3 | 92.6 | 62.1 |
| EIoU | 90.7 | 77.1 | 91.0 | 60.8 |

### Qualitative Findings

- The qualitative examples report that YOLO-ACF avoids some missed detections or false positives observed in RetinaNet, YOLOv3, YOLOv5, YOLOv6, and YOLOv8 across crack, finger, thick_line, star_crack, corner, horizontal_dislocation, vertical_dislocation, and short_circuit examples.
- The authors frame the method as useful for detecting both single and multiple defect types in photovoltaic panels of varying size and appearance.

## Dataset / Benchmark Details

- Benchmark: [[PVEL-AD benchmark]].
- The paper uses an object-detection setup on a selected [[PVEL-AD]] subset rather than the full dataset described by the PVEL-AD dataset paper.
- The class distribution is imbalanced, with corner defects especially scarce: 7 train instances, 0 validation instances, and 2 test instances.
- Data availability: all experiment data are reported as available via https://github.com/binyisu/PVEL-AD.

## Limitations

- The paper does not report code availability.
- Random seeds and statistical tests are not reported.
- The selected data subset excludes three of the twelve public defect types because some classes have insufficient samples.
- The class distribution is highly imbalanced; the corner class has no validation instances and only two test instances.
- The paper reports a single hardware setup and does not analyze performance across deployment devices.

## Reproducibility

- Code: not reported.
- Data: [[PVEL-AD]] GitHub repository reported.
- Hyperparameters: batch size 16, 100 epochs, input size 640 x 640, SGD with initial learning rate 0.001, momentum 0.937, weight decay 0.0005.
- Random seeds: not reported.
- Hardware: Intel Xeon CPU E5-2678 v3 and NVIDIA GeForce GTX 1080 Ti.
- Checkpoints / models: not reported.
- Artifact status: dataset available; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Surface defect detection]]
- Methods: [[YOLO-ACF]], [[YOLOv5]], [[YOLOv8]]
- Datasets: [[PVEL-AD]]
- Benchmark: [[PVEL-AD benchmark]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Precision]], [[Recall]], [[Average precision]], [[mAP]], [[FPS]]

### Builds On

- [[YOLOv5]]: YOLO-ACF uses YOLOv5s v6.0 as the baseline network.

### Contrasts With

- [[YOLOv8]]: YOLO-ACF is compared against YOLOv8 and reports higher recall, mAP50, and mAP50-95 on the selected PVEL-AD subset.

### Shares Dataset

- [[PVEL-AD]]: the experiments use selected PVEL-AD electroluminescence images.

### Shares Task

- [[Solar cell defect detection]]: the paper detects photovoltaic-panel EL defect categories.
- [[Surface defect detection]]: the detector is applied to visible defect localization in industrial inspection imagery.

### Shares Method

- [[YOLO-ACF]]: the paper introduces the method.
- [[YOLOv5]]: the method modifies the YOLOv5s baseline.

### Shares Metric

- [[Precision]], [[Recall]], [[Average precision]], [[mAP]], and [[FPS]]: used to evaluate detection quality and efficiency.

### Application / Domain

- [[Solar cells and photovoltaic]]: the inspection target is photovoltaic panels.

### Follow-Up Reading

- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]]: introduces the dataset and benchmark context reused by YOLO-ACF.
- [[PVEL-AD benchmark]]: summarizes the benchmark protocol and reported detector results for the dataset.

## Questions

- Would YOLO-ACF retain its reported speed/accuracy balance on edge hardware or newer GPUs?
- How sensitive are the reported gains to the omitted defect classes and highly imbalanced selected subset?
- Does the method generalize to the full PVEL-AD benchmark protocol used by the dataset paper?
