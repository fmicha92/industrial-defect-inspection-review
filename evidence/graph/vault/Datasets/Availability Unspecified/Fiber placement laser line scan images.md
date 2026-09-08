---
title: "Fiber placement laser line scan images"
aliases:
  - "Laser line scan sensor images from six fiber placement inspection cases"
availability: "not reported"
status: stable
concept_type: dataset
related_domain: "[[Aerospace and composite manufacturing]]"
url: "not reported"
data_sources: "not reported"
introduced_by: "not reported"
---
# Fiber placement laser line scan images

## Definition

Fiber placement laser line scan images are used in the processed AFP inspection paper note as the source images for defect classification and synthetic augmentation experiments. Availability: `not reported`.

## Why It Matters

They connect automated fiber placement inspection, DCGAN synthesis, and scarce-defect data augmentation.

## Dataset Details

- Sensor: AT C5-4090 laser line scan sensor.
- Acquisition setup: KUKA robot moving linearly over CFRP prepreg material.
- Raw scan format: 16-bit grayscale depth images with dimensions 4096 x 500 px.
- Sample coverage: about 250 x 150 mm.
- Scan velocity: 200 mm/s.
- Laser voltage: 5 V.
- Defect crop size: 128 x 128 px.
- Classes: no defect, wrinkle, twist, foreign body, overlap, and gap.
- Available images per class in the paper: no defect 86, wrinkle 49, twist 53, foreign body 22, overlap 166, gap 93.
- Availability: not reported; Python code is reported available on request.

## Used In These Papers

- [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] uses this dataset as reported in the processed paper note.
## Source Anchors

- Hosting source: not reported.
- Introducing paper: not reported.

## Related Concepts

- [[Automated fiber placement inspection]]
- [[Defect classification]]
- [[Aerospace and composite manufacturing]]
- [[Textile and fiber inspection]]
