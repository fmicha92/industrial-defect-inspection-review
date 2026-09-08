---
title: "A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images"
aliases:
  - "A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images"
paper_key: "sha256:5f7c5c4adb86d6b96a30eceef1702c76576481df7ed220e9a8c21f56f75a0ec4"
paper_type: review
year: 2023
venue: "IEEE Access"
authors:
  - "Yajie Cui"
  - "Zhaoxiang Liu"
  - "Shiguo Lian"
status: processed
processed_at: 2026-05-31
topics:
  - "unsupervised anomaly detection"
  - "industrial image datasets"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[AITEX]]"
  - "[[DAGM2007]]"
  - "[[MVTec AD]]"
methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
metrics:
  - "[[AU-ROC]]"
primary_metric: "not applicable"
doi: "10.1109/access.2023.3282993"
url: "https://doi.org/10.1109/ACCESS.2023.3282993"
pdf: "paper-inbox/10_processed/Review/2023 - Cui - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images.pdf"
related_methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[AITEX]]"
  - "[[DAGM2007]]"
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
source_file: "paper-inbox/10_processed/Review/2023 - Cui - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Cui - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Cui - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images.txt"
artifact_status: "review"
tags:
  - paper
---

# A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images

## Summary

This review categorizes unsupervised industrial visual anomaly detection algorithms and introduces publicly available industrial anomaly datasets. It is directly useful for the textile dataset question because it has a dedicated AITEX subsection and summarizes data augmentation-based anomaly detection.

## Paper Type

- Type: review.
- Why: It synthesizes unsupervised industrial anomaly detection algorithms and datasets.

## Review / Survey Details

- Scope: unsupervised visual industrial anomaly detection.
- Taxonomy: reconstruction-based, normalizing-flow, representation-based, data augmentation-based, and other algorithm categories.
- Dataset relevance: public dataset section includes AITEX, DAGM, MVTec AD, ELPV, MTD, and KolektorSDD.
- Synthesis relevance: data augmentation-based methods create synthetic abnormal images from normal images and train models jointly on normal and synthetic abnormal samples.

## Dataset Notes

- AITEX is described as 140 defect-free images plus 105 images with 12 common textile defect types, across seven fabric textures at 4096 x 256 pixels.
- DAGM is described as a surface-defect benchmark with weak supervision.
- MVTec AD is described as a public anomaly dataset with 15 categories.

## Methodological Patterns

- NSA and CutPaste are described as synthetic anomaly methods that paste or blend patches into normal images.
- Data augmentation-based methods can be fast and suitable for small datasets, but generated anomalies may not fully match real defects.
- The survey reports AUROC benchmark tables for AITEX and other datasets.

## Limitations

- Stated: open datasets cover limited scenarios, and high open-dataset AUROC may not be sufficiently instructive for real industrial deployment.
- Inferred: the survey supports AITEX as a public textile anomaly dataset but does not itself test textile synthesis.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[Unsupervised anomaly detection]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[AITEX]], [[DAGM2007]], [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Deep Industrial Image Anomaly Detection A Survey]] | Shares task | Both review public industrial anomaly datasets and synthesis-based anomaly detection. |
| [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]] | Follow-up reading | A primary AITEX textile synthesis paper. |

## Questions

- Which AUROC table values for AITEX should be extracted if comparing unsupervised methods directly?
