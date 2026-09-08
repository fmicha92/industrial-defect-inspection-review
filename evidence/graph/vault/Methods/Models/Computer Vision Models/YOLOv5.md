---
title: "YOLOv5"
aliases:
  - "YOLO v5"
tags:
  - method
  - model
  - object-detection
---

# YOLOv5

## Definition

YOLOv5 is an object detection model used as a baseline and base architecture in the processed CSDD paper. The paper describes it as consisting of a feature extraction network and detection network, with faster detection speed than several other object detection models.

## Why It Matters

YOLOv5 provides the base detector for [[YOLOv5 with global attention and partial convolution]], which improves CSDD detection mAP in the processed paper.

## Used In These Papers

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] evaluates YOLOv5 on [[CSDD]] and uses it as the base model for the proposed detector.
- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] compares against YOLOv5 on [[OGD-DET benchmark]].
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] benchmarks YOLOv5-m on [[SSGD]] and reports the highest Part II AP and fastest FPS among the listed Table 1 detectors.
- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] uses YOLOv5 for [[F-labelImg]] annotation and benchmarks YOLOv5 variants on [[PVEL-AD]].
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] uses YOLOv5 as the base detector for [[YOLOv5_zc]] in mobile phone flat-glass defect detection.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] uses YOLOv5s as the base detector for [[GBH-YOLOv5]] on [[PV-Multi-Defect]].
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses YOLOv5s as the ablation baseline and replaces the backbone, feature aggregation neck, multi-scale fusion, and localization loss to form [[IDD-Net]].
- [[2024 - Defect detection in textile manufacturing Improving findings using YOLOv5 versions]] compares YOLOv5s and YOLOv5x on AITEX-derived textile defect detection with transfer learning, rebalanced data, and native augmentation.

## Related Concepts

- [[YOLOv5 with global attention and partial convolution]]
- [[Casting surface defect detection]]
- [[Average precision]]
- [[mAP]]
- [[Deep convolutional neural network]]
- [[PVEL-AD benchmark]]
- [[YOLOv5_zc]]
- [[GBH-YOLOv5]]
- [[IDD-Net]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.

- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] supports steel surface defect detection, YOLOv5.
