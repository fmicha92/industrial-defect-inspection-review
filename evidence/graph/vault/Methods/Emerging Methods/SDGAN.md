---
title: "SDGAN"
aliases:
  - "SDGAN"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2020 - Defect Image Sample Generation With GAN for Improving Defect Recognition]]"
evidence_count: 1
tags:
  - emerging-method
---
# SDGAN

## Definition

SDGAN is a surface defect-generation adversarial network that generates defect images from defect-free industrial surface images using two generators, four discriminators, D2 adversarial loss, and cycle consistency loss.

## Why It Matters

It uses abundant defect-free production imagery to augment scarce defect samples, improving downstream anomaly recognition and defect classification.

## Used In These Papers


- [[2020 - Defect Image Sample Generation With GAN for Improving Defect Recognition]] uses [[SDGAN]] for defect image generation, GAN augmentation.

## Reported Results

- 1.77% error rate and 49.43% relative improvement for anomaly recognition on CCSD-NL.
- 0.74% error rate and 57.47% relative improvement for defect classification on CCSD-L.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
