---
title: "A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation"
aliases:
  - "A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation"
paper_key: "doi:10.1155/2022/9577096"
paper_type: research
year: 2022
venue: "Computational Intelligence and Neuroscience"
authors:
  - "Gang Li"
  - "Rui Shao"
  - "Honglin Wan"
  - "Mingle Zhou"
  - "Min Li"
status: processed
processed_at: "2026-06-11"
topics:
  - "industrial surface defect detection"
tasks:
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[BSData]]"
  - "[[NEU-DET]]"
  - "RSDDs"
  - "NRSD-MN"
methods:
  - "[[Data augmentation]]"
  - "[[Multi-head attention]]"
  - "feature distribution smoothing block"
architectures:
  - "[[YOLOv5]]"
metrics:
  - "[[mAP@0.50]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "YOLOv3"
  - "YOLOv4"
  - "[[YOLOv5]]"
doi: "10.1155/2022/9577096"
url: "https://doi.org/10.1155/2022/9577096"
pdf: "paper-inbox/10_processed/Research/2022 - Li - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Li - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Li - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Li - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation.txt"
artifact_status: "open access PDF processed locally"
related_datasets:
  - "[[BSData]]"
  - "[[NEU-DET]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Object detection]]"
related_methods:
  - "[[Data augmentation]]"
related_concepts:
  - "[[Surface defect detection]]"
tags:
  - paper
---

# A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation

## Summary

- The paper proposes an industrial surface defect object detector based on attention-enhanced CSPDarkNet53, feature distribution smoothing, and PANet feature fusion.
- It evaluates on one internal glass-bottle dataset and four public datasets, including [[BSData]] and [[NEU-DET]].
- On BSData, the method reports 82.00 mAP@0.5, compared with 81.79 for YOLOv5x and 81.38 for the CSPDarkNet53+SPP+PANet ablation baseline.

## Paper Type

- Type: research.
- Why: proposes and evaluates an object detection model with benchmark comparisons and module ablations.

## Problem

- Task: industrial product surface defect object detection.
- Setting: industrial scenes with changing camera angle, shooting distance, scale variation, angle variation, and motion blur.
- Inputs: industrial surface defect images.
- Outputs: bounding boxes and defect classes.
- Motivation: practical inspection images vary in scale, angle, and blur, degrading object-detection performance.
- Assumptions: attention augmentation and higher-resolution feature fusion improve detection across multiple defect datasets.

## Contribution

- Claimed: lower-level high-resolution features and multi-head self-attention improve practical surface defect detection.
- Shown: the method performs competitively across internal, railway, ball-screw, NEU-DET, and NRSD-MN datasets.
- Inferred: data augmentation is part of the training strategy, but the ablations isolate attention/FDS blocks rather than augmentation alone.

## Method

- Core idea: improve a YOLO-style detector with attention and feature fusion for industrial surface defects.
- Architecture / algorithm: CSPDarkNet53 + SPP + PANet baseline, plus MHSA attention block and feature distribution smoothing block.
- Objective / loss: not fully reported in extracted text.
- Optimization: freeze training followed by unfreezing; epoch counts vary by dataset.
- Training data: internal dataset, RSDDs, BSData, NEU-DET, NRSD-MN.
- Data pipeline: all datasets split 5:2:3 train/validation/test.
- Augmentation / synthesis: data augmentation, grayscale filling, and automatic conversion to three-channel RGB are adopted; no synthetic generation is reported.
- Inference: object detection with mAP@0.5.
- Complexity / deployment constraints: attention block increases computation; FDS block has less impact on computation and inference speed.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial surface images.
- Output target: object detection bounding boxes and classes.
- Supervision: supervised object detection.
- Objective: improve mAP@0.5 across multiple industrial defect datasets.

### Model And Training

