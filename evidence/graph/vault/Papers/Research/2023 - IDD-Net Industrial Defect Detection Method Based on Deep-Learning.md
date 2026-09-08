---
title: "IDD-Net: Industrial defect detection method based on Deep-Learning"
aliases:
  - "IDD-Net Industrial Defect Detection Method Based on Deep-Learning"
paper_key: "sha256:d3cc52c822c6b930e3fc7f82b844bd888aab3a5f4d56afa6c5c54b6e34e7b504"
paper_type: research
year: 2023
venue: "Engineering Applications of Artificial Intelligence"
authors:
  - "Zekai Zhang"
  - "Mingle Zhou"
  - "Honglin Wan"
  - "Min Li"
  - "Gang Li"
  - "Delong Han"
status: processed
processed_at: 2026-05-21
topics:
  - industrial defect detection
  - one-stage object detection
  - small defect detection
tasks:
  - "[[Defect detection]]"
  - "[[Object detection]]"
  - "[[Metallic surface defect detection]]"
  - "[[PCB defect detection]]"
  - "[[Glass container defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[Baidu aluminium surface defect dataset]]"
  - "[[DeepPCB]]"
  - "[[BBMP]]"
methods:
  - "[[IDD-Net]]"
  - "[[LGB-Net]]"
  - "[[TFLA-Net]]"
  - "[[Multi-scale feature fusion]]"
  - "[[Defect-IoU loss]]"
  - "[[Ghost module]]"
  - "[[YOLOv5]]"
model_family:
  - "[[YOLOv5]]"
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[mAP@0.50-0.95]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[GFLOPs]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.50]]"
code: "not reported"
data: "Data will be made available on request"
doi: "10.1016/j.engappai.2023.106390"
url: "https://doi.org/10.1016/j.engappai.2023.106390"
arxiv: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[IDD-Net]]"
  - "[[LGB-Net]]"
  - "[[TFLA-Net]]"
  - "[[Multi-scale feature fusion]]"
  - "[[Defect-IoU loss]]"
  - "[[Ghost module]]"
  - "[[YOLOv5]]"
related_datasets:
  - "[[NEU-DET]]"
  - "[[Baidu aluminium surface defect dataset]]"
  - "[[DeepPCB]]"
  - "[[BBMP]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Defect detection]]"
  - "[[Object detection]]"
  - "[[Metallic surface defect detection]]"
  - "[[PCB defect detection]]"
  - "[[Glass container defect detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Zhang - IDD-Net Industrial Defect Detection Method Based on Deep-Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Zhang - IDD-Net Industrial Defect Detection Method Based on Deep-Learning.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Zhang - IDD-Net Industrial Defect Detection Method Based on Deep-Learning.txt"
artifact_status: "data on request; code not reported"
tags:
  - paper
---

# IDD-Net Industrial Defect Detection Method Based on Deep-Learning

## Summary

Zhang et al. propose [[IDD-Net]], a one-stage industrial defect detector intended to balance detection accuracy, small-object sensitivity, and runtime. The architecture replaces the YOLOv5-style backbone and neck with [[LGB-Net]] for local-global feature extraction, [[TFLA-Net]] for three-layer feature aggregation, a [[Multi-scale feature fusion]] module before detection heads, and [[Defect-IoU loss]] to rebalance bounding-box regression for different defect scales. The evaluation spans steel, aluminium, PCB, and glass-bottle production data.

## Paper Type

- Type: research.
- Why: The paper introduces a detector architecture, evaluates it against object-detection baselines, and ablates the proposed modules.

## Problem

- Task: bounding-box [[Defect detection]] for industrial surface defects.
- Setting: industrial imagery with small objects, large scale variation, class imbalance, and production-speed constraints.
- Inputs: RGB or grayscale defect images resized to 640 x 640 for the main experiments.
- Outputs: defect class labels and bounding boxes from three detector heads for large, medium, and small objects.
- Motivation: standard object detectors can miss small industrial defects or trade too much speed for accuracy.

