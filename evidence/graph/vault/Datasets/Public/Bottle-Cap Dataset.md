---
title: "Bottle-Cap Dataset"
aliases:
  - "Bottle-Cap Dataset"
  - "BottleCap"
  - "BC defects"
  - "Bottle-Cap"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://github.com/zhg-SZPT/MeDetection/tree/master/dataset/BC%20defects"
data_sources:
  - "GitHub"
access: "public GitHub repository dataset folder"
licenses:
  - "not reported"
modalities:
  - "industrial RGB inspection images"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
introduced_by: "[Adaptive visual detection of industrial product defects](https://doi.org/10.7717/peerj-cs.1264)"
related_papers:
  - "[Adaptive visual detection of industrial product defects](https://doi.org/10.7717/peerj-cs.1264)"
  - "[[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]]"
---
# Bottle-Cap Dataset

## Definition

Bottle-Cap Dataset is a public industrial vision inspection dataset of bottle-cap defects. The repository and introducing paper call the dataset "BC defects"; FEGAN refers to it as Bottle-Cap or BottleCap.

## Why It Matters

The dataset provides a focused single-product anomaly-detection setting for bottle-cap surface inspection, complementing broader multi-category industrial anomaly benchmarks.

## Dataset Details

- Host: `BC defects` folder in the public MeDetection GitHub repository.
- Dataset name in host repository: BC defects.
- Product scope: bottle caps from real production lines.
- Modality: high-resolution color images.
- Scale: FEGAN reports more than 1,100 high-resolution color images.
- Anomaly classes: FEGAN reports seven distinct real anomalies.
- Labels/annotations: the MeDetection README says the homemade BC defects dataset is placed in the dataset folder; FEGAN reports carefully labeled images for each part. Exact file-level annotation schema is not reported in the checked source text.
- Access: public GitHub repository dataset folder.
- License: not reported in the checked repository metadata.

## Used In These Papers

- [Adaptive visual detection of industrial product defects](https://doi.org/10.7717/peerj-cs.1264) introduces the BC defects dataset and reports releasing the dataset and code through MeDetection.
- [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]] uses or reports [[Bottle-Cap Dataset]] for GAN anomaly detection, feature extraction.

## Source Anchors

- Hosting source: [MeDetection BC defects folder](https://github.com/zhg-SZPT/MeDetection/tree/master/dataset/BC%20defects).
- Repository README: [MeDetection](https://github.com/zhg-SZPT/MeDetection).
- Introducing paper: [Adaptive visual detection of industrial product defects](https://doi.org/10.7717/peerj-cs.1264).
- Related source: [[2024 - FEGAN A Feature Extraction Based Approach for GAN Anomaly Detection and Localization]].

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
