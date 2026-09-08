---
title: "LaceCls"
aliases:
  - "LaceCls dataset"
related_domain: "[[Textile and fiber inspection]]"
availability: "not reported"
introduced_by: "[[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]]"
related_papers:
  - "[[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]]"
tags:
  - dataset
---

# LaceCls

## Definition

LaceCls is an author-collected lace fabric defect classification dataset used to evaluate scarce-defect data augmentation for production-line textile inspection.

## Why It Matters

The dataset stresses augmentation under an extreme class-imbalance setting: the reported training split contains many defect-free examples but only ten defect images.

## Dataset Details

- Domain: [[Textile and fiber inspection]].
- Task: [[Defect classification]] for lace fabric images.
- Size: 6,610 lace production-line images.
- Training split: 4,800 defect-free images and 10 defect images.
- Test split: 900 defect-free images and 900 defect images.
- Defect classes: one defect class is reported for LaceCls.
- Annotation: image-level defective versus defect-free labels are used for classification; mask availability is discussed for DefectTransfer variants.
- Availability: not reported.

## Used In These Papers

- [[2022 - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data]] uses LaceCls to test DefectTransfer under heterogeneous production-line texture conditions. Table III reports that ResNet101 with no augmentation at the 10% defect-image setting obtains 50.00% accuracy and 0.00% F1-score, while ResNet101 with DefectTransfer obtains 94.44% accuracy and 94.33% F1-score. The 100% DefectTransfer setting reaches 96.56% accuracy and 96.45% F1-score.

## Related Concepts

- [[Textile and fiber inspection]]
- [[Textile defect detection]]
- [[Defect classification]]
- [[Data augmentation]]
