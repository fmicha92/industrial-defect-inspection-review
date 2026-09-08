---
title: "PSRT50"
aliases:
  - "PSO based ResNet50"
  - "PSO-ResNet50"
tags:
  - method
---

# PSRT50

## Definition

PSRT50 is a [[ResNet50]]-based fabric classification model whose learning rate and momentum are selected with [[Particle Swarm Optimization]]. It is proposed for classifying fabric microscopy images into plain, satin, and twill categories.

## Why It Matters

The model is designed for real-time textile inspection on resource-constrained hardware. [[2025 - AI-driven fabric classification]] reports that PSRT50 improves accuracy over the unoptimized ResNet50 baseline on the paper's augmented fabric image dataset.

## Used In These Papers

- [[2025 - AI-driven fabric classification]] introduces PSRT50 and deploys the pre-trained model on Raspberry Pi 4 for real-time fabric image classification.

## Related Concepts

- [[ResNet50]]
- [[Particle Swarm Optimization]]
- [[Textile and fiber inspection]]
- [[Defect classification]]
