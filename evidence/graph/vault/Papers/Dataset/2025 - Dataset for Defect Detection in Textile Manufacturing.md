---
title: "Dataset for defect detection in textile manufacturing"
aliases:
  - "Batavia and Sarga woven fabric dataset paper"
paper_key: "doi:10.36443/10259/9965"
paper_type: dataset
year: 2025
venue: "Data in Brief"
authors:
  - "Beatriz Gil-Arroyo"
  - "Juan Marcos Sanz"
  - "Angel Arroyo"
  - "Daniel Urda"
  - "Nuno Basurto"
  - "Alvaro Herrero"
status: processed
processed_at: 2026-05-27
topics:
  - textile manufacturing
  - fabric defect detection
  - image analysis
  - dataset
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "textile manufacturing quality inspection"
datasets:
  - "[[Batavia and Sarga woven fabric images]]"
dataset_sizes:
  - "2755 Batavia original images"
  - "1548 Sarga original images"
  - "8782 Batavia defect patches"
  - "19911 Batavia control patches"
  - "173 Sarga defect patches"
  - "18403 Sarga control patches"
splits:
  - "Batavia originals and patches grouped into cases and controls"
  - "Sarga originals and patches grouped into cases and controls"
modalities:
  - "grayscale textile images"
methods:
  - "image patch slicing"
model_family: []
architectures: []
losses: []
training_regime: "not applicable"
augmentation: []
synthetic_data: "none reported"
metrics: []
primary_metric: "not applicable"
metric_definitions: []
baselines: []
benchmarks: []
evaluation_protocol: "not applicable; the article describes dataset collection and preprocessing but does not report baseline model results"
parameters: "not applicable"
compute: "not reported"
hardware: "Basler raL camera with Awaiba DR-12k-3.5 CMOS sensor; 850 nm LED array"
training_time: "not applicable"
inference_cost: "not applicable"
url: "https://doi.org/10.1016/j.dib.2025.111451"
pdf: "paper-inbox/10_processed/Dataset/2025 - Gil-Arroyo - Dataset for defect detection in textile manufacturing.pdf"
code: "image preprocessing code reported available on GitHub; exact URL not included in extracted text"
data: "https://doi.org/10.36443/10259/9965"
doi: "10.1016/j.dib.2025.111451"
arxiv: "not reported"
related_papers:
  - "[[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]"
  - "[[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]"
  - "[[2019 - A Public Fabric Database for Defect Detection Methods and Results]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods: []
related_datasets:
  - "[[Batavia and Sarga woven fabric images]]"
  - "[[Lusitano]]"
  - "[[ZJU-Leaper]]"
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
related_benchmarks: []
concept_notes_created_or_updated:
  - "[[Batavia and Sarga woven fabric images]]"
source_file: "paper-inbox/10_processed/Dataset/2025 - Gil-Arroyo - Dataset for defect detection in textile manufacturing.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Gil-Arroyo - Dataset for defect detection in textile manufacturing.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Gil-Arroyo - Dataset for defect detection in textile manufacturing.txt"
artifact_status: "dataset and preprocessing code reported available"
tags:
  - paper
  - dataset
  - textile-inspection
---

# Dataset for defect detection in textile manufacturing

## Summary

- Introduces [[Batavia and Sarga woven fabric images]], a public textile image dataset collected at Textil Santanderina in Cantabria, Spain.
- Provides high-resolution grayscale images of Batavia and Sarga fabrics, plus cropped 365 x 365 patches labeled as cases or controls.
- The article is a dataset description rather than a model evaluation paper; it reports collection hardware, preprocessing, directory structure, patch counts, and reuse potential for AI-based [[Textile defect detection]].

## Paper Type

- Type: dataset paper.
- Why: The central contribution is a public image dataset and its preprocessing/organization, not a new model or benchmark result.

## Problem

