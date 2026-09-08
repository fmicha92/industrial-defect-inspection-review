---
title: "RepVGG+SA"
aliases:
  - "RepVGG_B3g4+SA"
  - "RepVGG with spatial attention"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]]"
evidence_count: 1
tags:
  - method
---
# RepVGG+SA

## Definition

RepVGG+SA is the RepVGG_B3g4 classifier augmented with a spatial attention module in the X-SDD paper. The spatial attention module pools feature maps across channels with average and max pooling, concatenates those maps, applies a 7 x 7 convolution, and uses a sigmoid map to reweight spatial features.

## Why It Matters

The method is a high-accuracy but computationally heavy CNN baseline for hot-rolled steel strip surface defect classification on [[X-SDD]].

## Used In These Papers

- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] reports RepVGG+SA at 95.10% accuracy, 93.92% macro-recall, 95.16% macro-precision, and 93.25% macro-F1 on X-SDD.

## Related Concepts

- [[Computer Vision Models]]
- [[Defect classification]]
- [[Metallic surface defect detection]]
- [[X-SDD]]
- [[Accuracy]]
