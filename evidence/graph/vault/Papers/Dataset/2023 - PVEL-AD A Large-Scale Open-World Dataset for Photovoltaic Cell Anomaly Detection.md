---
title: "PVEL-AD: A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection"
aliases:
  - "PVEL-AD"
paper_key: "doi:10.1109/tii.2022.3162846"
paper_type: dataset
year: 2023
venue: "IEEE Transactions on Industrial Informatics"
authors:
  - "Binyi Su"
  - "Zhong Zhou"
  - "Haiyong Chen"
status: processed
processed_at: 2026-05-29
topics:
  - photovoltaic cell anomaly detection
  - electroluminescence inspection
  - object detection benchmark
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
application_area: "Photovoltaic cell manufacturing quality inspection"
datasets:
  - "[[PVEL-AD]]"
dataset_sizes:
  - "36,543 near-infrared EL images"
  - "37,380 bounding boxes for eight defect types"
  - "11,351 anomaly-free images"
  - "21,044 defective images with box-wise annotations"
  - "4,148 defective images with category annotations"
splits:
  - "Training and testing distributions are shown for anomaly detection; exact split counts per class are in the paper tables."
modalities:
  - "near-infrared electroluminescence images"
methods:
  - "[[F-labelImg]]"
model_family:
  - object detection
architectures:
  - "[[YOLOv5]]"
  - "Faster RPAN-CNN"
  - "EfficientDet"
  - "BAF-Detector"
losses:
  - focal loss
training_regime: "Supervised object detection with transfer learning and data augmentation."
augmentation:
  - horizontal flipping
  - random resize/place/crop/distort
synthetic_data: "The paper suggests using anomaly-free images for GAN-based anomaly generation, but does not evaluate synthetic augmentation as a main result."
metrics:
  - "[[Average precision]]"
  - "[[mAP]]"
  - "[[IoU]]"
  - "[[mIoU]]"
  - "[[FPS]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "AP is computed from precision, recall, and IoU; AP50:5:95 averages IoU thresholds from 50% to 95% in 5% steps."
baselines:
  - "Faster RPAN-CNN"
  - "YOLOv5-s/m/l"
  - "EfficientDet-D0/D1/D2/D3"
  - "BAF-Detector"
benchmarks:
  - "[[PVEL-AD benchmark]]"
evaluation_protocol: "Benchmark object detection methods on PVEL-AD using AP, mAP, parameter count, and FPS on a 24 GB RTX 3090."
parameters: "YOLOv5-l has 50.3M parameters; EfficientDet-D0 has 3.9M parameters."
compute: "24 GB RTX 3090 GPU"
hardware: "24 GB RTX 3090 GPU"
training_time: "not reported"
inference_cost: "YOLOv5-s reaches 111.11 FPS; YOLOv5-l reaches 62.03 FPS for the reported linear-crack AP50 result."
url: "https://doi.org/10.1109/TII.2022.3162846"
pdf: "paper-inbox/10_processed/Dataset/2023 - Su - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection.pdf"
code: "https://github.com/binyisu/PVEL-AD"
data: "IEEE DataPort DOI:10.21227/pz6t-3s77; https://www.kaggle.com/competitions/pvelad"
doi: "10.1109/tii.2022.3162846"
arxiv: not reported
related_papers:
  - "[[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]]"
  - "[[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]"
  - "[[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[F-labelImg]]"
  - "[[YOLOv5]]"
related_datasets:
  - "[[PVEL-AD]]"
  - "[[EL-2019]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[PVEL-AD benchmark]]"
concept_notes_created_or_updated:
  - "[[PVEL-AD]]"
  - "[[PVEL-AD benchmark]]"
  - "[[F-labelImg]]"
source_file: "paper-inbox/10_processed/Dataset/2023 - Su - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Su - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Su - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection.txt"
artifact_status: "Public dataset and code links reported by the paper."
tags:
  - paper
  - dataset
  - photovoltaics
---

# PVEL-AD: A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection

## Summary

