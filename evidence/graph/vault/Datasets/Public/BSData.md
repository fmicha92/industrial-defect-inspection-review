---
title: "BSData"
aliases:
  - "Industrial Machine Tool Component Surface Defect Dataset"
  - "Industrial Machine Tool Element Surface Defect Dataset"
  - "Ball Screw Drive Surface Defect Dataset"
availability: "public"
status: "stable"
concept_type: "dataset"
related_domain: "[[Metal inspection]]"
url: "https://github.com/2Obe/BSData"
data_sources:
  - "GitHub"
  - "KITopen"
introduced_by: "[[2021 - Industrial Machine Tool Component Surface Defect Dataset]]"
licenses: "CC-BY-SA-4.0"
doi: "10.5445/IR/1000129520"
related_tasks:
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
  - "[[Wear forecasting]]"
related_methods:
  - "[[Mask R-CNN]]"
related_metrics:
  - "[[mIoU]]"
---

# BSData

## Definition

BSData is a public ball-screw-drive surface-defect dataset for pitting classification, detection, segmentation, and wear-progression analysis. It contains RGB image data from machine-tool component surfaces and annotations for pitting damage.

## Why It Matters

BSData provides a real-world machine-tool surface dataset where defects can be small, polluted, temporally developing, and difficult to annotate. It supports conventional pitting classification, pixel-level defect segmentation, and wear forecasting from image sequences.

## Dataset Details

- Hosting source: [GitHub repository](https://github.com/2Obe/BSData).
- Dataset publication DOI: [10.5445/IR/1000129520](https://doi.org/10.5445/IR/1000129520).
- License: CC-BY-SA-4.0 in the GitHub repository.
- Object/component: ball screw drives.
- Defect type: pitting from surface disruption.
- Image modality: RGB surface images.
- Annotation tooling: LabelMe JSON annotations, convertible to VOC and COCO formats.
- Segmentation/detection release: 1104 channel-3 images with 394 image annotations for pitting.
- Classification release: 21853 150 x 150 RGB PNG images, with 11075 images without pitting and 10778 images with pitting.
- Repository structure: `data` for JPEG images, `label` for annotations, and `saved_model` for the baseline model.
- Split script: `split_dataset.py` supports `train_test_split`, `wear_dev_split`, and `type_split`.
- Wear development: the detection/segmentation release contains 27 pitting development sequences.
- Baseline model: [[Mask R-CNN]] with COCO-pretrained Inception-ResNet-v2 backbone; the paper reports baseline mIoU 0.316.

## Splits

- `train_test_split`: train/test split used for the baseline model.
- `wear_dev_split`: creates the 27 wear-development sequences.
- `type_split`: splits the data by the two occurring ball-screw-drive types.

## Used In These Papers

- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] introduces BSData and reports the dataset structure, collection setup, annotation formats, and baseline model.
- [[2022 - A Model for Surface Defect Detection of Industrial Products Based on Attention Augmentation]] evaluates object detection on a 394-image BSData subset and reports 82.00 [[mAP@0.50]].
- [[2023 - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output]] uses BSData for binary defect classification with CAM localization, reporting best BSData localization [[IoU]] of 0.85.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses BSData as one of the source datasets for [[Industrial-5i]].

## Source Anchors

- Dataset host: [https://github.com/2Obe/BSData](https://github.com/2Obe/BSData).
- Dataset publication DOI: [10.5445/IR/1000129520](https://doi.org/10.5445/IR/1000129520).
- Related paper: [[2021 - Industrial Machine Tool Component Surface Defect Dataset]].

## Related Concepts

- [[Metal inspection]]
- [[Surface defect detection]]
- [[Defect classification]]
- [[Object detection]]
- [[Defect segmentation]]
- [[Wear forecasting]]
- [[mIoU]]
- [[Mask R-CNN]]
- [[Industrial-5i]]
