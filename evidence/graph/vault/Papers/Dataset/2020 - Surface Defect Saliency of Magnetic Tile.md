---
title: "Surface Defect Saliency of Magnetic Tile"
aliases:
  - "Saliency of magnetic tile surface defects"
paper_key: "doi:10.1007/s00371-018-1588-5"
doi: "10.1007/s00371-018-1588-5"
url: "https://doi.org/10.1007/s00371-018-1588-5"
pdf: "paper-inbox/10_processed/Dataset/2020 - Huang - Surface Defect Saliency of Magnetic Tile.pdf"
source_file: "paper-inbox/10_processed/Dataset/2020 - Huang - Surface Defect Saliency of Magnetic Tile.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Huang - Surface Defect Saliency of Magnetic Tile.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Huang - Surface Defect Saliency of Magnetic Tile.txt"
authors:
  - "Yibin Huang"
  - "Congying Qiu"
  - "Kui Yuan"
year: 2020
venue: "The Visual Computer"
paper_type: "dataset"
status: "processed"
processed_at: "2026-06-05"
topics:
  - "magnetic tile surface defects"
  - "saliency detection"
  - "industrial visual inspection"
tasks:
  - "[[Defect segmentation]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Magnetic Tile Defects]]"
methods:
  - "[[MCuePush U-Net]]"
  - "[[U-Net]]"
model_family:
  - "[[Segmentation Models]]"
architectures:
  - "[[U-Net]]"
losses:
  - "Softmax cross-entropy"
optimizers:
  - "SGD with momentum"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F-measure]]"
  - "[[AU-ROC]]"
  - "[[Mean Absolute Error]]"
primary_metric: "[[F-measure]]"
baselines:
  - "ITTI"
  - "BMS"
  - "FT"
  - "LC"
  - "HC"
  - "AC"
  - "MSS"
  - "SR"
  - "Rudinac"
  - "PHOT"
  - "RC"
  - "SF"
  - "GMR"
  - "MBP"
code: "https://github.com/abin24/Saliency-detection-toolbox"
data: "https://github.com/abin24/Magnetic-tile-defect-datasets."
artifact_status: "data and saliency toolbox reported"
related_methods:
  - "[[MCuePush U-Net]]"
  - "[[U-Net]]"
related_datasets:
  - "[[Magnetic Tile Defects]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Metallic surface defect detection]]"
---
# Surface Defect Saliency of Magnetic Tile

## Summary

The paper introduces [[Magnetic Tile Defects]], a pixel-labeled magnetic-tile surface-defect dataset, and proposes [[MCuePush U-Net]] for saliency-style defect segmentation with optional bounding-box localization. The method combines MCue saliency preprocessing, a U-Net segmentation model, and a Push network that predicts a defect bounding box for single-defect images.

## Paper Type

Dataset-introducing research paper. The paper contributes both a public magnetic-tile defect dataset and a model for real-time defect saliency detection.

## Problem

Magnetic tile surface defects are difficult to segment because a tile can have multiple curved surfaces, defect shapes vary, illumination changes, and several defect appearances are close to background texture. The paper targets pixel-level defect segmentation and explicit location output for industrial magnetic-tile inspection.

## Contribution

- Introduces [[Magnetic Tile Defects]] with 1344 cropped ROI images, six defect/status classes, and pixel-level ground-truth labels.
- Proposes [[MCuePush U-Net]], combining MCue saliency cues, U-Net segmentation, and a Push network for bounding-box localization.
- Reports faster processing than earlier hand-crafted saliency approaches, reducing average processing time from about 0.5 s per image to 0.07 s per image.

## Dataset

[[Magnetic Tile Defects]] contains magnetic-tile ROI images grouped into Blowhole, Crack, Fray, Break, Uneven, and Free classes. The paper reports that each dataset has pixel-level labels, that images are captured under multiple illumination conditions, and that 50% of images from each dataset are randomly selected for training while the rest are used for testing. Blowhole and Crack are also merged into `Blowhole&Crack`, and all classes are assembled into an `All` evaluation set.

