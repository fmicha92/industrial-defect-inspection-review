---
title: "Resilient machine learning for steel surface defect detection based on lightweight convolution"
aliases:
  - "Resilient machine learning for steel surface defect detection based on lightweight convolution"
paper_key: "doi:10.1007/s00170-024-14403-z"
paper_type: research
year: 2024
venue: "The International Journal of Advanced Manufacturing Technology"
authors:
  - "Li-Juan Liu"
  - "Yu Zhang"
  - "Hamid Reza Karimi"
status: processed
processed_at: "2026-06-11"
topics:
  - "metal surface defect detection"
tasks:
  - "[[Object detection]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[GC10-DET]]"
methods:
  - "ScConv"
  - "GSConv"
  - "VoV-GSCSP"
  - "[[Coordinate attention]]"
architectures:
  - "[[YOLOv8]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP@0.50]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "[[YOLOv8]]"
  - "[[YOLOv5]]"
  - "YOLOv6"
doi: "10.1007/s00170-024-14403-z"
url: "https://doi.org/10.1007/s00170-024-14403-z"
pdf: "paper-inbox/10_processed/Research/2024 - Liu - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Liu - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Liu - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Liu - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution.txt"
artifact_status: "open access PDF processed locally"
related_datasets:
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Object detection]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Metallic surface defect detection]]"
tags:
  - paper
---

# Resilient machine learning for steel surface defect detection based on lightweight convolution

## Summary

- The paper proposes a lightweight YOLOv8n-based detector for steel surface defects by adding ScConv, GSConv/VoV-GSCSP, Coordinate Attention, and LeakyReLU.
- It evaluates object detection on [[NEU-DET]] and [[GC10-DET]], reporting higher [[mAP@0.50]] and competitive [[FPS]] against YOLO-family baselines.
- The improvement is architectural; the paper does not report a synthetic-data or augmentation-before/after experiment.

## Paper Type

- Type: research.
- Why: proposes and evaluates a modified detector architecture with ablation studies and benchmark comparisons.

## Problem

- Task: steel surface defect object detection.
- Setting: visual inspection of steel surfaces in production, transport, and handling.
- Inputs: metal surface defect images.
- Outputs: defect class and bounding-box localization.
- Motivation: manual and traditional inspection are low-efficiency, subjective, and vulnerable to missed or false detections.
- Assumptions: public steel surface datasets are suitable proxies for industrial defect detection performance.

## Contribution

- Claimed: a resilient machine-learning detector that improves YOLOv8n with lightweight convolution, attention, and activation-function changes.
- Shown: mAP improves from 73.0% to 77.7% on NEU-DET and from 56.7% to 62.2% on GC10-DET in the paper's ablations.
- Inferred: the paper is best treated as an architecture-improvement paper, not as an augmentation or synthesis paper.

## Method

- Core idea: reduce redundant features while improving feature selection and target localization in YOLOv8n.
- Architecture / algorithm: ScConv is added before SPPF in the backbone; GSConv and VoV-GSCSP replace neck-layer convolution/C2f components; Coordinate Attention is added in the neck; LeakyReLU replaces the original activation.
- Objective / loss: YOLOv8 losses are used; the paper mentions BCE for classification and CIoU for bounding-box regression in the YOLOv8 review.
- Optimization: not fully reported beyond the experimental environment and training parameters.
- Training data: NEU-DET and GC10-DET.
- Data pipeline: GC10-DET split reported as 1836 training, 229 testing, and 229 validation images.
- Augmentation / synthesis: not reported as a contribution or controlled experiment.
- Inference: evaluated with FPS.
- Complexity / deployment constraints: lightweight convolution is motivated by complexity and real-time deployment.

## ML / DL Extraction

### Task Formulation

- Input modality: surface defect images.
- Output target: defect class and bounding box.
- Supervision: supervised object detection.
- Objective: maximize detection accuracy while preserving real-time speed.

### Model And Training

