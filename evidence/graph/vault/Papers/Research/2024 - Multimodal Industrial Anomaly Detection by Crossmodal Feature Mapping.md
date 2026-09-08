---
title: "Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping"
aliases:
  - "Crossmodal Feature Mapping"
paper_key: "sha256:766f715c8dcd2b1981b7fd4577a6f228f3655cb09df5d15498cc7d327a657f6b"
paper_type: research
year: 2024
venue: "CVPR 2024"
authors:
  - "Alex Costanzino"
  - "Pierluigi Zama Ramirez"
  - "Giuseppe Lisanti"
  - "Luigi Di Stefano"
status: processed
processed_at: 2026-05-22
topics:
  - "multimodal anomaly detection"
  - "crossmodal mapping"
  - "RGB-D inspection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec3D]]"
methods:
  - "[[Crossmodal Feature Mapping]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "multimodal feature mapping"
  - "RGB-D anomaly detection"
metrics:
  - "[[AU-PRO]]"
  - "[[FPS]]"
primary_metric: "[[AU-PRO]]"
baselines:
  - "M3DM"
  - "BTF"
  - "AST"
code: "https://cvlab-unibo.github.io/CrossmodalFeatureMapping/"
data: "[[MVTec3D]]"
doi: "10.1109/CVPR52733.2024.01631"
arxiv: "not reported"
url: "https://doi.org/10.1109/CVPR52733.2024.01631"
pdf: "paper-inbox/10_processed/Research/2024 - Costanzino - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Costanzino - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Costanzino - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Costanzino - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.txt"
artifact_status: "processed"
tags:
  - "paper"
  - "multimodal-anomaly-detection"
  - "crossmodal-mapping"
---

# Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping

## Summary

- The paper proposes a lightweight multimodal anomaly detection framework that maps features from one modality to another on nominal samples.
- Anomalies are detected as inconsistencies between observed and mapped RGB/3D features.
- It reports state-of-the-art detection and segmentation performance on MVTec 3D-AD in standard and few-shot settings while using less memory and faster inference than prior multimodal methods.

## Contribution

- Claimed: memory-bank multimodal methods have high memory footprint and inference time.
- Claimed: crossmodal feature mapping captures RGB-3D consistency without storing large feature banks.
- Shown: experiments report strong performance-speed-memory trade-offs on MVTec 3D-AD.

## Method

- Feature extractors produce RGB and 3D features.
- Lightweight mapping networks learn to predict features across modalities on nominal training data.
- At inference, inconsistencies between observed and mapped features produce anomaly maps that are aggregated and smoothed.

## Evidence

- Benchmark: MVTec 3D-AD.
- The abstract reports state-of-the-art detection and segmentation performance in standard and few-shot settings.
- The paper explicitly evaluates inference speed and memory occupancy against multimodal baselines.

## Limitations

- Exact metric values are not visible in the extracted abstract region used for this note.
- The method assumes registered multimodal inputs so that crossmodal feature inconsistencies are meaningful.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Crossmodal Feature Mapping]], [[Unsupervised anomaly detection]]
- Datasets: [[MVTec3D]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-PRO]], [[FPS]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec3D]] | Shares dataset | The paper evaluates multimodal anomaly detection on MVTec 3D-AD. |
| [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] | Contrasts with | Crossmodal Feature Mapping targets the memory and speed costs of memory-bank multimodal methods such as M3DM. |
| [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] | Shares task | Both seek efficient RGB-depth anomaly detection on MVTec3D. |

## Questions

- How sensitive is feature mapping to RGB-depth calibration errors?
- Which layer-pruning choices retain the best performance-memory trade-off?
