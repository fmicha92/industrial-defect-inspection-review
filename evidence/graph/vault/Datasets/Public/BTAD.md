---
title: "BTAD"
aliases:
  - "BTAD"
  - "BeanTech"
  - "BeanTech Anomaly Detection"
  - "BeanTech AD"
related_domain: "[[Multi-industry anomaly detection]]"
url: "http://avires.dimi.uniud.it/papers/btad/btad.zip"
data_sources:
  - "AIVR Lab / University of Udine"
access: "public direct ZIP download"
licenses:
  - "not reported"
modalities:
  - "industrial RGB inspection images"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
introduced_by: "[VT-ADL: A Vision Transformer Network for Image Anomaly Detection and Localization](https://arxiv.org/abs/2104.10036)"
related_papers:
  - "[VT-ADL: A Vision Transformer Network for Image Anomaly Detection and Localization](https://arxiv.org/abs/2104.10036)"
  - "[[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]]"
  - "[[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]]"
---
# BTAD

## Definition

BTAD, the BeanTech Anomaly Detection dataset, is a real-world industrial image anomaly dataset for unsupervised anomaly detection and localization across three industrial product categories.

## Why It Matters

The dataset is commonly used as a compact industrial anomaly-detection benchmark with normal-only training images and mixed normal/anomalous test images. It complements larger multi-category benchmarks such as [[MVTec AD]], [[MPDD]], and [[VisA]].

## Dataset Details

- Host: public BTAD ZIP at the AIVR Lab / University of Udine host.
- Alternate host noted by RealNet: Google Drive mirror in the RealNet repository.
- Dataset name: BeanTech Anomaly Detection dataset.
- Modality: real-world industrial product images.
- Product categories: 3 industrial products.
- Scale: survey sources report 2,830 real-world images; FastFlow reports 2,540 images. The discrepancy is preserved as source-specific.
- Defect Spectrum subset/view: Defect Spectrum reports 290 BeanTech images across 3 labels in its comparison table, which is kept as a source-specific subset or annotation view rather than a replacement for the broader BTAD count.
- Training split: normal images only.
- Test split: mixture of normal and abnormal images.
- Training images by product reported in the 2023 industrial-image anomaly-detection survey: product 0 has 400, product 1 has 1,000, and product 2 has 399 training images.
- Labels/annotations: used for image anomaly detection and pixel-level anomaly localization; exact mask format is not reported in the checked host/source text.
- Access: public direct ZIP download; the ZIP responded with HTTP 200 on 2026-06-09.
- License: not reported in the checked host/source text.

## Used In These Papers

- [VT-ADL: A Vision Transformer Network for Image Anomaly Detection and Localization](https://arxiv.org/abs/2104.10036) introduces BTAD as a real-world industrial anomaly dataset.
- [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]] uses or reports [[BTAD]] for realistic anomaly synthesis, feature selection.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[BTAD]] for industrial defect benchmarking and semantic defect annotation under the BeanTech name.
- [[2023 - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples]] evaluates synthetic anomaly simulation on BTAD and reports an improvement over VT-ADL.
- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] reports 95.5% image-level and 97.4% pixel-level AUROC on BTAD.
- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] reports 97.70% average pixel-level AUROC on BTAD.
- [[2024 - CAGEN Controllable Anomaly Generator Using Diffusion Model]] evaluates CAGen-generated anomaly augmentation on BTAD and reports mean localization AUROC/AP of 91.2/26.3 versus DRAEM's 88.3/20.3.

## Source Anchors

- Hosting source: [BTAD direct ZIP](http://avires.dimi.uniud.it/papers/btad/btad.zip).
- Mirror/source mention: [RealNet repository](https://github.com/cnulab/RealNet).
- Introducing paper: [VT-ADL: A Vision Transformer Network for Image Anomaly Detection and Localization](https://arxiv.org/abs/2104.10036).
- Related source: [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]].
- Related source: [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]].

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
