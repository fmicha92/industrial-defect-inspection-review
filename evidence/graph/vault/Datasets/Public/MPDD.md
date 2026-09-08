---
title: "MPDD"
aliases:
  - "MPDD"
related_domain: "[[Metal inspection]]"
url: "https://github.com/stepanje/MPDD"
data_sources: "GitHub"
introduced_by: "[[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]]"
---
# MPDD

## Definition

MPDD is a metal-parts anomaly detection dataset for complex production-like acquisition conditions, including variable part pose, changing lighting, multiple objects, non-homogeneous backgrounds, and motion blur.

## Why It Matters

It supports semi-supervised and unsupervised anomaly detection with normal-only training data, normal/anomalous test images, and pixel-level defect masks.

## Used In These Papers


- [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] introduces MPDD and benchmarks state-of-the-art anomaly detection methods on it.
- [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]] uses or reports [[MPDD]] for realistic anomaly synthesis, feature selection.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] uses or reports [[MPDD]] for gradient ascent anomaly synthesis, industrial anomaly detection.
- [[2023 - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection]] evaluates latent diffusion with feature editing on MPDD, reporting 96.5 detection AUROC and 99.0 localization AUROC.

## Dataset Details

- Classes: Bracket Black, Bracket Brown, Bracket White, Connector, Metal Plate, and Tubes.
- Training images: 888 normal images.
- Test images: 176 normal and 282 anomalous images.
- Image size: 1024 x 1024 pixels.
- Annotation: pixel-precise masks for anomalous samples.
- License: not reported.

## Source Anchors

- Hosting source: https://github.com/stepanje/MPDD.
- Introducing paper: [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]].

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
