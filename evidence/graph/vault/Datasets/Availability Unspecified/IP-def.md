---
title: "IP-def"
aliases:
  - "Insulation partition defect dataset"
related_domain: "[[Electrical power equipment inspection]]"
url: "not reported"
data_sources: "not publicly available; collected from production/sales manufacturers and power companies"
introduced_by: "[[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]]"
---
# IP-def

## Definition

IP-def is the insulation partition defect dataset used by the DG-GAN paper. It contains insulation partition defect images for scratches, pit points, ablation, and voltage breakdown.

## Why It Matters

It provides an electrical-power-equipment case study for DG-GAN pseudo-defect image generation and YOLOX defect detection.

## Used In These Papers

- [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] uses IP-def for defect image generation and downstream YOLOX detection.

## Dataset Details

- Size: 400 original defective images, 100 per defect type.
- Image size: 512 x 512 jpg images.
- Classes: scratches, pit points, ablation, and voltage breakdown.
- Generated expansion: DG-GAN generates 2000 defect images for the Fake2000 detection setting.
- Availability: paper data availability statement says the data cannot be disclosed.

## Source Anchors

- Hosting source: not reported.
- Introducing paper: [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]].

## Related Concepts

- [[Electrical power equipment inspection]]
- [[Surface defect detection]]
- [[DG-GAN]]
