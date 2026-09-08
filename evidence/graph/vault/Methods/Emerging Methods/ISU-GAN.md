---
title: "ISU-GAN"
aliases:
  - "Involution-SE-U GAN"
  - "Involution-SE-U-shaped GAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2022 - Using ISU-GAN for unsupervised small sample defect detection]]"
evidence_count: 1
tags:
  - method
---

# ISU-GAN

## Definition

ISU-GAN is an unsupervised small-sample defect detection model based on CycleGAN. Its generator adds skip connections, an SE module, and an Involution module to strengthen defect feature extraction and repair defective regions into defect-free reconstructions.

## Why It Matters

The method targets industrial settings where defect examples and labels are scarce. It uses positive and negative samples in an unsupervised GAN framework and extracts defect contours with an SSIM-based difference method.

## Used In These Papers

- [[2022 - Using ISU-GAN for unsupervised small sample defect detection]]: evaluates ISU-GAN on selected DAGM2007 classes and reports higher accuracy and F1-score than UNet, ResUNet++, CycleGAN, and DCGAN comparisons.

## Related Concepts

- [[GAN]]
- [[Unsupervised anomaly detection]]
- [[Defect segmentation]]
- [[DAGM2007]]
- [[SSIM]]
