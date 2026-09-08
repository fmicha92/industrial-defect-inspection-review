---
title: "BBMP"
aliases:
  - "Glass bottle bottom mold point dataset"
  - "Bottle bottom mold point dataset"
related_domain: "[[Glass inspection]]"
url: "not reported"
data_sources:
  - "industrial production-line collection"
introduced_by: "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
related_papers:
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
---
# BBMP

## Definition

BBMP is a glass-bottle bottom mold point recognition dataset collected in an actual industrial production scenario and used by [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] to test IDD-Net outside public benchmark datasets.

## Why It Matters

It evaluates whether a detector trained for industrial defects can reach production-speed constraints on highly similar glass-bottle mold-point categories.

## Dataset Details

- Availability: data will be made available on request.
- Capture setup: glass bottles are transported above a CCD camera by a conveyor belt while annular light and camera triggering are controlled by a photoelectric gate.
- Image resolution: 800 x 780.
- Collection rate: 125 pictures per hour for eight hours.
- Split: training, testing, and validation in a 6:2:2 ratio.
- Labels: bottom mold point categories are shown in a figure; exact category names and counts are not recoverable from the analysis input.
- License: not reported.

## Used In These Papers

- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates IDD-Net on BBMP, reporting 99.5% [[mAP@0.50]], 40 [[FPS]], 99.6% [[Precision]], and 99.5% [[Recall]].

## Source Anchors

- Hosting source: not reported.
- Introducing paper: [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]].

## Related Concepts

- [[Glass inspection]]
- [[Glass container defect detection]]
- [[Object detection]]
- [[FPS]]
