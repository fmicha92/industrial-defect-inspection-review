---
title: "Scarcity-GAN: Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets"
aliases:
  - "Scarcity-GAN: Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets"
paper_key: "sha256:174ded8816c007830ea9be967a5fc818b3b3297924016d15342ee787ce82ce5a"
paper_type: research
year: 2024
venue: "Neurocomputing"
authors:
  - "Chaobin Xu"
  - "Wei Li"
  - "Xiaohui Cui"
  - "Zhenyu Wang"
  - "Fengling Zheng"
  - "Xiaowu Zhang"
  - "Bin Chen"
status: processed
processed_at: 2026-05-23
topics:
  - "scarce data augmentation"
  - "GAN defect generation"
  - "defect detection"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[O-ring Dataset]]"
  - "[[Metal Iron Sheet Dataset]]"
  - "[[CODEBRIM]]"
  - "[[DAGM]]"
  - "[[Magnetic Tile Defects]]"
  - "[[CrackForestDataset]]"
methods:
  - "[[Scarcity-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[Scarcity-GAN]]"
metrics:
  - "[[FID]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions: []
baselines: []
benchmarks:
  - "[[O-ring Dataset]]"
  - "[[Metal Iron Sheet Dataset]]"
  - "[[CODEBRIM]]"
  - "[[DAGM]]"
  - "[[Magnetic Tile Defects]]"
  - "[[CrackForestDataset]]"
code: "not reported"
data: "not reported"
doi: "10.1016/j.neucom.2023.127061"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2024 - Xu - Scarcity-GAN Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Scarcity-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  []
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2024 - Xu - Scarcity-GAN Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Xu - Scarcity-GAN Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Xu - Scarcity-GAN Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Scarcity-GAN: Scarce Data Augmentation for Defect Detection via Generative Adversarial Nets

## Summary

The paper proposes Scarcity-GAN for scarce-data augmentation in defect detection. Scarcity-GAN selects extra defect features similar to a target scarce defect set, fuses those features with defect-free target images, and generates desired defects on the object surface. The metal-relevant experiment uses a Metal Iron Sheet dataset with only 15 scratch-defect images and 147 defect-free images, while extra defect information comes from [[DAGM]], [[Magnetic Tile Defects]], and [[CrackForestDataset]].

## Paper Type

- Type: research.
- Why: The title, abstract, and contribution framing describe a research method or evaluation study for industrial defect or anomaly inspection.

## Problem

- Task: [[Surface defect detection]], [[Defect classification]]
- Setting: [[Multi-industry anomaly detection]]
- Inputs: industrial inspection imagery, wafer maps, masks, or text prompts when reported by the source.
- Outputs: defect labels, anomaly scores, segmentation masks, generated defect samples, benchmark annotations, or classification predictions depending on the paper objective.
- Motivation: improve automated quality inspection under scarce, imbalanced, or hard-to-label defect data.
- Assumptions: not fully reported in the compact extraction unless stated above.

## Contribution

- Claimed: Targets scarce defect data augmentation using GAN-based synthesis.

- Inferred: The paper is relevant to [[Surface defect detection]], [[Defect classification]] through its stated task, dataset, method, or evaluation setting.

## Method

- Core idea: The paper proposes Scarcity-GAN for scarce-data augmentation in defect detection
- Architecture / algorithm: [[Scarcity-GAN]], [[GAN]], [[Data augmentation]], [[Scarcity-GAN]]
- Objective / loss: not reported in the compact extraction.
- Optimization: not reported in the compact extraction.
- Training data: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Data pipeline: not fully reported in the compact extraction.
- Augmentation / synthesis: [[Scarcity-GAN]], [[GAN]], [[Data augmentation]]
- Inference: not reported in the compact extraction.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Splits: not fully reported in the compact extraction.
- Baselines: not fully reported in the compact extraction.
- Used performance metrics: [[FID]], [[Precision]], [[Recall]], [[F1-score]]
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

- Shown: FID, precision, recall, and F1-score are reported; exact values are not fully extracted.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[FID]] | [[Surface defect detection]], [[Defect classification]] | not fully extracted | lower | not reported | recorded from compact extraction |
| [[Precision]] | [[Surface defect detection]], [[Defect classification]] | not fully extracted | higher | not reported | recorded from compact extraction |
| [[Recall]] | [[Surface defect detection]], [[Defect classification]] | not fully extracted | higher | not reported | recorded from compact extraction |
| [[F1-score]] | [[Surface defect detection]], [[Defect classification]] | not fully extracted | higher | yes | recorded from compact extraction |

## ML / DL Extraction

### Task Formulation

- Input modality: industrial visual inspection imagery, wafer maps, generated samples, masks, or multimodal prompts when reported.
- Output target: anomaly detection, localization, segmentation, classification, generation, or benchmark labels.
- Supervision: not fully reported in the compact extraction.
- Objective: not reported in the compact extraction.

