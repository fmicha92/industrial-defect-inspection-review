---
title: "Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing"
aliases:
  - "Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing"
paper_key: "sha256:48e61e01936126d4c184169dc6cdf7d42649e2568a6dc5371bde56a3dcb919f2"
paper_type: research
year: 2023
venue: "Robotics and Computer-Integrated Manufacturing"
authors:
  - "Wenhao Li"
  - "Haiou Zhang"
  - "Guilan Wang"
  - "Gang Xiong"
  - "Meihua Zhao"
  - "Guokuan Li"
  - "Runsheng Li"
status: processed
processed_at: 2026-05-21
topics:
  - "wire and arc additive manufacturing"
  - "online defect detection"
  - "YOLO attention"
tasks:
  - "[[Additive manufacturing defect detection]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
  - "[[Smart manufacturing]]"
datasets:
  - "[[WAAM metallic surface defect dataset]]"
methods:
  - "[[YOLO-attention]]"
  - "[[YOLOv4]]"
model_family:
  - "[[YOLOv4]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.5 is mean average precision at IoU 0.5; FPS measures inference throughput."
benchmarks:
  - "[[WAAM metallic surface defect dataset]]"
code: "not reported"
data: "paper-specific WAAM dataset with 760 tagged images and 8583 tagged targets; public availability not reported"
doi: "10.1016/j.rcim.2022.102470"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.rcim.2022.102470"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[YOLO-attention]]"
  - "[[YOLOv4]]"
related_datasets:
  - "[[WAAM metallic surface defect dataset]]"
related_tasks:
  - "[[Additive manufacturing defect detection]]"
  - "[[Metallic surface defect detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Li - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Li - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Li - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing.txt"
artifact_status: "not reported"
tags:
  - paper
---

# Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing

## Summary

Li et al. propose [[YOLO-attention]], a YOLOv4-based detector for online metallic surface defect detection in wire and arc additive manufacturing (WAAM). The method adds a channel-wise attention backbone, multiple spatial pyramid pooling branches, and exponential moving average training to improve detection of small and dense WAAM defects. On a paper-specific [[WAAM metallic surface defect dataset]], it reports 94.5 mAP@0.5 at 42 FPS on an NVIDIA GTX 1080Ti.

## Paper Type

- Type: research.
- Why: The paper proposes a modified object detector, builds a WAAM defect dataset, and reports experimental comparisons and ablations.

## Problem

- Task: [[Additive manufacturing defect detection]], [[Metallic surface defect detection]]
- Setting: [[Metal inspection]], [[Smart manufacturing]]
- Inputs: RGB images from a passive visual sensor monitoring WAAM weld beads.
- Outputs: bounding boxes and labels for welds, surface pores, grooves, and slag inclusions.
- Motivation: WAAM needs real-time automatic inspection; defects are small, dense, visually diverse, and often embedded in deceptive backgrounds.
- Assumptions: a one-stage detector is needed to satisfy real-time industrial detection requirements of at least 30 FPS.

## Contribution

- Claimed: Proposes a YOLOv4-based online WAAM defect detector named [[YOLO-attention]].
- Claimed: Channel-wise attention, multiple SPP, and EMA improve small-target detection and training stability.
- Shown: YOLO-attention reaches 94.5 mAP@0.5 and 42 FPS on the WAAM test set.
- Shown: Compared with original YOLOv4, the proposed model improves mAP by 29.8% with only a slight FPS reduction.

## Method

- Core idea: adapt YOLOv4 for WAAM defects by emphasizing informative channels, adding SPP on all FPN branches, and smoothing training weights with EMA.
- Architecture / algorithm: [[YOLO-attention]], [[YOLOv4]].
- Backbone: DarkNet53-attention with residual attention blocks.
- Neck: FPN with multiple SPPs to capture features at different receptive-field sizes for small targets.
- Training strategies: mosaic data augmentation, cosine decay, transfer learning from COCO, customized anchors, Kaiming initialization, SGD, and EMA.
- Inference: batch-normalization and convolution layers are fused in prediction to accelerate inference.

## ML / DL Extraction

### Task Formulation

- Input modality: 8-bit RGB images from a CMOS camera.
- Output target: object detection boxes/classes for welds, surface pores, grooves, and slag inclusions.
- Supervision: supervised object detection with tagged images and targets.
- Objective: maximize mAP@0.5 while maintaining real-time FPS.

### Model And Training

- Model family: [[YOLOv4]] one-stage object detection.
- Architecture: [[YOLO-attention]] with DarkNet53-attention, FPN, multiple SPPs, and YOLO detection heads.
- Pretraining: transfer learning from COCO.
- Optimizer: SGD with momentum 0.937 and weight decay 0.000332.
- Hyperparameters: 300 epochs, batch size 6, initial learning rate 0.01, final learning rate 0.0005, BN momentum 0.03.
- Loss weights: CIoU 2.52, objectness 102, class 1.51.
- Training compute: experiments report NVIDIA GeForce GTX 1080Ti for speed; full environment table is in the source.

### Data

