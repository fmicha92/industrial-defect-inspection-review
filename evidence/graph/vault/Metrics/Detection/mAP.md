---
title: "mAP"
aliases:
  - "mean average precision"
tags:
  - metric
  - detection
---

# mAP

## Definition

mAP is mean average precision, used in the paper notes as a detection metric summarizing average precision across defect classes.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] reports mAP-style metrics for [[YOLO-AL]] on [[APDDD]], including 81.5% [[mAP@0.50]].




- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] supports edge computing, surface defect detection.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] reports mAP@.5:.95 for YOLO-v5 and YOLO-v8 on SAPF and NEU-CLS with real and generated defect images.
- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] supports PCB component inspection, generative augmentation.
- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] supports weld defect detection, dataset.
- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] reports mAP-style COCO metrics for [[Co-DETR]] and [[YOLOv6-L6]] on [[DsPCBSD+]].
- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] reports mAP for one-class fabric anomaly detection on [[Lusitano]].
- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] reports 98.6% mAP at 62 FPS on DeepPCB.
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] uses AP and mAP for metallic surface defect detection evaluation.
- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] uses mAP as the primary metric for automatic augmentation on Tianchi-TILE, GC10-DET, and NEU-DET.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] uses mAP as the primary detection metric for [[CSDD benchmark]].
- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] uses mAP50 to validate object detectors on [[MSDD]].
- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] reports YOLOv5-l at 51.13% mAP50:5:95 on [[PVEL-AD benchmark]].
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] reports mAP at 0.5 IoU for Mask R-CNN trained with synthetic and GAN-refined industrial object images.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] reports 97.8% mAP for [[GBH-YOLOv5]] on [[PV-Multi-Defect]].

## Related Concepts

- [[Average precision]]
- [[AP@0.7 IoU]]
- [[PCB defect detection]]
- [[Metallic surface defect detection]]
- [[CSDD benchmark]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.

- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] supports steel surface defect detection, YOLOv5.

- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] reports DeepPCB mAP for YOLOv5 + DE-SSD, including 98.4% with 50 labeled samples and 98.7% with 1,000 labeled samples.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] reports DDN + ResNet50 at 82.3 mAP on [[NEU-DET]].
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reports mAP examples for object-detection AOI studies, including wheel hub, steel strip, WAAM, and PCB defect detection.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reports reviewed mAP examples for PCB, solar cell, aluminum-profile, and X-ray casting defect detection methods.
