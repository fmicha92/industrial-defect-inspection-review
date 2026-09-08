---
title: "LIME"
aliases:
  - "Local Interpretable Model-agnostic Explanations"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
  - "[[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]]"
evidence_count: 2
---
# LIME

## Definition

LIME explains an individual model prediction by fitting a local surrogate model around perturbed versions of the input. In the source paper, images are perturbed at the superpixel level and the local surrogate is evaluated with [[LIME surrogate fidelity]].

## Why It Matters

LIME helps identify whether photovoltaic fault classifiers attend to panel-intrinsic regions or to contextual shortcuts.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] uses LIME as the surrogate-based part of a multi-method explainability audit.
- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] uses LIME to interpret a Bird-drop prediction from a hybrid CNN + SVM PV panel classifier.

## Related Concepts

- [[Shortcut learning]]
- [[Solar cell defect detection]]
- [[Defect classification]]
- [[Occlusion sensitivity]]
- [[Integrated Gradients]]
