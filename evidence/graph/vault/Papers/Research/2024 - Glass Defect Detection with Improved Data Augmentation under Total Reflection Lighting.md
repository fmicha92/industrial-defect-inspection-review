---
title: "Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting"
aliases:
  - "Glass Defect Detection with Improved Data Augmentation"
paper_key: "sha256:783f4ef49bd0a25bcc1b8f1a20fbe0a93f0a00852f845ede9a0a4dde48da9458"
paper_type: research
year: 2024
venue: "Applied Sciences"
authors:
  - "Pengfei Ding"
  - "Liangen Yang"
status: processed
processed_at: 2026-06-03
topics:
  - "mobile phone flat glass defect detection"
  - "automatic optical inspection"
  - "small target detection"
  - "data augmentation"
tasks:
  - "[[Smartphone screen glass defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[Mobile Phone Flat Glass Defect Dataset]]"
methods:
  - "[[YOLOv5_zc]]"
  - "[[YOLOv5]]"
  - "[[Convolutional Block Attention Module]]"
  - "[[Poisson defect image augmentation]]"
  - "[[Total reflection grazing incidence combined lighting]]"
model_family:
  - "[[YOLOv5]]"
architectures:
  - "[[YOLOv5_zc]]"
metrics:
  - "[[mAP]]"
  - "[[Average precision]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[False acceptance rate]]"
  - "[[False rejection rate]]"
  - "[[Detection success rate]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "Precision: TP / (TP + FP)."
  - "Recall: TP / (TP + FN)."
  - "MAP: mean of AP values over categories."
baselines:
  - "YOLOv5"
  - "YOLOv5_c"
  - "YOLOv5_z"
benchmarks:
  - "not reported"
code: "not reported"
data: "raw data available from the authors on request"
doi: "10.3390/app14135658"
url: "https://doi.org/10.3390/app14135658"
pdf: "paper-inbox/10_processed/Research/2024 - Ding - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting.pdf"
related_papers:
  - "[[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]"
  - "[[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[YOLOv5_zc]]"
  - "[[Poisson defect image augmentation]]"
  - "[[Total reflection grazing incidence combined lighting]]"
related_datasets:
  - "[[Mobile Phone Flat Glass Defect Dataset]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Ding - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Ding - Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting.txt"
---

# Glass Defect Detection with Improved Data Augmentation under Total Reflection Lighting

## Summary

Ding and Yang build an automatic optical inspection system for mobile phone flat-glass defects. The system combines total-reflection and grazing-incidence illumination, segmentation-based defect augmentation with Poisson image editing, and an improved YOLOv5 detector with CBAM and a small-target detection layer.

## Paper Type

Research paper. It proposes and evaluates a complete inspection pipeline for four-class mobile phone flat-glass defect detection.

## Problem

Mobile phone flat glass can contain pitting, scratches, chipping, watermarks, dust, stains, and point defects after cutting, edging, tempering, handling, and transfer-line exposure. The paper focuses on tiny defects, especially dust and point defects, because dust can resemble bright point defects and conventional lighting makes the two difficult to separate.

## Contribution

- Designs a total reflection and grazing-incidence combined light source for an automatic optical inspection platform.
- Proposes a segmentation and Poisson image editing augmentation pipeline that extracts defects, fuses them onto clean backgrounds, and outputs class and position labels.
- Improves YOLOv5 with CBAM and a small-target detection layer for four defect categories on mobile phone flat glass.

## Method

The hardware platform includes lighting, mechanical/control, image acquisition/imaging, and computer subsystems. The inspection flow transports flat glass to a fixed position, captures images first with the total-reflection light source and then with the grazing-incidence light source, processes the acquired images, and rejects defective glass when the result is NG.

The model starts from YOLOv5. CBAM is embedded in the backbone to refine channel and spatial features, and an added small-target detection layer uses shallower feature maps to improve detection of tiny defects. The augmentation pipeline uses Butterworth low-pass filtering in the frequency domain, one-dimensional maximum entropy segmentation, mask-based defect extraction, and Poisson image editing to fuse defects onto 480 x 480 clean backgrounds.

