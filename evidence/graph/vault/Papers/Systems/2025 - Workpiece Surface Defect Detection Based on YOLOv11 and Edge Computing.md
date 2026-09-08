---
title: "Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing"
aliases:
  - "Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing"
paper_key: "doi:10.1371/journal.pone.0327546"
paper_type: systems
year: 2025
venue: "PLoS One"
authors:
  - "Zishuo Wang"
  - "Tao Ding"
  - "Shuning Liang"
  - "Hongwei Cui"
  - "Xingquan Gao"
status: processed
processed_at: 2026-05-22
topics:
  - "edge computing"
  - "surface defect detection"
  - "SA-GAN augmentation"
tasks:
  - "[[Workpiece surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[Tianchi aluminium profile surface defect dataset]]"
  - "[[Workpiece surface defect dataset]]"
methods:
  - "[[YOLOv11]]"
  - "[[SA-GAN]]"
  - "[[YOLOv11-RKNN edge deployment]]"
  - "[[Edge intelligence]]"
  - "[[Data augmentation]]"
model_family:
  - "[[YOLOv11]]"
architectures:
  - "[[YOLOv11]]"
  - "[[YOLOv11-RKNN edge deployment]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[Average precision]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[Detection time]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.5: mean average precision at IoU threshold 0.5; higher is better."
  - "Detection time: milliseconds per 200 x 200 image; lower is better."
baselines:
  - "YOLOv7"
  - "YOLOv8"
  - "YOLOv9"
  - "YOLOv10"
  - "YOLOv7 with SA-GAN"
  - "YOLOv8 with SA-GAN"
  - "YOLOv9 with SA-GAN"
  - "YOLOv10 with SA-GAN"
benchmarks:
  - "[[NEU-DET benchmark]]"
  - "[[Tianchi aluminium profile surface defect dataset]]"
code: "not reported"
data: "https://gitcode.com/open-source-toolkit/fa031"
doi: "10.1371/journal.pone.0327546"
arxiv: "not reported"
url: "https://doi.org/10.1371/journal.pone.0327546"
pdf: "paper-inbox/10_processed/Systems/2025 - Wang - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[YOLOv11]]"
  - "[[SA-GAN]]"
  - "[[YOLOv11-RKNN edge deployment]]"
  - "[[Edge intelligence]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-DET]]"
  - "[[Tianchi aluminium profile surface defect dataset]]"
  - "[[Workpiece surface defect dataset]]"
related_tasks:
  - "[[Workpiece surface defect detection]]"
  - "[[Object detection]]"
related_benchmarks:
  - "[[NEU-DET benchmark]]"
source_file: "paper-inbox/10_processed/Systems/2025 - Wang - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Wang - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Wang - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing.txt"
artifact_status: "data host reported; code not reported"
tags:
  - paper
---
# Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing

## Summary

The paper proposes a YOLOv11-based workpiece surface defect detector with SA-GAN data augmentation and RK3568 edge deployment. It expands NEU-DET from the paper's selected three classes to 3,463 relabelled images using random cropping, flipping, rotation, and SA-GAN synthesis; compares YOLOv7 through YOLOv11; validates on a Tianchi aluminium profile surface defect dataset; and converts the cloud YOLOv11 model into an INT8 YOLOv11-RKNN model for edge inference.

## Paper Type

Systems paper. The contribution combines model training, synthetic data augmentation, model conversion, INT8 quantization, and deployment on RK3568 edge hardware.

## Problem

- Task: [[Workpiece surface defect detection]] as [[Object detection]].
- Setting: industrial workpiece inspection where sending high-volume visual data to the cloud increases bandwidth and latency.
- Inputs: surface defect images from NEU-DET and Tianchi aluminium profile defect data.
- Outputs: defect detections for inclusion, patch, scratch, bruise, dirty, raised, and scratch-like defect categories depending on the dataset.
- Motivation: improve detection accuracy while moving inference closer to production equipment.

## Contribution

- Proposes an SA-GAN-based augmentation strategy for workpiece surface defects; on NEU-DET, YOLOv11 mAP@0.5 rises from 81.4% without SA-GAN to 85.1% with SA-GAN.
- Shows YOLOv11 with SA-GAN outperforming YOLOv7, YOLOv8, YOLOv9, and YOLOv10 on NEU-DET by 7.7, 3.1, 5.9, and 7.0 percentage points in mAP@0.5.
- Validates generalization on the Tianchi aluminium profile surface defect dataset, where YOLOv11 with SA-GAN reaches 87.0% mAP@0.5.
- Converts YOLOv11 to YOLOv11-RKNN with asymmetric INT8 quantization on RK3568, reducing model size from 10,156 KB to 4,194 KB and detection time from 52.1 ms to 33.6 ms for 200 x 200 images.

