---
title: "VisA"
aliases:
  - "VisA"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://github.com/amazon-science/spot-diff"
data_sources:
  - "https://github.com/amazon-science/spot-diff"
  - "https://amazon-visual-anomaly.s3.us-west-2.amazonaws.com/VisA_20220922.tar"
introduced_by: "[[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]]"
related_papers:
  - "[[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]]"
availability: "public"
access: "AWS S3 download linked from the official Amazon Science spot-diff repository."
license: "CC-BY-4.0"
modalities:
  - "RGB images"
  - "pixel-level anomaly masks"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
---
# VisA

## Definition

VisA is an industrial anomaly detection and segmentation dataset with 10,821 high-resolution RGB images across 12 object subsets and three domains. The SPot-the-Difference paper reports 9,621 normal images, 1,200 anomalous images, image-level labels, and pixel-level anomaly annotations.

## Dataset Details

- Scope: 12 subsets grouped into complex structures, multiple-instance views, and roughly aligned single-instance objects.
- Complex structures: PCB1, PCB2, PCB3, and PCB4.
- Multiple instances: Capsules, Candles, Macaroni1, and Macaroni2.
- Single instances: Cashew, Chewing gum, Fryum, and Pipe fryum.
- Anomalies: surface defects such as scratches, dents, color spots, and cracks, plus structural defects such as misplacement and missing parts.
- Labels: the official repository reports image-level labels and pixel-level annotation masks; normal-image masks are not stored to save space.
- Evaluation splits: the repository includes split files and a preparation script for 1-class, 2-class high-shot, and 2-class few-shot setups.
- Access: public AWS S3 archive linked from the official Amazon Science repository.
- License: CC-BY-4.0 for the dataset.

## Why It Matters

VisA is a public multi-object industrial anomaly benchmark that complements MVTec AD with more complex structures, multiple-object scenes, object pose/location variation, and both image-level and pixel-level annotations.

## Used In These Papers

- [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]] introduces VisA and evaluates SPD pre-training on its 1-class, 2-class high-shot, and 2-class 5/10-shot anomaly detection and segmentation protocols.
- [[2025 - Accurate Industrial Anomaly Detection with Efficient Multimodal Fusion]] evaluates RGBD anomaly fusion on VisA using estimated depth and attention-guided synthetic perturbations, reporting 99.0 pixel AUROC and 80.5 AUPRO.
- [[2025 - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion]] compares pseudo-anomaly insertion schemes on VisA and reports [[Affine anomaly insertion]] at 91.4% AUROCpixel and 44.1% APpixel.
- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] reports 95.35% image-level and 98.43% pixel-level AUROC on VisA.

## Source Anchors

- Hosting source: https://github.com/amazon-science/spot-diff.
- Dataset archive: https://amazon-visual-anomaly.s3.us-west-2.amazonaws.com/VisA_20220922.tar.
- Introducing paper: [[2022 - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation]].

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]

- [[2023 - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization]] supports unsupervised anomaly localization, multi-class anomaly detection.

- [[2024 - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection]] supports few-shot anomaly detection, prompt learning.

- [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] supports multi-class anomaly detection, diffusion models.

- [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]] uses or reports [[VisA]] for realistic anomaly synthesis, feature selection.
- [[2024 - A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization]] uses or reports [[VisA]] for gradient ascent anomaly synthesis, industrial anomaly detection.
