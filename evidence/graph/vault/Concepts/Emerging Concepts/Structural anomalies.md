---
title: "Structural anomalies"
aliases:
  - "structural anomaly"
status: emerging
concept_type: concept
candidate_parent: "Concepts/Anomaly Types"
source_papers:
  - "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
evidence_count: 1
---
# Structural anomalies

## Definition

Structural anomalies are new local visual structures that occur in confined regions and are absent from anomaly-free training data. Examples include scratches, dents, contaminations, broken parts, bent objects, and local color or texture defects.

## Why It Matters

Many industrial anomaly datasets primarily contain structural anomalies, which favors methods based on local visual descriptors. This can hide weaknesses on anomalies that require global context.

## Used In These Papers

- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] contrasts structural anomalies with [[Logical anomalies]] and reports separate localization results for both groups on [[MVTec LOCO AD]].

## Related Concepts

- [[Logical anomalies]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Defect segmentation]]
