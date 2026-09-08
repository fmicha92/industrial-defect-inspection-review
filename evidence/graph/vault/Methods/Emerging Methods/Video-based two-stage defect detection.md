---
title: "Video-based two-stage defect detection"
aliases:
  - "coarse-to-fine video defect detection"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]]"
evidence_count: 1
---
# Video-Based Two-Stage Defect Detection

## Definition

Video-based two-stage defect detection uses a coarse stage to locate the inspected object, a fine stage to detect defects in a higher-resolution crop, and multi-frame fusion to combine detections from different video perspectives.

## Why It Matters

The method addresses tiny defects that may disappear under full-image downsampling and may only be visible in some views of an inspected object.

## Used In These Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] applies the method to [[OGD-DET]] and reports improved AP, recall, and precision over one-stage detection and common baselines.

## Related Concepts

- [[Optical glass defect detection]]
- [[YOLOv4]]
- [[Color Channel Separation convolution]]
- [[Clustering-based image quality evaluation]]
- [[OGD-DET benchmark]]
