---
title: "Weibull texture features"
aliases:
  - "Weibull image statistics"
  - "Weibull features"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2011 - Non-parametric Texture Defect Detection Using Weibull Features]]"
evidence_count: 1
tags:
  - method
  - emerging-taxonomy
---

# Weibull Texture Features

## Definition

Weibull texture features summarize local image patches by fitting a Weibull distribution to the patch's gradient-magnitude distribution. [[2011 - Non-parametric Texture Defect Detection Using Weibull Features]] uses the fitted scale and shape parameters as a two-dimensional texture descriptor.

## Why It Matters

The descriptor is compact and supports unsupervised novelty detection for textured-surface defects. It avoids texture-specific supervised training in the cited paper because each image patch is compared to a per-image reference point in Weibull parameter space.

## Used In These Papers

- [[2011 - Non-parametric Texture Defect Detection Using Weibull Features]] uses Weibull scale and shape parameters from local gradient magnitudes to detect anomalous patches in [[DAGM2007]] texture images.

## Related Concepts

- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Weakly supervised learning]]
