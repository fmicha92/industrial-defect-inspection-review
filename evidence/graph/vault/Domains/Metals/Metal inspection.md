---
title: "Metal inspection"
tags:
  - domain
---

# Metal inspection

## Definition

Metal inspection covers visual, CT, and endoscopic inspection of metal parts and steel surfaces. The represented papers include public steel-strip defect datasets, casting and machined-part inspection, additive-manufacturing surface inspection, and synthetic or procedurally generated data where real labeled defects are scarce.

## Represented Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] introduces [[KolektorSDD]] for electrical commutator surface crack inspection and evaluates a segmentation-plus-decision detector.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] detects pores and cavities in cast aluminum CT scans.
- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] introduces the Northeastern University (NEU) surface defect database and evaluates noise-robust texture features for hot-rolled steel strip defect recognition.
- [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] generates synthetic steel surface defects and evaluates U-Net/Xception on real Severstal steel defect data.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] detects blowholes in turbocharger housing surfaces.
- [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] evaluates GAN-based augmentation for hot-rolled steel strip surface defect classification on [[NEU-CLS]].
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] introduces [[NEU-DET]] for hot-rolled steel strip surface defect detection and evaluates [[Defect Detection Network]].
- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] introduces [[NEU-SEG]] for pixel-wise hot-rolled steel strip surface defect segmentation and evaluates [[PGA-Net]].
- [[2020 - Surface Defect Saliency of Magnetic Tile]] introduces [[Magnetic Tile Defects]] and evaluates [[MCuePush U-Net]] for pixel-level magnetic-tile defect saliency.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] introduces [[X-SDD]] for seven-class hot-rolled steel strip surface defect classification.
- [[2023 - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing]] detects welds, surface pores, grooves, and slag inclusions in WAAM metallic surface imagery.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] evaluates [[Severstal Steel Defect Dataset]] as the steel-surface portion of a broader mixed-supervision surface-defect benchmark.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] introduces [[KolektorSDD2]] as a public metal surface-defect dataset with fine-grained masks and a fixed train/test split.
- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] evaluates PAR-CNN, NRMI feature selection, and SVM on [[Severstal Steel Defect Dataset]] for steel surface defect classification.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] benchmarks casting surface defect detection and segmentation on casting-like metal plate images.
- [[2025 - You Only Look Once-Aluminum]] evaluates [[YOLO-AL]] on [[APDDD]] for aluminum profile surface defect detection.
- [[2022 - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation]] evaluates an attention-augmented object detector on [[BSData]], [[NEU-DET]], and other industrial surface-defect datasets.
- [[2023 - Metal Surface Defect Detection Based on Improved YOLOv5]] evaluates an improved YOLOv5 detector on augmented [[GC10-DET]] metal surface defect images.
- [[2023 - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output]] uses [[BSData]] for defect classification with CAM-based localization.
- [[2024 - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution]] evaluates a YOLOv8n-derived detector on [[GC10-DET]] steel surface defects.
- [[2024 - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network]] evaluates FOHR Net on [[GC10-DET]] and [[APDDD]] metal surface defect detection.
- [[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]] evaluates semi-supervised defect segmentation on [[KolektorSDD]] and a steel dataset.
- [[2023 - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection]] evaluates latent diffusion anomaly detection on [[MPDD]].
- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]] evaluates [[GT-CutMix]] and SA-DSSD on [[X-SDD]] and [[NEU-DET]].
- [[2022 - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables]] evaluates pseudo-anomalous latent-variable generation on [[Magnetic Tile Defects]].
- [[2024 - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation]] evaluates DDIM augmentation and [[YOLO-DSC]] on [[NEU-DET]].
- [[2025 - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection]] evaluates [[DDPM-CSD]] synthetic data generation on [[NEU-CLS]].
- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] evaluates LoRA-adapted diffusion augmentation on [[NEU-SEG]].
- [[2026 - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks]] evaluates LoRA-adapted diffusion augmentation on [[Magnetic Tile Defects]].
- [[2024 - NHD-YOLO Improved YOLOv8 Using Optimized Neck and Head]] supports steel surface defect object detection on [[NEU-DET]] with small-object copy-paste augmentation.
- [[2023 - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT]] supports private synthetic image generation for industrial surface defect classification on [[NEU-CLS]].

## Related Datasets

### Public

