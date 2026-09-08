---
title: "A Survey of Defect Detection Applications Based on Generative Adversarial Networks"
aliases:
  - "A Survey of Defect Detection Applications Based on GAN"
paper_key: "doi:10.1109/access.2022.3217227"
paper_type: review
year: 2022
venue: "IEEE Access"
authors:
  - "Xiangjie He"
  - "Zhengwei Chang"
  - "Linghao Zhang"
  - "Houdong Xu"
  - "Hongbo Chen"
  - "Zhongqiang Luo"
status: processed
processed_at: 2026-05-31
topics:
  - "GAN defect detection"
  - "defect detection survey"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
methods:
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
metrics: []
primary_metric: "not applicable"
doi: "10.1109/access.2022.3217227"
url: "https://doi.org/10.1109/ACCESS.2022.3217227"
pdf: "paper-inbox/10_processed/Review/2022 - He - A Survey of Defect Detection Applications Based on Generative Adversarial Networks.pdf"
related_methods:
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
source_file: "paper-inbox/10_processed/Review/2022 - He - A Survey of Defect Detection Applications Based on Generative Adversarial Networks.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - He - A Survey of Defect Detection Applications Based on Generative Adversarial Networks.md"
extracted_text: "paper-inbox/90_processing/text/2022 - He - A Survey of Defect Detection Applications Based on Generative Adversarial Networks.txt"
artifact_status: "review"
tags:
  - paper
---

# A Survey of Defect Detection Applications Based on Generative Adversarial Networks

## Summary

This review surveys GAN theory, GAN variants, and GAN-based defect detection applications. It frames GANs as useful for defect detection because they can learn normal or defect distributions, generate pseudo-samples, and reduce the effect of scarce and imbalanced defect data.

## Paper Type

- Type: review.
- Why: It synthesizes GAN-based defect detection literature rather than reporting a new textile experiment.

## Review / Survey Details

- Scope: GAN and GAN variants used for defect detection across industrial products, textiles, roads, agriculture, and other visual inspection domains.
- Inclusion criteria: not fully reported in extracted source.
- Taxonomy: GAN principles and variants, development of GAN-based defect detection, application domains, limitations, and future directions.
- Textile relevance: the survey explicitly includes textiles as one of the GAN defect detection application fields and cites fabric defect detection work using supervised discriminant learning and GAN-related methods.
- Dataset relevance: the review does not itself introduce or evaluate a textile dataset.
- Synthesis relevance: GANs are discussed as a way to generate defect samples, learn feature representations, and train with normal-only data.

## Methodological Patterns

- GANs are used to generate defect samples when defect images are rare.
- Reconstruction-style GANs learn normal samples and detect defects by reconstruction differences.
- GAN variants such as cGAN, DCGAN, WGAN, and CycleGAN are repeatedly adapted for defect detection.

## Limitations

- Stated: GAN training can face instability, mode collapse, and application-specific challenges.
- Inferred: as a review, it is a reference-mining source rather than evidence that a particular public textile dataset benefits from synthesis.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Datasets: not applicable; review covers methods rather than running a dataset benchmark
- Methods: [[GAN]], [[Synthetic data generation]], [[Data augmentation]]
- Domains: [[Multi-industry anomaly detection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Data Augmentation Method for Fabric Defect Detection]] | Follow-up reading | Textile-specific GAN augmentation study found in the same research neighborhood. |
| [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]] | Follow-up reading | Later fabric-specific cGAN augmentation work. |

## Questions

- Which textile-specific GAN studies in the survey use public datasets rather than private industrial data?
