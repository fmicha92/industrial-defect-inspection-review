---
title: "NEU-DET benchmark"
aliases:
  - "NEU-DET detection benchmark"
dataset: "[[NEU-DET]]"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
metrics:
  - "[[mAP]]"
  - "[[Average precision]]"
  - "[[Recall]]"
  - "[[FPS]]"
source_papers:
  - "[[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]"
---

# NEU-DET Benchmark

## Definition

NEU-DET benchmark is a hot-rolled steel strip surface defect detection benchmark derived from [[NEU-CLS]] by adding XML bounding-box annotations for each defect instance.

## Protocol

- Dataset: [[NEU-DET]].
- Task: [[Metallic surface defect detection]] with bounding boxes and six defect classes.
- Classes: crazing, inclusion, patches, pitted surface, rolled-in scale, scratches.
- Images: 1,800 grayscale images, 300 per class.
- Annotations: nearly 5,000 ground-truth boxes in XML files.
- Split in the introducing paper: 1,260 training images and 540 test images.

## Reported Results

| Paper | Method | Result |
|---|---|---|
| [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] | [[Defect Detection Network]] + ResNet50 | 82.3 [[mAP]] with 300 proposals. |
| [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] | [[Defect Detection Network]] + ResNet34 | 74.8 [[mAP]] with 300 proposals. |
| [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] | DDN with 50 proposals | 20 [[FPS]] on a single GPU while preserving about 92% of the 300-proposal performance. |

## Related Concepts

- [[NEU-DET]]
- [[NEU-CLS]]
- [[Metal inspection]]
- [[Object detection]]
- [[mAP]]
