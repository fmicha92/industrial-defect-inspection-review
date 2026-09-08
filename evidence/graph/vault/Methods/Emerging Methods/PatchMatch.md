---
title: "PatchMatch"
aliases:
  - "PatchMatch nearest-neighbor field"
status: emerging
concept_type: method
candidate_parent: "Methods/Data Augmentation"
source_papers:
  - "[[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]]"
evidence_count: 1
tags:
  - method
---

# PatchMatch

## Definition

PatchMatch is used as a patch-based nearest-neighbor field method for removing defect regions before synthesizing non-defect periodic textures.

## Why It Matters

Patch-based defect removal can turn defective images into pseudo clean texture inputs when real non-defect samples are unavailable. In weakly supervised periodic-texture segmentation, this supports non-defect-domain construction for golden-template generation.

## Used In These Papers

- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses PatchMatch to remove manually localized defect regions before PSGAN synthesizes non-defect periodic texture images.

## Related Concepts

- [[Data augmentation]]
- [[Synthetic data generation]]
- [[PSGAN]]
- [[Defect segmentation]]
