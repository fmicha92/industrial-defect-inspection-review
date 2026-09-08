---
title: "LoHi-WELD"
aliases:
  - "LoHi-WELD"
related_domain: "[[Metal inspection]]"
url: "https://github.com/SylvioBlock/LoHi-Weld"
download_url: "https://drive.google.com/file/d/1pXeEnREfV_MYcL5MY2vkd9njBm_blPUK/view?usp=sharing"
data_sources:
  - "GitHub"
  - "Google Drive"
introduced_by: "[[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]]"
doi: "10.1109/ACCESS.2024.3407019"
license: "free for research, non-commercial, or commercial purposes with citation"
---
# LoHi-WELD

## Definition

LoHi-WELD is a public weld bead image dataset for defect detection and classification. The repository and paper report 3,022 real weld bead images with manual annotations for pores, deposits, discontinuities, and stains, including low- and high-resolution images acquired from a Metal Active Gas robotic welding industrial process.

## Why It Matters

It provides a public RGB weld-inspection benchmark with real industrial imagery, manual defect annotations, and a YOLOv7 baseline for weld defect detection and classification.

## Used In These Papers

- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] introduces LoHi-WELD with 3,022 weld bead images, more than 22,000 manual defect boxes, and YOLOv7/YOLOv7-tiny baselines for four-class and defect/non-defect detection.

## Dataset Details

- Subsets: `lweld` has 2,000 low-resolution weld bead images from a 640x480 sensor; `hweld` has 1,022 high-resolution weld bead images from a 2048x1080 sensor.
- Defect classes: pores, deposits, discontinuities, and stains.
- Defect counts: 3,950 pores, 2,935 deposits, 7,220 discontinuities, and 8,307 stains.
- Annotations: manual axis-aligned bounding boxes for defect instances and weld bead regions of interest.
- Baseline split: 80% train and 20% test per subset, with 5-fold cross-validation inside the training set.

## Source Anchors

- Hosting source: https://github.com/SylvioBlock/LoHi-Weld.
- Dataset download: https://drive.google.com/file/d/1pXeEnREfV_MYcL5MY2vkd9njBm_blPUK/view?usp=sharing.
- Full-image download: https://drive.google.com/drive/folders/1m1Bvo4u4Qre8yFjEe4XNxdfYa3A5YiW4?usp=sharing.
- Introducing paper: [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]].
- Paper DOI: https://doi.org/10.1109/ACCESS.2024.3407019.

## Related Concepts

- [[Metal inspection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
