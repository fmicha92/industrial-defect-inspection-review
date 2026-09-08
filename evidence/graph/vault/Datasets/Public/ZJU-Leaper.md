---
title: "ZJU-Leaper"
aliases:
  - "ZJU-Leaper dataset"
  - "ZJU-Leaper fabric dataset"
related_domain: "[[Textile and fiber inspection]]"
url: "http://www.qaas.zju.edu.cn/zju-leaper"
data_sources: "qaas.zju.edu.cn"
introduced_by: "[[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]"
---
# ZJU-Leaper

## Definition

ZJU-Leaper is a public fabric defect dataset introduced by [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]. It contains 98,777 high-quality fabric images from 19 fabric patterns, with image labels, bounding boxes, and pixel-wise masks for defective samples.

## Why It Matters

ZJU-Leaper is designed around practical [[Textile defect detection]] deployment, where each production line may use only a few fixed fabric textures for a period, defective samples are rare, and inspection models may need to improve progressively as more annotations become available.

## Used In These Papers

- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] introduces ZJU-Leaper and reports baseline experiments across five progressive annotation settings.
- [[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]] uses ZJU-Leaper to test DefectTransfer under 0.1%, 0.3%, 0.5%, and 1.0% defect-image scarcity settings. PDF Tables I-II report that ResNet101 at 0.1% defects improves from 74.91% accuracy / 1.51% F1-score with no augmentation to 84.78% accuracy / 61.15% F1-score with DefectTransfer; at 1.0% defects, DefectTransfer reaches 87.32% accuracy / 69.62% F1-score.
- [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] lists ZJU-Leaper among textile defect datasets, although its table reports sample counts inconsistently with the introducing paper.

## Dataset Details

- Domain: [[Textile and fiber inspection]].
- Task: [[Textile defect detection]], [[Defect segmentation]].
- Images: 98,777 total.
- Normal images: 71,127.
- Defective images: 27,650.
- Fabric patterns: 19 patterns organized into five texture groups.
- Annotations: image labels, bounding boxes, and pixel-wise masks.
- Test protocol: one predefined test set per pattern group, created by randomly selecting one third of the data from each pattern group.
- Artifact: http://www.qaas.zju.edu.cn/zju-leaper and https://github.com/nico-zck/zju-leaper-dataset.
- License: not reported.

## Source Anchors

- Hosting source: http://www.qaas.zju.edu.cn/zju-leaper.
- Introducing paper: [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]].

## Related Concepts

- [[ZJU-Leaper benchmark]]
- [[Textile defect detection]]
- [[Textile and fiber inspection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Dice score]]
- [[IoU]]
