---
title: "Transfer learning"
aliases:
  - "Transfer learning paradigm"
tags:
  - learning-paradigm
---

# Transfer Learning

## Definition

Transfer learning reuses a model, representation, or learned knowledge from one dataset, task, or domain to improve learning in another.

## Typical Use

Useful when target-domain labels are limited, target data is scarce, or pretrained models provide stronger features than training from scratch. In the papers, this often means starting from pretrained CNN weights or using synthetic-data pretraining before adapting to real industrial inspection images.

## Vault Relevance

Industrial inspection datasets in this vault are usually small or defect-scarce. Transfer learning reduces the amount of real defect data needed, but the papers also show that transfer depends on the gap between synthetic and real inspection images.

## Used In These Papers


- [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] supports benchmarking, self-supervised anomaly detection.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses an ImageNet-pretrained ResNet and compares real-world-only training with synthetic pretraining followed by real-world fine-tuning.
- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] trains on simulated CT data and evaluates transfer to real CT scans.
- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] reports transfer-learning feature comparisons as part of its aircraft engine defect detection framework.
- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] initializes a SwinV2-B transformer with pretrained weights before fine-tuning for EL-to-I-V curve prediction.
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] initializes YOLOv11 models with COCO-pretrained weights before fine-tuning on UAV thermal panel and synthetic fault data.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]] reports transfer learning in 83.05% of reviewed supervised CNN surface-defect studies.

## Related Concepts

- [[Domain gap]]
- [[Synthetic data generation]]
- [[Simulation-based data augmentation|Simulated training data]]
- [[ImageNet]]
