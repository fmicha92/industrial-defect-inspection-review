---
title: "Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention and Multi-Scale Feature Bi-Directional Path Aggregation Network"
aliases:
  - "DY-YOLO smartphone screen surface defect detection"
paper_key: "doi:10.1038/s41598-025-24225-y"
paper_type: "research"
year: 2025
venue: "Scientific Reports"
authors:
  - "Jiaqi Li"
  - "Huadiao Long"
  - "Meiyan Liu"
  - "Yi Huang"
  - "Nengsheng Bao"
status: "processed"
topics:
  - "smartphone screen surface defect detection"
  - "real-time object detection"
tasks:
  - "[[Smartphone screen glass defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[MSD]]"
  - "[[SSGD]]"
methods:
  - "[[DY-YOLO]]"
  - "[[YOLOv8]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[DY-YOLO]]"
  - "[[YOLOv8]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[mAP]]"
  - "[[mAP@0.50]]"
  - "[[FPS]]"
  - "[[GFLOPs]]"
  - "[[Parameter count]]"
  - "[[Inference time]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.5: mean average precision at IoU threshold 0.5"
  - "mAP@0.5:0.95: mean average precision averaged over IoU thresholds from 0.50 to 0.95"
  - "F1-score: 2 * precision * recall / (precision + recall)"
baselines:
  - "YOLOv3"
  - "YOLOv5"
  - "YOLOv6"
  - "RTDETR"
  - "YOLOv8"
  - "YOLOv9"
  - "YOLOv10"
  - "YOLOv11"
  - "YOLOv12"
benchmarks:
  - "MSD"
  - "SSGD"
code: "not reported"
data: "https://github.com/jianzhang96/MSD; https://github.com/VincentHancoder/SSGD"
doi: "10.1038/s41598-025-24225-y"
arxiv: "not reported"
url: "https://doi.org/10.1038/s41598-025-24225-y"
pdf: "paper-inbox/10_processed/Research/2025 - Li - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention.pdf"
source_file: "paper-inbox/10_processed/Research/2025 - Li - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Li - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Li - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention.txt"
related_papers:
  - "[[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[DY-YOLO]]"
  - "[[YOLOv8]]"
related_datasets:
  - "[[MSD]]"
  - "[[SSGD]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
  - "[[Object detection]]"
processed_at: "2026-06-03"
---
# Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention and Multi-Scale Feature Bi-Directional Path Aggregation Network

## Summary

The paper proposes [[DY-YOLO]], a [[YOLOv8]]-based detector for smartphone cover-glass defect detection in reflective production environments. The model adds Dynamic-C2f for adaptive feature extraction, Dynamic-LSKA for suppressing reflection/background interference, HSF-BPAN for multi-scale feature fusion, and DySample for lightweight dynamic upsampling.

The paper evaluates DY-YOLO on [[MSD]] and [[SSGD]]. It reports 99.3% mAP@0.5 and 70.9% mAP@0.5:0.95 on MSD, 46.0% mAP@0.5 and 20.2% mAP@0.5:0.95 on SSGD, 3.0M parameters, 5.8 GFLOPs, 8.21 ms latency, and 121.8 FPS.

## Paper Type

Research paper. It proposes an object-detection architecture and evaluates it on public smartphone cover-glass defect benchmarks.

## Problem

Smartphone cover-glass inspection must detect scratches, cracks, chips, stains, light leakage, and other defects despite transparent and reflective glass backgrounds. Production deployment also requires real-time throughput; a detector that cannot keep pace with assembly-line inspection can become a bottleneck.

## Contribution

- Proposes [[DY-YOLO]], a YOLOv8-based detector for smartphone cover-glass defects.
- Adds Dynamic-C2f and Dynamic-LSKA modules to improve adaptive feature extraction and anti-interference under reflections and low-contrast defects.
- Adds HSF-BPAN and DySample for multi-scale feature aggregation with lower computation.
- Reports higher mAP than YOLOv3, YOLOv5, YOLOv6, RTDETR, YOLOv8, YOLOv9, YOLOv10, YOLOv11, and YOLOv12 on MSD and SSGD, while retaining real-time inference speed.

## Method

DY-YOLO keeps YOLOv8 as the baseline detector and modifies the backbone and neck. Dynamic-C2f replaces standard convolution in bottleneck blocks with dynamic convolution, where per-sample kernels are produced by a routing layer over multiple expert kernels. The paper uses sigmoid routing rather than softmax so multiple experts can be active simultaneously.

Dynamic-LSKA combines dynamic convolution with Large Separable Kernel Attention. It decomposes large kernels into horizontal and vertical depthwise convolutions, adds dilated convolution for wider context, and uses a 1 x 1 convolution to generate an attention map. HSF-BPAN uses channel/spatial attention to screen features, then performs top-down and bottom-up feature aggregation. DySample learns sampling offsets for adaptive upsampling, preserving fine defect edges more effectively than fixed interpolation.

## Evidence

### Datasets

| Dataset | Size | Defect classes | Split used | Notes |
|---|---:|---|---|---|
| [[MSD]] | 1200 images | oil stain, scratch, spot | 8:2 train/validation | 400 images per class, 1920 x 1080, industrial camera, LabelMe annotations |
| [[SSGD]] | 2504 images | crack, broken, spot, scratch, light-leakage, blot, broken-membrane | 8:2 train/validation | 1500 x 1000 images from professional acquisition equipment |

