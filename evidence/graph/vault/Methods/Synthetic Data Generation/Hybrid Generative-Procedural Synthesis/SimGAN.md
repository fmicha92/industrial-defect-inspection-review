---
title: "SimGAN"
aliases:
  - "Simulated+Unsupervised learning"
tags:
  - method
---

# SimGAN

## Definition

SimGAN is a hybrid synthetic-data refinement method that uses a simulator to produce labeled synthetic images and an adversarial refiner network to make those images more realistic while preserving simulator-provided annotations.

## Why It Matters

The method targets the [[Domain gap]] between synthetic and real images without requiring labeled real images. The simulator supplies labels, while the learned refiner models missing real-image effects.

## Used In These Papers

- [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] introduces SimGAN for simulator-to-real refinement in gaze estimation and hand pose estimation.

## Related Concepts

- [[Hybrid generative-procedural synthesis]]
- [[Synthetic data generation]]
- [[GAN]]
- [[Domain gap]]
- [[Learned generative synthesis]]
- [[Procedural and simulation-based synthesis]]
