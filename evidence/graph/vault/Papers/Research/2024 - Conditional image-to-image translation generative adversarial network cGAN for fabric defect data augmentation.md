---
title: "Conditional image-to-image translation generative adversarial network (cGAN) for fabric defect data augmentation"
aliases:
  - "Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation"
paper_key: "doi:10.1007/s00521-024-10179-1"
paper_type: research
year: 2024
venue: "Neural Computing and Applications"
authors:
  - "Swash Sami Mohammed"
  - "Hulya Gokalp Clarke"
status: processed
processed_at: 2026-05-31
topics:
  - "fabric defect data augmentation"
  - "synthetic defect generation"
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[AITEX]]"
methods:
  - "[[Image-to-image cGAN fabric defect augmentation]]"
  - "[[GAN]]"
  - "[[U-Net]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[U-Net]]"
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Loss: downstream segmentation loss; lower is better."
  - "Accuracy: segmentation-model accuracy; higher is better."
  - "Recall: true positive detection coverage; higher is better."
  - "Precision: positive prediction correctness; higher is better."
  - "F1-score: harmonic mean of precision and recall; higher is better."
baselines:
  - "U-Net"
  - "PSPNet"
  - "DeepLabV3+"
  - "SegNet"
benchmarks:
  - "[[AITEX]]"
code: "not reported"
data: "AITEX open access; generated masks and synthetic samples available from corresponding author on reasonable request"
doi: "10.1007/s00521-024-10179-1"
url: "https://doi.org/10.1007/s00521-024-10179-1"
pdf: "paper-inbox/10_processed/Research/2024 - Mohammed - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation.pdf"
related_concepts:
  - "[[Textile and fiber inspection]]"
  - "[[Defect synthesis]]"
related_methods:
  - "[[Image-to-image cGAN fabric defect augmentation]]"
  - "[[GAN]]"
  - "[[U-Net]]"
related_datasets:
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Mohammed - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Mohammed - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Mohammed - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation.txt"
artifact_status: "dataset public; generated artifacts request-only"
tags:
  - paper
---

# Conditional image-to-image translation generative adversarial network (cGAN) for fabric defect data augmentation

## Summary

The paper proposes a mask-conditioned image-to-image cGAN for fabric defect augmentation. It uses AITEX fabric images, decomposes them into 256 x 256 samples, trains a conditional U-Net generator with a six-layer PatchGAN discriminator, and uses the generated samples to improve segmentation-model performance on fabric defects.

## Paper Type

- Type: research.
- Why: The paper introduces and evaluates a generative augmentation method for fabric defect segmentation.

## Problem

- Task: [[Textile defect detection]] and [[Defect segmentation]].
- Setting: scarce public fabric defect data in textile quality control.
- Inputs: clean fabric image plus segmented defect mask.
- Outputs: synthetic defective fabric image; downstream model outputs defect segmentation predictions.
- Motivation: AITEX and similar public fabric datasets are small and imbalanced, making robust AI training difficult.
- Assumptions: defect mask conditioning can control defect type, shape, size, and location.

## Contribution

- Claimed: A conditional U-Net generator inside a cGAN can synthesize realistic fabric defects from a clean fabric sample and a defect mask.
- Shown: Synthetic cGAN samples improved U-Net, PSPNet, DeepLabV3+, and SegNet metrics compared with training on the small real dataset.
- Inferred: The paper is primarily about learned synthetic data generation for textile defect segmentation.

## Method

- Core idea: condition the generator on both fabric texture and defect-mask geometry.
- Architecture / algorithm: conditional U-Net generator and six-layer PatchGAN discriminator.
- Objective / loss: adversarial cGAN loss plus L1 loss; the paper reports binary cross-entropy for the cGAN/discriminator loss and sets the L1 gain lambda to 100 to produce sharper images.
- Optimization: learning rate 0.0001, beta1 0.5, beta2 0.999.
- Training data: AITEX fabric defects after cropping and rotation augmentation.
- Data pipeline: original 4096 x 256 AITEX images are decomposed into 256 x 256 samples; three defect types are used.
- Augmentation / synthesis: 56 defective samples are rotated into 224 samples; the trained cGAN generates 1000 synthetic samples for downstream model training.
- Inference: generator takes clean fabric and mask inputs to produce a synthetic defective fabric image.
- Complexity / deployment constraints: estimated 35.98 TFLOPs; trained on Google Colab Pro with a Tesla T4 GPU and 14 GB RAM.

## ML / DL Extraction

