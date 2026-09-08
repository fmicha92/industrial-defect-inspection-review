---
title: "Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection"
aliases:
  - "GANs for Data Augmentation in Structural Adhesive Inspection"
paper_key: "sha256:130a402382d6f28756db7bd320aa38d95cfacc37e733fdc6566bba05c6a932bf"
paper_type: research
year: 2021
venue: "Applied Sciences"
authors:
  - "Ricardo Silva Peres"
  - "Miguel Azevedo"
  - "Sara Oleiro Araujo"
  - "Magno Guedes"
  - "Fabio Miranda"
  - "Jose Barata"
status: processed
processed_at: 2026-06-06
topics:
  - GAN data augmentation
  - structural adhesive inspection
  - object detection
  - scarce defect data
tasks:
  - "[[Adhesive bead defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Automotive manufacturing]]"
datasets:
  - "[[Structural Adhesive Defects Dataset]]"
dataset_sizes:
  - "143 real 1024 x 1024 adhesive defect images for GAN training"
  - "536 generated synthetic images"
  - "594 real-plus-synthetic object-detection training images"
  - "58 real validation images"
  - "19 real holdout images reported in the paper"
methods:
  - "[[GAN]]"
  - "[[StyleGAN2]]"
  - "[[GAN-based surface defect augmentation]]"
  - "[[YOLOv4]]"
  - "StyleGAN2-ADA"
  - "YOLOv4-Tiny"
model_family:
  - "[[Generative Models]]"
  - "[[Computer Vision Models]]"
architectures:
  - "[[StyleGAN2]]"
  - "[[YOLOv4]]"
training_regime:
  - transfer learning
  - data augmentation
synthetic_data:
  - "536 StyleGAN2-ADA generated structural adhesive defect images"
metrics:
  - "[[mAP@0.15]]"
  - "[[mAP@0.30]]"
  - "[[mAP@0.50]]"
  - "[[Average precision]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "YOLOv4-Tiny trained on 58 real images"
  - "YOLOv4-Tiny trained on 536 synthetic images"
  - "YOLOv4-Tiny trained on simulation-augmented data"
code: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive"
data: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0"
doi: "10.3390/app11073086"
url: "https://www.mdpi.com/2076-3417/11/7/3086"
pdf: "paper-inbox/10_processed/Research/2021 - Peres - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Peres - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Peres - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Peres - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection.txt"
artifact_status: "code, data, model weights, and configurations reported publicly available on GitHub"
related_papers:
  - "[[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[GAN-based surface defect augmentation]]"
  - "[[Learned generative synthesis]]"
related_methods:
  - "[[GAN]]"
  - "[[StyleGAN2]]"
  - "[[YOLOv4]]"
related_datasets:
  - "[[Structural Adhesive Defects Dataset]]"
related_domains:
  - "[[Automotive manufacturing]]"
related_tasks:
  - "[[Adhesive bead defect detection]]"
  - "[[Object detection]]"
tags:
  - paper
  - synthetic-data
  - gan
  - object-detection
---

# Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection

## Summary

The paper evaluates GAN-based data augmentation for structural adhesive inspection in an automotive pilot cell. It trains StyleGAN2-ADA on 143 cropped real adhesive defect images, generates 536 synthetic defect images, and uses the generated data to augment a YOLOv4-Tiny object detector for discontinuity and blob/excess adhesive defects. The augmented detector improves mAP across validation and holdout sets, with the largest gains on the harder holdout set and on the minority excess-defect class.

## Paper Type

Research paper. It proposes and evaluates a learned synthetic-data generation workflow for object detection under scarce manufacturing defect data.

## Problem

Structural adhesive inspection in automotive manufacturing is hard to automate because destructive testing is costly and defect data are scarce, imbalanced, and difficult to collect. The paper focuses on detecting discontinuities and blobs/excess material in adhesive bead images before downstream bonding makes correction difficult.

## Contribution

- Claimed: StyleGAN2-ADA can generate realistic structural adhesive defect images from a small real dataset and reduce the burden of collecting scarce defect examples.
- Shown: YOLOv4-Tiny trained on the real-plus-GAN augmented set outperforms models trained on synthetic-only, real-only, and simulation-augmented sets on mAP at IoU thresholds 0.15, 0.30, and 0.50.
- Shown: GAN augmentation especially improves the minority excess-defect class on the holdout set, where AP@0.50 rises from 0.2829 for real-only training to 0.5864 for GAN-augmented training.

## Method

