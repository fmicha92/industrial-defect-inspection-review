---
title: "CutPaste: Self-Supervised Learning for Anomaly Detection and Localization"
aliases:
  - "CutPaste: Self-Supervised Learning for Anomaly Detection and Localization"
paper_key: "arxiv:2104.04015"
paper_type: research
year: 2021
venue: "arXiv"
authors:
  - "Chun-Liang Li"
  - "Kihyuk Sohn"
  - "Jinsung Yoon"
  - "Tomas Pfister"
status: processed
processed_at: 2026-06-12
topics:
  - "self-supervised anomaly detection"
  - "CutPaste augmentation"
  - "defect localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Data augmentation]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures: []
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "Rotation prediction"
  - "Cutout prediction"
  - "Scar prediction"
  - "DOCC"
  - "Uninformed Student"
  - "P-SVDD"
benchmarks:
  - "[[MVTec AD]]"
code: "not reported"
data: "uses MVTec AD"
doi: "not reported"
arxiv: "2104.04015"
url: "https://arxiv.org/abs/2104.04015"
pdf: "paper-inbox/10_processed/Research/2021 - Li - CutPaste Self-Supervised Learning for Anomaly Detection and Localization.pdf"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Data augmentation]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2021 - Li - CutPaste Self-Supervised Learning for Anomaly Detection and Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Li - CutPaste Self-Supervised Learning for Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Li - CutPaste Self-Supervised Learning for Anomaly Detection and Localization.txt"
artifact_status: "not reported"
tags:
  - paper
---
# CutPaste: Self-Supervised Learning for Anomaly Detection and Localization

## Summary

CutPaste trains representations for industrial anomaly detection by making a network classify normal images against synthetic local irregularities created by cutting an image patch and pasting it elsewhere in the same image. On [[MVTec AD]], the paper reports image-level anomaly detection and pixel-level localization results, with the strongest scratch-trained CutPaste 3-way setup improving over rotation, Cutout, Scar, and prior one-class baselines.

## Paper Type

- Type: research.
- Why: The paper proposes a self-supervised augmentation objective and evaluates it quantitatively on anomaly detection and localization benchmarks.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: normal-only industrial visual inspection on [[MVTec AD]].
- Inputs: MVTec AD product and texture images.
- Outputs: image-level anomaly scores and pixel-level anomaly heatmaps.
- Motivation: real industrial anomaly patterns are unknown and scarce, so representations should learn local irregularity from normal data.
- Assumptions: local patch irregularities can teach a representation to detect real defects even when synthetic pasted patches are visually imperfect defect simulations.

## Contribution

- Claimed: Introduces CutPaste, a simple self-supervised augmentation objective that cuts a local patch and pastes it at a random location.
- Claimed: Extends the method to CutPaste-Scar and a 3-way classification objective over normal, CutPaste, and CutPaste-Scar samples.
- Shown: On MVTec AD image-level detection, CutPaste 3-way reaches 95.2 AUROC from scratch and 96.1 AUROC with an ensemble; EfficientNet-B4 fine-tuning reaches 96.6 AUROC.

## Method

