---
title: "Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects: A Survey"
aliases:
  - "Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects A Survey"
paper_key: "doi:10.1109/access.2023.3271748"
paper_type: review
year: 2023
venue: "IEEE Access"
authors:
  - "Michela Prunella"
  - "Roberto Maria Scardigno"
  - "Domenico Buongiorno"
  - "Antonio Brunetti"
  - "Nicola Longo"
  - "Raffaele Carli"
  - "Mariagrazia Dotoli"
  - "Vitoantonio Bevilacqua"
status: processed
processed_at: 2026-05-31
topics:
  - "industrial surface defect survey"
  - "deep learning defect recognition"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Textile and fiber inspection]]"
methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
metrics: []
primary_metric: "not applicable"
doi: "10.1109/access.2023.3271748"
url: "https://doi.org/10.1109/ACCESS.2023.3271748"
pdf: "paper-inbox/10_processed/Review/2023 - Prunella - Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects A Survey.pdf"
related_methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Review/2023 - Prunella - Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects A Survey.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Prunella - Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects A Survey.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Prunella - Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects A Survey.txt"
artifact_status: "review"
tags:
  - paper
---

# Deep Learning for Automatic Vision-Based Recognition of Industrial Surface Defects: A Survey

## Summary

This survey reviews more than 220 deep-learning papers on industrial surface defect recognition, organized by recognition task and learning paradigm. For the textile-dataset question, its most useful evidence is its discussion of dataset imbalance and the role of data augmentation and GAN-generated defect samples in defect classification, detection, and segmentation.

## Paper Type

- Type: review.
- Why: It summarizes existing industrial surface defect literature rather than running new experiments.

## Review / Survey Details

- Scope: deep-learning vision methods for industrial surface defect classification, detection, and segmentation.
- Inclusion criteria: articles published until February 2023; exact screening rules are not fully extracted.
- Taxonomy: task type, supervision level, architecture, dataset, and industrial scenario.
- Textile relevance: the survey covers fabric and textile manufacturing among industrial scenarios and cites fabric-specific surveys.
- Dataset relevance: public defect datasets are discussed in tables, but this source does not itself benchmark textile datasets.
- Synthesis relevance: the survey identifies data augmentation and GAN-generated defective samples as responses to class imbalance and small datasets.

## Methodological Patterns

- Small or imbalanced defect datasets are common in industrial inspection.
- The survey describes three augmentation families: geometric transformations, stochastic/lighting changes, and generative methods such as GANs.
- It notes that augmentation is valuable only when new features improve inspection, not just when sample count increases.

## Limitations

- Stated: industrial defect recognition still struggles with imbalance, scarce labels, multi-scale defects, real-time constraints, and physical interpretability.
- Inferred: because it is broad, it should be used to locate primary textile studies rather than as evidence of textile dataset performance.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect classification]], [[Defect segmentation]]
- Datasets: public and custom industrial surface-defect datasets summarized in survey tables
- Methods: [[GAN]], [[Data augmentation]], [[Synthetic data generation]]
- Domains: [[Multi-industry anomaly detection]], [[Textile and fiber inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - A Survey of Defect Detection Applications Based on Generative Adversarial Networks]] | Shares method | Both reviews synthesize GAN and augmentation use in defect detection. |
| [[2021 - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art]] | Shares domain | The fabric-specific survey narrows this paper's broad industrial scope to textiles. |

## Questions

- Which primary papers in its tables use public textile datasets and report synthetic-data gains?
