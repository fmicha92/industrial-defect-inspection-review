---
title: "Object detection"
tags:
  - task
---

# Object detection

## Definition

Object detection localizes and classifies object instances, typically with bounding boxes.

## Used In These Papers

- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] evaluates Mask R-CNN detection of industrial electric parts.
- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] provides pitting annotations in [[BSData]] that support object detection and instance segmentation.
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] evaluates Faster R-CNN vehicle detection on KITTI.
- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] evaluates FCOS, YOLOv5, YOLOv8, and RT-DETR for defect bounding-box detection on [[MSDD]].
- [[Metal Surface Defects Dataset]] is a Kaggle package derived from [[GC10-DET]] with XML bounding-box labels; treat [[GC10-DET]] as the canonical standalone dataset.
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] trains YOLOv11 models for PV panel detection and synthetic PV fault detection from UAV thermal imagery.
- [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]] trains [[GBH-YOLOv5]] for PV panel defect localization and classification on [[PV-Multi-Defect]].
- [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] uses YOLOX object detection to test whether generated NEU and IP-def defect images improve downstream mAP.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] uses object detection for steel surface defect classification and localization on [[NEU-DET]].
- [[2025 - You Only Look Once-Aluminum]] uses object detection for aluminum profile surface defects on [[APDDD]].
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses one-stage object detection for steel, aluminium, PCB, and glass-bottle defect datasets.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]] treats object detection as the second most common surface-defect problem type, appearing in 33.90% of final studies.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]] reviews YOLO and R-CNN object-detection methods for localizing visual defects in AOI.
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]] reviews Faster R-CNN, cascaded R-CNN, MobileNet-SSD, YOLOv3, and YOLOv5 for industrial product defect localization.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] evaluates object detection on RUOD, CARPK, and CarDD under cross-domain 1/5/10-shot settings.

## Related Concepts

- [[Average precision]]
- [[mAP]]
- [[Faster R-CNN]]
- [[Defect Detection Network]]
- [[NEU-DET benchmark]]
- [[Mask R-CNN]]
- [[FCOS]]
- [[RT-DETR]]
- [[YOLOv5]]
- [[YOLOv8]]
- [[YOLO-AL]]
- [[YOLOv11]]
- [[GBH-YOLOv5]]
- [[Cross-domain few-shot object detection]]
- [[GroundingDINO]]
- [[GLIP]]
