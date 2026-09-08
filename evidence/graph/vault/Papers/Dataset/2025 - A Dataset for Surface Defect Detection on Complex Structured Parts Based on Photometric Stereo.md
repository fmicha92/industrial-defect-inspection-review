---
title: "A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo"
aliases:
  - "A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo"
paper_key: "doi:10.1038/s41597-025-04454-6"
paper_type: dataset
year: 2025
venue: "Scientific Data"
authors:
  - "Lin Wu"
  - "Yu Ran"
  - "Li Yan"
  - "Yixing Liu"
  - "You Song"
  - "Dongran Han"
status: processed
processed_at: 2026-05-21
topics:
  - "surface defect detection"
  - "photometric stereo"
  - "casting metal inspection"
tasks:
  - "[[Casting surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[MSDD]]"
  - "[[NEU-DET]]"
  - "[[GC10-DET]]"
methods:
  - "[[Photometric stereo]]"
  - "[[Stroboscopic Illuminant Image Acquisition]]"
  - "[[Taylor Series Channel Mixer]]"
  - "[[Phase-Invariant Feature Module]]"
  - "[[YOLOv5]]"
  - "[[YOLOv8]]"
  - "[[FCOS]]"
  - "[[RT-DETR]]"
model_family:
  - "[[Object detection]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[mAP]]"
  - "[[Average precision]]"
  - "MSE"
  - "PSNR"
  - "[[SSIM]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP50: mean Average Precision at IoU threshold 0.50 for defect detection."
  - "MSE, PSNR, and SSIM: reconstruction-quality metrics used to compare image-mixing variants."
baselines:
  - "Static mixed RGB images"
  - "Direct n-channel original images"
  - "FCOS + ATSS"
  - "YOLOv5-m6"
  - "YOLOv8-m"
  - "YOLOv8-l"
  - "RT-DETR-l"
benchmarks:
  - "[[MSDD]]"
code: "https://github.com/Destinyia/Metal-SurfaceDefect-Detection"
data: "https://doi.org/10.57760/sciencedb.10794"
doi: "10.1038/s41597-025-04454-6"
url: "https://doi.org/10.1038/s41597-025-04454-6"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Photometric stereo]]"
  - "[[Stroboscopic Illuminant Image Acquisition]]"
  - "[[Taylor Series Channel Mixer]]"
  - "[[Phase-Invariant Feature Module]]"
related_datasets:
  - "[[MSDD]]"
  - "[[NEU-DET]]"
  - "[[GC10-DET]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Casting surface defect detection]]"
  - "[[Object detection]]"
source_file: "paper-inbox/10_processed/2025 - Wu - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Wu - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Wu - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo.txt"
artifact_status: "dataset and technical-validation code available"
tags:
  - paper
---

# A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo

## Summary

Wu et al. introduce [[MSDD]], the Metal Surface Defect Dataset, for detecting surface defects on non-planar casting metal parts. The dataset is built from multi-angle illumination images captured with a stroboscopic illuminant setup and mixed into RGB pseudo-color images that preserve depth-related cues from [[Photometric stereo]].

The paper also proposes a validation pipeline around [[Stroboscopic Illuminant Image Acquisition]], [[Taylor Series Channel Mixer]], and [[Phase-Invariant Feature Module]]. On MSDD, the best reported detector is YOLOv8-l with 0.854 mAP50, while YOLOv8-m is described as nearly as accurate and faster.

## Paper Type

- Type: dataset.
- Why: The central contribution is a publicly hosted dataset, with method and detector experiments used as technical validation.

## Problem

- Task: [[Casting surface defect detection]] with bounding-box object detection.
- Setting: gravity-cast metal parts with complex 3D structures, shadows, stains, low reflectivity, and lighting-angle sensitivity.
- Inputs: multi-angle strobe-illumination images and mixed RGB pseudo-color images.
- Outputs: defect class and bounding-box location.
- Motivation: static 2D AOI can confuse shadows and stains with defects, while conventional 3D scanning methods can be too slow, expensive, or narrow in field of view for online inspection.
- Assumptions: the paper frames photometric-stereo-derived pseudo-color imaging as a practical compromise for non-planar metal inspection.

## Contribution

- Claimed: proposes a real-time 3D imaging defect detection framework based on photometric stereo and deep learning.
- Claimed: introduces [[MSDD]], an aluminum casting surface defect dataset with eight defect types.
- Claimed: maps color-space transformations to spatial-domain illuminant transformations and uses hue randomization for data augmentation.
- Shown: FCOS, YOLOv5, YOLOv8, and RT-DETR can be trained on MSDD, with improved mixed-image/PIFM configurations outperforming static mixing and direct n-channel training.

