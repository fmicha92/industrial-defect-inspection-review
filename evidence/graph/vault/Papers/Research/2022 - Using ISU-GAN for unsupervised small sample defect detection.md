---
title: "Using ISU-GAN for unsupervised small sample defect detection"
aliases:
  - "Using ISU-GAN for unsupervised small sample defect detection"
paper_key: "doi:10.1038/s41598-022-15855-7"
paper_type: research
year: 2022
venue: "Scientific Reports"
authors:
  - "Yijing Guo"
  - "Linwei Zhong"
  - "Yi Qiu"
  - "Huawei Wang"
  - "Fengqiang Gao"
  - "Zongheng Wen"
  - "Choujun Zhan"
status: processed
processed_at: 2026-05-31
topics:
  - "unsupervised defect detection"
  - "small sample defect detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[DAGM2007]]"
methods:
  - "[[ISU-GAN]]"
  - "[[GAN]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[ISU-GAN]]"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[SSIM]]"
primary_metric: "[[F1-score]]"
baselines:
  - "UNet"
  - "ResUNet++"
  - "CycleGAN"
  - "DCGAN"
benchmarks:
  - "[[DAGM2007]]"
code: "not reported"
data: "DAGM2007 public"
doi: "10.1038/s41598-022-15855-7"
url: "https://doi.org/10.1038/s41598-022-15855-7"
pdf: "paper-inbox/10_processed/Research/2022 - Guo - Using ISU-GAN for unsupervised small sample defect detection.pdf"
related_methods:
  - "[[ISU-GAN]]"
  - "[[GAN]]"
  - "[[Unsupervised anomaly detection]]"
related_datasets:
  - "[[DAGM2007]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2022 - Guo - Using ISU-GAN for unsupervised small sample defect detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Guo - Using ISU-GAN for unsupervised small sample defect detection.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Guo - Using ISU-GAN for unsupervised small sample defect detection.txt"
artifact_status: "public benchmark; code not reported"
tags:
  - paper
---

# Using ISU-GAN for unsupervised small sample defect detection

## Summary

The paper proposes [[ISU-GAN]], an unsupervised small-sample defect detection model based on CycleGAN with skip connections, SE, and Involution modules. It evaluates on selected [[DAGM2007]] classes and reports 98.43% average accuracy and 0.9792 F1-score using less than one-third of the training data used by supervised comparators.

## Paper Type

- Type: research.
- Why: The paper proposes a model, reports benchmark experiments, and includes ablation studies.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: industrial surface defect detection with few unlabeled samples and costly labels.
- Inputs: positive defect-free samples and negative defective samples during unsupervised CycleGAN-style training.
- Outputs: anomaly decision and defect contour extracted through SSIM-based difference.
- Motivation: supervised segmentation models require many labeled defect samples.
- Assumptions: a defect repair generator can map defective images to defect-free reconstructions, making defects visible through structural difference.

## Contribution

- Claimed: ISU-GAN improves CycleGAN for small-sample industrial defect detection by adding skip, SE, and Involution modules.
- Shown: higher accuracy and F1-score than supervised UNet and ResUNet++ and unsupervised CycleGAN/DCGAN comparisons on selected DAGM2007 classes.
- Inferred: this is adjacent to textile work because DAGM2007 is a public textured-surface dataset, not a textile dataset.

## Method

- Core idea: train two mappings between positive and negative sample domains, then repair defects and use SSIM to extract contours.
- Architecture / algorithm: CycleGAN-based GAN with U-Net-like generator, skip connections, SE block, and Involution block.
- Objective / loss: CycleGAN consistency and GAN training; extracted text also discusses MSE for repair similarity in ablations.
- Training data: selected DAGM2007 classes 1, 6, and 7.
- Augmentation / synthesis: the model includes a defect manufacturing network that maps positive samples to pseudo-negative samples, but evaluation centers on unsupervised repair and detection.
- Inference: input test image to repair network, compute SSIM score map, threshold/extract defect contour.

## ML / DL Extraction

### Data

- Dataset: [[DAGM2007]].
- Dataset description: ten artificially produced texture-defect classes; grayscale 512 x 512 images; weakly supervised labels.
- Classes used: class 1 for diverse surface texture, class 6 for messy texture, and class 7 for sliver defects.
- Splits: uses DAGM official train/test split for comparators; ISU-GAN uses less than one-third of the training data. Exact per-class counts are in Table 1, but the extraction did not preserve every number.
- License: public download URL is reported by the paper.

### Evaluation

- Protocol: compare ISU-GAN against UNet, ResUNet++, CycleGAN, and DCGAN; ablate generator modules.
- Used performance metrics: [[Accuracy]], [[F1-score]], and MSE for repair ablation.
- Primary metric: [[F1-score]].
- Statistical tests: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| ISU-GAN average | DAGM2007 selected classes | Accuracy | higher | not reported | 98.43% | Reported in method summary |
| ISU-GAN average | DAGM2007 selected classes | F1-score | higher | not reported | 0.9792 | Reported in method summary |
| ISU-GAN vs UNet | DAGM2007 selected classes | Accuracy | higher | UNet | +2.84 percentage points | Uses fewer training samples than supervised model |
| ISU-GAN vs UNet | DAGM2007 selected classes | F1-score | higher | UNet | +0.025 | Uses fewer training samples than supervised model |
| ISU-GAN vs ResUNet++ | DAGM2007 selected classes | Accuracy | higher | ResUNet++ | +0.41 percentage points | Uses fewer training samples than supervised model |
| ISU-GAN vs ResUNet++ | DAGM2007 selected classes | F1-score | higher | ResUNet++ | +0.0012 | Uses fewer training samples than supervised model |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | binary defect detection | correct predictions | higher | yes | Reported as Acc |
| [[F1-score]] | binary defect detection | precision/recall harmonic mean | higher | yes | Used to compare imbalanced detection |
| MSE | repair ablation | reconstruction error | lower | no | Not linked as a metric note |
| [[SSIM]] | defect extraction | structural similarity score map | context-dependent | no | Used to extract contours |

## Dataset / Benchmark Details

- Source: DAGM2007 public industrial weakly supervised defect dataset.
- Collection: artificially produced texture defects.
- Annotation: weak labels; selected class labels and masks/labels used for evaluation.
- Size: ten classes in the full dataset; this paper selects three representative classes.
- Modalities: grayscale texture images.
- License: public dataset URL reported.
- Leakage risks: not reported.
- Bias / coverage: not textile-specific; synthetic texture defects may differ from real textile defects.

## Limitations

- Stated: not reported in the extracted conclusion beyond industrial small-sample framing.
- Inferred: evidence is limited to three DAGM classes rather than textile fabric datasets.

## Reproducibility

- Code: not reported.
- Data: DAGM2007 public.
- Hyperparameters: not fully extracted.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[ISU-GAN]], [[GAN]], [[Unsupervised anomaly detection]]
- Datasets: [[DAGM2007]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Accuracy]], [[F1-score]], [[SSIM]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation]] | Shares dataset / shares method | Both use DAGM2007 and CycleGAN-derived approaches, but ISU-GAN performs unsupervised detection while PreCaCycleGAN generates augmentation samples. |

### Backlinks Updated

- [[ISU-GAN]]

## Questions

- Are the per-class train/test counts from Table 1 needed for downstream benchmarking?
- Would the method work on public textile datasets such as AITEX or ZJU-Leaper?
