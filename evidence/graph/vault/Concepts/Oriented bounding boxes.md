---
title: "Oriented bounding boxes"
aliases:
  - "OBB"
  - "rotated bounding boxes"
tags:
  - concept
  - annotation
---

# Oriented Bounding Boxes

## Definition

Oriented bounding boxes are rotated rectangular annotations that can align with objects whose major axis is not horizontal or vertical.

## Why It Matters

Aircraft glass canopy defects can be slender, interlaced, or high aspect ratio. The AGDD paper uses OBB annotations so defect boxes can better fit scratches, cracks, and other rotated defect shapes.

## Used In These Papers

- [[2024 - Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies]] annotates AGDD with oriented bounding boxes and trains ADMF-Net with an OBB detection head.

## Related Concepts

- [[Object detection]]
- [[Aircraft glass canopy defect detection]]
- [[AGDD]]
