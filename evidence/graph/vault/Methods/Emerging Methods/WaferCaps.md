---
title: "WaferCaps"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Neural Networks"
source_papers:
  - "[[2022 - WaferCaps for Wafer Bin Map Classification Based on DCGAN Data Upsampling]]"
evidence_count: 1
tags:
  - emerging-method
---
# WaferCaps

## Definition

WaferCaps is a capsule-network classifier adapted for 64 x 64 wafer bin maps with additional convolutional layers, dropout, and larger convolution kernels.

## Why It Matters

It is designed to preserve spatial relationships in wafer-map defect patterns while benefiting from DCGAN-based data upsampling.

## Used In These Papers

- [[2022 - WaferCaps for Wafer Bin Map Classification Based on DCGAN Data Upsampling]] introduces WaferCaps and reports test accuracy improvement from 78.2% on original data to 91.41% with original plus DCGAN-generated wafer maps.

## Related Concepts

- [[DCGAN wafer map augmentation]]
- [[Wafer map defect classification]]
- [[Class imbalance]]
- [[Data augmentation]]
