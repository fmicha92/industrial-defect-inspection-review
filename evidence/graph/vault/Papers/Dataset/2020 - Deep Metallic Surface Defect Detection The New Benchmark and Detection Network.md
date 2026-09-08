---
title: "Deep Metallic Surface Defect Detection: The New Benchmark and Detection Network"
aliases:
  - "Deep Metallic Surface Defect Detection"
paper_key: "sha256:330bf36b67008058389ec82b0a477610a9e1197bf87d1048a76870430e091ba6"
paper_type: dataset
year: 2020
venue: "Sensors"
authors:
  - "Xiaoming Lv"
  - "Fajie Duan"
  - "Jia-jia Jiang"
  - "Xiao Fu"
  - "Lin Gan"
status: processed
processed_at: 2026-05-20
topics:
  - metallic surface defect detection
  - object detection
  - surface inspection benchmark
tasks:
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
methods:
  - "[[EDDN]]"
  - "[[Single Shot MultiBox Detector]]"
  - "[[Hard negative mining]]"
  - "[[Data augmentation]]"
metrics:
  - "[[Recall]]"
  - "[[Average precision]]"
  - "[[mAP]]"
  - "[[Inference time]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "Recall: correctly detected testing images divided by all testing images for each defect category."
  - "Average precision: per-class detected precision summarized across detection thresholds/ranking."
  - "mAP: mean average precision across defect categories."
  - "Inference time: milliseconds per image and seconds for the full testing set."
data: "reported available: https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets"
artifact_status: "dataset reported available"
url: "https://doi.org/10.3390/s20061562"
related_datasets:
  - "[[GC10-DET]]"
  - "[[NEU-DET]]"
related_tasks:
  - "[[Metallic surface defect detection]]"
related_methods:
  - "[[EDDN]]"
  - "[[Single Shot MultiBox Detector]]"
  - "[[Hard negative mining]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Lv - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Lv - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network.txt"
pdf: "paper-inbox/10_processed/2020 - Lv - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network.pdf"
source_file: "paper-inbox/10_processed/2020 - Lv - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network.pdf"
tags:
  - paper
  - dataset
  - metal-inspection
---

# Deep Metallic Surface Defect Detection

## Summary

- Introduces [[GC10-DET]], a public metallic surface defect dataset collected on steel sheet surfaces with 3,570 grayscale images and 10 defect types.
- Proposes [[EDDN]], an end-to-end defect detection network based on [[Single Shot MultiBox Detector]].
- Evaluates on [[NEU-DET]] and GC10-DET using recall, AP, and mAP, reporting that the proposed method has the best mAP on GC10-DET.

## Paper Type

Dataset paper with a benchmark detector.

## Contribution

- Claimed: GC10-DET addresses the limited scale and defect richness of existing metallic surface defect datasets.
- Shown: The dataset is available on GitHub and contains real collected steel sheet defects.
- Shown: EDDN uses multi-scale detection, hard negative mining, and data augmentation.

## Method

EDDN builds on SSD-style one-stage detection. It predicts confidence scores and default boxes at multiple scales, applies hard negative mining for imbalance, and uses data augmentation for limited training data.

## Evidence

| Evidence | Reported detail |
|---|---|
| GC10-DET size | 3,570 grayscale images |
| GC10-DET classes | 10 defect types |
| Availability | GitHub URL reported in paper |
| Comparison datasets | NEU-DET and GC10-DET |
| Metrics | Recall, AP, mAP |
| Result summary | Proposed method reports best mAP on GC10-DET |

### Performance Metrics

| Metric | Dataset | Used for | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP]] | [[NEU-DET]] | Six-class metallic surface defect detection | Higher is better | yes | Proposed method 0.724; SSD 0.724; Faster R-CNN 0.711; YOLO-V2 0.503; YOLO-V3 0.453. |
| [[mAP]] | [[GC10-DET]] | Ten-class metallic surface defect detection | Higher is better | yes | Proposed method 0.651; SSD 0.635; Faster R-CNN 0.627; YOLO-V2 0.433; YOLO-V3 0.388. |
| [[Average precision]] | [[NEU-DET]] | Per-class AP | Higher is better | no | Proposed method AP: Cr 0.417, In 0.763, Pa 0.863, Ps 0.851, Rs 0.581, Sc 0.856. |
| [[Average precision]] | [[GC10-DET]] | Per-class AP | Higher is better | no | Proposed method AP: Pu 0.900, Wl 0.885, Cg 0.848, Ws 0.558, Os 0.622, Ss 0.650, In 0.256, Rp 0.364, Cr 0.521, Wf 0.919. |
| [[Recall]] | [[NEU-DET]] | Per-class recall | Higher is better | no | Proposed method recall: Cr 0.965, In 0.974, Pa 0.987, Ps 1.000, Rs 0.966, Sc 0.981. |
| [[Recall]] | [[GC10-DET]] | Per-class recall | Higher is better | no | Proposed method recall: Pu 0.965, Wl 0.967, Cg 0.969, Ws 0.739, Os 0.891, Ss 0.988, In 0.667, Rp 0.333, Cr 0.857, Wf 1.000. |
| [[Inference time]] | [[NEU-DET]] / [[GC10-DET]] | Runtime | Lower is better | no | Proposed method: 27 ms/image and 6 s/test set on NEU-DET; 33 ms/image and 8 s/test set on GC10-DET. |

## Limitations

- Some detector baselines outperform EDDN on individual defect-class AP values.
- The extracted text does not include a full license statement for GC10-DET.
- On GC10-DET, the proposed method has weak recall for rolled pit, 0.333, and weak AP for inclusion, 0.256.
- On NEU-DET, SSD ties the proposed method on mAP at 0.724 and has higher AP for inclusion and rolled-in scale.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]]
- Datasets: [[GC10-DET]], [[NEU-DET]]
- Methods: [[EDDN]], [[Single Shot MultiBox Detector]], [[Hard negative mining]], [[Data augmentation]]
- Metrics: [[Recall]], [[Average precision]], [[mAP]], [[Inference time]]
- Domains: [[Metal inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Shares task family | Both address industrial surface defect detection, but this paper contributes a metallic benchmark and detector while Schmedemann et al. focus on procedural synthetic training data. |

## Questions

- Should GC10-DET become a benchmark note distinct from the dataset note?
- What train/test split was used for GC10-DET in the paper?
