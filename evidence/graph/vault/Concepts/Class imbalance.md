---
title: "Class imbalance"
aliases:
  - "Imbalanced datasets"
  - "Class-imbalanced learning"
tags:
  - concept
---

# Class Imbalance

## Definition

Class imbalance occurs when one label or outcome class has substantially fewer examples than another, causing models to favor majority-class predictions unless training or evaluation is adjusted.

## Why It Matters

Industrial defect datasets often contain many normal samples and few defective samples. This can make high overall accuracy misleading if the model misses rare defects.

## Used In These Papers

- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] uses DDPM-generated defective glass bottle images to reduce imbalance in the MVTec AD bottle subset from about 3:1 to 1.7:1.
- [[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]] addresses 2281 normal versus 28 defective real thermal samples with physics-guided defect synthesis.
- [[2020 - Infrared Solar Module Dataset for Anomaly Detection]] highlights class imbalance in solar PV anomaly detection and reports 10,000 no-anomaly samples versus smaller anomaly classes such as 175 Diode-Multi images.

## Related Concepts

- [[Data augmentation]]
- [[Defect classification]]
- [[Recall]]
- [[Industrial visual inspection]]
- [[Solar module anomaly classification]]
