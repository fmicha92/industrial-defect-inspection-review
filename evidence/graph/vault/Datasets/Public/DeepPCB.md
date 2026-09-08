---
title: "DeepPCB"
related_domain: "[[Semiconductor and electronics]]"
url: "https://github.com/tangsanli5201/DeepPCB"
data_sources: "GitHub"
introduced_by: "[[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]]"
---
# DeepPCB

## Definition

DeepPCB is a public PCB defect dataset with 1,500 template/test image pairs and annotations for six PCB defect types, as reported by Tang et al.

## Why It Matters

It provides a public benchmark for PCB defect detectors that need both defect localization and defect classification.

## Used In These Papers

- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] introduces DeepPCB and reports 98.6% mAP at 62 FPS on it.
- [[2023 - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection]] uses DeepPCB to test cTransGAN augmentation for PCB defect detection, reporting 98.8% mAP with Faster R-CNN ResNet101 plus cTransGAN.
- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] uses DeepPCB as the target benchmark for DE-SSD, including 50/100/200 labeled-sample semi-supervised settings and a 1,000-sample fully supervised setting.
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] uses a Peking University PCB dataset for generalization experiments and reports [[CE-SGNet]] at 53.8 AP and 97.0 AP50.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses 900 images from a Peking University PCB surface defects dataset with a 6:2:2 split and reports IDD-Net at 95.9% [[mAP@0.50]].
- [[2023 - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT]] uses DeepPCB to evaluate private synthetic image generation for industrial imbalanced learning.

## Dataset Details

- Size: 1,500 aligned PCB image pairs.
- Pair contents: one 640 x 640 defect-free template image and one defective tested image.
- Split: 1,000 image pairs for train/validation and 500 image pairs for test.
- Defect categories: open, short, mousebite, spur, pin hole, and spurious copper.
- Annotation: axis-aligned bounding boxes with class IDs.
- Capture: linear scan CCD at about 48 pixels per millimetre.
- Preprocessing: original images of about 16k x 16k pixels are clipped into 640 x 640 sub-images and aligned by template matching; binarization is used to reduce illumination disturbance.
- License: not reported.

## Source Anchors

- Hosting source: https://github.com/tangsanli5201/DeepPCB.
- Introducing paper: [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]].

## Related Concepts

- [[PCB defect detection]]
- [[PCB defect classification]]
- [[Semiconductor and electronics]]
- [[CE-SGNet]]

- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] supports PCB defect detection, semi-supervised learning.
