---
title: "You Only Look Once-Aluminum"
aliases:
  - "YOLO-AL"
  - "You Only Look Once-Aluminum: A Detection Model for Complex Aluminum Surface Defects Based on Improved YOLOv8"
paper_key: "sha256:742296c7dd255ab8b2561ea1cc762eb23947ea09ac99623c87ac7adeed8940a1"
doi: "10.3390/sym17050724"
url: "https://doi.org/10.3390/sym17050724"
pdf: "paper-inbox/10_processed/Research/2025 - Han - You Only Look Once-Aluminum.pdf"
source_file: "paper-inbox/10_processed/Research/2025 - Han - You Only Look Once-Aluminum.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Han - You Only Look Once-Aluminum.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Han - You Only Look Once-Aluminum.txt"
authors:
  - "Jiashu Han"
  - "Huiye Chen"
  - "Yitong Ding"
  - "Shudong Zhuang"
  - "Chengyu Zhou"
  - "Hua Chen"
year: 2025
venue: "Symmetry"
paper_type: "research"
status: "processed"
processed_at: "2026-06-05"
topics:
  - "aluminum surface defect detection"
  - "YOLOv8"
  - "industrial visual inspection"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[APDDD]]"
methods:
  - "[[YOLO-AL]]"
  - "[[YOLOv8]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[YOLOv8]]"
losses:
  - "Focaler-WIoU"
optimizers:
  - "not reported"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[mAP]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.50-0.95]]"
  - "[[GFLOPs]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "Faster R-CNN"
  - "SSD"
  - "CenterNet"
  - "RetainNet"
  - "FCOS"
  - "Damo-YOLO"
  - "YOLOv3-tiny"
  - "YOLOv5n"
  - "YOLOv8n"
  - "YOLOv10n"
  - "YOLOv11n"
  - "YOLOv12s"
code: "not reported"
data: "[[APDDD]]"
artifact_status: "paper says supporting data are available from the corresponding author upon request; APDDD host is recorded in the dataset note"
related_methods:
  - "[[YOLO-AL]]"
  - "[[YOLOv8]]"
related_datasets:
  - "[[APDDD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
---
# You Only Look Once-Aluminum

## Summary

The paper proposes [[YOLO-AL]], an improved YOLOv8n detector for complex aluminum surface defects. It evaluates on [[APDDD]], described as an Aliyun Tianchi aluminum-profile surface defect dataset with 3719 images, 5279 labeled boxes, and 10 defect categories.

## Paper Type

Research paper. It is primarily a detector-architecture paper, but it provides a detailed APDDD dataset description and a useful source anchor for the dataset note.

## Problem

Aluminum surface defect detection is difficult in industrial environments because defects can be subtle, low-resolution, small, strip-like, or imbalanced across easy and hard samples. The paper targets automated bounding-box detection of aluminum-profile surface defects for production inspection.

## Contribution

- Introduces [[YOLO-AL]], a YOLOv8n-based aluminum defect detector.
- Replaces early YOLOv8n C2f layers with C2f-US to improve low-resolution and small-object feature extraction.
- Adds CPMSCA attention for contextual and strip-like defect features.
- Replaces the neck with ODE-RepGFPN for multi-scale feature fusion.
- Uses Focaler-WIoU to focus learning on difficult boundary samples and address class imbalance.

## Dataset

[[APDDD]] is described as the Aluminum Profile Surface Detection Database from the Aliyun Tianchi competition. The paper reports 10 defect classes: non-conductive, scratch, corner-leaky-bottom, orange-peel, leaky-bottom, jet-stream, paint-bubble, pitting, variegated-color, and dirty-spots. It reports 3719 images, 5279 labeled frames, image resolution of 640 x 640, and a training/validation/test split of 7:1.5:1.5.

## Method

