---
title: "Phase-Invariant Feature Module"
aliases:
  - "PIFM"
tags:
  - method
  - feature-extraction
---

# Phase-Invariant Feature Module

## Definition

Phase-Invariant Feature Module is the optional feature module introduced in [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]]. It learns shallow image features intended to be invariant to hue transformations that approximate illuminant-angle changes.

## Why It Matters

PIFM is designed to reduce detector sensitivity to lighting angle. The paper reports average precision gains of 4.1 to 5.5 percentage points over static mixing when PIFM with phase-shift transformations is used across object detectors on [[MSDD]].

## Used In These Papers

- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] uses PIFM to replace early detector backbone stages and support end-to-end defect detection on [[MSDD]].

## Related Concepts

- [[Taylor Series Channel Mixer]]
- [[Stroboscopic Illuminant Image Acquisition]]
- [[Object detection]]
- [[mAP@0.50]]
