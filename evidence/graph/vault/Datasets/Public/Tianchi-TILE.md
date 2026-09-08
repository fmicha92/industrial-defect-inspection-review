---
title: "Tianchi-TILE"
aliases:
  - "Aliyun Tianchi ceramic tile defect detection dataset"
related_domain: "[[Multi-industry anomaly detection]]"
url: "not reported"
data_sources: "Aliyun Tianchi ceramic tile defect detection dataset"
introduced_by: "not reported"
---
# Tianchi-TILE

## Definition

Tianchi-TILE is a ceramic tile defect detection dataset used by the ALADA paper to evaluate automatic data augmentation for industrial object detection.

## Dataset Details

- The ALADA source reports 3,613 high-resolution defect images.
- Covered defect types include edge anomalies, corner anomalies, white dots, light blocks, dark spots, aperture defects, marker defects, and scratches.
- ALADA resizes images to 1500 x 1500 before detector training.
- The paper uses VOC-format bounding-box annotations and a 7:3 train/test split.

## Used In These Papers

- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] evaluates ALADA on Tianchi-TILE with FRCNN and RetinaNet and reports 54.74 mAP and 55.85 mAP, respectively.

## Source Anchors

- Hosting source: not reported.
- Introducing paper: not reported.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Surface defect detection]]
- [[Object detection]]
