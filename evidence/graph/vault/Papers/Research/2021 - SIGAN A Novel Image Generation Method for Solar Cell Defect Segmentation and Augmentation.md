---
title: "SIGAN: A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation"
aliases:
  - "SIGAN: A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation"
paper_key: "arxiv:2104.04953"
paper_type: research
year: 2021
venue: "arXiv"
authors:
  - "Binyi Su"
  - "Zhong Zhou"
  - "Haiyong Chen"
  - "Xiaochun Cao"
status: processed
processed_at: 2026-05-22
topics:
  - "solar cell defect segmentation"
  - "generative data augmentation"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[EL-2019]]"
methods:
  - "[[SIGAN]]"
  - "[[GAN]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[SIGAN]]"
metrics:
  - "[[F1-score]]"
  - "[[FID]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "F-score is used for defect segmentation; higher is better."
  - "FID is used for generated image quality; lower is better."
  - "Precision, recall, and F-measure are used for classification augmentation; higher is better."
baselines:
  - "FFT"
  - "Gabor filter"
  - "SEF"
  - "CycleGAN"
  - "ResNet50"
  - "MobileNet"
  - "InceptionV3"
  - "DenseNet121"
benchmarks:
  - "[[EL-2019]]"
code: "not reported"
data: "https://github.com/binyisu/EL-2019"
doi: "not reported"
arxiv: "2104.04953"
url: "https://arxiv.org/abs/2104.04953"
pdf: "paper-inbox/10_processed/Research/2021 - Su - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[SIGAN]]"
  - "[[GAN]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[EL-2019]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2021 - Su - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Su - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Su - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation.txt"
artifact_status: "EL-2019 dataset host reported; code not reported"
tags:
  - paper
---
# SIGAN: A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation

## Summary

- The paper proposes SIGAN, a strong-identity GAN for solar-cell electroluminescence defect segmentation and augmentation. SIGAN removes a defect region from an input defective image, subtracts the generated defect-free image from the original, and thresholds the difference image to segment the defect.
- The paper introduces [[EL-2019]], a multicrystalline solar-cell EL dataset with crack, finger-interruption, and defect-free image patches.

## Paper Type

- Type: research.
- Why: Classified from the title, abstract, and contribution framing in the preprocessed paper text.

## Problem

- Task: [[Solar cell defect detection]], [[Defect segmentation]]
- Setting: [[Solar cells and photovoltaic]]
- Inputs: industrial inspection images or derived visual representations as described by the source paper.
- Outputs: defect segmentation masks from thresholded difference images, generated defect-free EL patches, and generated defective EL patches for augmentation.
- Motivation: improve automated quality inspection for industrial products.
- Assumptions: unpaired defect and defect-free EL image domains are available; preserving background identity is necessary for the subtraction image to isolate the defect.

## Contribution

