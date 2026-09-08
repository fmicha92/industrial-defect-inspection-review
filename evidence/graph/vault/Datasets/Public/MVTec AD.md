---
title: "MVTec AD"
aliases:
  - "MVTec2D"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://www.mvtec.com/research-teaching/datasets/mvtec-ad"
data_sources: "MVTec"
introduced_by: "[[2021 - The MVTec Anomaly Detection Dataset]]"
related_papers:
  - "[[2021 - The MVTec Anomaly Detection Dataset]]"
availability: "public"
access: "downloadable from MVTec research dataset page"
licenses:
  - "CC BY-NC-SA 4.0"
---
# MVTec AD

## Definition

MVTec AD is a public industrial anomaly detection and localization benchmark with 5354 high-resolution color images across 15 texture and object categories. It uses defect-free training images and test images containing both normal samples and manually generated real-world-like defects with pixel-precise anomaly annotations.

## Why It Matters

It is a recurring comparison point for unsupervised visual inspection methods. The introducing paper uses it to compare reconstruction-based, pretrained-descriptor, and classical anomaly segmentation methods, and later papers reuse it as a standard industrial anomaly-localization benchmark.

## Dataset Details

- Total images: 5354.
- Categories: 5 textures and 10 objects.
- Splits: 3629 training images, 467 good test images, and 1258 defective test images.
- Defects: 73 defect groups and 1888 annotated anomalous regions.
- Image sizes: 700 x 700 to 1024 x 1024 pixels after cropping.
- Grayscale categories: grid, screw, and zipper.
- Annotation: pixel-precise ground truth for all anomalous regions.
- Evaluation: [[AU-ROC]], [[AU-PRO]], [[IoU]], and precision-recall based metrics.
- Availability: public download from https://www.mvtec.com/research-teaching/datasets/mvtec-ad.
- License: CC BY-NC-SA 4.0; commercial use is not allowed under the MVTec terms.

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] trains self-supervised CutPaste representations on MVTec AD and reports 95.2 image AUROC with the 3-way CutPaste objective.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] uses MVTec AD for attention-conditioned synthetic anomaly fine-tuning and reports 98.3 image AUROC / 98.2 pixel AUROC.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] evaluates SACD on MVTec AD with Simplex-noise pseudo-anomalies, reporting 99.3 image AUROC, 98.3 pixel AUROC, and 94.8 PRO.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] evaluates RGBD anomaly fusion on MVTec AD using estimated depth and attention-guided synthetic perturbations, reporting 99.6 image AUROC and 99.0 pixel AUROC.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] evaluates selective anomaly simulation on MVTec AD and reports 98.0 localization AUROC / 70.9 AP for the full method.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] uses MVTec AD for realistic synthetic anomaly training and reports 99.70 image AUROC in the final model.


- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses selected MVTec AD product categories as source material for [[Industrial-5i]].
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] supports self-supervised pre-training, industrial anomaly dataset.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] evaluates FMR-Net on MVTec AD texture categories.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] evaluates CDO on MVTec2D.
- [[2021 - The MVTec Anomaly Detection Dataset]] introduces MVTec AD and reports student-teacher anomaly detection as the strongest mean benchmark method among the evaluated baselines.

## Source Anchors

- Hosting source: https://www.mvtec.com/research-teaching/datasets/mvtec-ad.
- Introducing paper: [[2021 - The MVTec Anomaly Detection Dataset]].
- Access terms: CC BY-NC-SA 4.0, noncommercial.

## Related Concepts

- Automotive manufacturing
- Metal inspection
- [[Multi-industry anomaly detection]]
- Smart manufacturing
- Textile and fiber inspection
- [[MVTec3D]]
- [[Unsupervised anomaly detection]]
- [[Unsupervised anomaly localization]]
- [[Defect segmentation]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, frequency decoupling.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.

- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] uses or reports [[MVTec AD]] for defect synthesis, data augmentation.
- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] evaluates self-supervised pixel-level anomaly localization on MVTec AD using normal-only training images and pixel-wise AUROC.
- [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] uses or reports [[MVTec AD]] for self-supervised anomaly detection, synthetic anomalies.
- [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] reports 97.2 image-level AUROC and 96.3 pixel-level AUROC on MVTec AD with NSA (logistic).
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[MVTec AD]] for industrial defect benchmark, semantic defect annotation.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] uses or reports [[MVTec AD]] for few-shot anomaly generation, diffusion anomaly synthesis.
- [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]] uses or reports [[MVTec AD]] for realistic anomaly synthesis, feature selection.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] uses or reports [[MVTec AD]] for multi-modal anomaly synthesis, diffusion models.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] uses or reports [[MVTec AD]] for gradient ascent anomaly synthesis, industrial anomaly detection.
- [[2025 - Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation]] uses or reports [[MVTec AD]] for few-shot anomaly generation, dual diffusion models.
- [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]] uses or reports [[MVTec AD]] for GAN anomaly detection, feature extraction.
- [[2022 - Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures]] uses or reports [[MVTec AD]] for mask-guided defect generation, non-uniform structures.
- [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] uses or reports [[MVTec AD]] for few-shot defect generation, feature manipulation.
- [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] focuses its main-paper experiments on the MVTec AD hazelnut category and reports CC BY-NC-SA 4.0 licensing for the dataset.
- [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]] uses MVTec AD carpet and wood categories for DCDGANc synthetic segmentation augmentation and MVTec tile for zero-shot defect transfer.
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] uses the MVTec AD bottle subset for supervised glass bottle defect classification and DDPM-generated defective-image augmentation.
- [[2023 - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples]] reports 97.61% average ROC-AUC on MVTec AD with object-aware and diverse patch anomaly simulation.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] reports 98.4% image-level and 97.0% pixel-level AUROC on MVTec AD using [[PatchAnomaly]].
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] compares PAI schemes on MVTec AD and reports [[Affine anomaly insertion]] at 65.5% average APpixel.
- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] reports 99.10% image-level and 98.21% pixel-level AUROC on MVTec AD.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] reports downstream segmentation improvement on MVTec AD using image-mask aligned diffusion synthesis.
- [[2024 - CAGEN Controllable Anomaly Generator Using Diffusion Model]] fine-tunes CAGen on three images from each MVTec AD defect type and reports 97.7 mean localization AUROC / 71.5 AP when generated anomalies replace 30% of DRAEM-style training data.
