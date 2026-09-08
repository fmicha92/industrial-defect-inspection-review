---
title: "AITEX"
aliases:
  - "AITEX"
  - "AITEX AFID"
  - "Public fabric defect database"
related_domain: "[[Textile and fiber inspection]]"
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
url: "https://www.aitex.es/afid/"
data_sources:
  - "AITEX AFID"
  - "factory capture system"
  - "www.aitex.es/afid"
introduced_by: "[[2019 - A Public Fabric Database for Defect Detection Methods and Results]]"
license: "not reported"
---
# AITEX

## Definition

AITEX is the public fabric defect database introduced by [[2019 - A Public Fabric Database for Defect Detection Methods and Results]]. It contains 245 grayscale images of plain fabrics, with 140 defect-free images and 105 defective images from 12 textile defect types.

## Why It Matters

The dataset gives textile defect detection, classification, segmentation, and anomaly-detection methods a shared public benchmark with real production images and hand-created segmentation masks for defective samples. Later papers use it as AITEX, AITEX AFID, and the public fabric defect database.

## Used In These Papers

- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]] introduces the dataset and demonstrates a Gabor-filter detection pipeline.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] compares ZJU-Leaper against earlier public fabric datasets and motivates richer annotations and task settings.
- [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]] uses AITEX for mask-conditioned cGAN fabric defect synthesis and downstream segmentation evaluation.
- [[2022 - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things]] uses AITEX as a public fabric dataset for GAN repair-based segmentation evaluation.
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports AITEX for industrial defect benchmarking and semantic defect annotation.
- [[2024 - Deep Industrial Image Anomaly Detection A Survey]] lists AITEX among public industrial anomaly-detection datasets.
- [[2023 - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images]] describes AITEX as a fabric defect dataset for unsupervised anomaly detection.
- [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] lists AITEX AFID as a textile defect dataset.
- [[2024 - Defect detection in textile manufacturing Improving findings using YOLOv5 versions]] reorganizes AITEX into defective-only object-detection splits and evaluates YOLOv5s/YOLOv5x with augmentation and transfer-learning variants.

## Dataset Details

- Domain: [[Textile and fiber inspection]].
- Tasks: [[Textile defect detection]], [[Defect classification]], [[Defect segmentation]].
- Hosting source: https://www.aitex.es/afid/.
- Image count: 245 images.
- Resolution: 4096 x 256 pixels.
- Color format: grayscale.
- Fabric coverage: seven fabric structures, mainly plain fabrics.
- Defect-free images: 140 total, 20 per fabric structure.
- Defective images: 105 total.
- Defect categories: cut selvage, broken end, crease, warp ball, broken yarn, knots, contamination, nep, broken pick, weft crack, weft curling, and fuzzy ball.
- Annotation: defect labels and hand-created segmentation masks for defective images.
- License: not reported.

## Source Anchors

- Hosting source: https://www.aitex.es/afid/.
- Introducing paper: [[2019 - A Public Fabric Database for Defect Detection Methods and Results]].
- Paper DOI: https://doi.org/10.2478/aut-2019-0035.

## Related Concepts

- [[Textile and fiber inspection]]
- [[Textile defect detection]]
- [[Defect classification]]
- [[Defect segmentation]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[ZJU-Leaper]]
