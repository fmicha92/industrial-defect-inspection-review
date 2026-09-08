---
title: "Diffusion Models in Vision: A Survey"
aliases:
  - "Diffusion Models in Vision"
paper_key: "doi:10.1109/tpami.2023.3261988"
paper_type: review
year: 2023
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
authors:
  - "Florinel-Alin Croitoru"
  - "Vlad Hondru"
  - "Radu Tudor Ionescu"
  - "Mubarak Shah"
status: processed
processed_at: 2026-06-02
topics:
  - diffusion models
  - generative modeling
  - computer vision
tasks:
  - "[[Generative modeling]]"
  - "[[Image-to-image translation]]"
  - "[[Scientific image generation]]"
datasets: []
domains:
  - "[[General computer vision]]"
methods:
  - "[[Diffusion models]]"
  - "[[Variational Autoencoder]]"
  - "[[GAN]]"
metrics:
  - "[[FID]]"
  - "[[Inception Score]]"
  - "[[Log likelihood]]"
related_methods:
  - "[[Diffusion models]]"
doi: "10.1109/TPAMI.2023.3261988"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Review/2023 - Croitoru - Diffusion Models in Vision A Survey.pdf"
source_file: "paper-inbox/10_processed/Review/2023 - Croitoru - Diffusion Models in Vision A Survey.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Croitoru - Diffusion Models in Vision A Survey.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Croitoru - Diffusion Models in Vision A Survey.txt"
artifact_status: "processed"
tags:
  - paper
  - review
  - diffusion-models
---

# Diffusion Models in Vision: A Survey

## Summary

Croitoru et al. review denoising diffusion models for computer vision. The survey organizes the field around three formulations--denoising diffusion probabilistic models, noise-conditioned score networks, and stochastic differential equations--and categorizes vision applications by task, denoising condition, architecture, and datasets.

## Paper Type

Review paper. It synthesizes theoretical formulations, relationships to other generative models, computer-vision applications, limitations, and future directions.

## Problem

Diffusion models were rapidly expanding across image generation and other vision tasks by 2023. The paper provides a structured map of the model family and its applications so researchers can locate related work by formulation and target task.

## Contribution

- Identifies three generic diffusion-modeling frameworks: DDPMs, NCSNs, and SDE-based score models.
- Relates diffusion models to VAEs, GANs, energy-based models, autoregressive models, and normalizing flows.
- Provides a multi-perspective taxonomy for diffusion models in computer vision.
- Summarizes limitations, especially slow inference due to many denoising steps.

## Method

The paper defines diffusion models as deep generative models with a forward diffusion stage that progressively adds Gaussian noise and a reverse stage that learns to recover data by reversing that process. The survey then reviews representative work by task, including unconditional and conditional image generation, super-resolution, inpainting, image editing, image-to-image translation, segmentation, anomaly detection, video generation, point-cloud generation, classification, and inverse problems.

## Evidence

The evidence is a literature synthesis rather than a new benchmark. The paper emphasizes that diffusion models produce high-quality and diverse samples, have surpassed GANs in many image-generation settings, and have been used beyond generation in representation-learning and discriminative settings such as segmentation, classification, and anomaly detection.

## ML/DL Extraction

- Model families: [[Diffusion models]], DDPMs, NCSNs, SDE-based score models.
- Related generative families: [[Variational Autoencoder]], [[GAN]], energy-based models, autoregressive models, and normalizing flows.
- Application tasks: image generation, super-resolution, inpainting, editing, image-to-image translation, semantic segmentation, classification, anomaly detection, video generation, point-cloud generation, and inverse problems.
- Metrics discussed through surveyed works include [[FID]], [[Inception Score]], and [[Log likelihood]].

## Limitations

- The most significant disadvantage identified is slow inference, because generating one sample often requires many denoising steps.
- Text-to-image conditioning through CLIP embeddings can inherit weaknesses such as poor spelling information.
- Long-term temporal consistency in text-to-video generation remains open.
- The paper calls for more efficient sampling, broader use in non-generation vision tasks, better use of latent representations for discriminative tasks, and multi-purpose diffusion models.

## Connections

### Graph Hubs

- Tasks: [[Generative modeling]], [[Image-to-image translation]], [[Scientific image generation]]
- Datasets: not applicable
- Domains: [[General computer vision]]
- Methods: [[Diffusion models]], [[Variational Autoencoder]], [[GAN]]
- Metrics: [[FID]], [[Inception Score]], [[Log likelihood]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2014 - Generative Adversarial Nets]] | Contrasts with | The survey repeatedly compares diffusion models to GANs, especially on sample quality, diversity, and inference speed. |
| [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] | Builds on | The survey treats early nonequilibrium-thermodynamics diffusion models as part of the DDPM lineage. |

## Questions

- Which industrial inspection tasks benefit most from diffusion representations rather than diffusion-generated training samples?
