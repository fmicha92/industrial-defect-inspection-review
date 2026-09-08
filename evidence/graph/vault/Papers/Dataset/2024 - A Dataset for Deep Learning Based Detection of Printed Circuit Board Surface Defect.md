---
title: "A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect"
aliases:
  - "A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect"
  - "DsPCBSD+ paper"
paper_key: "doi:10.1038/s41597-024-03656-8"
paper_type: "dataset"
year: 2024
venue: "Scientific Data"
authors:
  - "Shengping Lv"
  - "Kaibin Zhang"
  - "Bin Ouyang"
  - "Zhihua Deng"
  - "Tairan Liang"
  - "Shixin Jiang"
  - "Jianyu Chen"
  - "Zhuohui Li"
status: "processed"
processed_at: "2026-06-09"
topics:
  - "PCB surface defects"
  - "dataset"
  - "object detection"
tasks:
  - "[[PCB defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[DsPCBSD+]]"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Co-DETR]]"
  - "[[YOLOv6-L6]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[Co-DETR]]"
  - "[[YOLOv6-L6]]"
metrics:
  - "[[mAP]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.75]]"
  - "[[mAP@0.50-0.95]]"
  - "[[Average precision]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "AP50, AP75, and AP50:95 are reported at IoU 0.50, IoU 0.75, and IoU 0.50-0.95."
  - "APS, APM, and APL report AP for small, medium, and large objects."
baselines:
  - "[[Co-DETR]]"
  - "[[YOLOv6-L6]]"
benchmarks:
  - "[[DsPCBSD+]]"
code: "Hash.py released with the dataset; label conversion uses VOC2YOLO and YOLO2COCO; validation uses public Co-DETR and YOLOv6 code"
data: "https://doi.org/10.6084/m9.figshare.24970329"
doi: "10.1038/s41597-024-03656-8"
url: "https://doi.org/10.1038/s41597-024-03656-8"
pdf: "paper-inbox/00_incoming/s41597-024-03656-8.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Co-DETR]]"
  - "[[YOLOv6-L6]]"
related_datasets:
  - "[[DsPCBSD+]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[PCB defect detection]]"
  - "[[Object detection]]"
related_benchmarks:
  - "[[DsPCBSD+]]"
source_file: "paper-inbox/00_incoming/s41597-024-03656-8.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Lv - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Lv - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect.txt"
artifact_status: "dataset, hash-filtering code, and validation-code links available"
tags:
  - paper
---
# A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect

## Summary

Lv et al. introduce [[DsPCBSD+]], a public PCB surface-defect dataset for deep-learning object detection. The dataset contains 10,259 JPG images of actual inner- and outer-layer PCB defects from Guangzhou FastPrint Technology AOI equipment, with 20,276 manually annotated bounding boxes across nine defect categories. The paper defines the defect taxonomy, explains filtering and labeling decisions, releases YOLO and COCO formats, and validates the dataset with [[Co-DETR]] and [[YOLOv6-L6]].

### Graph Hubs

