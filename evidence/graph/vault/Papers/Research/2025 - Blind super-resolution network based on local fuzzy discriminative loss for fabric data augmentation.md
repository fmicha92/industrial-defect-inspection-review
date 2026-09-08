---
title: "Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation"
aliases:
  - "Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation"
paper_key: "doi:10.1177/15589250241313158"
paper_type: research
year: 2025
venue: "Journal of Engineered Fibers and Fabrics"
authors:
  - "Ning Dai"
  - "Xiaohan Hu"
  - "Kaixin Xu"
  - "Xudong Hu"
  - "Yanhong Yuan"
  - "Bo Cao"
  - "Luhong Shi"
status: processed
processed_at: 2026-06-12
topics:
  - "fabric defect data augmentation"
  - "blind super-resolution"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[DAGM2007]]"
  - "[[TILDA]]"
methods:
  - "[[Super-resolution data augmentation]]"
  - "[[Data augmentation]]"
model_family:
  - "super-resolution network"
architectures:
  - "Real-ESRGAN"
  - "YOLOv5n"
losses:
  - "localized blur discriminative loss"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[mAP]]"
  - "[[FID]]"
  - "[[PSNR]]"
  - "[[SSIM]]"
  - "[[LPIPS]]"
primary_metric: "[[mAP]]"
baselines:
  - "Real-ESRGAN"
  - "CycleGAN"
  - "CutGAN"
  - "StyleGAN"
benchmarks:
  - "[[DAGM2007]]"
evaluation_protocol: "YOLOv5n fabric defect detection after training-data augmentation; image enhancement metrics on generated images"
doi: "10.1177/15589250241313158"
url: "https://doi.org/10.1177/15589250241313158"
pdf: "paper-inbox/10_processed/Research/2025 - Dai - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation.pdf"
code: "not reported"
data: "not reported"
related_methods:
  - "[[Super-resolution data augmentation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[DAGM2007]]"
  - "[[TILDA]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
concept_notes_created_or_updated:
  - "[[Super-resolution data augmentation]]"
source_file: "paper-inbox/10_processed/Research/2025 - Dai - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Dai - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Dai - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation.txt"
artifact_status: "not reported"
tags:
  - paper
---

# Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation

## Summary

The paper proposes a fabric defect data augmentation method based on an improved Real-ESRGAN blind super-resolution model. It replaces Gaussian noise in the resolution degradation module with Poisson noise and adds a localized blur discriminative loss to suppress local blur and artifacts. On [[DAGM2007]], augmenting YOLOv5n training data with the proposed OurSR method improves precision from 90.5% to 97.9%, recall from 95.7% to 96.7%, and mAP@0.5 from 0.961 to 0.986.

## Paper Type

- Type: research.
- Why: It proposes a model modification and evaluates augmentation effects on downstream fabric defect detection.

## Problem

- Task: [[Textile defect detection]].
- Setting: fabric defect detection with limited and poor-quality open-source defect data.
- Inputs: fabric defect images.
- Outputs: enhanced super-resolution images used as augmented training data for YOLOv5n detection.
- Motivation: conventional augmentation provides limited gains, while generative augmentation can be hard to train, artifact-prone, and require relabeling.
- Assumptions: super-resolution can improve training data quality while preserving texture and label geometry.

## Contribution

- Claimed: improves Real-ESRGAN for fabric image degradation by replacing Gaussian noise with Poisson noise.
- Claimed: introduces a localized blur discriminative loss to reduce local blur and fabric artifacts.
- Shown: downstream YOLOv5n detection metrics improve on DAGM2007 after augmentation.

## Method

- Core idea: use blind super-resolution as data augmentation for fabric defects rather than generating new semantic defect layouts.
- Architecture / algorithm: Real-ESRGAN-based super-resolution network; YOLOv5n downstream detector.
- Objective / loss: localized blur discriminative loss plus the Real-ESRGAN training losses reported by the baseline; exact full loss weighting is not reported in the extracted text.
- Optimization: not reported.
- Training data: [[DAGM2007]] and [[TILDA]] for generalization evaluation.
- Data pipeline: degrade and super-resolve fabric images, then train a detector with the enhanced data.
- Augmentation / synthesis: [[Super-resolution data augmentation]].
- Inference: downstream YOLOv5n detects fabric defects.

## Evidence

### Experimental Setup