- Dataset: [[WAAM metallic surface defect dataset]].
- Size: 760 tagged images and 8583 tagged targets.
- Split: shuffled dataset with 10% selected as the test set; the source also states 680 training images and 80 verification/test images.
- Sensor: MIROEX4-4096MM digital CMOS camera, 1920 x 1080, 60 FPS, with optical filter to reduce arc-light radiation.
- Target classes: welds, surface pores, grooves, and slag inclusions.
- Data source: actual industrial production plus harsh conditions created by manual experiments.
- License: not reported.

### Evaluation

- Protocol: compare YOLO-attention with YOLOv4, Faster R-CNN, EfficientDet variants, and architecture/training ablations under consistent experimental conditions.
- Used performance metrics: [[mAP@0.50]], [[FPS]].
- Primary metric: [[mAP@0.50]].
- Metric direction / units: higher is better for both mAP@0.5 and FPS.
- Statistical tests: 10 independent experiments with ANOVA; reported p < 0.01 for the optimization method effect.
- Failure cases: original YOLOv4 misses minor defects, with 48.8 mAP for slag inclusions and 72.8 mAP overall in the paper's experiment.

## Evidence

### Experimental Setup

- Dataset: [[WAAM metallic surface defect dataset]].
- Baselines: original YOLOv4, Faster R-CNN, EfficientDet variants, backbone/activation/SPP/EMA ablations.
- Used performance metrics: [[mAP@0.50]], [[FPS]].
- Hardware: NVIDIA GeForce GTX 1080Ti for reported 42 FPS.

### Main Results

| Result | Dataset / Task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| Final detector | [[WAAM metallic surface defect dataset]] / WAAM detection | [[mAP@0.50]] | YOLOv4 72.8 | 94.5 | Source states +29.8% mAP over YOLOv4. |
| Final detector speed | [[WAAM metallic surface defect dataset]] / online detection | [[FPS]] | not reported in note | 42 | Reported on NVIDIA GTX 1080Ti. |
| Backbone ablation | same | [[mAP@0.50]] | DarkNet53 86.7 | DarkNet53-attention 94.5 | FPS: 43 vs 42. |
| Multiple SPP ablation | same | [[mAP@0.50]] | no SPP 84.0 | 3 SPPs 94.5 | One SPP reports 89.2. |
| EMA ablation | same | [[mAP@0.50]] | without EMA 86.1 | with EMA 94.5 | No added inference computation. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP@0.50]] | object detection | mAP at IoU 0.5 | higher | yes | Main accuracy metric in result and ablation tables. |
| [[FPS]] | online detection speed | frames per second | higher | no | Real-time threshold discussed as at least 30 FPS. |

### Ablations

- Channel-wise attention improves mAP from 86.7 for DarkNet53 to 94.5 for DarkNet53-attention.
- Three SPP branches improve mAP from 84.0 with no SPP and 89.2 with one SPP to 94.5.
- EMA improves mAP from 86.1 to 94.5 without increasing inference computation.
- Transfer learning reaches 94.5 mAP after 126 epochs versus 90.7 mAP after 236 epochs when training from scratch.

## Dataset / Benchmark Details

- Source: paper-specific WAAM visual inspection data.
- Collection: CMOS images from actual production and manually created harsh conditions.
- Annotation: tagged images and object targets.
- Size: 760 images, 8583 targets.
- Split: 10% held out for test/validation.
- Modalities: RGB visual sensor imagery.
- License: not reported.
- Leakage risks: no explicit leakage checks reported.

## Limitations

- Stated: not directly framed as a limitations section in the extracted text.
- Inferred: the dataset is paper-specific and public availability is not reported.
- Inferred: the method is tailored to four WAAM target categories and should not be assumed to transfer to other additive manufacturing inspection settings without validation.

## Reproducibility

- Code: not reported.
- Data: [[WAAM metallic surface defect dataset]] described but not reported as public.
- Hyperparameters: optimizer, schedule, batch size, epochs, and loss weights are reported.
- Random seeds: not reported.
- Environment: hardware includes NVIDIA GTX 1080Ti for reported FPS.
- Artifact status: not reported.

## Connections

### Graph Hubs

- Tasks: [[Additive manufacturing defect detection]], [[Metallic surface defect detection]]
- Methods: [[YOLO-attention]], [[YOLOv4]]
- Datasets: [[WAAM metallic surface defect dataset]]
- Domains: [[Metal inspection]], [[Smart manufacturing]]
- Metrics: [[mAP@0.50]], [[FPS]]
- Concepts: [[Surface defect detection]]

### Shares Dataset

- [[WAAM metallic surface defect dataset]]: paper-specific online WAAM defect dataset.

### Shares Task

- [[Additive manufacturing defect detection]]: WAAM online inspection.
- [[Metallic surface defect detection]]: weld bead surface pores, grooves, and slag inclusions.

### Shares Method

- [[YOLO-attention]]: proposed detector.
- [[YOLOv4]]: base object detector.

### Shares Metric

- [[mAP@0.50]]: primary detection metric.
- [[FPS]]: online throughput metric.

### Application / Domain

- [[Metal inspection]], [[Smart manufacturing]]
