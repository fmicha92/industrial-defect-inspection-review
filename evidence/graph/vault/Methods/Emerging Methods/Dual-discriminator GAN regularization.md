---
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
aliases:
  - "dual discriminator GAN"
  - "dual-discriminator GAN"
  - "GAN with dual discriminators and regularization"
source_papers:
  - "[[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]]"
evidence_count: 1
---
# Dual-discriminator GAN regularization

## Definition

Dual-discriminator GAN regularization uses two discriminators with different regularization roles to train a GAN under limited surface-defect data. In the source paper, D1 is regularized to reduce overfitting to scarce real images, while D2 is regularized to remain sensitive to generated images and discourage low-diversity generator outputs.

## Why It Matters

Limited industrial defect datasets can cause discriminator overfitting and unstable GAN training. The dual-discriminator scheme is designed to keep generated defect images realistic and diverse enough to improve downstream defect detectors.

## Used In These Papers

- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] - introduces the method and reports improved FID/SDS generation metrics plus YOLO-v5 and YOLO-v8 mAP gains after generated-image augmentation.

## Related Concepts

- [[GAN]]
- [[GAN-based surface defect augmentation]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Surface Defect Score]]
