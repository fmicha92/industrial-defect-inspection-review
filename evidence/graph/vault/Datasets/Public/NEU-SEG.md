---
title: "NEU-SEG"
aliases:
  - "NEU-SEG"
  - "NEU-Seg"
  - "NEU Seg"
related_domain: "[[Metal inspection]]"
url: "http://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm"
download_url: "https://github.com/donghongwen/NEU_Seg"
data_sources:
  - "Northeastern University surface defect database"
  - "NEU_Seg GitHub repository"
introduced_by: "[[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]"
source_datasets:
  - "Northeastern University surface defect database"
related_papers:
  - "[[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]"
  - "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
---
# NEU-SEG

## Definition

NEU-SEG is a hot-rolled steel strip surface defect segmentation dataset introduced by [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]]. The paper starts from the Northeastern University surface defect database, selects inclusion, patches, and scratches, and adds pixel-wise LabelMe annotations for the pixel-wise surface defect detection task.

## Why It Matters

It provides pixel-level segmentation supervision for three hot-rolled steel strip defect classes: inclusion, patches, and scratches. It is the segmentation counterpart to the NEU surface defect database releases for classification and detection.

## Used In These Papers

- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] evaluates DiffDD on NEU-SEG and reports 87.75 mAP, 81.94 recall, 97.68 AUROC, 85.14 F1, and 76.53 IoU.


- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] uses or reports [[NEU-SEG]] for diffusion defect detection, surface defect detection.
- [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]] introduces NEU-SEG and reports 82.15% [[mIoU]] on the dataset.
- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]] evaluates [[FDSNet]] on NEU-SEG as a steel-strip surface-defect segmentation benchmark.
- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] augments NEU-SEG with LoRA-adapted Stable Diffusion images and improves DeepLabV3+ mIoU from 71.31 to 76.20.

## Source Anchors

- Host source: http://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm.
- NEU-Seg source link: https://github.com/donghongwen/NEU_Seg.
- Underlying source imagery: Northeastern University surface defect database.
- Introducing paper: [[2020 - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection]].
- Related source paper for the underlying NEU imagery: [[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]].

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Defect segmentation]]
- [[PGA-Net]]
- [[FDSNet]]
- [[mIoU]]
