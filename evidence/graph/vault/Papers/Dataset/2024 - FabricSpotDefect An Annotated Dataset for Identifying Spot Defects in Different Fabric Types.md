---
title: "FabricSpotDefect: An annotated dataset for identifying spot defects in different fabric types"
aliases:
  - "FabricSpotDefect dataset paper"
paper_key: "doi:10.17632/6574nhzm8x.1"
paper_type: dataset
year: 2024
venue: "Data in Brief"
authors:
  - "Farzana Islam"
  - "Sumaya"
  - "Md Fahad Monir"
  - "Ashraful Islam"
status: processed
processed_at: 2026-05-27
topics:
  - textile inspection
  - fabric spot defects
  - computer vision
  - data augmentation
  - object detection annotations
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "fabric spot-defect detection for textile quality control"
datasets:
  - "[[FabricSpotDefect]]"
dataset_sizes:
  - "1014 raw RGB images"
  - "3288 original spot annotations"
  - "2300 augmented images"
  - "7641 YOLOv8 annotations"
  - "7635 COCO annotations"
splits:
  - "Original: 643 train images, 219 validation images, 152 test images"
  - "Augmented: 1929 train images, 219 validation images, 152 test images"
modalities:
  - "RGB JPG fabric images"
methods:
  - "[[Data augmentation]]"
model_family: []
architectures: []
losses: []
training_regime: "not applicable"
augmentation:
  - "horizontal and vertical flips"
  - "90 degree clockwise and counter-clockwise rotations"
  - "horizontal and vertical shear within +/-15 degrees"
  - "saturation adjustment from -25% to +25%"
  - "brightness adjustment from -25% to +25%"
  - "noise addition up to 5.03% of pixels"
synthetic_data: "augmented images generated from original fabric images using RoboFlow transformations"
metrics: []
primary_metric: "not applicable"
metric_definitions: []
baselines: []
benchmarks: []
evaluation_protocol: "not applicable; the article describes a dataset and split structure but does not train or evaluate a model"
parameters: "not applicable"
compute: "not applicable"
hardware: "Samsung Galaxy Note20, Samsung Galaxy S20 FE, and Samsung Galaxy A53 5G smartphones"
training_time: "not applicable"
inference_cost: "not applicable"
url: "https://doi.org/10.1016/j.dib.2024.111165"
pdf: "paper-inbox/10_processed/Dataset/2024 - Islam - FabricSpotDefect An annotated dataset for identifying spot defects in different fabric types.pdf"
code: "not reported"
data: "https://data.mendeley.com/datasets/6574nhzm8x/1"
doi: "10.1016/j.dib.2024.111165"
arxiv: "not reported"
related_papers:
  - "[[2025 - Dataset for Defect Detection in Textile Manufacturing]]"
  - "[[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]"
  - "[[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]"
  - "[[2019 - A Public Fabric Database for Defect Detection Methods and Results]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Data augmentation]]"
related_datasets:
  - "[[FabricSpotDefect]]"
  - "[[Batavia and Sarga woven fabric images]]"
  - "[[Lusitano]]"
  - "[[ZJU-Leaper]]"
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks: []
concept_notes_created_or_updated:
  - "[[FabricSpotDefect]]"
source_file: "paper-inbox/10_processed/Dataset/2024 - Islam - FabricSpotDefect An annotated dataset for identifying spot defects in different fabric types.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Islam - FabricSpotDefect An annotated dataset for identifying spot defects in different fabric types.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Islam - FabricSpotDefect An annotated dataset for identifying spot defects in different fabric types.txt"
artifact_status: "dataset public on Mendeley Data; code not reported"
tags:
  - paper
  - dataset
  - textile-inspection
---

# FabricSpotDefect: An annotated dataset for identifying spot defects in different fabric types

## Summary

- Introduces [[FabricSpotDefect]], a public RGB image dataset for detecting spot defects across different fabric types.
- Provides 1014 raw images with 3288 manually created spot annotations, plus 2300 augmented images exported in COCO and YOLOv8 formats.
- The paper is a dataset description rather than a model evaluation study; it reports capture devices, annotation process, train/validation/test splits, preprocessing, augmentation, and limitations.

## Paper Type

- Type: dataset paper.
- Why: The central contribution is a public annotated fabric spot-defect dataset, not a new model or experimental benchmark result.

## Problem