## Method

The pipeline first expands training data in the cloud with random cropping, flipping, rotation, and [[SA-GAN]]. SA-GAN uses a self-attention mechanism over query, key, and value projections to capture long-range image dependencies and generate more realistic, diverse defect samples. The paper then trains YOLOv7, YOLOv8, YOLOv9, YOLOv10, and YOLOv11 from scratch under the same environment. The best cloud model is converted with RKNN-Toolkit2 into a YOLOv11-RKNN edge model, using asymmetric INT8 quantization and RKNN Lite deployment on RK3568.

## ML / DL Extraction

### Task Formulation

- Input modality: 2D industrial surface defect images.
- Output target: object-detection predictions for defect classes.
- Supervision: supervised object detection with relabelled augmented images.
- Objective: improve mAP@0.5 and deployment latency for workpiece surface defect detection.

### Model And Training

- Model family: [[YOLOv11]].
- Compared models: YOLOv7, YOLOv8, YOLOv9, YOLOv10, YOLOv11, each with and without SA-GAN augmentation.
- YOLOv11 components described by the paper: backbone, neck, and head, with added C3K2, SPPF, and C2PSA modules relative to prior YOLO versions.
- Optimizer: SGD.
- Hyperparameters: batch size 16, 300 epochs.
- Pretraining: all compared YOLO models are trained from scratch without official pretrained weights.
- Cloud environment: Linux, PyTorch 2.0, 32 GB memory, NVIDIA GeForce RTX 4090 GPU.
- Edge environment: Rockchip RK3568 board, Linux, quad-core ARM Cortex-A55 up to 2.0 GHz, ARM Mali-G52 2EE GPU, and 1.0 TOPS NPU.

### Data

| Dataset | Role | Source-reported details |
|---|---|---|
| [[NEU-DET]] | Main training and evaluation dataset | The paper uses three labels: scratches, inclusions, and patches. Each has 300 initial images. Random cropping/flipping expands the selected data to 2,450 images; SA-GAN expands it to 3,463 relabelled images. |
| [[Tianchi aluminium profile surface defect dataset]] | Generalization dataset | SA-GAN augments four defect types: bruise, dirty, raised, and scratches, producing 872 defect images: 208 bruise, 188 dirty, 168 raised, and 308 scratch images. |
| [[Workpiece surface defect dataset]] | Reported public data host | The data availability statement gives a GitCode URL for model training, validation, and evaluation data. |

NEU-DET after SA-GAN is split 80/10/10:

| Defect type | Train | Test | Validation | Total |
|---|---:|---:|---:|---:|
| Inclusion | 840 | 117 | 106 | 1,063 |
| Patches | 952 | 121 | 127 | 1,200 |
| Scratches | 979 | 108 | 113 | 1,200 |

### Augmentation And Synthesis

- Conventional augmentation: random cropping, flipping, and rotation.
- Synthetic augmentation: SA-GAN trained on augmented data generates additional defect samples.
- NEU-DET expansion: initial selected data contains 300 images per class for scratches, inclusions, and patches; random cropping/flipping yields 2,450 images; SA-GAN yields 3,463 relabelled images.
- Tianchi expansion: SA-GAN yields 872 images across bruise, dirty, raised, and scratch defects.
- Leakage checks: not reported.

## Evidence

### Experimental Setup

- Training split: 80% train, 10% validation, 10% test for the expanded NEU-DET data.
- Metrics: precision, recall, F1 score, true negative rate, AP, mAP@0.5, model size, and detection time.
- Baselines: YOLOv7, YOLOv8, YOLOv9, and YOLOv10, each trained in the same environment and compared with and without SA-GAN.

### Main Results

