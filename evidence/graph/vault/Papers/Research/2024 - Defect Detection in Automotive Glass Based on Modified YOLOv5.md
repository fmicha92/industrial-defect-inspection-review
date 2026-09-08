---
title: "Defect detection in automotive glass based on modified YOLOv5 with multi-scale feature fusion and dual lightweight strategy"
aliases:
  - "Modified YOLOv5 automotive glass defect detection"
paper_key: "doi:10.1007/s00371-023-03225-x"
paper_type: "research"
year: 2024
venue: "The Visual Computer"
authors:
  - "Zhe Chen"
  - "Shihao Huang"
  - "Hui Lv"
  - "Zhixue Luo"
  - "Jinhao Liu"
status: "processed"
topics:
  - "automotive glass inspection"
  - "YOLOv5"
  - "lightweight object detection"
tasks:
  - "[[Diverse glass surface defect detection]]"
datasets:
  - "[[AuGD]]"
methods:
  - "[[YOLOv5]]"
  - "[[MobileNet]]"
  - "[[Ghost module]]"
  - "[[Multi-scale feature fusion]]"
  - "[[Pseudo-labeling]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[GFLOPs]]"
primary_metric: "[[mAP@0.50]]"
related_domains:
  - "[[Glass inspection]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
doi: "10.1007/s00371-023-03225-x"
url: "https://doi.org/10.1007/s00371-023-03225-x"
pdf: "paper-inbox/10_processed/Research/2024 - Chen - Defect Detection in Automotive Glass Based on Modified YOLOv5.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Chen - Defect Detection in Automotive Glass Based on Modified YOLOv5.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Chen - Defect Detection in Automotive Glass Based on Modified YOLOv5.txt"
---
# Defect Detection in Automotive Glass Based on Modified YOLOv5

## Summary

The paper proposes a lightweight YOLOv5s variant for automotive glass defect detection. It addresses two deployment constraints: scarce labeled defect samples and the need for a compact detector suitable for resource-constrained industrial hardware. The final model combines pseudo-labeling, Mosaic augmentation, a MobileNetV3 backbone, Ghost modules in the neck, and a multi-scale feature-fusion module with coordinate attention. On the paper's automotive-glass dataset, the final model reports 94.1% mAP@0.5, 96.8% precision, 90.6% recall, and 3.7 GFLOPs.

## Paper Type

Research paper. It proposes and evaluates a modified object detector for automotive glass inspection, with a paper-specific dataset reported as available from the corresponding author on reasonable request.

## Problem

Automotive glass inspection is difficult because glass defects vary in shape, size, and distribution, while manual inspection is time-consuming and strains inspectors. Deep detectors can improve robustness, but automotive-glass defect samples are scarce and many accurate detectors are too large for edge deployment.

## Contribution

- Uses pseudo-labeling plus traditional data augmentation to expand scarce labeled automotive-glass defect samples.
- Replaces the YOLOv5 backbone with MobileNetV3 to reduce model complexity.
- Adds Ghost modules in the neck network to reduce computation while preserving feature information.
- Introduces an M-SFF module with coordinate attention to fuse semantic and location information.
- Reports ablations for pseudo-labeling, backbone choices, lightweight modules, and multi-scale feature fusion.

## Method

### Dataset Preparation

- The paper uses a self-built automotive-glass defect dataset.
- 210 automotive-glass photographs were collected in the field.
- Manual interception produced 1,600 datasets/images in the paper's wording.
- Traditional augmentation and pseudo-labeling expanded the final automotive-glass defect dataset to 7,100 samples.
- Data availability is by reasonable request from the corresponding author.

### Pseudo-labeling

- A small labeled subset is augmented with Mosaic and traditional augmentations.
- YOLOv5s is trained on labeled data to generate pseudo-label predictions for unlabeled images.
- Images meeting confidence criteria are retained and automatically labeled; lower-confidence predictions are discarded.
- The paper selected a confidence threshold of 0.5 after experiments.

### Model Architecture

- Base model: YOLOv5s.
- Backbone: MobileNetV3 replaces the original CSPDarknet-style feature extractor.
- Neck: Ghost modules replace ordinary convolution in the feature-fusion neck.
- Feature fusion: M-SFF merges shallow spatial information and deeper semantic information.
- Attention: coordinate attention is used inside M-SFF to capture horizontal and vertical positional information.

### Training Setup

