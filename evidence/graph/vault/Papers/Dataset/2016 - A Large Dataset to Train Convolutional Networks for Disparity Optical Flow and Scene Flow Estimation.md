---
title: "A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation"
aliases:
  - "Scene Flow synthetic dataset paper"
  - "FlyingThings3D dataset paper"
paper_key: "arxiv:1002.18000"
paper_type: dataset
year: 2016
venue: "CVPR 2016"
authors:
  - "Nikolaus Mayer"
  - "Eddy Ilg"
  - "Philip Hausser"
  - "Philipp Fischer"
  - "Daniel Cremers"
  - "Alexey Dosovitskiy"
  - "Thomas Brox"
status: processed
processed_at: 2026-06-02
topics:
  - synthetic stereo data
  - scene flow
  - optical flow
  - disparity estimation
tasks:
  - "[[Scene flow estimation]]"
  - "[[Optical flow estimation]]"
  - "[[Disparity estimation]]"
datasets:
  - "[[FlyingThings3D]]"
  - "[[Monkaa]]"
  - "[[Driving synthetic scene flow dataset]]"
domains:
  - "[[General computer vision]]"
methods:
  - "[[Synthetic data generation]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[DispNet]]"
  - "[[SceneFlowNet]]"
metrics:
  - "[[Endpoint error]]"
  - "[[D1-all]]"
related_methods:
  - "[[Synthetic data generation]]"
  - "[[Procedural and simulation-based synthesis]]"
doi: "not reported"
arxiv: "1002.18000"
url: "http://lmb.informatik.uni-freiburg.de/resources/datasets/"
pdf: "paper-inbox/10_processed/Dataset/2016 - Mayer - A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.pdf"
source_file: "paper-inbox/10_processed/Dataset/2016 - Mayer - A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2016 - Mayer - A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.md"
extracted_text: "paper-inbox/90_processing/text/2016 - Mayer - A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.txt"
artifact_status: "processed"
tags:
  - paper
  - dataset
  - synthetic-data
---

# A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation

## Summary

Mayer et al. introduce a synthetic stereo video dataset suite for training convolutional networks on [[Disparity estimation]], [[Optical flow estimation]], and [[Scene flow estimation]]. The suite contains [[FlyingThings3D]], [[Monkaa]], and a KITTI-like [[Driving synthetic scene flow dataset]], all rendered with customized Blender passes that provide dense ground truth not available at comparable scale in real scenes.

## Paper Type

Dataset paper. It contributes synthetic scene-flow datasets and evaluates convolutional baselines trained on them.

## Problem

Dense scene flow, optical flow, and disparity estimation require ground truth for every pixel, but real-world capture cannot easily provide dense labels for arbitrary 3D motion and occlusion. The paper addresses this by rendering synthetic stereo videos with automatically available labels.

## Contribution

- Introduces more than 35,000 stereo frames with dense ground truth for optical flow, disparity, disparity change, 3D position, camera parameters, object/material segmentation, and motion boundaries.
- Defines three complementary subsets: randomized object motion in FlyingThings3D, animated movie scenes in Monkaa, and a KITTI-like driving scene.
- Shows that networks trained on the synthetic data transfer to KITTI disparity benchmarks and that a joint scene-flow network can predict flow, disparity, and disparity change.

## Method

The authors use a customized Blender render pipeline. The render passes produce clean and final RGB images, disparity/depth, optical flow, disparity change, motion boundaries, object segmentation, material segmentation, 3D positions, and camera calibration. FlyingThings3D samples ShapeNet objects, randomized object trajectories, procedural or scraped textures, motion blur, and defocus blur. Monkaa uses an animated open-movie scene with nonrigid motion and fur. Driving recreates a street scene with a stereo baseline and camera geometry intended to resemble KITTI.

## Evidence

| Dataset | Frames / scenes reported | Resolution | Main labels |
|---|---:|---:|---|
| [[FlyingThings3D]] | 21,818 training frames, 4,248 test frames, 2,247 training scenes | 960x540 | flow, disparity/depth, disparity change, segmentation, motion boundaries |
| [[Monkaa]] | 8,591 frames, 8 scenes | 960x540 | flow, disparity/depth, disparity change, segmentation, motion boundaries |
| [[Driving synthetic scene flow dataset]] | 4,392 frames, 1 scene | 960x540 | KITTI-like flow, disparity, disparity change, segmentation, motion boundaries |

The paper reports that DispNetCorr1D fine-tuned on KITTI 2015 reaches 4.34% D1-all on the KITTI 2015 test set while running in 0.06 seconds per image pair on a Titan X. SceneFlowNet trained on FlyingThings3D reaches endpoint errors of 10.99 for flow, 2.21 for disparity, and 0.80 for disparity change on FlyingThings3D.

## ML/DL Extraction

- Models: [[DispNet]], DispNetCorr1D, FlowNet, and [[SceneFlowNet]].
- Training framework: custom Caffe.
- Optimizer: Adam with beta1 0.9, beta2 0.999, learning rate 0.0001, halved every 200,000 iterations from 400,000.
- Augmentation: spatial transforms, cropping, scaling, rotation, translation, and chromatic transformations.
- Evaluation metrics: [[Endpoint error]] for flow/disparity/change and KITTI D1-all disparity error.
- Runtime reported: DispNet variants 0.06 seconds per image pair on Nvidia GTX Titan X.

## Limitations

- The datasets are synthetic, so transfer depends on whether rendered variation covers relevant real-world appearance.
- The paper reports that FlyingThings3D did not improve FlowNet over FlyingChairs for optical flow in the tested setup.
- The evaluation demonstrates transfer, but not complete real-world scene-flow supervision.

## Connections

### Graph Hubs

- Tasks: [[Scene flow estimation]], [[Optical flow estimation]], [[Disparity estimation]]
- Datasets: [[FlyingThings3D]], [[Monkaa]], [[Driving synthetic scene flow dataset]]
- Methods: [[Synthetic data generation]], [[Procedural and simulation-based synthesis]], [[DispNet]], [[SceneFlowNet]]
- Domains: [[General computer vision]]
- Metrics: [[Endpoint error]], [[D1-all]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2017 - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World]] | Shares method family | Both use synthetic simulation to train models intended to transfer to real data, but this paper emphasizes dense visual motion labels rather than robotic control. |
| [[2018 - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization]] | Shares method family | Both use synthetic data for computer vision transfer; Tremblay et al. randomize scenes for object detection, while this paper renders dense stereo-video labels. |

## Questions

- Which subsets transfer best to current stereo and optical-flow architectures without fine-tuning on real data?
