---
title: "Occlusion sensitivity"
aliases:
  - "occlusion sensitivity analysis"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# Occlusion Sensitivity

## Definition

Occlusion sensitivity probes a trained vision model by masking local image patches and measuring how the prediction confidence changes. The source paper uses it to produce functional relevance maps for PV fault classifiers.

## Why It Matters

It tests whether masked image regions are causally important for the model decision, complementing visual saliency inspection.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports occlusion sensitivity maps with [[IoU@Top10%]], [[Occlusion entropy]], and [[Hoyer sparsity]].

## Related Concepts

- [[Shortcut learning]]
- [[LIME]]
- [[Integrated Gradients]]
- [[Defect classification]]
