---
title: "NHD-YOLO: Improved YOLOv8 using optimized neck and head for product surface defect detection with data augmentation"
aliases:
  - "NHD-YOLO"
paper_key: "doi:10.1049/ipr2.13073"
paper_type: research
year: 2024
venue: "IET Image Processing"
authors:
  - "Faquan Chen"
  - "Hui Gao"
  - "Miaolei Deng"
  - "Xiaoya Yang"
  - "Dexian Zhang"
status: processed
processed_at: 2026-06-11
topics:
  - "surface defect detection"
  - "small object detection"
  - "YOLOv8"
  - "copy-paste augmentation"
tasks:
  - "[[Defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[PKU-Market-PCB]]"
methods:
  - "[[NHD-YOLO]]"
  - "[[YOLOv8]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
architectures:
  - "[[YOLOv8]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.75]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  - "AP: COCO-style average precision over IoU thresholds; higher is better"
  - "AP50/AP75: average precision at 0.50 and 0.75 IoU; higher is better"
baselines:
  - "YOLOv8 variants"
  - "CA-AutoAssign"
  - "CANet"
  - "AP-Net"
  - "Faster R-CNN"
  - "Libra R-CNN"
  - "YOLOF"
  - "YOLOv5x"
  - "AGCA-YOLOv5x"
  - "YOLOXx"
doi: "10.1049/ipr2.13073"
url: "https://doi.org/10.1049/ipr2.13073"
data: "[[NEU-DET]], [[PKU-Market-PCB]], COCO"
code: "not reported"
related_methods:
  - "[[NHD-YOLO]]"
  - "[[YOLOv8]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-DET]]"
  - "[[PKU-Market-PCB]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect detection]]"
  - "[[Object detection]]"
source_file: "paper-inbox/10_processed/Research/2024 - Chen - NHD-YOLO Improved YOLOv8 using optimized neck and head for product surface defect detection with data augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Chen - NHD-YOLO Improved YOLOv8 using optimized neck and head for product surface defect detection with data augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Chen - NHD-YOLO Improved YOLOv8 using optimized neck and head for product surface defect detection with data augmentation.txt"
artifact_status: "code not reported; public/benchmark datasets used"
tags:
  - paper
---
# NHD-YOLO: Improved YOLOv8 using optimized neck and head for product surface defect detection with data augmentation

## Summary

The paper proposes [[NHD-YOLO]], an improved [[YOLOv8]] detector for industrial surface defects. The design modifies the feature neck, detection head, and training data: a shortcut feature pyramid network improves feature flow, an adaptive decoupled head aligns classification and regression features, and selective small object copy-paste augmentation adds small defect instances during training. The main evidence is on [[NEU-DET]], with additional generalization checks on [[PKU-Market-PCB]] and COCO.

## Paper Type

- Type: research.
- Why: The paper proposes an object detector and evaluates it against YOLOv8 and other detector baselines.

## Problem

- Task: [[Defect detection]] / [[Object detection]] for small and dense industrial defects.
- Setting: hot-rolled steel strip defects and PCB surface defects.
- Motivation: YOLOv8 is fast but can miss small defects and suffers from classification/regression feature misalignment.

## Contribution

- Claimed: SFPN improves transmission of low-level and high-level features.
- Claimed: ADH reduces spatial misalignment between classification and localization features.
- Claimed: SSOCP, a selective small object copy-paste augmentation method, improves small-object defect detection.
- Shown: NHD-YOLO improves AP over YOLOv8 variants on NEU-DET and PKU-Market-PCB, with especially large gains in APS.

## Method

- Base model: [[YOLOv8]].
- Neck: shortcut feature pyramid network (SFPN).
- Head: adaptive decoupled head (ADH) with prior classification and regression branches and deformable convolution offsets.
- Augmentation/synthesis: selective small object copy-paste (SSOCP). Objects below a 64^2 area threshold are copied, optionally using masks when available, and inserted with an IoU filter threshold of 0.2.
- Training: OpenMMLab implementation; YOLO models trained for 150 epochs with batch size 4 on a Tesla V100 32 GB GPU for NEU-DET; SGD learning rate 0.0025 and weight decay 0.0005.

## Data

