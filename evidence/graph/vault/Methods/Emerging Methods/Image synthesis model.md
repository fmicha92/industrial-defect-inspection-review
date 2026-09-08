---
title: "Image synthesis model"
aliases:
  - "ISM"
  - "strip surface defect image synthesis model"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]]"
evidence_count: 1
---
# Image synthesis model

## Definition

The image synthesis model is a DCGAN-style generator for strip steel surface defect images. The linked paper modifies the discriminator loss so that generated false samples become more realistic, then uses generated samples to expand NEU-CLS training data.

## Why It Matters

It addresses the labeled-data shortage in steel surface defect classification. The linked paper reports improved NEU-CLS classification accuracy for several generated-data expansion settings.

## Used In These Papers

- [[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]] uses the image synthesis model to generate additional NEU-CLS samples for semi-supervised strip steel defect classification.

## Related Concepts

- [[DCGAN]]
- [[GAN]]
- [[Data augmentation]]
- [[Defect synthesis]]
- [[NEU-CLS]]
