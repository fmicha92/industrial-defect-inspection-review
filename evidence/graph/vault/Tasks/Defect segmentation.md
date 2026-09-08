---
title: "Defect segmentation"
aliases:
  - "Defect localization"
  - "Anomaly localization"
tags:
  - concept
  - task
---

# Defect segmentation

## Definition

Defect segmentation identifies the location and extent of defects at pixel or voxel level. It includes 3D CT voxel segmentation, 2D image segmentation, anomaly localization, and textured surface defect segmentation.

## Why It Matters

Segmentation gives more actionable inspection output than image-level classification because it indicates where a defect is. The papers also show segmentation is harder to supervise because pixel- or voxel-level labels are expensive, motivating synthetic labels, simulated data, and unsupervised anomaly methods.

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] reports MVTec AD pixel-wise localization AUROC using patch-level CutPaste anomaly scores.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] reports MVTec AD pixel-wise anomaly localization after attention-guided synthetic anomaly fine-tuning.
- [[2025 - Industrial Image Anomaly Detection via Synthetic-Anomaly Contrastive Distillation]] reports MVTec AD pixel AUROC and PRO for synthetic-anomaly contrastive distillation.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] reports MVTec AD and VisA pixel AUROC/AUPRO using RGBD fusion and attention-guided synthetic perturbations.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] reports MVTec AD localization AUROC/AP and shows gains from selective anomaly simulation.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] reports MVTec AD defect localization AP gains from realistic synthetic anomaly training.

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] trains pixel-wise defect masks for [[KolektorSDD]] and uses the segmentation output as evidence for image-level defect decisions.
- [[2022 - Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures]] uses MDGAN-generated pixel-level annotations to train UNet and sResNet segmentation models.
- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] provides LabelMe pitting annotations for segmentation on [[BSData]].
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] evaluates binary pixel-level defect masks on [[Industrial-5i]].
- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] introduces [[NEU-SEG]] and evaluates [[PGA-Net]] for pixel-wise surface defect segmentation.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] introduces [[FDSNet]] and [[MSD]] for real-time pixel-level surface-defect segmentation.
- [[2020 - Surface Defect Saliency of Magnetic Tile]] introduces [[Magnetic Tile Defects]] and evaluates [[MCuePush U-Net]] for pixel-level magnetic-tile defect saliency.









- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] provides LabelMe pixel-level anomaly masks and reports pixel-level AUPRO for Real-IAD anomaly localization.
- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] supports logical anomalies, structural anomalies.
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] supports self-supervised pre-training, industrial anomaly dataset.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] supports 3D anomaly detection, industrial visual inspection.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] supports mixed supervision, surface defect detection.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] trains a 3D U-Net-like segmentation model on simulated CT data.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] trains customized U-Net models for aircraft engine defect segmentation.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] performs textured surface anomaly detection and segmentation.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] evaluates image anomaly localization using AU-ROC and AU-PRO.
- [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]] provides bounding-box and polygon annotations for fabric spot defects.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] produces pixel-level defect heatmaps for fabric anomaly localization and reports 91% localization precision.
- [[Dataset of Solar Cells Defect Segmentation]] provides refined labels for photovoltaic-cell EL defect segmentation.
- [[BenchmarkELimages]] provides pixel-level feature and defect masks for electroluminescence solar-cell semantic segmentation.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] introduces [[BenchmarkELimages]] and benchmarks U-Net, PSPNet, and DeepLabv3+ on solar-cell EL defect segmentation.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] evaluates [[LMFF]] for pixel-level segmentation of monocrystalline and polycrystalline solar-cell defects.
- [[EL-2019]] provides crack and finger-interruption solar-cell EL image patches used for SIGAN segmentation experiments.
- [[Heat Sink Surface Defect Dataset]] provides pixel-level labels for scratch and stain segmentation on gold-plated tungsten-copper alloy heat sink surfaces.
- [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]] proposes [[GSLU-Net]] for pixel-level heat-sink scratch and stain segmentation.

## Related Concepts

- [[Surface defect detection]]
- [[U-Net]]
- [[Unsupervised anomaly localization]]
- [[MVTec AD]]
- [[MVTec3D]]
- [[FD_Dataset]]
- [[FabricSpotDefect]]
- [[Dataset of Solar Cells Defect Segmentation]]
- [[BenchmarkELimages]]
- [[Heat Sink Surface Defect Dataset]]
- [[GSLU-Net]]
- [[LMFF]]
- [[EL-2019]]
- [[Industrial-5i]]
- [[IndustrialNet]]
- [[BSData]]
- [[Mask R-CNN]]
- [[FDSNet]]
- [[PGA-Net]]
- [[NEU-SEG]]
- [[MSD]]
- [[Magnetic Tile Defects]]
- [[MCuePush U-Net]]
- [[STDAN]]

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] supports unsupervised anomaly detection, anomaly localization.

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]] includes semantic segmentation and instance segmentation as higher-detail surface-defect problem types with lower adoption than classification and detection.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] treats pixel-level segmentation as a state-of-the-art AOI direction and recommends MeanIoU or Dice coefficient over accuracy-only comparisons.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reviews FCN, U-Net, lightweight semantic segmentation, and X-ray segmentation methods for industrial defect detection.

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] supports multimodal anomaly detection, RGB-D inspection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, frequency decoupling.

- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] supports unsupervised anomaly detection, normalizing flows.

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] supports 3D surface anomaly detection, depth simulation.

- [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] supports multimodal anomaly detection, crossmodal mapping.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] reports pixel-level anomaly localization with AUROC and PRO across MVTec AD, VisA, MPDD, and WFDD.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] performs weakly supervised periodic-texture defect segmentation by generating CycleGAN golden templates and thresholding patch-wise differences.
