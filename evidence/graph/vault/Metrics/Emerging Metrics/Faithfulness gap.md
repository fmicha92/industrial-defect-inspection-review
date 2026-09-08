---
title: "Faithfulness gap"
aliases:
  - "Deletion-insertion faithfulness gap"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# Faithfulness Gap

## Definition

Faithfulness gap is the insertion AUC minus deletion AUC in deletion-insertion attribution tests. Positive values indicate that confidence decreases when high-attribution pixels are removed and recovers when they are reintroduced.

## Direction

Higher positive values indicate stronger attribution faithfulness under the adopted perturbation protocol.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] reports faithfulness gap for Integrated Gradients explanations across five CNN architectures.

## Related Concepts

- [[Integrated Gradients]]
- [[Shortcut learning]]
- [[Defect classification]]
