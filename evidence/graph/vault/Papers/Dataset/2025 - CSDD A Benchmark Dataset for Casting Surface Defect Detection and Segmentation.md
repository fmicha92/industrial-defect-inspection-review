---
title: "CSDD: A Benchmark Dataset for Casting Surface Defect Detection and Segmentation"
aliases:
  - "CSDD"
  - "CSDD benchmark dataset"
paper_key: "doi:10.1109/jas.2025.125228"
paper_type: dataset
year: 2025
venue: "IEEE/CAA Journal of Automatica Sinica"
authors:
  - "Kai Mao"
  - "Ping Wei"
  - "Yangyang Wang"
  - "Meiqin Liu"
  - "Shuaijie Wang"
  - "Nanning Zheng"
status: processed
processed_at: 2026-05-21
topics:
  - casting surface defect detection
  - defect detection
  - defect segmentation
  - industrial visual inspection
tasks:
  - "[[Casting surface defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[CSDD]]"
dataset_sizes:
  - "2100 RGB images"
  - "56356 annotated defects"
splits:
  - "1343 training images"
  - "335 validation images"
  - "422 test images"
modalities:
  - RGB images
methods:
  - "[[YOLOv5 with global attention and partial convolution]]"
  - "[[YOLOv5]]"
  - "[[U-Net]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[YOLOv5]]"
  - "[[U-Net]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP]]"
  - "[[IoU]]"
  - "[[mIoU]]"
  - "[[GFLOPs]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "AP is computed as area under the precision-recall curve."
  - "mAP is the average AP across defect types."
  - "IoU is TPpixel / (TPpixel + FPpixel + FNpixel)."
  - "mIoU is the mean IoU across defect types."
baselines:
  - "Faster R-CNN"
  - "Cascade R-CNN"
  - "SSD"
  - "RetinaNet"
  - "YOLOv5"
  - "YOLOv8"
  - "YOLOv10"
  - "CenterNet"
  - "FCOS"
  - "Deformable DETR"
  - "Conditional DETR"
  - "FCN"
  - "U-Net"
  - "DeepLabv3"
  - "DeepLabv3plus"
  - "FastFCN"
  - "CGNet"
  - "DDRNet"
  - "PIDNet"
  - "Segmenter"
  - "SegFormer"
  - "MaskFormer"
  - "Mask2Former"
benchmarks:
  - "[[CSDD benchmark]]"
evaluation_protocol: "64/16/20 train/validation/test split; images resized to 1024 x 1024 for experiments where applicable."
compute: "4 NVIDIA Tesla 3090 GPUs for detection experiments; 4 NVIDIA GeForce RTX 3090 GPUs for segmentation experiments."
hardware: "4 NVIDIA Tesla 3090 GPUs; 4 NVIDIA GeForce RTX 3090 GPUs"
url: "https://doi.org/10.1109/JAS.2025.125228"
code: "reported available: https://github.com/Kerio99/CSDD"
data: "reported available: https://github.com/Kerio99/CSDD"
doi: "10.1109/JAS.2025.125228"
arxiv: "not reported"
related_papers:
  - "[[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[YOLOv5 with global attention and partial convolution]]"
  - "[[YOLOv5]]"
  - "[[U-Net]]"
related_datasets:
  - "[[CSDD]]"
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
related_tasks:
  - "[[Casting surface defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[CSDD benchmark]]"
concept_notes_created_or_updated:
  - "[[CSDD]]"
  - "[[CSDD benchmark]]"
  - "[[Casting surface defect detection]]"
  - "[[YOLOv5]]"
  - "[[YOLOv5 with global attention and partial convolution]]"
  - "[[mIoU]]"
  - "[[GFLOPs]]"
pdf: "paper-inbox/10_processed/2025 - Mao - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation.pdf"
source_file: "paper-inbox/10_processed/2025 - Mao - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Mao - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Mao - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation.txt"
artifact_status: "dataset and code reported available"
tags:
  - paper
  - dataset
  - benchmark
  - metal-inspection
---

# CSDD: A Benchmark Dataset for Casting Surface Defect Detection and Segmentation

## Summary

