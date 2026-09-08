---
title: "FlyingThings3D"
aliases:
  - "Flying Things 3D"
related_domain: "[[General computer vision]]"
url: "http://lmb.informatik.uni-freiburg.de/resources/datasets/"
introduced_by: "[[2016 - A Large Dataset to Train Convolutional Networks for Disparity Optical Flow and Scene Flow Estimation]]"
tags:
  - dataset
---

# FlyingThings3D

## Definition

FlyingThings3D is a synthetic stereo-video dataset for dense optical flow, disparity, disparity change, segmentation, and scene-flow training.

## Dataset Details

- Availability: freely available online according to the introducing paper.
- Size reported: 21,818 training frames, 4,248 test frames, and 2,247 training scenes at 960x540.
- Source assets: ShapeNet 3D models with train/test categories held disjoint.
- Labels: optical flow, disparity/depth, disparity change, object/material segmentation, 3D positions, camera parameters, and motion boundaries.

## Related Papers

- [[2016 - A Large Dataset to Train Convolutional Networks for Disparity Optical Flow and Scene Flow Estimation]] introduces FlyingThings3D and evaluates DispNet and SceneFlowNet variants trained on it.
