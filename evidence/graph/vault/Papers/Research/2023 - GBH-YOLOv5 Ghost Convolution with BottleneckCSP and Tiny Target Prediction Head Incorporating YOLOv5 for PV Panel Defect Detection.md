---
title: "GBH-YOLOv5: Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection"
aliases:
  - "GBH-YOLOv5"
paper_key: "sha256:337261a38e08a92e831d51766381541ca0bbcd5039c7442e2a06e91b6b583d96"
paper_type: "research"
year: 2023
venue: "Electronics"
authors:
  - "Longlong Li"
  - "Zhifeng Wang"
  - "Tingting Zhang"
affiliations:
  - "Central China Normal University"
  - "Northwest Normal University"
status: "processed"
topics:
  - "PV panel defect detection"
  - "YOLOv5"
  - "tiny target detection"
tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PV-Multi-Defect]]"
methods:
  - "[[GBH-YOLOv5]]"
  - "[[YOLOv5]]"
  - "[[Ghost module]]"
model_family:
  - "[[Computer Vision Models]]"
metrics:
  - "[[mAP]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[mAP]]"
baselines:
  - "YOLOv3-based method"
  - "Faster R-CNN"
  - "SVM"
  - "Mask R-CNN"
  - "SSD"
  - "YOLOv5s"
doi: "10.3390/electronics12030561"
url: "https://doi.org/10.3390/electronics12030561"
data: "https://github.com/CCNUZFW/PV-Multi-Defect"
code: "https://github.com/CCNUZFW/GBH-YOLOv5"
licenses:
  - "article: CC BY 4.0"
  - "dataset: not reported"
related_concepts:
  - "[[PV panel fault detection]]"
related_methods:
  - "[[GBH-YOLOv5]]"
  - "[[YOLOv5]]"
  - "[[Ghost module]]"
related_datasets:
  - "[[PV-Multi-Defect]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Li - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Li - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection.txt"
source_file: "paper-inbox/10_processed/Research/2023 - Li - GBH-YOLOv5 Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection.pdf"
---
# GBH-YOLOv5: Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection

## Summary

Li, Wang, and Zhang propose [[GBH-YOLOv5]], a modified YOLOv5s detector for photovoltaic panel surface defects. The paper also introduces [[PV-Multi-Defect]], a public dataset with 1,108 preprocessed 600 x 600 images and 4,235 defect targets across five classes. GBH-YOLOv5 reports 97.8% mAP on this dataset, improving over the listed comparison methods and over the YOLOv5s ablation by adding BottleneckCSP, an extra tiny-target prediction head, and Ghost convolution.

## Paper Type

Research paper with a dataset contribution. The main contribution is a YOLOv5-based detection architecture for PV panel surface-defect detection, supported by the release of [[PV-Multi-Defect]].

## Problem

PV panel surface-defect detection must localize multiple small and visually similar defects. The paper emphasizes scratches as tiny targets and notes that defect sizes can be less than 0.08% of the original image, making direct detection on raw high-resolution images difficult.

## Contribution

- Proposes [[GBH-YOLOv5]], a YOLOv5s-derived detector with BottleneckCSP, a tiny-target prediction head, and Ghost convolution.
- Introduces [[PV-Multi-Defect]], a public five-class PV panel surface-defect dataset.
- Reports comparison and ablation experiments showing 97.8% mAP for GBH-YOLOv5 on PV-Multi-Defect.

## Method

### Dataset

- Original collection: 307 PV-panel images at 5,800 x 3,504 pixels.
- Original module specification: photovoltaic modules with physical size 1.65 m x 0.991 m and 60 pieces.
- Preprocessing: grayscale processing, compression, and cropping to 600 x 600 pixels based on defect distribution.
- Final dataset: 1,108 defect images and 4,235 defective targets.
- Split: 886 training images and 222 validation images.
- Annotation format: LabelImg labels converted to XML in VOC2007-style format.
- Classes: broken, hot_spot, black_border, scratch, and no_electricity.

### Detector

- Base architecture: YOLOv5s.
- Input handling: images not already 600 x 600 are compressed and cropped.
- Training initialization: COCO pretrained weights.
- Data augmentation: Mosaic data enhancement and adaptive image scaling are used in the YOLOv5 pipeline.
- Backbone/neck changes: BottleneckCSP replaces the C3 residual module to extract deeper semantic information and fuse multiscale features.
- Tiny-target handling: a fourth prediction head is added using features from the second backbone layer, with an added anchor frame for small targets.
- Efficiency change: conventional convolutions are replaced with [[Ghost module|Ghost convolution]].
- Output: FPN and PAN structures classify extracted features; CIoU loss is used for bounding boxes and NMS is used for multiple or fuzzy targets.

## Evidence

### Training Setup

