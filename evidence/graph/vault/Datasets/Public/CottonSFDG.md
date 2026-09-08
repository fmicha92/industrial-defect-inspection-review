---
title: "CottonSFDG"
aliases:
  - "CottonSFDG"
  - "Cotton-Fabric"
  - "Standard Fabric Defect Glossary"
  - "Cotton Incorporated fabric defect glossary"
related_domain: "[[Textile and fiber inspection]]"
url: "https://www.cottoninc.com/quality-products/textile-resources/fabric-defect-glossary"
data_sources:
  - "Cotton Incorporated"
access: "public web glossary"
licenses:
  - "not reported"
modalities:
  - "fabric defect images"
tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
introduced_by: "not reported"
related_papers:
  - "[[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]]"
---
# CottonSFDG

## Definition

CottonSFDG refers to fabric-defect imagery and labels sourced from Cotton Incorporated's Standard Fabric Defect Glossary. Defect Spectrum also labels the comparison source as Cotton-Fabric.

## Why It Matters

The source provides textile defect examples with defect names, fabric types, defect types, descriptions, severity labels, and category labels. Defect Spectrum uses it as a small fabric-defect source when comparing industrial defect datasets and constructing richer semantic annotations.

## Dataset Details

- Host: Cotton Incorporated Standard Fabric Defect Glossary.
- Dataset/source type: public web glossary with fabric-defect example images and structured defect metadata.
- Modality: fabric defect images.
- Labels/metadata: defect number, defect name, fabric type, defect type, description, severity, and category.
- Scale: Defect Spectrum reports 89 Cotton-Fabric images and 1 label in its comparison table.
- Pixel masks: Defect Spectrum reports that Cotton-Fabric originally lacked pixel-wise labels.
- Access: public web glossary.
- License: not reported in the checked source text.
- Introducing paper: not reported; Defect Spectrum cites the Cotton Incorporated glossary as reference [20].

## Used In These Papers

- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[CottonSFDG]] for industrial defect benchmark, semantic defect annotation.

## Source Anchors

- Hosting source: [Cotton Incorporated Standard Fabric Defect Glossary](https://www.cottoninc.com/quality-products/textile-resources/fabric-defect-glossary).
- Introducing paper: not reported.
- Related source: [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]].

## Related Concepts

- [[Textile and fiber inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
