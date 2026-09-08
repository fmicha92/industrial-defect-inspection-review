---
title: "Severstal Steel Defect Dataset"
aliases:
  - "Severstal Steel defect dataset"
  - "Severstal Steel"
availability: "public"
status: stable
concept_type: dataset
related_domain: "[[Metal inspection]]"
url: "https://www.kaggle.com/c/severstal-steel-defect-detection"
data_sources:
  - "Kaggle competition page"
introduced_by: "not reported"
related_papers:
  - "[[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]]"
  - "[[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]]"
  - "[[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]]"
---
# Severstal Steel Defect Dataset

## Definition

Severstal Steel Defect Dataset is a Kaggle-hosted steel surface-defect dataset for detecting and classifying defects in steel. The mixed-supervision paper reports 12,568 grayscale images in four defect classes.

## Why It Matters

It provides a larger, more diverse industrial metal-defect evaluation setting than DAGM, KolektorSDD, and KolektorSDD2 in the mixed-supervision study.

## Used In These Papers

- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] evaluates weak, mixed, and fully supervised learning on a subset that uses all negative images and positive images from the most common defect class.
- [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]] uses Severstal Steel Defect Detection as the real validation and comparison dataset for U-Net segmentation and Xception classification trained on synthetic steel defect renders.
- [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]] evaluates binary defect/no-defect classification and five-class defect classification with PAR-CNN, NRMI feature selection, and SVM.

## Dataset Details

- Images: 12,568 grayscale images.
- Classes: four defect classes.
- Samples reported by the synthetic-data paper: 7095 samples with four defect classes.
- Split reported by the synthetic-data paper: 80% training and 20% test for the real-data comparison.
- Evaluation subset in the mixed-supervision paper: all negative images plus positive images from class 3.
- Defect appearance: scratches, dents, excess material, and ambiguous defects.
- Host: [Severstal: Steel Defect Detection](https://www.kaggle.com/c/severstal-steel-defect-detection).
- Availability: public Kaggle competition data; dataset files can be downloaded from Kaggle.

## Source Anchors

- Hosting source: [Severstal: Steel Defect Detection](https://www.kaggle.com/c/severstal-steel-defect-detection), a Kaggle competition page with the description "Can you detect and classify defects in steel?"
- Introducing paper: not reported.
- Related paper: [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]].
- Related paper: [[2021 - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning]].
- Related paper: [[2023 - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach]].

## Related Concepts

- [[Metal inspection]]
- [[Surface defect detection]]
- [[Defect classification]]
- [[Defect segmentation]]
