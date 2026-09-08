---
title: "SSGD: A Smartphone Screen Glass Dataset for Defect Detection"
aliases:
  - "SSGD paper"
paper_key: "arxiv:2303.06673"
paper_type: dataset
year: 2023
venue: "arXiv"
authors:
  - "Haonan Han"
  - "Rui Yang"
  - "Shuyan Li"
  - "Runze Hu"
  - "Xiu Li"
status: processed
processed_at: 2026-05-27
topics:
  - smartphone screen glass
  - defect detection
  - object detection
  - industrial visual inspection
  - benchmark dataset
tasks:
  - "[[Smartphone screen glass defect detection]]"
domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
application_area: "smartphone touch-screen glass production quality inspection"
datasets:
  - "[[SSGD]]"
dataset_sizes:
  - "2504 images"
  - "1258 Part I images"
  - "1246 Part II images"
splits:
  - "5-fold cross-validation"
  - "Part I and Part II grouped by two capture workstations"
modalities:
  - "line-scan camera images"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Vision Transformer]]"
  - "[[YOLOv5]]"
model_family:
  - "object detection"
  - "CNN"
  - "Transformer"
architectures:
  - "Faster R-CNN"
  - "Cascade R-CNN"
  - "RetinaNet"
  - "FCOS"
  - "ATSS"
  - "GFL"
  - "YOLOv5-m"
  - "YOLOX-m"
  - "Swin-T"
  - "PVT-S"
  - "ScalableViT-S"
  - "UniFormer-Sh14"
losses: []
training_regime: "supervised object detection with COCO-pretrained detector weights"
augmentation:
  - "multi-scale training for ResNet-50-based models"
synthetic_data: "none reported"
metrics:
  - "[[Average precision]]"
  - "[[mAP@0.50]]"
  - "[[GFLOPs]]"
  - "[[FPS]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  - "AP, AP50, AP75, APS, APM, and APL are reported for object detection."
  - "FLOPs and FPS are reported for computational cost and throughput."
baselines:
  - "Faster R-CNN"
  - "Cascade R-CNN"
  - "RetinaNet"
  - "FCOS"
  - "ATSS"
  - "GFL"
  - "YOLOv5-m"
  - "YOLOX-m"
  - "Swin-T"
  - "PVT-S"
  - "ScalableViT-S"
  - "UniFormer-Sh14"
benchmarks:
  - "[[SSGD benchmark]]"
evaluation_protocol: "5-fold cross-validation with results averaged over folds"
parameters: "reported per model in tables"
compute: "4 GPUs for ResNet-50 and YOLO-series models; 8 GPUs for Transformer-based models"
hardware: "industrial line-scan camera for acquisition; single NVIDIA RTX 3090 GPU for FLOPs and FPS testing"
training_time: "not reported"
inference_cost: "FLOPs and FPS reported per model"
url: "https://arxiv.org/abs/2303.06673"
pdf: "paper-inbox/10_processed/Dataset/2023 - Han - SSGD A Smartphone Screen Glass Dataset for Defect Detection.pdf"
code: "https://github.com/VincentHancoder/SSGD"
data: "https://github.com/VincentHancoder/SSGD"
doi: "not reported"
arxiv: "2303.06673"
related_papers:
  - "[[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]]"
  - "[[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]]"
  - "[[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]"
  - "[[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Vision Transformer]]"
  - "[[YOLOv5]]"
related_datasets:
  - "[[SSGD]]"
  - "[[DeepPCB]]"
  - "[[HRIPCB]]"
  - "[[GC10-DET]]"
  - "[[CSDD]]"
related_domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
related_benchmarks:
  - "[[SSGD benchmark]]"
concept_notes_created_or_updated:
  - "[[SSGD]]"
  - "[[SSGD benchmark]]"
  - "[[Smartphone screen glass defect detection]]"
