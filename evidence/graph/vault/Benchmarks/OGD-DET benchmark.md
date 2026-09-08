---
title: "OGD-DET benchmark"
aliases:
  - "OGD-DET optical glass defect benchmark"
datasets:
  - "[[OGD-DET]]"
tasks:
  - "[[Optical glass defect detection]]"
metrics:
  - "[[mAP@0.25]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.75]]"
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[FPS]]"
introduced_by: "[[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]]"
---
# OGD-DET Benchmark

## Definition

OGD-DET benchmark evaluates optical-glass defect detection on [[OGD-DET]] at image level and video level.

## Protocol

- Dataset: [[OGD-DET]].
- Task: [[Optical glass defect detection]].
- Training videos: 25.
- Test videos: 15.
- Test images: 511.
- Image-level input: frames resized to 416 x 416 pixels.
- Video-level test set: 15 videos, including 5 normal and 10 defective samples.
- Metrics: AP at IoU 0.25, 0.50, and 0.75; recall and precision at IoU 0.25 and confidence 0.5; FPS.

## Reported Results

| Model | AP@0.25 | AP@0.50 | AP@0.75 | FPS |
|---|---:|---:|---:|---:|
| Faster RCNN | 0.7821 | 0.6024 | 0.4740 | 10 |
| SSD300 | 0.6030 | 0.0280 | 0.0 | 46 |
| SSD512 | 0.8760 | 0.5246 | 0.2551 | 22 |
| YOLOv5 | 0.9730 | 0.7720 | 0.5270 | 25 |
| Proposed method | 0.9948 | 0.8616 | 0.8166 | 21 |

## Used In These Papers

- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] introduces the benchmark and reports image-level and video-level detector comparisons.

## Related Concepts

- [[OGD-DET]]
- [[Optical glass defect detection]]
- [[Video-based two-stage defect detection]]
- [[Average precision]]
- [[FPS]]
