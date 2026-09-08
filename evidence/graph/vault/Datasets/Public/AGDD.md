---
title: "AGDD"
aliases:
  - "Aircraft Glass Defect Dataset"
  - "Aircraft glass canopy defect dataset"
related_domain: "[[Glass inspection]]"
related_tasks:
  - "[[Aircraft glass canopy defect detection]]"
url: "https://github.com/core128/AGDD"
data_sources:
  - "GitHub"
licenses:
  - "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International"
introduced_by: "[[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]]"
---
# AGDD

## Definition

AGDD, the Aircraft Glass Defect Dataset, is a public defect-detection dataset for aircraft glass canopy inspection. It contains paired defect images captured under forward and backward lighting conditions, with annotations for four defect categories.

## Why It Matters

AGDD supports [[Aircraft glass canopy defect detection]] under transparent-material inspection conditions where lighting direction changes defect visibility. The paired illumination setup makes it useful for studying multi-modal or illumination-aware glass defect detection.

## Used In These Papers

- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] introduces AGDD and the dual-illumination inspection setup.

## Dataset Details

- Domain: [[Glass inspection]].
- Task: [[Aircraft glass canopy defect detection]].
- Object type: aircraft glass canopies.
- Defect categories: contusion, scratches, crack, and spot.
- Modalities: paired images captured under forward and backward lighting.
- Size: 1752 defect points and 4784 defect objects after augmentation.
- Split: 1576 training image pairs and 176 test image pairs.
- Annotation formats: oriented bounding boxes and rectangular boxes.
- Repository: https://github.com/core128/AGDD.
- Raw resource location: `.data` directory in the repository.
- Generation scripts: `generate_dual_dataset.py` for the dual-modal dataset and `generate_composite_dataset.py` for RGB channel fusion in YOLO directory format.
- Required generation dependencies: `numpy`, `opencv-python`, and `scipy`.
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.
- Commercial use: not allowed.

## Source Anchors

- Hosting source: https://github.com/core128/AGDD.
- Introducing paper: [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]].

## Related Concepts

- [[Aircraft glass canopy defect detection]]
- [[Glass inspection]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
- [[ADMF-Net]]
- [[Dual-modal illumination for transparent material inspection]]