## Contribution

- Proposes [[LGB-Net]], a five-stage local-global backbone combining convolutional blocks and lightweight self-attention blocks.
- Proposes [[TFLA-Net]], a descending three-layer feature aggregation neck that reuses all backbone hierarchical features and adjacent feature transfers.
- Adds [[Multi-scale feature fusion]] and [[Defect-IoU loss]] to improve multi-scale and small-defect detection.
- Demonstrates the detector on public steel, aluminium, and PCB data plus a glass-bottle mold-point production dataset.

## Method

- Backbone: [[LGB-Net]] has B1 as a Conv-Block and B2-B5 as Conv-Block plus TransformerBlock stages, with stage depths N1-N5 of 1, 1, 2, 2, and 1.
- Conv-Block: uses 3 x 3 [[Ghost module|ghost convolution]] and an attention module to reduce computation while preserving local features.
- TransformerBlock: uses one-dimensional positional encoding, four S-MHSA heads, patch size 16, and reduces Key/Value by 4x while leaving Query unchanged.
- Neck: [[TFLA-Net]] performs three-layer descending feature aggregation with dense adjacent feature transfer and ghost-convolution downsampling.
- Fusion: [[Multi-scale feature fusion]] applies global-average-pooling channel selection with a Softmax C x 1 x 1 weight matrix and learnable weighted fusion with epsilon 0.0001.
- Detector: three anchor-based heads predict large, medium, and small defects.
- Loss: classification and confidence use QFocal Loss; localization uses [[Defect-IoU loss]], which scales CIoU with a defect-size balance function.

## ML / DL Extraction

### Model And Training

- Base comparison: YOLOv5s is the main ablation baseline.
- Optimizer: Adam.
- Main training setup: 300 epochs, train batch 16, test batch 1, initial learning rate 0.001, momentum 0.9, weight decay 0.0001, IoU training threshold 0.2, image size 640 x 640, Defect-IoU parameter A = 1.
- Learning-rate schedule: cosine annealing unless otherwise specified.
- Main platform: Windows Server 2019, PyTorch 1.7, Intel i9-9900K at 5 GHz, 64 GB RAM, NVIDIA GeForce RTX 6000 with 24 GB memory.
- BBMP platform: Windows 10 Professional industrial computer, Intel i9-9900K at 5 GHz, RTX 3060Ti 8 GB GDDR6X, 64 GB RAM; BBMP training uses 400 epochs.

### Data

- [[NEU-DET]] / NEU steel surface defects: six hot-rolled steel-strip defect types; the paper reports fixing graphics bugs and rotating/stitching fracture images; split 6:2:2.
- [[Baidu aluminium surface defect dataset]]: Baidu PaddlePaddle aluminium surface defects with 640 x 480 source resolution, gamma enhancement, flipping, rotation, and shifting; expanded to 1236 images and split 8:1:1.
- [[DeepPCB]] / PCB Surface Defects Dataset: the paper describes a Peking University synthetic open-source PCB dataset with 1386 pictures, selects 900 images, and splits them 6:2:2.
- [[BBMP]]: glass-bottle bottom mold point data collected from an industrial production line with CCD camera resolution 800 x 780, 125 pictures per hour over eight hours, and a 6:2:2 split.

### Evaluation

- Metrics: [[mAP@0.50]], [[mAP@0.50-0.95]], [[Precision]], [[Recall]], [[F1-score]], [[GFLOPs]], and [[FPS]].
- Baselines: SSD, Faster R-CNN, YOLOv3, YOLOv4, YOLOv5s, YOLOv5x, EfficientDet-d3, CenterNet, RetinaNet, YOLOR-P6, YOLOX-s, PP-YOLOE-s, AIRDet-s, and YOLOv6-s, depending on dataset table.
- Ablations: backbone replacement, [[TFLA-Net]], [[Multi-scale feature fusion]], Conv-Block attention, TransformerBlock, Defect-IoU variants, and feature-fusion placement.

