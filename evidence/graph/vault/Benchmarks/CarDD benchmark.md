---
title: "CarDD benchmark"
aliases:
  - "CarDD detection benchmark"
  - "CarDD segmentation benchmark"
related_datasets:
  - "[[CarDD]]"
related_tasks:
  - "[[Car damage detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Salient object detection]]"
related_metrics:
  - "[[Average precision]]"
  - "[[F-measure]]"
  - "[[Weighted F-measure]]"
  - "[[S-measure]]"
  - "[[E-measure]]"
  - "[[Mean Absolute Error]]"
introduced_by: "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
---
# CarDD Benchmark

## Definition

CarDD benchmark evaluates car damage classification, object detection, instance segmentation, and salient object detection on [[CarDD]].

## Protocol

- Dataset: [[CarDD]].
- Split: 2,816 training images, 810 validation images, and 374 test images.
- Detection/segmentation metrics: COCO-style [[Average precision]], AP50, AP75, and object-size AP.
- Salient object detection metrics: [[F-measure]], [[Weighted F-measure]], [[S-measure]], [[E-measure]], and [[Mean Absolute Error]].
- Challenging setting: adds 500 undamaged images to the original 374 damaged test images.

## Reported Results

- ResNet-101 [[DCN+]]: 57.0 mask AP and 60.6 box AP on the standard test set.
- ResNet-101 [[DCN+]]: 55.8 mask AP and 59.4 box AP in the challenging setting.
- SGL-KRN: Fβ 0.791, weighted Fβ 0.744, Sm 0.809, Em 0.884, and MAE 0.071 for salient object detection.

## Related Concepts

- [[CarDD]]
- [[Car damage detection]]
- [[Defect segmentation]]
- [[Salient object detection]]