| Experiment | Dataset / task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| SA-GAN effect on YOLOv11 | [[NEU-DET]] / [[Object detection]] | mAP@0.5 | higher | YOLOv11 81.4% | YOLOv11 with SA-GAN 85.1% | +3.7 percentage points. |
| Best SA-GAN model vs YOLOv7 | [[NEU-DET]] | mAP@0.5 | higher | YOLOv7 with SA-GAN 77.4% | YOLOv11 with SA-GAN 85.1% | +7.7 percentage points. |
| Best SA-GAN model vs YOLOv8 | [[NEU-DET]] | mAP@0.5 | higher | YOLOv8 with SA-GAN 82.0% | YOLOv11 with SA-GAN 85.1% | +3.1 percentage points. |
| Best SA-GAN model vs YOLOv9 | [[NEU-DET]] | mAP@0.5 | higher | YOLOv9 with SA-GAN 79.2% | YOLOv11 with SA-GAN 85.1% | +5.9 percentage points. |
| Best SA-GAN model vs YOLOv10 | [[NEU-DET]] | mAP@0.5 | higher | YOLOv10 with SA-GAN 78.1% | YOLOv11 with SA-GAN 85.1% | +7.0 percentage points. |
| Generalization | [[Tianchi aluminium profile surface defect dataset]] | mAP@0.5 | higher | YOLOv8 with SA-GAN 83.7%; YOLOv10 with SA-GAN 74.8% | YOLOv11 with SA-GAN 87.0% | Best model in Table 7. |
| Edge deployment | RK3568 / 200 x 200 image | detection time | lower | cloud YOLOv11 52.1 ms | YOLOv11-RKNN 33.6 ms | 35.5% shorter detection time. |
| Edge model size | RK3568 conversion | model size | lower | cloud YOLOv11 10,156 KB | YOLOv11-RKNN 4,194 KB | INT8 input/output tensors after conversion. |

### NEU-DET YOLO Comparison

| Model | mAP@0.5 | Precision | Recall | F1 | TNR |
|---|---:|---:|---:|---:|---:|
| YOLOv7 | 71.6 | 81.2 | 64.9 | 72.1 | 70.3 |
| YOLOv8 | 79.4 | 84.1 | 76.1 | 79.9 | 78.2 |
| YOLOv9 | 78.7 | 86.7 | 76.9 | 81.5 | 78.5 |
| YOLOv10 | 75.3 | 80.8 | 73.1 | 76.8 | 73.9 |
| YOLOv11 | 81.4 | 84.4 | 79.9 | 82.0 | 81.8 |
| YOLOv7 with SA-GAN | 77.4 | 85.6 | 74.6 | 79.7 | 76.6 |
| YOLOv8 with SA-GAN | 82.0 | 82.0 | 74.1 | 77.9 | 81.2 |
| YOLOv9 with SA-GAN | 79.2 | 84.9 | 75.2 | 79.8 | 77.7 |
| YOLOv10 with SA-GAN | 78.1 | 85.9 | 77.3 | 81.4 | 75.8 |
| YOLOv11 with SA-GAN | 85.1 | 88.9 | 80.4 | 84.8 | 86.1 |

### Per-Defect NEU-DET AP With SA-GAN

| Model | mAP@0.5 | Inclusion | Patches | Scratches |
|---|---:|---:|---:|---:|
| YOLOv7 with SA-GAN | 77.4 | 76.2 | 80.1 | 76.0 |
| YOLOv8 with SA-GAN | 82.0 | 84.5 | 77.5 | 83.9 |
| YOLOv9 with SA-GAN | 79.2 | 72.6 | 78.5 | 86.6 |
| YOLOv10 with SA-GAN | 78.1 | 69.6 | 79.8 | 85.0 |
| YOLOv11 with SA-GAN | 85.1 | 86.6 | 80.1 | 88.7 |

### Tianchi Generalization Results

| Model | mAP@0.5 | Precision | Recall | F1 | TNR |
|---|---:|---:|---:|---:|---:|
| YOLOv7 | 77.9 | 80.2 | 75.6 | 77.8 | 80.4 |
| YOLOv8 | 80.1 | 82.4 | 78.9 | 80.6 | 79.7 |
| YOLOv9 | 75.7 | 77.8 | 71.2 | 74.3 | 74.9 |
| YOLOv10 | 69.8 | 72.1 | 68.5 | 70.2 | 69.1 |
| YOLOv11 | 83.2 | 84.2 | 80.5 | 82.3 | 83.0 |
| YOLOv7 with SA-GAN | 80.1 | 81.9 | 77.2 | 79.4 | 79.8 |
| YOLOv8 with SA-GAN | 83.7 | 83.6 | 79.9 | 81.7 | 83.3 |
| YOLOv9 with SA-GAN | 78.5 | 82.4 | 76.6 | 79.3 | 78.1 |
| YOLOv10 with SA-GAN | 74.8 | 79.1 | 71.5 | 75.1 | 73.5 |
| YOLOv11 with SA-GAN | 87.0 | 90.4 | 84.6 | 87.4 | 86.7 |