## Method

The imaging pipeline starts with [[Stroboscopic Illuminant Image Acquisition]], where multiple illuminants flash sequentially around the part while six cameras capture images from different lighting directions. The paper reports that each camera works with the illuminants at 30 FPS and that the full acquisition can complete within 0.96 seconds, matching a 300-pieces-per-hour aluminum alloy casting line.

[[Taylor Series Channel Mixer]] combines multi-angle single-channel images into RGB pseudo-color images. The mixer is trained with a VQ-VAE-style reconstruction objective using MSE, SSIM, vector-quantizer, and commitment losses. The optional [[Phase-Invariant Feature Module]] learns lighting-angle-invariant shallow features and can replace early detector backbone stages.

## Evidence

### Dataset / Benchmark Details

- Dataset: [[MSDD]].
- Host: ScienceDB / Science Data Bank.
- Access: public; ScienceDB metadata reports `conditionsOfAccess: PUBLIC`.
- License: Creative Commons Attribution 4.0 International, from ScienceDB structured metadata.
- Data volume: 138,585 single-channel images and 9,239 mixed RGB pseudo-color images.
- ScienceDB description: 5,746 defect-free images and 3,493 images with defects.
- Paper-reported annotated set: 9,332 annotated images.
- Collection: 1,507 defective metal parts captured under multiple lighting conditions by six cameras.
- Image size: 640 x 640 patches after sliding-window preprocessing with 15% overlap.
- Defect classes: Misrun, Inclusion, Dent, Parting line crack, Stamp collapse, Pockmarks, Mould scuffing, and Cut marks.
- Annotation: VOC files with filename, dimensions, defect category, and bounding box.
- Annotation protocol: two trained inspectors independently annotated defects; boxes with IoU above 0.8 were averaged, and lower-agreement boxes went to a quality supervisor.
- Split for technical validation: 4:1 training/testing split.

### Main Results

| Result | Dataset / Task | Metric | Direction | Method | Paper result | Notes |
|---|---|---|---|---|---:|---|
| Best reported detector | [[MSDD]] / [[Casting surface defect detection]] | [[mAP@0.50]] | higher | YOLOv8-l | 0.854 | Best all-class mAP50 reported in the model comparison table. |
| Best practical detector claim | [[MSDD]] / [[Casting surface defect detection]] | [[mAP@0.50]] and speed | higher/faster | YOLOv8-m | near YOLOv8-l accuracy | The paper says YOLOv8-m is almost identical in accuracy to YOLOv8-l but faster. |
| TSCM reconstruction effect | [[MSDD]] image mixing | PSNR | higher | TSCM | +6.02 to +6.03 | Compared with simpler mixing variants in ablation. |
| Vector quantization effect | [[MSDD]] defect detection | [[mAP@0.50]] | higher | vector quantization layer | +1.6 percentage points | Improves detection precision with little effect on reconstruction quality. |
| PIFM/phase-shift effect | [[MSDD]] defect detection | Average precision | higher | PIFM with phase-shift transformations | +4.1 to +5.5 percentage points | Improvement over static mixing scheme across object detectors. |
| End-to-end optimization effect | [[MSDD]] defect detection | Average precision | higher | end-to-end channel mixer optimization | +1.1 to +2.1 percentage points | Additional gain after PIFM/phase-shift improvement. |
| Strong class-level gain | [[MSDD]] / dent and inclusion defects | Average precision | higher | phase-shift transformation | up to +18.7 percentage points | Reported for defects with variable positions and strong illuminant-angle sensitivity. |

### Comparison With Existing Datasets

| Dataset | Gray images | RGB images | Image size | Structural complexity |
|---|---:|---:|---|---|
| [[NEU-DET]] | 1,800 | not applicable | 200 x 200 | Plane |
| [[GC10-DET]] | 2,280 | not applicable | 2048 x 1000 | Plane |
| [[MSDD]] | 149,312 | 9,332 | 640 x 640 | Non-plane |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP@0.50]] | Defect detection on MSDD | mean Average Precision at IoU threshold 0.50 | Higher is better | yes | YOLOv8-l reaches 0.854 all-class mAP50; TSCM/vector-quantization ablation ranges from 0.759 to 0.784. |
| MSE | Reconstruction error for image mixing | Mean squared error on test reconstruction | Lower is better | no | TSCM variants report 0.00015 and 0.00014 in Table 3. |
| PSNR | Reconstruction quality for image mixing | Peak signal-to-noise ratio | Higher is better | no | TSCM variants report 38.24 and 38.54 in Table 3. |
| [[SSIM]] | Reconstruction quality for image mixing | Structural similarity index | Higher is better | no | TSCM variants report 0.0299 and 0.0287 in Table 3; the paper treats these as reconstruction-comparison values. |

