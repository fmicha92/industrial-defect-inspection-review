---
title: "ToCoAD"
aliases:
  - "Two-Stage Contrastive Learning for Industrial Anomaly Detection"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---

# ToCoAD

## Definition

ToCoAD is a two-stage industrial anomaly detection method. It first trains a discriminative network on synthetic anomalies, then freezes that network to provide negative guidance while a feature extractor is fine-tuned with bootstrap contrastive learning.

## Why It Matters

The method targets the domain gap between ImageNet-pretrained feature extractors and industrial inspection images. Its second stage uses negative-guided contrastive learning to adapt features to target industrial data while preserving unsupervised training with only normal images.

## Used In These Papers

- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] reports 99.10% image-level and 98.21% pixel-level AUROC on [[MVTec AD]], 95.35% image-level and 98.43% pixel-level AUROC on [[VisA]], and 97.70% pixel-level AUROC on [[BTAD]].

## Related Concepts

- [[Industrial anomaly detection]]
- [[Self-supervised learning]]
- [[Contrastive learning]]
- [[Defect synthesis]]

