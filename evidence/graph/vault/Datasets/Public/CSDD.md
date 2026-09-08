---
title: "CSDD"
aliases:
  - "Casting Surface Defect Dataset"
  - "CSDD benchmark dataset"
related_domain: "[[Metal inspection]]"
url: "https://github.com/Kerio99/CSDD"
data_sources: "GitHub"
introduced_by: "[[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]"
---
# CSDD

## Definition

CSDD is a public casting surface defect dataset introduced by [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]. The paper reports 2100 high-resolution RGB images, 56,356 annotated defects, three defect classes, and both detection and segmentation annotations.

## Why It Matters

CSDD is designed to make [[Casting surface defect detection]] more realistic than simpler surface-defect datasets by using casting-like metal surface structures, high-resolution images, small defects, and complex backgrounds.

## Used In These Papers

- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] introduces CSDD and evaluates detection and segmentation baselines on it.

## Dataset Details

- Object/domain: casting-like metal surfaces.
- Images: 2100 RGB images.
- Resolution: 3648 x 3648.
- Defects: 56,356 total.
- Classes: scratches, spots, rusts.
- Annotations: bounding-box-style detection labels and pixel-level segmentation regions.
- Splits: 1343 training, 335 validation, 422 testing.
- Artifact: https://github.com/Kerio99/CSDD.
- License: not reported in the processed paper text.

## Source Anchors

- Hosting source: https://github.com/Kerio99/CSDD.
- Introducing paper: [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]].

## Related Concepts

- [[CSDD benchmark]]
- [[Casting surface defect detection]]
- [[Defect segmentation]]
- [[Metal inspection]]
- [[Surface defect detection]]
- [[GC10-DET]]
- [[NEU-DET]]
