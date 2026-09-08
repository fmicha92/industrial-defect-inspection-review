---
title: "Fabric Defect Detection in Textile Manufacturing: A Survey of the State of the Art"
aliases:
  - "Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art"
paper_key: "doi:10.1155/2021/9948808"
paper_type: review
year: 2021
venue: "Security and Communication Networks"
authors:
  - "Chao Li"
  - "Jun Li"
  - "Yafei Li"
  - "Lingmin He"
  - "Xiaokang Fu"
  - "Jingjing Chen"
status: processed
processed_at: 2026-05-31
topics:
  - "fabric defect detection survey"
  - "textile inspection"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "TILDA"
  - "KTH-TIPS"
methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
metrics: []
primary_metric: "not applicable"
doi: "10.1155/2021/9948808"
url: "https://doi.org/10.1155/2021/9948808"
pdf: "paper-inbox/10_processed/Review/2021 - Li - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art.pdf"
related_methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Review/2021 - Li - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Li - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Li - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art.txt"
artifact_status: "review"
tags:
  - paper
---

# Fabric Defect Detection in Textile Manufacturing: A Survey of the State of the Art

## Summary

This fabric-specific review covers statistical, spectral, structural, model-based, learning-based, and deep-learning methods for textile fabric defect detection. It is useful for dataset inventory because its tables mention TILDA, KTH-TIPS, Hong Kong patterned fabric data, and other collected or benchmark fabric datasets.

## Paper Type

- Type: review.
- Why: It surveys fabric defect detection methods rather than reporting a new experiment.

## Review / Survey Details

- Scope: automatic fabric defect detection in textile manufacturing.
- Inclusion criteria: literature retrieved using terms such as "Fabric defect detection," "textile inspection," "fabric defect recognition," and "automatic textile."
- Taxonomy: statistical, spectral, structural, model-based, learning-based, and deep-learning algorithms.
- Dataset relevance: tables mention TILDA, KTH-TIPS, benchmark databases, the fabric images database, yarn-dyed fabric data, Hong Kong patterned fabric data, and collected datasets.
- Synthesis relevance: the review notes GAN-based fabric image sample synthesis and the use of nondefect plus synthetic defective image data.

## Dataset Notes

- TILDA appears repeatedly in traditional and machine-learning fabric detection tables.
- KTH-TIPS appears with TILDA in spectral/traditional entries.
- Several deep-learning entries use collected datasets, synthetic and collected datasets, or benchmark/fabric-image databases rather than clearly public modern textile benchmarks.
- The review predates the public ZJU-Leaper paper and therefore does not cover it as a public textile benchmark.

## Limitations

- Stated: practical textile deployment faces small data, diversity, imbalance, complex textures, and real-time constraints.
- Inferred: dataset naming in the extracted tables is often incomplete, so primary papers must be checked before treating a dataset as public.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Datasets: TILDA, KTH-TIPS, Hong Kong patterned fabric data, benchmark fabric-image databases, and collected textile datasets
- Methods: [[GAN]], [[Data augmentation]], [[Synthetic data generation]]
- Domains: [[Textile and fiber inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] | Follow-up reading | Later textile review with a public dataset table including AITEX, Lusitano, and ZJU-Leaper. |
| [[2025 - YOLO Object Detection for Real-Time Fabric Defect Inspection in the Textile Industry]] | Follow-up reading | Later review focused on YOLO methods for fabric defect detection. |

## Questions

- Which named older textile datasets are still accessible and suitable for public-dataset synthesis experiments?
