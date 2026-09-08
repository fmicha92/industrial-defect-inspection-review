---
title: "Structured Domain Randomization: Bridging the Reality Gap by Context-Aware Synthetic Data"
aliases:
  - "Structured Domain Randomization"
  - "SDR"
paper_key: "sha256:b074dfc56bd6f325dd96157fca19476502f3030b0dcaf2881f6c2badbba4d872"
paper_type: research
year: 2019
venue: "ICRA 2019"
authors:
  - "Aayush Prakash"
  - "Eric Cameracci"
  - "Shaad Boochoon"
  - "Gavriel State"
  - "Mark Brophy"
  - "Omer Shapira"
  - "David Acuna"
  - "Stan Birchfield"
status: processed
processed_at: 2026-06-02
topics:
  - structured domain randomization
  - synthetic vehicle detection data
  - domain gap
tasks:
  - "[[Object detection]]"
datasets:
  - "[[SDR synthetic vehicle dataset]]"
  - "[[KITTI]]"
domains:
  - "[[Autonomous driving]]"
methods:
  - "[[Structured domain randomization]]"
  - "[[Domain randomization]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[Faster R-CNN]]"
metrics:
  - "[[AP@0.7 IoU]]"
related_concepts:
  - "[[Domain gap]]"
related_methods:
  - "[[Structured domain randomization]]"
  - "[[Domain randomization]]"
  - "[[Faster R-CNN]]"
doi: "not reported"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2019 - Prakash - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data.pdf"
source_file: "paper-inbox/10_processed/Research/2019 - Prakash - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2019 - Prakash - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data.md"
extracted_text: "paper-inbox/90_processing/text/2019 - Prakash - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data.txt"
artifact_status: "processed"
tags:
  - paper
  - synthetic-data
  - domain-randomization
---

# Structured Domain Randomization: Bridging the Reality Gap by Context-Aware Synthetic Data

## Summary

Prakash et al. introduce [[Structured domain randomization]], a context-aware version of domain randomization for synthetic vehicle detection data. Instead of placing objects uniformly at random, SDR samples scenarios, context splines, and object placements so vehicles, pedestrians, buildings, lanes, sidewalks, and other elements respect scene structure.

## Paper Type

Research paper. It introduces a procedural synthetic-data generation method and evaluates Faster R-CNN vehicle detection on KITTI.

## Problem

Ordinary domain randomization provides variation but can ignore context, which hurts small, occluded, or truncated object detection. The paper addresses this by preserving scene structure while retaining random variation.

## Contribution

- Claimed: structured domain randomization adds context to ordinary domain randomization.
- Shown: SDR-trained Faster R-CNN outperforms VKITTI, Sim 200k, and ordinary DR on KITTI Easy, Moderate, and Hard vehicle detection.
- Shown: SDR is useful as an initialization strategy before fine-tuning on limited KITTI real data.

## Method

SDR samples a scenario, global parameters, context splines, and objects. Context splines represent lanes, medians, sidewalks, gutters, and side stretches. Objects are placed conditionally on context, such as vehicles in lanes and pedestrians on sidewalks. UE4 renders images and exports labels including depth, segmentation masks, 2D bounding boxes, 3D boxes, truncation, and occlusion values.

## Evidence

| Training dataset | Size | Easy AP@0.7 | Moderate AP@0.7 | Hard AP@0.7 |
|---|---:|---:|---:|---:|
| VKITTI clones | 2.2K | 49.6 | 44.8 | 33.6 |
| VKITTI | 21K | 70.3 | 53.6 | 39.9 |
| Sim 200k | 200K | 68.0 | 52.6 | 42.1 |
| DR | 25K | 56.7 | 38.8 | 24.0 |
| SDR | 25K | 77.3 | 65.6 | 52.2 |

| Dataset size | DR Hard AP@0.7 | SDR Hard AP@0.7 |
|---:|---:|---:|
| 1K | 20.6 | 43.7 |
| 2.2K | 22.1 | 46.0 |
| 10K | 23.2 | 51.9 |
| 25K | 24.0 | 52.5 |
| 50K | 25.8 | 51.1 |
| 100K | 25.6 | 51.6 |

## ML/DL Extraction

- Detector: [[Faster R-CNN]] with ResNet V1 feature extractor pretrained on ImageNet.
- Optimizer: momentum 0.9 and learning rate 0.0003.
- Synthetic generator: UE4 scene generator with Substance material randomization.
- Main evaluation: KITTI vehicle detection with AP@0.7 IoU.
- Assets: 74 car models, 13 truck models, 5 bicycle models, 41 building models, 87 house models, 24 tree models, 20 pedestrian models, and 100 road sign models.

## Limitations

- The paper focuses on 2D vehicle detection.
- Ranges for many random variables were selected manually.
- It does not combine learned generative refinement with procedural generation.

## Connections

### Graph Hubs

- Methods: [[Structured domain randomization]], [[Domain randomization]], [[Procedural and simulation-based synthesis]], [[Faster R-CNN]]
- Tasks: [[Object detection]]
- Datasets: [[SDR synthetic vehicle dataset]], [[KITTI]]
- Domains: [[Autonomous driving]]
- Metrics: [[AP@0.7 IoU]]

### Hybrid Fit

Does not fit [[Hybrid generative-procedural synthesis]] as written. It is a procedural/simulation-based method with structured randomization, but no learned generative network is used for synthesis or refinement in the reported method.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] | Contrasts with | Both address synthetic-to-real object detection; this paper improves procedural context, while the 2018 paper combines domain randomization with GAN refinement. |
| [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] | Contrasts with | SimGAN learns realism with adversarial refinement, while SDR improves simulation structure and context directly. |

## Questions

- Would SDR plus learned image refinement improve over SDR alone without weakening contextual label consistency?
