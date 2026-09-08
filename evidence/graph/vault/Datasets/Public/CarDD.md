---
title: "CarDD"
aliases:
  - "Car Damage Detection"
  - "CarDD dataset"
  - "Car Damage Detection dataset"
related_domain: "[[Automotive damage assessment]]"
url: "https://cardd-ustc.github.io/"
dataset_download_url: "https://drive.google.com/file/d/1bbyqVCKZX5Ur5Zg-uKj0jD0maWAVeOLx/view?usp=sharing"
data_sources:
  - "CarDD project site"
  - "Google Drive"
  - "GitHub"
introduced_by: "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
related_papers:
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
  - "[[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]]"
related_tasks:
  - "[[Car damage detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Salient object detection]]"
  - "[[Cross-domain few-shot object detection]]"
licenses:
  - "PIC Lab license; prior consent required"
access: "public Google Drive file is listed on the project site; license form asks users to request/obtain access before use"
availability: public
host_verified_at: 2026-06-09
---
# CarDD

## Definition

CarDD is a vision-based car damage dataset for damage classification, object detection, instance segmentation, and salient object detection.

## Why It Matters

CarDD supports [[Car damage detection]] with high-resolution vehicle-damage images, instance annotations, and pixel-level masks for car-insurance damage assessment workflows.

## Used In These Papers

- [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]] introduces CarDD and evaluates state-of-the-art methods for car damage detection, instance segmentation, and salient object detection.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses CarDD as a cross-domain few-shot object detection target dataset and reports gains from Qwen-based generative augmentation.

## Dataset Details

- Domain: [[Automotive damage assessment]].
- Tasks: [[Car damage detection]], [[Defect classification]], [[Defect segmentation]].
- Image count: 4,000 high-resolution car damage images.
- Labeled instances: over 9,000 annotated damage instances.
- Damage categories: dent, scratch, crack, glass shatter, tire flat, and lamp broken.
- Annotation types: damage type labels, damage locations, COCO-style bounding boxes and polygon masks for object detection and instance segmentation, and binary maps for salient object detection.
- Split: 2,816 training images, 810 validation images, and 374 test images.
- Raw image sources: Flickr and Shutterstock.
- Average resolution: 684,231 pixels.
- Object-size distribution: 38.6% small, 32.6% medium, and 28.8% large instances.
- Dataset access: the project site exposes a Google Drive dataset link; a 2026-06-09 host check reached a Google Drive virus-scan warning page for `CarDD_release.zip` with reported size 5.6 GB.
- Access caveat: the project site also instructs users to first fill in the licensing form and send it to the authors to get the link.
- License terms: statistical and scientific research use is allowed after prior consent; commercial use, redistribution, and transfer require authorization from PIC Lab.
- Project artifacts: paper PDF, Google Drive dataset link, GitHub code/project repository, and licensing form.

## Source Anchors

- Project site: https://cardd-ustc.github.io/.
- Dataset download link: https://drive.google.com/file/d/1bbyqVCKZX5Ur5Zg-uKj0jD0maWAVeOLx/view?usp=sharing.
- Host audit: Google Drive presented `CarDD_release.zip` as a 5.6 GB file on 2026-06-09.
- Code/project repository: https://github.com/CarDD-USTC/CarDD-USTC.github.io.
- Licensing form: https://cardd-ustc.github.io/docs/CarDD_license.pdf.
- Introducing paper: [[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]].

## Related Concepts

- [[Automotive damage assessment]]
- [[Car damage detection]]
- [[Defect classification]]
- [[Defect segmentation]]
- [[Salient object detection]]
- [[Cross-domain few-shot object detection]]
- [[Qwen-Image generative augmentation]]
- [[Industrial visual inspection]]
