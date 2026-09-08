---
title: "Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images"
paper_key: "arxiv:1805.11778"
paper_type: research
year: 2018
venue: "arXiv preprint"
authors:
  - "Fernando Camaro Nogues"
  - "Andrew Huie"
  - "Sakyasingha Dasgupta"
status: processed
processed_at: 2026-06-02
topics:
  - object detection
  - domain randomization
  - adversarial refinement
tasks:
  - "[[Object detection]]"
datasets:
  - "[[Industrial electric parts synthetic dataset]]"
domains:
  - "[[Semiconductor and electronics]]"
methods:
  - "[[Domain randomization]]"
  - "[[CycleGAN]]"
  - "[[Hybrid generative-procedural synthesis]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[mAP]]"
related_concepts:
  - "[[Domain gap]]"
  - "[[Hybrid generative-procedural synthesis]]"
related_methods:
  - "[[CycleGAN]]"
  - "[[Domain randomization]]"
  - "Mask R-CNN"
doi: "not reported"
arxiv: "1805.11778"
url: "https://arxiv.org/abs/1805.11778"
pdf: "paper-inbox/10_processed/Research/2018 - Camaro Nogues - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images.pdf"
source_file: "paper-inbox/10_processed/Research/2018 - Camaro Nogues - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2018 - Camaro Nogues - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images.md"
extracted_text: "paper-inbox/90_processing/text/2018 - Camaro Nogues - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images.txt"
artifact_status: "processed"
tags:
  - paper
  - synthetic-data
  - object-detection
---

# Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images

## Summary

Camaro Nogues et al. train a near real-time industrial object detector with synthetic data produced by physics simulation, ray-traced rendering, domain randomization, and Cyclic-GAN refinement. The best reported training mixture combines GAN-refined fixed synthetic images with highly randomized rendered images.

## Paper Type

Research paper. It evaluates synthetic data generation and refinement strategies for object detection in an industrial electric-parts setting.

## Problem

Industrial labeled real data can be scarce, while purely synthetic data may not match real images. The paper tests whether domain randomization and adversarial image refinement reduce the real/synthetic gap for detecting electric parts.

## Contribution

- Claimed: combines domain randomization and GAN-based synthetic image refinement for industrial object detection.
- Shown: a mixture of refined synthetic images and highly randomized synthetic images gives the best reported Mask R-CNN mAP.
- Shown: neither domain randomization nor GAN refinement alone gives the same reported performance as the combined setting.

## Method

Synthetic images are generated with Bullet physics to place objects in physically consistent configurations and POV-Ray rendering to produce images. Domain randomization varies light count/color, object and floor colors/textures, and camera position. A Cyclic-GAN model is trained with 10K synthetic images and 256 real images to translate synthetic crops toward the real domain.

## Evidence

| Training data | [[mAP]] at 0.5 IoU |
|---|---:|
| 100% fixed-color synthetic | 0.812 |
| 100% fixed-color synthetic translated to real | 0.874 |
| 100% randomized synthetic without texture | 0.867 |
| 100% randomized synthetic with texture | 0.911 |
| 20% fixed-color synthetic and 80% randomized textured synthetic | 0.914 |
| 20% fixed-color translated-to-real and 80% randomized textured synthetic | 0.955 |
| 50% fixed-color translated-to-real and 50% randomized textured synthetic | 0.950 |

## ML/DL Extraction

- Detector: Mask R-CNN.
- Synthetic data: 10K training samples per experiment.
- Real data: 100 real test images; 256 real images for Cyclic-GAN training.
- Target objects: 12 tiny electronic parts with accurate 3D CAD models.
- Refinement model: Cyclic-GAN trained on 256 x 256 crops, then applied fully convolutionally to full-size images.
- Artifact link: the paper reports a real-time object detection video at `https://youtu.be/Q-WeXSSnZ0U`.

## Limitations

- The evaluation uses one industrial electric-parts setup.
- The paper reports that one object lost its color after GAN refinement until discriminator receptive-field changes were made.
- Dataset availability is not reported in the extracted source.

## Connections

### Graph Hubs

- Methods: [[Domain randomization]], [[CycleGAN]], [[Hybrid generative-procedural synthesis]], [[Synthetic data generation]]
- Tasks: [[Object detection]]
- Datasets: [[Industrial electric parts synthetic dataset]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[mAP]]

### Hybrid Fit

Fits [[Hybrid generative-procedural synthesis]]. It combines physics simulation, ray-traced procedural rendering, and domain randomization with learned Cyclic-GAN image refinement.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] | Builds on method | Uses a Cyclic-GAN architecture for unpaired synthetic-to-real translation. |
| [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] | Shares method | Both use unlabeled real images to adversarially refine simulator output while keeping synthetic labels usable. |
| [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] | Contrasts with | This paper combines GAN refinement with domain randomization, while SDR improves the procedural randomization structure without learned refinement. |

## Questions

- How much of the gain comes from adversarial realism versus the mixed training distribution?
