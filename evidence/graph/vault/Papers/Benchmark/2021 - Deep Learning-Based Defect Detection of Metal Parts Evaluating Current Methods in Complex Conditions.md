---
title: "Deep Learning-Based Defect Detection of Metal Parts: Evaluating Current Methods in Complex Conditions"
aliases:
  - "Deep Learning-Based Defect Detection of Metal Parts: Evaluating Current Methods in Complex Conditions"
paper_key: "doi:10.1109/icumt54235.2021.9631567"
paper_type: benchmark
year: 2021
venue: "ICUMT"
authors:
  - "Stepan Jezek"
  - "Martin Jonak"
  - "Radim Burget"
  - "Pavel Dvorak"
  - "Milos Skotak"
status: processed
processed_at: 2026-05-22
topics:
  - "metal part defect detection"
  - "complex industrial conditions"
  - "industrial anomaly detection benchmark"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[MPDD]]"
methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUROC: area under the receiver operating characteristic curve, reported separately for image-level and pixel-level defect detection."
baselines:
  - "PatchCore"
  - "CFLOW-AD"
  - "PaDiM"
  - "SemiOrthogonal"
  - "SPADE"
  - "DAGAN"
  - "Skip-GANomaly"
  - "ITAE"
benchmarks:
  - "[[MPDD]]"
code: "not reported"
data: "reported available: https://github.com/stepanje/MPDD"
doi: "10.1109/icumt54235.2021.9631567"
arxiv: "not reported"
url: "https://doi.org/10.1109/ICUMT54235.2021.9631567"
pdf: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Deep convolutional neural network]]"
related_datasets:
  - "[[MPDD]]"
related_tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/00_incoming/Deep_learning-based_defect_detection_of_metal_parts_evaluating_current_methods_in_complex_conditions.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Jezek - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Jezek - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions.txt"
artifact_status: "dataset reported available"
tags:
  - paper
---
# Deep Learning-Based Defect Detection of Metal Parts: Evaluating Current Methods in Complex Conditions

## Summary

Jezek et al. introduce [[MPDD]], a metal-parts anomaly detection dataset designed for complex production-like imaging conditions: variable object position, rotation, distance, multiple objects, changing light intensity, non-homogeneous backgrounds, shadows, reflections, and motion blur. The dataset targets painted metal parts fabrication, where defect types are not known in advance.

The paper evaluates state-of-the-art semi-supervised anomaly detection methods on MPDD and compares average performance with MVTec AD. The authors report that methods strong on MVTec AD can behave differently on MPDD, with image-level AUROC differences up to 23.12% and an average image-level AUROC difference of 15.24% across methods.

## Paper Type

- Type: benchmark.
- Why: The main contribution is a dataset plus comparative evaluation of anomaly detection methods under complex acquisition conditions.

## Problem

- Task: [[Metallic surface defect detection]] and [[Industrial anomaly detection]].
- Setting: painted metal parts on human-operated production lines.
- Inputs: RGB images of metal parts under variable acquisition conditions.
- Outputs: image-level anomaly detection and pixel-level anomaly segmentation.
- Motivation: MVTec AD and similar datasets often assume centered objects, stable pose, and homogeneous backgrounds, which do not match many production lines.
- Assumptions: only normal samples should be available for training because future defect types are not known in advance.

## Contribution

- Claimed: MPDD captures metal fabrication and painting conditions not well covered by MVTec AD, Kolektor SDD, or Magnetic Tile Defects.
- Shown: MPDD provides anomaly-free training images, normal and anomalous testing images, and pixel-precise ground-truth masks for anomalous areas.
- Shown: feature-extraction anomaly methods are generally more robust than reconstruction-based methods on MPDD.

## Method

The benchmark evaluates semi-supervised anomaly detection methods on MPDD. Feature-extraction methods use 256 x 256 input images, and reconstruction-based methods use 128 x 128 input images. Results are reported with AUROC for image-level detection and pixel-level segmentation.

## Evidence

### Dataset / Benchmark Setup

- Dataset: [[MPDD]].
- Classes: Bracket Black, Bracket Brown, Bracket White, Connector, Metal Plate, and Tubes.
- Training: 888 anomaly-free images total.
- Test normal: 176 images total.
- Test defect: 282 anomalous images total.
- Image size: all images resized to 1024 x 1024 pixels.
- Annotations: anomalous samples include pixel-precise ground-truth masks.
- Capture: consumer-grade camera with two LED light sources and often a neutral green-screen background.
- Availability: reported at `https://github.com/stepanje/MPDD`.

### Main Results