- Hardware: RTX 3090 GPU and 48 GB RAM.
- Framework: PyTorch with CUDA 11.1; the paper reports PyTorch version as 1.8.
- Optimizer: Adam.
- Batch size: 16.
- Learning rate: 0.001.
- Epochs selected for final model: 500.
- Code: the paper reports implementation code at [CCNUZFW/GBH-YOLOv5](https://github.com/CCNUZFW/GBH-YOLOv5).

### Dataset Distribution

| Defect class | Share of targets |
|---|---:|
| hot_spot | 49.09% |
| scratch | 36.62% |
| black_border | 6.02% |
| no_electricity | 4.28% |
| broken | 3.99% |

### Baseline Comparison

| Method | mAP |
|---|---:|
| Tommaso et al. YOLOv3-based method | 57.9% +/- 0.07 |
| Faster R-CNN-based method | 69.3% +/- 0.06 |
| SVM-based method | 45.3% +/- 0.07 |
| Mask R-CNN-based method | 51.2% +/- 0.06 |
| SSD-based method | 30.8% +/- 0.06 |
| GBH-YOLOv5 | 97.8% +/- 0.02 |

### Ablation Results

| Model | Description | mAP | Precision | Recall |
|---|---|---:|---:|---:|
| YOLOv5s | base YOLOv5s | 78.1% +/- 0.06 | 83.2% +/- 0.05 | 73.4% +/- 0.06 |
| YOLOv5-1 | YOLOv5s + BottleneckCSP | 94.2% +/- 0.03 | 88.2% +/- 0.04 | 90.5% +/- 0.04 |
| YOLOv5-2 | YOLOv5s + BottleneckCSP + extra prediction head | 97.1% +/- 0.02 | 93.4% +/- 0.03 | 94.6% +/- 0.03 |
| GBH-YOLOv5 | YOLOv5s + BottleneckCSP + extra prediction head + GhostConv | 97.8% +/- 0.02 | 96.4% +/- 0.02 | 93.3% +/- 0.02 |

### Per-Class mAP

| Model | broken | hot_spot | black_border | scratch | no_electricity |
|---|---:|---:|---:|---:|---:|
| YOLOv5s | 78.5% | 87.8% | 85.4% | 69.3% | 88.0% |
| YOLOv5-1 | 99.5% | 97.2% | 96.4% | 95.6% | 97.7% |
| YOLOv5-2 | 99.5% | 98.4% | 96.7% | 96.4% | 98.9% |
| GBH-YOLOv5 | 99.5% | 97.5% | 97.2% | 97.4% | 98.0% |

### Efficiency

| Model | Layers | Parameters | Average elapsed time |
|---|---:|---:|---:|
| YOLOv5s | 224 | 7.06 x 10^4 | 0.484 s |
| YOLOv5-1 | 228 | 7.15 x 10^4 | 0.658 s |
| YOLOv5-2 | 290 | 7.72 x 10^4 | 0.695 s |
| GBH-YOLOv5 | 270 | 7.24 x 10^4 | 0.587 s |

## ML/DL Extraction

- Task formulation: bounding-box object detection for PV panel surface defects.
- Inputs: 600 x 600 preprocessed PV panel surface images.
- Outputs: defect class and bounding box.
- Model family: YOLOv5-style one-stage object detection.
- Objective/loss: CIoU loss for bounding boxes; classification/objectness losses are not fully specified.
- Training recipe: COCO-pretrained initialization, Adam optimizer, 500 epochs, batch size 16, learning rate 0.001.
- Evaluation metrics: precision, recall, and mAP.
- Artifact availability: dataset and code URLs are reported.

## Limitations

- The selected dataset is grayscale processed, and the authors state this may generate errors when detecting PV panel defects in a natural production environment.
- The added modules increase parameter count and model volume relative to YOLOv5s.
- The paper reports a validation split, but no independent external test set is reported.
- The dataset license is not reported by the GitHub host page.
- The repository tree contains 1,108 image files and 1,106 XML annotation files under the main image/annotation folders; the paper does not explain this difference.

## Connections

### Graph Hubs

- Tasks: [[PV panel fault detection]], [[Object detection]]
- Methods: [[GBH-YOLOv5]], [[YOLOv5]], [[Ghost module]]
- Datasets: [[PV-Multi-Defect]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[mAP]], [[Precision]], [[Recall]]

### Introduces Dataset

- [[PV-Multi-Defect]] - public GitHub dataset for five-class PV panel surface-defect detection.

### Shares Task

- [[PV panel fault detection]] - the paper localizes five surface-defect types on PV panels.
- [[Object detection]] - the detector outputs bounding boxes and classes.

### Shares Method

- [[GBH-YOLOv5]] - proposed model.
- [[YOLOv5]] - base detector.
- [[Ghost module]] - used to replace conventional convolution for speed and parameter reduction.

### Shares Metric

- [[mAP]] - primary reported metric.
- [[Precision]] and [[Recall]] - reported during training and ablation.

### Application/domain

- [[Solar cells and photovoltaic]] - the task is PV panel inspection and maintenance.

## Questions

- How does GBH-YOLOv5 generalize to non-grayscale natural production images?
- Would an external solar-farm or factory dataset expose overfitting to the 222-image validation split?
- What explains the two-file gap between repository image and XML annotation counts?
