---
title: "F1-score"
aliases:
  - "F1-measure"
  - "F1 measure"
tags:
  - metric
  - classification
---

# F1-score

## Definition

F1-score combines precision and recall into a single harmonic-mean style score. The current vault evidence uses the paper's reported F1-measure name.

## Direction

Higher is better.

## Used In These Papers

- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] reports F1-score for EL solar-cell classification, including 98.14% binary F1 and 95.25% multiclass F1 for the augmented hybrid feature model.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] reports F1-score for STDAN, including 95.39% on [[FD_Dataset|FD_Dataset]].











- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] supports electroluminescence images, deep feature representations.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] supports photovoltaic cell defects, electroluminescence images.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] supports wafer map defect classification, class imbalance.
- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] supports mixed-type wafer defects, deformable convolution.
- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] supports weld defect detection, dataset.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] supports class imbalance, wafer map defect classification.
- [[2022 - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks]] supports semiconductor manufacturing, visual fault inspection.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] defines pixel-level, region-level, and sample-level F1-style metrics for fabric defect benchmark evaluation.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] reports F1-score alongside accuracy for limited-data defect recognition.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] reports [[RepVGG+SA]] at 93.25% macro-F1 on [[X-SDD]].
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] reports downstream F1-P 80.6 for pixel-level localization and F1-I 98.7 for image-level detection using generated MVTec AD data.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] reports F1-measure for textured surface defect inspection.
- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] reports mean F1-Score across S1-S4 gearbox component split protocols.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] reports F1-score for solar-cell defect segmentation, with LMFF reaching 81.3%, 67.5%, and 96.2% on SolarCells, SolarCells-S, and PVEL-S.
- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports ResNet50 as the best tested classifier with 0.825 macro-F1.
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] reports F1max for anomaly detection/localization, including 96.5 F1max-cls and 55.5 F1max-seg on multi-class MVTec AD.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] reports F1-max of 76.3 for pixel-level localization and 98.7 for image-level detection using generated anomaly data.
- [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]] reports class-level F1-score for YOLOv10x solar-cell defect detection on [[EL Solar Cells Dataset]].

## Related Metrics

- [[Precision]]
- [[Recall]]
- [[Classification metrics]]
- [[Gearbox component distribution-shift inspection benchmark]]