- Task: [[Textile defect detection]].
- Setting: textile manufacturing quality inspection for Batavia and Sarga woven fabrics.
- Inputs: grayscale fabric images captured under controlled VIS-NIR / infrared illumination.
- Outputs: original fabric images and cropped patches grouped into defect cases and non-defect controls.
- Motivation: automated inspection can improve efficiency, objectivity, and defect discovery in textile production.
- Assumptions: processed 8-bit images and cropped patches are suitable for training and evaluating AI/ML defect detection methods.

## Contribution

- Claimed: The dataset supports AI and ML models for identifying fabric defects such as weave inconsistencies, colour variations, and surface irregularities.
- Shown: The dataset includes 2755 Batavia originals, 1548 Sarga originals, and case/control patch folders with CSV metadata.
- Shown: The imaging setup uses a Basler raL camera with an Awaiba DR-12k-3.5 CMOS sensor, 10 pixels/mm resolution, and an 850 nm LED array.
- Inferred: The dataset is most immediately useful for supervised binary patch classification or defect-detection experiments, because it provides case/control labels but no pixel masks or baseline metrics.

## Method

- Core idea: capture high-resolution woven fabric images, reduce them from 16-bit to 8-bit, slice them into overlapping patches, and organize patches into case/control folders.
- Architecture / algorithm: not applicable.
- Objective / loss: not applicable.
- Optimization: not applicable.
- Training data: [[Batavia and Sarga woven fabric images]] can be used as training data; the paper itself does not train a model.
- Data pipeline: capture 2048 x 696 grayscale images, convert to 8-bit PNG, crop into twelve 365 x 365 patches using a 2 x 6 layout with overlap, and record patch labels in `info_patches.csv`.
- Augmentation / synthesis: none reported.
- Inference: not applicable.
- Complexity / deployment constraints: image capture uses a line-scan camera and infrared illumination designed to avoid interference with standard D65 visual inspection lighting.

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale textile images.
- Output target: defect case/control labels for cropped fabric patches.
- Supervision: supervised labels are provided as 0 for no defect and 1 for defect in CSV metadata.
- Objective: enable fabric defect detection and quality inspection experiments.

### Model And Training

- Model family: not applicable.
- Architecture: not applicable.
- Parameters: not applicable.
- Pretraining: not applicable.
- Fine-tuning: not applicable.
- Losses: not applicable.
- Optimizer: not applicable.
- Hyperparameters: not applicable.
- Seeds: not applicable.
- Training compute: not applicable.

### Data

- Datasets: [[Batavia and Sarga woven fabric images]].
- Data source: Textil Santanderina in Cabezón de la Sal, Cantabria, Spain.
- Dataset size: 2755 Batavia originals, 1548 Sarga originals, 8782 Batavia case patches, 19,911 Batavia control patches, 173 Sarga case patches, and 18,403 Sarga control patches.
- Labels / annotations: patch CSV files provide image and patch names plus operator and ground-truth labels, where 0 means no defect and 1 means defect.
- Splits: folders are organized by fabric type, originals, patches, cases, and controls; train/test splits are not reported.
- Preprocessing: original 16-bit images were downscaled to 8-bit PNG and cropped into overlapping 365 x 365 patches.
- Augmentation: none reported.
- Synthetic data: none reported.
- Leakage checks: not reported.
- License: article is CC BY-NC; dataset license is not separately reported in the extracted text.

### Evaluation

- Protocol: not applicable.
- Model evaluation metrics: not applicable.
- Primary metric: not applicable.
- Metric definitions: not applicable.
- Metric direction / units: not applicable.
- Baselines: not applicable.
- Benchmarks: not applicable.
- Statistical tests: not applicable.
- Failure cases: not reported.

## Evidence

### Experimental Setup