### Implementation

| Setting | Value |
|---|---|
| Framework | PyTorch |
| CPU | 13th Gen Intel Core i5-13400F |
| GPU | NVIDIA RTX 4070 12GB |
| RAM | 32GB |
| Optimizer | SGD |
| Batch size | 32 |
| Initial learning rate | 0.01 |
| Weight decay | 0.0005 |
| Scheduler | LambdaLR |
| Training augmentation | Mosaic, disabled in final ten epochs |
| Inference input | 640 x 640, batch size 1 |

### Performance Metrics

| Metric | Definition | Direction | Primary | Context |
|---|---|---|---|---|
| [[Precision]] | `TP / (TP + FP)` | higher | no | predicted-defect correctness |
| [[Recall]] | `TP / (TP + FN)` | higher | no | missed-defect control |
| [[mAP@0.50]] | mean AP at 0.5 IoU threshold | higher | yes | object-detection accuracy |
| [[mAP]] | average AP over IoU thresholds 0.50 to 0.95 | higher | no | stricter localization accuracy |
| [[F1-score]] | harmonic mean of precision and recall | higher | no | precision/recall balance |
| [[GFLOPs]] | floating-point operations per pass | lower | no | computational cost |
| [[Parameter count]] | trainable model parameters | lower | no | model size |
| [[Inference time]] | latency per image | lower | no | deployment speed |
| [[FPS]] | frames per second | higher | no | real-time throughput |

### Reported Results

| Dataset | Method | mAP@0.5 | mAP@0.5:0.95 | Avg recall |
|---|---|---:|---:|---:|
| MSD | DY-YOLO | 99.3 | 70.9 | 98.5 |
| SSGD | DY-YOLO | 46.0 | 20.2 | 46.2 |

DY-YOLO reports 3.0M parameters and 5.8 GFLOPs. At 640 x 640 input and batch size 1, it reports 8.21 ms latency and 121.8 FPS. The paper states that it reduces computational resource consumption by 33.3% compared with YOLOv8 while improving mAP.

### Ablations

- Enabling Dynamic-C2f, Dynamic-LSKA, and HSF-BPAN together gives the best reported overall performance on both MSD and SSGD.
- A Dynamic-C2f kernel size of 3 gives the best speed/accuracy tradeoff: 3.0M parameters, 5.8 GFLOPs, 99.3% mAP@0.5 on MSD, and 46.0% mAP@0.5 on SSGD.
- Dynamic-LSKA outperforms SE, CBAM, Deformable LKA, and standard LSKA in the paper's attention-module comparison.
- Dynamic-LSKA is presented as most helpful for reflection/low-contrast interference, while HSF-BPAN is presented as most helpful for defect scale variation.

## ML/DL Extraction

- Task formulation: object detection for smartphone cover-glass surface defects.
- Inputs: RGB cover-glass images from MSD and SSGD, resized to 640 x 640 for inference comparison.
- Outputs: bounding boxes and defect classes.
- Architecture: YOLOv8 baseline with Dynamic-C2f, Dynamic-LSKA, HSF-BPAN, DySample, and decoupled detection head.
- Training recipe: SGD, batch size 32, mixed precision, LambdaLR, learning rate 0.01, weight decay 0.0005, Mosaic augmentation except final ten epochs.
- Baselines: YOLOv3, YOLOv5, YOLOv6, RTDETR, YOLOv8, YOLOv9, YOLOv10, YOLOv11, and YOLOv12.
- Artifacts: datasets are public; code release is not reported.

## Limitations

- The paper states that accuracy still has room for improvement.
- SSGD performance remains much lower than MSD performance, especially on mAP@0.5:0.95, indicating the more diverse benchmark remains difficult.
- Code availability is not reported.
- The paper uses validation splits rather than reporting a separate held-out test protocol in the extracted text.

## Connections

### Graph Hubs

- Tasks: [[Smartphone screen glass defect detection]], [[Object detection]]
- Methods: [[DY-YOLO]], [[YOLOv8]]
- Datasets: [[MSD]], [[SSGD]]
- Domains: [[Glass inspection]]
- Metrics: [[Precision]], [[Recall]], [[F1-score]], [[mAP]], [[mAP@0.50]], [[FPS]], [[GFLOPs]], [[Parameter count]], [[Inference time]]

### Shares Dataset

- [[MSD]]: the paper evaluates DY-YOLO on oil stain, scratch, and spot detection.
- [[SSGD]]: the paper evaluates DY-YOLO on seven smartphone screen-glass defect classes.

### Shares Task

- [[Smartphone screen glass defect detection]]: cover-glass defect detection is the paper's target application.
- [[Object detection]]: DY-YOLO outputs localized defect detections.

### Shares Method

- [[YOLOv8]]: DY-YOLO uses YOLOv8 as the baseline architecture.

### Application/Domain

- [[Glass inspection]]: the task is visual inspection of smartphone cover-glass surfaces.

## Questions

- Code release is not reported.
- The extracted text does not report a separate final test set after the paper reallocates data into 8:2 train/validation splits.