## Evidence

### Main Results

| Dataset | IDD-Net result | Main comparison notes |
|---|---:|---|
| [[NEU-DET]] / NEU steel | 79.66% mAP@0.50, 43.6% mAP@0.50-0.95, 76.36% precision, 84.56% recall, 0.92 F1, 24.9 GFLOPs, 44 FPS | Best reported F1 and mAP@0.50-0.95 in Table 2; Table 2 lists AIRDet-s at 79.92% mAP@0.50 and YOLOX-s at 84.88% recall, so the table does not fully support the paper's narrative claim that IDD-Net exceeds every detector on all key accuracy fields. |
| [[Baidu aluminium surface defect dataset]] | 99.5% mAP@0.50, 57.79% mAP@0.50-0.95, 97.9% precision, 99.2% recall, 0.98 F1 | Ties YOLOv6-s on mAP@0.50 and exceeds it on mAP@0.50-0.95 and recall in Table 6. |
| [[DeepPCB]] / PCB surface defects | 95.9% mAP@0.50, 61.91% mAP@0.50-0.95, 84.8% precision, 96.11% recall, 0.90 F1 | Highest mAP@0.50 and mAP@0.50-0.95 in Table 13; other detectors have higher precision or F1 in some rows. |
| [[BBMP]] | 99.5% mAP@0.50, 40 FPS, 99.6% precision, 99.5% recall | Matches or exceeds the listed industrial baselines in mAP@0.50, precision, and recall; YOLOv6-s is faster at 63 FPS. |

### Ablations

| Dataset / ablation | Result |
|---|---|
| NEU steel, +Our Backbone over YOLOv5s | 76.4% mAP@0.50 vs 70.9%; 40.9% mAP@0.50-0.95 vs 35.6%; recall 77.91% vs 64.3%. |
| NEU steel, +TFLA-Net | 71.63% mAP@0.50; 40.7% mAP@0.50-0.95; recall 72.4%. |
| NEU steel, +MSF | 75.6% mAP@0.50; 41.1% mAP@0.50-0.95; precision 81.56%. |
| Aluminium, +Our Backbone over YOLOv5s | 98.9% mAP@0.50 vs 97.2%; recall 98.86% vs 96.8%. |
| Aluminium, +TFLA-Net | 97.99% mAP@0.50; 58.3% mAP@0.50-0.95. |
| Aluminium, +MSF | 99.1% mAP@0.50; 58.32% mAP@0.50-0.95. |
| Defect-IoU on aluminium | 99.5% mAP@0.50 and 99.2% recall; CIoU baseline is 99.18% mAP@0.50 and 97.78% recall. |
| PCB, TFLA-Net vs feature-fusion necks | +TFLA-Net reaches 92.1% mAP@0.50 and 53.5% mAP@0.50-0.95, with higher recall than YOLOv5s, Bi-FPN, and NAS-FPN in Table 14. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP@0.50]] | detector accuracy on all four datasets | mean average precision at IoU 0.50 | higher is better | yes | Main comparison metric in Tables 2, 6, 13, and 16. |
| [[mAP@0.50-0.95]] | detector localization robustness on public datasets | mean average precision averaged from IoU 0.50 to 0.95 | higher is better | no | Reported for NEU, aluminium, and PCB experiments. |
| [[Precision]] | false-positive control | TP / (TP + FP) | higher is better | no | Reported in comparison and ablation tables. |
| [[Recall]] | missed-defect control | TP / (TP + FN) | higher is better | no | Reported in comparison and ablation tables. |
| [[F1-score]] | precision-recall balance | harmonic mean of precision and recall | higher is better | no | Reported in the main comparison tables for NEU, aluminium, PCB, and BBMP. |
| [[GFLOPs]] | computational cost | billion floating-point operations | lower is better at comparable accuracy | no | Reported for NEU comparisons and summarized as 24.9 GFLOPs for IDD-Net. |
| [[FPS]] | inference speed | frames per second | higher is better | no | IDD-Net reports 44 FPS on NEU and 40 FPS on BBMP. |

