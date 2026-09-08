---
title: "PV-Multi-Defect"
aliases:
  - "PV Multi-Defect dataset"
  - "PV panel surface-defect detection dataset"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://github.com/CCNUZFW/PV-Multi-Defect"
data_sources:
  - "GitHub"
introduced_by: "[[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]]"
related_papers:
  - "[[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]]"
related_tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
related_methods:
  - "[[GBH-YOLOv5]]"
  - "[[YOLOv5]]"
licenses: "not reported"
modalities:
  - "RGB photovoltaic panel surface images"
  - "XML bounding-box annotations"
dataset_sizes:
  - "1,108 images"
  - "4,235 defective targets"
labels:
  - "broken"
  - "hot_spot"
  - "black_border"
  - "scratch"
  - "no_electricity"
---
# PV-Multi-Defect

## Summary

PV-Multi-Defect is a public GitHub-hosted object-detection dataset for photovoltaic panel surface-defect detection. It contains 1,108 preprocessed 600 x 600 images and XML annotations for five defect classes: broken, hot spot, black border, scratch, and no electricity.

## Dataset Details

- Host: [CCNUZFW/PV-Multi-Defect](https://github.com/CCNUZFW/PV-Multi-Defect).
- Repository status: public GitHub repository; the requested repository is a fork of `houhou34/PV-Multi-Defect`.
- Repository description: PV panel surface-defect detection dataset.
- License: not reported in the repository metadata or README.
- Folder structure: `JPEGImages` holds image files and `Annotations` holds label files.
- GitHub tree count: 1,108 `.jpg` files under `JPEGImages` and 1,106 `.xml` files under `Annotations`; the repository also contains one Markdown file in each of those folders and five top-level example images.
- Paper-reported size: 1,108 defect images from 307 original PV-panel images.
- Paper-reported original image size: 5,800 x 3,504 pixels.
- Paper-reported processed image size: 600 x 600 pixels after compression and cropping.
- Paper-reported split: 886 training images and 222 validation images.
- Paper-reported target count: 4,235 defective targets.
- Paper-reported module source: original images were taken by camera from photovoltaic modules with physical size 1.65 m x 0.991 m and specification of 60 pieces.

## Defect Classes

- `broken`: photovoltaic panels with broken areas.
- `hot_spot`: photovoltaic panels with obvious bright spot areas.
- `black_border`: photovoltaic panels with black or gray border areas.
- `scratch`: photovoltaic panels with scratched areas.
- `no_electricity`: photovoltaic panels showing black areas because they have no electricity.

## Class Distribution

The introducing paper reports the following target distribution:

| Defect class | Share of targets |
|---|---:|
| hot_spot | 49.09% |
| scratch | 36.62% |
| black_border | 6.02% |
| no_electricity | 4.28% |
| broken | 3.99% |

## Source

- Host page: [CCNUZFW/PV-Multi-Defect](https://github.com/CCNUZFW/PV-Multi-Defect).
- Introducing paper: [[2023 - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection]].
- DOI: [10.3390/electronics12030561](https://doi.org/10.3390/electronics12030561).

## Connections

- Domain: [[Solar cells and photovoltaic]].
- Tasks: [[PV panel fault detection]] and [[Object detection]].
- Model introduced with the dataset: [[GBH-YOLOv5]].
- Base detector: [[YOLOv5]].
- Evaluation metrics in the introducing paper: [[mAP]], [[Precision]], and [[Recall]].

## Open Questions

- The repository has 1,108 image files and 1,106 XML files under the primary image/annotation folders; the paper reports 1,108 images but does not explain the file-count difference.
- Dataset license is not reported.