- Tasks: [[PCB defect detection]], [[Object detection]]
- Datasets: [[DsPCBSD+]]
- Benchmarks: [[DsPCBSD+]]
- Domains: [[Semiconductor and electronics]]
- Methods: [[Deep convolutional neural network]], [[Co-DETR]], [[YOLOv6-L6]]
- Metrics: [[mAP]], [[mAP@0.50]], [[mAP@0.75]], [[mAP@0.50-0.95]], [[Average precision]], [[Precision]], [[Recall]], [[F1-score]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

## Paper Type

Dataset descriptor. The paper contributes a public labeled dataset, a PCB surface-defect taxonomy, dataset construction and validation procedures, and benchmark results showing that the dataset can train object detectors.

## Problem

PCB surface defects can affect appearance, electrical performance, and the whole board. Manual visual inspection is subjective, labor-intensive, inconsistent, and inefficient. Existing PCB defect datasets are limited by artificial synthesis, narrow defect coverage, missing or coarse categories, train/validation leakage after augmentation, ambiguous AOI crops, lack of guidance for visually indeterminate defects, and in many cases no public release.

## Contribution

- Defines a PCB surface-defect taxonomy with four cause-level groups and nine detection categories.
- Builds [[DsPCBSD+]] from actual PCB production defects after inner- and outer-layer etching, rather than artificial defect synthesis.
- Provides 10,259 images and 20,276 manually annotated bounding boxes in YOLO and COCO formats.
- Validates the dataset with [[Co-DETR]] and [[YOLOv6-L6]], including original 8:2 partition results and five-fold cross-validation.

## Dataset / Benchmark Details

[[DsPCBSD+]] is built from images retrieved from AGLE'OL AOI-100 V8 equipment at Guangzhou FastPrint Technology Co., Ltd. The equipment uses controllable LED spotlight illumination and a 16K line-scan image acquisition system with four cameras mounted on top and four on the bottom to capture both PCB sides. The source pool contains 32,259 JPG images at 226 x 226 pixels.

Defects are grouped by cause into copper residue, copper deficiency, conductor scratch, and foreign object. The nine detection categories are:

| Abbrev. | Category | Cause group |
|---|---|---|
| SH | Short | copper residue |
| SP | Spur | copper residue |
| SC | Spurious copper | copper residue |
| OP | Open | copper deficiency |
| MB | Mouse bite | copper deficiency |
| HB | Hole breakout | copper deficiency |
| CS | Conductor scratch | conductor scratch |
| CFO | Conductor foreign object | foreign object |
| BMFO | Base material foreign object | foreign object |

Filtering removes defect-free images, duplicate defect images, incomplete defect images, and visually indeterminate categories outside the nine-class scheme. Duplicate filtering uses hash-value matching followed by manual selection of the image with the highest defect percentage. All images containing Open and Short defects are retained because those defects can directly scrap PCB; other categories are sampled and supplemented to reduce class imbalance.

Annotations are made with LabelImg, initially in VOC XML format, then converted to YOLO and COCO. Each defective object receives a bounding box and one of the nine abbreviations. Images may contain multiple defect categories and multiple boxes.

Dataset counts:

| Split / size group | Images | Defect boxes |
|---|---:|---:|
| Total | 10,259 | 20,276 |
| Training | 8,208 | 16,184 |
| Validation | 2,051 | 4,092 |
| Small objects | not applicable | 13,575 |
| Medium objects | not applicable | 5,797 |
| Large objects | not applicable | 904 |

Category counts:

| Category | Small | Medium | Large | Total |
|---|---:|---:|---:|---:|
| SH | 710 | 205 | 0 | 915 |
| SP | 4,469 | 115 | 0 | 4,584 |
| SC | 1,352 | 231 | 10 | 1,593 |
| OP | 1,406 | 361 | 3 | 1,770 |
| MB | 2,421 | 108 | 0 | 2,529 |
| HB | 35 | 2,848 | 0 | 2,883 |
| CS | 734 | 1,043 | 713 | 2,490 |
| CFO | 1,140 | 582 | 110 | 1,832 |
| BMFO | 1,308 | 304 | 68 | 1,680 |

## Method

The paper is not primarily a model paper. Dataset validation trains [[Co-DETR]] and [[YOLOv6-L6]] on DsPCBSD+ using recommended default settings adjusted for dataset characteristics such as batch size, initial learning rate, and epochs. Co-DETR input images are resized to 1333 x 800; YOLOv6-L6 input images are resized to 1280 x 1280.

## Evidence

The dataset was validated by five PCB manufacturing experts, who manually reviewed all images and labels. Ambiguous cases involving similar categories, multi-element defects, or overlapping boxes were resolved by group discussion considering defect severity, defect location proportions, and visibility.

### Experimental Setup

- Models: [[Co-DETR]] and [[YOLOv6-L6]].
- Hardware: Ubuntu 20.04 64-bit, Intel Xeon Gold 6242R CPU, GeForce RTX 3090 GPU.
- Co-DETR environment: Python 3.7.11, PyTorch 1.11.0, Torchvision 0.12.0, MMCV-full 1.5.0, MMDetection 2.25.3.
- YOLOv6-L6 environment: Python 3.8.18, PyTorch 1.13.1, Torchvision 0.14.1.
- Training time: Co-DETR about 69 minutes; YOLOv6-L6 about 721 minutes on the reported test device configuration.

### Main Results

| Model | AP50 | AP75 | AP50:95 | APS | APM | APL | AR50:95 | ARS | ARM | ARL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [[Co-DETR]] | 0.848 | 0.490 | 0.492 | 0.425 | 0.554 | 0.671 | 0.668 | 0.600 | 0.743 | 0.846 |
| [[YOLOv6-L6]] | 0.851 | 0.525 | 0.514 | 0.405 | 0.597 | 0.681 | 0.654 | 0.590 | 0.748 | 0.812 |

Five-fold cross-validation:

| Model | AP50 | AP75 | AP50:95 | APS | APM | APL | AR50:95 | ARS | ARM | ARL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Co-DETR5 | 0.840 | 0.483 | 0.484 | 0.420 | 0.551 | 0.547 | 0.648 | 0.612 | 0.746 | 0.858 |
| YOLOv6-L65 | 0.837 | 0.512 | 0.502 | 0.405 | 0.591 | 0.614 | 0.651 | 0.596 | 0.748 | 0.823 |

The five-fold results show minimal deviation from the original split, which the paper interprets as evidence that the folds contain representative samples.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP@0.50]] | object detection | AP at IoU 0.50 | higher | yes | Co-DETR 0.848; YOLOv6-L6 0.851 |
| [[mAP@0.75]] | object detection | AP at IoU 0.75 | higher | no | Co-DETR 0.490; YOLOv6-L6 0.525 |
| [[mAP@0.50-0.95]] | object detection | AP over IoU 0.50 to 0.95 | higher | no | Co-DETR 0.492; YOLOv6-L6 0.514 |
| [[Average precision]] | per-class detection | per-class AP at IoU 0.50 | higher | no | HB is highest for both models: 0.973 Co-DETR, 0.971 YOLOv6-L6 |
| [[Precision]] | per-class detection | positive predictive value | higher | no | Co-DETR per-class P ranges 0.688 to 0.866; YOLOv6-L6 ranges 0.442 to 0.726 |
| [[Recall]] | per-class detection | detected true defects | higher | no | Co-DETR per-class R ranges 0.659 to 0.980; YOLOv6-L6 ranges 0.697 to 0.987 |
| [[F1-score]] | per-class detection | harmonic mean of precision and recall | higher | no | Co-DETR per-class F1 ranges 0.695 to 0.920; YOLOv6-L6 ranges 0.582 to 0.836 |

