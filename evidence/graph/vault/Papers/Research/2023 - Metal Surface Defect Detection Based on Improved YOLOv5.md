---
title: "Metal surface defect detection based on improved YOLOv5"
aliases:
  - "Metal surface defect detection based on improved YOLOv5"
paper_key: "doi:10.1038/s41598-023-47716-2"
paper_type: research
year: 2023
venue: "Scientific Reports"
authors:
  - "Chuande Zhou"
  - "Zhenyu Lu"
  - "Zhongliang Lv"
  - "Minghui Meng"
  - "Yonghu Tan"
  - "Kewen Xia"
  - "Kang Liu"
  - "Hailun Zuo"
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
  - "[[GC10-DET]]"
methods:
  - "CSPLayer"
  - "Global Attention Mechanism"
  - "[[Data augmentation]]"
architectures:
  - "[[YOLOv5]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.50-0.95]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "[[YOLOv5]]"
  - "Faster R-CNN"
doi: "10.1038/s41598-023-47716-2"
url: "https://doi.org/10.1038/s41598-023-47716-2"
pdf: "paper-inbox/10_processed/Research/2023 - Zhou - Metal Surface Defect Detection Based on Improved YOLOv5.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Zhou - Metal Surface Defect Detection Based on Improved YOLOv5.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Zhou - Metal Surface Defect Detection Based on Improved YOLOv5.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Zhou - Metal Surface Defect Detection Based on Improved YOLOv5.txt"
artifact_status: "open access PDF processed locally"
related_datasets:
  - "[[GC10-DET]]"
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

# Metal surface defect detection based on improved YOLOv5

## Summary

- The paper modifies [[YOLOv5]] for metal surface small-object detection by replacing C3 with CSPLayer and adding a Global Attention Mechanism.
- It evaluates on an augmented [[GC10-DET]] dataset with random rotation, brightness adjustment, sensor noise, and Gaussian blur, expanded to 4508 images and split 8:1:1.
- The proposed model improves YOLOv5s from 81.4% to 82.8% mAP@0.5 and from 53.8% to 55.5% mAP@0.5:0.95 on augmented GC10-DET.

## Paper Type

- Type: research.
- Why: proposes a detector architecture and evaluates it with ablations and comparisons.

## Problem

- Task: metal surface defect object detection.
- Setting: production of metal materials with complex texture and small defects.
- Inputs: GC10-DET metal surface defect images.
- Outputs: defect class and localized bounding box.
- Motivation: large background texture and small defects create false and missed detections.
- Assumptions: augmenting GC10-DET can represent practical variation in rotation, brightness, noise, and blur.

## Contribution

- Claimed: CSPLayer improves model flexibility and adaptability, while GAM improves cross-dimensional attention for speed and accuracy.
- Shown: the combined model improves precision, mAP@0.5, and mAP@0.5:0.95 over YOLOv5s on the augmented dataset.
- Inferred: augmentation is part of the dataset preparation, but the paper does not isolate augmentation itself as a before/after treatment.

## Method

- Core idea: improve YOLOv5s with a CSPLayer replacement and global attention.
- Architecture / algorithm: C3 is replaced with CSPLayer; GAMAttention is inserted into the detector.
- Objective / loss: YOLOv5 training objective; exact loss details not fully extracted.
- Optimization: learning rate 0.01, weight decay 0.0005, momentum 0.937.
- Training data: augmented GC10-DET.
- Data pipeline: random rotation, brightness adjustment, sensor noise, and Gaussian blur; dataset expanded to 4508 images.
- Augmentation / synthesis: geometric and photometric augmentation plus noise/blur; no synthetic generation reported.
- Inference: compared with FPS.
- Complexity / deployment constraints: model size and FPS are reported for industrial detection speed.

## ML / DL Extraction

### Task Formulation

- Input modality: metal surface images.
- Output target: bounding boxes and defect classes.
- Supervision: supervised object detection.
- Objective: improve small-defect detection accuracy and speed.

### Model And Training

- Model family: one-stage object detector.
- Architecture: YOLOv5s with CSPLayer and GAMAttention.
- Parameters: model size is used as a metric, but exact final size is not captured in the extracted result table.
- Losses: not reported in extracted text.
- Optimizer: SGD-style YOLO training implied by momentum/weight decay; exact optimizer name not reported in extracted text.
- Hyperparameters: learning rate 0.01; batch size 8; image size 640 x 640; weight decay 0.0005; momentum 0.937; 150 epochs.
- Seeds: not reported.
- Training compute: RTX 3060, Intel Core i5-12400F, Windows 10, PyTorch 1.12.1, Python 3.8, CUDA 12.

