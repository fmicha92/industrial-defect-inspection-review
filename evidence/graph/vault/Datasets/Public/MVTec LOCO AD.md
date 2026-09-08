---
title: "MVTec LOCO AD"
aliases:
  - "MVTec LOCO AD"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://www.mvtec.com/research-teaching/datasets/mvtec-loco-ad"
data_sources: "MVTec"
introduced_by: "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
related_papers:
  - "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
availability: "public"
access: "downloadable from MVTec research dataset page"
licenses:
  - "CC BY-NC-SA 4.0"
---
# MVTec LOCO AD

## Definition

MVTec LOCO AD is an industrial anomaly detection and localization dataset with five object categories and balanced coverage of [[Structural anomalies]] and [[Logical anomalies]].

## Why It Matters

It evaluates whether unsupervised anomaly methods can detect both local visual defects and violations of object-count, position, fill-level, wiring, or label constraints that require broader context than a local patch.

## Used In These Papers

- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] introduces MVTec LOCO AD, reports 3,644 images across five categories, and evaluates GCAD against several anomaly-localization baselines.

## Dataset Details

- Categories: Breakfast Box, Screw Bag, Pushpins, Splicing Connectors, and Juice Bottle.
- Training images: 1,772 anomaly-free images.
- Validation images: 304 anomaly-free images.
- Test images: 575 anomaly-free, 432 structural-anomaly, and 561 logical-anomaly images.
- Defect types: 89.
- Annotation: pixel-precise masks for all anomalies.
- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Primary metric in the introducing paper: [[Area Under Saturated Per-Region Overlap]].
- Availability: public download from https://www.mvtec.com/research-teaching/datasets/mvtec-loco-ad.
- License: CC BY-NC-SA 4.0; commercial use is not allowed under the MVTec terms.

## Source Anchors

- Hosting source: https://www.mvtec.com/research-teaching/datasets/mvtec-loco-ad.
- Introducing paper: [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]].
- Access terms: CC BY-NC-SA 4.0, noncommercial.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Logical anomalies]]
- [[Structural anomalies]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]

- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[MVTec LOCO AD]] for industrial defect benchmark, semantic defect annotation.
- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] uses or reports [[MVTec LOCO AD]] for multi-modal anomaly synthesis, diffusion models.