## Method

The model input is built from MCue saliency information and raw image channels. MCue combines cues from darker regions, structure tensor features, local color rarity, texture suppression, and visual attention. The U-Net component performs dense foreground/background prediction. The Push network contains two fully connected layers and an output layer that predicts bounding-box coordinates for a single defect region.

Training uses Softmax cross-entropy for foreground/background segmentation. The Push network uses a Euclidean bounding-box loss and does not update when an image contains more than one defect or no defect region. The paper reports SGD with momentum 0.9, learning rate 0.0001, mini-batch size 8, 400 iterations per epoch, and 42,000 training iterations taking about 10 hours on an Intel i7 laptop with 8 GB RAM and a GTX 1050Ti GPU.

The data augmentation pipeline uses moving least squares deformation with 5 x 5 grids and Delaunay triangulation, followed by regular transformations such as rotation, translation, zoom, and shear. The paper reports about 31,000 training images and labels after augmentation.

## Evidence

The paper evaluates on the magnetic-tile classes and combined sets using saliency and segmentation metrics. It compares MCuePush U-Net with U-Net, deformable U-Net, MCue variants, and 14 saliency models from the saliency toolbox. The reported qualitative pattern is that existing saliency models vary by defect class, while MCuePush U-Net improves localization and speed for the magnetic-tile setting.

## Performance Metrics

- [[Precision]]: reported for saliency/foreground detection.
- [[Recall]]: reported for saliency/foreground detection.
- [[F-measure]]: reported with beta squared equal to 0.3.
- [[AU-ROC]]: reported via ROC/AUC evaluation.
- [[Mean Absolute Error]]: reported as MAE for saliency-map error.
- Runtime: MCuePush U-Net is reported at 0.07 s per image; the paper contrasts this with 0.7 s for deformable U-Net and about 0.5 s average for earlier wavelet/curvelet/shearlet-style saliency approaches.

## ML/DL Extraction

- Task formulation: pixel-level magnetic-tile defect saliency and segmentation, with optional single-defect bounding-box localization.
- Inputs: cropped magnetic-tile ROI images, resized for model input; MCue saliency images and raw image channels.
- Output: foreground/background segmentation map; optional bounding box from the Push network.
- Architecture: MCue preprocessing, U-Net segmentation backbone, and Push localization branch.
- Objective: Softmax cross-entropy for segmentation and Euclidean bounding-box loss for Push localization.
- Optimizer: SGD with momentum 0.9.
- Training recipe: learning rate 0.0001, mini-batch size 8, 400 iterations per epoch, and 42,000 iterations reported.
- Compute: Intel i7 7th-generation CPU, 8 GB RAM, GTX 1050Ti GPU; about 10 hours for the reported training run.
- Artifacts: dataset host and saliency toolbox are reported.

## Limitations

- Pixel-level labeling is expensive, motivating the paper's augmentation pipeline.
- The Push network is limited to single-defect images during training; it does not update for images with more than one defect or no defect region.
- Uneven defects are reported as difficult because their color and texture can be close to background.
- License terms for the hosted dataset are not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Metallic surface defect detection]]
- Methods: [[MCuePush U-Net]], [[U-Net]]
- Datasets: [[Magnetic Tile Defects]]
- Domains: [[Metal inspection]]
- Metrics: [[Precision]], [[Recall]], [[F-measure]], [[AU-ROC]], [[Mean Absolute Error]]

### Shares Dataset

- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] also evaluates surface-defect segmentation on [[Magnetic Tile Defects]].
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses Magnetic Tile Defects as a source dataset for [[Industrial-5i]].

### Shares Task

- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] also studies pixel-level metal surface defect segmentation, but on [[NEU-SEG]] rather than magnetic tiles.

### Shares Method

- [[U-Net]] is the segmentation backbone family used by MCuePush U-Net.

## Questions

- The resolving GitHub repository has no license metadata; reuse conditions need confirmation before redistribution.
- The paper URL printed for the dataset differs from the resolving GitHub repository name; cite the DOI and the resolving host together when provenance matters.
