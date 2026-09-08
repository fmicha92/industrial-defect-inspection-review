---
title: "DDPM-CSD"
aliases:
  - "Cross-Scale Diffusion"
  - "Cross-Scale Diffusion for steel defect generation"
tags:
  - method
---
# DDPM-CSD

## Definition

DDPM-CSD is a DDPM-based steel defect image generator that adds cross-scale attention and sliding-window skip connections to improve generated sample fidelity across defect textures.

## Why It Matters

It generates synthetic [[NEU-CLS]] defect images that improve downstream classifier accuracy when mixed with original training images.

## Used In These Papers

- [[2025 - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection]] evaluates DDPM-CSD with [[FID]] and classification accuracy on [[NEU-CLS]].

## Related Concepts

- [[Diffusion models]]
- [[Learned generative synthesis]]
- [[Synthetic data generation]]
- [[FID]]
