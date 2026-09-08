---
title: "ALGAN: Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables"
aliases:
  - "ALGAN"
paper_key: "doi:10.1109/access.2022.3169594"
paper_type: research
year: 2022
venue: "IEEE Access"
authors:
  - "Hironori Murase"
  - "Kenji Fukumizu"
status: processed
processed_at: 2026-06-11
topics:
  - "anomaly detection"
  - "pseudo anomaly generation"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Magnetic Tile Defects]]"
methods:
  - "[[ALGAN]]"
  - "[[GAN]]"
  - "[[DCGAN]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "GANomaly"
  - "Skip-GANomaly"
  - "PatchCore"
  - "DifferNet"
doi: "10.1109/access.2022.3169594"
url: "https://doi.org/10.1109/access.2022.3169594"
pdf: "paper-inbox/10_processed/Research/2022 - Murase - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables.pdf"
hardware: "NVIDIA A100-SXM4 40GB GPU"
code: "not reported"
data: "uses MVTec AD, Magnetic Tile Defects, and COIL-100"
related_methods:
  - "[[ALGAN]]"
  - "[[GAN]]"
related_datasets:
  - "[[Magnetic Tile Defects]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/10_processed/Research/2022 - Murase - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Murase - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Murase - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables.txt"
tags:
  - paper
---
# ALGAN: Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables

## Summary

The paper proposes [[ALGAN]], a GAN-based anomaly detection method that creates pseudo-anomalous samples by sampling anomalous latent-variable states. The discriminator learns to distinguish real normal data from generated fake-normal and pseudo-anomalous data, then supplies anomaly scores. The evaluation includes MVTec AD, [[Magnetic Tile Defects]], and COIL-100.

## Paper Type

- Type: research.
- Why: The paper proposes a generative anomaly detection method and reports quantitative AUROC comparisons.

## Problem

- Task: normal-only anomaly detection.
- Setting: visual anomaly detection where anomalous examples are unavailable during training.
- Inputs: normal images or pretrained image features.
- Outputs: image-level anomaly scores.

## Contribution

- Claimed: Pseudo-anomalous latent variables let a GAN discriminator learn a boundary between normal and anomaly-like samples without real anomalies.
- Shown: On [[Magnetic Tile Defects]], ALGAN-image reports 0.956 AUROC using image data, higher than GANomaly and Skip-GANomaly in the same table.
- Shown: An MVTec AD ablation improves average AUROC from 0.643 without pseudo-anomaly mechanisms to 0.878 with both buffered data and anomalous latent data.

## Method

- Generator: produces fake-normal and pseudo-anomalous samples from normal and anomalous latent states.
- Discriminator: trained with real normal data, fake-normal data, and pseudo-anomalous data; output becomes the anomaly score.
- Variants: ALGAN-image uses a DCGAN-like convolutional architecture; ALGAN-feature uses WideResNet101 features and fully connected layers.
- Optimization: Adam with beta1 0, beta2 0.9; generator learning rate 2e-4; discriminator learning rate 1e-4; batch size 16; latent dimension 100; sigma 4.
- Training: ALGAN-image 512 epochs and ALGAN-feature 192 epochs.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| Image-data anomaly detection | [[Magnetic Tile Defects]] | [[AU-ROC]] | GANomaly 0.683 | ALGAN-image 0.956 | Higher is better. |
| Image-data anomaly detection | [[Magnetic Tile Defects]] | [[AU-ROC]] | Skip-GANomaly 0.504 | ALGAN-image 0.956 | Higher is better. |
| MVTec ablation | MVTec AD | [[AU-ROC]] | no buffered or anomalous latent data 0.643 | both mechanisms 0.878 | Average AUROC table. |

## Dataset / Benchmark Details

- [[Magnetic Tile Defects]]: 952 defect-free normal images and 392 anomalous images across five defect types.
- MVTec AD: normal-only training set with category-specific test anomalies.
- COIL-100: object-image anomaly detection setup with selected normal and anomalous categories.

## Limitations

- Rotation-heavy MVTec categories such as hazelnut and screw are weaker than comparison methods.
- The paper notes that ALGAN-feature with only the last WideResNet block may miss relevant Magnetic Tile Defects features.
- Code availability: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[ALGAN]], [[GAN]], [[DCGAN]], [[Synthetic data generation]]
- Datasets: [[Magnetic Tile Defects]]
- Domains: [[Metal inspection]]
- Metrics: [[AU-ROC]]

### Relationship Notes

- Shares dataset: [[Magnetic Tile Defects]].
- Shares method: [[ALGAN]], [[GAN]], [[DCGAN]], and [[Synthetic data generation]].
- Shares metric: [[AU-ROC]].
- Application/domain: [[Metal inspection]].

## Questions

- Would shallower pretrained features improve ALGAN-feature on magnetic-tile defects?
- How sensitive is the pseudo-anomalous latent distribution to sigma and buffer settings?
