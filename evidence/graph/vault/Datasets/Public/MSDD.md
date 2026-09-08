---
title: "MSDD"
aliases:
  - "Metal Surface Defect Dataset"
  - "MSDD"
  - "Photometric stereo complex structured parts dataset"
  - "Complex structured parts surface defect dataset"
related_domain: "[[Metal inspection]]"
url: "https://doi.org/10.57760/sciencedb.10794"
host_url: "https://www.scidb.cn/en/detail?dataSetId=3d739ddb4bdc439a9bf7ef550cae48d8"
data_sources: "ScienceDB"
license: "Creative Commons Attribution 4.0 International"
introduced_by: "[[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]]"
---
# MSDD

## Definition

MSDD, the Metal Surface Defect Dataset, is a public casting-metal surface defect dataset built with multi-angle stroboscopic illumination and photometric-stereo-derived pseudo-color images.

## Why It Matters

It targets [[Casting surface defect detection]] on non-planar metal parts where shadows, stains, surface reflectivity, and complex geometry make ordinary static 2D illumination unreliable.

## Used In These Papers

- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] introduces MSDD and validates FCOS, YOLOv5, YOLOv8, and RT-DETR on its mixed pseudo-color images.

## Dataset Details

- Source: ScienceDB / Science Data Bank.
- Access: public.
- License: Creative Commons Attribution 4.0 International, as reported by the ScienceDB structured metadata.
- Data volume: 138,585 single-channel images and 9,239 mixed RGB pseudo-color images.
- Image composition: 5,746 defect-free mixed images and 3,493 images containing defects, according to the ScienceDB description.
- Paper-reported annotated images: 9,332 annotated images.
- Collection: 1,507 defective metal parts imaged under multiple lighting conditions by six cameras.
- Image size: 640 x 640 patches after sliding-window preprocessing with 15% overlap; high-resolution acquisition used cameras up to 2560 x 1920 pixels.
- Defect types: Misrun, Inclusion, Dent, Parting line crack, Stamp collapse, Pockmarks, Mould scuffing, and Cut marks.
- Annotation format: VOC annotation files with filename, dimensions, category, and bounding-box location.
- Annotation protocol: two professionally trained inspectors independently annotated defects; annotations with IoU above 0.8 were averaged, and disagreements were reviewed by a quality supervisor.
- Split used in technical validation: 4:1 training/testing split.
- Benchmark models: FCOS, YOLOv5, YOLOv8, and RT-DETR.

## Source Anchors

- Hosting source: https://doi.org/10.57760/sciencedb.10794.
- ScienceDB detail page: https://www.scidb.cn/en/detail?dataSetId=3d739ddb4bdc439a9bf7ef550cae48d8.
- Introducing paper: [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]].

## Related Concepts

- [[Metal inspection]]
- [[Photometric stereo]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Casting surface defect detection]]
