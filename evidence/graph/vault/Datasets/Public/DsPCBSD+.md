---
title: "DsPCBSD+"
aliases:
  - "DsPCBSD+"
related_domain: "[[Semiconductor and electronics]]"
url: "https://doi.org/10.6084/m9.figshare.24970329"
doi: "10.6084/m9.figshare.24970329"
data_sources: "Figshare"
introduced_by: "[[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]]"
license: "CC BY 4.0"
modalities:
  - "image"
tasks:
  - "[[PCB defect detection]]"
  - "[[Object detection]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[mAP@0.50-0.95]]"
---
# DsPCBSD+

## Definition

DsPCBSD+ is a public PCB surface-defect object-detection dataset with manually annotated bounding boxes, built from actual inner- and outer-layer PCB defects after etching.

## Why It Matters

DsPCBSD+ gives PCB inspection work a larger public benchmark with real production defects, nine category labels, YOLO and COCO formats, and validation results from Co-DETR and YOLOv6-L6.

## Used In These Papers

- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] introduces DsPCBSD+ and validates it with [[Co-DETR]] and [[YOLOv6-L6]].

## Dataset Details

- Hosting source: [Figshare dataset DOI](https://doi.org/10.6084/m9.figshare.24970329).
- Figshare title: DsPCBSD+.
- Creator: Shengping Lv.
- Publication date: 2024-06-08.
- Access: public Figshare dataset; downloads are not disabled in the Figshare metadata.
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- File: `DsPCBSD+.zip`.
- File size: 128,541,608 bytes.
- Dataset scope: PCB surface-defect object detection for deep-learning AOI.
- Collection source: AGLE'OL AOI-100 V8 equipment in the Guangzhou FastPrint Technology Co., Ltd. workshop.
- Acquisition: controllable LED spotlight illumination and 16K line-scan imaging with four top cameras and four bottom cameras.
- Source pool: 32,259 JPG images, each 226 x 226 pixels.
- Images: 10,259.
- Annotated defects: 20,276.
- Annotation type: manually annotated bounding boxes.
- Released formats: YOLO and COCO; labels were initially annotated in VOC style with LabelImg.
- Splits: 8,208 training images with 16,184 boxes; 2,051 validation images with 4,092 boxes.
- Defect categories: Short, Spur, Spurious copper, Open, Mouse bite, Hole breakout, Conductor scratch, Conductor foreign object, and Base material foreign object.
- Object sizes: 13,575 small, 5,797 medium, and 904 large bounding boxes under COCO size definitions.
- Filtering: removes defect-free images, duplicate defect images, incomplete defect images, and defect categories that cannot be identified from 2D visual inspection alone.
- Validation baselines: [[Co-DETR]] reports AP50 0.848 and AP50:95 0.492; [[YOLOv6-L6]] reports AP50 0.851 and AP50:95 0.514.
- Limitations: 2D AOI images cannot identify raised or recessed defects; images are cropped local regions rather than full-board locations; solder-mask-stage defects are outside the selected scope.

## Source Anchors

- Hosting source: https://doi.org/10.6084/m9.figshare.24970329.
- Figshare landing page: https://figshare.com/articles/dataset/DsPCBSD_/24970329.
- Introducing paper: [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]].

## Related Concepts

- [[Semiconductor and electronics]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[PCB defect detection]]
- [[Object detection]]
- [[Co-DETR]]
- [[YOLOv6-L6]]
