---
title: "Affine anomaly insertion"
aliases:
  - "AA insertion"
  - "Affine pseudo-anomaly insertion"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Procedural and Simulation-Based Synthesis"
source_papers:
  - "[[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]]"
evidence_count: 1
tags:
  - method
---

# Affine anomaly insertion

## Definition

Affine anomaly insertion is a pseudo-anomaly insertion method that transforms image patches and inserts them into normal samples to generate synthetic anomaly images and masks. The paper reports variants that directly apply transformed patches, use an anomaly source image, or apply color transforms.

## Why It Matters

The method emphasizes pixel-level anomaly realism and mask quality. In the reported PAI comparison, affine anomaly insertion achieved the highest APpixel averages on [[MVTec AD]] and [[VisA]], indicating stronger synthetic supervision for anomaly segmentation than the competing pseudo-anomaly schemes tested in that paper.

## Used In These Papers

- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] evaluates affine anomaly insertion against source-free and source-based PAI schemes, reporting APpixel gains of 5.2% on [[MVTec AD]] and 10.1% on [[VisA]] over the second-best PAI method.

## Related Concepts

- [[Defect synthesis]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Self-supervised learning]]

