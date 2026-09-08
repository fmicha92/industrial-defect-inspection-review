---
title: "Defects Localization in Images Using Deep Learning-based Classification with CAM Output"
aliases:
  - "Defects Localization in Images Using Deep Learning-Based Classification with CAM Output"
paper_key: "doi:10.1109/idaacs58523.2023.10348813"
paper_type: research
year: 2023
venue: "IEEE IDAACS"
authors:
  - "Rytis Augustauskas"
  - "Lukas Zabulis"
  - "Arnas Lipnickas"
  - "Simas Jokubauskas"
status: processed
processed_at: "2026-06-11"
topics:
  - "defect localization from classification"
tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[BSData]]"
  - "Oliena glass bottle defects"
  - "PCB defects"
methods:
  - "class activation mapping"
architectures:
  - "[[ConvNeXt]]"
  - "[[MobileNet]]"
  - "[[EfficientNet]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[IoU]]"
primary_metric: "[[IoU]]"
baselines:
  - "[[ConvNeXt]]"
  - "[[MobileNet]]"
doi: "10.1109/IDAACS58523.2023.10348813"
url: "https://doi.org/10.1109/IDAACS58523.2023.10348813"
pdf: "paper-inbox/10_processed/Research/2023 - Augustauskas - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Augustauskas - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Augustauskas - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Augustauskas - Defects Localization in Images Using Deep Learning-Based Classification with CAM Output.txt"
artifact_status: "PDF processed locally"
related_datasets:
  - "[[BSData]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
related_concepts:
  - "[[Surface defect detection]]"
tags:
  - paper
---

# Defects Localization in Images Using Deep Learning-based Classification with CAM Output

## Summary

- The paper adds a CAM-style output to binary defect classifiers so that classification models can produce rough defect-localization heatmaps without pixel-wise training labels.
- It evaluates on glass bottle, PCB, and [[BSData]] images, using binary classification labels for training and pixel/region labels only for localization evaluation.
- On BSData, MobileNetV3 reaches the best reported localization IoU of 0.85 among the listed configurations.

## Paper Type

- Type: research.
- Why: proposes a lightweight localization add-on to classifiers and evaluates classification/localization behavior on multiple defect datasets.

## Problem

- Task: defect classification with approximate defect localization.
- Setting: industrial visual inspection where segmentation annotation is expensive.
- Inputs: images cropped or prepared for binary defective/good classification.
- Outputs: binary defect prediction and CAM heatmap.
- Motivation: classification labels are cheaper than pixel masks, but classifiers provide weak reasoning and troubleshooting signals.
- Assumptions: CAM maps can approximate defect location even when the model is trained with image-level labels.

## Contribution

- Claimed: a non-trainable CAM output can be attached to classifiers to estimate defect location in a single prediction pass without pixel-wise labels.
- Shown: CAM outputs produce usable localization IoU on PCB and BSData; BSData best IoU is 0.85.
- Inferred: the method is localization-from-classification rather than segmentation training.

## Method

- Core idea: attach CAM output to lightweight classification architectures.
- Architecture / algorithm: ConvNeXtTiny, EfficientNetB0, MobileNetV3 and shortened variants with higher CAM output resolution.
- Objective / loss: binary classification objective; exact loss not reported in extracted text.
- Optimization: AdamW with cosine decay.
- Training data: image-level defective/good labels.
- Data pipeline: pixel-wise/region labels are discarded for training; some datasets are divided into smaller overlapping windows with a sliding window.
- Augmentation / synthesis: not reported.
- Inference: single prediction pass produces class prediction and heatmap.
- Complexity / deployment constraints: MFLOPS are reported; CAM operations are lightweight.

## ML / DL Extraction

### Task Formulation

- Input modality: glass bottle, PCB, and ball-screw-drive surface images.
- Output target: binary defective/good classification plus normalized CAM heatmap.
- Supervision: image-level binary labels for training; pixel/region labels used for evaluation.
- Objective: approximate localization without pixel-wise annotation.

