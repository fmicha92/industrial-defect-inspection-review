---
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
aliases:
  - "Strong Identity GAN"
  - "strong identity GAN"
source_papers:
  - "[[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]]"
evidence_count: 1
---
# SIGAN

## Definition

SIGAN is a GAN-based image translation method for solar-cell electroluminescence defect segmentation and augmentation. It uses adversarial loss, cycle-consistency loss, and strong identity loss to translate between defective and defect-free image domains while preserving the non-defect background.

## Why It Matters

SIGAN supports defect segmentation by generating a defect-free version of a defective EL patch and subtracting it from the original image. It also supports augmentation by generating crack and finger-interruption defect images from defect-free patches.

## Used In These Papers

- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] - introduces SIGAN for EL-2019 segmentation and augmentation, reporting 90.34% total segmentation F-score and improved classifier F-measure after generated-image augmentation.

## Related Concepts

- [[GAN]]
- [[Defect synthesis]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[EL-2019]]