- Data source: images were collected in a structural adhesive application cell at Introsys S.A. in Castelo Branco, Portugal, with an ABB IRB 2400 robotic adhesive application station and downstream visual quality inspection using two Teledine cameras.
- Defect types: discontinuity and blob/excess adhesive.
- GAN training set: 143 real adhesive defect images cropped to 1024 x 1024 and centered on the adhesive bead.
- Generator: StyleGAN2-ADA using NVIDIA's implementation, initialized from an FFHQ 1024 x 1024 pretrained model via transfer learning.
- GAN training hardware and runtime: one NVIDIA Tesla V100 GPU, approximately eight hours.
- Synthetic generation: 536 synthetic adhesive defect images generated with varied seeds and truncation values; inference averaged 105 images per minute on the same setup.
- Object detection model: YOLOv4-Tiny trained in Darknet for 6000 iterations.
- Real object-detection data: 116 real images with contemplated defect types, split 50/50 into training and validation sets.
- Augmented object-detection training: 58 real training images plus generated images, yielding 594 1024 x 1024 training images annotated manually with LabelImg.
- Class balancing: the real training set contains 75 discontinuity and 34 excess instances; the augmented set contains 582 discontinuity and 580 excess instances.

## Evidence

| Evidence | Reported detail |
|---|---|
| Public artifact host | GitHub repository `RicardoSPeres/GAN_Synth_Adhesive` |
| Dataset release | [[Structural Adhesive Defects Dataset]] v1.0 release, published 2021-03-30 |
| Validation set | 58 real images with 60 discontinuity and 60 excess instances |
| Holdout set | Paper reports 19 real images with 40 discontinuity and 17 excess instances |
| Augmented validation mAP | 0.9131 mAP@0.15, 0.8569 mAP@0.30, 0.7708 mAP@0.50 |
| Augmented holdout mAP | 0.7675 mAP@0.15, 0.7256 mAP@0.30, 0.5788 mAP@0.50 |
| Real-only holdout mAP | 0.5986 mAP@0.15, 0.5249 mAP@0.30, 0.4125 mAP@0.50 |
| Synthetic-only result | Worst performance across all tests, showing that real data remains important |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP@0.15]] | Object detection on validation and holdout sets | Mean average precision at IoU 0.15 | Higher is better | no | GAN-augmented: 0.9131 validation, 0.7675 holdout |
| [[mAP@0.30]] | Object detection on validation and holdout sets | Mean average precision at IoU 0.30 | Higher is better | no | GAN-augmented: 0.8569 validation, 0.7256 holdout |
| [[mAP@0.50]] | Object detection on validation and holdout sets | Mean average precision at IoU 0.50 | Higher is better | yes | GAN-augmented: 0.7708 validation, 0.5788 holdout; real-only: 0.7221 validation, 0.4125 holdout |
| [[Average precision]] | Per-class AP at IoU 0.50 | Average precision by defect class | Higher is better | no | Holdout excess AP improves from 0.2829 real-only to 0.5864 GAN-augmented |

## ML/DL Extraction

| Field | Extracted detail |
|---|---|
| Task formulation | Object detection of structural adhesive bead discontinuity and excess/blob defects |
| Input | 1024 x 1024 structural adhesive bead images |
| Output | Bounding boxes and defect classes for adhesive defects |
| Generator architecture | StyleGAN2-ADA |
| Detector architecture | YOLOv4-Tiny |
| Training objective | GAN adversarial training and YOLO object-detection training; exact detector loss terms not reported |
| Pretraining | StyleGAN2-ADA transfer learning from FFHQ 1024 x 1024 pretrained model |
| Optimizer | not reported |
| Hyperparameters | YOLOv4-Tiny trained for 6000 iterations; GAN truncation values varied for generation |
| Compute | single NVIDIA Tesla V100 GPU |
| Evaluation protocol | mAP at IoU 0.15, 0.30, and 0.50 on validation and holdout sets |
| Artifacts | code, data, model weights, and configurations reported available at the GitHub repository |

## Limitations

- The paper describes results as preliminary and based on one automotive structural adhesive pilot cell.
- Synthetic images still required manual annotation for the object-detection training set.
- The authors identify controllability over defect type and finer latent-space control as remaining work.
- The approach still needs real data; the synthetic-only detector performed worst across tests.
- The paper suggests that more real data or smaller partially overlapping crops could improve GAN results.
- The holdout set is small, with 19 real images reported in the paper.

## Connections

### Graph Hubs

- Datasets: [[Structural Adhesive Defects Dataset]]
- Tasks: [[Adhesive bead defect detection]], [[Object detection]]
- Domains: [[Automotive manufacturing]]
- Methods: [[GAN]], [[StyleGAN2]], [[GAN-based surface defect augmentation]], [[YOLOv4]], [[Synthetic data generation]], [[Learned generative synthesis]]
- Metrics: [[mAP@0.15]], [[mAP@0.30]], [[mAP@0.50]], [[Average precision]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] | Builds on | The GAN paper explicitly positions its method as a follow-up to the earlier simulation-based adhesive augmentation work, replacing explicit simulation modeling with learned synthesis from real images. |
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Shares method | Both use GAN-based synthetic defect generation to improve downstream defect detection or inspection performance, but this paper targets automotive adhesive beads with StyleGAN2-ADA and YOLOv4-Tiny. |

## Questions

- Is the release's `holdout.zip` count of 18 images a packaging difference from the paper's 19-image holdout description?
- What license or reuse terms apply to the GitHub release assets?
- Would automatic labeling or controllable latent editing reduce the remaining manual annotation burden?
