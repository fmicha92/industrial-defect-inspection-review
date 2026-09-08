---
title: "G2LGAN"
aliases:
  - "Global-to-local generative adversarial network"
  - "global-to-local GAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]]"
evidence_count: 1
---
# G2LGAN

## Definition

G2LGAN is a global-to-local GAN training strategy for imbalanced wafer-map augmentation. It first trains a generator on all classes to learn global wafer-map structure, then fine-tunes class-specific generators to learn local defect-pattern features.

## Why It Matters

The method targets minority classes in imbalanced [[WM-811K]] and 21-Defect wafer-map datasets, where training a separate generator from scratch can collapse or produce low-diversity samples.

## Used In These Papers

- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] introduces G2LGAN and reports that adding its generated samples improves WM-811K accuracy from 89.23% to 98.39% and F1-score from 84.25% to 93.01%.

## Related Concepts

- [[GAN]]
- [[DCGAN wafer map augmentation]]
- [[Data augmentation]]
- [[Synthetic data generation]]
- [[Wafer map defect classification]]
- [[WM-811K]]
