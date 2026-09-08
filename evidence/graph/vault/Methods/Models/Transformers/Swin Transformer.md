---
title: "Swin Transformer"
aliases:
  - "SwinV2-B"
  - "SWin transformer"
tags:
  - method
concept_type: method
candidate_parent: "Methods/Models/Transformers"
source_papers:
  - "[[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]]"
evidence_count: 1
---
# Swin Transformer

## Definition

Swin Transformer is a vision transformer family used for image feature extraction. In [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]], a SwinV2-B backbone extracts features from electroluminescence images before a dense output layer predicts a 400-point normalized I-V curve.

## Why It Matters

The shifted-window transformer design gives the paper a multi-scale image-feature extractor for relating EL image patterns to photovoltaic module electrical behavior.

## Used In These Papers

- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] initializes a SwinV2-B transformer with ImageNet weights, trains an output layer, then fine-tunes the full model for I-V curve prediction.

## Related Concepts

- [[Vision Transformer]]
- [[PV module current-voltage curve prediction]]
- [[Transfer learning]]
