---
title: "SolarDK: A high-resolution urban solar panel image classification and localization dataset"
aliases:
  - "SolarDK"
  - "SolarDK paper"
  - "SolarDK: A high-resolution urban solar panel image classification and localisation dataset"
paper_key: "sha256:12fae438f8e138b106917e3059bac1588e2da97e8824b53a7e1963a7c9ef80b7"
paper_type: "dataset"
year: 2022
venue: "Tackling Climate Change with Machine Learning workshop at NeurIPS 2022"
authors:
  - "Maxim Khomiakov"
  - "Mathias Bonde Sørensen"
  - "Julius Holbech Radzikowski"
  - "Carl Anton Schmidt"
  - "Mads Andersen"
  - "Michael Riis Andersen"
  - "Jes Frellsen"
status: "processed"
topics:
  - "solar panel mapping"
  - "aerial imagery"
  - "geographic generalization"
tasks:
  - "[[Solar panel classification]]"
  - "[[Solar panel localization]]"
  - "[[Urban semantic segmentation]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[SolarDK]]"
methods:
  - "[[ConvNeXt]]"
  - "[[EfficientNet]]"
  - "[[InceptionV3]]"
  - "[[ResNet50]]"
  - "[[DeepLabV3+]]"
model_family:
  - "[[Computer Vision Models]]"
  - "[[Segmentation Models]]"
architectures:
  - "[[ConvNeXt]]"
  - "[[EfficientNet]]"
  - "[[InceptionV3]]"
  - "[[ResNet50]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Cohen's kappa]]"
  - "[[mIoU]]"
primary_metric: "[[Cohen's kappa]]"
metric_definitions:
  - "Classification uses precision, recall, and Cohen's kappa."
  - "Segmentation uses precision, recall, and mean Intersection over Union."
baselines:
  - "ConvNeXt"
  - "EfficientNet-b5"
  - "EfficientNet-b7"
  - "InceptionV3"
  - "ResNet50"
  - "ResNet101"
  - "ResNet152"
  - "DeepSolarDE"
  - "DeepSolarDK"
benchmarks:
  - "[[SolarDK benchmark]]"
code: "not reported"
data: "https://osf.io/aj539/overview"
doi: "not reported"
arxiv: "2212.01260"
url: "https://arxiv.org/abs/2212.01260"
pdf: "paper-inbox/10_processed/Dataset/2022 - Khomiakov - SolarDK A high-resolution urban solar panel image classification and localization dataset.pdf"
source_file: "paper-inbox/10_processed/Dataset/2022 - Khomiakov - SolarDK A high-resolution urban solar panel image classification and localization dataset.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Khomiakov - SolarDK A high-resolution urban solar panel image classification and localization dataset.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Khomiakov - SolarDK A high-resolution urban solar panel image classification and localization dataset.txt"
related_papers:
  - "[[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]]"
related_concepts:
  - "[[Solar panel classification]]"
  - "[[Solar panel localization]]"
related_methods:
  - "[[ConvNeXt]]"
  - "[[EfficientNet]]"
  - "[[InceptionV3]]"
  - "[[ResNet50]]"
  - "[[DeepLabV3+]]"
related_datasets:
  - "[[SolarDK]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar panel classification]]"
  - "[[Solar panel localization]]"
  - "[[Urban semantic segmentation]]"
related_benchmarks:
  - "[[SolarDK benchmark]]"
processed_at: "2026-06-04"
---
# SolarDK: A high-resolution urban solar panel image classification and localization dataset

## Summary

The paper introduces [[SolarDK]], a public Danish aerial-imagery dataset for [[Solar panel classification]] and [[Solar panel localization]]. It provides manually labelled classification images, segmentation masks for positive examples, and a larger BBR-derived positive classification set from the Danish national building registry.

The paper's central benchmark finding is that geographic generalization remains difficult: DeepSolarDE performs poorly when run directly on SolarDK, but fine-tuning on SolarDK substantially improves classification and segmentation results.

## Paper Type

Dataset and benchmark paper. It introduces datasets, split definitions, evaluation scenarios, and baseline results for solar-panel classification and localization from aerial imagery.

## Problem

Remote sensing can help track residential solar adoption, but public benchmark datasets for PV arrays are limited and models trained in one geographic region can fail in another because imagery differs in ground sample distance, acquisition angle, time of day, and atmospheric conditions.

## Contribution

- Introduces [[SolarDK]], spanning Danish urban and national building-registry sources.
- Provides a manually labelled classification dataset from Gentofte and Herlev municipalities.
- Provides segmentation masks for the same positive manually labelled instances.
- Provides a BBR-derived positive classification set covering most variations of Danish urban and rural landscapes.
- Reports classification and segmentation baselines under three scenarios: out-of-domain pretrained models, BBR minority-class augmentation, and same-domain but different-geography fine-tuning.

## Method

SolarDK uses GeoDanmark aerial images with 10 cm to 15 cm variable ground sample distance, sampled between March 1 and May 1, 2021. The manually labelled classification data comes from Gentofte and Herlev municipalities in the Greater Copenhagen Region. Gentofte is used for training and validation; Herlev is used for testing.

Manual image labels were produced with Pigeon. Segmentation labels were produced with AI-assisted annotation software from Toronto Annotation Suite. The BBR set is derived from the Danish national building registry and contains positive PV examples across Denmark.