source_file: "paper-inbox/10_processed/Dataset/2023 - Han - SSGD A Smartphone Screen Glass Dataset for Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Han - SSGD A Smartphone Screen Glass Dataset for Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Han - SSGD A Smartphone Screen Glass Dataset for Defect Detection.txt"
artifact_status: "dataset and code reported available on GitHub"
tags:
  - paper
  - dataset
  - glass-inspection
---

# SSGD: A Smartphone Screen Glass Dataset for Defect Detection

## Summary

- Introduces [[SSGD]], a public smartphone touch-screen glass defect dataset with 2504 high-resolution images and seven defect categories.
- Benchmarks CNN- and Transformer-based object detectors on [[SSGD benchmark]] using 5-fold cross-validation.
- Reports that popular detectors perform modestly on high-resolution screen-glass defects, and that Transformer models are slower than CNN counterparts in this industrial setting.

## Paper Type

- Type: dataset paper.
- Why: The primary contribution is a public dataset and benchmark for [[Smartphone screen glass defect detection]], with baseline object-detection results.

## Problem

- Task: [[Smartphone screen glass defect detection]].
- Setting: production quality inspection for smartphone touch-screen glass.
- Inputs: 1500 x 1000 pixel screen-glass images captured on fixed workstations.
- Outputs: bounding boxes for seven defect categories.
- Motivation: manual screen-glass defect inspection is labor-intensive and inefficient, and public datasets for smartphone screen defects were lacking.
- Assumptions: object detection models trained with supervised bounding boxes can support automated screen-glass inspection.

## Contribution

- Claimed: The paper presents the first publicly available Smartphone Screen Glass Dataset for defect detection.
- Shown: [[SSGD]] contains 2504 images, grouped into Part I with 1258 images and Part II with 1246 images.
- Shown: The dataset covers crack, broken, spot, scratch, light-leakage, blot, and broken-membrane defects.
- Shown: The paper benchmarks CNN and Transformer object detectors with AP, AP50, AP75, object-size AP, FLOPs, parameters, and FPS.
- Shown: ATSS performs best among ResNet-50-based detectors on Part I, while YOLOv5-m reports the highest Part II AP and fastest FPS in Table 1.

## Method

- Data acquisition: defective smartphone screens were collected, selected, and captured on calibrated fixed workstations using an industrial line-scan camera.
- Scene setup: a black background was used to reduce visible-light interference; screen panels were placed on a level capture platform.
- Preprocessing: image resolution was standardized to 1500 x 1000 pixels after collection and initial cleaning.
- Annotation: LabelMe was used to label defect categories and bounding-box locations, producing one XML file per image.
- Benchmarking: mainstream object detectors were trained and evaluated with 5-fold cross-validation on Part I and Part II.

## ML / DL Extraction

### Task Formulation

- Input modality: high-resolution screen-glass images.
- Output target: defect category and bounding-box location.
- Supervision: bounding-box annotations for seven defect categories.
- Objective: detect and localize production defects on smartphone touch-screen glass.

### Model And Training

- Model family: CNN and Transformer object detectors.
- Architectures: Faster R-CNN, Cascade R-CNN, RetinaNet, FCOS, ATSS, GFL, YOLOv5-m, YOLOX-m, Swin-T, PVT-S, ScalableViT-S, and UniFormer-Sh14.
- Parameters: reported per model in the benchmark tables.
- Pretraining: detector weights initialized from COCO; new classification-head layers use the Normal scheme.
- Optimizers: SGD for ResNet-50-based models; AdamW for Transformer-based models.
- Training schedule: 2x, 24 epochs, for ResNet-50 and Transformer-based models; YOLO-series models trained for 100 epochs.
- Batch size and compute: global batch size 16 on 4 GPUs for ResNet-50-based and YOLO-series models; global batch size 8 on 8 GPUs for Transformer-based models.
- Input sizes: ResNet-50-based models use multi-scale training with short side randomly resized to 800-1500 pixels and long side up to 2250 pixels; Transformer models use 1500 x 1000 input; YOLO inputs are padded to 1500 x 1500.
- Seeds: not reported.

### Data

