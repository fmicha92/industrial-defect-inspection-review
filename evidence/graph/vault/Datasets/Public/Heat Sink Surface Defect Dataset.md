---
title: "Heat Sink Surface Defect Dataset"
aliases:
  - "Heat sink surface defect dataset"
  - "kaifengyang/heat-sink-surface-defect-dataset"
related_domain: "[[Semiconductor and electronics]]"
url: "https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset"
data_sources: "Kaggle"
introduced_by: "[[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]]"
license: "CC BY-NC-SA 4.0"
availability: "public"
tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
---
# Heat Sink Surface Defect Dataset

## Definition

Heat Sink Surface Defect Dataset is a public Kaggle dataset for segmentation of gold-plated tungsten-copper alloy heat sink surface defects. It contains 1000 annotated 320 x 320 images with background, scratch, and stain labels.

## Why It Matters

The dataset supports pixel-level inspection research where surface defects occupy a small part of each image. DatasetNinja reports that stains and scratches account for roughly 1.7% and 1.3% of all pixels, respectively, which makes class imbalance a central evaluation concern.

## Used In These Papers

- [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]] introduces the dataset and evaluates [[GSLU-Net]] on scratch and stain segmentation.

## Dataset Details

- Object/domain: gold-plated tungsten-copper alloy heat sink surfaces.
- Images: 1000.
- Resolution: 320 x 320 pixels.
- Labels: 0 background or defect-free area, 1 scratch area, and 2 stain area.
- Annotation: defect annotations for segmentation are reported.
- Source organization: State Key Laboratories of Transducer Technology, Institute of Semiconductors, Chinese Academy of Sciences.
- Creator/owner: Kaifeng Yang.
- Availability: public Kaggle dataset; Kaggle reports `isPrivate: false`.
- License: CC BY-NC-SA 4.0.
- Size: 664,789,672 bytes.
- Last updated: 2022-07-24.
- Splits: Kaggle metadata does not report train, validation, or test splits; DatasetNinja reports no predefined train/validation/test split.
- Secondary statistics from DatasetNinja: 7118 labeled objects, with 4953 stain-area objects and 2165 scratch-area objects.

## Source Anchors

- Hosting source: https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset.
- Dataset reference: `kaifengyang/heat-sink-surface-defect-dataset`.
- Mirror/statistics source: https://datasetninja.com/heat-sink-surface-defect-dataset.
- Citation requested by the dataset: [[2022 - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network]].

## Related Concepts

- [[Semiconductor and electronics]]
- [[Defect segmentation]]
- [[Surface defect detection]]
- [[GSLU-Net]]

## Questions

- The Kaggle metadata does not report the file layout or mask encoding.
- The Kaggle metadata does not report train, validation, or test splits.
- Whether the cited IEEE paper introduces the complete dataset or a subset needs paper-level processing.
