---
title: "Accuracy"
aliases:
  - "classification accuracy"
tags:
  - metric
  - classification
---

# Accuracy

## Definition

Accuracy measures the fraction or percentage of predictions that are correct. It is used for classification and segmentation-adjacent model evaluation when reported by the paper.

## Direction

Higher is better.

## Used In These Papers

- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] reports recognition accuracy on [[NEU-CLS]], with AECLBP + SVM reaching 98.93 +/- 0.63 across 100 random partitions.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] reports [[RepVGG+SA]] at 95.10% accuracy on [[X-SDD]], with the lowest per-class accuracy 78.95% for oxide scale of plate system.
- [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] reports classification accuracy for small-sample surface defect classification, including 98.53% on [[KolektorSDD]] and 99.57% average on [[DAGM2007]] classes 1-6 in the headline settings.
- [[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]] reports wafer bin map defect-pattern classification accuracy for classifiers trained with DCGAN-augmented versus CAE-augmented data.
- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] reports 98.15% binary accuracy and 95.35% multiclass accuracy on [[ELPV Dataset]] using fused Inception-V3 and ResNet50 deep features with data augmentation.










- [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] reports 94.63% overall accuracy for two-stage WMFPR on the WM-811K test set.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] reports 95.4% average accuracy on [[WM-811K]] after CAE augmentation and 97.5% on [[MixedWM38]].
- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] supports electroluminescence images, deep feature representations.
- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]] supports fabric inspection, public benchmark.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses accuracy as the primary defect recognition metric on NEU-CLS and the PCB case.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] supports limited defect data, dual discriminator GAN.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] supports photovoltaic cell defects, electroluminescence images.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] supports wafer map defect classification, class imbalance.
- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] supports mixed-type wafer defects, deformable convolution.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] supports class imbalance, wafer map defect classification.
- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] supports wafer map defect classification, class imbalance.
- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] reports ResNet34 and DenseNet121 classification accuracy with and without Defect-GAN augmentation.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses accuracy as the primary metric for blowhole classification.
- [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] reports NEU-CLS classification accuracy for classic, DCGAN, ACGAN, InfoGAN, and fine-tuned CNN augmentation settings.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] reports validation accuracy for U-Net defect segmentation experiments.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] reports 95% detection accuracy for STDAN on fabric defect detection.

## Related Metrics

- [[Precision]]
- [[Recall]]
- [[Specificity]]
- [[Classification metrics]]
- [[NEU-CLS]]
- [[Adjacent evaluation completed local binary patterns]]

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] supports wafer map defect recognition, class imbalance.
- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] reports 88.02% MGGAN auxiliary-classifier accuracy on original data and 93.43% ResNet101 accuracy after MGGAN enhancement.

- [[2020 - Self-Supervised Representation Learning for Wafer Bin Map Defect Pattern Classification]] supports wafer bin map classification, self-supervised learning.
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] reports 96.988% accuracy at K value 8 for solar panel fault classification.
- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports ResNet50 as the best tested classifier with 82.3% accuracy on the selected PV panel fault dataset subset.
- [[2020 - Infrared Solar Module Dataset for Anomaly Detection]] proposes future classification benchmarking on [[InfraredSolarModules]], but does not report accuracy values.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]] reports VGG16 wafer-map classification accuracy, including 93.56% baseline and ViT-vs-CycleGAN equalized-training comparisons up to 93.91% for ViT at 3,000 samples per class.
- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] reports 66.09% average anomaly classification accuracy for ResNet-34 trained on generated MVTec AD anomaly data.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] reports 74.70% MVTec AD and 50.95% MVTec LOCO anomaly classification accuracy for ResNet-34 trained on generated anomaly data.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reports reviewed accuracy examples for surface and X-ray defect detection, including ShuffleDefectNet on NEU and CNN welding X-ray recognition.
