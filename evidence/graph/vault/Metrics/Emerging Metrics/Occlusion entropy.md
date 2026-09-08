---
title: "Occlusion entropy"
aliases:
  - "occlusion-map entropy"
  - "Shannon entropy"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# Occlusion Entropy

## Definition

Occlusion entropy measures dispersion in a normalized occlusion sensitivity relevance map using Shannon entropy.

## Direction

Lower generally indicates more concentrated relevance, but the source paper warns that concentration alone does not prove correct localization.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports entropy to distinguish diffuse and concentrated occlusion maps.

## Related Concepts

- [[Occlusion sensitivity]]
- [[Hoyer sparsity]]
- [[Shortcut learning]]
