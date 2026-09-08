---
title: "Learning from Simulated and Unsupervised Images through Adversarial Training"
aliases:
  - "Simulated+Unsupervised learning"
  - "SimGAN"
paper_key: "arxiv:1024.02000"
paper_type: research
year: 2017
venue: "CVPR 2017"
authors:
  - "Ashish Shrivastava"
  - "Tomas Pfister"
  - "Oncel Tuzel"
  - "Josh Susskind"
  - "Wenda Wang"
  - "Russ Webb"
status: processed
processed_at: 2026-06-02
topics:
  - simulated-to-real transfer
  - adversarial refinement
  - synthetic data generation
tasks:
  - "[[Gaze estimation]]"
  - "[[Hand pose estimation]]"
datasets:
  - "[[UnityEyes]]"
  - "[[MPIIGaze]]"
  - "[[NYU hand pose dataset]]"
domains:
  - "[[Human-computer interaction]]"
methods:
  - "[[SimGAN]]"
  - "[[Hybrid generative-procedural synthesis]]"
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[Gaze estimation error]]"
  - "[[Hand pose threshold accuracy]]"
related_concepts:
  - "[[Domain gap]]"
  - "[[Hybrid generative-procedural synthesis]]"
related_methods:
  - "[[SimGAN]]"
  - "[[GAN]]"
doi: "not reported"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2017 - Shrivastava - Learning from Simulated and Unsupervised Images through Adversarial Training.pdf"
source_file: "paper-inbox/10_processed/Research/2017 - Shrivastava - Learning from Simulated and Unsupervised Images through Adversarial Training.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2017 - Shrivastava - Learning from Simulated and Unsupervised Images through Adversarial Training.md"
extracted_text: "paper-inbox/90_processing/text/2017 - Shrivastava - Learning from Simulated and Unsupervised Images through Adversarial Training.txt"
artifact_status: "processed"
tags:
  - paper
  - synthetic-data
  - gan
---

# Learning from Simulated and Unsupervised Images through Adversarial Training

## Summary

Shrivastava et al. propose Simulated+Unsupervised learning and implement it as [[SimGAN]], a refiner network that turns simulator images into more realistic images using unlabeled real data while preserving simulator annotations. The method is a clear instance of [[Hybrid generative-procedural synthesis]]: labels and structure come from simulators, while a learned adversarial refiner models real-image appearance.

## Paper Type

Research paper. It introduces an adversarial synthetic-data refinement method and evaluates it on gaze estimation and hand pose estimation.

## Problem

Synthetic images can provide automatic labels, but models trained on them may fail on real images because synthetic and real image distributions differ. The paper addresses this [[Domain gap]] without requiring labeled real images.

## Contribution

- Claimed: S+U learning improves simulator realism using unlabeled real data while preserving synthetic annotations.
- Claimed: SimGAN stabilizes adversarial refinement with self-regularization, local adversarial loss, and a history buffer of refined images.
- Shown: Refined synthetic images improve gaze estimation on MPIIGaze and hand pose estimation on NYU hand pose relative to unrefined synthetic images.

## Method

SimGAN takes a simulator image as input and applies a fully convolutional refiner network. The refiner is trained with an adversarial loss against a discriminator plus a self-regularization loss that penalizes large changes from the original synthetic image so labels remain valid. The discriminator operates locally on image patches, and training uses a buffer of previously refined images to reduce adversarial instability.

## Evidence

| Result | Dataset / task | Metric | Direction | Baseline | SimGAN result |
|---|---|---|---|---|---|
| Visual realism user study | Refined eye images | human classification accuracy | closer to chance is better | original synthetic vs real: 162/200 correct | real vs refined: 517/1000 correct, 51.7% |
| Gaze estimation threshold | [[MPIIGaze]] / [[Gaze estimation]] | percentage within 7 degrees | higher | synthetic 4x: 64.9% | refined synthetic 4x: 87.2% |
| Mean gaze error | [[MPIIGaze]] / [[Gaze estimation]] | [[Gaze estimation error]] | lower | CNN with UnityEyes synthetic images: 11.2 degrees | CNN with UnityEyes refined images: 7.8 degrees |
| Hand pose threshold | [[NYU hand pose dataset]] / [[Hand pose estimation]] | [[Hand pose threshold accuracy]] at 5 pixels | higher | synthetic data 3x: 77.7%; real data: 74.5% | refined synthetic data 3x: 83.3% |

## ML/DL Extraction

- Architecture: fully convolutional refiner network with ResNet blocks; discriminator is a convolutional patch discriminator.
- Objective: adversarial realism loss plus self-regularization loss.
- Training: refiner and discriminator are trained alternately; discriminator updates use a history of refined images.
- Data: UnityEyes synthetic eye images, MPIIGaze real eye images, and NYU hand pose depth images.
- Artifacts: public code or dataset release not reported in the extracted source.

## Limitations

- The method depends on simulators that already preserve useful labels.
- Self-regularization can restrict refinement when synthetic and real distributions differ substantially.
- The paper reports single-image refinement; it lists video refinement and noise distribution modeling as future work.

## Connections

### Graph Hubs

- Methods: [[SimGAN]], [[Hybrid generative-procedural synthesis]], [[GAN]], [[Synthetic data generation]]
- Tasks: [[Gaze estimation]], [[Hand pose estimation]]
- Datasets: [[UnityEyes]], [[MPIIGaze]], [[NYU hand pose dataset]]
- Domains: [[Human-computer interaction]]
- Metrics: [[Gaze estimation error]], [[Hand pose threshold accuracy]]
- Concepts: [[Domain gap]]

### Hybrid Fit

Fits [[Hybrid generative-procedural synthesis]]. The simulator provides labeled synthetic images and the GAN-like refiner learns real-image appearance from unlabeled real images.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2018 - RenderGAN Generating Realistic Labeled Data]] | Shares method | Both preserve labels from a synthetic generator while learning realism from unlabeled real data. |
| [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] | Follow-up / shares method | Both refine synthetic rendered images with adversarial training for downstream real-world performance. |

## Questions

- How robust is the annotation-preservation assumption when the refiner is applied to larger geometric transformations?
