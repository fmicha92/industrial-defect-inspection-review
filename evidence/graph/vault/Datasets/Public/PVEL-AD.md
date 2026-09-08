---
title: "PVEL-AD"
aliases:
  - "PV EL Anomaly Detection dataset"
  - "PVEL-AD-2021"
  - "PVEL-AD-2019"
  - "PV Panel EL"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://github.com/binyisu/PVEL-AD"
data_sources: "GitHub"
introduced_by: "[[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]]"
---
# PVEL-AD

## Definition

PVEL-AD is a public photovoltaic-cell electroluminescence anomaly dataset introduced by [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]]. It contains near-infrared EL images of polycrystalline solar cells collected from real industrial manufacturing.

## Why It Matters

PVEL-AD gives [[Solar cell defect detection]] a larger public benchmark with box-wise annotations, anomaly-free images, long-tailed defect classes, and real production background variability.

## Used In These Papers

- [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] introduces PVEL-AD and benchmarks object detectors on it.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] uses a public high-resolution PV EL defect dataset linked at `http://aihebut.com/col.jsp?id=118` for ten-class photovoltaic defect classification; the paper reports 5,991 images and an 80/20 train/test split.
- [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] reports data availability through the PVEL-AD GitHub repository and uses it for photovoltaic panel defect detection.
- [[Dataset of Solar Cells Defect Segmentation]] includes PVEL-S, a pixel-level segmentation subset derived from PVEL-AD.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Task: [[Solar cell defect detection]], [[Defect classification]].
- Modality: 1024 x 1024 near-infrared electroluminescence images.
- Total images: 36,543.
- Anomaly-free images: 11,351.
- Defective images with box-wise annotations: 21,044.
- Defective images with category annotations: 4,148.
- Bounding boxes: 37,380 for eight defect types.
- Box-annotated defects: linear crack, star crack, finger interruption, black core, thick line, scratch, fragment, and corner.
- Category-only defects: misalignment and material anomalies.
- Acquisition: dark-room EL imaging with a cooled Si-CCD camera and polycrystalline solar cells excited by 24-V DC voltage and 8-A current.
- Artifact: IEEE DataPort DOI:10.21227/pz6t-3s77; https://github.com/binyisu/PVEL-AD; https://www.kaggle.com/competitions/pvelad.
- YOLO-ACF reuse: [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] reports the data as available at https://github.com/binyisu/PVEL-AD.
- Segmentation subset: [[Dataset of Solar Cells Defect Segmentation]] reports PVEL-S as 1200 selected PVEL-AD polysilicon defect images with pixel-level labels.
- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] evaluates [[LMFF]] on PVEL-S, a 1200-image pixel-level subset selected from PVEL-AD.
- License: not reported in the extracted text.

## Source Anchors

- Hosting source: https://github.com/binyisu/PVEL-AD.
- Introducing paper: [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]].

## Related Concepts

- [[PVEL-AD benchmark]]
- [[Solar cell defect detection]]
- [[Solar cells and photovoltaic]]
- [[F-labelImg]]
- [[Average precision]]
- [[mAP]]
- [[FPS]]