- Core idea: learn representations by predicting whether an image is normal or synthetically modified by CutPaste-style local irregularities.
- Architecture / algorithm: self-supervised classification objective plus one-class classifier on learned representations; patch-level scoring is used for localization.
- Objective / loss: cross-entropy over augmentation labels for the proxy task.
- Training data: MVTec AD normal training images.
- Data pipeline: patches are cut from an image and pasted at random locations; variants include rectangular CutPaste and elongated scar-like CutPaste.
- Augmentation / synthesis: CutPaste, CutPaste-Scar, and a 3-way combination; baseline augmentations include rotation, Cutout, and Scar.
- Inference: image-level anomaly scores from learned representations; localization uses dense patch anomaly scores, receptive-field upsampling, and Gaussian smoothing.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]].
- Splits: category-wise one-class protocol with normal training examples and normal/anomalous test images.
- Baselines: DOCC, Uninformed Student, P-SVDD, rotation prediction, Cutout prediction, Scar prediction.
- Used performance metrics: [[AU-ROC]].
- Seeds: main detection table reports mean and standard error over five random seeds.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| CutPaste 3-way vs rotation | MVTec AD image-level anomaly detection | AUROC (%) | higher | 73.1 | 95.2 | Scratch-trained self-supervised proxy task. |
| CutPaste 3-way vs Cutout | MVTec AD image-level anomaly detection | AUROC (%) | higher | 71.3 | 95.2 | Same representation-learning framework, different augmentation. |
| CutPaste 3-way vs Scar | MVTec AD image-level anomaly detection | AUROC (%) | higher | 85.0 | 95.2 | 3-way CutPaste combines rectangular and scar-like local irregularities. |
| CutPaste 3-way vs P-SVDD | MVTec AD image-level anomaly detection | AUROC (%) | higher | 92.1 | 95.2 | P-SVDD is a prior learning-from-scratch baseline. |
| CutPaste ensemble | MVTec AD image-level anomaly detection | AUROC (%) | higher | 95.2 | 96.1 | Ensemble of five CutPaste 3-way models. |
| EfficientNet-B4 fine-tuned with CutPaste | MVTec AD image-level anomaly detection | AUROC (%) | higher | 94.5 | 96.6 | Baseline is pretrained EfficientNet-B4 without CutPaste fine-tuning. |
| Patch CutPaste localization | MVTec AD pixel-wise anomaly localization | AUROC (%) | higher | 90.4 | 96.0 | Source compares against DistAug contrastive localization; GradCAM variant reports 88.3. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level detection and pixel-level localization | Percent AUROC | higher | yes | Main reported metric. |

### Ablations

- CutPaste and CutPaste-Scar improve over simpler Cutout/Scar proxy tasks; the 3-way objective improves the all-category detection average to 95.2 AUROC.
- A synthetic-defect generalization study patches shapes such as MNIST digits, squares, ellipses, and hearts into normal images, but the main evidence for MVTec AD is the baseline-versus-CutPaste table.

## ML / DL Extraction

### Data

- Datasets: [[MVTec AD]].
- Dataset size: source describes MVTec AD as 15 categories with 10 object and 5 texture categories; number of training images varies from 60 to 391 by category.
- Labels / annotations: normal training images, normal/anomalous test images, pixel-level annotations for defective test images.
- Preprocessing: images resized for model inputs; exact per-experiment preprocessing beyond this is not fully reported in the extracted text.
- Augmentation: CutPaste, CutPaste-Scar, rotation, Cutout, Scar, and variants of Cutout.
- Synthetic data: synthetic local irregularities are generated from normal images; no external defect images are required.
- Leakage checks: not reported.

### Evaluation

- Protocol: one-class category-wise evaluation on MVTec AD.
- Baselines: listed above.
- Statistical tests: standard error over five random seeds is reported for main self-supervised variants.
- Failure cases: rotation prediction performs poorly for unaligned object categories such as screw.

## Limitations

- Stated: CutPaste is not a perfect simulation of real defects.
- Inferred: the method depends on whether pasted-patch irregularities transfer to the real anomaly morphology of each category.

## Reproducibility

- Code: not reported.
- Data: MVTec AD is public.
- Hyperparameters: not fully reported in the analysis input.
- Random seeds: five random seeds for main detection table.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Data augmentation]], [[Defect synthesis]], [[Synthetic data generation]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Shares Dataset

- [[MVTec AD]]: main dataset for anomaly detection and localization.

### Shares Method

- [[Data augmentation]] and [[Defect synthesis]]: CutPaste is a synthetic local irregularity augmentation designed as a self-supervised proxy task.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]]: reports image-level detection and pixel-wise localization.

### Shares Metric

- [[AU-ROC]]: primary quantitative result for detection and localization.

## Questions

- Does the released version report code or exact implementation details beyond the extracted arXiv text?
- How stable is CutPaste under more recent multi-dataset benchmarks such as [[VisA]] or [[MVTec AD 2]]?
