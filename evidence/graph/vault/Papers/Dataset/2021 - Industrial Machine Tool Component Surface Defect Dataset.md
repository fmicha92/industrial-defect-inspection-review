---
title: "Industrial Machine Tool Component Surface Defect Dataset"
aliases:
  - "Industrial Machine Tool Element Surface Defect Dataset"
  - "BSData paper"
paper_key: "arxiv:2103.13003"
arxiv: "2103.13003"
url: "https://arxiv.org/abs/2103.13003"
pdf: "paper-inbox/10_processed/Dataset/2021 - Schlagenhauf - Industrial Machine Tool Component Surface Defect Dataset.pdf"
source_file: "paper-inbox/10_processed/Dataset/2021 - Schlagenhauf - Industrial Machine Tool Component Surface Defect Dataset.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Schlagenhauf - Industrial Machine Tool Component Surface Defect Dataset.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Schlagenhauf - Industrial Machine Tool Component Surface Defect Dataset.txt"
authors:
  - "Tobias Schlagenhauf"
  - "Magnus Landwehr"
  - "Juergen Fleischer"
year: 2021
venue: "Data in Brief"
paper_type: "dataset"
status: "processed"
processed_at: "2026-06-03"
topics:
  - "ball screw drive surface defects"
  - "pitting detection"
  - "industrial wear forecasting"
tasks:
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
  - "[[Wear forecasting]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[BSData]]"
methods:
  - "[[Mask R-CNN]]"
  - "[[Faster R-CNN]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[Mask R-CNN]]"
metrics:
  - "[[mIoU]]"
primary_metric: "[[mIoU]]"
baselines:
  - "Mask R-CNN with COCO-pretrained Inception-ResNet-v2"
benchmarks:
  - "[[BSData]]"
code: "https://github.com/2Obe/BSData"
data: "https://doi.org/10.5445/IR/1000129520"
licenses: "CC-BY-SA-4.0 for GitHub-hosted BSData repository"
related_papers:
  - "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[Mask R-CNN]]"
related_datasets:
  - "[[BSData]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
  - "[[Wear forecasting]]"
related_benchmarks:
  - "[[BSData]]"
---

# Industrial Machine Tool Component Surface Defect Dataset

## Summary

The paper introduces [[BSData]], a real-world ball-screw-drive surface-defect dataset for pitting classification, detection, segmentation, and wear-progression analysis. It describes the sensor system and test bench, reports a 21853-image classification release, a 1104-image detection/segmentation release with 394 pitting annotations, and provides a baseline [[Mask R-CNN]] model that reaches mIoU 0.316.

## Paper Type

Dataset paper. The contribution is the dataset itself, including its collection setup, annotation structure, defect-progression sequences, and baseline model.

## Problem

Industrial machine-tool components need automated surface inspection and predictive-maintenance support, but real-world labeled data are scarce. Ball screw drives are wear-prone components, and pitting on their surfaces can develop from small early defects into larger failure modes.

## Contribution

- Provides a real-world ball-screw-drive surface-defect dataset with classification labels and pixel-level pitting annotations.
- Captures pitting development over time, enabling defect-size tracking and wear forecasting.
- Reports a ready-to-use [[Mask R-CNN]] baseline for pitting segmentation on BSData.

## Method

The dataset was generated during destruction testing at Karlsruhe Institute of Technology. A camera system mounted on the ball-screw-drive nut photographs the spindle surface under diffuse lighting. The camera is a Raspberry Pi V2 microcontroller camera, configured to capture 2592 x 1944 images. Areas of 150 x 150 pixels are cropped automatically from the large images.

The test bench can wear up to five spindles in parallel. The spindles are standard 32 mm diameter spindles without special treatment or prestress. Each spindle is preloaded with 70% of the manufacturer's `Ca`, with `Ca` chosen as 12 kN in the reported setup. The system triggers one camera drive every four hours, and the spindle is turned by 22.5 degrees between images.

## Evidence

### Classification Release

- 21853 RGB PNG images.
- Image size: 150 x 150 pixels.
- Labels: pitting (`P`) and no pitting (`N`).
- Class counts: 11075 images without pitting and 10778 images with pitting.
- Approximate balance: about 50% of images show pitting.
- The data include clean no-defect surfaces, small pitting, small pitting with pollution, no pitting with pollution, and large pitting with and without pollution.

### Detection And Segmentation Release

- 1104 channel-3 images.
- 394 image annotations for pitting.
- Annotation format: LabelMe JSON, convertible to VOC and COCO formats.
- Images come from two ball-screw-drive types.
- Repository folders include `data`, `label`, and `saved_model`.
- The release supports train/test split, wear-development split, and type split.
- The dataset contains 27 pitting development sequences.

### Baseline

- Architecture: [[Mask R-CNN]].
- Backbone: COCO-pretrained Inception-ResNet-v2.
- Reported baseline score: mIoU 0.316.
- The paper reports that the baseline has difficulty predicting small pitting.

## ML/DL Extraction

- Task formulation: pitting classification, object detection, semantic segmentation, instance segmentation, and wear-progress analysis on ball-screw-drive surface images.
- Inputs: RGB image crops or larger JPEG images, depending on release.
- Outputs: class labels, object localization, pixel-wise masks, and defect-size trajectories.
- Baseline model: [[Mask R-CNN]] with a two-stage detector and fully convolutional mask branch.
- Metrics: [[mIoU]] for the reported segmentation baseline.
- Code/model host: https://github.com/2Obe/BSData.
- Dataset DOI: https://doi.org/10.5445/IR/1000129520.

## Limitations

- The dataset is focused on pitting on ball screw drives; other machine-tool components and defect mechanisms are not covered by the reported dataset.
- The baseline mIoU is modest at 0.316, and the paper states that small pitting is difficult for the model to predict.
- Annotation uncertainty appears in the wear-development example because apparent pitting size can decrease in annotations even though the physical pitting should not shrink.
- The paper does not report a broad comparison against multiple modern segmentation or detection architectures.

## Connections

### Shares Dataset

- [[BSData]] is introduced by the paper and later reused as a source dataset for [[Industrial-5i]].

### Shares Task

- [[Defect classification]] covers the pitting/no-pitting classification release.
- [[Object detection]] and [[Defect segmentation]] cover localization and pixel-level pitting masks.
- [[Wear forecasting]] covers the pitting-development sequences over time.

### Shares Method

- [[Mask R-CNN]] is the reported baseline model.
- [[Faster R-CNN]] is part of the Mask R-CNN architecture described by the paper.

### Shares Metric

- [[mIoU]] is the reported segmentation baseline metric.

### Application/domain

- [[Metal inspection]] because the dataset images ball-screw-drive metal surfaces.

### Follow-up reading

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses BSData as one source for [[Industrial-5i]].

### Graph Hubs

- Tasks: [[Defect classification]], [[Object detection]], [[Defect segmentation]], [[Wear forecasting]]
- Methods: [[Mask R-CNN]], [[Faster R-CNN]]
- Datasets: [[BSData]]
- Domains: [[Metal inspection]]
- Metrics: [[mIoU]]

## Questions

- Which exact GitHub commit or release corresponds to the paper's baseline model?
- Are the 21853-image classification release and 1104-image segmentation release versioned together or separately?
- What train/test split file was used for the reported mIoU 0.316 baseline?
