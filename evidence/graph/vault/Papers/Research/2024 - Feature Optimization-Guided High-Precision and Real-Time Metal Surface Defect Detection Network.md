---
title: "Feature optimization-guided high-precision and real-time metal surface defect detection network"
aliases:
  - "FOHR Net"
  - "Feature optimization-guided high-precision and real-time metal surface defect detection network"
paper_key: "doi:10.1038/s41598-024-83430-3"
paper_type: research
year: 2024
venue: "Scientific Reports"
authors:
  - "Sixian Chan"
  - "Suqiang Li"
  - "Hongkai Zhang"
  - "Xiaolong Zhou"
  - "Jiafa Mao"
  - "Feng Hong"
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
  - "[[APDDD]]"
methods:
  - "multi-layer feature alignment"
  - "dual-branch feature reorganization"
architectures:
  - "FOHR Net"
metrics:
  - "[[mAP]]"
  - "[[FPS]]"
primary_metric: "[[mAP]]"
baselines:
  - "YOLOv8s"
  - "YOLOv3-spp"
  - "[[YOLOv5]]"
doi: "10.1038/s41598-024-83430-3"
url: "https://doi.org/10.1038/s41598-024-83430-3"
pdf: "paper-inbox/10_processed/Research/2024 - Chan - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Chan - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Chan - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Chan - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network.txt"
artifact_status: "open access PDF processed locally"
related_datasets:
  - "[[GC10-DET]]"
  - "[[APDDD]]"
  - "[[NEU-DET]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Object detection]]"
related_concepts:
  - "[[Surface defect detection]]"
tags:
  - paper
---

# Feature optimization-guided high-precision and real-time metal surface defect detection network

## Summary

- The paper proposes FOHR Net, a metal surface object detector built around multi-layer feature alignment and dual-branch feature reorganization.
- It evaluates on [[NEU-DET]], [[GC10-DET]], and [[APDDD]], reporting mAP values of 78.3%, 70.5%, and 65.9%, respectively.
- The reported gains are architecture/component gains, not augmentation or synthesis gains.

## Paper Type

- Type: research.
- Why: proposes a new detection network and validates it with benchmark comparisons, ablations, visualization, and cross-validation.

## Problem

- Task: metal surface defect object detection.
- Setting: metal materials with overlapping defects, intra-class variation, inter-class similarity, and low-clarity defect contours.
- Inputs: defect images from public metal surface datasets.
- Outputs: class-specific detection boxes.
- Motivation: missed and false detections occur when feature extraction fails under similar textures and blurry contours.
- Assumptions: feature alignment and reorganization can preserve shallow/detail and deep/semantic cues for small or overlapping defects.

## Contribution

- Claimed: FOHR Net improves defect feature expressiveness through multi-layer feature alignment and dual-branch feature reorganization.
- Shown: FOHR Net obtains the best mAP among compared detectors on NEU-DET, GC10-DET, and APDDD in the reported tables.
- Inferred: APDDD evaluation is useful evidence for aluminum profile defect detection, but APDDD is not used for ablation in the extracted table.

## Method

- Core idea: align multi-layer feature maps and reorganize channel/slice features to reduce feature loss and improve detection.
- Architecture / algorithm: multi-layer feature alignment module fuses shallow and deep information; dual-branch feature reorganization splits and transforms features, applies channel-level soft attention, and adaptively merges outputs.
- Objective / loss: ECIoU loss is mentioned as an optimization component; full loss setup not completely reported in extracted text.
- Optimization: SGD optimizer, momentum 0.937.
- Training data: NEU-DET, GC10-DET, APDDD.
- Data pipeline: random 7:3 train/test split for all three datasets.
- Augmentation / synthesis: not reported.
- Inference: compared with FPS and real-time threshold.
- Complexity / deployment constraints: speed above 30 FPS is treated as an industrial real-time benchmark.

## ML / DL Extraction

### Task Formulation

- Input modality: metal surface defect images.
- Output target: defect class and localization.
- Supervision: supervised object detection.
- Objective: improve detection mAP while retaining real-time speed.

### Model And Training