- The paper introduces [[PVEL-AD]], a public photovoltaic-cell electroluminescence anomaly dataset with 36,543 near-infrared images, ten anomalous categories, and 37,380 bounding boxes for eight defect types.
- The dataset is collected from real-world industrial polycrystalline solar-cell manufacturing rather than a laboratory setting.
- The paper provides an initial [[PVEL-AD benchmark]] using Faster RPAN-CNN, YOLOv5, EfficientDet, and BAF-Detector, and reports that no detector dominates across all metrics or defect categories.

## Paper Type

- Type: dataset and benchmark paper.
- Why: the core contribution is a public dataset with annotations, an annotation workflow, and baseline object-detection results.

## Problem

- Task: [[Solar cell defect detection]] in photovoltaic-cell electroluminescence images.
- Setting: industrial solar-cell production using near-infrared EL imaging.
- Inputs: 1024 x 1024 near-infrared EL images of polycrystalline PV cells.
- Outputs: defect class labels and bounding boxes for detected anomalies.
- Motivation: small private EL datasets and limited public annotations make fair comparison of photovoltaic defect detectors difficult.
- Assumptions: EL imaging can reveal internal solar-cell anomalies that ordinary optical or infrared cameras cannot directly capture.

## Contribution

- Claimed: [[PVEL-AD]] is the first public PV solar-cell anomaly-detection dataset with box-wise ground truth.
- Claimed: the dataset supports anomaly detection, few-shot detection, one-class classification, and anomaly generation.
- Claimed: [[F-labelImg]] reduces annotation workload while preserving high-quality bounding boxes.
- Shown: PVEL-AD contains 36,543 high-resolution images, 11,351 anomaly-free images, 21,044 defective images with box-wise annotations, and 4,148 defective images with category annotations.
- Shown: YOLOv5-l reaches 51.13% mAP50:5:95; YOLOv5-s reaches 111.11 FPS; BAF-Detector and EfficientDet-D3 lead on some individual defect categories.
- Inferred: the paper is primarily a benchmark-enabling dataset contribution rather than a new detector architecture paper.

## Method

- Core idea: collect and release a large open-world PV cell EL anomaly dataset from an industrial manufacturing process, then benchmark representative object detectors.
- Architecture / algorithm: dataset construction, semiautomatic annotation via [[F-labelImg]], and supervised detector benchmarking.
- Objective / loss: object detection losses are architecture-specific; EfficientDet uses focal loss. The exact loss configuration for all baselines is not fully reported in the extracted text.
- Optimization: transfer learning from ImageNet-pretrained backbones and detector-specific training settings.
- Training data: PVEL-AD training split with horizontal-flip augmentation and random resize/place/crop/distort augmentation.
- Data pipeline: PV cells are excited with 24-V DC voltage and 8-A current in a dark-room EL acquisition subsystem; a cooled Si-CCD camera captures near-infrared emission around 1000-1200 nm.
- Augmentation / synthesis: horizontal flipping before training and random augmentation during training; anomaly generation is discussed as a dataset application.
- Inference: object detectors predict defect class and position; YOLOv5 uses test-time augmentation.
- Complexity / deployment constraints: EL acquisition requires electrical contact, which the authors identify as a risk to solar cells.

## ML / DL Extraction

### Task Formulation

- Input modality: near-infrared electroluminescence images.
- Output target: defect bounding boxes and defect categories for anomaly detection; image category labels for defects not suitable for object detection.
- Supervision: supervised object detection with box annotations for eight defect types; anomaly-free images also support one-class classification.
- Objective: detect and localize photovoltaic-cell defects under open-world manufacturing variability.

### Model And Training

- Model family: object detection.
- Architecture: Faster RPAN-CNN, YOLOv5-s/m/l, EfficientDet-D0/D1/D2/D3, and BAF-Detector.
- Parameters: YOLOv5-l has 50.3M parameters; EfficientDet-D0 has 3.9M parameters.
- Pretraining: ImageNet-pretrained networks are used for transfer learning.
- Fine-tuning: detectors are trained on PVEL-AD with architecture-specific settings.
- Losses: focal loss is reported for EfficientDet; other losses are not fully reported.
- Optimizer: not reported.
- Hyperparameters: YOLOv5 batch size 8 and 300 epochs; EfficientDet batch size 8 and 300 epochs; Faster RPAN-CNN and BAF-Detector use 40,000 max iterations with 600 x 600 resized inputs.
- Seeds: not reported.
- Training compute: 24 GB RTX 3090 GPU.

