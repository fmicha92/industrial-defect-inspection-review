---
title: "MSFT-YOLO: Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface"
aliases:
  - "MSFT-YOLO"
paper_key: "sha256:71400e99d5a28196dd178421e4cf5112ae8647962db180f9014895b2cdc0715a"
paper_type: research
year: 2022
venue: "Sensors"
authors:
  - "Zexuan Guo"
  - "Chensheng Wang"
  - "Guang Yang"
  - "Zeyuan Huang"
  - "Guo Li"
status: processed
processed_at: 2026-05-22
topics:
  - "steel surface defect detection"
  - "YOLOv5"
  - "transformer module"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
methods:
  - "[[MSFT-YOLO]]"
  - "[[YOLOv5]]"
  - "[[Transformers]]"
  - "[[Multi-scale feature fusion]]"
model_family:
  - "YOLOv5l"
  - "transformer-enhanced one-stage detector"
metrics:
  - "[[mAP]]"
  - "[[FPS]]"
primary_metric: "[[mAP]]"
baselines:
  - "YOLOv3"
  - "YOLOv5"
  - "Faster R-CNN"
  - "RetinaNet"
code: "not reported"
data: "available on request from the corresponding author"
doi: "10.3390/s22093467"
arxiv: "not applicable"
url: "https://doi.org/10.3390/s22093467"
pdf: "paper-inbox/10_processed/Research/2022 - Guo - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Guo - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Guo - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Guo - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface.txt"
artifact_status: "data available on request; code not reported"
tags:
  - "paper"
  - "steel-surface-defect-detection"
  - "yolov5"
---

# MSFT-YOLO: Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface

## Summary

MSFT-YOLO is a YOLOv5l-based one-stage detector for steel surface defects. The paper targets cluttered backgrounds, easily confused defect categories, large scale changes, and poor small-defect detection in industrial steel imagery. It adds a Transformer-derived TRANS module to the end of the CSPDarknet backbone and to detection heads, replaces the YOLOv5 PANet neck with BiFPN-style weighted multi-scale fusion, and uses data augmentation plus multi-step training.

On [[NEU-DET]], the final model reports 0.752 mAP and 30.6 FPS in the main comparison table, compared with 0.682 mAP and 52.5 FPS for YOLOv5. The conclusion describes this as a 7.5 percentage-point mAP gain over the baseline while retaining real-time potential.

## Paper Type

- Type: research.
- Why: proposes a detector architecture and training strategy, then evaluates it against detector baselines on a steel surface defect benchmark.

## Problem

- Task: [[Metallic surface defect detection]], [[Object detection]].
- Setting: hot-rolled steel strip surface inspection.
- Inputs: grayscale steel surface images.
- Outputs: bounding boxes and defect classes for six NEU-DET defect categories.
- Motivation: ordinary convolutional detectors struggle with clutter, category confusion, scale variation, and small defects in industrial steel images.

## Contribution

- Proposes TRANS, a Transformer encoder block inserted at the end of the YOLOv5l backbone and in prediction heads to add global context.
- Replaces PANet with a BiFPN-style feature fusion neck using learnable weights for multi-scale feature integration.
- Adds dataset expansion and multi-step training, including MixUp, CutMix, Mosaic, and defect-free samples collected as a new class to reduce false detection.
- Shows higher mAP than YOLOv3, YOLOv5, Faster R-CNN, and RetinaNet on NEU-DET while maintaining 30.6 FPS.

## Method

- Base detector: YOLOv5l, selected because it had higher mAP than YOLOv5s and YOLOv5m in the paper's preliminary experiments while retaining deployment potential.
- Backbone: CSPDarknet53 with a TRANS module at the end; the authors avoid inserting TRANS in shallow backbone stages because it triggered boundary regression and lost useful context.
- Neck: BiFPN replaces PANet to combine high- and low-resolution features with learnable fusion weights.
- Heads: detection heads integrate TRANS modules to explore self-attention for prediction under dense and scale-varying defects.
- Training strategy: data preprocessing uses MixUp, CutMix, and Mosaic; multi-step training adds defect-free samples from detections as a new sample class.

## Evidence

### Experimental Setup

- Dataset: [[NEU-DET]], a Northeastern University hot-rolled steel strip surface defect dataset.
- Dataset size: 1800 grayscale images.
- Classes: crazing, inclusion, patches, pitted surface, rolled-in scale, and scratches.
- Per-class count: 300 samples per defect type.
- Metrics: [[mAP]] and [[FPS]].
- Optimizer: SGD with weight decay 0.0005 and momentum 0.937 by default.
- Learning rate schedule: warm-up then cosine annealing; 3 warm-up epochs with momentum 0.8; initial learning rate 0.02; trained for 200 epochs.

### Main Results

| Model | mAP | FPS | Notes |
|---|---:|---:|---|
| YOLOv3 | 0.496 | 61.2 | fastest but lowest mAP in Table 2 |
| YOLOv5 | 0.682 | 52.5 | baseline |
| Faster R-CNN | 0.713 | 24.0 | two-stage baseline |
| RetinaNet | 0.702 | 48.2 | one-stage baseline |
| MSFT-YOLO | 0.752 | 30.6 | best average result in Table 2 |

### Ablations

| Variant | mAP | FPS | Source-supported interpretation |
|---|---:|---:|---|
| YOLOv5l baseline | 0.682 | 52.5 | baseline |
| + TRANS backbone | 0.722 | 43.3 | improves several categories but reduces speed |
| + BiFPN | 0.732 | 41.2 | improves multi-scale handling |
| + Multi-step training | 0.757 | 29.1 | ablation table's final staged variant |

## Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | object detection accuracy | mean average precision across IoU thresholds from 0.50 to 0.95 in 0.05 steps | higher | yes | paper's main accuracy metric |
| [[FPS]] | real-time detection throughput | frames per second under the same hardware conditions | higher | no | used to judge industrial real-time potential |

## Dataset / Benchmark Details

- [[NEU-DET]] contains six typical hot-rolled steel strip surface defect classes.
- Each NEU-DET image can contain multiple defects.
- The paper reports the study data are available on request from the corresponding author.

## Limitations

- Evaluation is limited to NEU-DET in the reported experiments.
- The authors state future work should introduce richer datasets to enhance generalization capability.
- The authors also plan model compression for better adaptation to real-time industrial monitoring.
- Code availability is not reported in the source.

## Reproducibility

- Code: not reported.
- Data: available on request from the corresponding author.
- Training details: optimizer, schedule, epoch count, and several augmentations are reported.
- Hardware: FPS is reported, but the exact hardware for the detection-speed table is not specified in the extracted source.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]], [[Object detection]]
- Methods: [[MSFT-YOLO]], [[YOLOv5]], [[Transformers]], [[Multi-scale feature fusion]]
- Datasets: [[NEU-DET]]
- Domains: [[Metal inspection]]
- Metrics: [[mAP]], [[FPS]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[NEU-DET]] | Shares dataset | MSFT-YOLO evaluates on NEU-DET's six hot-rolled steel defect categories. |
| [[YOLOv5]] | Base detector | MSFT-YOLO is built from YOLOv5l and reports improvements over YOLOv5. |
| [[Faster R-CNN]] | Baseline | Table 2 compares MSFT-YOLO with Faster R-CNN on NEU-DET. |
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Shares dataset and task | Both evaluate metallic surface defect detection on NEU-DET. |

## Questions

- Does the method generalize beyond NEU-DET to other steel or metal inspection datasets?
- What exact hardware was used for the FPS comparison?
- How much of the final gain comes from adding defect-free samples versus the architecture changes?
