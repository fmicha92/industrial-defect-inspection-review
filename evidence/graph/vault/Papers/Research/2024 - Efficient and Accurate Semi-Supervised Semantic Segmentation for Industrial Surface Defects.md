---
title: "Efficient and accurate semi-supervised semantic segmentation for industrial surface defects"
aliases:
  - "Efficient and accurate semi-supervised semantic segmentation for industrial surface defects"
paper_key: "doi:10.1038/s41598-024-72579-6"
paper_type: research
year: 2024
venue: "Scientific Reports"
authors:
  - "Chenbo Shi"
  - "Kang Wang"
  - "Guodong Zhang"
  - "Zelong Li"
  - "Changsheng Zhu"
status: processed
processed_at: "2026-06-11"
topics:
  - "semi-supervised defect segmentation"
tasks:
  - "[[Defect segmentation]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[KolektorSDD]]"
  - "Steel dataset"
methods:
  - "two-branch perturbation cross pseudo-supervision"
  - "[[Pseudo-labeling]]"
  - "[[Data augmentation]]"
architectures:
  - "[[DeepLabV3+]]"
  - "[[MobileNet]]"
metrics:
  - "[[mIoU]]"
  - "[[F1-score]]"
  - "pixel accuracy"
  - "[[FPS]]"
primary_metric: "[[mIoU]]"
baselines:
  - "SupOnly"
  - "CPS"
  - "AEL"
  - "ST++"
  - "U2PL"
  - "GAT-seg"
  - "CCVC"
  - "AugSeg"
  - "DGCL"
doi: "10.1038/s41598-024-72579-6"
url: "https://doi.org/10.1038/s41598-024-72579-6"
pdf: "paper-inbox/10_processed/Research/2024 - Shi - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Shi - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Shi - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Shi - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects.txt"
artifact_status: "open access PDF processed locally"
related_datasets:
  - "[[KolektorSDD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
related_methods:
  - "[[Pseudo-labeling]]"
  - "[[Data augmentation]]"
related_learning_paradigms:
  - "[[Semi-supervised learning]]"
related_concepts:
  - "[[Surface defect detection]]"
tags:
  - paper
---

# Efficient and accurate semi-supervised semantic segmentation for industrial surface defects

## Summary

- The paper proposes a semi-supervised defect segmentation framework based on image-space and feature-space perturbation invariance with cross-pseudo-supervision.
- It evaluates on self-built industrial datasets, public [[KolektorSDD]], and a steel dataset, reporting improved [[mIoU]] under limited labeled data.
- The augmentation-like component is perturbation and random data enhancement, not synthetic defect generation.

## Paper Type

- Type: research.
- Why: proposes a semi-supervised segmentation method and validates it with benchmark comparisons, public datasets, and ablation studies.

## Problem

- Task: pixel-level industrial defect segmentation.
- Setting: industrial inspection where labeled defect masks are costly and sample sizes are small.
- Inputs: industrial defect images with partial labels and unlabeled images.
- Outputs: pixel-wise segmentation masks.
- Motivation: fully supervised methods require expensive annotation; low contrast and background noise degrade segmentation.
- Assumptions: perturbation invariance across image and feature spaces can exploit unlabeled samples.

## Contribution

- Claimed: diverse perturbation cross-pseudo-supervision reduces dependence on labeled datasets while improving edge and small-target segmentation.
- Shown: the method exceeds SOTA semi-supervised methods on KolektorSDD by 4.39% mIoU and achieves 85.11% mIoU in the final ablation configuration.
- Inferred: the work is relevant to augmentation because it uses random data enhancement and perturbation, but its main framing is semi-supervised segmentation.

## Method

- Core idea: train a semi-supervised segmentation model with perturbation consistency and pseudo-label supervision.
- Architecture / algorithm: two-branch perturbation cross-pseudo-supervision, improved DeepLabv3Plus with simplified MobileNetv2, lightweight attention module, and shallow feature fusion.
- Objective / loss: label supervision and pseudo-label supervision; exact loss formulas are not fully captured in the extracted sections.
- Optimization: SGD optimizer with polynomial learning-rate scheduler.
- Training data: labeled and unlabeled portions of industrial defect datasets.
- Data pipeline: labeled samples are fractions of the training set; remaining samples are used in the unlabeled branch.
- Augmentation / synthesis: random data enhancement at scale [0.5, 2.0] through geometric disturbances, non-geometric disturbances, and image erasure; feature perturbation is also used.
- Inference: evaluated with frame rate and inference time.
- Complexity / deployment constraints: lightweight network reduces parameters and preserves high frame rate.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial visual defect images.
- Output target: pixel-wise defect masks.
- Supervision: semi-supervised learning with labeled and unlabeled branches.
- Objective: improve mIoU under limited labeled masks.

### Model And Training

