---
title: "Defect classification"
tags:
  - concept
  - task
---

# Defect classification

## Definition

Defect classification assigns an inspection image or detected region to a defect-related class. It appears in surface inspection, construction defect inspection, fiber placement inspection, and turbocharger housing blowhole detection.

## Why It Matters

Classification is often easier to label than segmentation and is a common first target for synthetic data augmentation. It may be insufficient when the inspection workflow needs precise defect location or size.

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] classifies [[KolektorSDD]] images as defect-present or defect-absent using a [[Segmentation-decision network]].
- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] evaluates six-class hot-rolled steel strip surface defect recognition on [[NEU-CLS]] using AECLBP, LBP, LTP, and CLBP descriptors.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] introduces [[X-SDD]] for seven-class hot-rolled steel strip surface defect classification and reports [[RepVGG+SA]] at 95.10% accuracy.
- [[2022 - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks]] classifies wafer dicing chips and streets as flawless or faulty.
- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] provides a pitting/no-pitting classification release in [[BSData]].










- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] supports electroluminescence images, deep feature representations.
- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]] supports fabric inspection, public benchmark.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] evaluates limited-data defect recognition with Con-GAN augmentation.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] supports photovoltaic cell defects, electroluminescence images.
- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] supports edge computing, surface defect detection.
- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] supports weld defect detection, dataset.
- [[2022 - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks]] supports semiconductor manufacturing, visual fault inspection.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] classifies Severstal steel surface images into binary defect/no-defect and five defect classes with PAR-CNN, NRMI, and SVM.
- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] evaluates whether synthesized defects improve ResNet34 and DenseNet121 classification accuracy.
- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] evaluates generated AFP defect images with GAN-Train GAN-Test.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] evaluates defective versus defect-free classification for turbocharger housing images.
- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] evaluates OK/nOK classification for gearbox component image patches.
- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] describes misalignment and material anomalies as better suited to image classification than object detection.
- [[ELPV Dataset]] annotates solar-cell electroluminescence images with defect probabilities and module type for defective-cell identification.
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] classifies solar panel images into clean, dusty, bird-drop, electrical-damage, physical-damage, and snow-covered classes.
- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] evaluates CNN classification of the same six RGB PV panel condition classes and audits explanation faithfulness.
- [[2025 - AI-driven fabric classification]] documents the recording process for [[DME Fabric Defect Detection Dataset]] and evaluates PSRT50 on image-level fabric classification experiments.
- [[2011 - Non-parametric Texture Defect Detection Using Weibull Features]] classifies DAGM2007 texture images as defective or non-defective from maximum patch distance in Weibull feature space.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]] reports image classification as the most common reviewed surface-defect problem type, appearing in 49.15% of final studies.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reviews supervised CNN classification for AOI and contrasts image-level labels with pixel-level localization needs.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reviews classification-oriented defect detection methods across surface images and X-ray images.

## Related Concepts

- [[Surface defect detection]]
- [[Defect segmentation]]
- [[Synthetic data generation]]
- [[Distribution shift]]
- [[ELPV Dataset]]
- [[DME Fabric Defect Detection Dataset]]
- [[FD_Dataset]]
- [[MVEP]]
- [[PV Panel Defect Dataset]]
- [[IncepViTH-Net]]
- [[Shortcut learning]]
- [[BSData]]
- [[NEU-CLS]]
- [[X-SDD]]
- [[Adjacent evaluation completed local binary patterns]]
