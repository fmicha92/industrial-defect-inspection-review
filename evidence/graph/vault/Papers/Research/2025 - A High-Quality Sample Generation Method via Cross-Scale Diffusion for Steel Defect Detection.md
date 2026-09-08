---
title: "A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection"
paper_key: "doi:10.1109/ijcnn64981.2025.11228398"
paper_type: research
year: 2025
venue: "International Joint Conference on Neural Networks"
authors:
  - "Ziyang Zhu"
  - "Feng Wang"
status: processed
processed_at: 2026-06-11
topics:
  - "steel defect synthesis"
  - "cross-scale diffusion"
tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-CLS]]"
methods:
  - "[[DDPM-CSD]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[FID]]"
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
optimizers:
  - "[[Adam]]"
doi: "10.1109/ijcnn64981.2025.11228398"
url: "https://doi.org/10.1109/ijcnn64981.2025.11228398"
pdf: "paper-inbox/10_processed/Research/2025 - Zhu - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection.pdf"
hardware: "single NVIDIA RTX 4090 GPU"
code: "not reported"
data: "uses NEU-CLS"
related_methods:
  - "[[DDPM-CSD]]"
  - "[[Diffusion models]]"
related_datasets:
  - "[[NEU-CLS]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2025 - Zhu - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Zhu - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Zhu - A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection.txt"
tags:
  - paper
---
# A High-Quality Sample Generation Method via Cross-Scale Diffusion for Steel Defect Detection

## Summary

The paper proposes [[DDPM-CSD]], a cross-scale diffusion generator for steel defect images. The method adds sliding-window skip connections and cross-scale attention to a DDPM generator, then uses generated [[NEU-CLS]] images to augment downstream defect classifiers. The paper reports lower FID than several baselines on average and higher classification accuracy after augmentation.

## Paper Type

- Type: research.
- Why: The paper proposes a synthetic data generator and evaluates generated-image quality plus downstream ML performance.

## Problem

- Task: [[Defect classification]] for steel surface defects.
- Setting: scarce defect-image training data in [[Metal inspection]].
- Inputs: cropped 64x64 NEU-CLS defect images.
- Outputs: generated defect images and downstream class predictions.

## Contribution

- Claimed: Cross-scale attention and sliding-window skip connections improve DDPM-based defect synthesis.
- Shown: ResNet-18 accuracy improves from 93.24 without synthetic data to 99.89 with DDPM-CSD augmentation.
- Shown: MobileNet accuracy improves from 91.26 to 99.95, and VGG-16 improves from 90.26 to 99.87.

## Method

- Generator: DDPM-CSD with cross-scale attention and sliding-window skip connections.
- Objective: MSE and perceptual loss balanced by lambda.
- Training: batch size 8, 70 epochs, Adam learning rate 1e-4, T=1000, beta1=1e-4, betaT=0.02, gradient clipping max norm 1.0.
- Synthetic-data protocol: each generation method creates 3,780 synthetic defect images, which are combined with 1,260 original training images; the real test set has 540 images.
- Evaluation: five-fold cross-validation for downstream classifiers.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| ResNet-18 augmentation | [[NEU-CLS]] classification | [[Accuracy]] | no synthetic data 93.24 | DDPM-CSD 99.89 | Higher is better. |
| MobileNet augmentation | [[NEU-CLS]] classification | [[Accuracy]] | no synthetic data 91.26 | DDPM-CSD 99.95 | Higher is better. |
| VGG-16 augmentation | [[NEU-CLS]] classification | [[Accuracy]] | no synthetic data 90.26 | DDPM-CSD 99.87 | Higher is better. |
| Generation ablation | [[NEU-CLS]] synthesis | [[FID]] | DDPM category FIDs 107.76/133.39/159.10/102.82/151.44/170.24 | DDPM-CSD 67.53/65.49/80.11/62.15/57.38/83.32 | Lower is better; categories are Cr, In, Pa, Ps, Rs, Sc. |

## Dataset / Benchmark Details

- [[NEU-CLS]]: 1,800 grayscale hot-rolled steel surface images across rolling scale, patch, crack, pitted surface, inclusion, and scratch classes.
- Split: 7:3 train/test after standardizing defect-region crops to 64x64.

## Limitations

- Code availability: not reported.
- The evaluation is limited to NEU-CLS cropped grayscale images.
- The paper does not report dataset license details.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Metallic surface defect detection]]
- Methods: [[DDPM-CSD]], [[Diffusion models]], [[Synthetic data generation]]
- Datasets: [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[FID]], [[Accuracy]]

### Relationship Notes

- Shares dataset: [[NEU-CLS]].
- Shares method: [[DDPM-CSD]], [[Diffusion models]], and [[Synthetic data generation]].
- Shares metric: [[FID]] and [[Accuracy]].
- Application/domain: [[Metal inspection]].

## Questions

- Does DDPM-CSD improve detectors or segmenters, or only image-level classifiers?
- How sensitive are the reported accuracy gains to generated-image filtering or train/test split choices?
