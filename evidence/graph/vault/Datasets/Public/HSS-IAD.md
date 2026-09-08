---
title: "HSS-IAD"
aliases:
  - "HSS-IAD"
availability: "public"
status: stable
concept_type: dataset
related_domain: "[[Metal inspection]]"
url: "https://github.com/Qiqigeww/HSS-IAD-Dataset"
data_sources:
  - "GitHub"
  - "Google Drive"
introduced_by: "[[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]]"
---
# HSS-IAD

## Definition

HSS-IAD is a heterogeneous same-sort industrial anomaly detection dataset of metallic-like industrial parts. It contains 8,580 images with precise anomaly annotations.

## Why It Matters

HSS-IAD targets subtle defects that closely resemble the base materials, including defects that can be confused with machining marks, oil stains, machining residues, and process features. It provides a public benchmark for industrial anomaly detection under class-separated and multi-class settings.

## Used In These Papers

- [[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]] supports heterogeneous same-sort anomaly detection, dataset.

## Dataset Details

- Host: [HSS-IAD-Dataset](https://github.com/Qiqigeww/HSS-IAD-Dataset).
- Download: public image data are linked from the host page through Google Drive.
- Size: 8,580 images.
- Objects/materials: metallic-like industrial parts.
- Categories: seven categories, described by the paper as multiple metallic-like categories; the host page names three object categories, Casting_C1, Casting_C2, and Casting_C3, and four texture categories, KolektorSDD, KolektorSDD2, Magnetic-tile-defect, and STEEL.
- Annotations: precise anomaly annotations.
- Additional files: foreground images for synthetic anomaly generation.
- Anomalous pixel ratio: 3.0% in the introducing paper.
- Evaluation settings: class-separated and multi-class industrial anomaly detection.
- License: not reported.

## Source Anchors

- Hosting source: https://github.com/Qiqigeww/HSS-IAD-Dataset.
- Introducing paper: [[2025 - HSS-IAD A Heterogeneous Same-Sort Industrial Anomaly Detection Dataset]].

## Related Concepts

- [[Metal inspection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