### Failure Cases

- Smaller detected defect objects produce lower average precision and recall for both Co-DETR and YOLOv6-L6.
- SC is misclassified as SP at a relatively higher rate than other cross-category errors, attributed to similar features when spurious copper is close to a conductor.
- SP, CS, and CFO have relatively high missed-detection rates. The paper attributes SP misses to small size, CS misses to large internal size variation and small scratches, and CFO misses to color, size, and morphology variation that can resemble the background.

## ML/DL Extraction

- Task formulation: object detection for PCB surface-defect localization and classification.
- Inputs: 226 x 226 local PCB defect images in JPG format.
- Outputs: bounding boxes and nine-class defect labels.
- Supervision: fully supervised object detection from manually annotated boxes.
- Baselines: [[Co-DETR]] and [[YOLOv6-L6]].
- Training data: 8,208 training images and 16,184 training boxes.
- Validation data: 2,051 validation images and 4,092 validation boxes.
- Preprocessing: AOI image preprocessing includes noise removal, contrast enhancement, and brightness adjustment before source images are archived; dataset construction filters defect-free, duplicate, incomplete, and out-of-scope defect images.
- Label formats: VOC-style annotation during labeling, released as YOLO and COCO.
- Compute: Intel Xeon Gold 6242R and GeForce RTX 3090.
- Code: `Hash.py` is released with the dataset; label conversion and model validation use public tooling.

## Limitations

- Defects are limited to 2D because the AOI cameras lack 3D depth information, so raised or recessed defects cannot be identified.
- Images come from inner and outer board layers after etching and do not include solder-mask-stage defects.
- Images are cropped local regions, not whole-board images; practical localization would require integrating local detections back into the complete board.
- Small, visually subtle, and background-similar defects remain difficult for the validation models.

## Reproducibility

- Data: public Figshare dataset at [10.6084/m9.figshare.24970329](https://doi.org/10.6084/m9.figshare.24970329).
- Dataset code: `Hash.py` for hash-value duplicate filtering is released with the dataset.
- Annotation tool: LabelImg.
- Format conversion: VOC2YOLO and YOLO2COCO are referenced.
- Validation code: public [[Co-DETR]] and [[YOLOv6-L6]] repositories are referenced.
- Environment: package versions are reported for both validation models.
- Random seeds: not reported.

## Connections

### Shares Dataset

- [[DsPCBSD+]] is introduced by this paper as a public PCB surface-defect dataset.

### Shares Task

- [[PCB defect detection]] is the main applied task.
- [[Object detection]] is the benchmark formulation because defects are annotated with bounding boxes and evaluated with AP/mAP.

### Shares Method

- [[Co-DETR]] and [[YOLOv6-L6]] are validation baselines trained on DsPCBSD+.
- [[Deep convolutional neural network]] is the broader model family supporting the paper's DL-based AOI motivation.

### Shares Metric

- [[mAP@0.50]], [[mAP@0.75]], [[mAP@0.50-0.95]], [[Average precision]], [[Precision]], [[Recall]], and [[F1-score]] are used to validate detector performance.

### Application/Domain

- [[Semiconductor and electronics]] is the domain because the dataset covers PCB inner- and outer-layer surface defects from PCB fabrication.
- [[Surface defect detection]] and [[Industrial visual inspection]] describe the inspection setting.

### Follow-Up Reading

- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] introduces [[DeepPCB]], one of the earlier PCB defect datasets compared in this paper.
- [[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]] introduces [[HRIPCB|PKU-Market-PCB]], another earlier PCB defect dataset compared in this paper.

## Source Anchors

- Paper DOI: [10.1038/s41597-024-03656-8](https://doi.org/10.1038/s41597-024-03656-8)
- Dataset DOI: [10.6084/m9.figshare.24970329](https://doi.org/10.6084/m9.figshare.24970329)
- LabelImg: [https://github.com/heartexlabs/labelImg](https://github.com/heartexlabs/labelImg)
- VOC2YOLO: [https://github.com/RapidAI/VOC2YOLO](https://github.com/RapidAI/VOC2YOLO)
- YOLO2COCO: [https://github.com/RapidAI/YOLO2COCO](https://github.com/RapidAI/YOLO2COCO)
- Co-DETR: [https://github.com/Sense-X/Co-DETR](https://github.com/Sense-X/Co-DETR)
- YOLOv6: [https://github.com/meituan/YOLOv6](https://github.com/meituan/YOLOv6)

## Questions

- How well do detectors trained on cropped local images transfer to full-board localization workflows?
- Which model changes improve small SP, CS, and CFO detection without increasing confusion between SP and SC?