YOLO-AL starts from YOLOv8n. C2f-US combines a Universal Inverted Bottleneck with SPD-Conv and replaces the first two C2f layers in the backbone. CPMSCA is added at the end of the backbone and uses a class-symmetric attention design to extract multi-scale and strip-like features. ODE-RepGFPN replaces the original neck to fuse high-level semantics and low-level spatial information. Focaler-WIoU replaces the original loss to emphasize hard samples near positive/negative boundaries.

## Evidence

The main comparison reports [[YOLO-AL]] at 86.5% [[Precision]], 77.8% [[Recall]], 81.5% [[mAP@0.50]], 7.9 [[GFLOPs]], 3.4M parameters, and 212.9 [[FPS]] on [[APDDD]]. YOLOv8n is reported at 82.4% precision, 75.9% recall, 79.3% mAP@0.50, 8.1 GFLOPs, 3.0M parameters, and 202.3 FPS. YOLO-AL is also reported above YOLOv12s by 2.0 percentage points in precision and 2.9 percentage points in mAP@0.50.

Per-class results show strong performance on leaky-bottom, non-conductive, orange-peel, variegated-color, pitting, and corner-leaky-bottom classes, but paint-bubble remains difficult. The paper reports paint-bubble mAP of 39.6% for YOLO-AL and states that paint-bubble defects can cover only a few tens of pixels.

## Performance Metrics

- [[Precision]]: main YOLO-AL result is 86.5%.
- [[Recall]]: main YOLO-AL result is 77.8%.
- [[mAP@0.50]]: main YOLO-AL result is 81.5%.
- [[mAP@0.50-0.95]]: used in training curves and ablations; full YOLO-AL main-table value is not reported in the extracted table.
- [[GFLOPs]]: main YOLO-AL result is 7.9.
- [[FPS]]: main YOLO-AL result is 212.9.

## ML/DL Extraction

- Task formulation: bounding-box detection and classification of aluminum surface defects.
- Input: 640 x 640 aluminum defect images.
- Backbone: YOLOv8n with C2f-US replacing the first two C2f modules and CPMSCA at the end of the backbone.
- Neck: ODE-RepGFPN.
- Loss: Focaler-WIoU.
- Training: PyTorch 2.0.0, Python 3.8.10, CUDA 11.2, input resolution 640 x 640, initial learning rate 0.01, momentum 0.937, batch size 16, 8 threads, weight decay 0.0005, and 200 epochs.
- Augmentation: Mosaic data augmentation.
- Hardware: NVIDIA RTX 4090 GPU with 80 GB RAM, Ubuntu OS.
- Artifacts: code not reported; data availability statement says the data used to support the study are available from the corresponding author upon request.

## Limitations

- Paint-bubble defects remain difficult despite YOLO-AL having the highest reported value among compared methods.
- The paper does not evaluate domain shift, noise, vibration, or optical interference from real production lines.
- The paper calls for statistical significance testing and cross-validation for reliability across data partitions.
- The APDDD host is external to the paper; the paper itself states data are available from the corresponding author upon request.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]], [[Object detection]]
- Methods: [[YOLO-AL]], [[YOLOv8]]
- Datasets: [[APDDD]]
- Domains: [[Metal inspection]]
- Metrics: [[Precision]], [[Recall]], [[mAP]], [[mAP@0.50]], [[mAP@0.50-0.95]], [[GFLOPs]], [[FPS]]

### Shares Dataset

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] also reports APDDD results, but its primary focus is hot-rolled steel surface defect detection.

### Shares Method

- [[YOLOv8]] is the base detector family modified by YOLO-AL.
- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] also builds an improved YOLOv8-style detector for surface defects, but in smartphone screen inspection.

## Questions

- Which APDDD release or reconstruction exactly corresponds to the 3719-image, 5279-box dataset used in the paper?
- Are the APDDD train/validation/test partitions released, or were they generated by the authors?
- How robust is YOLO-AL under vibration, blur, optical interference, or domain shift from real aluminum production lines?
