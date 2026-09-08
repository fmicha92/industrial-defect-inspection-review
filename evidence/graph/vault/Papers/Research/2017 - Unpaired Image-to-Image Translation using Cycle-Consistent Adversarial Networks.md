---
title: "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks"
aliases:
  - "CycleGAN paper"
paper_key: "arxiv:2863.01000"
paper_type: research
year: 2017
venue: "ICCV 2017"
authors:
  - "Jun-Yan Zhu"
  - "Taesung Park"
  - "Phillip Isola"
  - "Alexei A. Efros"
status: processed
processed_at: 2026-06-02
topics:
  - image-to-image translation
  - unpaired translation
  - generative adversarial networks
tasks:
  - "[[Image-to-image translation]]"
datasets:
  - "[[Cityscapes]]"
domains:
  - "[[General computer vision]]"
methods:
  - "[[CycleGAN]]"
  - "[[GAN]]"
  - "[[Learned generative synthesis]]"
metrics:
  - "[[IoU]]"
  - "[[Accuracy]]"
related_concepts:
  - "[[Learned generative synthesis]]"
related_methods:
  - "[[CycleGAN]]"
  - "[[Pix2Pix]]"
  - "[[GAN]]"
doi: "not reported"
arxiv: "1703.10593"
url: "https://arxiv.org/abs/1703.10593"
pdf: "paper-inbox/10_processed/Research/2017 - Zhu - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.pdf"
source_file: "paper-inbox/10_processed/Research/2017 - Zhu - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2017 - Zhu - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.md"
extracted_text: "paper-inbox/90_processing/text/2017 - Zhu - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.txt"
artifact_status: "processed"
tags:
  - paper
  - gan
  - image-translation
---

# Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks

## Summary

Zhu et al. introduce [[CycleGAN]], an unpaired image-to-image translation framework. It learns mappings between two image domains with adversarial losses and cycle-consistency losses, enabling translation without paired examples.

## Paper Type

Research paper. It introduces a general-purpose unpaired image translation method and evaluates it across perceptual, segmentation, and qualitative tasks.

## Problem

Image-to-image translation is easier with paired examples, but paired data are often unavailable or expensive. The paper addresses how to learn mappings from unordered sets of source and target domain images.

## Contribution

- Claimed: adversarial losses plus cycle consistency constrain unpaired translation enough to learn useful mappings.
- Shown: CycleGAN outperforms CoGAN, BiGAN/ALI, pixel-loss plus GAN, and feature-loss plus GAN baselines on reported maps/photos and Cityscapes evaluations.
- Shown: removing either adversarial loss or cycle consistency degrades results.

## Method

The method trains two mappings, G: X to Y and F: Y to X, with discriminators for both domains. Adversarial losses make translated images match target-domain distributions. Cycle-consistency losses encourage x -> G(x) -> F(G(x)) to reconstruct x and y -> F(y) -> G(F(y)) to reconstruct y.

## Evidence

| Evaluation | Metric | Direction | Baseline | CycleGAN |
|---|---|---|---|---|
| Maps to aerial photos AMT realism | percent labeled real | higher | CoGAN 0.6%, BiGAN/ALI 2.1%, pixel loss + GAN 0.7%, feature loss + GAN 1.2% | 26.8% |
| Aerial photos to maps AMT realism | percent labeled real | higher | CoGAN 0.9%, BiGAN/ALI 1.9%, pixel loss + GAN 2.6%, feature loss + GAN 0.3% | 23.2% |
| Cityscapes labels to photos | class IoU | higher | best listed baseline 0.06; pix2pix 0.18 | 0.11 |
| Cityscapes photos to labels | class IoU | higher | best listed baseline 0.08; pix2pix 0.32 | 0.16 |

## ML/DL Extraction

- Architecture: generator architecture adapted from Johnson et al.; discriminators use 70 x 70 PatchGANs.
- Objective: adversarial losses for both directions plus cycle-consistency loss; least-square GAN loss is used for stability.
- Training stabilization: discriminator updates use a history buffer of 50 previously generated images.
- Code: the paper text reports `https://github.com/junyanz/CycleGAN`.

## Limitations

- Results are not uniformly successful.
- The method struggles with large geometric changes, such as dog-to-cat transfiguration in the reported failure cases.
- The paper notes a gap between unpaired results and paired pix2pix results.

## Connections

### Graph Hubs

- Methods: [[CycleGAN]], [[GAN]], [[Learned generative synthesis]]
- Tasks: [[Image-to-image translation]]
- Datasets: [[Cityscapes]]
- Domains: [[General computer vision]]
- Metrics: [[IoU]], [[Accuracy]]
- Related methods: [[Pix2Pix]]

### Hybrid Fit

Does not itself fit [[Hybrid generative-procedural synthesis]]. CycleGAN is a learned unpaired translation method. It becomes part of a hybrid approach when paired with a simulator or procedural renderer, as in [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] | Used by | Uses Cyclic-GAN refinement on procedurally rendered industrial object images. |
| [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] | Shares method family | Both use adversarial image refinement/translation with unpaired real images, but SimGAN is explicitly simulator-label preserving. |

## Questions

- Which industrial inspection settings need semantic or geometric constraints beyond cycle consistency?
