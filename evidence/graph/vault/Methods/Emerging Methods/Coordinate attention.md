---
title: "Coordinate attention"
aliases:
  - "Coordinate Attention"
  - "CA mechanism"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]"
  - "[[2024 - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution]]"
evidence_count: 2
---
# Coordinate attention

## Definition

Coordinate attention is an attention mechanism used in convolutional vision models to strengthen feature maps with position-aware information. In [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]], it is embedded into the ResNet152-Xception feature-fusion model to improve PV electroluminescence defect classification.

## Why It Matters

Defect inspection models often need to preserve subtle spatial cues. Coordinate attention is relevant when the paper's model must distinguish small or background-like defects such as cracks, star cracks, and thin-line defects in PV cell EL images.

## Used In These Papers

- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] embeds coordinate attention into a ResNet152-Xception feature-fusion classifier for PV cell defect classification.
- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] uses coordinate attention inside a multi-scale feature-fusion module for automotive glass defect detection.
- [[2024 - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution]] adds coordinate attention to the YOLOv8n neck for steel surface defect detection.

## Related Concepts

- [[Deep convolutional neural network]]
- [[Xception]]
- [[Multi-scale feature fusion]]
- [[Solar cell defect detection]]
