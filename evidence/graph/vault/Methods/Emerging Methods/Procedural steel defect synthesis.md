---
title: "Procedural steel defect synthesis"
aliases:
  - "Procedural steel defect synthesis"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]]"
evidence_count: 1
tags:
  - emerging-method
---
# Procedural steel defect synthesis

## Definition

Procedural steel defect synthesis generates steel-surface defect images and masks with 3D graphics and shader programs. [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] implements the method in Blender by rendering a slab surface, transforming procedural noise textures into defect appearances, and producing masks alongside images.

## Why It Matters

It reduces dependence on real steel-defect collection and manual mask annotation, but it also introduces a realism gap because each defect type needs a shader and artificial defect images may not fully match real defects.

## Used In These Papers


- [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] uses [[Procedural steel defect synthesis]] for procedural defect synthesis, steel defect detection.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Procedural generation]]
- [[Defect segmentation]]
- [[Defect classification]]
- [[Metal inspection]]
