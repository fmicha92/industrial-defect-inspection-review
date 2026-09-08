---
title: "Open Stamped Parts Dataset"
aliases:
  - "OSPD"
  - "Open Stamped Parts Dataset"
  - "Synthetic-OSPD"
related_domain: "[[Automotive manufacturing]]"
url: "https://214557p1st.blob.core.windows.net/public/case2024.ZIP"
landing_url: "https://arxiv.org/abs/2403.10369"
doi: "10.48550/arXiv.2403.10369"
data_sources:
  - "Azure Blob Storage"
  - "General Motors"
access: "open"
modalities:
  - "image"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Defect segmentation]]"
methods:
  - "[[Simulation-based data augmentation]]"
  - "[[Procedural and simulation-based synthesis]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
  - "[[Synthetic data generation]]"
  - "[[Domain gap]]"
introduced_by: "[[2024 - Open Stamped Parts Dataset]]"
related_papers:
  - "[[2024 - Open Stamped Parts Dataset]]"
---
# Open Stamped Parts Dataset

## Definition

Open Stamped Parts Dataset (OSPD) is a public image dataset for stamped metal-sheet inspection in auto manufacturing. It combines real camera images from stamped parts with synthetic images generated to mimic the production environment.

## Why It Matters

OSPD targets missing stamped-hole defects, a quality-control problem where actual defects are rare and manual inspection is laborious. The dataset is useful for studying synthetic-to-real transfer, object detection, instance segmentation, and domain gap in automotive visual inspection.

## Dataset Details

- Dataset purpose: develop and evaluate machine-vision models for detecting stamped holes and inferring missing-hole defects in metal-sheet stamping.
- Organization: General Motors.
- Authors: Sarah Antiles and Sachin S. Talathi.
- Domain: [[Automotive manufacturing]].
- Modality: grayscale images of stamped metal sheets.
- Real image acquisition: real part images were captured from 7 cameras; the fixture has 40 cameras across the left, right, entrance, and exit sides.
- Synthetic data generation: Unreal Engine was used to simulate camera angle, focal length, lighting, random camera shift, part shift, and lighting changes.
- Total images reported in the paper comparison table: 11,340 synthetic images and 9,660 real images.
- Real labeled data: 1,680 labeled real images.
- Real unlabeled data: 7,980 unlabeled real images.
- Synthetic splits: 7,980 training images, 1,680 validation images, and 1,680 test images.
- Annotation types: bounding boxes around stamped holes; synthetic data also includes segmentation masks.
- Hole categories: 7 distinct hole categories are generated in the synthetic images.
- Defect construction: 10% of holes are masked to mimic missing stamped-hole defects.
- Masked-hole counts reported: 665 masked holes in the real 10% masked set and 4,964 masked holes in the synthetic data.
- Dataset subsets: synthetic, real labeled reference, real unlabeled, real labeled, and real labeled 10% masked.
- Primary task framing: detect existing holes, then infer which expected holes are missing.
- Benchmark model: YOLOv7 hole-detection baseline trained for 1,000 epochs with batch size 8 on an NVIDIA A100 GPU.
- Reported best baseline: synthetic multi-class model reports 67.2 modified recall and 94.4 precision.
- Download size observed from the redirected dataset URL: about 14.1 GB.
- License: not reported in the arXiv paper text.

## Source Anchors

- Paper landing page: [https://arxiv.org/abs/2403.10369](https://arxiv.org/abs/2403.10369)
- Paper DOI: [10.48550/arXiv.2403.10369](https://doi.org/10.48550/arXiv.2403.10369)
- Dataset link given by the paper: [https://tinyurl.com/hm6xatd7](https://tinyurl.com/hm6xatd7)
- Resolved dataset file: [https://214557p1st.blob.core.windows.net/public/case2024.ZIP](https://214557p1st.blob.core.windows.net/public/case2024.ZIP)

## Related Concepts

- [[2024 - Open Stamped Parts Dataset]]
- [[Automotive manufacturing]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
- [[Metallic surface defect detection]]
- [[Defect segmentation]]
- [[Synthetic data generation]]
- [[Simulation-based data augmentation]]
- [[Procedural and simulation-based synthesis]]
- [[Domain gap]]

## Questions

- What license or reuse terms apply to the released ZIP file?
- Does the dataset include a formal metadata file describing file layout, splits, and labels?
- Should missing stamped-hole detection become a dedicated task note if more automotive stamping papers are added?
