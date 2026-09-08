---
title: "Recall"
aliases:
  - "Sensitivity"
  - "True Positive Rate"
  - "TPR"
tags:
  - metric
  - classification
---

# Recall

## Definition

Recall measures the share of true positives that are detected. It is used for defect classification, segmentation, and textured surface inspection reporting.

## Direction

Higher is better.

## Used In These Papers

- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] reports recall for STDAN, including 94.88% on [[FD_Dataset|FD_Dataset]].

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] reports the false-positive burden required to reach 100% recall on [[KolektorSDD]].
- [[2020 - Surface Defect Saliency of Magnetic Tile]] reports recall for magnetic-tile surface-defect saliency on [[Magnetic Tile Defects]].
- [[2025 - You Only Look Once-Aluminum]] reports 77.8% recall for [[YOLO-AL]] on [[APDDD]].
- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] reports recall at IoU 0.25 and confidence 0.5 for [[OGD-DET benchmark]].

- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] reports recall for blowhole classification.
- [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] reports sensitivity/recall for NEU-CLS steel surface defect classification, including 95.33% mean sensitivity for DCGAN augmentation.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] reports [[RepVGG+SA]] at 93.92% macro-recall on [[X-SDD]].
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] reports validation recall for U-Net experiments.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] reports recall in classification augmentation experiments on [[EL-2019]].
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] reports recall for textured defect inspection.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] reports 93.3% recall for [[GBH-YOLOv5]] on [[PV-Multi-Defect]].

## Related Metrics

- [[Precision]]
- [[F1-score]]
- [[Specificity]]
- [[Classification metrics]]

- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] supports PCB defect detection, semi-supervised learning.
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] reports TPR as 97.988% at K value 8 for solar panel fault classification.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] reports median recall on [[BenchmarkELimages]], including 0.86 for cracks and 0.85 for gridline defects with DeepLabV3+ custom weights.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] reports image-level recall in a manufacturing simulation, improving from 85.33% with original annotations to 96.07% with Defect Spectrum annotations.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] emphasizes minority-class recall, including Donut recall improving from 83.45% to 89.35% with 4-head ViT augmentation and Scratch recall improving from 80.33% to 86.21% with 8-head augmentation.
