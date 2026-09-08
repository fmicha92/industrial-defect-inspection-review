---
title: "Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment"
aliases:
  - "Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0"
paper_key: "doi:10.37391/ijeer.130411"
paper_type: research
year: 2025
venue: "International Journal of Electrical and Electronics Research"
authors:
  - "Mosbah Laouamer"
  - "Mohammed Adaika"
  - "Souhaib Remha"
  - "Abdelkader Mahmoudi"
  - "Hamza Adaika"
status: processed
processed_at: 2026-06-11
topics:
  - "PV surface fault classification"
  - "CNN benchmarking"
  - "data augmentation"
tasks:
  - "[[Solar panel classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
application_area: "RGB photovoltaic surface inspection"
datasets:
  - "[[PV Panel Defect Dataset]]"
dataset_sizes:
  - "1,574 RGB images across six classes"
splits:
  - "five-fold cross-validation"
modalities:
  - "RGB photovoltaic panel images"
methods:
  - "[[Data augmentation]]"
model_family:
  - "convolutional neural networks"
architectures:
  - "[[ResNet50]]"
  - "[[EfficientNet]]"
  - "[[MobileNet]]"
  - "DenseNet121"
losses:
  - "categorical cross-entropy"
optimizers:
  - "[[Adam]]"
training_regime: "supervised transfer learning with five-fold cross-validation"
augmentation:
  - "random rotation"
  - "horizontal flipping"
  - "vertical flipping"
  - "zoom scaling"
  - "brightness variation"
  - "Gaussian noise perturbation"
synthetic_data: "not applicable; uses classical augmentation, not generative synthesis"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "macro-averaged F1-score is emphasized in the abstract"
baselines:
  - "ResNet50"
  - "EfficientNetB0"
  - "MobileNetV3Small"
  - "DenseNet121"
benchmarks: []
evaluation_protocol: "same preprocessing, training, validation settings and five-fold cross-validation across four CNN architectures"
parameters: "ResNet50 about 25.6M; EfficientNetB0 about 5.3M; MobileNetV3Small about 2.5M; DenseNet121 about 7.2M"
compute: "not reported"
hardware: "not reported"
training_time: "reported comparatively; exact extracted values not used as primary evidence"
inference_cost: "real-time GUI deployment demonstrated; latency not reported"
url: "https://ijeer.forexjournal.co.in/archive/volume-13/ijeer-130411.html"
pdf: "paper-inbox/10_processed/Research/2025 - Laouamer - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment.pdf"
code: "not reported"
data: "Kaggle PV Panel Defect Dataset"
doi: "10.37391/ijeer.130411"
arxiv: "not applicable"
related_papers:
  - "[[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]]"
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
related_concepts:
  - "[[Data augmentation]]"
related_methods:
  - "[[Data augmentation]]"
  - "[[ResNet50]]"
  - "[[EfficientNet]]"
  - "[[MobileNet]]"
related_datasets:
  - "[[PV Panel Defect Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar panel classification]]"
  - "[[Defect classification]]"
related_benchmarks: []
concept_notes_created_or_updated: []
source_file: "paper-inbox/10_processed/Research/2025 - Laouamer - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Laouamer - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Laouamer - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment.txt"
artifact_status: "code not reported; dataset public on Kaggle"
tags:
  - paper
---

# Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0 with Real-Time Deployment

## Summary

- The paper benchmarks ResNet50, EfficientNetB0, MobileNetV3Small, and DenseNet121 for six-class RGB PV surface fault classification.
- The dataset is [[PV Panel Defect Dataset]], with 1,574 RGB images and augmentation applied to the training data.
- DenseNet121 is reported as the best classifier with 96% accuracy and 0.96 F1-score; ResNet50 reaches 93.68% test accuracy, EfficientNetB0 92.63%, and MobileNetV3Small about 92%.

## Paper Type

- Type: research.
- Why: it reports a comparative supervised CNN evaluation and a real-time GUI deployment prototype.

## Problem

- Task: classify PV panel surface condition into clean, dust, bird-drop, snow-covered, electrical-damage, and physical-damage classes.
- Setting: RGB image analysis for PV inspection.
- Inputs: visible-light RGB PV panel images.
- Outputs: six-class surface-fault label.
- Motivation: manual PV inspection is inefficient for large solar farms.
- Assumptions: data augmentation and five-fold cross-validation improve robustness for a moderate-size dataset.

## Contribution

- Claimed: reproducible benchmark of four CNN architectures under identical preprocessing and validation.
- Shown: DenseNet121 has the strongest extracted macro F1 and accuracy; compact models trade lower accuracy for faster convergence and deployment suitability.
- Inferred: the augmentation contribution is not isolated by a no-augmentation baseline in the extracted results, so the note treats augmentation as part of the training protocol rather than a proven standalone improvement.

## Method

- Core idea: use transfer-learning CNNs with shared preprocessing and augmentation for PV surface fault classification.
- Architecture / algorithm: ResNet50, EfficientNetB0, MobileNetV3Small, DenseNet121.
- Objective / loss: categorical cross-entropy.
- Optimization: Adam is reported.
- Training data: [[PV Panel Defect Dataset]] RGB images.
- Data pipeline: resize/preprocess images, augment training samples, train across five folds, report class-wise and macro metrics.
- Augmentation / synthesis: rotation, flips, zoom, brightness variation, Gaussian noise.
- Inference: trained models integrated into GUI for real-time PV fault classification.
- Complexity / deployment constraints: MobileNetV3Small and EfficientNetB0 are framed as more suitable for lightweight deployment; deeper models score higher.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB panel image.
- Output target: six-class fault label.
- Supervision: supervised class labels.
- Objective: multi-class PV surface fault classification.