- Datasets: [[Batavia and Sarga woven fabric images]].
- Splits: not reported.
- Baselines: not applicable.
- Model evaluation metrics: not applicable.
- Compute: not reported.
- Hardware: Basler raL camera with Awaiba DR-12k-3.5 CMOS sensor and 850 nm LED array.
- Training time: not applicable.
- Inference cost: not applicable.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Batavia originals | [[Batavia and Sarga woven fabric images]] / [[Textile defect detection]] | count | higher | not applicable | 2755 | Original 2048 x 696 grayscale images. |
| Sarga originals | [[Batavia and Sarga woven fabric images]] / [[Textile defect detection]] | count | higher | not applicable | 1548 | Original 2048 x 696 grayscale images. |
| Batavia patches | [[Batavia and Sarga woven fabric images]] / [[Textile defect detection]] | count | higher | not applicable | 8782 case / 19,911 control | 4367 ambiguous Batavia patches were excluded. |
| Sarga patches | [[Batavia and Sarga woven fabric images]] / [[Textile defect detection]] | count | higher | not applicable | 173 case / 18,403 control | Sarga patch count equals 1548 originals times 12. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| not applicable | not applicable | not applicable | not applicable | not applicable | The paper does not report model performance metrics. |

### Ablations

- Not applicable.

## Dataset / Benchmark Details

- Source: Textil Santanderina, Cabezón de la Sal, Cantabria, Spain.
- Collection: November 2022 using controlled lighting and a VIS-NIR imaging setup.
- Annotation: case/control patch labels are reported in CSV metadata; ambiguous Batavia patches were excluded after review by Textil Santanderina.
- Size: 4303 original images and 47,269 retained cropped patches across Batavia and Sarga.
- Splits: not reported.
- Modalities: 8-bit grayscale PNG images.
- License: article is CC BY-NC; dataset-specific license is not separately reported.
- Leakage risks: patch slicing creates multiple overlapping patches from each original image, so experiments should split by original image rather than random patch when testing generalization.
- Bias / coverage: two weave types from one manufacturer and one collection period; Sarga defect cases are much rarer than Batavia defect cases.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: the article lists limitations as not applicable.
- Inferred: no baseline model results are reported, so practical detection difficulty is not quantified.
- Inferred: class imbalance is substantial, especially for Sarga patches.
- Inferred: train/test protocol and dataset license are not fully specified in the extracted text.

## Reproducibility

- Code: image preprocessing code is reported as uploaded to GitHub, but the extracted text does not include the exact URL.
- Data: https://doi.org/10.36443/10259/9965.
- Hyperparameters: not applicable.
- Random seeds: not applicable.
- Environment: Python libraries listed include `os`, `glob`, `PIL/Pillow`, and `shutil`.
- Checkpoints / models: not applicable.
- Exact preprocessing: 16-bit to 8-bit conversion, 2048 x 696 originals, 2 x 6 slicing into 365 x 365 patches with 29-pixel x-axis overlap and 35-pixel y-axis overlap.
- Artifact status: dataset and preprocessing code reported available.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]]
- Datasets: [[Batavia and Sarga woven fabric images]], [[Lusitano]], [[ZJU-Leaper]], [[AITEX]]
- Methods: not applicable
- Metrics: not applicable
- Domains: [[Textile and fiber inspection]], [[Industrial visual inspection]]
- Benchmarks: not applicable

### Builds On

- not reported.

### Contrasts With

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]: both introduce public textile defect datasets, but Lusitano is framed around one-class anomaly detection with baseline model results, while this paper provides Batavia/Sarga case-control patches without reported baseline metrics.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]: ZJU-Leaper provides richer benchmark evaluation and segmentation-style annotations, while this paper focuses on a smaller two-weave dataset and patch-level case/control organization.

### Shares Dataset

- [[Batavia and Sarga woven fabric images]]: introduced by this paper.

### Shares Task

- [[Textile defect detection]]: the dataset is designed for fabric defect detection and textile quality inspection.

### Shares Method

- not applicable.

### Shares Metric

- not applicable.

### Application / Domain

- [[Textile and fiber inspection]]: the data come from woven fabric manufacturing inspection.
- [[Industrial visual inspection]]: the paper frames reuse around automated quality inspection.

### Follow-Up Reading

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]: useful for comparing another recent public textile dataset with reported anomaly detection baselines.
- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]: useful for fabric defect benchmark protocols and richer annotation regimes.

## Questions

- What exact URL hosts the GitHub preprocessing code referenced by the article?
- What dataset license applies to the University of Burgos repository item?
- Should experiments split by original image to avoid overlap leakage between patches?
