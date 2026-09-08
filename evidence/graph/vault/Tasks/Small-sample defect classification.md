---
title: "Small-sample defect classification"
aliases:
  - "few-sample defect classification"
tags:
  - task
---
# Small-sample defect classification

## Definition

Small-sample defect classification assigns defect or normal labels when only a few labeled defect examples are available for training.

## Why It Matters

Industrial inspection often has many normal examples but few defect examples, so classification models can overfit or fail to learn discriminative defect regions without augmentation, transfer learning, or other scarce-data methods.

## Used In These Papers

- [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] uses [[AttenCGAN]] to synthesize pseudo defect samples and train an attention-enhanced classifier from one to eight defect samples on [[KolektorSDD]] and one to forty defect samples on [[DAGM2007]].

## Related Concepts

- [[Defect classification]]
- [[Surface defect detection]]
- [[Data augmentation]]
- [[GAN]]
