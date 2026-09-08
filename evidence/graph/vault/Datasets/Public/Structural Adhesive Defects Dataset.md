---
title: "Structural Adhesive Defects Dataset"
aliases:
  - "GAN_Synth_Adhesive"
  - "GAN Structural Adhesive Dataset"
  - "Structural adhesive GAN dataset"
  - "Structural Adhesive Defects"
  - "adhesive1024"
availability: public
status: stable
concept_type: dataset
related_domain: "[[Automotive manufacturing]]"
url: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0"
repository_url: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive"
data_sources:
  - "GitHub release"
  - "Structural adhesive application cell at Introsys S.A."
licenses:
  - "not reported"
access: open
modalities:
  - image
tasks:
  - "[[Adhesive bead defect detection]]"
  - "[[Object detection]]"
methods:
  - "[[GAN]]"
  - "[[StyleGAN2]]"
  - "[[GAN-based surface defect augmentation]]"
introduced_by: "[[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]]"
related_papers:
  - "[[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]]"
host_verified_at: 2026-06-06
---
# Structural Adhesive Defects Dataset

## Definition

Structural Adhesive Defects Dataset is a public structural adhesive defect image release associated with [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]]. It is hosted in the `GAN_Synth_Adhesive` GitHub repository and contains real and synthetic adhesive bead defect images for GAN training and object detection experiments.

## Why It Matters

The dataset supports automotive adhesive bead defect detection under scarce and imbalanced real defect data. The release provides the real images used to train the GAN, the augmented object-detection training set, and real validation and holdout splits.

## Dataset Details

- Host: [GitHub release v1.0](https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0), named "Dataset Release - Published Version."
- Repository: [https://github.com/RicardoSPeres/GAN_Synth_Adhesive](https://github.com/RicardoSPeres/GAN_Synth_Adhesive).
- Release date: 2021-03-30.
- GAN training file: `adhesive1024.zip`, containing 143 real 1024 x 1024 images of structural adhesive defects.
- Object detection training file: `obj.zip`, containing 594 real and synthetic structural adhesive defect images for training.
- Validation file: `test.zip`, containing 58 real structural adhesive defect images for validation.
- Holdout file: `holdout.zip`, containing 18 real structural adhesive defect images for testing as the holdout set.
- Defect classes reported by the paper: discontinuity and blob/excess adhesive.
- Paper dataset construction: 143 cropped real images trained StyleGAN2-ADA, which generated 536 synthetic images; the 58-image real training set was augmented to 594 images for object detection.
- Labeling: object-detection images were manually annotated with LabelImg.
- License: not reported in the GitHub repository or release metadata checked on 2026-06-06.

## Used In These Papers

- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] trains StyleGAN2-ADA on real adhesive defect images, augments YOLOv4-Tiny object-detection training data with generated images, and reports improved mAP on validation and holdout sets.

## Source Anchors

- Dataset release: [https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0](https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0)
- Repository: [https://github.com/RicardoSPeres/GAN_Synth_Adhesive](https://github.com/RicardoSPeres/GAN_Synth_Adhesive)
- Introducing paper: [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]]
- Article DOI: [10.3390/app11073086](https://doi.org/10.3390/app11073086)

## Related Concepts

- [[Automotive manufacturing]]
- [[Adhesive bead defect detection]]
- [[Object detection]]
- [[Synthetic data generation]]
- [[GAN-based surface defect augmentation]]
- [[StyleGAN2]]
- [[YOLOv4]]
