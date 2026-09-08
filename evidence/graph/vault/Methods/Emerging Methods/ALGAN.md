---
title: "ALGAN"
aliases:
  - "Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2022 - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables]]"
evidence_count: 1
tags:
  - method
---
# ALGAN

## Definition

ALGAN is a GAN-based anomaly detection method that generates fake-normal and pseudo-anomalous samples by changing latent-variable states. The discriminator learns from real normal data, fake-normal data, and pseudo anomalies, then supplies the anomaly score.

## Why It Matters

It creates pseudo-anomalous supervision when only normal training images are available, supporting anomaly detection on industrial image datasets such as [[Magnetic Tile Defects]].

## Used In These Papers

- [[2022 - ALGAN Anomaly Detection by Generating Pseudo Anomalous Data via Latent Variables]] evaluates ALGAN-image and ALGAN-feature on MVTec AD, [[Magnetic Tile Defects]], and COIL-100.

## Related Concepts

- [[GAN]]
- [[DCGAN]]
- [[Synthetic data generation]]
- [[Industrial anomaly detection]]
