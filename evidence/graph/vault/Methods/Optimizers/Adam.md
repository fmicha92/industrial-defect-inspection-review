---
title: "Adam"
aliases:
  - "Adaptive Moment Estimation"
  - "Adam optimizer"
tags:
  - method
  - optimizer
---
# Adam

## Definition

Adam is a first-order stochastic optimization algorithm that keeps exponential moving averages of gradients and squared gradients, then uses bias-corrected moment estimates to update parameters with adaptive per-parameter step sizes.

## Why It Matters

Adam combines sparse-gradient behavior associated with AdaGrad and non-stationary-objective behavior associated with RMSProp while remaining easy to implement and memory efficient.

## Used In These Papers

- [[2015 - Adam A Method for Stochastic Optimization]] introduces Adam, analyzes its online convex optimization regret, and evaluates it on MNIST, IMDB bag-of-words, CIFAR-10, and VAE training.
- [[2017 - Attention Is All You Need]] uses Adam with beta1 = 0.9, beta2 = 0.98, epsilon = 1e-9, and an inverse-square-root warmup schedule.
- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] trains OCR-GAN with Adam using beta1 0.5, beta2 0.999, weight decay 1e-4, and learning rate 0.002.
- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] trains OmniAL with Adam at initial learning rate 1e-4.
- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] trains DiAD with Adam at learning rate 1e-5, batch size 12, for 1,000 epochs on a single NVIDIA Tesla V100 32GB.
- [[2025 - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images]] trains CNN backbones with Adam while evaluating GAN-oversampled PV EL defect classification.
- [[2025 - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0]] uses Adam for supervised RGB PV surface fault classification.
- [[2024 - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies]] trains ResNet50 with Adam at learning rate 0.0001 for solar panel defect classification augmentation experiments.

## Related Concepts

- [[Optimizers]]
- [[AdaGrad]]
- [[RMSProp]]
- [[AdaMax]]
- [[Stochastic gradient descent]]