- Claimed: Strong identity loss helps preserve the defect-free background while a GAN removes the defect region, making the subtraction image useful for segmentation.
- Shown: On [[EL-2019]], SIGAN reports 90.34% total F-score for segmentation, outperforming FFT, Gabor, SEF, and CycleGAN baselines reported in the paper.
- Shown: SIGAN-generated defective images improve total F-measure for four classification backbones in the paper's augmentation experiment.
- Dataset contribution: The paper releases [[EL-2019]], with 260 defective images and 280 defect-free images.
- Inferred: The work is relevant to [[Solar cell defect detection]], [[Defect segmentation]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: Generate a defect-free version of a defective EL image, subtract it from the original defective input, and threshold the subtraction image to obtain the defect region.
- Architecture / algorithm: [[SIGAN]], [[GAN]], [[Defect synthesis]], [[Synthetic data generation]], [[Data augmentation]]
- Objective / loss: adversarial loss, cycle-consistency loss, and strong identity loss are reported.
- Optimization: Adam optimizer with learning rate 0.0002; the learning rate is unchanged for 30 epochs and linearly decreases to zero over the next 30 epochs.
- Training data: [[EL-2019]]
- Data pipeline: raw 1024 x 1024 EL images are cropped into 128 x 128 patches for [[EL-2019]]; model inputs are normalized and resized to 256 x 256 before training.
- Augmentation / synthesis: [[GAN]], [[Synthetic data generation]], [[Data augmentation]]
- Inference: generate a defect-free version of the defective input, subtract it from the original image, and threshold the subtraction image to segment the defect.
- Complexity / deployment constraints: SIGAN and CycleGAN are both reported at 62 ms per image in the paper's time-efficiency comparison.

## ML / DL Extraction

### Task Formulation

- Input modality: solar-cell electroluminescence image patches.
- Output target: defect segmentation mask derived from a thresholded subtraction image; generated defect images for augmentation.
- Supervision: unpaired image-to-image translation between defective and defect-free domains.
- Objective: remove defects while preserving background identity, then use the difference image for segmentation.

### Model And Training

- Model family: [[GAN]]
- Architecture: [[SIGAN]], a GAN-based image translation method with strong identity loss.
- Losses: adversarial loss, cycle-consistency loss, and strong identity loss.
- Optimizer: Adam.
- Hyperparameters: batch size 4; lambda1 = 10; lambda2 = 5; learning rate 0.0002.
- Training compute: Intel Core i7-10700 CPU and NVIDIA GeForce RTX 3090 reported.

### Data

- Datasets: [[EL-2019]]
- Data source: [EL-2019 GitHub repository](https://github.com/binyisu/EL-2019), with substantive dataset details reported in the paper.
- Dataset size: 540 images total; 280 defect-free, 130 crack, and 130 finger-interruption images.
- Labels / annotations: crack, finger interruption, and defect-free categories; segmentation evaluation uses defect regions produced by the dataset/evaluation setup.
- Splits: segmentation/generation split uses 200 defect-free, 50 crack, and 50 finger-interruption images for training; 80 defect-free, 80 crack, and 80 finger-interruption images for testing.
- Preprocessing: defective images are mirrored, flipped, and contrast-normalized when augmenting insufficient defective samples; training inputs are normalized and resized to 256 x 256.
- Augmentation: [[Synthetic data generation]], [[Data augmentation]]
- Synthetic data: reported

### Evaluation

- Protocol: segmentation is evaluated on [[EL-2019]] against FFT, Gabor, SEF, and CycleGAN baselines; generation is evaluated with [[FID]]; augmentation is evaluated by training ResNet50, MobileNet, InceptionV3, and DenseNet121 classifiers with and without generated images.
- Used performance metrics: [[F1-score]], [[FID]], [[Precision]], [[Recall]]
- Primary metric: [[F1-score]]
- Metric definitions: F-score is used for segmentation, FID for image generation quality, and precision/recall/F-measure for classification augmentation.
- Metric direction / units: higher is better for F-score, precision, recall, and F-measure; lower is better for FID and latency.
- Baselines: FFT, Gabor, SEF, and CycleGAN for segmentation; ResNet50, MobileNet, InceptionV3, and DenseNet121 for augmentation evaluation.
- Benchmarks: [[EL-2019]]
- Failure cases: the paper reports CycleGAN failures from background changes and incomplete defect removal; SIGAN is designed to reduce those failures through strong identity loss.

## Evidence

### Experimental Setup

- Datasets: [[EL-2019]]
- Splits: train/test split as reported for [[EL-2019]]: 300 training images and 240 test images for segmentation/generation.
- Baselines: FFT, Gabor, SEF, CycleGAN.
- Used performance metrics: [[F1-score]], [[FID]], [[Precision]], [[Recall]]
- Compute: training performed on a server reported with Intel Core i7-10700 CPU and NVIDIA GeForce RTX 3090.
- Hardware: Intel Core i7-10700 CPU; NVIDIA GeForce RTX 3090.
- Inference cost: SIGAN is reported at 62 ms per image.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Segmentation, total | [[EL-2019]] / [[Defect segmentation]] | F-score | higher | SEF 69.08; CycleGAN 40.32 | SIGAN 90.34 | FFT 45.49 and Gabor 54.97 are also reported. |
| Crack segmentation | [[EL-2019]] / crack defects | F-score | higher | SEF 72.18; CycleGAN 17.89 | SIGAN 86.96 | FFT 52.67; Gabor 54.92. |
| Finger-interruption segmentation | [[EL-2019]] / finger-interruption defects | F-score | higher | SEF 65.97; CycleGAN 62.74 | SIGAN 93.71 | FFT 38.30; Gabor 55.02. |
| Total segmentation timing | [[EL-2019]] / [[Defect segmentation]] | milliseconds per image | lower | CycleGAN 62 ms; SEF 86 ms | SIGAN 62 ms | FFT 72 ms; Gabor 94 ms. |
| Classification augmentation | [[EL-2019]] / defect classification | F-measure | higher | Original total F-measure 96.97-99.06 | Augmented total F-measure 97.80-99.85 | Improvements range from 0.46 to 0.91 percentage points across four backbones. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[F1-score]] | [[Solar cell defect detection]], [[Defect segmentation]] | F-score / F-measure | higher | yes | SIGAN reports 90.34 total F-score for segmentation. |
| [[FID]] | generated EL image quality | Frechet Inception Distance | lower | no | Strong identity loss improves FID for defect-free, crack, and finger-interruption generation. |
| [[Precision]] | classification augmentation | classification precision | higher | no | Reported for ResNet50, MobileNet, InceptionV3, and DenseNet121. |
| [[Recall]] | classification augmentation | classification recall | higher | no | Reported for ResNet50, MobileNet, InceptionV3, and DenseNet121. |

Metric-related source snippets:
- The paper reports 90.34% total F-score for SIGAN segmentation on EL-2019.
- FID is reported for generated defect-free, crack, and finger-interruption images.

### Ablations

- The paper ablates strong identity loss: adding it reduces FID from 102.88 to 86.33 for defect-free images, from 156.25 to 100.05 for crack images, and from 91.12 to 77.84 for finger-interruption images.

## Dataset / Benchmark Details

- Source: [EL-2019 GitHub repository](https://github.com/binyisu/EL-2019).
- Collection: multicrystalline solar-cell EL images collected during manufacturing with a near-infrared WP-US146 camera using a SONY ICX825 chip.
- Annotation: crack, finger interruption, and defect-free categories; segmentation evaluation uses reported defect regions.
- Size: 540 image patches; 260 defective and 280 defect-free.
- Splits: train has 200 defect-free, 50 crack, and 50 finger-interruption images; test has 80 defect-free, 80 crack, and 80 finger-interruption images.
- Modalities: electroluminescence imagery.
- Bias / coverage: bounded to multicrystalline solar-cell EL patches with crack and finger-interruption defects.

## Limitations

- Stated: SIGAN can only generate 256 x 256 EL image patches; generating raw 1024 x 1024 EL images is left as future work.
- Inferred: conclusions are bounded by the reported EL-2019 split and the two defect categories, crack and finger interruption.

## Reproducibility

- Data: https://github.com/binyisu/EL-2019
- Hyperparameters: batch size 4; lambda1 = 10; lambda2 = 5; learning rate 0.0002.
- Environment: Intel Core i7-10700 CPU and NVIDIA GeForce RTX 3090 reported.
- Exact preprocessing: normalization and resizing to 256 x 256 before training; defective samples augmented by mirror, flip, and contrast normalization for small-sample augmentation experiments.
- Artifact status: EL-2019 dataset host reported; code not reported.

## Systems Details

- Hardware / software stack: Intel Core i7-10700 CPU and NVIDIA GeForce RTX 3090 reported.
- Latency: SIGAN is reported at 62 ms per image in the time-efficiency comparison.
- Deployment assumption: patch-level EL image processing at 256 x 256 input size.
- Failure modes: background changes and incomplete defect removal are observed for CycleGAN; SIGAN is designed to reduce them with strong identity loss.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect segmentation]]
- Methods: [[SIGAN]], [[GAN]], [[Defect synthesis]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[EL-2019]]
- Benchmarks: [[EL-2019]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[F1-score]], [[FID]], [[Precision]], [[Recall]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] | Shares domain | Both evaluate solar-cell EL defect detection, while SIGAN focuses on GAN-based segmentation and augmentation. |
| [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] | Shares domain | Both concern photovoltaic anomaly data, but SIGAN introduces EL-2019 for crack and finger-interruption patches. |

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[SIGAN]] | Created | Paper method and ablation sections |
| [[EL-2019]] | Updated | Paper dataset section and GitHub host page |

## Questions

- Can the strong-identity loss preserve background structure when scaling from 256 x 256 patches to 1024 x 1024 raw EL images?
- Does SIGAN remain effective for solar-cell defect types beyond cracks and finger interruptions?
