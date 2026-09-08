---
title: "Domain-randomized KITTI car detection synthetic dataset"
aliases:
  - "Tremblay DR car detection dataset"
related_domain: "[[Autonomous driving]]"
introduced_by: "[[2018 - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization]]"
tags:
  - dataset
---

# Domain-Randomized KITTI Car Detection Synthetic Dataset

## Definition

This synthetic dataset consists of domain-randomized car-detection images generated for KITTI transfer experiments.

## Dataset Details

- Availability: not reported.
- Size reported: 100,000 rendered images.
- Image size: 1200x400.
- Assets: 36 generic sedan and hatchback car models.
- Labels: 2D bounding boxes for car detection.
- Randomization: car count and placement, textures, backgrounds, camera pose, lighting, ground plane visibility, and flying distractors.

## Related Papers

- [[2018 - Training Deep Networks with Synthetic Data Bridging the Reality Gap by Domain Randomization]] trains Faster R-CNN, R-FCN, and SSD detectors on this synthetic dataset for KITTI car detection.
