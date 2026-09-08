---
title: "DCN+"
aliases:
  - "improved DCN"
  - "CarDD DCN+"
source_papers:
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
related_methods:
  - "[[Focal loss]]"
  - "[[Multi-scale learning]]"
---
# DCN+

## Definition

DCN+ is an improved deformable-convolution detection and instance-segmentation model proposed for [[CarDD]]. It combines [[Focal loss]] with [[Multi-scale learning]] to improve hard car-damage classes.

## Why It Matters

The model targets dent, scratch, and crack instances, which the CarDD paper identifies as hard because of small scale, irregular shape, flexible boundaries, and visual similarity.

## Used In These Papers

- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] reports that ResNet-101 DCN+ improves over ResNet-101 DCN from 52.5 to 57.0 mask AP and from 54.3 to 60.6 box AP on [[CarDD benchmark]].

## Related Concepts

- [[Focal loss]]
- [[Multi-scale learning]]
- [[CarDD]]
- [[Car damage detection]]
