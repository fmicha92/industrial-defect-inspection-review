---
title: "Training Deep Networks with Synthetic Data: Bridging the Reality Gap by Domain Randomization"
aliases:
  - "Training Deep Networks with Synthetic Data"
paper_key: "sha256:ca6ab579854a235332f5691b8271953d9a13f88ba596d5a387c91da3332ac2cf"
paper_type: research
year: 2018
venue: "CVPR 2018"
authors:
  - "Jonathan Tremblay"
  - "Aayush Prakash"
  - "David Acuna"
  - "Mark Brophy"
  - "Varun Jampani"
  - "Cem Anil"
  - "Thang To"
  - "Eric Cameracci"
  - "Shaad Boochoon"
  - "Stan Birchfield"
status: processed
processed_at: 2026-06-02
topics:
  - domain randomization
  - synthetic car detection data
  - autonomous driving
tasks:
  - "[[Object detection]]"
datasets:
  - "[[Domain-randomized KITTI car detection synthetic dataset]]"
  - "[[KITTI]]"
domains:
  - "[[Autonomous driving]]"
methods:
  - "[[Domain randomization]]"
  - "[[Synthetic data generation]]"
  - "[[Faster R-CNN]]"
  - "[[Single Shot MultiBox Detector]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[Average precision]]"
related_methods:
  - "[[Domain randomization]]"
doi: "not reported"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2018 - Tremblay - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization.pdf"
source_file: "paper-inbox/10_processed/Research/2018 - Tremblay - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2018 - Tremblay - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization.md"
extracted_text: "paper-inbox/90_processing/text/2018 - Tremblay - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization.txt"
artifact_status: "processed"
tags:
  - paper
  - synthetic-data
  - domain-randomization
---

# Training Deep Networks with Synthetic Data: Bridging the Reality Gap by Domain Randomization

## Summary

Tremblay et al. apply [[Domain randomization]] to real-world car detection on [[KITTI]]. The paper generates non-photorealistic synthetic images with randomized cars, textures, lights, camera poses, backgrounds, and flying distractors, then trains object detectors that transfer to real KITTI images.

## Paper Type

Research paper. It evaluates a synthetic-data generation strategy for object detection and transfer from simulation to real driving imagery.

## Problem

Accurate object detection needs labeled real images, but labeled driving data is expensive. Synthetic data can be labeled automatically, but photorealism alone may not close the synthetic-to-real gap.

## Contribution

- Extends domain randomization from robotic localization to car detection in street-scene images.
- Shows that random textures, randomized lighting, augmentations, and distractors matter for synthetic-to-real transfer.
- Reports that domain-randomized pretraining plus real fine-tuning outperforms real-only training in the reported KITTI setup.

## Method

The renderer places a random number of cars and distractors, applies random textures from Flickr images or simple procedural choices, randomizes camera azimuth/elevation/pan/tilt/roll, samples one to twelve point lights plus ambient illumination, and may hide or show the ground plane. It outputs 1200x400 images and 2D bounding boxes through an Unreal Engine 4 plugin.

## Evidence

The paper trains on 100,000 domain-randomized images with up to 14 cars per image, 36 car models, and about 8,000 texture images. It evaluates on 500 random KITTI images with AP at 0.5 IoU for objects taller than 40 pixels and truncation below 0.15.

| Detector | Virtual KITTI AP@0.5 | Domain-randomized AP@0.5 |
|---|---:|---:|
| Faster R-CNN | 79.7 | 78.1 |
| R-FCN | 64.6 | 71.5 |
| SSD | 36.1 | 46.3 |

Fine-tuning with all 6,000 real images gives DR+real AP of 98.5, reported as 1.6 points above Virtual KITTI plus real and 2.1 points above real-only. An ablation with Faster R-CNN ResNet V1 reports 73.7 AP for full randomization, 67.6 AP with fixed lighting, 69.0 AP without texture randomization, and a 1.1 point drop without distractors.

## ML/DL Extraction

- Detectors: [[Faster R-CNN]], R-FCN, and [[Single Shot MultiBox Detector]].
- Feature extractors: Inception-ResNet V2 for Faster R-CNN/R-FCN and ResNet101 for SSD.
- Pretraining: ImageNet pretraining for detector backbones; COCO pretraining is also tested.
- Augmentation: brightness, contrast, Gaussian noise, flips, resizing, box jitter, and crop.
- Hardware: NVIDIA DGX Station.
- Metric: [[mAP@0.50]] / [[Average precision]] at 0.5 IoU.

## Limitations

- The generator needs 3D object assets; the authors call for more object models and better scene structure.
- Context mismatch remains important at high recall, especially because randomized scenes do not fully model parked cars and other structured street context.
- The paper focuses on car detection rather than full-scene autonomous-driving perception.

## Connections

### Graph Hubs

- Tasks: [[Object detection]]
- Datasets: [[Domain-randomized KITTI car detection synthetic dataset]], [[KITTI]]
- Domains: [[Autonomous driving]]
- Methods: [[Domain randomization]], [[Synthetic data generation]], [[Faster R-CNN]], [[Single Shot MultiBox Detector]]
- Metrics: [[mAP@0.50]], [[Average precision]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2017 - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World]] | Builds on | Both test domain randomization for sim-to-real transfer; this paper scales the idea to car detection in driving imagery. |
| [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] | Follow-up reading | Structured domain randomization later adds context-aware road-scene layout to improve KITTI vehicle detection. |
| [[2016 - The SYNTHIA Dataset A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes]] | Shares domain | Both use synthetic urban-driving imagery, but SYNTHIA targets semantic segmentation rather than car detection. |

## Questions

- Would context-aware scene generation recover the high-recall cases where ordinary domain randomization struggles?
