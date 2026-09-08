---
title: "An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features"
aliases:
  - "An End-to-End Steel Surface Defect Detection Approach"
  - "DDN NEU-DET paper"
paper_key: "doi:10.1109/tim.2019.2915404"
paper_type: dataset
year: 2020
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Yu He"
  - "Kechen Song"
  - "Qinggang Meng"
  - "Yunhui Yan"
status: processed
processed_at: 2026-06-05
topics:
  - steel surface defect detection
  - defect detection dataset
  - multilevel feature fusion
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-CLS]]"
  - "[[NEU-DET]]"
  - "[[ImageNet]]"
methods:
  - "[[Defect Detection Network]]"
  - "[[Multilevel feature fusion network]]"
  - "[[Faster R-CNN]]"
  - "[[ResNet50]]"
metrics:
  - "[[mAP]]"
  - "[[Average precision]]"
  - "[[Recall]]"
  - "[[FPS]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "Precision: TP / (TP + FP)."
  - "Recall: TP / (TP + FN)."
  - "AP: defined in the paper as (Precision + Recall) / 2."
  - "mAP: mean AP across defect classes."
doi: "10.1109/TIM.2019.2915404"
url: "https://doi.org/10.1109/TIM.2019.2915404"
data: "NEU-DET reported opened by the authors; host page listed in the paper footnote."
artifact_status: "dataset reported available; code not reported"
related_datasets:
  - "[[NEU-CLS]]"
  - "[[NEU-DET]]"
  - "[[ImageNet]]"
related_tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
related_methods:
  - "[[Defect Detection Network]]"
  - "[[Multilevel feature fusion network]]"
  - "[[Faster R-CNN]]"
  - "[[ResNet50]]"
related_benchmarks:
  - "[[NEU-DET benchmark]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - He - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features.md"
extracted_text: "paper-inbox/90_processing/text/2020 - He - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features.txt"
pdf: "paper-inbox/10_processed/Dataset/2020 - He - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features.pdf"
source_file: "paper-inbox/10_processed/Dataset/2020 - He - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features.pdf"
tags:
  - paper
  - dataset
  - metal-inspection
---

# An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features

## Summary

- Introduces [[NEU-DET]] by adding XML bounding-box annotations to the earlier [[NEU-CLS]] hot-rolled steel strip surface defect classification dataset.
- Proposes [[Defect Detection Network]], an end-to-end steel surface defect detector that uses ResNet features, [[Multilevel feature fusion network]], RPN proposals, ROI pooling, and classifier/regressor heads.
- Reports 74.8 mAP with ResNet34 and 82.3 mAP with ResNet50 on [[NEU-DET]] using 300 proposals, with a 50-proposal setting reaching 20 FPS on a single GPU while preserving about 92% of the 300-proposal performance.

## Paper Type

Dataset paper with a task-specific detection method. The paper upgrades the original NEU surface defect classification data into [[NEU-DET]] and evaluates a new end-to-end detector on that benchmark.

## Problem

The paper frames automated steel plate defect inspection as a joint classification and localization problem. Classification alone cannot represent multiple defects, multiclass defects, overlapping defects, or the defect locations needed for downstream quality assessment. Traditional hand-crafted feature pipelines are described as subjective and often limited to coarse localization, while deep learning defect detection is constrained by scarce location-annotated industrial datasets.

## Contribution

- Claimed: [[Defect Detection Network]] integrates ResNet, RPN, ROI pooling, and a detector head to classify and localize steel surface defects end to end.
- Claimed: [[Multilevel feature fusion network]] combines lower- and higher-level CNN features so region proposals preserve more location detail than single-level high-level features.
- Shown: [[NEU-DET]] adds detection annotations to the earlier [[NEU-CLS]] dataset and supports training and evaluation of bounding-box steel surface defect detectors.

## Method

DDN processes a single-scale image through a ResNet backbone and extracts convolutional feature maps from multiple residual stages. MFN attaches branches to selected residual blocks, normalizes their resolution and dimensionality, and concatenates them into a multilevel feature map. An RPN slides over this feature representation using anchor ratios of 1:1, 1:2, and 2:1 and scales of 64^2, 128^2, 256^2, and 512^2. After NMS with an IoU threshold of 0.7, the top-ranked proposals are transformed by ROI pooling and global average pooling, then passed to classification and bounding-box regression heads.

Training uses ImageNet-pretrained ResNet34 or ResNet50, stochastic gradient descent with weight decay 0.0001 and momentum 0.9, one image per minibatch, 64 ROIs for detector training, 128 ROIs for RPN training, 200k iterations at learning rate 0.001, and 100k more at 0.0001. The loss combines softmax classification with smooth-L1 localization and uses a localization weight of 2. The paper reports rotation, reflection, and shift augmentation and removes dropout.

