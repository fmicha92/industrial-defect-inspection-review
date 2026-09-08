---
title: "Adaptive Receptive Field Attention Module"
aliases:
  - "ARFAM"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]]"
evidence_count: 1
tags:
  - method
  - emerging
---

# Adaptive Receptive Field Attention Module

## Definition

Adaptive Receptive Field Attention Module is an attention block with channel attention and spatial selection attention. It adapts the receptive field used for defect features so a detector can capture the contextual region most relevant to each defect.

## Why It Matters

Smartphone screen defects can be tiny, irregular, and low contrast. The CE-SGNet paper reports that ARFAM improves AP and AP50 relative to FPN-only features and outperforms SENet, CBAM, channel-only, and spatial-only attention variants in its attention comparison.

## Used In These Papers

- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] inserts ARFAM after FPN in [[CE-SGNet]] and reports 24.0 AP / 51.2 AP50 for ARFAM on SSGD-LB101 in the attention comparison.

## Related Concepts

- [[CE-SGNet]]
- [[Convolutional Block Attention Module]]
- [[Smartphone screen glass defect detection]]
- [[Average precision]]