- Model family: YOLO-style object detector.
- Architecture: CSPDarkNet53, SPP, PANet, MHSA attention block, FDS block.
- Parameters: not reported.
- Pretraining: freeze/unfreeze training suggests transfer learning, but exact pretraining source is not fully reported in extracted text.
- Losses: not reported.
- Optimizer: not reported.
- Hyperparameters: BSData training uses batch size 2 on NVIDIA RTX 3060; freeze training for 50 epochs and unfreeze training for 50 epochs.
- Seeds: not reported.
- Training compute: RTX 3060 for internal/RSDDs/BSData; RTX 3080 for NEU-DET and NRSD-MN.

### Data

- Datasets: internal glass-bottle bottom mold-point dataset, RSDDs, [[BSData]], [[NEU-DET]], NRSD-MN.
- Splits: 5:2:3 train/validation/test ratio.
- BSData subset: 394 images at 1130 x 460 resolution are selected in the study.
- Labels / annotations: object detection labels.
- Preprocessing: grayscale filling and automatic conversion to three-channel RGB.
- Augmentation: data augmentation is adopted; specific augmentation operations are not fully enumerated in the extracted text.
- Synthetic data: not reported.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: compare against YOLOv3, YOLOv4, YOLOv5l, YOLOv5x; conduct module ablations on each dataset.
- Used performance metrics: mAP@0.5.
- Primary metric: [[mAP@0.50]].
- Metric direction / units: higher is better; percent.
- Baselines: YOLOv3, YOLOv4, YOLOv5l, YOLOv5x, CSPDarkNet53+SPP+PANet ablation.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Proposed method vs YOLOv5x | BSData object detection | mAP@0.5 | higher | 81.79 | 82.00 | Table 1. |
| Proposed method vs ablation baseline | BSData object detection | mAP@0.5 | higher | 81.38 | 82.00 | Table 4. |
| Attention block | BSData object detection | mAP@0.5 | higher | 81.38 | 81.59 | +0.21 in Table 4. |
| FDS block | BSData object detection | mAP@0.5 | higher | 81.38 | 81.79 | +0.41 in Table 4. |
| Proposed method vs YOLOv5x | NEU-DET object detection | mAP@0.5 | higher | 74.07 | 74.67 | Table 1. |
| Proposed method vs ablation baseline | NEU-DET object detection | mAP@0.5 | higher | 70.35 | 74.67 | Table 5. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| mAP@0.5 | Object detection | PASCAL VOC-style mAP at IoU 0.5 | higher | yes | Main metric across datasets. |

### Ablations

- On BSData, CSPDarkNet53+SPP+PANet scores 81.38 mAP; attention block scores 81.59; FDS block scores 81.79; both together score 82.00.
- On NEU-DET, the same ablation sequence scores 70.35, 72.08, 71.22, and 74.67 mAP.
- On NRSD-MN, the final method improves from 75.4 to 81.09 mAP.

## Limitations

- Stated: not reported in extracted conclusion.
- Inferred: BSData improvement over YOLOv5x is small; augmentation/preprocessing is not isolated from architectural changes.

## Reproducibility

- Code: not reported.
- Data: public datasets used; internal dataset not reported as public.
- Hyperparameters: split ratio and per-dataset training epoch details are partly reported.
- Random seeds: not reported.
- Environment: RTX 3060 and RTX 3080 GPUs.
- Artifact status: open access PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Object detection]].
- Methods: [[Data augmentation]], [[Multi-head attention]].
- Datasets: [[BSData]], [[NEU-DET]].
- Domains: [[Metal inspection]].
- Metrics: [[mAP@0.50]].
- Concepts: [[Surface defect detection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] | Shares dataset | This paper evaluates object detection on [[BSData]]. |
| [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] | Shares task and dataset family | Both evaluate metallic surface defect object detection using NEU-derived datasets. |

### Backlinks Updated

- [[BSData]], [[Metal inspection]], and [[Data augmentation]] link back to this paper.

## Questions

- Which concrete augmentation operations were applied in the reported experiments?
- Is the internal glass-bottle dataset available for replication?
