---
title: "Bosch Surface Defect Inspection Dataset"
aliases:
  - "Bosch Surface Defect Inspection Dataset"
  - "Bosch industrial dataset"
  - "Surface Defect Inspection"
  - "SDI"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset"
data_sources:
  - "https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset"
  - "https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset/blob/main/SDI_DATASET_v1.zip"
introduced_by: "[[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]]"
related_papers:
  - "[[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]]"
access: "public archived GitHub repository with SDI_DATASET_v1.zip"
licenses:
  - "CC-BY-SA-4.0"
modalities:
  - "industrial surface inspection images"
tasks:
  - "[[Defect classification]]"
  - "[[Industrial anomaly detection]]"
---
# Bosch Surface Defect Inspection Dataset

## Definition

Bosch Surface Defect Inspection Dataset, also called Surface Defect Inspection (SDI), is a public Bosch Research industrial surface-inspection image dataset released with the DT-GAN paper. The dataset contains 20,414 images at varied resolutions across three anonymous product types, Product A, Product B, and Product C, labeled into Normal, Scratches, and Spots foreground defect domains.

## Dataset Details

- Host: archived public Bosch Research GitHub repository `The-Surface-Defect-Inspection-Dataset`.
- Dataset archive: `SDI_DATASET_v1.zip`.
- Scope: three industrial product surfaces, anonymized as Product A, Product B, and Product C.
- Labels: each image is labeled by defect type; the dataset PDF groups labels into Normal, Scratches, and Spots.
- Full distribution: Product A has 6,250 Normal, 340 Scratches, and 108 Spots images; Product B has 6,250 Normal, 167 Scratches, and 670 Spots images; Product C has 6,250 Normal, 121 Scratches, and 258 Spots images.
- Split policy: for each foreground defect and background product, 50 images are randomly selected; 30% are used for validation and 70% for test, and all remaining images are used for GAN and classifier training.
- DT-GAN training subset: Product A uses 700 Normal, 290 Scratches, and 58 Spots images; Product B uses 700 Normal, 117 Scratches, and 620 Spots images; Product C uses 700 Normal, 71 Scratches, and 208 Spots images.
- Classifier training: the normal-image count is varied incrementally at 1,500, 2,200, 4,000, and 6,200 while the defect counts follow the training split.
- Access: public GitHub repository, archived read-only on 2026-02-19.
- License: CC-BY-SA-4.0.

## Why It Matters

The dataset provides the downstream manufacturing defect-classification setting where DT-GAN synthetic images are tested as data augmentation, and it exposes the small-defect, class-imbalanced regime typical of production-line surface inspection.

## Used In These Papers

- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] introduces SDI, uses it for image synthesis and downstream ResNet-50 defect classification, and reports DT-GAN error-rate improvements over traditional augmentation on products A, B, and C.

## Source Anchors

- Hosting source: https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset.
- Dataset archive: https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset/blob/main/SDI_DATASET_v1.zip.
- Dataset details PDF: https://github.com/boschresearch/The-Surface-Defect-Inspection-Dataset/blob/main/DT_GAN_BMVC_SDI_dataset.pdf.
- Introducing paper: [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]].

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