- [[NEU-DET]]: 1,800 hot-rolled steel strip images, 200 x 200 pixels, six classes: inclusion, rolled-in scale, scratches, crazing, patches, and pitted surface. Split: 1,260 training and 540 testing images.
- [[PKU-Market-PCB]]: 693 original printed circuit board images across spurious copper, short, open circuit, missing hole, mouse bite, and spur. Split: 493 training and 200 testing images, resized to 640 x 640.
- COCO: 118,000 training images and 5,000 validation images; used as a generic object-detection generalization check.

## Evidence

### NEU-DET Results

| Model | AP | AP50 | AP75 | APS | APM | APL | FPS | Params |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| YOLOv8s | 38.5 | 71.4 | 34.6 | 24.3 | 31.1 | 47.9 | 62.1 | 138.17M |
| NHD-YOLOs | 39.6 | 72.6 | 35.6 | 31.3 | 33.1 | 50.6 | 58.5 | 179.65M |
| YOLOv8x | 39.5 | 74.0 | 35.8 | 29.0 | 32.9 | 49.6 | 46.9 | 806.93M |
| NHD-YOLOx | 40.8 | 74.3 | 37.6 | 33.6 | 33.7 | 51.8 | 44.6 | 1025.14M |

### Baseline vs Augmentation / Synthesis

| Setting | Baseline result | After method / augmentation | Metric | Delta |
|---|---:|---:|---|---:|
| YOLOv8s baseline | 38.5 | 39.6 with SFPN + ADH + SSOCP | AP | +1.1 |
| YOLOv8s + SFPN + ADH | 26.9 | 31.3 with SSOCP | APS | +4.4 |
| YOLOv8s on PKU-Market-PCB | 47.8 | 49.2 with NHD-YOLOs | AP | +1.4 |
| YOLOv8s on COCO | 42.2 | 43.7 with NHD-YOLOs | AP | +1.5 |

### Ablation on NEU-DET

| Variant | AP | AP50 | AP75 | APS | APM | APL |
|---|---:|---:|---:|---:|---:|---:|
| YOLOv8s baseline | 38.5 | 71.4 | 34.6 | 24.3 | 31.1 | 47.9 |
| + SFPN | 38.9 | 71.4 | 35.9 | 24.5 | 32.2 | 48.3 |
| + SFPN + ADH | 39.5 | 72.6 | 36.1 | 26.9 | 32.6 | 50.6 |
| + SFPN + ADH + SSOCP | 39.6 | 72.6 | 35.6 | 31.3 | 33.1 | 50.6 |

## ML / DL Extraction

- Task formulation: bounding-box defect detection.
- Input: 200 x 200 NEU-DET images and 640 x 640 resized PCB/COCO images.
- Architecture: YOLOv8 with SFPN and ADH.
- Loss/objective: not fully specified beyond YOLOv8 training setup.
- Optimizer: [[Stochastic gradient descent]].
- Augmentation: SSOCP small-object copy-paste.
- Baselines: YOLOv8 variants and multiple object detectors.
- Metrics: [[Average precision]], [[mAP@0.50]], [[mAP@0.75]], APS/APM/APL, FPS, parameters.
- Code: not reported.

## Limitations

- NHD-YOLO improves accuracy but adds parameters and reduces inference speed relative to YOLOv8.
- The authors identify remaining challenges in detection accuracy and speed.
- Future work: efficient attention modules, model pruning, and quantization.

## Connections

### Graph Hubs

- Tasks: [[Defect detection]], [[Object detection]]
- Methods: [[NHD-YOLO]], [[YOLOv8]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[NEU-DET]], [[PKU-Market-PCB]]
- Domains: [[Metal inspection]]
- Metrics: [[Average precision]], [[mAP@0.50]], [[mAP@0.75]]

### Relationship Notes

- Shares dataset: [[NEU-DET]] with steel surface defect detection papers.
- Shares task: [[Defect detection]] and [[Object detection]].
- Shares method: [[YOLOv8]], [[Data augmentation]], and [[Synthetic data generation]] through copy-paste augmentation.
- Application/domain: [[Metal inspection]].

## Questions

- How much of the AP gain comes from SSOCP alone under larger model sizes?
- Does SSOCP preserve realistic defect context when masks are unavailable and bounding boxes are pasted?
- Are code and trained model weights available outside the paper?
