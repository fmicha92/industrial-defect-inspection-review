---
title: "Deep Industrial Image Anomaly Detection: A Survey"
aliases:
  - "Deep Industrial Image Anomaly Detection A Survey"
paper_key: "doi:10.1007/s11633-023-1459-z"
paper_type: review
year: 2024
venue: "Machine Intelligence Research"
authors:
  - "Jiaqi Liu"
  - "Guoyang Xie"
  - "Jinbao Wang"
  - "Shangnian Li"
  - "Chengjie Wang"
  - "Feng Zheng"
  - "Yaochu Jin"
status: processed
processed_at: 2026-05-31
topics:
  - "industrial image anomaly detection"
  - "anomaly synthesis"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[AITEX]]"
  - "[[DAGM2007]]"
  - "[[MVTec AD]]"
methods:
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
  - "[[GAN]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PR]]"
  - "[[F1-score]]"
primary_metric: "not applicable"
doi: "10.1007/s11633-023-1459-z"
url: "https://doi.org/10.1007/s11633-023-1459-z"
pdf: "paper-inbox/10_processed/Review/2024 - Liu - Deep Industrial Image Anomaly Detection A Survey.pdf"
related_methods:
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
  - "[[GAN]]"
related_datasets:
  - "[[AITEX]]"
  - "[[DAGM2007]]"
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
source_file: "paper-inbox/10_processed/Review/2024 - Liu - Deep Industrial Image Anomaly Detection A Survey.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Liu - Deep Industrial Image Anomaly Detection A Survey.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Liu - Deep Industrial Image Anomaly Detection A Survey.txt"
artifact_status: "review"
tags:
  - paper
---

# Deep Industrial Image Anomaly Detection: A Survey

## Summary

This survey reviews deep industrial image anomaly detection methods by architecture, supervision level, loss, metric, and dataset. It explicitly discusses anomaly synthesis and lists public anomaly datasets including AITEX, DAGM, MVTec AD, and a fabric dataset entry.

## Paper Type

- Type: review.
- Why: It synthesizes industrial anomaly detection literature and benchmark resources.

## Review / Survey Details

- Scope: deep-learning industrial image anomaly detection.
- Inclusion criteria: not fully reported in extracted text.
- Taxonomy: feature-embedding, reconstruction, normalizing flow, memory, supervision setting, anomaly synthesis, datasets, and metrics.
- Dataset relevance: Table 7 compares anomaly-detection datasets; AITEX and a fabric dataset are included among industrial datasets.
- Synthesis relevance: Section 4.3 discusses anomaly synthesis, including generated defects on defect-free fabric images, CycleGAN transfer between fabrics, SDGAN, DTGAN, and DefectGAN.

## Dataset Notes

- AITEX is described as an industrial anomaly dataset in the survey's dataset comparison.
- DAGM and MVTec AD are also listed as important public anomaly datasets.
- The survey notes that most open-source anomaly datasets either generate anomalies from anomaly-free products or do not represent real production anomalies.

## Methodological Patterns

- Synthetic anomaly images are used to improve anomaly maps and train segmentation modules.
- Reconstruction-based methods often compare original and reconstructed images.
- GAN, diffusion, and other generative methods are identified as anomaly synthesis directions.

## Limitations

- Stated: current open industrial anomaly datasets are limited in domain diversity and may not reflect real production distributions.
- Inferred: textile-specific conclusions require primary textile papers rather than this broad survey.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[Synthetic data generation]], [[Data augmentation]], [[GAN]]
- Datasets: [[AITEX]], [[DAGM2007]], [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PR]], [[F1-score]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - A Survey on Unsupervised Anomaly Detection Algorithms for Industrial Images]] | Shares task | Both survey unsupervised/industrial anomaly detection and public datasets. |
| [[2022 - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things]] | Shares dataset / shares method | A primary AITEX GAN-repair paper relevant to the survey's anomaly synthesis discussion. |

## Questions

- Which "Fabric dataset" entry in Table 7 maps to an existing public textile dataset note?
