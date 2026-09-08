---
title: "Online PCB Defect Detector on a New PCB Defect Dataset"
paper_key: "sha256:0ccaa125d5cbfb8845ef22c1a2811275d98554ed37e64b5d819341181484fb96"
paper_type: dataset
year: 2019
venue: "not reported"
arxiv: "1902.06197"
url: "https://arxiv.org/abs/1902.06197"
authors:
  - "Sanli Tang"
  - "Fan He"
  - "Xiaolin Huang"
  - "Jie Yang"
status: processed
processed_at: 2026-05-20
topics:
  - PCB defect detection
  - online detection
  - PCB dataset
tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[DeepPCB]]"
methods:
  - "[[Group pyramid pooling]]"
metrics:
  - "[[mAP]]"
  - "[[FPS]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "mAP: mean average precision across six PCB defect categories."
  - "F1-score/F-mean: harmonic mean of precision and recall for defect detection."
  - "FPS: inference throughput in frames per second."
code: "reported available: https://github.com/tangsanli5201/DeepPCB"
data: "reported available: https://github.com/tangsanli5201/DeepPCB"
artifact_status: "dataset and code reported available"
related_datasets:
  - "[[DeepPCB]]"
related_tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
related_methods:
  - "[[Group pyramid pooling]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2019 - Tang - Online PCB Defect Detector on a New PCB Defect Dataset.md"
extracted_text: "paper-inbox/90_processing/text/2019 - Tang - Online PCB Defect Detector on a New PCB Defect Dataset.txt"
pdf: "paper-inbox/10_processed/2019 - Tang - Online PCB Defect Detector on a New PCB Defect Dataset.pdf"
source_file: "paper-inbox/10_processed/2019 - Tang - Online PCB Defect Detector on a New PCB Defect Dataset.pdf"
tags:
  - paper
  - dataset
  - pcb
---

# Online PCB Defect Detector on a New PCB Defect Dataset

## Summary

- Introduces [[DeepPCB]], a public PCB defect dataset with 1,500 template/test image pairs and six defect categories.
- Proposes an online PCB defect detector with a [[Group pyramid pooling]] module.
- Reports 98.6% mAP at 62 FPS on DeepPCB.

## Paper Type

Dataset paper with an accompanying detector.

## Contribution

- Claimed: DeepPCB is the first public dataset for PCB defect detection at the time of the paper.
- Shown: The dataset includes 640 x 640 defect-free template images and tested images with bounding-box/class annotations.
- Shown: The detector improves mAP while maintaining low computation time.
- Shown: The max-pooling GPP variant reports 98.6% mAP and 98.2 F-mean at 62 FPS.

## Method

The detector treats PCB defect detection as object detection over template/test image pairs. The proposed group pyramid pooling module extracts multi-scale features for PCB defects and is evaluated against object detection baselines and ablations.

The network uses a convolutional backbone with shared parameters for the template and tested image, subtracts feature maps, applies GPP, predicts small/medium/large boxes, and applies non-maximum suppression. The training setup uses a single Titan X GPU, Adam, initial learning rate 10^-3, 0.0005 weight decay, 500 epochs, batch size 16, learning-rate decay of 0.33 every 100 epochs, and about 0.5 day of training.

## Evidence

| Evidence | Reported detail |
|---|---|
| Dataset | DeepPCB |
| Size | 1,500 template/test image pairs |
| Defect types | 6 |
| Dataset availability | GitHub URL reported in the paper |
| Main result | 98.6% mAP at 62 FPS |
| Ablation | GPP improves mAP by 1.5% over average pooling |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP]] | Six-class PCB defect detection on [[DeepPCB]] | Mean average precision over open, short, mousebite, spur, copper, and pin-hole classes | Higher is better | yes | Ours-MP: 98.6; Ours-AP: 97.1; Faster R-CNN-style baseline: 97.6; SSD: 95.9; YOLO: 92.6; image processing baseline: 89.3. |
| [[FPS]] | Inference throughput | Frames per second | Higher is better | no | Ours: 62 FPS; SSD: 64 FPS; YOLO: 34 FPS; Faster R-CNN-style baseline: 4 FPS; image processing baseline: 78 FPS. |
| [[Precision]] | Ablation on [[DeepPCB]] | Detection precision | Higher is better | no | SSD-FPN: 94.9; ours-non-GPP: 94.3; ours-MP: 98.2. |
| [[Recall]] | Ablation on [[DeepPCB]] | Detection recall | Higher is better | no | SSD-FPN: 96.8; ours-non-GPP: 96.3; ours-MP: 98.1. |
| [[F1-score]] | Ablation and speed/accuracy comparison | F-mean / harmonic mean of precision and recall | Higher is better | no | SSD-FPN: 95.8; ours-non-GPP: 95.3; ours-MP: 98.2. |

## Limitations

- The dataset is built around paired template/test images, so methods may assume availability of a defect-free reference.
- The extracted text does not report DOI or full venue metadata.
- The tested images include manually augmented artificial defects, so performance may not fully reflect natural defect distributions.
- Evaluation uses IoU > 0.33 for a correct detection, which is less strict than common IoU 0.5 object-detection settings.

## Connections

### Graph Hubs

- Tasks: [[PCB defect detection]], [[PCB defect classification]]
- Datasets: [[DeepPCB]]
- Methods: [[Group pyramid pooling]]
- Metrics: [[mAP]], [[FPS]], [[Precision]], [[Recall]], [[F1-score]]
- Domains: [[Semiconductor and electronics]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]] | Shares task | Both introduce PCB defect datasets and detection/classification baselines. |

## Questions

- Is the DeepPCB GitHub still available, and what exact license does it use?
- How sensitive is the model to image alignment quality?
