---
title: "BenchmarkELimages"
aliases:
  - "Benchmark datasets for defect detection in EL images of solar cells using semantic segmentation"
  - "Benchmark dataset of solar PV EL images and ground truth masks"
  - "PV EL semantic segmentation benchmark"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://github.com/TheMakiran/BenchmarkELimages"
data_sources:
  - "GitHub"
  - "Dropbox"
  - "CSIR Energy Centre"
  - "CFV Labs"
  - "ARTsolar"
  - "CWRU SDLE Research Center"
  - "ZAE Bayern"
introduced_by: "[[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]]"
related_papers:
  - "[[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
related_methods:
  - "[[U-Net]]"
  - "[[PSPNet]]"
  - "[[DeepLabV3+]]"
related_metrics:
  - "[[mIoU]]"
  - "[[Recall]]"
licenses: "not reported"
modalities:
  - "electroluminescence images"
  - "pixel-level ground truth masks"
dataset_sizes:
  - "593 labelled images in the introducing paper"
  - "over 150,000 unlabelled cell-level images linked from the repository"
labels:
  - "24 classes in dataset_20211104"
  - "29 classes in dataset_20221008"
---
# BenchmarkELimages

## Summary

BenchmarkELimages is a public GitHub-hosted benchmark collection for multi-class semantic segmentation of solar-cell electroluminescence images. It provides labelled EL images, indexed ground-truth masks, RGB masks, train/validation/test folders, and a linked unlabelled set of cropped cell-level EL images for semi-supervised or self-supervised learning.

## Dataset Details

- Host: [TheMakiran/BenchmarkELimages](https://github.com/TheMakiran/BenchmarkELimages).
- Repository description: benchmark dataset of solar PV EL images and corresponding ground truth masks.
- Availability: public GitHub repository; the unlabelled set is linked through Dropbox.
- License: not reported in the repository metadata or README.
- Labelled sources: three private sources, named as CSIR Energy Centre, CFV Labs, and ARTsolar, plus public images selected from CWRU SDLE Research Center and ZAE Bayern.
- Paper-reported labelled dataset: 593 EL images of solar cells with pixel-level ground-truth masks.
- Image format reported by the paper: final 512 x 512 images with a full cell centered and surrounding adjacent cells, module edge, or padding depending on source and cell location.
- Crystal types: roughly equal mono-crystalline and multi-crystalline cells.
- Original labelled dataset: `dataset_20211104` has 24 labels, described as 12 intrinsic features and 12 extrinsic defects.
- Later repository release: `dataset_20221008` class mapping has 29 labels, adding labels such as half-cut mono spacing, scuff, corrosion cell, brightening, and star.
- Repository top-level labelled releases: `dataset_20211104`, `dataset_20220723`, and `dataset_20221008`.
- Repository tree counts from GitHub API:
  - `dataset_20211104`: 50 test images, 54 validation images, 478 original training images, 1,434 augmented training images, with matching coded masks.
  - `dataset_20220723`: 66 test images, 65 validation images, 2,044 training images, and 642 RGB masks.
  - `dataset_20221008`: 72 test images, 70 validation images, 2,212 training images, and 695 RGB masks.
- Unlabelled set: the repository README links a Dropbox folder with over 150,000 cell-level EL images cropped from 2,573 module-level EL images; over 2,000 module-level images came from one module supplier during construction of a 911 kWp DC rooftop installation at CSIR commissioned in 2018.

## Label Scope

- Feature labels include background, mono/multi/dogbone cell spacing, ribbons, border, text, padding, clamp, busbars, frame edge, and junction-box-related features.
- Defect labels in the original class map include crack ribbon edge, inactive, rings, material, crack, gridline, splice, dead cell, corrosion, belt mark, edge dark, and measurement artifact.
- The introducing paper focuses evaluation on cracks, inactive areas, gridline defects, ribbon interconnects, and cell spacing.

## Source

- Host page: [TheMakiran/BenchmarkELimages](https://github.com/TheMakiran/BenchmarkELimages).
- Introducing paper: [[2023 - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation]].
- Prior dataset citation for `dataset_20211104`: the README asks users to cite the 2021 Renewable Energy paper on defect detection and quantification using U-Net semantic segmentation.
- Repository citation for other dataset releases and the unlabelled set: the README asks users to cite the 2023 Systems and Soft Computing paper.

## Connections

- Domain: [[Solar cells and photovoltaic]].
- Tasks: [[Solar cell defect detection]] and [[Defect segmentation]].
- Compared segmentation models in the introducing paper: [[U-Net]], [[PSPNet]], and [[DeepLabV3+]].
- Evaluation metrics in the introducing paper: [[mIoU]] and [[Recall]].

## Open Questions

- The repository does not report a license.
- The README reports later releases and corrections beyond the 593-image dataset described in the paper; source-specific counts should be kept separate when comparing experiments.
