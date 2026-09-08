---
title: "Gearbox components remanufacturing inspection dataset"
aliases:
  - "gearboxcomponents-remanufacturing-inspection"
  - "Gearbox components remanufacturing inspection"
  - "Remanufacturing gearbox component dataset"
related_domain: "[[Remanufacturing inspection]]"
url: "https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection"
data_sources: "Kaggle"
introduced_by: "[[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]]"
availability: "public"
licenses: "not reported"
---
# Gearbox Components Remanufacturing Inspection Dataset

## Definition

Gearbox components remanufacturing inspection dataset is a public RGB image-patch dataset introduced by [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]]. It contains OK/nOK labels for patches from worn automotive gearbox components.

## Why It Matters

The dataset supports [[Defect classification]] under realistic train-test shifts in [[Remanufacturing inspection]]. Its split protocols test whether image classifiers generalize beyond random IID splits to new acquisition settings, physical parts, and component categories.

## Used In These Papers

- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] introduces the dataset, defines split protocols, and reports CNN and Transformer baselines.

## Dataset Details

- Domain: [[Remanufacturing inspection]].
- Task: [[Defect classification]].
- Source: defective BMW E36 automatic transmission and Mini r53 6-speed manual transmission.
- Components: 46 physical components, with 19 from the BMW transmission and 27 from the Mini transmission.
- Image modality: RGB image patches.
- Patch size: 128 x 128 pixels.
- Total labeled patches: 15,588.
- Labels: 8,334 OK and 7,254 nOK.
- Component categories: gear wheel, synchronizer ring/cone, synchronizer body, synchronizer collar, and spline.
- Splits: S1 random images, S2 acquisition settings, S3 functional part IDs, and S4 component categories.
- Artifact: https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection.
- License: not reported in the extracted text.

## Source Anchors

- Hosting source: https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection.
- Introducing paper: [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]].

## Related Concepts

- [[Gearbox component distribution-shift inspection benchmark]]
- [[Remanufacturing inspection]]
- [[Automotive manufacturing]]
- [[Industrial visual inspection]]
- [[Distribution shift]]
- [[Defect classification]]
