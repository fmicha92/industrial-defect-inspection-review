---
title: "Integrated Gradients"
aliases:
  - "IG"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# Integrated Gradients

## Definition

Integrated Gradients attributes a prediction to input pixels by integrating gradients along a path from a baseline image to the actual image.

## Why It Matters

In photovoltaic fault recognition, Integrated Gradients can be paired with deletion-insertion tests to check whether high-attribution pixels are causally coupled to the predicted class.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] uses Integrated Gradients and reports [[Faithfulness gap]] from deletion-insertion analysis.

## Related Concepts

- [[Shortcut learning]]
- [[LIME]]
- [[Occlusion sensitivity]]
- [[Defect classification]]