Classification baselines include ConvNeXt, EfficientNet-b5/b7, InceptionV3, ResNet50/101/152, DeepSolarDE inference, and DeepSolarDK. Segmentation baselines include ResNet-backed DeepLabV3+, FPN, PSPNet, DeepSolarDE inference, and DeepSolarDK.

## Evidence

### Dataset Composition

| Dataset | Negatives | Positives | Area |
|---|---:|---:|---:|
| Herlev | 7,048 | 398 | 12.07 km2 |
| Gentofte | 15,489 | 482 | 25.70 km2 |
| BBR | not applicable | 104,397 | 3,853.02 km2 |
| Total | 22,537 | 105,344 | 3,890.79 km2 |

### Manual Split

| Split | Negatives | Positives | Share |
|---|---:|---:|---:|
| Training | 10,376 | 323 | 46% |
| Validation | 5,113 | 159 | 22% |
| Test | 7,048 | 398 | 32% |
| Total | 22,537 | 880 | 100% |

### Classification Baselines

The paper reports classification precision, recall, and [[Cohen's kappa]]. ConvNeXt has the strongest out-of-domain ImageNet-pretrained block by kappa, with 0.60 +/- 0.04 recall, 0.79 +/- 0.03 precision, and 0.66 +/- 0.02 kappa. With BBR minority-class augmentation, ConvNeXt reports 0.65 +/- 0.07 recall, 0.70 +/- 0.06 precision, and 0.65 +/- 0.03 kappa. DeepSolarDE inference reports 0.42 recall, 0.17 precision, and 0.21 kappa, while DeepSolarDK reports 0.73 recall, 0.65 precision, and 0.67 kappa.

### Segmentation Baselines

The paper reports segmentation recall, precision, and [[mIoU]]. ResNet50-DeepLabV3Plus, ResNet50-FPN, and ResNet152-FPN each report 0.72 IoU in the out-of-domain segmentation block. DeepSolarDE inference reports 0.53 recall, 0.34 precision, and 0.51 IoU. DeepSolarDK reports 0.85 recall, 0.75 precision, and 0.62 IoU.

## ML/DL Extraction

- Task formulation: binary classification of whether a solar PV system exists in an aerial image, plus pixel-level localization of PV regions.
- Inputs: GeoDanmark aerial images from Denmark.
- Outputs: binary PV/no-PV labels and binary segmentation masks for PV pixels.
- Training data: Gentofte municipality training/validation images; optional BBR positive examples for classification minority-class augmentation.
- Test data: Herlev municipality.
- Models: ConvNeXt, EfficientNet-b5/b7, InceptionV3, ResNet50/101/152, DeepSolarDE, DeepSolarDK, DeepLabV3+, FPN, and PSPNet variants.
- Losses: binary cross entropy for classification and DICE loss for segmentation.
- Evaluation: [[Precision]], [[Recall]], [[Cohen's kappa]], and [[mIoU]] at a threshold of 0.5.
- Artifacts: OSF-hosted dataset is reported; code is not reported in the extracted paper text.

## Limitations

- Geographic generalization remains incomplete; models trained on a related German solar dataset perform poorly before SolarDK fine-tuning.
- The dataset does not include geospatial coordinates of images or PV systems due to privacy concerns.
- BBR metadata is only provided at municipal aggregation level.
- The paper calls for more annotated data across geographic regions to improve generalization.
- Hyperparameter and architecture comparisons are bounded to the reported baseline scenarios rather than an exhaustive search.

## Connections

### Graph Hubs

- Datasets: [[SolarDK]]
- Benchmarks: [[SolarDK benchmark]]
- Tasks: [[Solar panel classification]], [[Solar panel localization]], [[Urban semantic segmentation]]
- Domains: [[Solar cells and photovoltaic]]
- Methods: [[ConvNeXt]], [[EfficientNet]], [[InceptionV3]], [[ResNet50]], [[DeepLabV3+]]
- Metrics: [[Precision]], [[Recall]], [[Cohen's kappa]], [[mIoU]]

### Introduces Dataset

- [[SolarDK]]: the paper introduces the classification, segmentation, and BBR-derived SolarDK datasets and points to the OSF release.

### Introduces Benchmark

- [[SolarDK benchmark]]: the paper defines train/validation/test splits and reports classification and segmentation baselines.

### Shares Task

- [[Solar panel classification]]: predicts whether aerial imagery contains a PV system.
- [[Solar panel localization]]: segments pixels belonging to PV systems.
- [[Urban semantic segmentation]]: SolarDK's segmentation task is a solar-specific urban aerial-imagery segmentation problem.

### Application/Domain

- [[Solar cells and photovoltaic]]: the paper supports solar adoption mapping from aerial imagery, not PV defect inspection.

### Related Reading

- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] is another RGB-image solar-panel classification dataset paper, but it focuses on panel condition classes rather than aerial PV-system mapping.

## Questions

- Does the OSF archive include a fixed manifest with per-file checksums beyond OSF's per-part checksums?
- How sensitive are the baselines to exact image tiling around rooftops?
- Would models trained on SolarDK transfer to countries with different roof materials, solar-panel installation patterns, or aerial-imagery acquisition pipelines?