- Introduces [[CSDD]], a public casting surface defect dataset with 2100 high-resolution RGB images, 56,356 manually annotated defects, and both detection and segmentation annotations.
- Defines [[CSDD benchmark]] for [[Casting surface defect detection]] and [[Defect segmentation]] with detection baselines, segmentation baselines, and a proposed [[YOLOv5 with global attention and partial convolution]] detector.
- Reports that the proposed detector achieves 71.1% mAP on CSDD, compared with 69.5% for the strongest listed baseline, YOLOv5.

## Paper Type

- Type: dataset / benchmark paper.
- Why: The main contribution is a new dataset and benchmark protocol, with baseline experiments and an accompanying detector.

## Problem

- Task: [[Casting surface defect detection]] and [[Defect segmentation]].
- Setting: RGB imaging of metal plates designed to simulate casting surfaces with complex inner structures.
- Inputs: 3648 x 3648 RGB images, resized to 1024 x 1024 for experiments where reported.
- Outputs: defect classes, bounding boxes, and pixel-level defect regions.
- Motivation: Existing surface defect datasets are described as limited by low resolution, simple backgrounds, constrained volume, or fewer annotated defects.
- Assumptions: Simulated casting-surface plates can represent practical casting surface structure closely enough to support benchmark development.

## Contribution

- Claimed: CSDD has the largest number of defects for casting surface defect detection and segmentation among compared datasets.
- Claimed: CSDD better reflects practical casting inspection because images contain complex inner structures and small defects.
- Shown: The dataset contains 2100 RGB images and 56,356 annotated defects: 31,634 scratches, 10,470 spots, and 14,252 rusts.
- Shown: The paper provides detection and segmentation baselines across CNN and Transformer methods.
- Shown: The proposed YOLOv5 modification with global attention and partial convolution improves detection mAP from 69.5% to 71.1% on CSDD.

## Method

- Core idea: Build a casting surface defect dataset and evaluate representative detection and segmentation methods on it.
- Architecture / algorithm: The proposed detector modifies YOLOv5 by adding a global attention mechanism before SPPF and replacing two C3 modules with P3 modules using partial convolution.
- Objective / loss: Detection baselines use method-specific losses; the proposed method follows YOLOv5 training settings with CIoU location loss and BCE class/object losses.
- Optimization: Detection methods use SGD or AdamW depending on architecture; YOLO-style methods use SGD with learning rate 0.01, weight decay 0.0005, momentum 0.8, batch size 4, and 300 epochs.
- Training data: 1343 CSDD training images.
- Data pipeline: Images collected from metal plates with manufactured scratches, spots, and rusts, manually annotated for defect type and region.
- Augmentation / synthesis: YOLO-style detection experiments use mosaic, mixup, HSV color-space augmentation, and random flip.
- Inference: Defect detection predicts class and bounding boxes; segmentation predicts pixel masks.
- Complexity / deployment constraints: The paper reports GFLOPs for detection and segmentation methods. The proposed detector reports 16.2 GFLOPs.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB images of casting-like metal surfaces.
- Output target: Bounding boxes and classes for detection; pixel masks for segmentation.
- Supervision: Fully supervised detection and segmentation labels.
- Objective: Benchmark casting surface defect detection and segmentation and improve YOLOv5 detection performance.

### Model And Training

- Model family: CNN-based object detection and semantic segmentation models, plus Transformer-based baselines.
- Architecture: Proposed detector is YOLOv5 with GAM and PConv/P3 modules.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: CIoU and BCE for YOLO-style detection; CE + Dice for most segmentation methods; CE + Focal + Dice for MaskFormer.
- Optimizer: SGD or AdamW depending on method.
- Hyperparameters: Tables III and VI report learning rates, weight decay, momentum, batch size, and epochs/iterations by method.
- Seeds: not reported.
- Training compute: 4 NVIDIA Tesla 3090 GPUs for detection; 4 NVIDIA GeForce RTX 3090 GPUs for segmentation.

### Data