### Edge Deployment Results

| Model | Input tensor | Output tensor | Image size | FLOPs | Model size | Detection time |
|---|---|---|---|---:|---:|---:|
| YOLOv7 | float32 | float32 | 200 x 200 | 104.7G | 20,475 KB | 93.3 ms |
| YOLOv8 | float32 | float32 | 200 x 200 | 8.1G | 11,976 KB | 56.4 ms |
| YOLOv9 | float32 | float32 | 200 x 200 | 266.1G | 30,348 KB | 152.4 ms |
| YOLOv10 | float32 | float32 | 200 x 200 | 8.2G | 12,102 KB | 58.7 ms |
| YOLOv11 | float32 | float32 | 200 x 200 | 6.3G | 10,156 KB | 52.1 ms |
| YOLOv11-RKNN | int8 | int8 | 200 x 200 | 6.3G | 4,194 KB | 33.6 ms |

The paper reports that YOLOv11-RKNN keeps detection accuracy basically consistent with cloud YOLOv11 on NEU-DET and Tianchi while improving edge inference time.

## Limitations

- The paper evaluates only selected NEU-DET classes and Tianchi aluminium profile defect categories, so conclusions are bounded to those workpiece surface-defect settings.
- Code availability is not reported.
- The data host is reported, but the paper does not provide a detailed license analysis in the extracted text.
- The paper does not report random seeds or statistical uncertainty.

## Reproducibility

- Data: https://gitcode.com/open-source-toolkit/fa031.
- Training: PyTorch 2.0, 300 epochs, batch size 16, SGD, from-scratch training without official pretrained weights.
- Cloud hardware: NVIDIA GeForce RTX 4090 GPU, 32 GB memory.
- Edge hardware: RK3568 with ARM Cortex-A55, Mali-G52 2EE GPU, and 1.0 TOPS NPU.
- Conversion: RKNN-Toolkit2 with asymmetric INT8 quantization; input mean [0,0,0] and normalization [255,255,255].

## Systems Details

- Architecture: cloud training followed by edge conversion and deployment.
- Edge stack: RKNN-Toolkit2 conversion, RKNN Lite deployment, RKNPU2 driver, Python interface on RK3568.
- Latency target: the paper describes a field-to-edge delay under 150 ms, with acquisition/transmission under 50 ms, inference under 50 ms, and result return under 50 ms.
- Quantization effect: model tensors change from float32 to int8; model size falls by 58.7%; detection time falls by 35.5%.

## Connections

### Graph Hubs

- Tasks: [[Workpiece surface defect detection]], [[Object detection]]
- Methods: [[YOLOv11]], [[SA-GAN]], [[YOLOv11-RKNN edge deployment]], [[Edge intelligence]], [[Data augmentation]]
- Datasets: [[NEU-DET]], [[Tianchi aluminium profile surface defect dataset]], [[Workpiece surface defect dataset]]
- Benchmarks: [[NEU-DET benchmark]]
- Domains: [[Multi-industry anomaly detection]], [[Metal inspection]]
- Metrics: [[mAP@0.50]], [[Average precision]], [[Precision]], [[Recall]], [[F1-score]], [[Detection time]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] | Shares dataset | Introduces NEU-DET, which this paper uses for YOLOv7-YOLOv11 comparison after selecting three classes and augmenting them. |
| [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] | Shares dataset and augmentation problem | Both evaluate augmentation strategies for industrial defect detection on NEU-DET-like benchmark settings, but ALADA searches augmentation policies while this paper uses SA-GAN synthesis plus YOLOv11 edge deployment. |
| [[2024 - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation]] | Shares dataset and synthesis motivation | Both use generative augmentation for NEU-DET surface defect detection, with this paper using SA-GAN and YOLOv11. |

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[SA-GAN]] | Created | Paper data augmentation section |
| [[YOLOv11-RKNN edge deployment]] | Created | Paper model conversion and deployment sections |
| [[Tianchi aluminium profile surface defect dataset]] | Created | Paper generalization experiment section |
| [[Workpiece surface defect dataset]] | Updated | Data availability statement and experiment sections |

## Questions

- Does the GitCode dataset exactly mirror the NEU-DET and Tianchi subsets used in the paper, or does it include additional workpiece data?
- How sensitive are the reported gains to SA-GAN training randomness and relabelling quality?
- Would edge deployment preserve accuracy under full-resolution industrial camera streams rather than 200 x 200 test images?
