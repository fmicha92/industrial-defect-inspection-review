---
title: "A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data"
aliases:
  - "Con-GAN"
  - "A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data"
paper_key: "doi:10.1109/tim.2022.3232649"
paper_type: research
year: 2023
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Zongwei Du"
  - "Liang Gao"
  - "Xinyu Li"
status: processed
processed_at: 2026-05-23
topics:
  - "contrastive GAN"
  - "limited data defect recognition"
  - "data augmentation"
tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[NEU-CLS]]"
  - "[[PCB defect recognition dataset]]"
methods:
  - "[[Contrastive GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[Contrastive GAN]]"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[FID]]"
  - "[[MMD]]"
  - "[[Inference time]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
  - "F1 = 2TP / (2TP + FP + FN)"
baselines:
  - "no augmentation"
  - "classic color augmentation"
  - "classic geometric augmentation"
  - "color-geometric augmentation"
  - "WGAN-LP"
  - "SAGAN"
  - "Hinge GAN"
benchmarks:
  - "[[NEU-CLS]]"
  - "[[PCB defect recognition dataset]]"
code: "not reported"
data: "NEU-CLS public; PCB case availability not reported"
doi: "10.1109/tim.2022.3232649"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2023 - Du - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data.pdf"
related_papers:
  - "[[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Synthetic data generation]]"
related_methods:
  - "[[Contrastive GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Learned generative synthesis]]"
related_datasets:
  - "[[NEU-CLS]]"
  - "[[PCB defect recognition dataset]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Du - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Du - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Du - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data.txt"
artifact_status: "not reported"
tags:
  - paper
  - gan-augmentation
  - surface-defect-recognition
---
# A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data

## Summary

- The paper proposes Con-GAN, a contrastive GAN for generating defect images when only a small number of defective samples are available.
- The method uses generated defects as offline augmentation for surface defect recognition networks.
- Experiments evaluate generated-image quality and recognition performance on [[NEU-CLS]], then apply the same pipeline to a real-world PCB defect recognition case.

## Paper Type

- Type: research.
- Why: The source proposes a new GAN training method, evaluates it against GAN and augmentation baselines, and applies it to industrial defect recognition.

## Problem

- Task: [[Defect classification]], [[Surface defect detection]]
- Setting: [[Multi-industry anomaly detection]]
- Inputs: limited labeled surface-defect images; NEU-CLS GAN inputs are scaled to 64 x 64 and recognition-network inputs to 224 x 224 RGB.
- Outputs: generated defect images and defect class predictions.
- Motivation: GAN-based augmentation can improve defect recognition, but conventional GANs can overfit, collapse modes, or generate poor details under scarce defect samples.
- Assumptions: the synthesis stage is offline, and generated images are not filtered before being used for recognition training.

## Contribution

- Claimed: Con-GAN can generate high-quality and diverse defect images from extremely limited defective samples, including ten samples per class, without auxiliary defect-free images.
- Claimed: Shared data augmentation helps avoid discriminator overfitting, feature attention matching improves generated quality, and sphere contrastive loss pushes generated images beyond ordinary classical transforms.
- Shown: Con-GAN reports the best average FID and MMD over the compared GANs in the limited NEU-CLS settings, improves pretrained recognition networks, and reaches 91.84% accuracy in the PCB case.

## Method

- Generator/discriminator backbone: based on SAGAN, with self-attention and spectral normalization choices following the source configuration.
- Shared data augmentation (SDA): applies the same random transform to real and generated images before discriminator input.
- Feature attention matching (FAM): aligns features extracted from real and generated images and supports the feature-matching loss.
- Objective: adversarial loss, feature-matching loss, and sphere contrastive loss.
- Recognition pipeline: train Con-GAN per defect class, generate synthetic images, mix generated samples with classical augmentations, and fine-tune pretrained ResNet18, MobileNet, or EfficientNet recognition networks.

## Evidence

### Experimental Setup

- Public dataset: [[NEU-CLS]], 1,800 hot-rolled steel surface defect images, six classes, 300 images per class, 200 x 200 resolution.
- NEU-CLS split: 1:1 train/test; limited training sets use 50, 30, or 10 images per class sampled with replacement from the training set.
- PCB case: five defect classes from a Chinese electronics manufacturing company; only 50 training samples per defect are available.
- GAN training: 10,000 epochs, about 1 hour; generator learning rate 0.0004, discriminator learning rate 0.0001, Adam beta1 0.0 and beta2 0.9.
- Recognition training: 50 epochs; cross-entropy loss; NEU-CLS uses SGD with learning rate 0.001; PCB case uses Adam.
- Hardware: RTX 3080Ti 12 GB GPU and Intel Core i9-10980XE CPU reported for the public-dataset experiments.