- Model family: one-stage object detector.
- Architecture: modified YOLOv8n with ScConv, GSConv, VoV-GSCSP, Coordinate Attention, and LeakyReLU.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: BCE and CIoU are described for YOLOv8; exact final loss settings are not otherwise detailed.
- Optimizer: not reported.
- Hyperparameters: batch size 32, epochs 300.
- Seeds: not reported.
- Training compute: RTX 3080 GPU; Intel Xeon Platinum 8255C CPU; CUDA 11.8; Python 3.8; PyTorch 2.0.0.

### Data

- Datasets: [[NEU-DET]] and [[GC10-DET]].
- Dataset size: GC10-DET split as 1836 train, 229 test, 229 validation; NEU-DET size not captured in the extracted section.
- Labels / annotations: object detection classes and boxes.
- Splits: train/test/validation for GC10-DET; NEU-DET split not fully reported in the extracted text.
- Preprocessing: not reported.
- Augmentation: not reported.
- Synthetic data: not applicable.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: comparison against YOLOv5, YOLOv6, YOLOv8 variants, and literature methods; ablation studies on NEU-DET and GC10-DET.
- Used performance metrics: AP, mAP, FPS.
- Primary metric: [[mAP@0.50]].
- Metric direction / units: mAP and AP higher is better; FPS higher is better.
- Baselines: YOLOv8n, YOLOv8s/m/l, YOLOv5, YOLOv6, and two literature methods.
- Statistical tests: not reported.
- Failure cases: the conclusion says mAP still needs improvement.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Final detector vs YOLOv8n | NEU-DET object detection | mAP@0.50 (%) | higher | 73.0 | 77.7 | Ablation table. |
| Final detector vs YOLOv8n | NEU-DET object detection | FPS | higher | 11.57 | 17.36 | Ablation table. |
| Final detector vs YOLOv8n | GC10-DET object detection | mAP@0.50 (%) | higher | 56.7 | 62.2 | Ablation table. |
| Final detector vs YOLOv8n | GC10-DET object detection | FPS | higher | 19.53 | 15.63 | Accuracy improves while speed drops versus YOLOv8n. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| AP | Per-class object detection | Average precision | higher | no | Formula given in paper. |
| mAP | Multi-class object detection | Mean of AP values | higher | yes | Reported as mAP50 / %. |
| FPS | Inference speed | frames per second | higher | no | Used for deployment trade-off. |

### Ablations

- On NEU-DET, the final combination improved mAP from 73.0 to 77.7 and FPS from 11.57 to 17.36.
- On GC10-DET, ScConv, GSConv/VoV-GSCSP, Coordinate Attention, and LeakyReLU each affected mAP; the final combination reached 62.2 mAP and 15.63 FPS.

## Limitations

- Stated: the model's mAP still needs improvement.
- Inferred: no augmentation/synthesis ablation is reported; results isolate architecture components rather than data-pipeline changes.

## Reproducibility

- Code: not reported.
- Data: public datasets used, but dataset download details are not central in the paper.
- Hyperparameters: batch size, epochs, software stack, and hardware are reported.
- Random seeds: not reported.
- Environment: RTX 3080, CUDA 11.8, Python 3.8, PyTorch 2.0.0.
- Artifact status: open access PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Object detection]], [[Metallic surface defect detection]].
- Methods: ScConv, GSConv, VoV-GSCSP, [[Coordinate attention]].
- Datasets: [[NEU-DET]], [[GC10-DET]].
- Domains: [[Metal inspection]].
- Metrics: [[Average precision]], [[mAP@0.50]], [[FPS]].
- Concepts: [[Surface defect detection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Shares dataset | Both evaluate object detection on [[GC10-DET]]. |
| [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] | Shares dataset and task | Both improve YOLO-family metal surface defect detectors and evaluate on [[GC10-DET]]. |

### Backlinks Updated

- [[GC10-DET]], [[Metal inspection]], and [[Coordinate attention]] link back to this paper.

## Questions

- Does the implementation release code or trained weights outside the paper?
- How sensitive are the reported gains to data augmentation, if any was used but not isolated?