- Datasets: [[SSGD]].
- Data source: smartphone screen glass samples with production defects.
- Dataset size: 2504 images.
- Labels / annotations: XML bounding-box annotations for seven categories.
- Splits: 5-fold cross-validation; Part I and Part II correspond to two capture workstations.
- Preprocessing: resolution standardized to 1500 x 1000 pixels.
- Augmentation: multi-scale training for ResNet-50-based models; no test-time augmentation.
- Synthetic data: none reported.
- Leakage checks: not reported.
- License: not reported in extracted text.

### Evaluation

- Protocol: 5-fold cross-validation.
- Model evaluation metrics: [[Average precision]], [[mAP@0.50]], AP75, APS, APM, APL, [[GFLOPs]], parameters, and [[FPS]].
- Primary metric: [[Average precision]].
- Metric direction / units: higher is better for AP, AP50, AP75, APS, APM, APL, and FPS; lower is better for parameters and FLOPs when measuring efficiency.
- Baselines: Faster R-CNN, Cascade R-CNN, RetinaNet, FCOS, ATSS, GFL, YOLOv5-m, YOLOX-m, Swin-T, PVT-S, ScalableViT-S, and UniFormer-Sh14.
- Benchmarks: [[SSGD benchmark]].
- Statistical tests: not reported.

## Evidence

### Experimental Setup

- Dataset: [[SSGD]].
- Splits: 5-fold cross-validation over Part I and Part II.
- Baselines: CNN- and Transformer-based object detectors.
- Metrics: [[Average precision]], [[mAP@0.50]], AP75, APS, APM, APL, [[GFLOPs]], and [[FPS]].
- Hardware: single NVIDIA RTX 3090 GPU for FLOPs and FPS testing.
- Training time: not reported.
- Inference cost: FLOPs and FPS reported per model.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best Part I ResNet-50 detector | [[SSGD]] / [[Smartphone screen glass defect detection]] | AP | higher | not reported | 22.3 | ATSS. |
| Best Part II Table 1 detector | [[SSGD]] / [[Smartphone screen glass defect detection]] | AP | higher | not reported | 27.8 | YOLOv5-m. |
| ATSS Part II | [[SSGD]] / [[Smartphone screen glass defect detection]] | AP50 / AP75 | higher | not reported | 52.8 / 26.4 | Best AP50 and AP75 among ResNet-50-based Table 1 methods. |
| Best Transformer Part I | [[SSGD]] / [[Smartphone screen glass defect detection]] | AP | higher | not reported | 21.2 | ScalableViT-S with Faster R-CNN. |
| Best Transformer Part II | [[SSGD]] / [[Smartphone screen glass defect detection]] | AP | higher | not reported | 27.0 | Swin-T with Faster R-CNN. |
| Transformer speed example | [[SSGD]] / [[Smartphone screen glass defect detection]] | [[FPS]] | higher | ResNet-50 Faster R-CNN: 26.2 | Swin-T Faster R-CNN: 18.1 | The paper emphasizes Transformer speed limits at 1500 x 1000 resolution. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] | Object detection accuracy | AP percentage-like score | higher | yes | Tables report AP, AP50, AP75, APS, APM, and APL. |
| [[mAP@0.50]] | Object detection at IoU 0.50 | AP50 | higher | no | Reported as AP50. |
| AP75 | Object detection at IoU 0.75 | AP75 | higher | no | No dedicated graph note exists. |
| [[GFLOPs]] | Computational cost | billions of floating-point operations | lower | no | Reported per model. |
| [[FPS]] | Inference throughput | images per second | higher | no | Tested on one RTX 3090 GPU. |

### Ablations

- Not applicable; the paper benchmarks existing detectors rather than isolating a proposed model component.

## Dataset / Benchmark Details

