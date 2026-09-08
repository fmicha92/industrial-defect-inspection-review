---
title: "Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model"
paper_key: "doi:10.1088/1361-6501/ad5b7c"
paper_type: research
year: 2024
venue: "Measurement Science and Technology"
authors:
  - "Liyuan Lin"
  - "Aolin Wen"
  - "Ying Wang"
  - "Shuxian Zhao"
  - "Shun Zhang"
  - "Jingpeng Yan"
  - "Yuan Zhou"
  - "Weibin Zhou"
status: processed
processed_at: 2026-06-11
topics:
  - "strip steel surface defect detection"
  - "data augmentation"
tasks:
  - "[[Defect detection]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[X-SDD]]"
methods:
  - "[[GT-CutMix]]"
  - "[[Data augmentation]]"
metrics:
  - "[[mAP]]"
primary_metric: "[[mAP]]"
baselines:
  - "SSD"
  - "DSSD"
  - "RetinaNet"
  - "YOLOv5"
  - "Faster R-CNN"
  - "Mask R-CNN"
doi: "10.1088/1361-6501/ad5b7c"
url: "https://doi.org/10.1088/1361-6501/ad5b7c"
pdf: "paper-inbox/10_processed/Research/2024 - Lin - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model.pdf"
code: "not reported"
data: "X-SDD availability not reported; NEU-DET is public"
related_methods:
  - "[[GT-CutMix]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-DET]]"
  - "[[X-SDD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect detection]]"
source_file: "paper-inbox/10_processed/Research/2024 - Lin - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Lin - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Lin - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model.txt"
tags:
  - paper
---
# Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model

## Summary

The paper combines [[GT-CutMix]] data augmentation with improved DSSD-style steel surface object detection. GT-CutMix samples labeled defect regions and inserts them into same-class images to rebalance scarce defects. The paper evaluates augmentation on X-SDD and then reports an improved detector, SA-DSSD, on X-SDD and [[NEU-DET]].

## Paper Type

- Type: research.
- Why: The paper proposes an augmentation algorithm and detector changes, then reports quantitative object-detection results.

## Problem

- Task: [[Defect detection]] for strip-steel surfaces.
- Setting: [[Metal inspection]] with class imbalance and sparse labeled defect examples.
- Inputs: steel surface images with bounding-box annotations.
- Outputs: defect boxes and classes.

## Contribution

- Claimed: [[GT-CutMix]] improves strip-steel detector training by inserting ground-truth defect regions rather than arbitrary image patches.
- Shown: On X-SDD, GT-CutMix raises mAP for DSSD from 67.78 to 72.75 and for Faster R-CNN from 68.52 to 74.39.
- Shown: SA-DSSD reports 74.88 mAP on [[NEU-DET]] with 40 FPS.

## Method

- Augmentation: GT sampling, basic image augmentation, in-class mixed augmentation, and defect-region integration into original images.
- Detector: S-DSSD replaces the DSSD ResNet101 backbone with SI-MobileNet; SA-DSSD adds a PSA prediction module.
- Training: PyTorch, Python 3.8, CUDA 10.2, Ubuntu 18.04, NVIDIA GeForce RTX A5000; SGD with momentum 0.9, weight decay 0.0001, batch size 16, learning rate 0.001, 100 epochs.

## Evidence

| Result | Dataset / task | Metric | Baseline | After augmentation / method | Notes |
|---|---|---|---:|---:|---|
| GT-CutMix with SSD | [[X-SDD]] detection | [[mAP]] | 72.64 | 73.70 | Augmentation comparison. |
| GT-CutMix with DSSD | [[X-SDD]] detection | [[mAP]] | 67.78 | 72.75 | Augmentation comparison. |
| GT-CutMix with RetinaNet | [[X-SDD]] detection | [[mAP]] | 73.84 | 75.73 | Augmentation comparison. |
| GT-CutMix with YOLOv5 | [[X-SDD]] detection | [[mAP]] | 76.10 | 76.50 | Augmentation comparison. |
| GT-CutMix with Faster R-CNN | [[X-SDD]] detection | [[mAP]] | 68.52 | 74.39 | Augmentation comparison. |
| GT-CutMix with Mask R-CNN | [[X-SDD]] detection | [[mAP]] | 64.61 | 69.38 | Augmentation comparison. |
| Final detector | [[X-SDD]] detection | [[mAP]] | DSSD 72.75 | SA-DSSD 78.63 | GT-CutMix augmented setting. |
| Cross-dataset detector | [[NEU-DET]] detection | [[mAP]] | DSSD 71.01 | SA-DSSD 74.88 | 40 FPS reported. |

## Dataset / Benchmark Details

- [[X-SDD]]: 1,360 hot-rolled strip-steel images, seven defect types, 940 training images, 420 test images.
- [[NEU-DET]]: 1,800 images, six hot-rolled steel strip defect classes, 300 images per class.

## Limitations

- The paper reports that GT-CutMix can create in-class mixed defects that make one defect class resemble another, increasing misclassification.
- Code availability: not reported.
- X-SDD host URL and license: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect detection]], [[Metallic surface defect detection]]
- Methods: [[GT-CutMix]], [[Data augmentation]]
- Datasets: [[NEU-DET]], [[X-SDD]]
- Domains: [[Metal inspection]]
- Metrics: [[mAP]]

### Relationship Notes

- Shares dataset: [[NEU-DET]] and [[X-SDD]].
- Shares method: [[GT-CutMix]] and [[Data augmentation]].
- Shares metric: [[mAP]].
- Application/domain: [[Metal inspection]].

## Questions

- Does GT-CutMix preserve physically plausible defect context across all X-SDD classes?
- How much of SA-DSSD's NEU-DET gain comes from detector architecture rather than augmentation?
