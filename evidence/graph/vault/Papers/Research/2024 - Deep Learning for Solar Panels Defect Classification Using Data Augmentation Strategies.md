---
title: "Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies"
aliases:
  - "Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies"
paper_key: "sha256:d7a56694798d4b80a791b0b2cf1cb5cb69597987614fb938d31958a9cf0b89c5"
paper_type: research
year: 2024
venue: "Learning and Nonlinear Models"
authors:
  - "Marcos Vinicius Franca Nunes"
  - "Andre Luiz Carvalho Ottoni"
status: processed
processed_at: 2026-06-11
topics:
  - "solar panel defect classification"
  - "classical data augmentation"
tasks:
  - "[[Solar panel classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
application_area: "solar panel visual inspection"
datasets:
  - "combined Kaggle solar panel image datasets"
dataset_sizes:
  - "3,048 images after duplicate removal and cropping"
splits:
  - "defective: 1,206 train / 417 test; clean: 1,069 train / 356 test"
modalities:
  - "RGB solar panel images"
methods:
  - "[[Data augmentation]]"
model_family:
  - "convolutional neural networks"
architectures:
  - "[[ResNet50]]"
losses: []
optimizers:
  - "[[Adam]]"
training_regime: "supervised transfer learning"
augmentation:
  - "zoom"
  - "rotation"
  - "horizontal shift"
  - "vertical shift"
synthetic_data: "classical Keras ImageDataGenerator augmentation creates transformed images from real samples"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "F1-score, recall, precision, and accuracy reported as percentages"
baselines:
  - "ResNet50 without data augmentation"
benchmarks: []
evaluation_protocol: "four-stage comparison of no augmentation, individual transforms, selected transform combinations, and best combined transforms"
parameters: "ResNet50: 23,587,712 parameters"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2024 - Nunes - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies.pdf"
code: "not reported"
data: "two Kaggle solar panel image datasets cited as sources"
doi: "not reported"
arxiv: "not applicable"
related_papers: []
related_concepts:
  - "[[Data augmentation]]"
related_methods:
  - "[[Data augmentation]]"
  - "[[ResNet50]]"
related_datasets: []
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar panel classification]]"
  - "[[Defect classification]]"
related_benchmarks: []
concept_notes_created_or_updated: []
source_file: "paper-inbox/10_processed/Research/2024 - Nunes - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Nunes - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Nunes - Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies.txt"
artifact_status: "code not reported; Kaggle data sources cited"
tags:
  - paper
---

# Deep Learning for Solar Panels Defect Classification Using Data Augmentation Strategies

## Summary

- The paper evaluates classical augmentation configurations for binary solar panel defect classification with ResNet50.
- The baseline without data augmentation reaches 83.05% accuracy and 83.00% F1-score at 30 epochs; the best reported augmentation is 35-degree rotation at 87.64% accuracy and 88.00% F1-score.
- The paper also shows that not all augmentation helps: eight configurations perform worse than the no-augmentation reference.

## Paper Type

- Type: research.
- Why: it performs staged experiments comparing augmentation transformations and reports classification metrics.

## Problem

- Task: binary solar panel defect classification.
- Setting: visual inspection of clean vs defective/dirty solar panel images.
- Inputs: 256 x 256 RGB images.
- Outputs: class 0 defective board or class 1 clean board.
- Motivation: solar panel inspection is risky and datasets are limited.
- Assumptions: transformed images from real samples can improve classifier generalization.

## Contribution

- Claimed: systematic exploration of zoom, rotation, horizontal shift, and vertical shift augmentation for solar panel defect classification.
- Shown: a 35-degree rotation improves accuracy by 4.59 percentage points over the 30-epoch no-augmentation baseline.
- Inferred: augmentation tuning matters because some combinations reduce accuracy below baseline.

## Method

- Core idea: train ResNet50 under no-augmentation and augmentation configurations, then compare classification metrics.
- Architecture / algorithm: ImageNet-pretrained ResNet50 from Keras.
- Objective / loss: not reported in extracted text.
- Optimization: Adam with learning rate 0.0001.
- Training data: two Kaggle solar panel image datasets merged, cropped, and deduplicated.
- Data pipeline: binary clean/defective labels, resize to 256 x 256, train/evaluate across staged augmentation experiments.
- Augmentation / synthesis: Keras ImageDataGenerator transformations: zoom, rotation, horizontal displacement, vertical displacement.
- Inference: binary image classification.
- Complexity / deployment constraints: ResNet50 chosen for lower computational complexity relative to heavier models in related work.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB solar panel image.
- Output target: binary clean/defective label.
- Supervision: supervised classification.
- Objective: improve defect classification using augmentation.

### Model And Training