- Task: [[Textile defect detection]] and spot localization using bounding boxes or polygons.
- Setting: textile quality control for varied fabric types under ordinary indoor image-capture conditions.
- Inputs: RGB fabric images resized to 416 x 416 pixels.
- Outputs: one defect class, `Spot`, with bounding-box or polygon annotations.
- Motivation: manual textile inspection is fatigue-prone and subjective, while patterned and colorful fabrics make spot defects difficult to identify by eye.
- Assumptions: a single spot-defect class is useful for training ML models to detect diverse spot appearances regardless of their specific source.

## Contribution

- Claimed: The dataset is designed specifically for fabric spot detection across varied fabric types and spot appearances.
- Shown: The original data contain 1014 RGB images and 3288 manually annotated spot defects.
- Shown: The augmented data include 2300 additional images with 7641 YOLOv8 annotations and 7635 COCO annotations.
- Shown: The data are publicly available through Mendeley Data with DOI 10.17632/6574nhzm8x.1.
- Inferred: The dataset is most directly useful for object detection or localization workflows because it provides bounding boxes and polygon annotations rather than only image-level labels.

## Method

- Core idea: capture fabric spot images using smartphones, annotate spot defects in RoboFlow, resize images to a common 416 x 416 resolution, and export original and augmented versions for ML use.
- Data acquisition: images were captured using Samsung Galaxy Note20, Samsung Galaxy S20 FE, and Samsung Galaxy A53 5G smartphones under natural or ordinary indoor lighting.
- Annotation: spots such as stains, discoloration, oil marks, and irregular patches were labeled with bounding boxes and, for some samples, polygon annotations.
- Preprocessing: RoboFlow auto-orient removed EXIF orientation inconsistency; images were resized to 416 x 416 pixels using stretch resizing.
- Augmentation: only training data were augmented with flips, 90 degree rotations, shear, saturation adjustment, brightness adjustment, and noise.
- Export formats: original images use COCO-format labels; augmented data are provided in COCO and YOLOv8 formats.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB JPG fabric images.
- Output target: one `Spot` class with bounding-box or polygon localization.
- Supervision: manual annotations on original images; augmented versions inherit transformed annotations.
- Objective: support ML models that detect fabric spot defects for quality control.

### Model And Training

- Model family: not applicable.
- Architecture: not applicable.
- Parameters: not applicable.
- Pretraining: not applicable.
- Fine-tuning: not applicable.
- Losses: not applicable.
- Optimizer: not applicable.
- Hyperparameters: not applicable.
- Seeds: not applicable.
- Training compute: not applicable.

### Data

- Datasets: [[FabricSpotDefect]].
- Data source: available fabrics photographed in Dhaka, Bangladesh.
- Dataset size: 1014 raw images; 2300 augmented images.
- Labels / annotations: one class named `Spot`; original images have 3288 spot annotations.
- Splits: original split has 643 train, 219 validation, and 152 test images; augmented split has 1929 train, 219 validation, and 152 test images.
- Preprocessing: auto-orient and stretch resize to 416 x 416 pixels.
- Augmentation: flips, rotations, shear, saturation adjustment, brightness adjustment, and noise.
- Synthetic data: augmented training images only; no generative or simulated data reported.
- Leakage checks: the paper states RoboFlow assigns each image uniquely to train, validation, or test with no overlap, and augmentation occurs after the original split.
- License: article is CC BY; dataset-specific license is not separately reported in the extracted text.

### Evaluation

- Protocol: not applicable.
- Model evaluation metrics: not applicable.
- Primary metric: not applicable.
- Metric direction / units: not applicable.
- Baselines: not applicable.
- Benchmarks: not applicable.
- Statistical tests: not applicable.
- Failure cases: not applicable.

## Evidence

### Experimental Setup

- Datasets: [[FabricSpotDefect]].
- Splits: train, validation, and test splits are provided for original and augmented versions.
- Baselines: not applicable.
- Model evaluation metrics: not applicable.
- Compute: not applicable.
- Hardware: Samsung Galaxy Note20, Galaxy S20 FE, and Galaxy A53 5G smartphones.
- Training time: not applicable.
- Inference cost: not applicable.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Original images | [[FabricSpotDefect]] / [[Textile defect detection]] | count | higher | not applicable | 1014 | Raw RGB images. |
| Original annotations | [[FabricSpotDefect]] / [[Defect segmentation]] | count | higher | not applicable | 3288 | Bounding-box and polygon spot annotations. |
| Augmented images | [[FabricSpotDefect]] / [[Textile defect detection]] | count | higher | not applicable | 2300 | Additional training-focused augmented images. |
| YOLOv8 annotations | [[FabricSpotDefect]] / [[Defect segmentation]] | count | higher | not applicable | 7641 | Exported annotation format for YOLOv8 workflows. |
| COCO annotations | [[FabricSpotDefect]] / [[Defect segmentation]] | count | higher | not applicable | 7635 | Exported annotation format for COCO-compatible workflows. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| not applicable | not applicable | not applicable | not applicable | not applicable | The article does not report model performance metrics. |