### Data

- Datasets: [[AITEX]].
- Dataset size: AITEX has 245 images of 4096 x 256 pixels, with 140 defect-free images and 105 defective images from 12 defect types.
- Textile subset used: fuzzy ball, broken end, and broken yarn, selected as the three most common defect types.
- Splits: downstream experiments use 80% training and 20% testing under three settings: 56 real samples, 224 rotated samples, and 1000 cGAN synthetic samples tested against the original dataset.
- Labels / annotations: segmented defect masks are used as cGAN inputs.
- License: AITEX is reported as open access.

### Evaluation

- Protocol: train downstream segmentation models for 100 epochs under the three data settings.
- Used performance metrics: loss, [[Accuracy]], [[Recall]], [[Precision]], and [[F1-score]].
- Baselines: U-Net, PSPNet, DeepLabV3+, and SegNet under smaller real/augmented data settings.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| U-Net trained with synthetic samples | AITEX segmentation | Loss | lower | 1.5927 | 0.0788 | Case 1 to case 3 |
| U-Net trained with synthetic samples | AITEX segmentation | F1-score | higher | 0.2678 | 0.9699 | Case 1 to case 3 |
| PSPNet trained with synthetic samples | AITEX segmentation | Accuracy | higher | 0.6179 | 0.9966 | Case 1 to case 3 |
| DeepLabV3+ trained with synthetic samples | AITEX segmentation | Recall | higher | 0.5345 | 0.9974 | Case 1 to case 3 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| Loss | segmentation model evaluation | downstream segmentation loss | lower | no | U-Net loss decreases from 1.5927 in case 1 to 0.0788 in case 3. |
| [[Accuracy]] | segmentation model evaluation | segmentation-model accuracy | higher | no | PSPNet accuracy increases from 0.6179 in case 1 to 0.9966 in case 3. |
| [[Recall]] | segmentation model evaluation | true positive detection coverage | higher | no | DeepLabV3+ recall increases from 0.5345 in case 1 to 0.9974 in case 3. |
| [[Precision]] | segmentation model evaluation | positive prediction correctness | higher | no | SegNet precision increases from 0.6483 in case 1 to 0.9920 in case 3. |
| [[F1-score]] | segmentation model evaluation | harmonic mean of precision and recall | higher | yes | U-Net F1-score increases from 0.2678 in case 1 to 0.9699 in case 3. |

## Dataset / Benchmark Details

- Source: AITEX fabric defect dataset, available at the AITEX AFID host and cited through DOI 10.2478/aut-2019-0035.
- Collection: seven fabric structures.
- Annotation: defect masks are used; exact mask source is not expanded beyond the paper's dataset discussion.
- Size: 245 full-size images, decomposed into 56 defect samples for the selected three defect types, then rotated into 224 samples.
- Splits: 80/20 train/test for downstream experiments.
- Modalities: grayscale fabric imagery and segmentation masks.
- Leakage risks: not reported.
- Bias / coverage: only three of the 12 AITEX defect types are used.
- Maintenance: not reported.

## Limitations

- Stated: public fabric defect datasets are small and insufficiently diverse.
- Inferred: evaluation is constrained by using only three AITEX defect categories and by testing synthetic-data gains on a small source dataset.

## Reproducibility

- Code: not reported.
- Data: AITEX is public; masks and generated synthetic samples are request-only.
- Hyperparameters: learning rate 0.0001, beta1 0.5, beta2 0.999, 100 epochs, generator batch size 1.
- Hardware: Google Colab Pro, Intel Xeon CPU 2.20 GHz, Tesla T4 GPU, 14 GB RAM.
- Artifact status: dataset public; synthetic artifacts request-only.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect segmentation]]
- Methods: [[Image-to-image cGAN fabric defect augmentation]], [[GAN]], [[U-Net]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[AITEX]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Accuracy]], [[Recall]], [[Precision]], [[F1-score]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things]] | Shares dataset / shares method | Both use AITEX and GAN-based fabric defect processing, but this paper uses cGAN synthesis for augmentation while the other uses GAN repair for segmentation. |
| [[2022 - Data Augmentation Method for Fabric Defect Detection]] | Shares task / shares method | Both use GAN-based augmentation for fabric defect detection. |

### Backlinks Updated

- [[Image-to-image cGAN fabric defect augmentation]]

## Questions

- Are the generated masks hand-labeled from AITEX masks or derived by an additional preprocessing step?
- Do the results hold when all 12 AITEX defect types are included?
