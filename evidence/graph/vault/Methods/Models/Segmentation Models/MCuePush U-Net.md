---
title: "MCuePush U-Net"
aliases:
  - "MCuePushU"
  - "MCue Push U-Net"
tags:
  - concept
  - architecture
source_papers:
  - "[[2020 - Surface Defect Saliency of Magnetic Tile]]"
---
# MCuePush U-Net

## Definition

MCuePush U-Net is a magnetic-tile surface-defect saliency model that combines MCue saliency preprocessing, a [[U-Net]] segmentation network, and a Push branch for bounding-box localization.

## Why It Matters

The model is designed for [[Defect segmentation]] where magnetic-tile defects can be small, low contrast, and affected by illumination. It adds explicit localization while keeping the segmentation path usable at test time without the Push branch.

## Used In These Papers

- [[2020 - Surface Defect Saliency of Magnetic Tile]] introduces MCuePush U-Net and evaluates it on [[Magnetic Tile Defects]].

## Related Concepts

- [[U-Net]]
- [[Segmentation Models]]
- [[Defect segmentation]]
- [[Metallic surface defect detection]]
- [[Magnetic Tile Defects]]
- [[F-measure]]
- [[Mean Absolute Error]]
