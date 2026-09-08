---
title: "Mobile Phone Flat Glass Defect Dataset"
aliases:
  - "Mobile phone flat glass dataset"
  - "Cell phone flat glass defect dataset"
tags:
  - dataset
  - availability-unspecified
domain: "[[Glass inspection]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
related_papers:
  - "[[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]]"
modalities:
  - "visible-light industrial images"
labels:
  - "bright spot"
  - "scratch"
  - "dust"
  - "stain"
availability: "available on request"
license: "not reported"
url: "not reported"
---

# Mobile Phone Flat Glass Defect Dataset

## Summary

The dataset contains mobile phone flat-glass defect images collected from a manufacturing enterprise using a custom automatic optical inspection platform with total-reflection and grazing-incidence illumination.

## Dataset Details

- Source: mobile phone flat glass samples from a manufacturing enterprise.
- Acquisition: custom inspection platform with two CMOS industrial cameras, a main total-reflection light source, an auxiliary grazing-incidence light source, motion/control components, and image acquisition hardware.
- Defect classes: bright spot, scratch, dust, and stain.
- Training data: 1000 collected defect images plus generated samples from segmented defect fusion; 800 clean background images were added to simulate the real environment, yielding 1600 training images with 2400 point, slice, dust, and dirt defects.
- Validation data: 200 images with 300 point, slice, dust, and dirt defects.
- Test data: 200 non-synthetic unlabeled original images with 300 point, slice, dust, and dirt defects.
- Image size for model input: 480 x 480.
- Availability: raw data supporting the paper's conclusions will be made available by the authors on request.

## Used In These Papers

- [[2024 - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting]] uses the dataset to evaluate [[YOLOv5_zc]] for four-class defect detection on mobile phone flat glass.

## Related Concepts

- [[Smartphone screen glass defect detection]]
- [[Glass inspection]]
- [[Surface defect detection]]
- [[Total reflection grazing incidence combined lighting]]
- [[Poisson defect image augmentation]]
