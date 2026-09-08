---
title: "Northeastern University (NEU) surface defect database"
aliases:
  - "Northeastern University surface defect database"
  - "NEU surface defect database"
  - "NEU-CLS"
  - "NEU classification dataset"
related_domain: "[[Metal inspection]]"
url: "https://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm"
data_sources:
  - "Northeastern University surface defect database"
introduced_by: "[[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]"
related_papers:
  - "[[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]"
  - "[[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]"
  - "[[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]]"
  - "[[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]]"
---
# Northeastern University (NEU) surface defect database

## Definition

The Northeastern University (NEU) surface defect database is a hot-rolled steel strip surface defect classification dataset introduced by [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]. The source paper reports 1,800 grayscale 200 x 200 images, with 300 samples each for rolled-in scale, patches, crazing, pitted surface, inclusion, and scratches. `NEU-CLS` is retained as an alias for the classification version of the dataset.

## Why It Matters

It supports evaluation or training for defect detection, localization, classification, segmentation, generation, or benchmark construction.

## Used In These Papers


- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] constructs the Northeastern University (NEU) surface defect database and evaluates AECLBP for six-class steel strip surface defect recognition.
- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] compares [[X-SDD]] with NEU-CLS, noting that X-SDD adds one defect category and has stronger class imbalance.
- [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] uses NEU-CLS to compare classic augmentation, DCGAN, ACGAN, InfoGAN, and fine-tuned CNN classifiers for steel surface defect classification.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] identifies NEU-CLS as the original six-class NEU surface defect dataset and upgrades it into [[NEU-DET]] with detection annotations.
- [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses NEU-CLS for limited-data Con-GAN defect generation and recognition experiments, with 1,800 steel surface images across six defect classes.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] uses NEU-CLS for generated-image FID/SDS evaluation and YOLO-v5/YOLO-v8 detection augmentation experiments.
- [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] uses NEU-CLS for hot-rolled strip steel defect image generation and YOLOX detection, reporting mAP@0.5 improvement from 72.1 to 78.2 with generated images.
- [[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]] uses NEU-CLS for semi-supervised strip steel surface defect classification with synthetic image generation.
- [[2023 - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2]] uses NEU-CLS for EDCGAN-generated steel surface defect augmentation and MobileNet V2 classification.
- [[2025 - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection]] uses DDPM-CSD to generate NEU-CLS defect images and improves ResNet-18 classification accuracy from 93.24 to 99.89.
- [[2023 - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT]] uses NEU-CLS as an industrial surface-defect dataset for private synthetic image generation and downstream classification.

## Source Anchors

- Hosting source: https://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm.
- Mirror/source pointer: the NEU faculty page was identified through indexed paper and search evidence; the page did not return successfully during the 2026-06-05 audit.
- Introducing paper for the classification dataset: [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] names the dataset the Northeastern University (NEU) surface defect database and reports 1,800 images across six classes.
- Detection-annotation follow-up: [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] upgrades NEU-CLS into [[NEU-DET]].
- Popular usage paper: [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] uses NEU-CLS for steel surface defect classification and GAN augmentation.
- Additional usage paper: [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] uses NEU-CLS for limited-data surface defect recognition.

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Defect classification]]
- [[Adjacent evaluation completed local binary patterns]]
- [[Accuracy]]
- [[X-SDD]]
