---
title: "ALADA: A Lite Automatic Data Augmentation Framework for Industrial Defect Detection"
aliases:
  - "ALADA"
  - "ALADA: A Lite Automatic Data Augmentation Framework for Industrial Defect Detection"
paper_key: "sha256:b6478659a3c96712e94d66c4ebf9c2e7523fc748b850e46f5e69c7c81f30f172"
paper_type: research
year: 2023
venue: "Advanced Engineering Informatics"
authors:
  - "Yuxuan Wang"
  - "Sai-Ho Chung"
  - "Waqar Ahmed Khan"
  - "Tianteng Wang"
  - "David Jingjun Xu"
status: processed
processed_at: 2026-05-22
topics:
  - "automatic data augmentation"
  - "industrial defect detection"
tasks:
  - "[[Surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Tianchi-TILE]]"
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
methods:
  - "[[ALADA]]"
  - "[[Data augmentation]]"
  - "[[Automatic data augmentation]]"
  - "[[Policy gradient sampling]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "FRCNN"
  - "RetinaNet"
metrics:
  - "[[mAP]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "VOC-style mAP with detections counted correct at IoU > 0.5"
baselines:
  - "FRCNN"
  - "RetinaNet"
  - "MixUp"
  - "Mosaic"
  - "AutoAugment"
  - "TrivialAugment"
  - "DADA"
benchmarks:
  - "[[Tianchi-TILE]]"
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
code: "not reported"
data: "evaluated datasets are named; article data-availability statement says authors do not have permission to share data"
doi: "10.1016/j.aei.2023.102205"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.aei.2023.102205"
pdf: "paper-inbox/10_processed/Research/2023 - Wang - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[ALADA]]"
  - "[[Data augmentation]]"
  - "[[Automatic data augmentation]]"
  - "[[Policy gradient sampling]]"
  - "[[Deep convolutional neural network]]"
related_datasets:
  - "[[Tianchi-TILE]]"
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Object detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Wang - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wang - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wang - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection.txt"
artifact_status: "not reported"
tags:
  - paper
  - automatic-data-augmentation
  - surface-defect-detection
---
# ALADA: A Lite Automatic Data Augmentation Framework for Industrial Defect Detection

## Summary

- ALADA is a lite automatic data augmentation framework for industrial defect detection.
- The method jointly optimizes augmentation policy weights and defect detector parameters, replacing the retraining stage used by many search-based automatic augmentation methods.
- It is evaluated on [[Tianchi-TILE]], [[GC10-DET]], and [[NEU-DET]] with FRCNN and RetinaNet detectors.

## Paper Type

- Type: research.
- Why: The source proposes a new automatic augmentation optimization method and evaluates it experimentally on industrial defect detection datasets.

## Problem

- Task: [[Surface defect detection]], [[Object detection]]
- Setting: [[Multi-industry anomaly detection]]
- Inputs: industrial defect images with VOC-format bounding-box annotations.
- Outputs: defect bounding boxes and classes.
- Motivation: industrial defect detectors suffer from insufficient examples and intraclass variation, while manual augmentation choices are empirical and not universal across products.
- Assumptions: the candidate augmentation operations are basic image-processing operations, and each sampled policy uses one operation with one discrete magnitude.

## Contribution

- Claimed: A lite augmentation search space with 25 candidate operations and 5 magnitude levels improves policy sampling efficiency.
- Claimed: A three-step bi-level optimization scheme alternately updates detector parameters and augmentation parameters without a separate retraining stage.
- Claimed: Policy gradient sampling estimates gradients for non-differentiable augmentation operations.
- Shown: ALADA outperforms compared augmentation methods on Tianchi-TILE, GC10-DET, and NEU-DET for both FRCNN and RetinaNet.

## Method

- Search space: 25 photometric, geometric, and bounding-box-aware operations with 5 magnitude levels, for 125 possible policies.
- Optimization: split the original training set into new training and validation sets, sample multiple augmentation policies, update detector parameters from augmented training batches, update augmentation weights from validation gradients, then update detector parameters again.
- Detector baselines: FRCNN and RetinaNet with ResNet50 backbones pretrained on ImageNet and FPN necks.
- Training optimizer: SGD with momentum 0.9 and weight decay 0.0001.
- Search settings: augmentation learning rate 0.001; sampling trajectories M = 4 for Tianchi-TILE and M = 8 for GC10-DET and NEU-DET.
- Implementation: MMDetection on a single NVIDIA RTX 3080 GPU.

## Evidence

### Experimental Setup

- Datasets: [[Tianchi-TILE]], [[GC10-DET]], [[NEU-DET]]
- Splits: all three datasets use a 7:3 train/test split; the original training split is further divided 1:1 into new training and validation sets for ALADA.
- Preprocessing: images are resized to 1500 x 1500 for Tianchi-TILE, 250 x 512 for GC10-DET, and 256 x 256 for NEU-DET.
- Metric: [[mAP]] with VOC-format annotations and IoU threshold 0.5.
- Baseline augmentations: no augmentation, MixUp, Mosaic, AutoAugment, TrivialAugment, and DADA.

