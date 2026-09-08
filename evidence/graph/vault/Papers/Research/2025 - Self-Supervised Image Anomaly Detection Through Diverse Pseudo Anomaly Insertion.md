---
title: "Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion"
aliases:
  - "Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion"
paper_key: "doi:10.1109/access.2025.3580864"
paper_type: research
year: 2025
venue: "IEEE Access"
authors:
  - "Rizwan Ali Shah"
  - "Odilbek Urmonov"
  - "Hyungwon Kim"
status: processed
processed_at: 2026-06-12
topics:
  - "pseudo anomaly insertion"
  - "self-supervised anomaly segmentation"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[KolektorSDD2]]"
methods:
  - "[[Affine anomaly insertion]]"
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
primary_metric: "[[Average precision]]"
baselines:
  - "CutPaste"
  - "CutPaste-Scar"
  - "Perlin noise pattern"
  - "Simplex anomaly"
  - "fractal augmentation"
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[KolektorSDD2]]"
evaluation_protocol: "PAI methods integrated into a baseline self-supervised anomaly detector and evaluated with AUROCimage, AUROCpixel, and APpixel"
doi: "10.1109/access.2025.3580864"
url: "https://doi.org/10.1109/ACCESS.2025.3580864"
pdf: "paper-inbox/10_processed/Research/2025 - Shah - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion.pdf"
code: "https://github.com/RizwanAliQau/pail.git"
data: "not reported"
related_methods:
  - "[[Affine anomaly insertion]]"
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[KolektorSDD2]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
concept_notes_created_or_updated:
  - "[[Affine anomaly insertion]]"
source_file: "paper-inbox/10_processed/Research/2025 - Shah - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Shah - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Shah - Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion.txt"
artifact_status: "code reported"
tags:
  - paper
---

# Self-Supervised Image Anomaly Detection Through Diverse Pseudo Anomaly Insertion

## Summary

The paper presents a pseudo-anomaly insertion framework and PAI library for self-supervised anomaly detection and segmentation. It compares multiple source-free and source-based pseudo anomaly insertion schemes on [[MVTec AD]], [[VisA]], and [[KolektorSDD2]], and introduces affine anomaly insertion (AA) with variants that insert transformed patches, anomaly source images, or color-transformed patches. AA is reported as the strongest pixel-precision method overall, improving APpixel by 5.2% on MVTec AD and 10.1% on VisA relative to the second-best PAI technique.

## Paper Type

- Type: research.
- Why: It proposes an anomaly insertion tool and evaluates multiple synthetic-anomaly training schemes across anomaly benchmarks.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: self-supervised anomaly detection where real defects are scarce or unavailable for training.
- Inputs: normal images, and anomaly-source images for source-based insertion methods.
- Outputs: pseudo-anomalous training images, masks, and downstream anomaly detection / segmentation predictions.
- Motivation: anomaly detector performance depends strongly on the pseudo-anomaly insertion scheme used for self-supervised training.
- Assumptions: a library of diverse insertion schemes lets practitioners select pseudo anomalies whose pattern, color, and scale better match target defects.

## Contribution

- Claimed: integrates multiple PAI schemes into one framework with adaptive or selective insertion modes.
- Claimed: introduces affine anomaly insertion (AA) and variants AAS and AAC.
- Shown: AA dominates APpixel on MVTec AD and VisA averages and ranks near the top for AUROCimage and AUROCpixel.

## Method

- Core idea: compare and package pseudo-anomaly insertion schemes for self-supervised anomaly detector training.
- Architecture / algorithm: PAI library plus a baseline self-supervised anomaly detector; exact detector architecture is not reported in the extracted text.
- Objective / loss: the detector learns from synthetic anomaly labels and masks; exact loss is not reported.
- Optimization: not reported.
- Training data: [[MVTec AD]], [[VisA]], and [[KolektorSDD2]].
- Data pipeline: resize images, generate pseudo anomalies and masks using source-free or source-based insertion methods, train the downstream detector.
- Augmentation / synthesis: cut-paste variants, Perlin noise, simplex/fractal methods, random perturbations, and [[Affine anomaly insertion]].
- Inference: evaluate real anomaly detection and segmentation on benchmark test sets.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[VisA]], [[KolektorSDD2]].
- Baselines / compared PAI schemes: CutPaste, CutPaste-Scar, source-based Perlin noise pattern, random perturbations, fractal augmentation, simplex anomaly, and several source-based variants.
- Used performance metrics: AUROCimage, AUROCpixel, and APpixel.
- Code: `https://github.com/RizwanAliQau/pail.git`.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| AA average | MVTec AD | AUROCimage | higher | PNP 95.9% | 95.3% | Second-highest, 0.6 points below top. |
| AA average | MVTec AD | AUROCpixel | higher | PNPRI 89.6% | 89.4% | Second-highest, 0.3 points below top. |
| AA average | MVTec AD | APpixel | higher | PNPRI 60.3% | 65.5% | Highest; +5.2 points over second-best. |
| AA average | VisA | AUROCimage | higher | SA 90.5% | 90.2% | Top-three, 0.3 points below top. |
| AA average | VisA | AUROCpixel | higher | RACP 85.5% | 91.4% | Highest; +5.9 points over second-best. |
| AA average | VisA | APpixel | higher | SA 34.0% | 44.1% | Highest; +10.1 points over second-best. |

### Ablations / Analysis

- The paper groups anomaly types into internal, external, and logical classes and reports that logical anomalies remain harder for PAI methods.
- MVTec AD categories with internal anomalies such as capsule and screw show lower APpixel for some PAI methods.
- AA, PNPRI, PNP, and SA are highlighted as robust methods for internal and external anomaly categories.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] / APpixel | pixel-level anomaly segmentation | pixel-wise average precision, percent | higher | yes | Used as the key metric for comparing PAI schemes. |
| [[AU-ROC]] / AUROCpixel | pixel-level anomaly localization | area under ROC curve, percent | higher | no | AA reports 89.4% on MVTec AD and 91.4% on VisA averages. |
| [[AU-ROC]] / AUROCimage | image-level anomaly detection | area under ROC curve, percent | higher | no | AA reports 95.3% on MVTec AD and 90.2% on VisA averages. |

## Dataset / Benchmark Details

- [[MVTec AD]]: used for class-wise and anomaly-type analysis.
- [[VisA]]: 12 classes across PCB, multiple-instance, and single-instance categories.
- [[KolektorSDD2]]: used as an additional segmentation dataset.
- License: not reported.

## Limitations

- Stated: the method discussion implies logical anomalies remain more difficult for pseudo-anomaly insertion.
- Inferred: PAI scheme ranking depends on the downstream detector and dataset class composition.

## Reproducibility

- Code: `https://github.com/RizwanAliQau/pail.git`.
- Data: public benchmarks are named.
- Hyperparameters: not reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Affine anomaly insertion]], [[Defect synthesis]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[VisA]], [[KolektorSDD2]]
- Benchmarks: [[MVTec AD]], [[VisA]], [[KolektorSDD2]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]]

### Shares Dataset

- [[MVTec AD]], [[VisA]], and [[KolektorSDD2]] are used to compare pseudo anomaly insertion schemes.

### Shares Method

- [[Affine anomaly insertion]]: introduced and reported as the strongest APpixel method on MVTec AD and VisA.
- [[Defect synthesis]] and [[Data augmentation]]: all evaluated schemes generate synthetic anomaly training samples.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]].

## Questions

- How sensitive are the rankings to the baseline detector architecture?
- Can the PAI library select schemes automatically per anomaly type rather than requiring user preference?
