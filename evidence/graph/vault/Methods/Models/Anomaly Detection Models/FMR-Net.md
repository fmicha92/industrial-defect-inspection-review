---
title: "FMR-Net"
aliases:
  - "Feature Memory Rearrangement Network"
  - "Feature Memory Rearrangement Network for textured surface defects"
tags:
  - method
  - model
  - anomaly-detection
status: stable
concept_type: method
source_papers:
  - "[[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
related_methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Synthetic data generation]]"
  - "[[Edge intelligence]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[DAGM]]"
  - "[[RSDDs]]"
  - "[[Printed product surface dataset]]"
---
# FMR-Net

## Definition

FMR-Net is an unsupervised textured surface defect inspection model that restores defective regions toward normal texture before scoring anomalies. It combines an encoder-decoder reconstruction network, a contrastive-learning-based memory feature module, a global feature rearrangement module, synthetic defect training, multimodal anomaly scoring, and multilevel inference for edge-cloud inspection.

## Why It Matters

Industrial texture inspection often lacks real labeled defect examples. FMR-Net targets that setting by training from defect-free samples and artificial synthetic defects, then using feature memory and rearrangement to suppress residual anomalous patterns during reconstruction.

## Used In These Papers

- [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] proposes FMR-Net for unsupervised textured surface anomaly detection and evaluates it on [[MVTec AD]], [[DAGM]], [[RSDDs]], and printed product surface defects.

## Method Details

- Contrastive-learning-based memory feature module records normal texture features and substitutes normal features for anomalous latent features.
- Global feature rearrangement suppresses residual defects on skip-connection features using texton-based local feature rearrangement.
- Two-phase training first learns background reconstruction and the memory bank, then trains defect restoration with artificial synthetic defect images.
- Multimodal inspection fuses anomaly maps from gradient-magnitude similarity, structural similarity, and per-pixel residual criteria.
- Multilevel inference supports patch-level early exit and pixel-level inspection for edge-cloud deployment.

## Related Concepts

- [[Anomaly Detection Models]]
- [[Unsupervised anomaly detection]]
- [[Unsupervised anomaly localization]]
- [[Synthetic data generation]]
- [[Edge intelligence]]
- [[Surface defect detection]]
- [[Defect segmentation]]