### Data

- Datasets: [[GC10-DET]].
- Dataset size: augmented dataset has 4508 images; 3608 train, 450 validation, 450 test.
- Labels / annotations: 10 GC10-DET defect classes with detection labels.
- Splits: 8:1:1 train/validation/test.
- Preprocessing: not reported beyond augmentation.
- Augmentation: random rotation, brightness adjustment, sensor noise, Gaussian blur.
- Synthetic data: not reported.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: ablation of CSPLayer and GAMAttention; comparison against Faster R-CNN and YOLOv5 variants.
- Used performance metrics: precision, recall, F1-score, mAP@0.5, mAP@0.5:0.95, FPS, model size.
- Primary metric: [[mAP@0.50]].
- Metric direction / units: all accuracy metrics higher is better; FPS higher is better.
- Baselines: YOLOv5s, YOLOv5m, YOLOv5l, YOLOv5x, Faster R-CNN.
- Statistical tests: not reported.
- Failure cases: attention alternatives can miss small inclusions; recall slightly drops with GAMAttention.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Proposed model vs YOLOv5s | Augmented GC10-DET object detection | Precision (%) | higher | 88.5 | 93.8 | Ablation table. |
| Proposed model vs YOLOv5s | Augmented GC10-DET object detection | Recall (%) | higher | 77.1 | 76.0 | Recall drops. |
| Proposed model vs YOLOv5s | Augmented GC10-DET object detection | mAP@0.5 (%) | higher | 81.4 | 82.8 | Combined CSPLayer + GAMAttention. |
| Proposed model vs YOLOv5s | Augmented GC10-DET object detection | mAP@0.5:0.95 (%) | higher | 53.8 | 55.5 | Combined CSPLayer + GAMAttention. |
| Proposed model | Augmented GC10-DET object detection | FPS | higher | 78.1 | 79.4 | Compared with YOLOv5s. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| Precision | Detection correctness | percent | higher | no | Formula reported. |
| Recall | Detection completeness | percent | higher | no | Formula reported. |
| F1-score | Combined precision/recall | score | higher | no | Formula reported. |
| mAP@0.5 | Detection accuracy | percent at IoU 0.5 | higher | yes | Main result table. |
| mAP@0.5:0.95 | COCO-style detection accuracy | percent | higher | no | Main result table. |
| FPS | Inference speed | frames per second | higher | no | Reported in model comparison. |

### Ablations

- CSPLayer alone improves mAP@0.5 from 81.4 to 81.5 and mAP@0.5:0.95 from 53.8 to 55.1.
- GAMAttention alone improves mAP@0.5 to 82.4 but reduces recall to 77.0.
- CSPLayer + GAMAttention reaches 82.8 mAP@0.5 and 55.5 mAP@0.5:0.95.

## Limitations

- Stated: not reported.
- Inferred: augmentation is used for all reported experiments, so the paper does not quantify the independent benefit of data augmentation.

## Reproducibility

- Code: not reported.
- Data: GC10-DET is public; augmented dataset construction is described at a high level.
- Hyperparameters: learning rate, batch size, image size, weight decay, momentum, and epochs are reported.
- Random seeds: not reported.
- Environment: RTX 3060, Windows 10, PyTorch 1.12.1, Python 3.8, CUDA 12.
- Artifact status: open access PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Object detection]], [[Metallic surface defect detection]].
- Methods: [[Data augmentation]], CSPLayer, Global Attention Mechanism.
- Datasets: [[GC10-DET]].
- Domains: [[Metal inspection]].
- Metrics: [[Precision]], [[Recall]], [[F1-score]], [[mAP@0.50]], [[mAP@0.50-0.95]], [[FPS]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Shares dataset | Both evaluate metal surface object detection on [[GC10-DET]]. |
| [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] | Shares dataset and method family | Both use [[GC10-DET]] and data augmentation, but this paper uses fixed augmentation and architecture changes rather than automatic augmentation search. |

### Backlinks Updated

- [[GC10-DET]], [[Metal inspection]], and [[Data augmentation]] link back to this paper.

## Questions

- Does the augmented GC10-DET split preserve original-image grouping and avoid augmented variants crossing train/test boundaries?
- Would the same model improve over YOLOv5s on the unaugmented GC10-DET split?
