---
title: "Defect Transfer GAN"
aliases:
  - "Defect Transfer GAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]]"
  - "[[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]]"
evidence_count: 2
tags:
  - emerging-method
---
# Defect Transfer GAN

## Definition

Defect Transfer GAN is a GAN-based defect synthesis method that disentangles foreground defect shape and style from background product information. It generates diverse defective images by transferring defect characteristics across products while preserving the chosen background.

## Why It Matters

It supports semantic data augmentation for automated visual inspection when defective samples are scarce. The source paper reports downstream classifier error-rate reductions when DT-GAN synthetic images are added to traditional augmentation.

## Used In These Papers


- [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] proposes DT-GAN and reports improved defect-classification error rates on an industrial SDI dataset, including Product A error reduction from 13.81% with traditional augmentation to 6.72% with DT-GAN synthetic data.
- [[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]] uses DefectTransfer for scarce fabric defect classification on [[ZJU-Leaper]] and [[LaceCls]], combining cut-paste defect synthesis with adversarial transformations.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Small-sample defect classification]]
- [[FID]]
- [[LPIPS]]
