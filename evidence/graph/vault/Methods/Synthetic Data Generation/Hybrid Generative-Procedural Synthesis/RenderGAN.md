---
title: "RenderGAN"
aliases:
  - "RenderGAN synthetic labeled data"
tags:
  - method
---

# RenderGAN

## Definition

RenderGAN is a hybrid generative-procedural synthesis method that combines a simple 3D marker model with learned GAN-driven augmentations for blur, lighting, background, and image detail.

## Why It Matters

RenderGAN preserves labels from the 3D model while learning hard-to-model image effects from unlabeled real data. This makes it useful when high-level labels are expensive but a controllable object model exists.

## Used In These Papers

- [[2018 - RenderGAN Generating Realistic Labeled Data]] uses RenderGAN to generate labeled honeybee marker images for decoder training.

## Related Concepts

- [[Hybrid generative-procedural synthesis]]
- [[Synthetic data generation]]
- [[GAN]]
- [[Rule-based data synthesis]]
- [[Domain gap]]
