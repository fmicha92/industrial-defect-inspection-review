---
title: "Data Augmentation Method For Fabric Defect Detection"
aliases:
  - "Data Augmentation Method for Fabric Defect Detection"
paper_key: "doi:10.1109/icce-taiwan55306.2022.9869278"
paper_type: research
year: 2022
venue: "IEEE International Conference on Consumer Electronics - Taiwan"
authors:
  - "Po-Hsiang Wang"
  - "Chien-Chou Lin"
status: processed
processed_at: 2026-05-31
topics:
  - "fabric defect detection"
  - "GAN augmentation"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "Original Fabric Defect Datasets"
methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Faster R-CNN]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[Faster R-CNN]]"
metrics:
  - "[[Average precision]]"
  - "[[SSIM]]"
primary_metric: "[[Average precision]]"
baselines:
  - "Faster R-CNN with original dataset"
benchmarks: []
code: "not reported"
data: "not reported"
doi: "10.1109/icce-taiwan55306.2022.9869278"
url: "https://doi.org/10.1109/ICCE-TAIWAN55306.2022.9869278"
pdf: "paper-inbox/10_processed/Research/2022 - Wang - Data Augmentation Method for Fabric Defect Detection.pdf"
related_methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Faster R-CNN]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Research/2022 - Wang - Data Augmentation Method for Fabric Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Wang - Data Augmentation Method for Fabric Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Wang - Data Augmentation Method for Fabric Defect Detection.txt"
artifact_status: "data availability not reported"
tags:
  - paper
---

# Data Augmentation Method For Fabric Defect Detection

## Summary

The paper proposes a multi-channel Faster R-CNN for fabric defect detection and expands a small training set with geometric transformations and GAN-generated pseudo defects. The extracted paper text reports 100 original defect images, 720 geometric augmented pseudo images, and 1,868 GAN-generated pseudo images, with AP improving from 75.03% to 90.05%.

## Paper Type

- Type: research.
- Why: It proposes a detection model plus augmentation pipeline and reports experimental AP.

## Problem

- Task: [[Textile defect detection]].
- Setting: small color fabric defect dataset.
- Inputs: RGB and CIELAB fabric images.
- Outputs: defect detection boxes/classes from Faster R-CNN.
- Motivation: existing deep-learning fabric defect approaches do not address small-dataset limitations.
- Assumptions: generated pseudo images should be neither too similar nor too different from real defects.

## Contribution

- Claimed: combines RGB and CIELAB channels in Faster R-CNN and expands the small defect set with geometric and GAN-based augmentation.
- Shown: multi-channel Faster R-CNN trained with augmented data reaches 90.05% AP versus 75.03% for Faster R-CNN with the original dataset.
- Inferred: the method uses learned data synthesis, but the paper does not identify a public textile dataset by name.

## Method

- Core idea: train a fabric detector on original, geometric-augmented, and GAN-generated samples.
- Architecture / algorithm: multi-channel Faster R-CNN using RGB and CIELAB inputs.
- Objective / loss: standard Faster R-CNN training losses; GAN objective not detailed in extracted text.
- Training data: 100 original defect images, 720 geometric pseudo images, and 1,868 GAN pseudo images.
- Data pipeline: rotation, scaling, and flipping; GAN pseudo-image filtering by SSIM target 0.4 to 0.6.
- Augmentation / synthesis: geometric augmentation plus GAN-generated fabric defect images.
- Inference: Faster R-CNN detects defects.

## ML / DL Extraction

### Data

- Dataset name: "Original Fabric Defect Datasets" in Table 1; no canonical host or public name is reported in the extracted text.
- Training set: 80 original images, 576 geometric augmented images, and 1,724 GAN augmented images.
- Test set: 20 original images, 144 geometric augmented images, and 144 GAN augmented images.
- Splits: 80% training and 20% test.
- Labels / annotations: ground-truth bounding boxes are implied by Faster R-CNN training and bounding-box regression.
- License: not reported.

### Evaluation

- Protocol: compare Faster R-CNN trained on original data against multi-channel Faster R-CNN trained with augmented data.
- Used performance metrics: AP and SSIM for pseudo-image filtering.
- Hardware: Intel Xeon E5-2690 v4 CPU, 120 GB memory, NVIDIA P100 GPU; Python/PyTorch 0.4 on Ubuntu 16.04.
- Statistical tests: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Faster R-CNN original vs augmented | Fabric defect detection | AP | higher | 75.03% | 90.05% | Augmented model uses multi-channel Faster R-CNN and GAN/geometric data |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] | detection performance | percent AP | higher | yes | Table 2 labels the metric AP |
| [[SSIM]] | generated-image filtering | structural similarity | target range | no | Target set to 0.4-0.6 |

## Dataset / Benchmark Details

- Source: not reported.
- Collection: not reported.
- Annotation: bounding-box ground truth implied; details not reported.
- Size: 100 original defect images before augmentation.
- Splits: 80/20.
- Modalities: color fabric images.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: very small original dataset; no fabric types or defect classes are reported.

## Limitations

- Stated: pseudo images that are too dissimilar reduce detector accuracy.
- Inferred: dataset provenance and defect taxonomy are underspecified, limiting reuse.

## Reproducibility

- Code: not reported.
- Data: not reported.
- Hardware: Intel Xeon E5-2690 v4, 120 GB memory, NVIDIA P100.
- Environment: Anaconda, Python, PyTorch 0.4, Ubuntu 16.04.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Datasets: not reported by canonical public name; source table labels the data as "Original Fabric Defect Datasets"
- Methods: [[GAN]], [[Data augmentation]], [[Faster R-CNN]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Average precision]], [[SSIM]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]] | Shares task / shares method | Both use GAN-based synthetic data to improve fabric defect models. |
| [[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]] | Shares task | Both address scarce fabric defect data with augmentation, but this paper focuses on detection rather than classification. |

### Backlinks Updated

- not reported

## Questions

- What exact fabric dataset was used, and is it public?
- What GAN architecture generated the pseudo images?
