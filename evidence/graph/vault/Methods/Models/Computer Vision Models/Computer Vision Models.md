---
title: "Computer Vision Models"
tags:
  - model-family
---

# Computer Vision Models

## Scope

Computer vision models process images, video, depth maps, CT volumes, and related visual inspection data.

## Common Model Types

- Classification: [[ResNet-18]], ResNet, EfficientNet, Vision Transformer
- Hybrid classification: [[IncepViTH-Net]]
- Object detection: YOLO, [[YOLOv5]], [[GBH-YOLOv5]], Faster R-CNN, RetinaNet, DETR
- Segmentation: [[U-Net]], Mask R-CNN, DeepLab, Segment Anything
- Anomaly detection: PaDiM, PatchCore, STFPM, [[CDO]], [[FMR-Net]]
- Generative vision: [[GAN]], diffusion models, VAEs

## Current Vault Links

- [[Neural Networks]]
- [[Transformers]]
- [[Segmentation Models]]
- [[Anomaly Detection Models]]
- [[Generative Models]]
- [[Defect segmentation]]
- [[Defect classification]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Unsupervised anomaly localization]]

## Used In These Papers

- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] uses a 3D convolutional segmentation network for CT defect segmentation.
- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] evaluates YOLOv4-family object detectors.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses an ImageNet-pretrained 18-layer ResNet classifier.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] uses U-Net, DCGAN, Pix2Pix, and image preprocessing.
- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] and [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] evaluate visual anomaly-localization models.
- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] uses [[ResNet-18]] as the self-supervised anomaly-localization backbone.
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] combines convolutional, transformer, segmentation, and harmonic-fusion components for solar panel fault classification.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] proposes [[GBH-YOLOv5]], a YOLOv5-derived object detector for PV panel surface defects.
- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] proposes [[Parallel attention-residual CNN]] for steel surface defect feature extraction and classification.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] proposes [[IDD-Net]], a one-stage industrial defect detector combining local-global backbone features, three-layer feature aggregation, multi-scale fusion, and Defect-IoU localization loss.
