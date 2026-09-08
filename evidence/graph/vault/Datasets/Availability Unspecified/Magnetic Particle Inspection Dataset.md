---
title: "Magnetic Particle Inspection Dataset"
aliases:
  - "Magnetic Particle Inspection Dataset"
related_domain: "[[Metal inspection]]"
url: "not reported"
data_sources:
  - "DALSA Linea 2k 7.04 um 2048 x 2-26 kHz color line-scan camera"
  - "magnetic particle inspection apparatus at Erreka Fastening Solutions"
introduced_by: "[[2023 - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks]]"
---
# Magnetic Particle Inspection Dataset

## Definition

Magnetic Particle Inspection Dataset is a line-scan RGB fastener defect dataset collected from a magnetic particle inspection apparatus. It contains 1050 images, with 780 nondefective images and 270 defective images used to train [[Magna-Defect-GAN]].

## Why It Matters

It supports research on scarce-defect augmentation because the dataset includes mask annotations and guide labels for defect shape, location, number, thickness, brightness, and background. Those labels let a conditional generator synthesize defects with controlled intraclass variation.

## Used In These Papers


- [[2023 - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks]] introduces the dataset and uses it for GAN-based defect synthesis and binary defect classification.

## Dataset Details

- Domain: [[Metal inspection]].
- Task: [[Surface defect detection]], [[Defect classification]].
- Images: 1050 RGB line-scan images.
- Training composition reported for GAN training: 780 nondefective and 270 defective images.
- Acquisition: DALSA Linea 2k 7.04 um 2048 x 2-26 kHz color line-scan camera with 12 mm fixed focal length lens and 600 mm field of view.
- Source setting: magnetic particle inspection apparatus at Erreka Fastening Solutions.
- Annotations: ground-truth masks plus guide labels from experienced quality engineers.
- Availability: available upon request from the corresponding author.
- License: not reported.

## Source Anchors

- Hosting source: not reported.
- Introducing paper: [[2023 - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks]].
- Dataset access: available upon request from the corresponding author.

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Defect classification]]
- [[Data augmentation]]