### Data

- Datasets: [[PVEL-AD]].
- Data source: practical industrial manufacturing of polycrystalline solar cells.
- Dataset size: 36,543 high-resolution images; 37,380 box annotations for eight defect types.
- Labels / annotations: one defect-free type, ten anomalous categories, bounding boxes for linear crack, star crack, finger interruption, black core, thick line, scratch, fragment, and corner; category-only annotations for misalignment and material anomalies.
- Splits: the paper shows train/test distributions for anomaly detection; exact table cells are not preserved in the extracted text.
- Preprocessing: input resizing is detector-specific; YOLOv5 uses test-time augmentation.
- Augmentation: horizontal flipping, random resize/place/crop/distort, and detector-specific augmentation.
- Synthetic data: not used as a primary benchmark method; anomaly generation is presented as a possible dataset application.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: compare object detectors on PVEL-AD using AP, mAP, model size, and FPS.
- Used performance metrics: [[Average precision]], [[mAP]], [[IoU]], [[FPS]], and [[mIoU]] for annotation similarity.
- Primary metric: [[mAP]].
- Metric definitions: AP is computed over precision-recall curves and IoU thresholds; mAP is the mean AP over classes.
- Metric direction / units: AP/mAP/mIoU/FPS are higher-is-better; FPS is frames per second.
- Baselines: Faster RPAN-CNN, YOLOv5, EfficientDet, and BAF-Detector.
- Benchmarks: [[PVEL-AD benchmark]].
- Statistical tests: not reported.
- Failure cases: small linear cracks near PV-cell edges and heterogeneous background interference are difficult.

## Evidence

### Experimental Setup

- Datasets: [[PVEL-AD]].
- Splits: train/test distributions are used for anomaly detection; exact counts per split are in the paper figures/tables but not preserved in the text extraction.
- Baselines: Faster RPAN-CNN, YOLOv5-s/m/l, EfficientDet-D0/D1/D2/D3, and BAF-Detector.
- Used performance metrics: AP50:5:95, AP50, AP75, mAP, parameter count, FPS, mIoU for annotation comparison.
- Compute: 24 GB RTX 3090 GPU.
- Hardware: 24 GB RTX 3090 GPU.
- Training time: not reported.
- Inference cost: YOLOv5-s reports 111.11 FPS; YOLOv5-l reports 62.03 FPS in the per-anomaly discussion.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best overall detector in prose | [[PVEL-AD]] / [[Solar cell defect detection]] | [[mAP]]50:5:95 | higher | not reported | 51.13% | YOLOv5-l; table cells for all baselines were not preserved in extraction. |
| Fastest detector in prose | [[PVEL-AD]] / object detection | [[FPS]] | higher | not reported | 111.11 | YOLOv5-s. |
| Lightweight detector note | [[PVEL-AD]] / object detection | parameters and [[FPS]] | fewer / higher | not applicable | 3.9M and 83.33 FPS | EfficientDet-D0 has the fewest parameters but is not fastest. |
| Linear crack result | [[PVEL-AD]] / linear crack detection | AP50 | higher | not reported | 66.04% | YOLOv5-l; linear cracks are difficult because many are small and near cell edges. |
| Black core result | [[PVEL-AD]] / black core detection | AP50 | higher | not reported | 98.25% | BAF-Detector. |
| Finger interruption result | [[PVEL-AD]] / finger interruption detection | AP50 | higher | not reported | 94.24% | BAF-Detector. |
| Thick line result | [[PVEL-AD]] / thick line detection | AP50 | higher | not reported | 72.71% | EfficientDet-D3. |
| Annotation speed / similarity | 1000 defective images with 1536 anomalies | [[mIoU]] | higher | manual labelImg | 99.13% | F-labelImg versus manual labelImg; F-labelImg took about half an hour versus about one and a half hours. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] | Per-class object detection | Area under precision-recall curve at one or more IoU thresholds | higher | yes | Reported as AP50:5:95, AP50, and AP75. |
| [[mAP]] | Multi-class defect detection | Mean AP over classes | higher | yes | YOLOv5-l reaches 51.13% mAP50:5:95. |
| [[IoU]] | Bounding-box overlap | Intersection over union | higher | no | Used to compute AP and mIoU. |
| [[mIoU]] | Annotation-tool comparison | Mean intersection over union | higher | no | F-labelImg reaches 99.13% similarity to manual labelImg on the evaluation sample. |
| [[FPS]] | Inference throughput | Frames per second | higher | no | YOLOv5-s reaches 111.11 FPS. |