## Evidence

The training set uses 1000 collected images of bright spots, scratches, dust, and stains plus generated samples; 800 clean background images are added, yielding 1600 training images with 2400 point, slice, dust, and dirt defects. The validation set contains 200 images with 300 defects, and the test set contains 200 non-synthetic original images with 300 defects.

Validation-set ablations report:

| Model | MAP | Precision | Recall | FPS |
|---|---:|---:|---:|---:|
| YOLOv5 | 95.74% | 96.01% | 95.98% | 87 |
| YOLOv5_c | 96.73% | 96.27% | 96.32% | 65 |
| YOLOv5_z | 97.56% | 97.94% | 97.02% | 87 |
| YOLOv5_zc | 98.36% | 98.68% | 98.72% | 65 |

On the testing set, YOLOv5_zc correctly detects 296/300 point defects, 300/300 slice defects, 289/300 dust defects, and 300/300 dirty defects. The average correct detection rate is 98.75%. The abstract reports FAR of 1.27%, FRR of 2.47%, and detection speed of 64 FPS.

## ML/DL Extraction

- Task formulation: four-class object detection for bright spot, scratch/slice, dust, and stain/dirty defects on mobile phone flat glass.
- Inputs: 480 x 480 images from a custom optical inspection platform and fused augmentation images.
- Architecture: improved YOLOv5 with CBAM in the backbone and an extra small-target detection layer.
- Training environment: PyTorch on Windows 10; AMD R9-5900H CPU, RTX 3070 GPU, 32 GB memory, 8 GB video memory.
- Loss/objective: YOLOv5 detection training objective; exact loss weighting is not reported.
- Hyperparameters: learning rate, batch size, and weight magnitudes are adjusted, but exact values are not reported.
- Evaluation protocol: validation-set ablation across YOLOv5, YOLOv5_c, YOLOv5_z, and YOLOv5_zc; final testing on non-synthetic original images with NMS IoU 0.45.
- Code: not reported.
- Data: raw data available from authors on request.

## Limitations

- Edge-region defect detection on mobile phone flat glass is not completed; the paper states that future work will include edge defects.
- The dataset is not directly released in the paper; raw data is available only on request.
- The reported test set is small at 200 images and 300 defects.
- Hyperparameters and code availability are not fully reported.

## Connections

### Graph Hubs

- Tasks: [[Smartphone screen glass defect detection]], [[Object detection]]
- Methods: [[YOLOv5_zc]], [[YOLOv5]], [[Convolutional Block Attention Module]], [[Poisson defect image augmentation]], [[Total reflection grazing incidence combined lighting]]
- Datasets: [[Mobile Phone Flat Glass Defect Dataset]]
- Domains: [[Glass inspection]]
- Metrics: [[mAP]], [[Average precision]], [[Precision]], [[Recall]], [[False acceptance rate]], [[False rejection rate]], [[Detection success rate]]

### Relationship Rationale

- Shares task: [[Smartphone screen glass defect detection]] because the paper detects defects on mobile phone flat glass.
- Application/domain: [[Glass inspection]] because the inspection target is mobile phone flat glass.
- Shares dataset: [[Mobile Phone Flat Glass Defect Dataset]] is the paper-specific dataset collected with the inspection platform.
- Shares method: [[YOLOv5_zc]] is the proposed improved detector.
- Shares method: [[Poisson defect image augmentation]] is used to synthesize defect images and labels for training.
- Shares method: [[Total reflection grazing incidence combined lighting]] is the inspection lighting setup used to distinguish defect appearances.
- Shares metric: [[mAP]], [[Precision]], [[Recall]], [[False acceptance rate]], [[False rejection rate]], and [[Detection success rate]] are reported for model evaluation.
- Follow-up reading: [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] and [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] cover related smartphone screen glass datasets and detectors.

## Questions

- How well does the method transfer to the edge-region defect detection task the authors leave for future work?
- Would the same illumination and augmentation pipeline remain stable across different factories, glass coatings, and camera/light-source calibrations?
