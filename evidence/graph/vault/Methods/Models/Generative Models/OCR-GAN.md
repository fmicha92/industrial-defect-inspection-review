---
title: "OCR-GAN"
aliases:
  - "OCR-GAN"
  - "Omni-Frequency Channel-Selection Reconstruction"
  - "Omni-frequency Channel-selection Reconstruction"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Generative Models"
source_papers:
  - "[[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---

# OCR-GAN

## Definition

OCR-GAN is an omni-frequency channel-selection reconstruction network for unsupervised anomaly detection. It decouples an input image into frequency-specific images, reconstructs those components with parallel GAN generators, and uses channel selection to exchange information among frequency-specific encoders.

## Why It Matters

OCR-GAN targets sensory anomaly detection without pretrained feature extractors or extra training data. Its frequency-decoupling and channel-selection modules improve reconstruction-based anomaly scoring on MVTec AD, DAGM, and KolektorSDD by making abnormal regions harder to reconstruct than normal image structure.

## Used In These Papers

- [[2023 - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection]] introduces OCR-GAN, trains it from scratch on normal samples with CutPaste/CutOut forged abnormal samples for discriminator training, and reports 98.3 AU-ROC on [[MVTec AD]].

## Related Concepts

- [[Unsupervised anomaly detection]]
- [[MVTec AD]]
- [[DAGM2007]]
- [[KolektorSDD]]
- [[AU-ROC]]
- [[Adam]]
