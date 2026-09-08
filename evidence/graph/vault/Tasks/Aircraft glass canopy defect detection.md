---
title: "Aircraft glass canopy defect detection"
aliases:
  - "Aircraft glass defect detection"
  - "Aircraft canopy glass defect detection"
related_domains:
  - "[[Glass inspection]]"
related_datasets:
  - "[[AGDD]]"
tags:
  - task
  - glass-inspection
---
# Aircraft Glass Canopy Defect Detection

## Definition

Aircraft glass canopy defect detection localizes visible defects on aircraft glass canopies. [[AGDD]] frames the task around contusion, scratches, crack, and spot defects captured under paired forward and backward lighting.

## Why It Matters

Aircraft glass canopies are transparent components where defect visibility changes with illumination direction. Paired-lighting datasets such as [[AGDD]] support inspection methods that can exploit complementary views of the same defect.

## Used In These Datasets

- [[AGDD]] contains paired forward-lighting and backward-lighting images with oriented bounding-box and rectangular-box annotations.

## Used In These Papers

- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] introduces AGDD and evaluates [[ADMF-Net]] for this task.

## Related Concepts

- [[AGDD]]
- [[Glass inspection]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
- [[ADMF-Net]]
- [[Dual-modal illumination for transparent material inspection]]
