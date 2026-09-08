---
title: "Multi-industry anomaly detection"
tags:
  - domain
---

# Multi-industry anomaly detection

## Definition

Multi-industry anomaly detection covers methods and benchmarks intended to generalize across multiple industrial objects, textures, or product categories rather than one manufacturing use case. In the current vault, this is mainly represented by MVTec-style anomaly benchmarks and unsupervised localization methods.

## Represented Papers

- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] evaluates sparse, anonymized manufacturing failure prediction on [[Bosch Production Line Performance]].
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] evaluates on MVTec AD, DAGM, RSDDs, and printed product surfaces.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] evaluates on MVTec2D, MVTec3D, and automotive plastic parts.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] introduces a multi-source semantic defect benchmark with refined masks, multi-defect labels, captions, and synthetic defect generation.

## Related Datasets

### Public

- [[Bosch Production Line Performance]]
- [[Bosch Surface Defect Inspection Dataset]]
- [[BTAD]]
- [[Bottle-Cap Dataset]]
- [[DAGM2007]]
- [[Defect Spectrum]]
- [[Industrial-5i]]
- [[MVTec AD]]
- [[MVTec AD 2]]
- [[MVTec Caption]]
- [[MVTec LOCO AD]]
- [[MVTec3D]]
- [[Real-IAD]]
- [[VisA]]
- [[Workpiece surface defect dataset]]

### Availability Unspecified

- [[Automotive plastic parts dataset]]
- [[Commutator Cylinder Surface Defect Dataset]]
- [[CrackForestDataset]]
- [[DAGM]]
- [[Fabric Dataset]]
- [[Hand-labeled real CT defect scans]]
- [[Industrial defect detection augmentation datasets]]
- [[Metal Hook Defect Dataset]]
- [[Metal Iron Sheet Dataset]]
- [[Metal Phone Band Dataset]]
- [[O-ring Dataset]]
- [[Piston Dataset]]
- [[Printed product surface dataset]]
- [[RSDDs]]
- [[Real-IAD D3]]
- [[Real-world endoscopic defect image test dataset]]
- [[Real-world endoscopic defect image training dataset]]
- [[Simulated CT defect scans]]
- [[Six public industrial image datasets]]
- [[Surface defect limited-data benchmark datasets]]
- [[Synthetic turbocharger housing defect dataset]]
- [[Eyecandies]]

## Related Concepts

- [[MVTec AD]]
- [[MVTec3D]]
- [[Unsupervised anomaly detection]]
- [[Unsupervised anomaly localization]]
- [[Manufacturing failure prediction]]
- [[Smart manufacturing]]
- [[Surface defect detection]]

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] evaluates CutPaste self-supervised anomaly detection and localization across the multi-category MVTec AD benchmark.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] evaluates attention-conditioned synthetic anomaly fine-tuning across MVTec AD object and texture categories.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] evaluates SACD on MVTec AD and BTAD multi-category industrial anomaly benchmarks.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] evaluates RGBD anomaly fusion on MVTec AD, VisA, and a RealSense D435i industrial dataset.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] evaluates selective anomaly simulation across MVTec AD product and texture categories.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] evaluates realistic synthetic anomaly training across MVTec AD categories.
- [[2023 - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples]] evaluates patch-based synthetic anomaly simulation on MVTec AD and BTAD.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] evaluates PatchAnomaly on MVTec AD and BTAD.
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] compares pseudo anomaly insertion schemes on MVTec AD, VisA, and KolektorSDD2.
- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] evaluates a two-stage contrastive anomaly detector on MVTec AD, VisA, and BTAD.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] evaluates image-mask aligned diffusion synthesis on MVTec AD and Real-IAD.

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] introduces [[Industrial-5i]] for few-shot defect segmentation across multiple industrial product categories.










- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] supports automatic data augmentation, industrial defect detection.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] supports edge computing, surface defect detection.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] covers 30 industrial object classes across metal, plastic, wood, ceramics, and mixed materials, making Real-IAD a multi-industry anomaly benchmark.
- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] supports self-supervised pre-training, industrial anomaly dataset.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] supports 3D anomaly detection, industrial visual inspection.
- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] supports multi-category MVTec AD anomaly localization with normal-only training and pseudo-abnormal local augmentation.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] supports manufacturing failure prediction, sparse production-line tabular data.

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, frequency decoupling.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.
- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] evaluates 3DSR on [[MVTec3D]] and [[Eyecandies]] for multi-object RGB+3D anomaly detection.

- [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] supports multimodal anomaly detection, crossmodal mapping.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] evaluates GLASS on MVTec AD, VisA, MPDD, and WFDD for multi-dataset industrial anomaly detection.
- [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] evaluates normal-only synthetic anomaly localization on MVTec AD.
- [[2022 - Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures]] evaluates mask-guided industrial defect synthesis on multiple MVTec AD items and phone-band imagery.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates one detector across steel, aluminium, PCB, and glass-bottle production data.
