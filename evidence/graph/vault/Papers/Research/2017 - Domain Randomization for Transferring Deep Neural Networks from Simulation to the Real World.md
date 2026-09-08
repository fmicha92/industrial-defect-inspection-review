---
title: "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World"
aliases:
  - "Domain Randomization for Sim-to-Real Transfer"
paper_key: "sha256:a4fdac3d13d95201c141f138e812f197984cf2b96ac86ea1a08c2df753e4d6ce"
paper_type: research
year: 2017
venue: "IROS 2017"
authors:
  - "Josh Tobin"
  - "Rachel Fong"
  - "Alex Ray"
  - "Jonas Schneider"
  - "Wojciech Zaremba"
  - "Pieter Abbeel"
status: processed
processed_at: 2026-06-02
topics:
  - domain randomization
  - sim-to-real transfer
  - robotic object localization
tasks:
  - "[[Robotic object localization]]"
datasets:
  - "[[Tobin geometric object localization dataset]]"
domains:
  - "[[Robotic manipulation]]"
methods:
  - "[[Domain randomization]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[Mean localization error]]"
  - "[[Grasp success rate]]"
related_methods:
  - "[[Domain randomization]]"
doi: "not reported"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2017 - Tobin - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World.pdf"
source_file: "paper-inbox/10_processed/Research/2017 - Tobin - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2017 - Tobin - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World.md"
extracted_text: "paper-inbox/90_processing/text/2017 - Tobin - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World.txt"
artifact_status: "processed"
tags:
  - paper
  - domain-randomization
  - sim-to-real
---

# Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

## Summary

Tobin et al. evaluate [[Domain randomization]] as a way to transfer a deep visual object-localization model from low-fidelity simulation to a real robot setup. The paper trains on randomized simulated RGB images and tests on real tabletop objects without real-image pretraining or fine-tuning.

## Paper Type

Research paper. It introduces and evaluates a sim-to-real training strategy for robotic perception and control.

## Problem

Simulation can cheaply generate labeled images, but models trained on ordinary simulation often fail on real cameras. The paper tests whether a wide distribution of randomized synthetic scenes can make real-world images look like another variation of the simulator.

## Contribution

- Shows sim-to-real transfer for robotic object localization from synthetic RGB images alone.
- Identifies texture randomization and distractor objects as important contributors to robust transfer.
- Demonstrates robotic grasping with a Fetch robot using the transferred detector.

## Method

The simulator renders tabletop scenes in MuJoCo with randomized object positions, textures, camera pose, field of view, lighting, distractors, and image noise. The model is a modified VGG-16-style convolutional network that maps a 224x224 RGB image to x, y, z object coordinates using an L2 position loss.

## Evidence

The real test set contains 480 webcam images: 60 per object across eight geometric objects, with object-only, distractor, and partial-occlusion cases. Average real-world localization is about centimeter scale; the paper reports many object/category errors around 0.7 cm to 2.6 cm, with some larger failures under occlusion.

The ablation table shows that removing distractors substantially degrades performance, especially in real distractor and occlusion cases. Texture-randomization experiments report that fewer than 1,000 textures significantly hurts transfer. The robot pickup experiments report 38 of 40 successful pickups for two consistently accurate detectors, and 9 of 10 successful pickups for an unseen spam-can setting with food-item distractors.

## ML/DL Extraction

- Input/output: single uncalibrated 224x224 RGB image to Cartesian object center.
- Architecture: modified VGG-16 convolutional stack with smaller fully connected layers of 256 and 64 units.
- Initialization: ImageNet-pretrained convolutional layers usually used; random initialization can approach similar performance with enough simulated data.
- Optimizer/objective: SGD or Adam with L2 loss; learning rate approximately 0.0001.
- Evaluation metrics: [[Mean localization error]] in centimeters and [[Grasp success rate]].

## Limitations

- The setup uses known 3D object models and object-specific detectors.
- Some neural-network failures are large and hard to interpret.
- The paper notes uncertainty about generalization to new scenes, camera/table settings, and broader robotic tasks.

## Connections

### Graph Hubs

- Tasks: [[Robotic object localization]]
- Datasets: [[Tobin geometric object localization dataset]]
- Domains: [[Robotic manipulation]]
- Methods: [[Domain randomization]], [[Procedural and simulation-based synthesis]], [[Deep convolutional neural network]]
- Metrics: [[Mean localization error]], [[Grasp success rate]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2018 - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization]] | Builds on | Tremblay et al. extend domain randomization from robotic object localization to real-world car detection. |
| [[2016 - A Large Dataset to Train Convolutional Networks for Disparity Optical Flow and Scene Flow Estimation]] | Shares method family | Both use simulation-generated labeled data for transfer, but this paper randomizes simple scenes for robotic localization. |

## Questions

- How much of the transfer comes from diversity alone versus the particular camera, object, and task constraints?