## Evidence

| Evidence | Reported detail |
|---|---|
| Source classification dataset | [[NEU-CLS]], opened seven years earlier by the authors' group |
| Detection dataset | [[NEU-DET]] |
| Images | 1,800 grayscale images, 300 per class |
| Defect classes | crazing, inclusion, patches, pitted surface, rolled-in scale, scratches |
| Detection annotations | XML files with class labels and top-left / bottom-right bounding-box coordinates |
| Ground-truth boxes | nearly 5,000 total |
| Split | 1,260 training images and 540 test images |
| Baselines | [[Faster R-CNN]], HyperNet, and comparable ResNet34/50 Faster R-CNN settings |
| Best headline result | DDN + ResNet50 reaches 82.3 mAP on NEU-DET with 300 proposals |

### Performance Metrics

| Metric | Dataset / task | Direction | Primary? | Reported values |
|---|---|---|---|---|
| [[mAP]] | [[NEU-DET]] object detection | Higher is better | yes | DDN + ResNet34: 74.8; DDN + ResNet50: 82.3 with 300 proposals. |
| [[mAP]] | [[NEU-DET]] object detection with VGG16 baseline | Higher is better | yes | DDN: 76.6; HyperNet: 74.8; Faster R-CNN: 72.3. |
| [[mAP]] | DDN vs Faster R-CNN under ResNet34/50 | Higher is better | yes | DDN is 4.6/4.4 mAP points higher than Faster R-CNN under ResNet34/50. |
| [[FPS]] | [[NEU-DET]] detection speed | Higher is better | no | With 50 proposals, DDN detects at 20 FPS on a single GPU and keeps about 92% of the 300-proposal performance. |
| Classification accuracy | [[NEU-CLS]] | Higher is better | no | DDN reaches 99.67% defect classification accuracy. |

## ML/DL Extraction

- Task formulation: classify and localize steel surface defects with bounding boxes and defect class scores.
- Input: grayscale hot-rolled steel strip surface images.
- Output: one-of-C defect class prediction plus bounding-box coordinates for each ROI.
- Architecture: ResNet34/50 backbone, [[Multilevel feature fusion network]], RPN, ROI pooling, global average pooling, fully connected classification and localization heads.
- Objective/loss: softmax classification loss plus smooth-L1 localization loss, with localization enabled for positive samples and weighted by lambda = 2.
- Training data: [[NEU-DET]], derived from [[NEU-CLS]] with XML detection annotations.
- Pretraining: [[ImageNet]]-pretrained ResNet.
- Augmentation: rotation, reflection, and shift.
- Optimizer: SGD with momentum 0.9 and weight decay 0.0001.
- Evaluation protocol: fixed 1,260 / 540 train/test split on NEU-DET; metrics include AP, mAP, recall-style proposal analysis, and FPS.
- Compute/hardware: single GPU for the 20 FPS report; GPU model is not reported.
- Code availability: not reported.
- Data availability: NEU dataset website is listed in a paper footnote.

## Limitations

- The paper states that discontinuous, confusing, similar-overlapping, and scattered defects remain failure cases.
- Manual bounding-box annotation is expensive; the authors identify data augmentation as future work.
- The paper notes that more detection data may improve AP, but other kinds of data may not transfer well after ImageNet pretraining.
- The source does not report a license for NEU-DET.
- The source does not report code availability.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]], [[Object detection]]
- Datasets: [[NEU-CLS]], [[NEU-DET]], [[ImageNet]]
- Benchmark: [[NEU-DET benchmark]]
- Methods: [[Defect Detection Network]], [[Multilevel feature fusion network]], [[Faster R-CNN]], [[ResNet50]]
- Metrics: [[mAP]], [[Average precision]], [[Recall]], [[FPS]]
- Domains: [[Metal inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Shares dataset and task | Both evaluate detectors on [[NEU-DET]] for metallic surface defect detection; Lv et al. also introduce [[GC10-DET]]. |
| [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] | Follow-up usage | Evaluates a YOLOv5-based detector on [[NEU-DET]] after this paper introduced the detection annotations. |
| [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] | Follow-up usage | Uses NEU-DET to evaluate automatic data augmentation for industrial defect detection. |

## Questions

- Does the public NEU host still expose the exact NEU-DET XML annotation package, or only the original NEU surface defect database landing page?
- What license or redistribution terms apply to NEU-DET?