- Framework: Python 3.7, PyTorch 1.9.1, CUDA 11.2.
- CPU: Intel Core i7-11700K.
- GPU: RTX 3060 Ti.
- Memory: 16 GB.
- Image size: 640 x 640.
- Learning rate: 0.01.
- Optimizer: Adam.
- Batch size: 16.
- Epochs: 100.

## Evidence

### Pseudo-labeling Effect

| Method | mAP@0.5 | Precision | Recall |
|---|---:|---:|---:|
| YOLOv5s | 78.8% | 90.5% | 65.5% |
| YOLOv5s + pseudo-label | 90.2% | 97.1% | 83.0% |

The paper reports pseudo-labeling improved mAP by 11.4 percentage points, precision by 6.6 percentage points, and recall by 17.5 percentage points.

### Backbone Comparison

| Model | mAP@0.5 | Precision | Recall | FLOPs |
|---|---:|---:|---:|---:|
| YOLOv5s | 90.2% | 97.1% | 83.0% | 15.8 G |
| YOLOv5s-MobileNetV3 | 90.0% | 96.8% | 82.7% | 5.9 G |
| YOLOv5s-ShuffleNetV2 | 84.4% | 95.1% | 72.2% | 5.6 G |
| YOLOv5s-PPLCNet | 88.1% | 95.4% | 79.8% | 5.8 G |

### Final Ablation Result

The final YOLOv5s + MobileNetV3 with SPPF + Ghost neck + M-SFF model reports 94.1% mAP@0.5, 96.8% precision, 90.6% recall, and 3.7 GFLOPs. Compared with the original YOLOv5s in the ablation table, the final model raises mAP by 3.9 percentage points and recall by 7.6 percentage points while reducing FLOPs by 76.6%.

## ML/DL Extraction

- Task formulation: object detection of automotive-glass surface defects.
- Input: automotive glass images, resized to 640 x 640.
- Output: defect bounding boxes and classes.
- Model family: YOLOv5 one-stage object detection.
- Augmentation: Mosaic, random flipping, scaling, cropping, brightness/darkness/noise changes, and pseudo-labeling.
- Architecture changes: MobileNetV3 backbone, Ghost neck, M-SFF with coordinate attention.
- Metrics: [[mAP@0.50]], [[Precision]], [[Recall]], [[GFLOPs]], and model weight size.
- Baselines: YOLOv5s, MobileNetV3, ShuffleNetV2, PPLCNet, and mainstream detectors including YOLOv3, YOLOv4, YOLOx, and YOLOv7.
- Code: not reported.
- Data: available from corresponding author on reasonable request.

## Limitations

- The paper addresses four common defect types and explicitly notes that additional and more intricate defect categories require further validation.
- The dataset is self-built and not openly released in the paper.
- The paper reports aggregate detection metrics but not per-defect-class performance in the extracted text.
- Industrial deployment is argued from model size and FLOPs; production-line latency and hardware deployment tests are not fully reported.

## Connections

### Graph Hubs

- Tasks: [[Diverse glass surface defect detection]]
- Datasets: [[AuGD]]
- Methods: [[YOLOv5]], [[MobileNet]], [[Ghost module]], [[Multi-scale feature fusion]], [[Pseudo-labeling]]
- Metrics: [[mAP@0.50]], [[Precision]], [[Recall]], [[GFLOPs]]
- Domains: [[Glass inspection]]

### Shares Dataset

- [[AuGD]]: the GSDNet source table points to this paper as the automotive-glass dataset source.

### Shares Task

- [[Diverse glass surface defect detection]]: the paper focuses on automotive-glass defect detection, one of the glass-surface contexts grouped by the task note.

### Shares Method

- [[YOLOv5]]: base object detector.
- [[MobileNet]]: used via MobileNetV3 to lightweight the backbone.
- [[Ghost module]]: used to reduce neck computation.
- [[Multi-scale feature fusion]]: proposed to fuse semantic and location features.
- [[Pseudo-labeling]]: used to expand scarce labeled samples.

### Shares Metric

- [[mAP@0.50]], [[Precision]], [[Recall]], and [[GFLOPs]] are reported in experiments and ablations.

### Application/domain

- [[Glass inspection]]: the paper targets automated inspection of automotive glass.

## Questions

- What are the four defect categories in the released/requestable dataset?
- Are the pseudo-labeled annotations included with the dataset available from the authors?
- What embedded hardware was targeted for deployment, and what was the measured inference latency?
