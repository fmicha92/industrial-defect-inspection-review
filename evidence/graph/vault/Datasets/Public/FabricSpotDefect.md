---
title: FabricSpotDefect
aliases:
  - FabricSpotDefect dataset
  - "FabricSpotDefect: An Annotated Dataset for Identifying Spot Defects in Different Fabric Types"
related_domain: "[[Textile and fiber inspection]]"
url: https://data.mendeley.com/datasets/6574nhzm8x/1
data_sources: Mendeley Data
introduced_by: "[[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]]"
---
# FabricSpotDefect

## Definition

FabricSpotDefect is a public fabric spot-defect dataset introduced by [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]]. It contains RGB images of daily-use fabrics with spot defects annotated as a single class, `Spot`.

## Why It Matters

The dataset supports [[Textile defect detection]] and [[Defect segmentation]] experiments where spot defects appear on varied fabrics, including patterned and colorful textiles. It provides both COCO and YOLOv8 annotation exports for object detection or localization workflows.

## Used In These Papers

- [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]] introduces FabricSpotDefect, describes image capture and RoboFlow annotation, and reports the train/validation/test splits.
- [[2026 - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection]] evaluates [[STDAN]] on FabricSpotDefect and reports 98.21% AUC, 96.84% precision, 95.73% recall, and 96.28% F1-score.

## Dataset Details

- Domain: [[Textile and fiber inspection]].
- Task: [[Textile defect detection]], [[Defect segmentation]].
- Source location: Independent University Bangladesh, Dhaka, Bangladesh.
- Image modality: 2D RGB JPG images.
- Original images: 1014 raw images.
- Original annotations: 3288 spot annotations.
- Augmented images: 2300 additional augmented images.
- Augmented annotations: 7641 YOLOv8 annotations and 7635 COCO annotations.
- Classes: one class, `Spot`.
- Defect examples: stains, discolorations, oil marks, rust, blood marks, paint spots, marker spots, makeup stains, glue spots, detergent stains, coffee stains, food spots, and sweat stains.
- Fabric examples: cotton, linen, silk, denim, patterned textiles, and jacquard fabrics.
- Image size after preprocessing: 416 x 416 pixels.
- Annotation types: bounding boxes and polygons.
- Splits: original images use 643 train, 219 validation, and 152 test images; augmented train set has 1929 images while validation and test counts remain 219 and 152.
- Artifact: https://data.mendeley.com/datasets/6574nhzm8x/1.
- Dataset DOI: 10.17632/6574nhzm8x.1.
- License: article is CC BY; dataset-specific license is not separately reported in the extracted text.

## Source Anchors

- Hosting source: https://data.mendeley.com/datasets/6574nhzm8x/1.
- Introducing paper: [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]].

## Related Concepts

- [[Textile defect detection]]
- [[Defect segmentation]]
- [[Textile and fiber inspection]]
- [[Industrial visual inspection]]
- [[Data augmentation]]
- [[Batavia and Sarga woven fabric images]]
- [[Lusitano]]
- [[ZJU-Leaper]]
- [[AITEX]]
