---
title: "Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation"
paper_key: "doi:10.1109/icispc63824.2024.00010"
paper_type: systems
year: 2024
venue: "2024 8th International Conference on Imaging, Signal Processing and Communications"
authors:
  - "Yuhang Hong"
  - "Ziwen Wang"
  - "Wenzhen Wu"
  - "Zhenbing Liu"
  - "Benying Tan"
  - "Guangxi Chen"
  - "Yujie Li"
status: processed
processed_at: 2026-06-11
topics:
  - "steel surface defect detection"
  - "diffusion data augmentation"
  - "edge deployment"
tasks:
  - "[[Defect detection]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
methods:
  - "[[Diffusion models]]"
  - "[[Data augmentation]]"
  - "[[YOLO-DSC]]"
architectures:
  - "[[YOLOv8]]"
  - "[[YOLO-DSC]]"
optimizers:
  - "[[AdamW]]"
metrics:
  - "[[mAP@0.50]]"
primary_metric: "[[mAP@0.50]]"
doi: "10.1109/icispc63824.2024.00010"
url: "https://doi.org/10.1109/icispc63824.2024.00010"
pdf: "paper-inbox/10_processed/Systems/2024 - Hong - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation.pdf"
hardware: "NVIDIA TITAN RTX for training; Jetson Nano for edge inference"
inference_cost: "0.05 seconds per 224x224 image on Jetson Nano"
code: "not reported"
data: "uses NEU-DET"
related_methods:
  - "[[Diffusion models]]"
  - "[[YOLO-DSC]]"
related_datasets:
  - "[[NEU-DET]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect detection]]"
source_file: "paper-inbox/10_processed/Systems/2024 - Hong - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Hong - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Hong - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation.txt"
tags:
  - paper
---
# Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation

## Summary

The paper uses denoising diffusion implicit models to augment [[NEU-DET]] and proposes [[YOLO-DSC]], a YOLOv8n-derived detector with distribution shifting convolution. The augmented detector improves mAP@0.5 over a YOLOv8n baseline and is deployed on Jetson Nano for steel surface defect inspection.

## Paper Type

- Type: systems.
- Why: The paper combines model design, synthetic data augmentation, and embedded inference reporting.

## Problem

- Task: [[Defect detection]] on steel surface images.
- Setting: real-time [[Metal inspection]] with limited labeled defect images.
- Inputs: NEU-DET grayscale defect images.
- Outputs: defect bounding boxes and classes.

## Contribution

- Claimed: DDIM augmentation can improve steel defect detector training, while distribution shifting convolution lowers model cost.
- Shown: YOLOv8n baseline mAP@0.5 improves from 0.748 to 0.803 with DDIM augmentation; final YOLO-DSC reports 0.809.
- Shown: YOLO-DSC has 2.81M parameters and 7.3 GFlops, lower than YOLOv8n's 3.16M parameters and 8.9 GFlops.

## Method

- Synthetic data: DDIMs generate 17,984 images; high/low-exposure and defect-free samples are removed; 1,816 generated images are selected, labeled, and mixed with original NEU-DET data.
- Detector: YOLO-DSC modifies YOLOv8n with distribution shifting convolution in feature fusion.
- Training: PyTorch, Python 3.8, AdamW, input size 224x224, learning rate 0.01, batch size 64, 300 epochs.
- Diffusion generation: DDIM training uses 60,000 epochs per individual image, batch size 20, sampling step size 100, eta 0, and two NVIDIA TITAN RTX GPUs.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| DDIM augmentation | [[NEU-DET]] detection | [[mAP@0.50]] | YOLOv8n 0.748 | YOLOv8n + DDIM 0.803 | Higher is better. |
| Final detector | [[NEU-DET]] detection | [[mAP@0.50]] | YOLOv8n 0.748 | YOLO-DSC 0.809 | Includes augmentation and DSC changes. |
| Efficiency | [[NEU-DET]] detection | parameters | YOLOv8n 3.16M | YOLO-DSC 2.81M | Lower is smaller. |
| Efficiency | [[NEU-DET]] detection | GFlops | YOLOv8n 8.9 | YOLO-DSC 7.3 | Lower is smaller. |

## Dataset / Benchmark Details

- [[NEU-DET]]: 1,800 grayscale images, six steel surface defect categories, 300 images per class.
- The source text calls one augmentation training set "NET-DET" while the dataset section identifies [[NEU-DET]]; this appears to be a naming inconsistency in the paper.

## Limitations

- Transformer-based detection methods are not compared because the paper treats their parameter counts as too large for real-time detection.
- Generated images are manually filtered and labeled, so the augmentation pipeline is not fully automatic.
- Code availability: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect detection]], [[Metallic surface defect detection]]
- Methods: [[Diffusion models]], [[Data augmentation]], [[YOLO-DSC]]
- Datasets: [[NEU-DET]]
- Domains: [[Metal inspection]]
- Metrics: [[mAP@0.50]]

### Relationship Notes

- Shares dataset: [[NEU-DET]].
- Shares method: [[Diffusion models]], [[Data augmentation]], and [[YOLO-DSC]].
- Shares metric: [[mAP@0.50]].
- Application/domain: [[Metal inspection]].

## Questions

- How reproducible is the generated-image selection step without the manual luminance and defect filtering details?
- Does YOLO-DSC remain efficient at higher input resolutions?