- Model family: semantic segmentation network.
- Architecture: improved DeepLabv3Plus with simplified MobileNetv2, lightweight attention module, shallow feature fusion, and two-branch perturbation cross-pseudo-supervision.
- Parameters: final model 11.52M parameters in ablation table.
- Losses: supervised and pseudo-label losses are used; exact loss terms not fully reported in extracted text.
- Optimizer: SGD with momentum 0.9.
- Hyperparameters: initial learning rate 0.001; initial prediction threshold 0.9.
- Seeds: not reported.
- Training compute: Ubuntu 22.04.1, GeForce RTX 3090 GPU, Intel Core i7-12700K CPU; PyTorch data-parallel/distributed training.

### Data

- Datasets: five self-built industrial datasets, [[KolektorSDD]], and a steel dataset from Kaggle.
- KolektorSDD size: 399 images reported in this paper, with 52 visible-defect images and 347 non-defect images.
- KolektorSDD split: 1/4 and 1/2 of training set as supervised learning part, with remaining images used as unsupervised branch.
- Steel dataset: 12,568 training images and 5,506 test images at 1600 x 256; 1/4 of training set labeled and remainder unlabeled.
- Labels / annotations: pixel-level defect masks for supervised samples.
- Augmentation: random geometric and non-geometric disturbances plus image erasure.
- Synthetic data: not reported.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: compare semi-supervised methods under label fractions; compare segmentation network backbones; public dataset evaluation; ablation of TPCPS, DeepLabv3+ modification, LAM, and SFF.
- Used performance metrics: mIoU, F1 score, pixel accuracy, mPA, inference time, frame rate, GPU memory.
- Primary metric: [[mIoU]].
- Metric direction / units: mIoU, F1, pixel accuracy, and mPA higher is better; inference time lower is better; FPS higher is better.
- Baselines: SupOnly, CPS, AEL, ST++, U2PL, GAT-seg, CCVC, AugSeg, DGCL; U-Net, PSPNet, DeepLabv3Plus, HRNet, SegNet.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Proposed method vs SOTA | KolektorSDD segmentation | mIoU | higher | not reported | +4.39% | Abstract-level claim against current SOTA. |
| Proposed DeepLabv3Plus vs original | Steel segmentation | mIoU (%) | higher | 79.38 | 82.37 | Table 10. |
| Proposed DeepLabv3Plus vs original | Steel segmentation | mPA (%) | higher | 84.45 | 90.98 | Table 10. |
| Final ablation configuration | Industrial segmentation | mIoU (%) | higher | 60.38 | 85.11 | Table 12. |
| Final ablation configuration | Industrial segmentation | Speed (fps) | higher | 55.01 | 64.59 | Table 12, not monotonic across ablations. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| mIoU | Segmentation quality | percent | higher | yes | Main reported metric. |
| F1 score | Segmentation quality | score | higher | no | Used in self-built datasets. |
| Pixel accuracy | Segmentation quality | percent | higher | no | Used in self-built datasets. |
| mPA | Mean pixel accuracy | percent | higher | no | Used for steel dataset. |
| FPS | Inference speed | frames per second | higher | no | Deployment metric. |

### Ablations

- Base: 60.38 mIoU, 30.02M parameters, 55.01 FPS.
- TPCPS: 71.79 mIoU, 31.42M parameters, 48.32 FPS.
- Modified DeepLabv3Plus: 68.56 mIoU, 9.08M parameters, 70.38 FPS.
- Adding LAM: 75.41 mIoU, 10.29M parameters, 67.77 FPS.
- Adding SFF: 80.36 mIoU, 10.31M parameters, 67.82 FPS.
- Final combination: 85.11 mIoU, 11.52M parameters, 64.59 FPS.

## Limitations

- Stated: future work could investigate more efficient architectures or compression to increase inference speed while preserving detection performance.
- Inferred: the paper reports gains from perturbation-based semi-supervision and network changes together; the exact independent contribution of random data enhancement alone is not isolated.

## Reproducibility

- Code: not reported in extracted text.
- Data: KolektorSDD is public; self-built datasets are described but availability is not reported in extracted text.
- Hyperparameters: optimizer, learning rate, prediction threshold, and augmentation scale are reported.
- Random seeds: not reported.
- Environment: Ubuntu 22.04.1, RTX 3090, Intel i7-12700K.
- Artifact status: open access PDF processed locally.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]].
- Methods: [[Pseudo-labeling]], [[Data augmentation]], perturbation consistency.
- Learning paradigm: [[Semi-supervised learning]].
- Datasets: [[KolektorSDD]].
- Domains: [[Metal inspection]].
- Metrics: [[mIoU]], [[F1-score]], [[FPS]].
- Models: [[DeepLabV3+]], [[MobileNet]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] | Shares dataset and task | Both evaluate defect segmentation on [[KolektorSDD]]. |
| [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] | Shares supervision theme | Both study surface-defect segmentation/detection with reduced annotation requirements. |

### Backlinks Updated

- [[KolektorSDD]], [[Metal inspection]], [[Data augmentation]], [[Pseudo-labeling]], and [[Semi-supervised learning]] link back to this paper.

## Questions

- Are the self-built industrial datasets publicly released?
- What exact loss functions and pseudo-label filtering rules are used beyond the extracted threshold value?
