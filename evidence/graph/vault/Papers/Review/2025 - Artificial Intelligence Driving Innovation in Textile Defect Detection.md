---
title: "Artificial Intelligence Driving Innovation in Textile Defect Detection"
aliases:
  - "Artificial Intelligence Driving Innovation in Textile Defect Detection"
paper_key: "doi:10.3390/textiles5020012"
paper_type: review
year: 2025
venue: "Textiles"
authors:
  - "Ahmet Ozek"
  - "Mine Seckin"
  - "Pinar Demircioglu"
  - "Ibrahim Bogrekci"
status: processed
processed_at: 2026-05-31
topics:
  - "AI textile defect detection"
  - "textile defect datasets"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[AITEX]]"
  - "[[Lusitano]]"
  - "[[TILDA]]"
  - "[[ZJU-Leaper]]"
methods:
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[GAN]]"
metrics: []
primary_metric: "not applicable"
doi: "10.3390/textiles5020012"
url: "https://doi.org/10.3390/textiles5020012"
pdf: "paper-inbox/10_processed/Review/2025 - Ozek - Artificial Intelligence Driving Innovation in Textile Defect Detection.pdf"
related_methods:
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[GAN]]"
related_datasets:
  - "[[AITEX]]"
  - "[[Lusitano]]"
  - "[[TILDA]]"
  - "[[ZJU-Leaper]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Review/2025 - Ozek - Artificial Intelligence Driving Innovation in Textile Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Ozek - Artificial Intelligence Driving Innovation in Textile Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Ozek - Artificial Intelligence Driving Innovation in Textile Defect Detection.txt"
artifact_status: "review"
tags:
  - paper
---

# Artificial Intelligence Driving Innovation in Textile Defect Detection

## Summary

This review surveys traditional, machine-learning, and deep-learning textile defect detection and includes a useful table of textile defect datasets. It identifies limited high-quality labeled textile data as a key challenge and names data augmentation, GANs, and synthetic image generation as future directions for robust model training.

## Paper Type

- Type: review.
- Why: It reviews textile defect detection technologies and datasets.

## Review / Survey Details

- Scope: textile quality control, defect types, imaging technologies, machine learning, deep learning, and future AI directions.
- Dataset relevance: Table 2 lists textile defect datasets including AITEX AFID, Fabric Defect Dataset, FabricDefect, Fabric Defect Detection, Lusitano, ZJU-Leaper, TILDA, ZJU-Leaper GitHub, and TILDA_400.
- Synthesis relevance: Section 5.4 states that future textile defect research will focus on data augmentation, GANs, and synthetic image generation to create more diverse and realistic defect images.

## Dataset Notes

- AITEX AFID: 245 samples; the table describes 4096 x 256 grayscale images and segmentation masks.
- Lusitano: 33,684 samples; table reports 32k normal training images and a test split with 1,646 defect images and 1,038 normal images.
- ZJU-Leaper: table reports 2,000 samples, but this conflicts with the ZJU-Leaper paper and vault dataset note, which report a much larger dataset; treat the review table with caution.
- TILDA: 3,200 samples with seven defect classes, 768 x 512 8-bit grayscale TIF images.

## Limitations

- Stated: deep learning requires large, high-quality datasets and can overfit on smaller textile datasets.
- Inferred: some dataset table fields appear inconsistent or incomplete, so primary dataset notes should remain authoritative.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Methods: [[Data augmentation]], [[Synthetic data generation]], [[GAN]]
- Datasets: [[AITEX]], [[Lusitano]], [[TILDA]], [[ZJU-Leaper]]
- Domains: [[Textile and fiber inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art]] | Follow-up reading | Earlier fabric defect detection survey. |
| [[2025 - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry]] | Shares domain | Later YOLO-specific textile review. |

## Questions

- Which dataset table entries should be reconciled against primary dataset papers, especially ZJU-Leaper sample counts?