## Dataset / Benchmark Details

- [[NEU-DET]] classes as reported: rolled-in scale, plaque, silver streak, pitting, inclusions, and scratches.
- [[Baidu aluminium surface defect dataset]] classes and counts: zhen_kong 516, ca_shang 694, zang_wu 1087, zhe_zhou 307.
- [[DeepPCB]] / PCB classes and counts used in the paper: missing hole 255, mouse bite 292, open circuit 173, spur 306, short 281, spurious copper 436.
- [[BBMP]] class distribution is shown in a figure, but exact class names and counts are not recoverable from the analysis input.
- Data availability: the article states that data will be made available on request.

## Limitations

- The paper's future work is to improve generalization and design detectors for different application scenarios, including industrial security monitoring.
- BBMP is request-only in the paper, so independent reproducibility of the production-line experiment is limited.
- Several comparison tables show mixed wins rather than uniform superiority; the strongest claim is that IDD-Net offers a competitive accuracy-speed balance, not that it dominates every metric.
- Exact BBMP class counts are not available in the extracted text.

## Reproducibility

- Code: not reported.
- Data: available on request.
- Hyperparameters: main training and BBMP platform settings are reported.
- Random seeds: not reported.
- Environment: PyTorch 1.7, Windows Server 2019 for main experiments; Windows 10 Professional industrial computer for BBMP.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect detection]], [[Object detection]], [[Metallic surface defect detection]], [[PCB defect detection]], [[Glass container defect detection]]
- Methods: [[IDD-Net]], [[LGB-Net]], [[TFLA-Net]], [[Multi-scale feature fusion]], [[Defect-IoU loss]], [[Ghost module]], [[YOLOv5]]
- Datasets: [[NEU-DET]], [[Baidu aluminium surface defect dataset]], [[DeepPCB]], [[BBMP]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mAP@0.50]], [[mAP@0.50-0.95]], [[Precision]], [[Recall]], [[F1-score]], [[GFLOPs]], [[FPS]]

### Builds On

- [[YOLOv5]]: IDD-Net uses YOLOv5s as the main baseline and replaces backbone, feature aggregation, fusion, and localization loss components.
- [[Ghost module]]: Conv-Blocks and downsampling use ghost convolution to reduce computational cost.

### Shares Dataset

- [[NEU-DET]]: shares steel surface defect detection context with NEU-DET detector papers.
- [[DeepPCB]]: shares PCB defect detection context with PCB detector and augmentation papers.

### Shares Task

- [[Defect detection]] and [[Object detection]]: the detector predicts bounding boxes and defect categories.
- [[Metallic surface defect detection]], [[PCB defect detection]], and [[Glass container defect detection]]: each dataset anchors one application setting.

### Shares Method

- [[Multi-scale feature fusion]]: IDD-Net fuses multi-scale features before its detector heads.
- [[Defect-IoU loss]]: the localization loss modifies CIoU with a scale-sensitive balance term.

### Shares Metric

- [[mAP@0.50]], [[mAP@0.50-0.95]], [[Precision]], [[Recall]], [[F1-score]], [[GFLOPs]], and [[FPS]] are used to evaluate detector accuracy and speed.

### Application / Domain

- [[Multi-industry anomaly detection]]: the evaluation covers steel, aluminium, electronics, and glass-bottle production rather than a single material or product domain.

### Follow-Up Reading

- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]]: a transformer-enhanced YOLOv5 steel-defect detector on NEU-DET.
- [[2025 - You Only Look Once-Aluminum]]: a later YOLO-family aluminium defect detector with a dedicated aluminium profile dataset.

## Questions

- Can the request-only BBMP data be obtained, and does it include the class labels and counts hidden in the figure?
- How does IDD-Net compare under a uniform modern training recipe against newer YOLO variants after 2023?