### Model And Training

- Model family: CNN transfer learning.
- Architecture: ResNet50, EfficientNetB0, MobileNetV3Small, DenseNet121.
- Parameters: about 25.6M, 5.3M, 2.5M, and 7.2M respectively.
- Pretraining: transfer learning is used; exact pretrained source not fully extracted for every model.
- Fine-tuning: yes.
- Losses: categorical cross-entropy.
- Optimizer: Adam.
- Hyperparameters: not fully extracted.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[PV Panel Defect Dataset]].
- Data source: Kaggle, compiled by Alicja Lenarczyk.
- Dataset size: 1,574 images.
- Labels / annotations: six surface classes.
- Splits: five-fold cross-validation; augmentation is applied to training data only.
- Preprocessing: not fully extracted.
- Augmentation: random rotation, horizontal and vertical flipping, zoom scaling, brightness variation, Gaussian noise perturbation.
- Synthetic data: not applicable.
- Leakage checks: training-only augmentation is stated; no separate leakage audit reported.
- License: see dataset note.

### Evaluation

- Protocol: same dataset partitions and training/validation settings for four CNNs.
- Used performance metrics: accuracy, precision, recall, F1-score, confusion matrices, ROC curves.
- Primary metric: macro F1-score.
- Metric definitions: standard classification metrics.
- Metric direction / units: higher is better.
- Baselines: each architecture is a comparator; no no-augmentation baseline is reported in the extracted text.
- Benchmarks: [[PV Panel Defect Dataset]].
- Statistical tests: not reported.
- Failure cases: some confusion between visually similar fault classes is discussed.

## Evidence

### Experimental Setup

- Datasets: [[PV Panel Defect Dataset]].
- Splits: five-fold cross-validation.
- Baselines: ResNet50, EfficientNetB0, MobileNetV3Small, DenseNet121.
- Used performance metrics: accuracy, precision, recall, F1-score.
- Compute: not reported.
- Hardware: not reported.
- Training time: compared qualitatively.
- Inference cost: GUI deployment shown; latency not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best model | PV surface fault classification | Accuracy | higher | ResNet50 93.68% | DenseNet121 96% | DenseNet121 also reports F1 = 0.96. |
| Efficient model | PV surface fault classification | Accuracy | higher | EfficientNetB0 92.63% | MobileNetV3Small about 92% | Compact models are framed as deployment-friendly. |
| Macro comparison | PV surface fault classification | F1-score | higher | ResNet50 0.93; EfficientNetB0 0.92; MobileNetV3Small 0.92 | DenseNet121 0.96 | Extracted from abstract and results discussion. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | test and validation classification | percent correct | higher | no | DenseNet121 reaches 96%. |
| [[F1-score]] | macro and class-wise evaluation | harmonic mean | higher | yes | DenseNet121 reaches 0.96. |
| [[Precision]] | class-wise evaluation | fraction of predicted positives correct | higher | no | Tables report per class. |
| [[Recall]] | class-wise evaluation | fraction of actual positives found | higher | no | Tables report per class. |

### Ablations

- Architecture comparison is the primary ablation.
- No extracted no-augmentation baseline is available, so augmentation is not treated as independently proven.

## Dataset / Benchmark Details

- Source: Kaggle [[PV Panel Defect Dataset]].
- Collection: open-source RGB PV surface images.
- Annotation: six class labels.
- Size: 1,574 RGB images.
- Splits: five-fold cross-validation.
- Modalities: RGB images.
- License: see dataset note.
- Leakage risks: no explicit leakage audit.
- Bias / coverage: moderate dataset size; extracted text states this remains a limitation even after x5 augmentation.
- Maintenance: not reported.

## Limitations

- Stated: dataset remains moderate in size despite augmentation.
- Stated: RGB-only imagery excludes thermal/IR and EL modalities.
- Inferred: augmentation is not isolated from architecture and training protocol in the extracted baseline comparisons.

## Reproducibility

- Code: not reported.
- Data: Kaggle dataset.
- Hyperparameters: partially reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: partially reported.
- Artifact status: dataset available, code unavailable in extracted text.

## Connections

### Graph Hubs

- Tasks: [[Solar panel classification]], [[Defect classification]].
- Methods: [[Data augmentation]], [[ResNet50]], [[EfficientNet]], [[MobileNet]].
- Optimizers: [[Adam]].
- Datasets: [[PV Panel Defect Dataset]].
- Benchmarks: not reported.
- Domains: [[Solar cells and photovoltaic]].
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]].
- Concepts: transfer learning, real-time GUI deployment.
- Dataset-domain links: [[PV Panel Defect Dataset]] is associated with [[Solar cells and photovoltaic]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] | Shares dataset | Uses the same Kaggle PV Panel Defect Dataset family. |
| [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] | Shares dataset / contrasts with | Both use RGB PV panel classification; the later paper audits shortcut learning risks. |

### Backlinks Updated

- Pending graph audit.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| not applicable | not applicable | Existing dataset, method, task, and metric notes cover central graph links. |

## Questions

- Does the GUI code exist outside the article? Not reported.
- The no-augmentation baseline is not visible in the extracted text, so augmentation-specific improvement should not be claimed without manual table verification.
