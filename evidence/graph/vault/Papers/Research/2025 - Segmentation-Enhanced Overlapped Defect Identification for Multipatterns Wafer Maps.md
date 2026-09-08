---
title: "Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps"
aliases:
  - "SEODI"
paper_key: "doi:10.1109/tim.2025.3565049"
paper_type: research
year: 2025
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Tianming Ni"
  - "Wen Jiang"
  - "Huaguo Liang"
  - "Xiaoqing Wen"
  - "Mu Nie"
status: processed
processed_at: 2026-06-11
topics:
  - "wafer map defect identification"
  - "overlapped defects"
  - "segmentation-enhanced detection"
  - "copy-paste augmentation"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Defect detection]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[MixedWM38]]"
methods:
  - "[[SEODI]]"
  - "[[YOLOv7]]"
  - "[[U-Net]]"
  - "[[Data augmentation]]"
metrics:
  - "[[mAP]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[Exact match]]"
primary_metric: "[[mAP]]"
baselines:
  - "Kim et al. multipattern wafer-map classifier"
  - "Shinde et al. wafer defect detection baseline"
  - "Mask R-CNN"
  - "DC-Net"
doi: "10.1109/TIM.2025.3565049"
url: "https://doi.org/10.1109/TIM.2025.3565049"
data: "[[MixedWM38]]"
code: "not reported"
related_methods:
  - "[[SEODI]]"
  - "[[YOLOv7]]"
  - "[[U-Net]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MixedWM38]]"
related_tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2025 - Ni - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Ni - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Ni - Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps.txt"
artifact_status: "code not reported"
tags:
  - paper
---
# Segmentation-Enhanced Overlapped Defect Identification for Multipatterns Wafer Maps

## Summary

The paper proposes [[SEODI]], a two-stage wafer-map framework that combines YOLO-style detection with [[U-Net]] segmentation to identify single, mixed, and overlapped wafer-map defect patterns. It uses copy-paste augmentation, rotation augmentation, and similarity-based label generation to reduce manual segmentation labeling for [[MixedWM38]]-based experiments.

## Paper Type

- Type: research.
- Why: The paper proposes a wafer-map detection/segmentation framework and evaluates it quantitatively against prior multipattern recognition baselines.

## Problem

- Task: multipattern and overlapped wafer-map defect identification.
- Setting: real semiconductor wafer maps where several defect patterns may occur together.
- Motivation: classification-only methods can miss overlap structure and cannot localize defect regions.

## Contribution

- Claimed: segmentation enhances overlapped defect identification beyond classification-only multipattern recognition.
- Claimed: similarity matching between detection results and segmentation masks reduces manual mask labeling.
- Shown: the method reports 89.3% overlapped type recognition accuracy and 89% mAP for defect localization.

## Method

- Detection stage: YOLOv7-style detector using ELAN/CBS/REP components.
- Segmentation stage: [[U-Net]].
- Augmentation: copy-paste augmentation and rotation augmentation; the paper reports four rotational augmentations as optimal, with three augmentations reaching 0.97 accuracy and five giving no further improvement.
- Label-generation support: SIFT + FLANN feature matching, ratio test threshold 0.8, and positional/shape similarity scoring connect detection output to segmentation labels.
- Overlap classes: crossed, sandwich, and accessory.

## Data

- Dataset: [[MixedWM38]], described as a real semiconductor fabrication wafer-map dataset with 38,014 wafer images and 38 defect types.
- Experiment subset: 1,160 raw wafer images, including 700 single defects, 200 mixed defects, and overlapped maps split across 90 crossed, 90 sandwich, and 80 accessory cases.
- Split: 8:1:1 after augmentation.

## Evidence

| Setting | Baseline result | Result after segmentation / augmentation | Metric | Notes |
|---|---:|---:|---|---|
| Single defect localization | not fully preserved in extracted comparison table | 89.6 | mAP | Text reports 89.6% mAP and 99.4% F1 for single defect tests. |
| Multipattern recognition | not fully preserved in extracted comparison table | 89 | exact match | Text reports 89% exact match for multipattern recognition. |
| Overlapped type recognition | Kim et al. lower by 6 points | 89.3 | accuracy | Text reports +6% accuracy, +5.1% F1, and +8% recall over Kim et al. |
| Localization | not reported as a baseline-vs-augmented pair | 89 | mAP | Abstract-level localization result. |

## ML / DL Extraction

- Task formulation: detect, segment, and classify wafer defect patterns, including overlapped combinations.
- Input: wafer-map images from [[MixedWM38]].
- Model family: YOLO-style object detection plus U-Net segmentation.
- Training: PyTorch; RTX 3090 GPU; the source reports SGD, learning rate 0.001, and batch sizes 16 and 4 in the experiment setup.
- Metrics: [[mAP]], [[Precision]], [[Recall]], [[F1-score]], Hamming loss, and [[Exact match]].
- Code: not reported.

## Limitations

- The approach still needs some manually marked masks.
- Edge-loc and edge-ring are visually similar enough that the paper unifies them for segmentation handling.
- Future work: unseen overlap types, stronger self-learning, and end-to-end wafer inspection integration.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Defect segmentation]], [[Defect detection]]
- Methods: [[SEODI]], [[YOLOv7]], [[U-Net]], [[Data augmentation]]
- Datasets: [[MixedWM38]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[mAP]], [[Precision]], [[Recall]], [[F1-score]], [[Exact match]]

### Relationship Notes

- Shares dataset: [[MixedWM38]].
- Shares task: [[Wafer map defect classification]], [[Defect segmentation]], and [[Defect detection]].
- Shares method: [[YOLOv7]], [[U-Net]], and [[Data augmentation]].
- Application/domain: [[Semiconductor and electronics]].

## Questions

- What are the exact baseline values in the image-only tables that were not preserved in the text extraction?
- How robust is the similarity-matching label generation when wafer maps contain unseen overlap types?
- Can the segmentation stage be trained end-to-end without manual mask correction?
