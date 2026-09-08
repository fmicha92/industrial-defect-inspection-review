---
title: "Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples"
aliases:
  - "Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples"
paper_key: "doi:10.1007/s44196-023-00328-0)/author(mingjing"
paper_type: research
year: 2023
venue: "International Journal of Computational Intelligence Systems"
authors:
  - "Mingjing Pei"
  - "Ningzhong Liu"
  - "Bing Zhao"
  - "Han Sun"
status: processed
processed_at: 2026-06-12
topics:
  - "self-supervised anomaly detection"
  - "synthetic anomaly simulation"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
methods:
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
  - "[[Self-supervised learning]]"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "CutPaste"
  - "VT-ADL"
  - "PaDiM"
  - "P-SVDD"
benchmarks:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
evaluation_protocol: "ROC-AUC on MVTec AD and BTAD"
doi: "10.1007/s44196-023-00328-0"
url: "https://doi.org/10.1007/s44196-023-00328-0"
pdf: "paper-inbox/10_processed/Research/2023 - Pei - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples.pdf"
code: "not reported"
data: "not reported"
related_papers:
  - "[[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]]"
related_methods:
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2023 - Pei - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Pei - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Pei - Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples.txt"
artifact_status: "not reported"
tags:
  - paper
---

# Self-Supervised Learning for Industrial Image Anomaly Detection by Simulating Anomalous Samples

## Summary

The paper improves CutPaste-style self-supervised anomaly simulation by constraining patch placement and broadening augmentation. For object categories, extracted patches are pasted onto the object rather than arbitrary background; for both object and texture categories, the method uses a combination of geometric and color transformations to cover more anomaly appearances. It reports 97.6% average ROC-AUC on [[MVTec AD]], +1.5% over the CutPaste baseline, and about +4% over VT-ADL on [[BTAD]].

## Paper Type

- Type: research.
- Why: It proposes a synthetic-anomaly training method and evaluates it on public anomaly detection datasets.

## Problem

- Task: [[Industrial anomaly detection]].
- Setting: industrial anomaly detection with scarce abnormal samples and normal-only training.
- Inputs: normal industrial images.
- Outputs: image-level anomaly scores and visual localization maps via Full Grad-CAM.
- Motivation: random patch placement in CutPaste can create unrealistic pseudo anomalies, especially when patches are pasted outside the target object.
- Assumptions: object-aware patch placement and a more diverse augmentation set produce pseudo anomalies closer to real anomaly distributions.

## Contribution

- Claimed: extracted patches in object classes should be pasted on the object surface rather than arbitrary background.
- Claimed: multiple geometric and color augmentations better cover diverse anomaly types than single augmentations.
- Shown: average ROC-AUC improves on MVTec AD and BTAD relative to reported baselines.

## Method

- Core idea: simulate anomalous samples through patch extraction, data augmentation, object-aware patch paste, and one-class classification.
- Architecture / algorithm: patch extraction and paste pipeline plus a one-class classifier; Full Grad-CAM is used to visualize anomaly regions.
- Objective / loss: classification between normal and simulated anomalous samples; exact loss is not reported in the extracted text.
- Optimization: not reported.
- Training data: normal samples from [[MVTec AD]] and [[BTAD]].
- Data pipeline: generate pseudo anomalies by extracting patches, applying augmentation, and compositing with object masks for object categories.
- Augmentation / synthesis: geometric and color transformations selected to match anomaly patterns observed in the test datasets.
- Inference: anomaly score maps are generated from image-level feature vectors and visualized with Full Grad-CAM.
- Complexity / deployment constraints: similar GPU memory and training time to the CutPaste baseline in the reported comparison.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]] and [[BTAD]].
- Baselines: CutPaste, PaDiM, P-SVDD, U-Student, AnoGAN, RAID, AE+MSE, AE+MSE+SSIM, and VT-ADL.
- Used performance metrics: ROC-AUC.
- Compute: GPU memory comparison reports 126.67 MB for baseline and 130.38 MB for the proposed method.
- Training time: reported as 3.08 us for baseline and 3.51 us for the proposed method.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Synthetic anomaly method | MVTec AD | average ROC-AUC | higher | CutPaste 96.10% | 97.61% | +1.51 percentage points. |
| Object-aware patch placement | MVTec AD object classes | ROC-AUC | higher | 87.55% | 92.05% | +4.5 points without data augmentation in that ablation. |
| Synthetic anomaly method | BTAD | ROC-AUC | higher | VT-ADL not fully table-extracted | about +4% | Text reports the proposed method is higher than VT-ADL by about 4%. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] / ROC-AUC | anomaly detection | area under ROC curve, percent | higher | yes | Reported for MVTec AD and BTAD. |

### Ablations

- Object-aware patch placement improves object-category ROC-AUC from 87.55% to 92.05% in the no-augmentation placement ablation.
- The proposed method uses more GPU memory and time than the baseline in the small resource table, but the reported difference is small.

## Dataset / Benchmark Details

- Source: [[MVTec AD]] and [[BTAD]] public anomaly-detection datasets.
- Modalities: industrial visual inspection images.
- Labels / annotations: benchmark anomaly labels and masks for evaluation; generated pseudo labels for training.
- License: not reported.

## Limitations

- Stated: not reported.
- Inferred: the method uses test-dataset anomaly statistics to select augmentations, which may need careful separation from evaluation if adapted to new domains.

## Reproducibility

- Code: not reported.
- Hyperparameters: patch sizing and augmentation selection are described, but full training recipe is not reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Defect synthesis]], [[Data augmentation]], [[Self-supervised learning]]
- Datasets: [[MVTec AD]], [[BTAD]]
- Benchmarks: [[MVTec AD]], [[BTAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Shares Dataset

- [[MVTec AD]] and [[BTAD]] are used to evaluate anomaly detection.

### Shares Method

- [[Defect synthesis]] and [[Data augmentation]]: the method synthesizes pseudo anomalies from normal images.
- [[Self-supervised learning]]: generated pseudo labels define the pretext task.

### Follow-Up Reading

- [[2024 - Patch-Wise Augmentation for Anomaly Detection and Localization]] also builds synthetic local patch anomalies but trains a direct reconstruction-detection model.

## Questions

- Which exact augmentation list is used per MVTec category, and how category-specific is the selection?
- Does the method preserve performance when augmentation selection is not tuned using test anomaly distributions?