- Model family: CNN.
- Architecture: ResNet50.
- Parameters: 23,587,712.
- Pretraining: ImageNet weights.
- Fine-tuning: yes.
- Losses: not reported.
- Optimizer: Adam.
- Hyperparameters: 30 epochs for stages 1 and 2; 70 epochs for stage 3; learning rate 0.0001; input 256 x 256 x 3.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: two Kaggle solar panel image datasets.
- Data source: Kaggle sources `pythonafroz/solar-panel-images` and another cited Kaggle dataset.
- Dataset size: 3,048 images after preprocessing.
- Labels / annotations: class 0 defective boards and class 1 clean boards.
- Splits: defective 1,206 train / 417 test; clean 1,069 train / 356 test.
- Preprocessing: cropping and duplicate removal.
- Augmentation: zoom, rotation, horizontal shift, vertical shift.
- Synthetic data: transformed copies of real images; no generative model.
- Leakage checks: duplicate images between datasets are removed; no other leakage audit reported.
- License: not reported.

### Evaluation

- Protocol: compare no augmentation, individual transforms, selected pairs, and selected four-transform combinations.
- Used performance metrics: accuracy, F1-score, recall, precision.
- Primary metric: F1-score with accuracy used for ranking.
- Metric definitions: standard classification metrics.
- Metric direction / units: higher percentage is better.
- Baselines: no data augmentation at 30 and 70 epochs.
- Benchmarks: not reported as a named benchmark.
- Statistical tests: not reported.
- Failure cases: some transform combinations reduce accuracy below the no-augmentation baseline.

## Evidence

### Experimental Setup

- Datasets: merged Kaggle solar panel images.
- Splits: fixed train/test counts by class.
- Baselines: no augmentation at 30 and 70 epochs.
- Used performance metrics: accuracy, F1, recall, precision.
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| No augmentation, 30 epochs | Solar panel binary classification | Accuracy | higher | not applicable | 83.05% | Reference for augmentation ranking. |
| No augmentation, 30 epochs | Solar panel binary classification | F1-score | higher | not applicable | 83.00% | Reference F1. |
| Best individual augmentation | Solar panel binary classification | Accuracy | higher | 83.05% | 87.64% | Rotation 35 deg, +4.59 percentage points. |
| Best individual augmentation | Solar panel binary classification | F1-score | higher | 83.00% | 88.00% | Rotation 35 deg. |
| Best Stage 3 combined augmentation | Solar panel binary classification | Accuracy | higher | 83.05% | 84.60% | Zoom 0.4 + rotation 35 deg + HS 0.6 + VS 1.0. |
| Best Stage 3 combined augmentation | Solar panel binary classification | F1-score | higher | 83.00% | 85.00% | Combined transforms underperform the best single rotation. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | binary classification | percent correct | higher | no | Used for ranking top and worst configurations. |
| [[F1-score]] | binary classification | percent | higher | yes | Best is 88%. |
| [[Recall]] | binary classification | percent | higher | no | Best rotation reports 88%. |
| [[Precision]] | binary classification | percent | higher | no | Best rotation reports 88%. |

### Ablations

- No augmentation vs each transform isolates augmentation effect.
- Stage 2 combines top transform settings in pairs.
- Stage 3 combines selected zoom, rotation, HS, and VS settings.
- Worst-configuration ranking shows augmentation can harm performance.

## Dataset / Benchmark Details

- Source: Kaggle image datasets.
- Collection: not reported beyond Kaggle sources.
- Annotation: clean vs defective/dirty labels.
- Size: 3,048 after preprocessing.
- Splits: 2,275 training images and 773 testing images total by extracted class counts.
- Modalities: RGB images.
- License: not reported.
- Leakage risks: duplicate removal between sources is reported; no explicit split leakage audit.
- Bias / coverage: combines dirty and physically defective panels in the defective class.
- Maintenance: not reported.

## Limitations

- Stated: some augmentation configurations perform worse than no augmentation.
- Inferred: binary labeling merges different defect and soiling conditions, which may limit interpretability.
- Inferred: exact Kaggle source metadata should be checked before treating the merged dataset as a stable benchmark.

## Reproducibility

- Code: not reported.
- Data: Kaggle sources cited.
- Hyperparameters: epochs, learning rate, optimizer, architecture, and augmentation values are reported.
- Random seeds: not reported.
- Environment: Keras 2.15.0 for ImageDataGenerator.
- Checkpoints / models: not reported.
- Exact preprocessing: cropping and duplicate removal reported but not fully specified.
- Artifact status: partial.

## Connections

### Graph Hubs

- Tasks: [[Solar panel classification]], [[Defect classification]].
- Methods: [[Data augmentation]], [[ResNet50]].
- Optimizers: [[Adam]].
- Datasets: combined Kaggle solar panel image datasets.
- Benchmarks: not reported.
- Domains: [[Solar cells and photovoltaic]].
- Metrics: [[Accuracy]], [[F1-score]], [[Recall]], [[Precision]].
- Concepts: augmentation sensitivity, transformation search.
- Dataset-domain links: combined solar panel images map to [[Solar cells and photovoltaic]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| not reported | not applicable | The paper compares with related solar-panel DL works, but no existing vault paper was identified as a direct shared-dataset match from the extracted text. |

### Backlinks Updated

- Pending graph audit.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| not applicable | not applicable | Existing augmentation, ResNet50, task, and metric notes cover central graph links. |

## Questions

- The second Kaggle dataset name is not fully visible in the extracted text; verify before creating a dataset note.
- The source does not report seeds or a statistical test for augmentation comparisons.