- Datasets: [[CSDD]], with generalization experiments on [[NEU-DET]] and [[GC10-DET]].
- Data source: Metal plates machined to simulate casting surfaces, with defects created using production tools.
- Dataset size: 2100 images, 56,356 defects.
- Labels / annotations: Defect type and defect region manually annotated; detection and segmentation formats provided.
- Splits: 1343 training, 335 validation, 422 testing.
- Preprocessing: Gamma correction used during image acquisition processing to obtain uniform brightness.
- Augmentation: Detection experiments include random flip and, for YOLO-style methods, mosaic, mixup, HSV color-space augmentation, and random flip.
- Synthetic data: The paper uses a manufacturing-simulation approach to create defective samples on machined plates; it does not report generated synthetic images in the ML augmentation sense.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: Same 64/16/20 split is used for all reported methods.
- Used performance metrics: [[Average precision]], [[mAP]], [[IoU]], [[mIoU]], [[GFLOPs]].
- Primary metric: [[mAP]] for detection; [[mIoU]] for segmentation.
- Metric definitions: AP is area under the precision-recall curve; mAP averages AP across defect types; IoU is pixel-level intersection over union; mIoU averages IoU across defect types.
- Metric direction / units: Higher is better for AP, mAP, IoU, and mIoU; lower is better for GFLOPs.
- Baselines: Faster R-CNN, Cascade R-CNN, SSD, RetinaNet, YOLOv5, YOLOv8, YOLOv10, CenterNet, FCOS, Deformable DETR, Conditional DETR, FCN, U-Net, DeepLabv3, DeepLabv3plus, FastFCN, CGNet, DDRNet, PIDNet, Segmenter, SegFormer, MaskFormer, and Mask2Former.
- Benchmarks: [[CSDD benchmark]].
- Statistical tests: not reported.
- Failure cases: Rust detection and small/complex defects remain harder than scratches and spots.

## Evidence

### Experimental Setup

- Datasets: [[CSDD]], with generalization experiments on [[NEU-DET]] and [[GC10-DET]].
- Splits: 64% train, 16% validation, 20% test.
- Baselines: Detection and segmentation baselines listed above.
- Used performance metrics: AP, mAP, IoU, mIoU, and GFLOPs.
- Compute: 4 NVIDIA Tesla 3090 GPUs for detection; 4 NVIDIA GeForce RTX 3090 GPUs for segmentation.
- Hardware: NVIDIA 3090-class GPUs.
- Training time: not reported.
- Inference cost: GFLOPs reported, but wall-clock inference latency is not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Proposed detector vs YOLOv5 | CSDD detection | mAP | higher | 69.5% | 71.1% | Proposed method uses GAM and PConv. |
| Scratch AP | CSDD detection | AP | higher | 83.6% YOLOv5 | 84.4% | Proposed method. |
| Spot AP | CSDD detection | AP | higher | 71.3% YOLOv5 | 73.2% | Proposed method. |
| Rust AP | CSDD detection | AP | higher | 53.7% YOLOv5 | 55.8% | Rust remains hardest. |
| Best segmentation baseline | CSDD segmentation | mIoU | higher | not applicable | 54.29% | U-Net is best listed method. |
| Proposed method generalization | NEU-DET detection | mAP | higher | 62.0% YOLOv5 | 73.1% | Same split proportions reported. |
| Proposed method generalization | GC10-DET detection | mAP | higher | 59.5% YOLOv5 | 64.3% | Same split proportions reported. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] | Detection | Area under precision-recall curve | higher | no | Reported per defect type. |
| [[mAP]] | Detection | Average AP across defect types | higher | yes | Main detection metric. |
| [[IoU]] | Segmentation | TPpixel / (TPpixel + FPpixel + FNpixel) | higher | no | Reported per defect type. |
| [[mIoU]] | Segmentation | Mean IoU across defect types | higher | yes | Main segmentation metric. |
| [[GFLOPs]] | Complexity | Floating-point operations for a single forward pass | lower | no | Reported for detection and segmentation methods. |

### Ablations

- Base YOLOv5: 69.5% mAP, 15.8 GFLOPs.
- Base + GAM: 70.0% mAP, 17.2 GFLOPs.
- Base + PConv: 70.6% mAP, 14.6 GFLOPs.
- Base + GAM + PConv: 71.1% mAP, 16.2 GFLOPs.