- Datasets: [[DAGM2007]] and [[TILDA]].
- Baselines: CycleGAN, CutGAN, StyleGAN, Real-ESRGAN/SR, and traditional augmentation methods.
- Used performance metrics: precision, recall, F1-score, mAP@0.5, DLP, FID, PSNR, SSIM, LPIPS.
- Compute: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Downstream detection gain | DAGM2007 / YOLOv5n | Precision | higher | raw data 90.5% | OurSR 97.9% | +7.4 percentage points over raw data. |
| Downstream detection gain | DAGM2007 / YOLOv5n | Recall | higher | raw data 95.7% | OurSR 96.7% | +1.0 percentage point over raw data. |
| Downstream detection gain | DAGM2007 / YOLOv5n | mAP@0.5 | higher | raw data 0.961 | OurSR 0.986 | +0.025 over raw data. |
| Real-ESRGAN improvement | DAGM2007 / YOLOv5n | Precision / recall / mAP@0.5 | higher | SR 96.2% / 96.1% / 0.977 | OurSR 97.9% / 96.7% / 0.986 | Shows the Poisson-noise and localized-blur-loss variant improves the SR augmentation baseline. |
| Traditional augmentation comparison | DAGM2007 / YOLOv5n | mAP@0.5 | higher | horizontal flip 0.965; vertical flip 0.980; Gaussian noise 0.927; contrast 0.975 | OurSR 0.986 | Gaussian noise worsens raw-data recall and mAP. |
| Localization degradation | DAGM2007 / YOLOv5n | DLP | lower | SR 0.049 | OurSR 0.038 | Smallest DLP among compared methods. |
| Image quality | TILDA / enhancement | FID | lower | SR 98.174 | OurSR 69.433 | Lower is better. |
| Image quality | TILDA / enhancement | PSNR | higher | SR 13.29 | OurSR 15.22 | Higher is better. |
| Image quality | TILDA / enhancement | SSIM | higher | SR 0.613 | OurSR 0.750 | Higher is better. |
| Image quality | TILDA / enhancement | LPIPS | lower | SR 0.662 | OurSR 0.357 | Lower is better. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | fabric defect detection | mean average precision | higher | yes | Reported with YOLOv5n. |
| [[Precision]] | fabric defect detection | detection precision | higher | no | Gain reported. |
| [[Recall]] | fabric defect detection | detection recall | higher | no | Gain reported. |
| [[FID]] | enhancement quality | distribution distance | lower | no | Reported for generated/enhanced images. |
| [[PSNR]] | enhancement quality | peak signal-to-noise ratio | higher | no | Reported for generated/enhanced images. |
| [[SSIM]] | enhancement quality | structural similarity | higher | no | Reported for generated/enhanced images. |
| [[LPIPS]] | enhancement quality | perceptual distance | lower | no | Reported for generated/enhanced images. |

## Dataset / Benchmark Details

- [[DAGM2007]]: used for fabric defect detection augmentation and YOLOv5n evaluation.
- [[TILDA]]: natural-environment fabric defect images; 395 images selected after preprocessing and resized to 512 x 512, with holes, threads, stains, and dirt.
- License: not reported.

## Limitations

- Stated: future work should test other image datasets or industries.
- Inferred: the method improves quality of existing examples but does not create new defect semantics or annotations beyond the original labels.

## Reproducibility

- Code: not reported.
- Data: DAGM2007 and TILDA are named.
- Hyperparameters: not reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Methods: [[Super-resolution data augmentation]], [[Data augmentation]]
- Datasets: [[DAGM2007]], [[TILDA]]
- Benchmarks: [[DAGM2007]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Precision]], [[Recall]], [[F1-score]], [[mAP]], [[FID]], [[PSNR]], [[SSIM]], [[LPIPS]]

### Shares Dataset

- [[DAGM2007]] is the primary defect detection dataset.
- [[TILDA]] is used for image-enhancement generalization experiments.

### Shares Method

- [[Super-resolution data augmentation]] is the central augmentation strategy.
- [[Data augmentation]] connects the paper to broader scarce-defect-data workflows.

### Application/domain

- [[Textile and fiber inspection]]: the paper targets fabric defect detection.

## Questions

- Does the method improve segmentation masks or only bounding-box/object detection performance?
- How much of the gain comes from Poisson degradation modeling versus the localized blur discriminative loss?
