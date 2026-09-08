---
title: "Anomaly Detection for Real-World Industrial Applications: Benchmarking Recent Self-Supervised and Pretrained Methods"
aliases:
  - "Anomaly Detection for Real-World Industrial Applications: Benchmarking Recent Self-Supervised and Pretrained Methods"
paper_key: "doi:10.1109/icumt57764.2022.9943437"
paper_type: benchmark
year: 2022
venue: "ICUMT"
authors:
  - "Stepan Jezek"
  - "Martin Jonak"
  - "Radim Burget"
  - "Pavel Dvorak"
  - "Milos Skotak"
status: processed
processed_at: 2026-05-22
topics:
  - "industrial anomaly detection benchmark"
  - "metal part defect detection"
  - "self-supervised anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[MPDD2]]"
methods:
  - "[[Self-supervised learning]]"
  - "[[Transfer learning]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[FastFlow]]"
  - "[[Natural Synthetic Anomalies]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures:
  - "ResNet-18"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUROC: area under the receiver operating characteristic curve, interpreted by the paper as the probability that a randomly selected anomalous sample receives a higher anomaly score than a randomly selected normal sample."
baselines:
  - "CutPaste"
  - "NSA"
  - "PatchCore"
  - "FastFlow"
  - "CFLOW-AD"
  - "PaDiM"
  - "CFA"
benchmarks:
  - "[[MPDD2]]"
  - "[[MVTec AD]]"
code: "not reported"
data: "available from https://github.com/stepanje/MPDD2 with a Google Drive download link"
doi: "10.1109/icumt57764.2022.9943437"
arxiv: "not reported"
url: "https://doi.org/10.1109/ICUMT57764.2022.9943437"
pdf: "not reported"
related_papers:
  - "[[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]]"
  - "[[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]]"
  - "[[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Self-supervised learning]]"
  - "[[Transfer learning]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[FastFlow]]"
  - "[[Natural Synthetic Anomalies]]"
related_datasets:
  - "[[MPDD2]]"
  - "[[MVTec AD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Metallic surface defect detection]]"
related_benchmarks:
  - "[[MPDD2]]"
  - "[[MVTec AD]]"
source_file: "paper-inbox/00_incoming/Anomaly_detection_for_real-world_industrial_applications_benchmarking_recent_self-supervised_and_pretrained_methods.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Jezek - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Jezek - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods.txt"
artifact_status: "dataset reported available"
tags:
  - paper
---
# Anomaly Detection for Real-World Industrial Applications: Benchmarking Recent Self-Supervised and Pretrained Methods

## Summary

Jezek et al. benchmark recent visual anomaly detection methods on a metal-parts fabrication dataset designed to differ from [[MVTec AD]] through fewer training samples and stronger pose, rotation, lighting, and acquisition variability. The benchmark compares ImageNet-pretrained feature extractors against feature extractors trained from scratch with self-supervised synthetic-anomaly tasks.

The strongest average result on the proposed dataset is CutPaste at 86.55% AUROC. NSA is second at 74.72% AUROC, while the best pretrained-feature method is FastFlow at 73.29% AUROC. The paper reports that self-supervised methods outperform pretrained-feature methods by 16.72 AUROC points on average, while average AUROC on the proposed dataset is 29.46 points lower than reported MVTec AD averages.

## Paper Type

- Type: benchmark.
- Why: The paper introduces a metal-parts anomaly detection dataset and uses it to compare recent anomaly detection methods under real-world industrial acquisition conditions.

## Problem

- Task: [[Industrial anomaly detection]] and [[Metallic surface defect detection]].
- Setting: painted metal parts fabrication, where acquisition can include limited samples, object pose/rotation variation, lighting changes, and motion blur.
- Inputs: images of non-defective and defective metal parts.
- Outputs: image-level anomaly scores for discriminating normal and anomalous samples.
- Motivation: [[MVTec AD]] is a high-quality industrial anomaly benchmark, but the paper argues it may not represent production cases with lower sample counts and higher acquisition noise.
- Assumptions: anomaly detection methods are trained with normal samples only; normal and anomalous samples are available for testing.

## Contribution

- Claimed: introduces a new dataset focused on detecting anomalies during metal parts fabrication.
- Claimed: compares recent state-of-the-art visual anomaly detection methods on that dataset.
- Shown: self-supervised feature extraction methods outperform ImageNet-pretrained feature extraction methods on the proposed dataset, reversing the pattern reported on MVTec AD.
- Shown: all evaluated methods have lower average AUROC on the proposed dataset than their reported MVTec AD averages.

## Method

