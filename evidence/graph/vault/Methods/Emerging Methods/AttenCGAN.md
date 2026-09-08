---
title: "AttenCGAN"
aliases:
  - "AttenCGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]]"
evidence_count: 1
tags:
  - emerging-method
---
# AttenCGAN

## Definition

AttenCGAN is a CycleGAN-based defect image synthesis and attention-enhanced classification method for small-sample surface defect classification. It synthesizes pseudo defect images from few real defect samples and trains an Inception V3-based SDCNN with bilinear attention pooling plus attention-guided cropping and dropping augmentation.

## Why It Matters

It targets the common industrial setting where only a few defect images are available. The linked paper reports that AttenCGAN keeps higher classification accuracy than MobileNet-V2, ResNet-50, VGG16, and SDCNN without synthetic defect samples as the real defect sample count decreases.

## Used In These Papers


- [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] proposes AttenCGAN and reports 98.53% accuracy on [[KolektorSDD]] with eight defect samples and 99.57% average accuracy on [[DAGM2007]] classes 1-6 with forty defect samples.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[Defect classification]]
- [[FID]]
- [[Accuracy]]
