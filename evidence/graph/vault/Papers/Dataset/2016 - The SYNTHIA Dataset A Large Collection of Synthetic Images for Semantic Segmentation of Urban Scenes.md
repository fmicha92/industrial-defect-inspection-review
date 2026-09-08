---
title: "The SYNTHIA Dataset: A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes"
aliases:
  - "The SYNTHIA Dataset"
  - "SYNTHIA dataset paper"
paper_key: "arxiv:4748.68000"
paper_type: dataset
year: 2016
venue: "CVPR 2016"
authors:
  - "German Ros"
  - "Laura Sellart"
  - "Joanna Materzynska"
  - "David Vazquez"
  - "Antonio M. Lopez"
status: processed
processed_at: 2026-06-02
topics:
  - synthetic urban scenes
  - semantic segmentation
  - autonomous driving
tasks:
  - "[[Urban semantic segmentation]]"
datasets:
  - "[[SYNTHIA]]"
  - "[[KITTI]]"
  - "[[CamVid]]"
  - "[[Urban LabelMe]]"
  - "[[CBCL StreetScenes]]"
domains:
  - "[[Autonomous driving]]"
methods:
  - "[[Synthetic data generation]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[Per-class accuracy]]"
  - "[[Global accuracy]]"
related_methods:
  - "[[Synthetic data generation]]"
doi: "not reported"
arxiv: "not reported"
url: "http://adas.cvc.uab.es/synthia"
pdf: "paper-inbox/10_processed/Dataset/2016 - Ros - The SYNTHIA Dataset A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes.pdf"
source_file: "paper-inbox/10_processed/Dataset/2016 - Ros - The SYNTHIA Dataset A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2016 - Ros - The SYNTHIA Dataset A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes.md"
extracted_text: "paper-inbox/90_processing/text/2016 - Ros - The SYNTHIA Dataset A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes.txt"
artifact_status: "processed"
tags:
  - paper
  - dataset
  - synthetic-data
---

# The SYNTHIA Dataset: A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes

## Summary

Ros et al. introduce [[SYNTHIA]], a large synthetic dataset for [[Urban semantic segmentation]] in driving scenes. The dataset is generated in a Unity virtual city and provides pixel-level semantic labels, depth maps, multiple viewpoints, seasonal variation, illumination variation, and dynamic urban objects.

## Paper Type

Dataset paper. It contributes a synthetic urban-scene dataset and evaluates whether it improves semantic segmentation on real datasets.

## Problem

Semantic segmentation for autonomous driving needs dense labels for roads, pedestrians, cars, buildings, and related scene elements. Dense manual annotation is expensive, and rare conditions are hard to collect systematically.

## Contribution

- Provides a virtual-city dataset with 13 semantic classes, depth, multiple viewpoints, seasons, weather/illumination variation, and dynamic objects.
- Defines SYNTHIA-Rand with 13,400 randomized frames and SYNTHIA-Seqs with four approximately 50,000-frame seasonal sequences.
- Shows that adding SYNTHIA-Rand to small real training sets improves average per-class accuracy across CamVid, KITTI, Urban LabelMe, and CBCL StreetScenes experiments.

## Method

The authors render urban scenes in Unity with city blocks, highways, rural areas, shops, parks, roads, sidewalks, lane markings, traffic signs, poles, people, cars, vans, pedestrians, and cyclists. The model outputs labels for 13 classes: sky, building, road, sidewalk, fence, vegetation, lane-marking, pole, car, traffic signs, pedestrians, cyclists, and miscellaneous. The training setup mixes synthetic and real examples through balanced gradient contribution, with an experiment batch composition of six real and four synthetic images.

## Evidence

SYNTHIA-Rand contains 13,400 frames at 960x720. SYNTHIA-Seqs contains four seasonal video sequences of approximately 50,000 frames each. Each sequence uses a virtual car with two multi-camera rigs separated by a 0.8 m baseline; each multi-camera rig has four 100-degree-FOV monocular cameras and a virtual depth sensor with range 1.5 m to 50 m.

For T-Net, adding SYNTHIA-Rand improves average per-class accuracy by 10.2 points on CamVid, 7.4 points on KITTI, 10.3 points on Urban LabelMe, and 10.5 points on CBCL StreetScenes in the reported low-resolution setup.

## ML/DL Extraction

- Models: T-Net and FCN.
- Training objective: weighted cross-entropy with weights inverse to class frequency.
- Initialization: VGG-F for T-Net and VGG-16 for FCN, pretrained on ILSVRC.
- Optimizer: Adam.
- Preprocessing: local contrast normalization per channel.
- Evaluation metrics: [[Per-class accuracy]] and [[Global accuracy]].
- Real datasets: [[CamVid]], [[KITTI]], [[Urban LabelMe]], and [[CBCL StreetScenes]].

## Limitations

- Synthetic-to-real domain shift remains; SYNTHIA is most useful in the reported experiments when mixed with real data.
- Some small or texture-sensitive classes are difficult at low resolution.
- The paper evaluates semantic segmentation rather than all possible uses of the depth and multi-view annotations.

## Connections

### Graph Hubs

- Tasks: [[Urban semantic segmentation]]
- Datasets: [[SYNTHIA]]
- Domains: [[Autonomous driving]]
- Methods: [[Synthetic data generation]], [[Procedural and simulation-based synthesis]], [[Deep convolutional neural network]]
- Metrics: [[Per-class accuracy]], [[Global accuracy]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2016 - A Large Dataset to Train Convolutional Networks for Disparity Optical Flow and Scene Flow Estimation]] | Shares method family | Both generate synthetic visual data with dense labels, but SYNTHIA targets urban semantic segmentation while Mayer et al. target stereo motion and geometry. |
| [[2018 - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization]] | Shares domain | Both evaluate synthetic data for autonomous-driving perception, but Tremblay et al. target car detection with domain randomization. |

## Questions

- How much of the reported gain comes from scene diversity versus label density versus balanced synthetic/real batch construction?
