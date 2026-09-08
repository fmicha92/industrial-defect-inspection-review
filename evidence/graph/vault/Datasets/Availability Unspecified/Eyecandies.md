---
title: "Eyecandies"
aliases:
  - "EyeCandies"
related_domain: "[[Multi-industry anomaly detection]]"
availability: "not reported"
access: "not reported"
licenses:
  - "not reported"
modalities:
  - "RGB"
  - "depth"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_papers:
  - "[[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]]"
---
# Eyecandies

## Definition

Eyecandies is a rendered RGB+3D anomaly detection benchmark used by [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] to evaluate image-level anomaly detection in 3D-only and RGB+3D settings.

## Why It Matters

It provides a second RGB+3D benchmark beyond [[MVTec3D]] for testing whether 3D anomaly detection methods generalize to rendered objects and subtle depth or appearance anomalies.

## Dataset Details

- Object classes: 10.
- Training examples: 10000 anomaly-free examples.
- Test examples: 500.
- Anomalous test examples: 250.
- Modalities: RGB and 3D/depth.
- Availability: not reported in the checked paper.
- License: not reported in the checked paper.

## Used In These Papers

- [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] reports 3DSR image-level AUROC of 77.6 in 3D-only and 90.9 in RGB+3D on Eyecandies.

## Source Anchors

- Related source: [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]].

## Related Concepts

- [[MVTec3D]]
- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Defect segmentation]]
