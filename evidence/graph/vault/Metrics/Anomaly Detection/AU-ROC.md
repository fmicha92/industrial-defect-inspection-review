---
title: "AU-ROC"
aliases:
  - "AUC ROC"
  - "AUROC"
  - "AUC-ROC"
tags:
  - metric
  - anomaly-detection
---

# AU-ROC

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] reports 95.2 image-level AUROC for CutPaste 3-way and 96.0 pixel-wise localization AUROC on MVTec AD.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] reports 98.3 image-level AUROC and 98.2 pixel-wise AUROC on MVTec AD.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] reports 99.3 image-level AUROC and 98.3 pixel-level AUROC on MVTec AD.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] reports 99.6 image-level AUROC and 99.0 pixel-level AUROC on MVTec AD, plus 99.0 pixel-level AUROC on VisA.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] reports 98.3 detection AUROC and 98.0 localization AUROC on MVTec AD.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] reports 99.70 image-level AUROC on MVTec AD.

- [[2020 - Surface Defect Saliency of Magnetic Tile]] reports ROC/AUC evaluation for magnetic-tile surface-defect saliency on [[Magnetic Tile Defects]].
- [[2016 - Predict Failures in Production Lines A Two-stage Approach with Clustering and Supervised Learning]] uses AUROC as an additional robustness metric for the imbalanced Bosch failure-prediction classifiers and reports total AUROC 0.692.

## Definition

AU-ROC measures area under the receiver operating characteristic curve. It is used for anomaly detection and textured defect inspection evaluation.

## Direction

Higher is better.

## Used In These Papers

- [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] reports image-level and pixel-level AUROC for MPDD anomaly detection methods, with CFLOW-AD averaging 86.12 image-level AUROC and 97.72 pixel-level AUROC.











- [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]] uses anomaly-detection evaluation context.
- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] supports industrial visual inspection, automotive assembly.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] reports image-level AUROC for a four-class metal-parts anomaly benchmark; CutPaste has the best average at 86.55%, NSA is second at 74.72%, and FastFlow is the best pretrained-feature method at 73.29%.
- [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] supports metal part defect detection, complex industrial conditions.
- [[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]] supports heterogeneous same-sort anomaly detection, dataset.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] reports I-AUROC and S-AUROC for Real-IAD; mean I-AUROC is 87.6 on single-view Real-IAD and 85.0 on multi-view Real-IAD.
- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] reports AU-ROC with AU-PR but warns that AU-ROC can give an inflated view of performance on imbalanced anomaly detection and segmentation tasks.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] describes AU-ROC as the sample-level anomaly-classification metric for MVTec3D.
- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] reports AUC/AU-ROC for [[DBFAD]] and [[RD4AD]] on [[Lusitano]].
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] uses AUC ROC as the primary metric.
- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] reports AU-ROC at image level for anomaly detection and pixel level for localization, including 99.4 image-level and 98.5 pixel-level AUC on MVTec AD.
- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] reports pixel-wise AUROC on MVTec AD, including 89.4% for wood, 95.5% for zipper, and a dynamic-local-augmentation ablation of 93.04 versus 82.92 for static local augmentation.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] reports AU-ROC alongside AU-PRO.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] reports ROC AUC for STDAN, including 97% overall and 97.56% on [[FD_Dataset|FD_Dataset]].
- [[2011 - Non-parametric Texture Defect Detection Using Weibull Features]] reports AUC values of 0.96, 0.99, 0.99, and 0.99 on four [[DAGM2007]] texture classes.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reports AUROC/AUC examples from reviewed industrial defect methods, including PatchCore over 99% AUROC on MVTec and 0.873 AUC on a tire X-ray dataset.

## Related Metrics

- [[AU-PRO]]
- [[Anomaly detection metrics]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, frequency decoupling.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] reports DiAD at 97.2 AUROC-cls and 96.8 AUROC-seg on multi-class MVTec AD, plus 86.8 AUROC-cls and 96.0 AUROC-seg on VisA.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] reports image-level and pixel-level AUROC for GLASS, including 99.9/99.3 on MVTec AD and 99.6/99.4 on MPDD for GLASS-j.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] reports downstream U-Net localization at 99.1 pixel-level AUROC and image-level detection at 99.2 AUROC on MVTec AD using generated data.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] reports downstream U-Net localization AUC-P 99.3 and image-level detection AUC-I 99.2 on MVTec AD using generated data.
- [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]] reports image-level and pixel-level AUC-ROC, including 0.978/0.982 on [[MVTec AD]] and 0.956/0.979 on [[Bottle-Cap Dataset]].
- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] reports AUROC for image-wise and pixel-wise anomaly evaluation, including 99.7% detection AUROC and 98.8% localization AUROC on [[MVTec AD]].
