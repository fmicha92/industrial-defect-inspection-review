---
title: "AuGD"
aliases:
  - "Automotive Glass Defects"
  - "Automotive glass defect dataset"
related_domain: "[[Glass inspection]]"
related_tasks:
  - "[[Diverse glass surface defect detection]]"
url: "https://github.com/FisherYuuri/GSDNet"
data_sources:
  - "GSDNet GitHub repository"
  - "Springer paper"
licenses:
  - "not reported"
introduced_by: "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
related_papers:
  - "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
  - "https://doi.org/10.1016/j.engappai.2025.110640"
access: "available from corresponding author on reasonable request"
---
# AuGD

## Definition

AuGD is an automotive glass defect dataset referenced by the GSDNet repository. The repository labels it as "Automotive Glass Defects" and points to the automotive-glass defect detection paper as the dataset source.

## Why It Matters

AuGD supports [[Diverse glass surface defect detection]] for automotive glass inspection. It adds an automotive-glass context to the glass inspection graph without merging it into broader automotive-manufacturing datasets.

## Used In These Papers

- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]] is listed by the GSDNet repository as the AuGD source.
- [A lightweight and robust detection network for diverse glass surface defects via scale- and shape-aware feature extraction](https://doi.org/10.1016/j.engappai.2025.110640) provides the GSDNet code and dataset table that references AuGD.

## Dataset Details

- Domain: [[Glass inspection]].
- Task: [[Diverse glass surface defect detection]].
- Object type: automotive glass.
- Dataset type in source table: Automotive Glass Defects.
- Host/source table: https://github.com/FisherYuuri/GSDNet.
- Dataset source listed by repository: https://link.springer.com/article/10.1007/s00371-023-03225-x.
- Image count: 7,100 final automotive-glass defect samples after augmentation and pseudo-labeling; the paper reports 210 field photographs and 1,600 manually intercepted samples before expansion.
- Defect categories: four common automotive-glass defect types are reported, but their names are not stated in the extracted text.
- Annotation format: not reported.
- Access status: available from the corresponding author on reasonable request.
- License: not reported.

## Source Anchors

- Hosting/source table: https://github.com/FisherYuuri/GSDNet.
- Dataset source paper: [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]].
- GSDNet paper: https://doi.org/10.1016/j.engappai.2025.110640.

## Related Concepts

- [[Diverse glass surface defect detection]]
- [[Glass inspection]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
