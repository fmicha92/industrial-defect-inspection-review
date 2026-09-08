---
title: "Magnetic Tile Defects"
aliases:
  - "Magnetic Tile Defects"
  - "Magnetic Tile Defect Dataset"
  - "Magnetic tile defect datasets"
  - "Magnetic tile surface defects"
related_domain: "[[Metal inspection]]"
url: "https://github.com/abin24/Magnetic-tile-defect-datasets."
data_sources:
  - "GitHub"
  - "magnetic tile surface images"
introduced_by: "[[2020 - Surface Defect Saliency of Magnetic Tile]]"
related_papers:
  - "[[2020 - Surface Defect Saliency of Magnetic Tile]]"
  - "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
  - "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
  - "[[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]]"
  - "[[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]]"
---
# Magnetic Tile Defects

## Definition

Magnetic Tile Defects is a public magnetic-tile surface-defect dataset with pixel-level ground-truth annotations. The introducing paper reports 1344 cropped magnetic-tile ROI images collected under multiple illumination conditions and grouped into six defect/status classes: Blowhole, Crack, Fray, Break, Uneven, and Free.

## Dataset Details

- Host: [Magnetic-tile-defect-datasets.](https://github.com/abin24/Magnetic-tile-defect-datasets.)
- Repository structure: `MT_Blowhole`, `MT_Break`, `MT_Crack`, `MT_Fray`, `MT_Free`, and `MT_Uneven`.
- Labels: pixel-level ground truth.
- Images: 1344 cropped ROI images reported by the introducing paper.
- Splits: the introducing paper randomly uses 50% of each dataset for training and the rest for testing.
- Derived evaluation grouping: Blowhole and Crack are merged into `Blowhole&Crack`; all classes are assembled into an `All` dataset for combined evaluation.
- License: not reported.

## Why It Matters

Magnetic tiles have curved surfaces, changing illumination, and defect appearances that can be close to background texture. The dataset supports pixel-level [[Defect segmentation]] and saliency-based [[Metallic surface defect detection]] where low contrast and surface texture make labels and model robustness important.

## Used In These Papers

- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] evaluates DiffDD on Magnetic Tile and reports 68.41 mAP, 71.38 recall, 95.21 AUROC, 67.72 F1, and 59.44 IoU.

- [[2020 - Surface Defect Saliency of Magnetic Tile]] introduces the dataset and evaluates [[MCuePush U-Net]] for saliency-style defect segmentation and bounding-box localization.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] evaluates [[FDSNet]] on Magnetic Tile Defects for surface-defect segmentation.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses Magnetic Tile Defects as a source dataset for [[Industrial-5i]].
- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] uses or reports [[Magnetic Tile Defects]] for diffusion defect detection and surface defect detection.
- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] uses or reports [[Magnetic Tile Defects]] for defect synthesis and data augmentation.
- [[2022 - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables]] evaluates pseudo-anomalous latent-variable generation on Magnetic Tile Defects and reports ALGAN-image at 0.956 AUROC.
- [[2026 - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks]] uses LoRA-adapted diffusion augmentation for rare-class Magnetic Tile Defects classification, improving F1 from 0.051 to 0.296 at a 4x synthetic ratio.
- [[2024 - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection]] evaluates image-wise anomaly detection on Magnetic Tile Defects and reports 99.2% AUROC.

## Source Anchors

- Host source: [https://github.com/abin24/Magnetic-tile-defect-datasets.](https://github.com/abin24/Magnetic-tile-defect-datasets.)
- Requested source variant without the trailing dot returned 404 when checked on 2026-06-05: `https://github.com/abin24/Magnetic-tile-defect-datasets`.
- Paper caption URL variant: `https://github.com/abin24/Magnetic-tile-defectdatasets`.
- Introducing paper: [[2020 - Surface Defect Saliency of Magnetic Tile]].

## Related Concepts

- [[Metal inspection]]
- [[Metallic surface defect detection]]
- [[Surface defect detection]]
- [[Defect segmentation]]
- [[MCuePush U-Net]]
- [[U-Net]]
- [[F-measure]]
- [[Mean Absolute Error]]