The benchmark evaluates feature-extraction anomaly detection methods. All evaluated methods use a ResNet-18 feature extractor in the paper's setup. For pretrained methods, the feature extractor is initialized from ImageNet training; for self-supervised methods, the feature extractor is trained from scratch on a binary task that distinguishes normal images from synthetically augmented anomalous images.

Self-supervised training uses binary cross-entropy on normal samples and augmented samples. The paper discusses CutPaste, which pastes a random image patch at another location, and NSA, which creates more natural synthetic anomalies by blending patches with Poisson image editing. Pretrained-feature methods include PatchCore, FastFlow, CFLOW-AD, PaDiM, and CFA.

## Evidence

### Experimental Setup

- Dataset: [[MPDD2]].
- Classes: Bracket Brown, Bracket Grey, Bracket White, and Rosette.
- Training set: 385 normal images total.
- Test set: 96 normal images and 264 anomalous images total.
- Input preprocessing: all input images are resized to 256 x 256 pixels before evaluation.
- Evaluation protocol: methods train on normal images and are evaluated on labeled normal/anomalous test images.
- Metric: [[AU-ROC]].
- Baselines: CutPaste, NSA, PatchCore, FastFlow, CFLOW-AD, PaDiM, and CFA.
- Settings: every method is evaluated with default settings from its original publication.

### Dataset / Benchmark Details

| Class | Train normal | Test normal | Test defect |
|---|---:|---:|---:|
| Bracket Brown | 44 | 15 | 81 |
| Bracket Grey | 64 | 19 | 65 |
| Bracket White | 195 | 49 | 91 |
| Rosette | 82 | 13 | 27 |
| Total | 385 | 96 | 264 |

### Main Results

| Result | Dataset / Task | Metric | Direction | Best method | Paper result | Notes |
|---|---|---|---|---|---:|---|
| Best average on proposed dataset | [[MPDD2]] / [[Industrial anomaly detection]] | [[AU-ROC]] | higher | CutPaste | 86.55 | Best average across four classes. |
| Second-best average on proposed dataset | [[MPDD2]] / [[Industrial anomaly detection]] | [[AU-ROC]] | higher | NSA | 74.72 | Also self-supervised. |
| Best pretrained-feature method | [[MPDD2]] / [[Industrial anomaly detection]] | [[AU-ROC]] | higher | FastFlow | 73.29 | Best average among ImageNet-pretrained feature methods. |
| Self-supervised vs pretrained feature extractors | Method group averages | [[AU-ROC]] | higher | self-supervised methods | +16.72 points | The paper attributes the gain to better adaptation to the dataset. |
| Proposed dataset vs MVTec AD | Method averages | [[AU-ROC]] | higher | MVTec AD averages | +29.46 points | Methods generally score lower on the proposed dataset. |

### Per-Method AUROC

| Method | Bracket Brown | Bracket Grey | Bracket White | Rosette | Average | Reported MVTec AD average |
|---|---:|---:|---:|---:|---:|---:|
| CutPaste | 70.62 | 79.35 | 99.91 | 96.30 | 86.55 | 95.20 |
| NSA | 64.76 | 86.17 | 80.98 | 66.96 | 74.72 | 97.20 |
| PatchCore | 35.14 | 71.09 | 66.38 | 66.67 | 59.82 | 99.60 |
| FastFlow | 80.06 | 67.35 | 72.22 | 73.51 | 73.29 | 99.40 |
| CFLOW-AD | 24.44 | 74.74 | 74.19 | 86.89 | 65.07 | 98.26 |
| PaDiM | 52.82 | 32.41 | 79.12 | 37.03 | 50.35 | 97.90 |
| CFA | 36.66 | 79.90 | 90.90 | 76.62 | 71.02 | 99.50 |
| Class average | 52.07 | 70.14 | 80.53 | 72.00 | 68.69 | 98.15 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection on metal-part classes | Area under receiver operating characteristic curve; the paper interprets it as probability that an anomalous sample receives a higher anomaly score than a normal sample | Higher is better | yes | Average AUROC ranges from 50.35 for PaDiM to 86.55 for CutPaste on the proposed dataset. |

## ML / DL Extraction

### Task Formulation

- Input modality: visual inspection images of metal parts.
- Output target: binary normal/anomalous discrimination by anomaly score.
- Supervision: normal-only training; labeled normal and anomalous samples for testing.
- Objective: compare whether self-supervised feature extractors or ImageNet-pretrained feature extractors transfer better to a metal-parts anomaly detection dataset.

### Model And Training

