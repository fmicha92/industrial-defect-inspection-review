---
title: "Adjacent evaluation completed local binary patterns"
aliases:
  - "AECLBP"
  - "AECLBPs"
  - "adjacent evaluation CLBP"
  - "adjacent evaluation completed local binary pattern"
tags:
  - method
status: "stable"
concept_type: "method"
source_papers:
  - "[[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]"
related_methods:
  - "[[Feature extraction]]"
related_tasks:
  - "[[Defect classification]]"
related_datasets:
  - "[[NEU-CLS]]"
related_metrics:
  - "[[Accuracy]]"
---
# Adjacent evaluation completed local binary patterns

## Definition

Adjacent evaluation completed local binary patterns (AECLBP) is a local texture descriptor that modifies completed local binary patterns by replacing each neighbor pixel value with the mean value of a small adjacent evaluation window around that neighbor. The paper combines sign, magnitude, and center components as AECLBP S/M/C histograms for defect recognition.

## Why It Matters

AECLBP is designed to make local binary-pattern-style feature extraction less sensitive to noise in hot-rolled steel strip surface images. On the NEU surface defect database, AECLBP reports higher recognition accuracy than LBP, LTP, and CLBP in both clean and Gaussian-noise experiments.

## Used In These Papers

- [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]] introduces AECLBP and reports 98.93 +/- 0.63 SVM accuracy on [[NEU-CLS]].

## Related Concepts

- [[Feature extraction]]
- [[Defect classification]]
- [[NEU-CLS]]
- [[Accuracy]]