### Model And Training

- Model family: image classifiers with CAM output.
- Architecture: ConvNeXtTiny, EfficientNetB0, MobileNetV3 and shortened variants.
- Parameters: not reported; MFLOPS reported for configurations.
- Losses: not reported.
- Optimizer: [[AdamW]].
- Hyperparameters: learning rate 10^-3 except ConvNeXtTiny at 10^-4; 50 epochs; batch sizes are shown in the training table but extraction is partially fragmented.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: Oliena glass bottle defects, [[BSData]], PCB defects.
- BSData size: 394 RGB images, with 324 for training and 70 for testing in the paper's dataset summary.
- PCB defects size: 1386 images, split 1109 train and 277 test.
- Labels / annotations: original pixel-wise or region labels exist for some datasets, but binary classification training uses defective/good directories.
- Splits: BSData 324 train / 70 test.
- Preprocessing: sliding-window cropping for non-Oliena datasets; CAM output normalized to 0-255 for evaluation.
- Augmentation: not reported.
- Synthetic data: PCB defects are described as semi-artificial because defects are generated with image editor software.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: train classifiers and evaluate CAM overlap against available localization labels.
- Used performance metrics: classification [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[IoU]], and MFLOPS.
- Primary metric: IoU for localization.
- Metric direction / units: IoU and F1 higher is better.
- Baselines: architecture/configuration variants rather than external methods.
- Statistical tests: not reported.
- Failure cases: narrow defects are not reliably highlighted; CAM sometimes reacts to surrounding areas.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| MobileNetV3 CAM | BSData localization | IoU | higher | not reported | 0.85 | Best BSData IoU in extracted evaluation. |
| MobileNetV3 CAM | BSData localization | F1 | higher | not reported | 0.89 | Same configuration as best IoU row. |
| ConvNeXtTiny_s CAM | PCB localization | IoU | higher | not reported | 0.87 | Best PCB IoU noted in text. |
| MobileNetV3_s CAM | Oliena localization | IoU | higher | not reported | 0.33 | Identified as the lowest result. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Binary defect classification | fraction | higher | no | Table IV. |
| [[Precision]] | Localization/classification evaluation | fraction | higher | no | Tables VI/VII. |
| [[Recall]] | Localization/classification evaluation | fraction | higher | no | Tables VI/VII. |
| [[F1-score]] | Localization overlap | score | higher | no | Reported with IoU. |
| [[IoU]] | CAM/localization overlap | score | higher | yes | Key localization measure. |

### Ablations

- Shortened classifiers increase CAM output resolution and improve localization in two cases.
- The method struggles with narrow defects where CAM reacts to a broader surrounding region.

## Limitations

- Stated: narrow defects are not always highlighted; CAM may react to a larger surrounding area.
- Inferred: CAM-based localization should not be treated as a substitute for pixel-level segmentation when precise boundaries are required.

## Reproducibility

- Code: not reported.
- Data: BSData and PCB datasets are public; Oliena availability not reported in extracted text.
- Hyperparameters: optimizer, learning rate, epochs, and some batch settings are reported.
- Random seeds: not reported.
- Environment: not reported.
- Artifact status: PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Defect segmentation]].
- Datasets: [[BSData]].
- Domains: [[Metal inspection]].
- Methods: class activation mapping.
- Models: [[ConvNeXt]], [[MobileNet]], [[EfficientNet]].
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[IoU]].
- Concepts: [[Surface defect detection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] | Shares dataset | This paper uses [[BSData]] for binary classification and CAM localization. |
| [[2023 - Few-shot semantic segmentation for industrial defect recognition]] | Shares dataset/task area | Both use [[BSData]] for defect localization or segmentation under reduced annotation pressure. |

### Backlinks Updated

- [[BSData]] and [[Metal inspection]] link back to this paper.

## Questions

- Which exact architecture configuration corresponds to each numbered BSData table row?
- Are the CAM evaluation scripts available?
