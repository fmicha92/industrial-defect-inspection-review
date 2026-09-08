---
title: "YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry: A Review of YOLOv1 to YOLOv11"
aliases:
  - "YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry"
paper_key: "sha256:4587be58fa4ab25c895bae2358cc588e626b1cab9597fae65c2b42d69d4ea013"
paper_type: review
year: 2025
venue: "Sensors"
authors:
  - "Makara Mao"
  - "Min Hong"
status: processed
processed_at: 2026-05-31
topics:
  - "YOLO fabric defect detection"
  - "real-time textile inspection"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
methods:
  - "[[YOLOv5]]"
  - "[[YOLOv10]]"
  - "[[YOLOv11]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[mAP]]"
  - "[[FPS]]"
primary_metric: "not applicable"
doi: "10.3390/s25072270"
url: "https://doi.org/10.3390/s25072270"
pdf: "paper-inbox/10_processed/Review/2025 - Mao - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry.pdf"
related_methods:
  - "[[YOLOv5]]"
  - "[[YOLOv10]]"
  - "[[YOLOv11]]"
  - "[[Data augmentation]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Review/2025 - Mao - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Mao - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Mao - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry.txt"
artifact_status: "review"
tags:
  - paper
---

# YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry: A Review of YOLOv1 to YOLOv11

## Summary

This review compares YOLO versions from YOLOv1 to YOLOv11 for real-time fabric defect inspection. It does not introduce a new dataset or experiment, but it highlights dataset limitations, domain generalization, and synthetic data generation as future directions for fabric defect detection.

## Paper Type

- Type: review.
- Why: It reviews YOLO architectures and their implications for textile inspection.

## Review / Survey Details

- Scope: YOLO object detection models for real-time textile/fabric defect inspection.
- Taxonomy: YOLO version evolution, architecture changes, fabric applications, real-time constraints, and industrial adoption challenges.
- Dataset relevance: the review emphasizes lack of standardized datasets and limited dataset diversity for textile inspection.
- Synthesis relevance: synthetic data generation is proposed as a future solution to dataset limitations and domain generalization.

## Methodological Patterns

- YOLO-based fabric inspection prioritizes speed, localization, and deployment feasibility.
- Mosaic and other YOLO training augmentations are discussed as part of model evolution.
- The review frames synthetic data generation, federated learning, and edge AI as future paths.

## Limitations

- Stated: dataset limitations, domain generalization, and computational constraints remain key barriers.
- Inferred: it is a good orientation source for detector choice, not evidence that synthetic textile data improves a specific public dataset.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Datasets: fabric defect datasets discussed as a limitation; no new benchmark is introduced
- Methods: [[YOLOv5]], [[YOLOv10]], [[YOLOv11]], [[Data augmentation]], [[Synthetic data generation]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[mAP]], [[FPS]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Data Augmentation Method for Fabric Defect Detection]] | Follow-up reading | A primary fabric detection study using GAN/geometric augmentation with Faster R-CNN rather than YOLO. |
| [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] | Shares domain | A broader 2025 textile defect detection review with dataset tables. |

## Questions

- Which YOLO fabric-defect papers in the review use public datasets such as ZJU-Leaper or AITEX?