- Feature extractor: ResNet-18 is used as the feature extractor for all evaluated methods.
- Pretrained-feature group: PatchCore, FastFlow, CFLOW-AD, PaDiM, and CFA.
- Self-supervised group: CutPaste and NSA.
- Self-supervised objective: binary cross-entropy for classifying normal samples versus synthetically augmented anomalous samples.
- Feature processing: extracted feature maps are processed according to each method, often by selecting layers 2 and 3 and vectorizing feature maps.
- Hyperparameters: default settings from the original method publications.
- Optimizer, seeds, hardware, and training time: not reported.

### Data

- Dataset: [[MPDD2]].
- Data source: metal parts fabrication.
- Split: normal-only training; normal and anomalous testing.
- Labels / annotations: normal/anomalous image labels are reported in the paper; the repository describes normal/anomalous validation samples.
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International, from the repository LICENSE file.
- Leakage checks: not reported.

### Evaluation

- Protocol: resize images to 256 x 256 pixels, train on normal images, compute anomaly scores on the test set, and report AUROC.
- Baselines: CutPaste, NSA, PatchCore, FastFlow, CFLOW-AD, PaDiM, and CFA.
- Statistical tests: not reported.
- Failure cases: Bracket Brown has the lowest average AUROC, which the paper attributes to greater position/rotation variation and fewer training samples; Bracket White has the highest class average and less position/rotation variation.

## Dataset / Benchmark Details

- Source: the paper footnote is OCR-rendered ambiguously, but the corresponding public repository is https://github.com/stepanje/MPDD2.
- Host availability: the repository is public and links a Google Drive download folder.
- Collection: metal parts fabrication images.
- Annotation: normal/anomalous image labels are reported.
- Size: 745 images total across the reported split.
- Host-reported size: more than 700 images.
- Classes: Bracket Brown, Bracket Grey, Bracket White, and Rosette.
- Modalities: visual images.
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International, from the repository LICENSE file.
- Bias / coverage: focused on metal parts fabrication; not intended to represent all industrial anomaly detection domains.
- Maintenance: not reported.

## Limitations

- The proposed dataset is narrower than broad industrial benchmarks and focuses on metal parts fabrication.
- Method implementations use default settings from prior publications, so the comparison may not reflect dataset-specific hyperparameter tuning.
- The paper reports image-level AUROC only in the extracted text; pixel-level localization metrics are not reported.
- Exact acquisition hardware, random seeds, and compute settings are not reported in the extracted text.

## Reproducibility

- Code: not reported.
- Data: available from https://github.com/stepanje/MPDD2; the repository links a Google Drive download folder.
- Hyperparameters: method defaults from the original publications.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: resize input images to 256 x 256 pixels.
- Artifact status: dataset reported available.

## Systems Details

- Hardware / software stack: not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: not reported.
- Deployment assumptions: production-like metal-parts inspection conditions with variable pose, rotation, lighting, and motion blur.
- Cost: not reported.
- Failure modes: high variation and low sample counts reduce AUROC on some classes.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Metallic surface defect detection]]
- Methods: [[Self-supervised learning]], [[Transfer learning]], [[Unsupervised anomaly detection]], [[FastFlow]], [[Natural Synthetic Anomalies]]
- Datasets: [[MPDD2]], [[MVTec AD]]
- Benchmarks: [[MPDD2]], [[MVTec AD]]
- Domains: [[Metal inspection]]
- Metrics: [[AU-ROC]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Deep Learning-Based Defect Detection of Metal Parts Evaluating Current Methods in Complex Conditions]] | Shares domain and dataset family | Both papers are by Jezek et al. and evaluate anomaly detection on metal-parts fabrication data under complex acquisition conditions. |
| [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] | Shares method | FastFlow is one of the pretrained-feature baselines and is the best pretrained method in this benchmark. |
| [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] | Shares method | NSA is a self-supervised synthetic-anomaly method and is the second-best average method in this benchmark. |

### Connection Rationale

- [[MPDD2]] is the central benchmark introduced and evaluated in the paper.
- [[MVTec AD]] is the comparison benchmark used to show that method rankings and absolute AUROC can change under more variable real-world conditions.
- [[Self-supervised learning]] is central because CutPaste and NSA outperform pretrained-feature methods in the reported average.
- [[Transfer learning]] is central because the competing group relies on ImageNet-pretrained feature extractors.
- [[Metal inspection]] is the supported domain because the dataset is restricted to metal parts fabrication.

## Questions

- Are segmentation masks available, or only image-level anomaly labels?
- Would method rankings change under tuned hyperparameters instead of original default settings?
- Which acquisition factors, such as rotation, lighting, or blur, contribute most to the lower AUROC relative to MVTec AD?
