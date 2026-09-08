---
title: "Average precision"
aliases:
  - "AP"
tags:
  - metric
  - detection
---

# Average Precision

## Definition

Average precision is used in the processed detection papers as a per-class detection metric.

## Direction

Higher is better.

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] uses average precision as the primary metric on [[KolektorSDD]] and reports 99.9% AP for the best [[Segmentation-decision network]].
- [[2025 - You Only Look Once-Aluminum]] uses average precision through mAP metrics for aluminum profile surface defect detection on [[APDDD]].

- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] reports per-class AP@0.50 for discontinuity and excess adhesive defects; holdout excess AP improves from 0.2829 real-only to 0.5864 with GAN augmentation.
- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] supports industrial visual inspection, automotive assembly.
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] reports AP by defect category and mAP across categories.
- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] reports average precision-style detection results through mAP.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] reports AP for scratches, spots, and rusts on [[CSDD benchmark]].
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] reports AP, AP75, and object-size AP for CNN and Transformer detectors on [[SSGD benchmark]].
- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] reports AP50:5:95, AP50, and AP75 for [[PVEL-AD benchmark]] detector evaluation.
- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] reports AP@0.25, AP@0.50, and AP@0.75 for [[OGD-DET benchmark]].
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] reports AP@0.7 IoU for KITTI vehicle detection.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] defines AP for NEU-DET detector evaluation and averages it into mAP across defect classes.

## Related Concepts

- [[mAP]]
- [[AP@0.7 IoU]]
- [[Detection metrics]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] reports AP for multi-class anomaly detection/localization, including 99.0 AP-cls and 52.6 AP-seg on MVTec AD.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] reports downstream AP of 81.4 for pixel-level anomaly localization and 99.7 for image-level anomaly detection using generated MVTec AD data.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] reports downstream AP-P 86.1 for pixel-level localization and AP-I 99.8 for image-level detection using generated MVTec AD data.
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] uses APpixel as the key segmentation precision metric for pseudo-anomaly insertion schemes and reports [[Affine anomaly insertion]] at 65.5% on MVTec AD and 44.1% on VisA.