### Model And Training

- Model family: [[GAN]], [[Generative Models]]
- Architecture: [[Scarcity-GAN]]
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: not reported in the compact extraction.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Data source: not fully reported in the compact extraction.
- Dataset size: not fully reported in the compact extraction.
- Labels / annotations: defect labels, masks, bounding boxes, wafer-map classes, text captions, or benchmark labels when reported.
- Splits: not fully reported in the compact extraction.
- Preprocessing: not reported.
- Augmentation: [[Scarcity-GAN]], [[GAN]], [[Data augmentation]]
- Synthetic data: reported when synthesis or augmentation is part of the method.
- Leakage checks: not reported.
- License: not reported in the compact extraction.

### Evaluation

- Protocol: not fully reported in the compact extraction.
- Used performance metrics: [[FID]], [[Precision]], [[Recall]], [[F1-score]]
- Primary metric: [[F1-score]]
- Metric definitions: standard metric names are recorded when present; exact definitions are not fully extracted.
- Metric direction / units: higher is better for accuracy, F-score, AU-ROC, AU-PR, AU-PRO, AP, mAP, IoU, and Dice-style metrics unless the paper states otherwise; lower is better for FID and LPIPS.
- Baselines: not fully reported in the compact extraction.
- Benchmarks: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Statistical tests: not reported.
- Failure cases: not fully reported in the compact extraction.

## Dataset / Benchmark Details

- Source: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], and [[CrackForestDataset]].
- Collection: industrial O-ring and metal iron sheet product images plus public/general defect datasets for extra defect features.
- Annotation: defect labels are used for detection evaluation; exact annotation format is not fully reported in the extracted text.
- Size: O-ring contains 200 defect-free images and 12 impurity-defect images. Metal Iron Sheet contains 147 defect-free images and 15 scratch-defect images. CODEBRIM experiment selects 10 crack-defect images and 175 defect-free images for training.
- Splits: original scarce defect images are used as test images for Faster R-CNN evaluation after training on synthesized images; exact full split for every dataset is not reported.
- Modalities: 2D surface defect images.
- License: not reported.
- Leakage risks: extra datasets are used to provide similar defect features; the paper does not report a formal leakage audit.
- Bias / coverage: targets very scarce defect classes and depends on availability of extra datasets with similar defect features.
- Maintenance: not reported.

## Metal Dataset Extraction

- [[Metal Iron Sheet Dataset]]: 147 defect-free images and 15 scratch-defect images; used as a scarce target metal dataset.
- [[Magnetic Tile Defects]]: used as an extra dataset providing blowhole/category defect features for feature selection and synthesis.
- [[DAGM]]: used as an extra defect dataset for feature maps similar to target defects.
- Synthesis: Scarcity-GAN uses clustering to select target-like extra defect feature maps, an encoder-decoder generator, Fusion Patch-Embedding to place defects on object regions, and a defect quality loss.
- Evaluation: generated samples train Faster R-CNN detectors; [[Precision]], [[Recall]], and [[F1-score]] are used. For Metal Iron Sheet, the paper reports Scarcity-GAN achieving the highest values across the three metrics compared with rotation and CutPaste.

## Limitations

- Dataset names, splits, and full result tables are not fully reported in the compact extraction.

- Inferred: conclusions should be checked against the full experimental protocol, dataset splits, and baseline details before using the paper as strong evidence.

## Reproducibility

- Code: not reported
- Data: not reported
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]]
- Methods: [[Scarcity-GAN]], [[GAN]], [[Data augmentation]]
- Datasets: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Benchmarks: [[O-ring Dataset]], [[Metal Iron Sheet Dataset]], [[CODEBRIM]], [[DAGM]], [[Magnetic Tile Defects]], [[CrackForestDataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[FID]], [[Precision]], [[Recall]], [[F1-score]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- not reported

### Shares Method

- [[Scarcity-GAN]]: central to the paper method or comparison framing.
- [[GAN]]: central to the paper method or comparison framing.
- [[Data augmentation]]: central to the paper method or comparison framing.

### Shares Task

- [[Surface defect detection]]: task supported by the paper title, abstract, or evaluation description.
- [[Defect classification]]: task supported by the paper title, abstract, or evaluation description.

### Shares Metric

- [[FID]]: used as an evaluation metric in the compact extraction.
- [[Precision]]: used as an evaluation metric in the compact extraction.
- [[Recall]]: used as an evaluation metric in the compact extraction.
- [[F1-score]]: used as an evaluation metric in the compact extraction.

### Application / Domain

- [[Multi-industry anomaly detection]]: application setting represented by the paper.

### Follow-up Reading

- not reported.

## Questions

- Which dataset splits, baselines, and implementation details are required before treating the reported gains as robust evidence?
- Are the synthetic samples evaluated for leakage, artifact overfitting, or distribution shift beyond the reported metrics?