| Result | Dataset / Task | Metric | Direction | Best method | Paper result | Notes |
|---|---|---|---|---|---:|---|
| Image-level detection average | [[MPDD]] / [[Industrial anomaly detection]] | [[AU-ROC]] | higher | CFLOW-AD | 86.12 | Best average across MPDD classes. |
| Pixel-level detection average | [[MPDD]] / [[Industrial anomaly detection]] | [[AU-ROC]] | higher | CFLOW-AD | 97.72 | Best average across MPDD classes. |
| MVTec AD vs. MPDD gap | Method averages | [[AU-ROC]] | smaller gap means more stable transfer | PaDiM has largest reported difference | up to 23.12% image-level difference | Average image-level difference across methods is 15.24%. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection on [[MPDD]] | Area under ROC curve | Higher is better | yes | Average by method: PatchCore 82.12, CFLOW-AD 86.12, PaDiM 74.78, SemiOrthogonal 73.79, SPADE 77.08, DAGAN 72.48, Skip-GANomaly 64.84, ITAE 69.68. |
| [[AU-ROC]] | Pixel-level anomaly segmentation on [[MPDD]] | Area under ROC curve | Higher is better | yes | Average by method: PatchCore 95.66, CFLOW-AD 97.72, PaDiM 96.74, SemiOrthogonal 88.22, SPADE 95.93, DAGAN 83.31, Skip-GANomaly 82.19. |

## ML / DL Extraction

### Task Formulation

- Input modality: visual metal-part inspection images.
- Output target: image-level anomaly score and pixel-level anomaly mask.
- Supervision: semi-supervised/unsupervised anomaly detection with normal-only training images.
- Objective: test whether existing anomaly detection methods remain robust under production-like acquisition variability.

### Model And Training

- Evaluated methods: PatchCore, CFLOW-AD, PaDiM, SemiOrthogonal, SPADE, DAGAN, Skip-GANomaly, and ITAE.
- Feature-extraction methods: use features from pretrained networks.
- Reconstruction-based methods: learn normal image reconstruction.
- Exact hyperparameters: not reported in the extracted text.
- Compute: not reported.

### Data

- Dataset: [[MPDD]].
- Data source: painted metal parts fabrication scenes.
- Split: normal-only training; normal and anomalous testing.
- Defect types: scratches, defective shapes, missing or torn-off components, and related metal fabrication/painting defects are discussed; exact per-class defect taxonomy is not fixed in advance.
- Leakage checks: not reported.
- License: not reported in the extracted text.

### Evaluation

- Protocol: train semi-supervised anomaly methods on normal images and evaluate on normal/anomalous test images.
- Metrics: image-level and pixel-level [[AU-ROC]].
- Baselines: PatchCore, CFLOW-AD, PaDiM, SemiOrthogonal, SPADE, DAGAN, Skip-GANomaly, ITAE.
- Failure cases: connector contains a missing-part defect; black bracket has subtle defects that are difficult to spot.

## Dataset / Benchmark Details

| Class | Train normal | Test normal | Test defect |
|---|---:|---:|---:|
| Bracket Black | 289 | 32 | 47 |
| Bracket Brown | 185 | 26 | 51 |
| Bracket White | 110 | 30 | 30 |
| Connector | 128 | 30 | 14 |
| Metal Plate | 54 | 26 | 69 |
| Tubes | 122 | 32 | 71 |
| Total | 888 | 176 | 282 |

## Limitations

- Dataset size may be insufficient for some reconstruction-based methods.
- MPDD is focused on metal fabrication and painting, so conclusions should not be generalized to all industrial anomaly detection domains without additional datasets.
- Some defects are subtle or difficult to spot, especially black bracket defects.
- Exact method hyperparameters and compute settings are not preserved in the extracted text.

## Reproducibility

- Code: not reported.
- Data: reported available at `https://github.com/stepanje/MPDD`.
- Environment: not reported.
- Random seeds: not reported.
- Ground truth: pixel masks for anomalous samples are reported.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]], [[Industrial anomaly detection]]
- Methods: [[Unsupervised anomaly detection]], [[Deep convolutional neural network]]
- Datasets: [[MPDD]]
- Benchmarks: [[MPDD]]
- Domains: [[Metal inspection]]
- Metrics: [[AU-ROC]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] | Shares domain/task | Both evaluate metal surface defect detection, but MPDD emphasizes complex production-like acquisition conditions and unsupervised anomaly detection. |

## Questions

- What license applies to MPDD?
- Which exact implementations and hyperparameters were used for each anomaly detection method?
- How sensitive are MPDD rankings to input resolution and feature backbone choices?
