---
title: "Data augmentation"
tags:
  - method
---

# Data Augmentation

## Definition

Data augmentation expands or perturbs training data to improve robustness, reduce overfitting, or cover scarce cases.

## Main Forms

- Classical augmentation: flips, crops, rotations, color jitter, noise, blur, geometric transforms.
- [[Learned generative synthesis]]: synthetic examples produced by learned generative models.
- [[Procedural and simulation-based synthesis]]: synthetic examples produced from rules, rendering, physics, or controlled simulation.
- [[Hybrid generative-procedural synthesis]]: synthetic examples produced by combining learned generators with procedural, rule-based, rendering, or simulation components.

## Related Concepts

- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[Hybrid generative-procedural synthesis]]
- [[Domain gap]]

## Used In These Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] uses CutPaste, CutPaste-Scar, and 3-way augmentation prediction to improve MVTec AD detection AUROC over rotation, Cutout, and Scar baselines.
- [[2023 - Attention-Conditioned Augmentations for Self-Supervised Anomaly Detection and Localization]] uses attention-conditioned masking and synthetic anomaly augmentation to improve MVTec AD pixel and image AUROC.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] uses modality-dropout augmentation and attention-guided perturbations to improve RGBD anomaly localization.
- [[2024 - A Comprehensive Augmentation Framework for Anomaly Detection]] removes indiscriminate rotation augmentation and replaces it with selective anomaly simulation plus split training.
- [[2024 - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction]] uses rotation and realistic synthetic anomaly images to improve detection and localization on MVTec AD.










- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] supports automatic data augmentation, industrial defect detection.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses Con-GAN generated defect images as offline data augmentation for limited-data surface defect recognition.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] uses row-row swapping, vertical and horizontal flips, blur variants, and brightness/contrast/saturation changes to improve PV EL defect classification under small, imbalanced training data.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] uses [[G2LGAN]] to generate minority-class wafer maps up to a 5000-sample training target and improve WM-811K macro F1-score by 8.76 points.
- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] balances eight [[WM-811K]] defect classes to 10,000 samples each via autoencoder latent-noise reconstruction, improving CNN validation accuracy from about 85% to about 98%.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] balances wafer-map classes with [[JRGAN]] synthetic samples before [[ResNet-18]] classification.
- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] supports PCB component inspection, generative augmentation.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] supports class imbalance, wafer map defect classification.
- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] supports wafer map defect classification, class imbalance.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] uses ViT attention-derived heatmaps as generated wafer-map samples and compares the augmentation strategy with CycleGAN.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] uses feature-level and image-level anomaly synthesis as augmentation for unsupervised industrial anomaly detection.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] uses generated anomaly image-mask pairs as training data for U-Net localization and ResNet-34 anomaly classification.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] uses generated anomaly image-mask pairs as downstream training data for U-Net localization/detection and ResNet-34 anomaly classification.
- [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]] augments EL solar-cell training images with rotation, mirroring, and flipping.
- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] supports self-supervised pre-training, industrial anomaly dataset.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] supports solar cell defect segmentation, generative data augmentation.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] uses synthetic and GAN-refined images as training data for object detection.
- [[2018 - RenderGAN Generating Realistic Labeled Data]] generates labeled marker data for decoder training.

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] supports wafer map defect recognition, class imbalance.

- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] supports PCB defect detection, semi-supervised learning.
- [[2022 - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation]] adopts data augmentation and grayscale/RGB preprocessing for multi-dataset industrial surface defect detection, but its ablations isolate attention and FDS modules rather than augmentation alone.
- [[2023 - Metal Surface Defect Detection Based on Improved YOLOv5]] expands [[GC10-DET]] with rotation, brightness adjustment, sensor noise, and blur before evaluating improved YOLOv5 variants.
- [[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]] uses geometric and non-geometric disturbances plus image erasure as perturbation-based augmentation in semi-supervised segmentation.
- [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]] uses RoboFlow flips, rotations, shear, saturation, brightness, and noise to expand fabric spot-defect training images.
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] adds 60 DDPM-generated defective MVTec AD bottle images and improves recall/F1 for three CNN classifiers.
- [[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]] uses physics-guided thermal defect synthesis to expand scarce defective pharmaceutical-bag sealing samples.
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] uses [[Poisson defect image augmentation]] to create mobile phone flat-glass defect samples and labels from segmented defects.
- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] augments paired EL-image/I-V training samples with horizontal, vertical, and combined flips.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]] reports data augmentation in 59.32% of reviewed supervised CNN surface-defect studies.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] describes data augmentation as a common response to scarce and imbalanced industrial defect images.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] lists augmentation, resampling, synthetic samples, and transfer learning as responses to unbalanced and small defect datasets.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] augments segmentation training with Defect-Gen synthetic image-mask pairs.
- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]] uses [[GT-CutMix]] to improve detector mAP on [[X-SDD]].
- [[2024 - Steel Surface Defect Detection Based on Denoising Diffusion Implicit Models with Data Augmentation]] uses DDIM-generated [[NEU-DET]] images to improve YOLOv8n mAP@0.5 from 0.748 to 0.803.
- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] uses LoRA-adapted diffusion augmentation to improve [[NEU-SEG]] segmentation mIoU.
- [[2026 - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks]] uses LoRA-adapted diffusion augmentation to improve rare-class [[Magnetic Tile Defects]] classification F1.
- [[2025 - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images]] uses GAN-based AUG300 oversampling to improve PV EL defect classification recall.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses generated defect and non-defect periodic textures to improve weakly supervised golden-template defect segmentation.
- [[2023 - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples]] uses object-aware patch paste plus diverse geometric and color augmentation to improve MVTec AD and BTAD ROC-AUC over CutPaste-style baselines.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] uses [[PatchAnomaly]] to synthesize local anomaly-like patches and train a direct reconstruction-detection model.
- [[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]] uses [[Super-resolution data augmentation]] to improve YOLOv5n fabric defect detection on [[DAGM2007]].
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] compares pseudo-anomaly insertion schemes and reports [[Affine anomaly insertion]] as strongest for APpixel on MVTec AD and VisA.
- [[2025 - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0]] uses rotation, flips, zoom, brightness variation, and Gaussian noise as the training-data augmentation protocol for PV RGB fault classification.
- [[2024 - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies]] compares zoom, rotation, horizontal shift, and vertical shift, with 35-degree rotation improving accuracy from 83.05% to 87.64%.
- [[2024 - Defect detection in textile manufacturing Improving findings using YOLOv5 versions]] uses AITEX-derived augmented bases plus native YOLOv5 augmentation parameters such as mosaic, mixup, and copy-paste for textile defect detection.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses [[Qwen-Image generative augmentation]] to expand scarce RUOD and CarDD support sets for cross-domain few-shot object detection.
