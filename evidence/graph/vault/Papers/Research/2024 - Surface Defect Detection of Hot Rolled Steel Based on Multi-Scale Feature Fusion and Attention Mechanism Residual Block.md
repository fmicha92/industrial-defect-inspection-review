---
title: "Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block"
aliases:
  - "Improved YOLOv5s with MSF and CRA block"
paper_key: "doi:10.1038/s41598-024-57990-3)/author(hongkai"
paper_type: research
year: 2024
venue: "Scientific Reports"
authors:
  - "Hongkai Zhang"
  - "Suqiang Li"
  - "Qiqi Miao"
  - "Ruidi Fang"
  - "Song Xue"
  - "Qianchuan Hu"
  - "Jie Hu"
  - "Sixian Chan"
status: processed
processed_at: 2026-05-22
topics:
  - "steel surface defect detection"
  - "object detection"
  - "multi-scale feature fusion"
tasks:
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-DET]]"
  - "[[GC10-DET]]"
  - "[[APDDD]]"
methods:
  - "[[YOLOv5]]"
  - "[[Multi-scale feature fusion and CRA block]]"
model_family:
  - "YOLOv5"
  - "convolutional neural network"
metrics:
  - "[[mAP]]"
  - "[[FPS]]"
  - "[[GFLOPs]]"
  - "[[Average precision]]"
primary_metric: "[[mAP]]"
baselines:
  - "YOLOv5s"
  - "Faster R-CNN"
  - "SSD"
  - "RetinaNet"
  - "YOLOv3"
code: "not reported"
data: "[[NEU-DET]], [[GC10-DET]], APDDD"
doi: "10.1038/s41598-024-57990-3"
arxiv: "not applicable"
url: "https://doi.org/10.1038/s41598-024-57990-3"
pdf: "paper-inbox/10_processed/Research/2024 - Zhang - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Zhang - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Zhang - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Zhang - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block.txt"
artifact_status: "processed"
tags:
  - "paper"
  - "steel-surface-defect-detection"
  - "object-detection"
---

# Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block

## Summary

- The paper improves YOLOv5s for hot-rolled steel strip defect detection with multi-scale feature fusion and an attention-based residual block.
- The method is designed for small defects, overlapping defects, and fine-grained localization.
- It reports mAP of 78.5% on NEU-DET, 67.3% on GC10-DET, and 59.2% on APDDD.

## Contribution

- Claimed: multi-scale feature fusion combines shallow detail with deeper semantic features for steel strip defect localization.
- Claimed: the CRA block adds attention, residual, and skip connections to reduce defect information loss.
- Shown: the improved model reports +4.9 mAP over baseline on NEU-DET and +2.1 mAP on GC10-DET.

## Method

- The baseline is YOLOv5s.
- The MSF strategy fuses feature maps from different levels to preserve resolution and semantic information.
- The CRA block uses attention with residual connections to improve fine-grained defect feature extraction.

## Evidence

- NEU-DET mAP: 78.5%.
- GC10-DET mAP: 67.3%.
- APDDD mAP: 59.2%.
- The paper evaluates AP, mAP, GFLOPs, and FPS.

## Limitations

- The paper focuses on steel strip surface datasets; transfer to other material domains is only partially tested through APDDD.
- The exact code release status is not reported in the extracted source.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]]
- Methods: [[YOLOv5]], [[Multi-scale feature fusion and CRA block]]
- Datasets: [[NEU-DET]], [[GC10-DET]], [[APDDD]]
- Domains: [[Metal inspection]]
- Metrics: [[mAP]], [[FPS]], [[GFLOPs]], [[Average precision]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[NEU-DET]] | Shares dataset | The paper reports its main steel defect detection comparison on NEU-DET. |
| [[GC10-DET]] | Shares dataset | The paper uses GC10-DET as a second steel strip defect benchmark. |
| [[YOLOv5]] | Shares method | The architecture is an improved YOLOv5s detector. |
| [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] | Shares task | Both improve YOLO-style detectors for NEU-DET steel surface defect detection. |

## Questions

- Are the APDDD annotations and splits public and directly comparable with NEU-DET and GC10-DET?
- How much latency is added by the CRA block in production settings?
