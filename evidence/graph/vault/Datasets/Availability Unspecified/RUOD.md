---
title: "RUOD"
aliases:
  - "Rethinking general underwater object detection"
availability: "unspecified"
related_domain: "[[Underwater object detection]]"
related_tasks:
  - "[[Object detection]]"
  - "[[Cross-domain few-shot object detection]]"
related_papers:
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
---
# RUOD

## Definition

RUOD is an underwater object detection dataset used as a target domain for cross-domain few-shot object detection in GiPL.

## Dataset Details

- Domain: [[Underwater object detection]].
- Task: [[Object detection]] under [[Cross-domain few-shot object detection]].
- Reported visual challenges: low contrast, color distortion, and varying turbidity.
- Shot settings in GiPL: 1-shot, 5-shot, and 10-shot.
- Availability: not reported in the GiPL paper.
- Size, classes, splits, and license: not reported in the GiPL paper.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses RUOD with [[GroundingDINO]] and [[Qwen-Image generative augmentation]], reporting 34.6, 41.1, and 42.1 mAP@0.50 for 1-shot, 5-shot, and 10-shot settings.

## Related Concepts

- [[Underwater object detection]]
- [[Object detection]]
- [[Cross-domain few-shot object detection]]
- [[Qwen-Image generative augmentation]]
