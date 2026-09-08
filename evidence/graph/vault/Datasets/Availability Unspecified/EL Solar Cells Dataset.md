---
title: "EL Solar Cells Dataset"
aliases:
  - "EL Solar Cells"
  - "EL Solar Cells dataset"
related_domain: "[[Solar cells and photovoltaic]]"
introduced_by: "[[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]]"
related_papers:
  - "[[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]]"
related_tasks:
  - "[[Solar cell defect detection]]"
modalities:
  - "electroluminescence images"
dataset_sizes:
  - "10,500 training/validation images"
  - "6,000 unseen test images"
labels:
  - "bounding boxes"
  - "12 defect classes"
availability: "available on responsible request"
access: "request to corresponding author"
licenses:
  - "not reported"
---
# EL Solar Cells Dataset

## Summary

EL Solar Cells Dataset is the electroluminescence solar-cell defect dataset used by [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]]. The paper describes it as sourced from a manufacturing facility at Hebei University of Technology and Beihang University and annotated for 12 solar-cell defect classes.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Task: [[Solar cell defect detection]].
- Modality: electroluminescence solar-cell images.
- Training/validation size: 10,500 images.
- Class balance: 12 classes with 875 samples per class for training and validation.
- Test set: 500 samples per defect class, 6,000 unseen images total.
- Cell technologies: polycrystalline and monocrystalline silicon solar cells.
- Defect classes: line crack, star crack, finger interruption, black core, vertical dislocation, horizontal dislocation, thick line, scratch, fragment, corner, short circuit, and printing error.
- Annotation: colored bounding boxes are shown in the paper; the source describes the classes as annotated for object detection.
- Source institution: manufacturing facility at Hebei University of Technology and Beihang University.
- Availability: data available on responsible request to the corresponding author.
- License: not reported.

## Used In These Papers

- [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]] trains YOLOv10x on this dataset and reports 98.5% mAP@0.5.

## Source Anchors

- Introducing paper: [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]].
- Access statement: data available on responsible request to the corresponding author.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar cell defect detection]]
- [[mAP@0.50]]