### Main Results

- Generated quality: Con-GAN reports the best average FID and MMD on all NEU-CLS limited-data settings; the source states average FID improves by 3.19-36.17 and MMD by 0.04-0.13 over compared GANs.
- Recognition: compared with no augmentation, Con-GAN improves NEU-CLS recognition accuracy by 0.44%-4.88% and F1 by 0.005-0.049 across tested models and limited-data settings.
- NEU-CLS headline: recognition accuracies range from 95.00% to 99.56% for different limited-data settings and pretrained models.
- PCB case: Con-GAN reaches 91.84% accuracy and reports ResNet18 inference at about 2.31 ms per image.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Defect recognition | (TP + TN) / (TP + TN + FP + FN) | higher | yes | Used for NEU-CLS and PCB recognition comparisons. |
| [[F1-score]] | Defect recognition | 2TP / (2TP + FP + FN) | higher | no | Paired with accuracy because F1 is less affected by class distribution. |
| [[FID]] | Generated defect-image quality | Distribution distance between real and generated Inception-v3 features | lower | no | Used to compare Con-GAN with DCGAN, DRAGAN, LSGAN, SAGAN, WGAN-LP, RAGAN, SphereGAN, and Hinge. |
| [[MMD]] | Generated defect-image quality | Kernel maximum mean discrepancy over Inception-v3 features | lower | no | Used with FID to assess generated-image quality and variance relative to real images. |
| [[Inference time]] | PCB recognition runtime | Milliseconds per image | lower | no | ResNet18 reports approximately 2.31 ms per image in the PCB case. |

## Data

- [[NEU-CLS]]: six classes, crazing, inclusion, patches, pitted surface, rolled-in scale, and scratches.
- [[PCB defect recognition dataset]]: five typical PCB defect classes, copper short, short, open, near open, and near short.
- Synthetic data: NEU-CLS recognition experiments generate 1,500 synthetic samples per class; the PCB case generates 500 images per defect and expands original samples to 1,000 images per defect.
- Preprocessing: GAN inputs are normalized to [-1, 1]; recognition images are resized to 224 x 224 with three RGB channels.

## Evaluation

- Generation baselines: DCGAN, DRAGAN, LSGAN, SAGAN, WGAN-LP, RAGAN, SphereGAN, and Hinge.
- Recognition baselines: no augmentation, color transforms, geometric transforms, combined color-geometric transforms, WGAN-LP, SAGAN, and Hinge synthetic augmentation.
- PCB baselines: SVM, MobileNet, EfficientNet, ResNet18, ResNet50, and ResNet18 with classic augmentation.
- The source reports independent repeated runs: three times for NEU-CLS recognition comparisons and five times for the PCB comparison.

## Limitations

- Generated images are not selected or filtered before entering the recognition network.
- Con-GAN training is time-consuming and offline.
- Inclusion defects in NEU-CLS have large intraclass variation, making them harder for the GAN to model.
- Accuracy can decrease when too many augmented images introduce distribution-shift or noisy examples.

## Reproducibility

- Code: not reported.
- Data: [[NEU-CLS]] is public; PCB case availability is not reported.
- Hyperparameters: key GAN, recognition, and augmentation mixing settings are reported.
- Random seeds: not reported.
- Environment: RTX 3080Ti 12 GB GPU and Intel Core i9-10980XE CPU.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Surface defect detection]]
- Methods: [[Contrastive GAN]], [[GAN]], [[Data augmentation]], [[Learned generative synthesis]]
- Datasets: [[NEU-CLS]], [[PCB defect recognition dataset]]
- Benchmarks: [[NEU-CLS]], [[PCB defect recognition dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Accuracy]], [[F1-score]], [[FID]], [[MMD]], [[Inference time]]
- Concepts: [[Synthetic data generation]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] | Contrasts with | Both address limited industrial defect data through augmentation; Con-GAN learns synthetic defect generation for recognition, while ALADA learns automatic augmentation policies for detection. |
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Shares method family | Both use GAN-based defect synthesis to improve automated inspection under scarce defect examples. |

### Backlinks Updated

- [[NEU-CLS]] links this paper as a limited-data Con-GAN recognition benchmark user.
- [[Contrastive GAN]] links this paper as the defining Con-GAN method note.
- [[Data augmentation]] links this paper as learned generative augmentation for defect recognition.
- [[FID]], [[MMD]], [[Accuracy]], [[F1-score]], and [[Inference time]] link this paper as a metric user.

## Questions

- Would filtering generated images before recognition training reduce noisy synthetic samples?
- How sensitive are the reported gains to the transformed/synthetic mixing ratio outside NEU-CLS and PCB defects?