- Model family: object detection network.
- Architecture: FOHR Net with CSPDarkNet53 feature extraction, multi-layer feature alignment, and dual-branch feature reorganization.
- Parameters: not reported in extracted text.
- Pretraining: all models are trained without pre-training weights.
- Losses: ECIoU loss is referenced; exact complete objective not fully reported.
- Optimizer: SGD.
- Hyperparameters: batch size 8, initial learning rate 0.01, momentum 0.937, epochs 500, image size 640 x 640, early stopping after 50 epochs without improvement.
- Seeds: not reported.
- Training compute: Intel Xeon Gold 6130 CPU, NVIDIA GeForce RTX 3090 24GB GPU, Windows 10, PyTorch 2.0.1, CUDA 11.8, cuDNN 8.6.0.

### Data

- Datasets: [[NEU-DET]], [[GC10-DET]], [[APDDD]].
- Dataset sizes: NEU-DET 1800 images; GC10-DET 2298 images; APDDD 1885 images.
- Splits: NEU-DET 1260 train / 540 test; GC10-DET 1608 train / 690 test; APDDD 1319 train / 566 test.
- Labels / annotations: object-detection classes.
- Preprocessing: not reported.
- Augmentation: not reported.
- Synthetic data: not applicable.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: comparison with mainstream one-stage and two-stage detection models; ablation on NEU-DET and GC10-DET; visualization; cross-validation on NEU-DET and GC10-DET.
- Used performance metrics: mAP, FPS.
- Primary metric: [[mAP]].
- Metric direction / units: mAP higher is better; FPS higher is better.
- Baselines: DDN, Faster R-CNN, Cascade R-CNN, FCOS, YOLO-family detectors, and recent literature detectors.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| FOHR Net | NEU-DET object detection | mAP (%) | higher | 76.1 | 78.3 | Baseline is FOHR Net without MFAM/DFRM in ablation. |
| FOHR Net | GC10-DET object detection | mAP (%) | higher | 64.4 | 70.5 | Ablation table. |
| FOHR Net | APDDD object detection | mAP (%) | higher | not reported | 65.9 | Reported as best APDDD comparison result. |
| MFAM only | GC10-DET object detection | mAP (%) | higher | 64.4 | 69.7 | Multi-layer feature alignment impact. |
| DFRM only | GC10-DET object detection | mAP (%) | higher | 64.4 | 69.1 | Dual-branch feature reorganization impact. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| mAP | Object detection accuracy | percent | higher | yes | Main metric across three datasets. |
| FPS | Inference speed | frames per second | higher | no | Used for real-time deployment trade-off. |

### Ablations

- Baseline without MFAM/DFRM: 76.1 mAP on NEU-DET and 64.4 mAP on GC10-DET.
- MFAM only: 77.3 mAP on NEU-DET and 69.7 mAP on GC10-DET.
- DFRM only: 77.4 mAP on NEU-DET and 69.1 mAP on GC10-DET.
- MFAM + DFRM: 78.3 mAP on NEU-DET and 70.5 mAP on GC10-DET.

## Limitations

- Stated: future directions include limitations discussed in the paper's discussion section, but the extracted text does not preserve specific limitation details.
- Inferred: no synthetic-data or augmentation comparison is reported; APDDD is used for external evaluation but not for module ablation in the extracted table.

## Reproducibility

- Code: not reported.
- Data: public datasets; APDDD source URL appears in the extracted references but detailed access conditions are not discussed.
- Hyperparameters: optimizer, learning rate, batch size, epochs, image size, early stopping, and hardware/software environment are reported.
- Random seeds: not reported.
- Environment: RTX 3090 24GB GPU, PyTorch 2.0.1, CUDA 11.8.
- Artifact status: open access PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Object detection]], [[Metallic surface defect detection]].
- Methods: multi-layer feature alignment, dual-branch feature reorganization.
- Datasets: [[NEU-DET]], [[GC10-DET]], [[APDDD]].
- Domains: [[Metal inspection]].
- Metrics: [[mAP]], [[FPS]].
- Concepts: [[Surface defect detection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] | Shares dataset and task | Both report YOLO-family metal surface detection on [[NEU-DET]], [[GC10-DET]], and [[APDDD]]. |
| [[2025 - You Only Look Once-Aluminum]] | Shares dataset | Both evaluate aluminum profile defect detection on [[APDDD]]. |

### Backlinks Updated

- [[GC10-DET]], [[APDDD]], and [[Metal inspection]] link back to this paper.

## Questions

- Are exact APDDD class-level results available in the table OCR, and do they show consistent improvements across all aluminum defect classes?
- Is code or a trained FOHR Net implementation available?
