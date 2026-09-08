---
title: "CARPK"
aliases:
  - "CARPK dataset"
availability: "unspecified"
related_domain: "[[Parking lot vehicle monitoring]]"
related_tasks:
  - "[[Object detection]]"
  - "[[Cross-domain few-shot object detection]]"
related_papers:
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
---
# CARPK

## Definition

CARPK is a drone-based parking-lot vehicle dataset used as a dense-object target domain in GiPL.

## Dataset Details

- Domain: [[Parking lot vehicle monitoring]].
- Task: [[Object detection]] under [[Cross-domain few-shot object detection]].
- Reported challenge: high-density vehicle instances, with sparse few-shot support annotations that may label only one instance per image.
- Shot settings in GiPL: 1-shot, 5-shot, and 10-shot.
- Availability: not reported in the GiPL paper.
- Size, classes, splits, and license: not reported in the GiPL paper.

## Used In These Papers

- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses CARPK with [[GLIP]] and iterative [[Pseudo-labeling]], reporting 63.3, 63.0, and 61.3 mAP@0.50 for 1-shot, 5-shot, and 10-shot settings.

## Related Concepts

- [[Parking lot vehicle monitoring]]
- [[Object detection]]
- [[Cross-domain few-shot object detection]]
- [[Pseudo-labeling]]
