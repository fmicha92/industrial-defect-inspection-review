---
title: "GSLU-Net"
aliases:
  - "Ghost-SE light U-Net"
  - "Ghost-SE Light U-Net"
tags:
  - concept
  - architecture
---
# GSLU-Net

## Definition

GSLU-Net is a lightweight U-Net-inspired fully convolutional segmentation network that combines [[Ghost module]] layers, squeeze-and-excitation channel attention, skip connections, and a three-level encoder-decoder structure for pixelwise surface defect detection.

## Why It Matters

The architecture targets industrial defect segmentation where small defects require dense localization but deployment constraints make heavy FCNs inconvenient. The heat-sink study reports 276,131 trainable parameters, 552,314 FLOPs, and 14.115 ms inference time per image on its heat-sink defect dataset.

## Used In These Papers

- [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]] proposes GSLU-Net for scratch and stain segmentation on heat-sink surface images.

## Related Concepts

- [[U-Net]]
- [[Ghost module]]
- [[Segmentation Models]]
- [[Defect segmentation]]
- [[Surface defect detection]]