- Source: smartphone touch-screen glass samples with production defects.
- Collection: industrial line-scan camera on calibrated fixed workstations.
- Annotation: LabelMe XML bounding boxes.
- Size: 2504 images.
- Categories: crack, broken, spot, scratch, light-leakage, blot, broken-membrane.
- Part I: 1258 images; category counts include crack 988, broken 304, spot 175, scratch 99, light-leakage 63, blot 18, broken-membrane 10.
- Part II: 1246 images; category counts include crack 787, broken 756, spot 467, scratch 163, light-leakage 60, blot 13, broken-membrane 11.
- Object sizes: Part I includes 241 small, 378 medium, and 1038 large objects; Part II includes 783 small, 441 medium, and 1033 large objects.
- Artifact: https://github.com/VincentHancoder/SSGD.
- License: not reported.
- Bias / coverage: samples come from two workstations; blot and broken-membrane categories are rare.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Transformer detectors are slower than CNN counterparts for the high-resolution input required by the dataset.
- Inferred: rare categories such as blot and broken-membrane may make category-specific evaluation unstable.
- Inferred: the paper reports public availability but does not state a dataset license in the extracted text.
- Inferred: collection from two workstations may leave open how models generalize to other screen-glass production lines or capture systems.

## Reproducibility

- Code: https://github.com/VincentHancoder/SSGD.
- Data: https://github.com/VincentHancoder/SSGD.
- Hyperparameters: 2x schedules for ResNet-50 and Transformer models; 100 epochs for YOLO series; batch sizes and input resizing settings are reported.
- Random seeds: not reported.
- Environment: MMDetection for most experiments; official YOLOv5 and YOLOX repositories for those models.
- Checkpoints / models: not reported.
- Exact preprocessing: resolution standardized to 1500 x 1000 pixels.
- Artifact status: dataset and code reported available on GitHub.

## Connections

### Graph Hubs

- Tasks: [[Smartphone screen glass defect detection]]
- Datasets: [[SSGD]], [[DeepPCB]], [[HRIPCB]], [[GC10-DET]], [[CSDD]]
- Methods: [[Deep convolutional neural network]], [[Vision Transformer]], [[YOLOv5]]
- Metrics: [[Average precision]], [[mAP@0.50]], [[GFLOPs]], [[FPS]]
- Domains: [[Glass inspection]], [[Semiconductor and electronics]], [[Industrial visual inspection]]
- Benchmarks: [[SSGD benchmark]]

### Builds On

- not reported.

### Contrasts With

- [[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]]: both are electronics manufacturing defect datasets, but SSGD targets smartphone screen glass and high-resolution object detection, while HRIPCB targets printed circuit board defects.
- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]]: both benchmark defect detectors with detection metrics and speed, but SSGD addresses screen glass rather than PCB inspection.
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]: both introduce public surface-defect detection datasets and detector baselines, but SSGD's domain is smartphone glass rather than metal surfaces.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]: both include AP-style detection metrics and detector baselines, but CSDD focuses on casting surfaces and segmentation while SSGD focuses on screen glass bounding boxes.

### Shares Dataset

- [[SSGD]]: introduced by this paper.

### Shares Task

- [[Smartphone screen glass defect detection]]: the dataset and benchmark target this task.

### Shares Method

- [[Deep convolutional neural network]]: CNN detectors form the main baseline group.
- [[Vision Transformer]]: Transformer backbones are evaluated under Faster R-CNN.
- [[YOLOv5]]: YOLOv5-m is one of the reported baselines.

### Shares Metric

- [[Average precision]], [[mAP@0.50]], [[GFLOPs]], and [[FPS]] are used in the benchmark tables.

### Application / Domain

- [[Glass inspection]]: the dataset targets touch-screen glass defects.
- [[Semiconductor and electronics]]: smartphone screen inspection belongs to electronics manufacturing quality control.
- [[Industrial visual inspection]]: the paper frames the work as automated production-line inspection.

### Follow-Up Reading

- [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]]: useful for comparing another electronics inspection dataset with speed-sensitive detection.
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]]: useful for AP-style industrial surface-defect benchmark design.

## Questions

- What license applies to SSGD and its code release?
- How do the models perform per defect category, especially rare blot and broken-membrane classes?
- How well do models trained on the two reported workstations generalize to other screen-glass production lines?
