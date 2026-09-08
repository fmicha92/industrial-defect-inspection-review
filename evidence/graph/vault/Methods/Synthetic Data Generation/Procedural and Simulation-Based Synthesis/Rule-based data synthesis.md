---
title: "Rule-based data synthesis"
aliases:
  - "Rule-based synthetic data"
  - "Rule-based synthetic data generation"
  - "Rule-based data generation"
tags:
  - method
---

# Rule-based data synthesis

## Definition

Rule-based data synthesis creates artificial examples from explicit rules, templates, constraints, perturbation policies, or parameterized procedures rather than from a learned generative model.

## Why It Matters

Rule-based synthesis is useful when generated examples must be controllable, reproducible, interpretable, or automatically labeled. Its main risk is that handcrafted rules can miss the variability and edge cases present in real data.

## Typical Use

- Generate rare or expensive defect cases with explicit placement, shape, severity, or frequency rules.
- Create synthetic labels, masks, bounding boxes, or class assignments as part of the generation process.
- Stress-test models with controlled variations that isolate specific factors.
- Produce training data when real examples are scarce and learned generators would be underconstrained.

## Used In These Papers

- not reported

## Related Concepts

- [[Synthetic data generation]]
- [[Procedural and simulation-based synthesis]]
- [[Hybrid generative-procedural synthesis]]
- [[Procedural generation]]
- [[Simulation-based data augmentation]]
- [[Domain randomization]]
- [[Defect synthesis]]
