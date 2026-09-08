---
title: "Logical anomalies"
aliases:
  - "logical anomaly"
status: emerging
concept_type: concept
candidate_parent: "Concepts/Anomaly Types"
source_papers:
  - "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
evidence_count: 1
---
# Logical anomalies

## Definition

Logical anomalies violate underlying logical or geometric constraints in otherwise permissible image content. Examples include a required object being absent, an object appearing in an invalid location, an incorrect object count, or an invalid pairing between two individually normal components.

## Why It Matters

Local patch descriptors can miss logical anomalies because each local part may look normal. Detecting them often requires modeling long-range relationships, object counts, positions, or globally consistent context.

## Used In These Papers

- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] defines logical anomalies, introduces [[MVTec LOCO AD]] to evaluate them, and proposes [[Global Context Anomaly Detection]] to improve their localization.

## Related Concepts

- [[Structural anomalies]]
- [[Industrial anomaly detection]]
- [[Defect segmentation]]
- [[Area Under Saturated Per-Region Overlap]]