- [[APDDD]]
- [[BSData]]
- [[CSDD]]
- [[GC10-DET]]
- [[HSS-IAD]]
- [[KolektorSDD]]
- [[KolektorSDD2]]
- [[LoHi-WELD]]
- [[Magnetic Tile Defects]]
- [[MPDD]]
- [[MPDD2]]
- [[NEU-CLS]]
- [[NEU-DET]]
- [[Tianchi aluminium profile surface defect dataset]]
- [[NEU-SEG]]
- [[MSDD]]
- [[Severstal Steel Defect Dataset]]
- [[X-SDD]]

### Availability Unspecified

- [[Baidu aluminium surface defect dataset]]
- [[Magnetic Particle Inspection Dataset]]
- [[Metal parts complex conditions dataset]]
- [[Synthetic steel defect dataset]]
- [[WAAM metallic surface defect dataset]]

## Related Concepts

- [[Industrial visual inspection]]
- [[Defect segmentation]]
- [[Nondestructive testing]]
- [[Simulation-based data augmentation]]
- [[Procedural generation]]
- [[Casting surface defect detection]]
- [[CSDD]]

## Used In These Papers

- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] constructs [[NEU-CLS]] for hot-rolled steel strip defect recognition and evaluates [[Adjacent evaluation completed local binary patterns]].
- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] introduces [[BSData]] for pitting classification, segmentation, and wear forecasting on ball-screw-drive metal surfaces.
- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] evaluates a transformer-enhanced YOLOv5 detector on NEU-DET steel surface defects.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] evaluates real-time defect segmentation on [[NEU-SEG]], a hot-rolled steel strip segmentation dataset introduced by the PGA-Net paper.
- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] introduces [[NEU-SEG]] from the NEU surface defect database and reports 82.15% [[mIoU]] on that dataset.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] introduces [[NEU-DET]] and reports DDN + ResNet50 at 82.3 mAP on the benchmark.
- [[2020 - Surface Defect Saliency of Magnetic Tile]] introduces [[Magnetic Tile Defects]] for pixel-level magnetic-tile surface-defect saliency and localization.
- [[2025 - You Only Look Once-Aluminum]] describes [[APDDD]] as a 3719-image aluminum profile surface defect dataset and reports [[YOLO-AL]] at 81.5% [[mAP@0.50]].
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates [[IDD-Net]] on NEU steel defects and the [[Baidu aluminium surface defect dataset]].


- [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] supports metal part defect detection, complex industrial conditions.
- [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] supports metal-parts fabrication anomaly detection with four classes and normal-only training.
- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] supports weld defect detection, dataset.

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.
- [[2023 - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing]] supports online metallic surface defect detection for wire-and-arc additive manufacturing.

- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] supports steel surface defect detection, YOLOv5.
- [[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]] supports strip steel surface defect classification on [[NEU-CLS]] with synthetic image generation.
- [[2023 - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2]] supports steel surface defect classification on [[NEU-CLS]] with EDCGAN data augmentation.
- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] introduces [[MSDD]] for photometric-stereo-based casting metal surface defect detection on non-planar parts.
- [[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]] introduces [[HSS-IAD]], a public metallic-like industrial anomaly detection dataset with 8,580 images and precise anomaly annotations.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] introduces [[KolektorSDD2]] with 3335 color production-item images and fine-grained segmentation masks for metal surface-defect evaluation.
- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] introduces [[KolektorSDD]] as a public electrical commutator surface-defect dataset with pixel-wise masks.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] introduces [[X-SDD]] with 1,360 hot-rolled steel strip defect images and reports [[RepVGG+SA]] at 95.10% [[Accuracy]].
- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] supports steel surface inspection with binary and multi-class classification experiments on [[Severstal Steel Defect Dataset]].
- [[2022 - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation]] supports industrial surface defect object detection with [[BSData]] and [[NEU-DET]] evaluation.
- [[2023 - Metal Surface Defect Detection Based on Improved YOLOv5]] supports metal surface object detection on augmented [[GC10-DET]].
- [[2023 - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output]] supports classification-based localization on [[BSData]].
- [[2024 - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution]] supports steel surface object detection on [[GC10-DET]].
- [[2024 - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network]] supports real-time metal surface object detection on [[GC10-DET]] and [[APDDD]].
- [[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]] supports semi-supervised industrial defect segmentation on [[KolektorSDD]].
