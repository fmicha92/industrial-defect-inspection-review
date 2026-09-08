---
title: "DPG-DT: Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT"
aliases:
  - "DPG-DT"
paper_key: "doi:10.1109/msn60784.2023.00049"
paper_type: research
year: 2023
venue: "IEEE MSN"
authors:
  - "Siyuan Li"
  - "Xi Lin"
  - "Gaolei Li"
  - "Lixing Chen"
  - "Siyi Liao"
  - "Jing Wang"
  - "Jianhua Li"
status: processed
processed_at: 2026-06-11
topics:
  - "differential privacy"
  - "generative digital twin"
  - "imbalanced learning"
  - "industrial IoT"
tasks:
  - "[[Defect classification]]"
domains:
  - "[[Metal inspection]]"
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[NEU-CLS]]"
  - "[[DeepPCB]]"
methods:
  - "[[DPG-DT]]"
  - "[[Synthetic data generation]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
metrics:
  - "[[Accuracy]]"
  - "[[FID]]"
  - "[[Inception Score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: downstream classifier accuracy on generated data; higher is better"
  - "FID: distribution distance for generated images; lower is better"
  - "Inception Score: generated image quality/diversity proxy; higher is better"
baselines:
  - "DP-DCGAN"
  - "DP-BigGAN"
  - "GS-WGAN"
doi: "10.1109/MSN60784.2023.00049"
url: "https://doi.org/10.1109/MSN60784.2023.00049"
data: "MNIST, Fashion-MNIST, [[NEU-CLS]], [[DeepPCB]]"
code: "not reported"
related_methods:
  - "[[DPG-DT]]"
  - "[[Synthetic data generation]]"
  - "[[GAN]]"
related_datasets:
  - "[[NEU-CLS]]"
  - "[[DeepPCB]]"
related_tasks:
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2023 - Li - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Li - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Li - DPG-DT Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT.txt"
artifact_status: "code not reported"
tags:
  - paper
---
# DPG-DT: Differentially Private Generative Digital Twin for Imbalanced Learning in Industrial IoT

## Summary

The paper proposes [[DPG-DT]], a privacy-preserving generative digital-twin framework for class-imbalanced industrial learning. Its PSIE model uses an energy-based generative process with differential privacy, rather than a standard GAN generator, to produce synthetic industrial images for downstream classification. The industrial evaluations use [[NEU-CLS]] and [[DeepPCB]], with additional MNIST and Fashion-MNIST experiments.

## Paper Type

- Type: research.
- Why: The paper proposes a generative synthetic-data framework and evaluates generated data quality and downstream classification.

## Problem

- Task: imbalanced visual classification in industrial IoT settings.
- Motivation: industrial defect/anomaly data are scarce, imbalanced, and privacy-sensitive, so direct sharing of real data is difficult.

## Contribution

- Claimed: DPG-DT generates privacy-preserving synthetic industrial images suitable for model training.
- Claimed: PSIE combines an energy-based model, Langevin MCMC sampling, and differential privacy mechanisms.
- Shown: downstream classifiers trained with DPG-DT data outperform private generative baselines, with the abstract reporting up to 23.9% improvement in industrial scenarios.

## Method

- Framework: private generative AI-empowered digital twin.
- Generator: PSIE, an energy-based generative model.
- Sampling: Langevin MCMC.
- Privacy: Gaussian noise and randomized response are used to support differential privacy.
- Baselines: DP-DCGAN, DP-BigGAN, and GS-WGAN.
- Synthetic data role: generated images are used for imbalanced downstream classification.

## Data

- [[NEU-CLS]]: industrial steel surface defect images from the NEU surface defect database.
- [[DeepPCB]]: PCB defect images; the paper uses generated 128 x 128 examples and reports experiments at privacy budget epsilon = 10.
- MNIST and Fashion-MNIST: non-industrial sanity-check datasets.

## Evidence

| Dataset | Task | Baseline result | Result after DPG-DT / PSIE | Metric | Notes |
|---|---|---:|---:|---|---|
| Industrial scenarios | downstream classification | private generative baselines | +23.9% over baselines | [[Accuracy]] | Abstract-level improvement; exact per-dataset values are not present in the extracted text. |
| [[NEU-CLS]] | generated-image quality and classification | DP-DCGAN / DP-BigGAN / GS-WGAN | DPG-DT reported as best | [[Accuracy]], [[FID]], [[Inception Score]] | Figures report comparative trends; numeric figure values are not preserved in the text extraction. |
| [[DeepPCB]] | generated-image quality | private generative baselines | DPG-DT produces private synthetic images at epsilon = 10 | [[FID]], [[Inception Score]] | DeepPCB is described as harder, with higher FID at larger resolutions. |

## ML / DL Extraction

- Task formulation: generate private synthetic images to improve imbalanced downstream classification.
- Model family: energy-based generative model in a digital-twin framework.
- Training/sampling: Langevin MCMC; privacy noise mechanisms.
- Metrics: [[Accuracy]], [[FID]], and [[Inception Score]].
- Baselines: DP-DCGAN, DP-BigGAN, GS-WGAN.
- Code: not reported.

## Limitations

- Exact numeric figure values are not preserved in the extracted text; only the abstract-level 23.9% improvement and qualitative trends are available.
- Future work: deploy DPG-DT/PSIE in real industrial digital-twin environments and compare with more private generative models.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]]
- Methods: [[DPG-DT]], [[Synthetic data generation]], [[GAN]], [[Data augmentation]]
- Datasets: [[NEU-CLS]], [[DeepPCB]]
- Domains: [[Metal inspection]], [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[FID]], [[Inception Score]]

### Relationship Notes

- Shares datasets: [[NEU-CLS]] and [[DeepPCB]].
- Shares task: [[Defect classification]] under class imbalance.
- Shares method family: [[Synthetic data generation]], [[GAN]] baselines, and [[Data augmentation]] for generated training data.
- Application/domains: [[Metal inspection]] and [[Semiconductor and electronics]].

## Questions

- What are the exact per-dataset classifier accuracies for NEU-CLS and DeepPCB?
- How does privacy budget epsilon affect the downstream accuracy-quality trade-off?
- Are PSIE implementation details sufficient to reproduce the exact training schedule?