## Dataset / Benchmark Details

- Source: Machined metal plates designed to simulate actual casting surfaces.
- Collection: Defects were produced using production tools under instructions from professional production and quality inspection engineers; images were captured with a visual sensor.
- Annotation: Six annotators labeled randomly divided groups, then double-checked and amended each other's annotations.
- Size: 2100 images and 56,356 annotated defects.
- Splits: 1343 train, 335 validation, 422 test.
- Modalities: High-resolution RGB images.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: Dataset uses manufactured plates and three defect classes, so coverage of real casting products and broader defect types is limited by the reported setup.
- Maintenance: Code and dataset are reported at GitHub, but maintenance policy is not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Rusts are harder to detect than scratches and spots because of complex shapes and larger size variation.
- Stated: Spots and rusts are harder to segment than scratches, with small defects and significant size variation remaining challenging.
- Inferred: Because the dataset is created from machined simulation plates, external validity to all real casting surfaces requires further validation.
- Inferred: The artifact license and maintenance policy are not available in the extracted paper text.

## Reproducibility

- Code: GitHub URL reported: https://github.com/Kerio99/CSDD.
- Data: GitHub URL reported: https://github.com/Kerio99/CSDD.
- Hyperparameters: Detection and segmentation training details are reported in Tables III and VI.
- Random seeds: not reported.
- Environment: MMDetection and MMSegmentation are reported for most baselines; official YOLO packages are used for YOLOv5, YOLOv8, and YOLOv10.
- Checkpoints / models: dataset and code reported available.
- Exact preprocessing: Images resized to 1024 x 1024 for experiments where stated; gamma correction used in image acquisition.
- Artifact status: code and dataset URL reported.

## Systems Details

- Hardware / software stack: MMDetection, MMSegmentation, official YOLO packages, NVIDIA 3090-class GPUs.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling behavior: not reported.
- Deployment assumptions: casting surface inspection with RGB visual sensors.

## Connections

### Graph Hubs

- Tasks: [[Casting surface defect detection]], [[Defect segmentation]], [[Metallic surface defect detection]]
- Datasets: [[CSDD]], [[GC10-DET]], [[NEU-DET]]
- Methods: [[YOLOv5 with global attention and partial convolution]], [[YOLOv5]], [[U-Net]], [[Deep convolutional neural network]]
- Metrics: [[Average precision]], [[mAP]], [[IoU]], [[mIoU]], [[GFLOPs]]
- Domains: [[Metal inspection]], [[Industrial visual inspection]]
- Benchmarks: [[CSDD benchmark]]

### Builds On

- [[YOLOv5]]: The proposed detector modifies YOLOv5 by adding a global attention mechanism and partial convolution modules.

### Contrasts With

- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]: Both contribute metallic surface defect benchmarks, but CSDD targets casting-like surfaces with 3648 x 3648 RGB images, 56,356 defects, and both detection and segmentation annotations.

### Shares Dataset

- [[GC10-DET]] and [[NEU-DET]]: Used for generalization experiments and dataset comparison, not as the main benchmark.

### Shares Task

- [[Casting surface defect detection]]: Main detection task.
- [[Defect segmentation]]: Pixel-level defect segmentation task.
- [[Metallic surface defect detection]]: Broader related metal surface inspection task.

### Shares Method

- [[YOLOv5 with global attention and partial convolution]]: Proposed detector.
- [[YOLOv5]]: Base detector.
- [[U-Net]]: Best listed segmentation baseline on CSDD.

### Shares Metric

- [[Average precision]], [[mAP]], [[IoU]], [[mIoU]], and [[GFLOPs]] are used for evaluation.

### Application / Domain

- [[Metal inspection]]: CSDD simulates casting surfaces on metal plates.
- [[Industrial visual inspection]]: The paper frames the dataset as supporting industrial vision research and manufacturing applications.

### Follow-Up Reading

- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]: Useful prior benchmark context for metallic surface defect detection.

## Questions

- What license governs CSDD on GitHub?
- How closely do the manufactured simulation plates match defect distributions on real casting production parts?
- Are the released annotations identical to the split used in the paper?
