---
title: "Image-mask aligned diffusion synthesis"
aliases:
  - "Alignment-regularized anomaly diffusion"
  - "Image-mask alignment regularization"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
source_papers:
  - "[[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]]"
evidence_count: 1
tags:
  - method
---

# Image-mask aligned diffusion synthesis

## Definition

Image-mask aligned diffusion synthesis trains a diffusion generator to model anomaly images and masks jointly so generated anomaly regions better align with their segmentation masks. The associated paper adds an Alignment Regularization loss between image and mask denoising branches and a Generative Feedback loss for downstream segmentation training.

## Why It Matters

Mask-guided anomaly generation can produce label drift when generated defects do not match their conditioning masks. Image-mask aligned diffusion synthesis directly targets that failure mode and uses the trained generator as both a synthetic-data source and an additional training signal for segmentation.

## Used In These Papers

- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] reports higher downstream segmentation mIoU than AnomalyDiffusion on [[MVTec AD]], [[Real-IAD]], and Floor Dirty, with the largest reported industrial gain on [[Real-IAD]].

## Related Concepts

- [[Diffusion models]]
- [[Defect synthesis]]
- [[Learned generative synthesis]]
- [[Synthetic data generation]]
- [[Defect segmentation]]