### Ablations

- Not applicable.

## Dataset / Benchmark Details

- Source: daily-use home clothes and other available fabrics.
- Collection: smartphone photography under natural and household lighting.
- Annotation: RoboFlow bounding boxes and polygon annotations for spot defects.
- Size: 1014 original images, 3288 original annotations, 2300 augmented images.
- Classes: one class, `Spot`.
- Splits: 643/219/152 original train/validation/test images; augmented train grows to 1929 images.
- Modalities: 2D RGB JPG images.
- Artifact: https://data.mendeley.com/datasets/6574nhzm8x/1.
- License: article is CC BY; dataset-specific license is not separately reported.
- Leakage risks: augmentation after splitting reduces train/test overlap risk, but exact grouping by source fabric or capture session is not reported.
- Bias / coverage: images come from stationary fabrics under household lighting rather than moving industrial production lines; no non-defect fabric images are included.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: image quality can vary because of smartphone-specific capture settings, zoom, noise, or blur.
- Stated: augmentation may not cover all real-world defect patterns.
- Stated: household lighting may not reflect industrial lighting conditions.
- Stated: the dataset contains limited-quality spot-defect images and no non-defect fabric images, which can make defect versus non-defect discrimination difficult.
- Stated: stationary fabric images may not transfer directly to production environments where fabrics are moving.
- Stated: intricate patterns or similar shades may confuse model performance.

## Reproducibility

- Code: not reported.
- Data: https://data.mendeley.com/datasets/6574nhzm8x/1.
- Hyperparameters: not applicable.
- Random seeds: not applicable.
- Environment: RoboFlow is used for annotation, preprocessing, splitting, augmentation, and export.
- Checkpoints / models: not applicable.
- Exact preprocessing: RoboFlow auto-orient and stretch resize to 416 x 416 pixels.
- Artifact status: dataset public on Mendeley Data; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect segmentation]]
- Datasets: [[FabricSpotDefect]], [[Batavia and Sarga woven fabric images]], [[Lusitano]], [[ZJU-Leaper]], [[AITEX]]
- Methods: [[Data augmentation]]
- Metrics: not applicable
- Domains: [[Textile and fiber inspection]], [[Industrial visual inspection]]
- Benchmarks: not applicable

### Builds On

- not reported.

### Contrasts With

- [[2025 - Dataset for Defect Detection in Textile Manufacturing]]: both are Data in Brief textile datasets, but FabricSpotDefect targets one-class spot localization with COCO/YOLOv8 exports, while Batavia/Sarga provides case/control patch data for woven fabric defects.
- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]: Lusitano emphasizes factory-collected anomaly detection with normal training images, while FabricSpotDefect emphasizes spot annotations on varied everyday fabrics.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]: ZJU-Leaper is much larger and benchmark-oriented, while FabricSpotDefect focuses on a single spot class and export-ready annotation formats.

### Shares Dataset

- [[FabricSpotDefect]]: introduced by this paper.

### Shares Task

- [[Textile defect detection]]: the dataset targets fabric spot-defect detection.
- [[Defect segmentation]]: polygon and bounding-box annotations localize spot defects.

### Shares Method

- [[Data augmentation]]: the paper uses RoboFlow flips, rotations, shear, saturation, brightness, and noise to enlarge the training data.

### Shares Metric

- not applicable.

### Application / Domain

- [[Textile and fiber inspection]]: the data support textile quality control.
- [[Industrial visual inspection]]: the paper frames the dataset as a resource for automated visual quality inspection.

### Follow-Up Reading

- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]: useful for richer fabric defect benchmark protocols and annotation regimes.
- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]: useful for one-class fabric anomaly detection under factory collection conditions.
- [[2025 - Dataset for Defect Detection in Textile Manufacturing]]: useful for another recent Data in Brief textile dataset with patch labels.

## Questions

- What dataset license applies on Mendeley Data beyond the article's CC BY license?
- Are source-fabric identifiers available to prevent leakage across visually similar fabric captures?
- How should models trained only on spot-defect images handle defect-free fabrics at deployment time?