### Main Results

| Dataset | Detector | No augmentation | ALADA | Source comparison |
|---|---|---:|---:|---|
| [[Tianchi-TILE]] | FRCNN | 52.39 mAP | 54.74 mAP | Best among compared augmentations |
| [[Tianchi-TILE]] | RetinaNet | 54.27 mAP | 55.85 mAP | Best among compared augmentations |
| [[GC10-DET]] | FRCNN | 69.60 mAP | 71.23 mAP | Best among compared augmentations |
| [[GC10-DET]] | RetinaNet | 63.75 mAP | 67.91 mAP | Best among compared augmentations |
| [[NEU-DET]] | FRCNN | 77.88 mAP | 78.48 mAP | Best among compared augmentations |
| [[NEU-DET]] | RetinaNet | 74.48 mAP | 76.34 mAP | Best among compared augmentations |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | Defect object detection | Mean average precision in VOC-style evaluation, with detections correct if IoU with ground truth is greater than 0.5 | higher | yes | Used across all three datasets and both detector baselines. |

### Ablations

- Lite search space: enlarging policies from one to three operations increases the search space and hurts sampling validity.
- Retraining: the source reports that retraining with top searched policies can degrade mAP without hyperparameter tuning; ALADA removes this retraining stage.
- Sampling trajectories: increasing M improves mAP until the chosen cost/accuracy trade-off of M = 4 for Tianchi-TILE and M = 8 for GC10-DET and NEU-DET.
- Learning rate: eta = 0.001 gives the best Tianchi-TILE result in the reported augmentation-learning-rate sweep.

## Data

- [[Tianchi-TILE]]: 3,613 high-resolution ceramic tile defect images covering edge anomalies, corner anomalies, white dots, light blocks, dark spots, aperture defects, marker defects, and scratches.
- [[GC10-DET]]: 2,294 metallic defect images from steel sheets, with ten defect categories and 2048 x 1000 image resolution.
- [[NEU-DET]]: 1,800 steel surface defect images, six classes, and 300 images per class.
- The paper treats these as a multi-industry benchmark set spanning ceramic tile and steel/metal surface defects.

## Evaluation

- ALADA is compared with MixUp, Mosaic, AutoAugment, TrivialAugment, and DADA under the same detector hyperparameters.
- Against DADA, ALADA reports mAP gains of 3.1, 3.61, and 0.3 points on Tianchi-TILE, GC10-DET, and NEU-DET in the search-method comparison.
- Basic brightness and rotation augmentations are not universal across datasets; brightness hurts Tianchi-TILE in the reported comparison, while ALADA improves the baseline.
- Visualization shows ALADA reducing missed detections under textured background, uneven brightness, low contrast, and intraclass difference cases.

## Limitations

- Candidate augmentation operations are based on basic image-processing techniques.
- The authors identify specialized industrial augmentation operations, GAN integration, and YOLO-specific automatic augmentation as future work.
- YOLO integration is not handled; the source notes YOLO-specific computational burden and custom augmentation schedules as challenges.

## Reproducibility

- Code: not reported.
- Data: the evaluated datasets are named; the article data-availability statement says the authors do not have permission to share data.
- Hyperparameters: detector, search-space, sampling, optimizer, and augmentation learning-rate settings are reported.
- Random seeds: not reported.
- Environment: MMDetection and single NVIDIA RTX 3080 GPU.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Object detection]]
- Methods: [[ALADA]], [[Data augmentation]], [[Automatic data augmentation]], [[Policy gradient sampling]], [[Deep convolutional neural network]]
- Datasets: [[Tianchi-TILE]], [[GC10-DET]], [[NEU-DET]]
- Benchmarks: [[Tianchi-TILE]], [[GC10-DET]], [[NEU-DET]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mAP]]
- Concepts: [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] | Contrasts with | Both address limited industrial defect data with augmentation, but ALADA searches basic detection augmentations while Con-GAN learns synthetic defect images for recognition. |

### Backlinks Updated

- [[Tianchi-TILE]], [[GC10-DET]], and [[NEU-DET]] link this paper as an ALADA benchmark user.
- [[Data augmentation]] links this paper as an automatic augmentation example for defect detection.
- [[mAP]] links this paper as a detection metric example.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[ALADA]] | Created | Source method and experimental sections |
| [[Tianchi-TILE]] | Created | Source dataset section |
| [[GC10-DET]] | Updated | Source dataset section |
| [[NEU-DET]] | Updated | Source dataset section |
| [[mAP]] | Updated | Source evaluation metric section |

## Questions

- How would ALADA perform with augmentation operations specialized for particular industrial defects?
- Can the same optimization scheme be adapted cleanly to YOLO-style augmentation schedules?
