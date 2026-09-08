---
title: "Domain gap"
aliases:
  - "Synthetic-to-real gap"
tags:
  - concept
---

# Domain gap

## Definition

Domain gap is the mismatch between the data distribution used for training and the data distribution encountered during real inspection. In these notes, it most often refers to synthetic-to-real transfer failures caused by missing real-world effects, different sensors, noise, artifacts, or unrealistic generated defects.

## Why It Matters

Most papers try to compensate for scarce real defect data. Their value depends on whether simulated or generated examples improve performance on real inspection data rather than only looking plausible or performing well in synthetic validation.

## Used In These Papers

- [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] explicitly notes simulated-to-real performance drops and possible missing real-world aspects.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses domain randomization and still requires real-world fine-tuning in the reported experiment.
- [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] uses synthetic perturbations and notes better anomaly generation as future work.
- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] reports that extreme cases far from the training set remain difficult.
- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] reports weaker DINOv2 frozen-feature performance and frames it as a domain gap between pretraining data and gearbox inspection images.
- [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] uses SimGAN to reduce the simulator-to-real image gap with unlabeled real data.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] compares domain randomization and GAN refinement for industrial object detection.
- [[2018 - RenderGAN Generating Realistic Labeled Data]] learns realistic marker-image effects from unlabeled real data to close the gap from an idealistic 3D model.
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] structures domain randomization around scene context for vehicle detection on KITTI.

## Related Concepts

- [[Synthetic data generation]]
- [[Domain randomization]]
- [[Hybrid generative-procedural synthesis]]
- [[Structured domain randomization]]
- [[Transfer learning]]
- [[Simulation-based data augmentation]]
- [[Distribution shift]]
