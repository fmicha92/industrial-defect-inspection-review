---
title: "Glass inspection"
aliases:
  - "Screen glass inspection"
  - "Smartphone screen glass inspection"
  - "Touch-screen glass inspection"
tags:
  - domain
---

# Glass inspection

## Definition

Glass inspection covers automated visual quality inspection of glass surfaces and glass products, including scratches, cracks, contamination, light leakage, and other visible production defects. [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] uses this domain for smartphone touch-screen glass defect localization.

## Scope Note

The method acronym [[GLASS]] refers to anomaly synthesis, not glass-surface inspection. It is not treated as evidence for this domain.

## Represented Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]]
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]
- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]]
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]]
- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]]
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]]

## Related Datasets

### Public

- [[AGDD]]
- [[Glass Defects]]
- [[Glass Bangle Defect Detection Classification]]
- [[MSD]]
- [[MVEP]]
- [[SSGD]]

### Private

- [[AuGD]]

### Availability Unspecified

- [[BBMP]]
- [[CGD]]
- [[Mobile Phone Flat Glass Defect Dataset]]
- [[OGD-DET]]
- [[RSGD]]

## Related Benchmarks

- [[OGD-DET benchmark]]
- [[SSGD benchmark]]

## Related Tasks

- [[Glass container defect detection]]
- [[Aircraft glass canopy defect detection]]
- [[Glass bangle defect classification]]
- [[Laminated glass defect detection]]
- [[Diverse glass surface defect detection]]
- [[Optical glass defect detection]]
- [[Smartphone screen glass defect detection]]

## Related Domains

- [[Semiconductor and electronics]]

## Related Concepts

- [[Surface defect detection]]
- [[Industrial visual inspection]]

## Used In These Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] supports optical-glass sub-millimeter defect detection with video-based multi-perspective inspection.
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] supports smartphone touch-screen glass production quality inspection with bounding-box defect annotations.
- [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] evaluates [[DY-YOLO]] for smartphone cover-glass defect detection on [[MSD]] and [[SSGD]].
- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] evaluates [[YOLOv5_zc]] with [[Poisson defect image augmentation]] and [[Total reflection grazing incidence combined lighting]] for mobile phone flat-glass defect detection.
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] evaluates [[CE-SGNet]] with attention and graph reasoning on [[SSGD]] smartphone screen defects.
- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] evaluates a lightweight YOLOv5 variant for automotive-glass defect detection on [[AuGD]].
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] evaluates DDPM-generated defective bottle images for supervised glass container defect classification on the MVTec AD bottle subset.
- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates [[IDD-Net]] on [[BBMP]], a glass-bottle bottom mold point production-line dataset.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] introduces [[MSD]] for pixel-level segmentation of mobile phone screen surface defects.
- [[AGDD]] supports aircraft glass canopy defect detection with paired forward-lighting and backward-lighting images.
- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] introduces [[AGDD]] and [[ADMF-Net]] for aircraft glass canopy defect detection.
- [[Glass Defects]] supports laminated-glass defect detection with YOLO-format bounding-box annotations.
- [[2023 - Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning]] introduces [[Glass Bangle Defect Detection Classification]] for three-class bangle quality inspection with factory-collected images.
- [[AuGD]], [[RSGD]], and [[CGD]] are referenced by the GSDNet repository for diverse glass surface defect detection.
