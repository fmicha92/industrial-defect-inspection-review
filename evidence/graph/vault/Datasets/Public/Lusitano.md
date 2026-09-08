---
title: "Lusitano"
aliases:
  - "Lusitano dataset"
  - "Projeto Lusitano fabric defect dataset"
related_domain: "[[Textile and fiber inspection]]"
url: "https://kailashhambarde.github.io/Lusitano/"
data_sources: "kailashhambarde.github.io"
introduced_by: "[[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]"
---
# Lusitano

## Definition

Lusitano is a public fabric anomaly detection dataset introduced by [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]. It contains real factory textile images collected over three months from Paulo de Oliveira, S.A. in Covilha, Portugal.

## Why It Matters

Lusitano supports one-class [[Textile defect detection]]: training uses only normal fabric images, while testing includes normal and defective images. The paper emphasizes that the images are collected under factory conditions without artificial defect generation, augmentation, or post-processing.

## Used In These Papers

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] introduces Lusitano and evaluates [[RD4AD]] and [[DBFAD]] on it.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] evaluates [[STDAN]] on Lusitano and reports 96.74% AUC, 94.63% precision, 93.52% recall, and 94.07% F1-score.

## Dataset Details

- Domain: [[Textile and fiber inspection]].
- Task: [[Textile defect detection]], [[Industrial anomaly detection]].
- Image size: 4096 x 1024 before experiment cropping.
- Capture device: industrial-grade Teledyne Dalsa Linea camera.
- Collection period: January to March 2024.
- Training split: 32,000 normal images.
- Test split: 1038 normal images and 1646 defect images. The paper also summarizes the test split as about 1100 normal and 1300 defect images in some prose.
- Defects: real factory defects, not artificially generated.
- Synthetic data: none reported.
- Artifact: https://kailashhambarde.github.io/Lusitano/.
- License: article is CC BY; dataset license is not separately reported in the extracted text.

## Source Anchors

- Hosting source: https://kailashhambarde.github.io/Lusitano/.
- Introducing paper: [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]].

## Related Concepts

- [[Lusitano benchmark]]
- [[Textile defect detection]]
- [[Industrial anomaly detection]]
- [[Unsupervised anomaly detection]]
- [[Textile and fiber inspection]]
- [[ZJU-Leaper]]
- [[AITEX]]
