---
title: "KolektorSDD2"
aliases:
  - "KolektorSDD2"
availability: "public"
status: stable
concept_type: dataset
related_domain: "[[Metal inspection]]"
url: "https://www.vicos.si/Downloads/KolektorSDD2"
data_sources:
  - "VICOS"
  - "Kolektor Group"
introduced_by: "[[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]]"
related_papers:
  - "[[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]]"
---
# KolektorSDD2

## Definition

KolektorSDD2 is a public metal surface-defect dataset introduced by the mixed-supervision paper. It contains 3335 color images of production items captured with a visual inspection system in a controlled setup, with fine-grained defect masks for several defect appearances.

## Why It Matters

It supports public evaluation or training for metal surface defect detection, localization, classification, segmentation, generation, or benchmark construction.

## Used In These Papers

- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] evaluates DiffDD on KolektorSDD2 and reports 78.90 mAP, 58.90 recall, 95.44 AUROC, 74.57 F1, and 64.73 IoU.


- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] introduces KolektorSDD2, reports its public download URL, and evaluates weak, mixed, and full supervision on its fixed train/test split.
- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]] uses or reports [[KolektorSDD2]] for diffusion defect detection, surface defect detection.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses KolektorSDD2 as a source dataset for [[Industrial-5i]].

## Dataset Details

- Source: color images of defective production items provided and partially annotated by Kolektor Group d.o.o.
- Capture: visual inspection system in a controlled environment.
- Image size: approximately 230 pixels wide and 630 pixels high; the paper reports runtime at 232 x 640.
- Size: 3335 images total, with 2979 negative and 356 positive images.
- Train split: 2085 negative and 246 positive images.
- Test split: 894 negative and 110 positive images.
- Defects: shape, size, and color vary from small scratches and minor spots to large surface imperfections.
- Annotations: fine-grained segmentation masks.
- Evaluation protocol: the introducing paper reports image-level [[Average precision]] for weak, mixed, and fully supervised defect detection.
- Reported benchmark results: AP 73.3 with weak labels only, AP 83.2 with 16 pixel-annotated positive samples, and AP 95.4 with full pixel-level supervision.
- Availability: public.
- License: not reported.
- Domain: [[Metal inspection]].

## Source Anchors

- Hosting source: https://www.vicos.si/Downloads/KolektorSDD2.
- Introducing paper: [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]].

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
