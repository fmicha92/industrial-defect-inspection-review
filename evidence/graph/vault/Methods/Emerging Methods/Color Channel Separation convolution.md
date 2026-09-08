---
title: "Color Channel Separation convolution"
aliases:
  - "CCS convolution"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]]"
evidence_count: 1
---
# Color Channel Separation Convolution

## Definition

Color Channel Separation convolution is a fine-stage backbone modification that processes RGB channels separately with CBL and repeated MCBL operations before later detection layers.

## Why It Matters

The paper uses CCS convolution to extract more detailed color-channel information for tiny optical-glass defects that can occupy only a few image pixels.

## Used In These Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] reports that adding CCS improves AP@0.25 from 0.8820 to 0.9050 and precision from 0.8010 to 0.9050 in its ablation table.

## Related Concepts

- [[Video-based two-stage defect detection]]
- [[Optical glass defect detection]]
- [[Deep convolutional neural network]]