### Ablations

- The paper does not report ablations in the extracted text. It compares detector families and model scales, including EfficientDet-D0 through D3 and YOLOv5-s through YOLOv5-l.

## Dataset / Benchmark Details

- Source: real-world industrial solar-cell production lines.
- Collection: near-infrared EL imaging of polycrystalline solar cells using a cooled Si-CCD camera and dark-room acquisition system.
- Annotation: expert-assisted bounding boxes; [[F-labelImg]] uses a pretrained YOLOv5 detector to propose boxes, then annotators fine-tune, delete, or add boxes.
- Size: 36,543 images, including 11,351 anomaly-free images and 25,192 defective images.
- Splits: training/testing distribution is shown for anomaly detection; exact split table values are not preserved in the extraction.
- Modalities: 1024 x 1024 near-infrared EL imagery.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: limited to polycrystalline solar cells and EL imaging; defect distribution is long-tailed.
- Maintenance: authors state that more expert-annotated samples will be collected in the future.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: EL imaging requires electrical contacts, which adds risk to the solar cell.
- Stated: photoluminescence imaging is suggested as a noncontact alternative.
- Stated: when training samples are small, [[F-labelImg]] can degenerate into ordinary labelImg because overfitting may cause the detector to fail.
- Inferred: the benchmark is limited to CNN/object-detection baselines available at the time; exact table values for all baselines are not available in the text extraction.

## Reproducibility

- Code: https://github.com/binyisu/PVEL-AD.
- Data: IEEE DataPort DOI:10.21227/pz6t-3s77 and Kaggle competition URL are reported.
- Hyperparameters: partially reported for YOLOv5, EfficientDet, Faster RPAN-CNN, and BAF-Detector.
- Random seeds: not reported.
- Environment: 24 GB RTX 3090 GPU; software stack not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: detector-specific resizing and augmentations are partially reported.
- Artifact status: public dataset and code links are reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[F-labelImg]], [[YOLOv5]]
- Datasets: [[PVEL-AD]], [[EL-2019]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Average precision]], [[mAP]], [[IoU]], [[mIoU]], [[FPS]]

### Builds on

- [[EL-2019]]: the paper positions PVEL-AD as larger and more diverse than the earlier EL image dataset, with box-wise annotations.

### Contrasts with

- [[MVTec AD]]: PVEL-AD is domain-specific to photovoltaic EL inspection and collected from real manufacturing, while MVTec AD is a general industrial anomaly dataset.

### Shares dataset

- not applicable.

### Shares task

- [[Solar cell defect detection]]: the dataset and benchmark target photovoltaic-cell anomaly detection and localization.
- [[Defect classification]]: misalignment and material anomalies are described as better suited to image classification than object detection.

### Shares method

- [[YOLOv5]]: used both for F-labelImg initialization and as a benchmark detector.
- [[F-labelImg]]: introduced as the semiautomatic annotation method for PVEL-AD.

### Shares metric

- [[Average precision]], [[mAP]], [[IoU]], [[mIoU]], and [[FPS]]: used for detector evaluation, annotation similarity, or throughput.

### Application/domain

- [[Solar cells and photovoltaic]]: PVEL-AD is collected from PV-cell manufacturing EL inspection.

### Follow-up reading

- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]: related photovoltaic EL defect detection work.
- [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]]: later solar-cell detector evaluation.

## Questions

- What license and access constraints apply to the IEEE DataPort, GitHub, and Kaggle versions?
- What exact train/test split counts are used for each defect category in the benchmark tables?
- How do newer detectors and anomaly-generation methods perform on the long-tailed PVEL-AD classes?
- Can noncontact photoluminescence imaging reproduce the same benchmark behavior without electrical-contact risk?
