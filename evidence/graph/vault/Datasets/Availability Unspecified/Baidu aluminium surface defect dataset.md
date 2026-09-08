---
title: "Baidu aluminium surface defect dataset"
aliases:
  - "Baidu PaddlePaddle aluminium surface defect dataset"
  - "Aluminium surface defect dataset"
related_domain: "[[Metal inspection]]"
url: "not reported"
data_sources:
  - "Baidu PaddlePaddle"
introduced_by: "not reported"
related_papers:
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
---
# Baidu Aluminium Surface Defect Dataset

## Definition

The Baidu aluminium surface defect dataset is an aluminium-surface defect detection dataset used by [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]. The paper attributes the dataset to Baidu PaddlePaddle and reports 640 x 480 source images with zhen_kong, ca_shang, zang_wu, zhe_zhou, and other defect types.

## Why It Matters

It provides a small, imbalanced aluminium defect detection setting for evaluating whether object detectors handle variable defect scale, low visibility, and lighting effects.

## Dataset Details

- Availability: not reported as directly public in the paper.
- Source resolution: 640 x 480.
- Preprocessing: gamma enhancement with Gamma = 0.9 to improve dark defect details and reduce some white noise.
- Augmentation: flipping, rotation, and shifting.
- Expanded size: 1236 images.
- Split: training, validation, and test in an 8:1:1 ratio.
- Reported class counts: zhen_kong 516, ca_shang 694, zang_wu 1087, zhe_zhou 307.
- License: not reported.

## Used In These Papers

- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] evaluates IDD-Net and detector baselines on this aluminium defect dataset, reporting IDD-Net at 99.5% [[mAP@0.50]] and 57.79% [[mAP@0.50-0.95]].

## Source Anchors

- Hosting source: not reported.
- Paper source: [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]].
- Introducing paper: not reported.

## Related Concepts

- [[Metal inspection]]
- [[Metallic surface defect detection]]
- [[Object detection]]
- [[mAP@0.50]]