## ML / DL Extraction

### Task Formulation

- Input modality: multi-angle illuminated single-channel images and mixed RGB pseudo-color images.
- Output target: bounding-box object detection over defect categories.
- Supervision: supervised detection with inspector-reviewed bounding-box annotations.
- Objective: build and validate a dataset and imaging pipeline for defect detection on non-planar metal casting surfaces.

### Model And Training

- Detector families: FCOS + ATSS, YOLOv5-m6, YOLOv8-m, YOLOv8-l, and RT-DETR-l.
- Imaging modules: [[Stroboscopic Illuminant Image Acquisition]], [[Taylor Series Channel Mixer]], and [[Phase-Invariant Feature Module]].
- Reconstruction optimization: VQ-VAE-style autoencoder with MSE loss, SSIM loss, vector quantizer loss, and commitment loss.
- Framework: PyTorch 1.10.1; Ultralytics used for rapid detector construction, but the paper says it is not essential.
- Hardware: Intel Xeon Silver 4110 CPU at 2.10 GHz, 32 GB memory, 24 GB NVIDIA GeForce 3090 GPU, Windows 10.
- Training details not reported: seeds, full hyperparameter grid, and training time.

### Data

- Data source: aluminum casting parts.
- Preprocessing: high-resolution images were cut into 640 x 640 patches using a sliding window with 15% overlap; images were slightly distorted, scaled, and sheared to obscure true product dimensions and shapes.
- Privacy/commercial protection: logos and identifying marks were removed.
- Data augmentation in usage notes: Translate, Scale, Mosaic, Random-Affine, MixUp, Augment HSV, and Horizontal Flip are reported as effective.
- License: Creative Commons Attribution 4.0 International for the ScienceDB dataset; code uses Apache-2.0 according to the paper.

## Limitations

- Stated: SIIA struggles with highly reflective surfaces because complex light-source arrangements can create reflections that obscure defects.
- Stated: the dataset is imbalanced, with some defect categories underrepresented.
- Stated: future work should collect more diverse samples, test non-metallic surfaces such as wood, leather, and fabric more thoroughly, and improve detection accuracy for industrial requirements.
- Inferred from the validation table: misrun and pockmarks were excluded from the main detector comparison because their sample sizes were too small for statistically meaningful comparison.

## Reproducibility

- Data: https://doi.org/10.57760/sciencedb.10794 and https://www.scidb.cn/en/detail?dataSetId=3d739ddb4bdc439a9bf7ef550cae48d8.
- Code: https://github.com/Destinyia/Metal-SurfaceDefect-Detection.
- Code license: Apache-2.0, as reported in the paper.
- Demo scripts: `train_tscm.py`, `train_pifm.py`, and `train_detector.py`.
- Dataset structure: `OrigImages`, `JPEGImages`, and `Annotations`.
- Artifact status: dataset and technical-validation code available.

## Connections

### Graph Hubs

- Tasks: [[Casting surface defect detection]], [[Object detection]]
- Methods: [[Photometric stereo]], [[Stroboscopic Illuminant Image Acquisition]], [[Taylor Series Channel Mixer]], [[Phase-Invariant Feature Module]]
- Datasets: [[MSDD]], [[NEU-DET]], [[GC10-DET]]
- Domains: [[Metal inspection]]
- Metrics: [[mAP@0.50]], [[mAP]], [[Average precision]], [[SSIM]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] | Shares task/domain | Both introduce casting-surface defect datasets for metal inspection, but MSDD emphasizes photometric-stereo pseudo-color imaging for non-planar parts. |
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Contrasts dataset | GC10-DET is used as a planar metallic-surface comparison point against MSDD's non-planar casting-parts setting. |

### Connection Rationale

- [[MSDD]] is the central dataset introduced and technically validated.
- [[Photometric stereo]] is central because the imaging setup uses multi-angle illumination to recover depth-related cues that help distinguish shadows, stains, and concave defects.
- [[mAP@0.50]] is the primary reported detector metric.
- [[Metal inspection]] is the supported domain because the dataset covers casting-formed metal blank surface defects.

## Questions

- What is the exact per-class distribution for all eight defect categories?
- How do the reported validation results change when the rare misrun and pockmarks categories are included?
- Are the distorted/scaled/sheared images sufficient to reproduce the original deployment geometry constraints?
