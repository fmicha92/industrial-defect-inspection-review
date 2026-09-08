---
title: Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection
aliases:
  - Texture conditioned GAN based self supervised framework for fabric defect detection
  - STDAN fabric defect detection
paper_key: doi:10.1038/s41598-026-51763-w
paper_type: research
year: 2026
venue: Scientific Reports
authors:
  - R. Sujitha
  - K. Venkatasalam
status: processed
processed_at: 2026-06-05
topics:
  - fabric defect detection
  - self-supervised anomaly detection
  - texture decomposition
  - feature-level defect amplification
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[FabricSpotDefect]]"
  - "[[FD_Dataset]]"
  - "[[Lusitano]]"
methods:
  - "[[STDAN]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Self-supervised learning]]"
  - "[[GAN]]"
model_family:
  - "[[Anomaly Detection Models]]"
  - "[[Computer Vision Models]]"
architectures:
  - "[[STDAN]]"
  - CNN-Transformer hybrid texture-consistency encoder
losses:
  - contrastive loss
  - reconstruction loss
  - GAN adversarial loss
optimizers:
  - "[[Adam]]"
training_regime: Self-supervised normal-only training with contrastive learning and feature-level defect amplification.
augmentation:
  - Flip
  - Crop
  - Color Jitter
synthetic_data: Feature-level defect amplification creates amplified residual anomaly features as pseudo-negative samples; pixel-level synthesis is used only as an ablation comparator.
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[AU-ROC]]"
  - "[[Localization precision]]"
  - "[[Feature embedding separation]]"
  - "[[Texture robustness]]"
  - "[[Defect sensitivity]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - AnoGAN
  - SPADE
  - PaDiM
  - PatchCore
code: not reported
data: "reported available: https://figshare.com/articles/dataset/FD_Dataset_7z/25546465 and https://doi.org/10.5281/zenodo.19382704"
doi: 10.1038/s41598-026-51763-w
url: https://doi.org/10.1038/s41598-026-51763-w
pdf: paper-inbox/10_processed/Research/2026 - Sujitha - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection.pdf
source_file: paper-inbox/10_processed/Research/2026 - Sujitha - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection.pdf
preprocessed_input: paper-inbox/90_processing/analysis-inputs/2026 - Sujitha - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection.md
extracted_text: paper-inbox/90_processing/text/2026 - Sujitha - Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection.txt
artifact_status: data links reported; code not reported
related_papers:
  - "[[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]]"
  - "[[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]]"
  - "[[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]]"
related_concepts:
  - "[[Unsupervised anomaly detection]]"
  - "[[Self-supervised learning]]"
  - "[[Textile defect detection]]"
related_methods:
  - "[[STDAN]]"
  - "[[GAN]]"
related_datasets:
  - "[[FabricSpotDefect]]"
  - "[[FD_Dataset]]"
  - "[[Lusitano]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect detection]]"
  - "[[Defect segmentation]]"
concept_notes_created_or_updated:
  - "[[STDAN]]"
  - "[[Localization precision]]"
  - "[[Feature embedding separation]]"
  - "[[Texture robustness]]"
  - "[[Defect sensitivity]]"
tags:
  - paper
  - fabric-defect-detection
  - anomaly-detection
---

# Texture Conditioned GAN Based Self Supervised Framework for Fabric Defect Detection

## Summary

Sujitha and Venkatasalam propose [[STDAN]], a self-supervised fabric anomaly-detection framework that combines texture decomposition, feature-level defect amplification, and contrastive learning. The method is trained from defect-free fabric images and is evaluated on [[FabricSpotDefect]], [[FD_Dataset|FD_Dataset]], and [[Lusitano]]. The strongest source-supported result for the related Figshare dataset is 97.56% AUC, 95.91% precision, 94.88% recall, and 95.39% F1-score on FD_Dataset.

## Paper Type

Research paper. It introduces and evaluates a new self-supervised anomaly-detection framework for fabric defect detection and localization; it uses public datasets rather than introducing the [[FD_Dataset]].

## Problem

Fabric inspection needs methods that can detect small, low-contrast, and previously unseen defects on woven, knitted, jacquard, and patterned surfaces. The paper frames supervised and weakly supervised approaches as costly to scale because pixel-level defect annotations are expensive and incomplete for industrial variability. It formulates the task as normal-only self-supervised anomaly detection: train on defect-free fabric images, then detect and localize defects at inference time without defect annotations.

## Contribution

- Claimed: [[STDAN]] decomposes fabric representations into normal texture bases and residual anomaly cues without requiring defect markings.
- Claimed: feature-level defect amplification perturbs residual anomaly features in latent space rather than synthesizing pixel-level defects, reducing unrealistic artifact risk.
- Shown: on FD_Dataset, the paper reports 97.56% AUC, 95.91% precision, 94.88% recall, and 95.39% F1-score.
- Shown: the full model outperforms the no-amplification and pixel-level augmentation ablations in Table 7, reaching 98.21% AUC and 96.28% F1-score in the reported ablation setting.
- Inferred: the paper is useful for the [[FD_Dataset]] note as an external user of the Figshare dataset, not as the dataset's source of record.

## Method

[[STDAN]] has four main components:

- Texture-consistency encoder: a hybrid CNN-Transformer encoder using a ResNet-style convolutional backbone followed by Transformer encoder blocks to represent local texture features and long-range texture correlations.
- Texture decomposition: encoded features are decomposed into normal texture bases, activation coefficients, and residual anomaly features.
- Feature-level defect amplification: residual anomaly features are perturbed with controlled stochastic variations and passed through a GAN-based feature amplification module to form pseudo-negative anomaly features.
- Self-supervised contrastive learning: normal texture features and amplified defect features are embedded so normal textures cluster while amplified defect embeddings are separated.

Inference uses learned normal texture representations to compute anomaly scores and pixel-level defect heatmaps.

## Evidence

### Dataset Results

| Dataset | AUC (%) | Precision (%) | Recall (%) | F1-score (%) |
|---|---:|---:|---:|---:|
| [[FabricSpotDefect]] | 98.21 | 96.84 | 95.73 | 96.28 |
| [[FD_Dataset]] | 97.56 | 95.91 | 94.88 | 95.39 |
| [[Lusitano]] | 96.74 | 94.63 | 93.52 | 94.07 |

### Baseline Comparison

| Method | Learning type | Image-level AUC (%) | Pixel-level AUC (%) | Localization precision (%) | Limitation reported |
|---|---|---:|---:|---:|---|
| AnoGAN | GAN reconstruction | 86.4 | 82.1 | 79.3 | pixel reconstruction blur |
| SPADE | feature embedding | 90.7 | 87.5 | 85.2 | sensitive to texture variation |
| PaDiM | distribution modeling | 92.3 | 89.1 | 87.6 | no anomaly enhancement |
| PatchCore | memory-based nearest neighbor | 93.8 | 90.4 | 88.9 | lacks texture semantics |
| [[STDAN]] | texture decomposition plus self-supervised learning | 97.0 | 94.6 | 91.0 | not reported |

### Ablation

| Variant | Description | AUC (%) | Precision (%) | Recall (%) | F1-score (%) |
|---|---|---:|---:|---:|---:|
| Variant A | STDAN without defect amplification | 95.83 | 93.42 | 92.11 | 92.76 |
| Variant B | Pixel-level defect augmentation | 96.41 | 94.05 | 93.27 | 93.65 |
| Full [[STDAN]] | Feature-level defect amplification | 98.21 | 96.84 | 95.73 | 96.28 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported value |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection and ROC analysis | Area under ROC curve, percent | higher | yes | 97% overall; 97.56% on FD_Dataset |
| [[Accuracy]] | Normal/defective classification | percent correct | higher | no | 95% detection accuracy |
| [[Localization precision]] | Pixel-level defect heatmap alignment | percent spatial precision | higher | no | 91% |
| [[Feature embedding separation]] | Normal-vs-defect latent separation | inter-class distance | higher | no | 1.99 |
| [[Texture robustness]] | Consistency across texture categories | average AUC across texture categories | higher | no | 92% |
| [[Defect sensitivity]] | Detection of weak or subtle anomalies | TP / (TP + FN), percent | higher | no | 97% |
| [[Precision]] | Dataset-level anomaly detection | percent | higher | no | 95.91% on FD_Dataset |
| [[Recall]] | Dataset-level anomaly detection | percent | higher | no | 94.88% on FD_Dataset |
| [[F1-score]] | Dataset-level anomaly detection | percent | higher | no | 95.39% on FD_Dataset |

## ML/DL Extraction

- Task formulation: self-supervised fabric anomaly detection and localization.
- Input: fabric images from public fabric inspection datasets.
- Output: anomaly score and pixel-level defect heatmap.
- Supervision: normal-only training; normal and defective samples are used in testing.
- Architecture: CNN-Transformer texture-consistency encoder, texture decomposition module, GAN-based feature-level defect amplification module, contrastive embedding module, and anomaly scoring/localization head.
- Objective / losses: contrastive objective, reconstruction loss for texture decomposition, GAN adversarial loss, and feature consistency regularization.
- Optimizer: [[Adam]] with learning rate 1e-4.
- Training setup: batch size 16; 100-500 training iterations; input resolution 256 x 256 or 512 x 512.
- Augmentation: flip, crop, and color jitter.
- Hardware: NVIDIA GPU, with RTX 2080 Ti given as an example.
- Framework: PyTorch / TensorFlow.
- Code: not reported.
- Data: two links reported in the data availability statement, including the Figshare FD_Dataset URL and a Zenodo DOI.

## Limitations

- The method assumes the normal-only training data are highly free of defects; contaminated normal data can reduce performance.
- Feature-level amplification adds computational cost during training.
- Extreme illumination changes and severe geometric distortions can produce false positives or missed defects.
- Future work is stated for resilience to polluted training data, lower computational complexity, and multimodal inspection such as infrared or hyperspectral fabric analysis.
- Dataset split counts for each evaluated dataset are not reported in the extracted text beyond the general normal-only training and normal/defective testing protocol.

## Connections

### Graph Hubs

- Datasets: [[FD_Dataset]] is used as FD_Dataset in the evaluation and is linked through the Figshare URL in the data availability statement.
- Related datasets: [[FabricSpotDefect]] and [[Lusitano]] are also evaluated.
- Tasks: [[Textile defect detection]], [[Defect detection]], and [[Defect segmentation]].
- Domains: [[Textile and fiber inspection]].
- Methods: [[STDAN]], [[Unsupervised anomaly detection]], [[Self-supervised learning]], and [[GAN]].
- Metrics: [[AU-ROC]], [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[Localization precision]], [[Feature embedding separation]], [[Texture robustness]], and [[Defect sensitivity]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - FabricSpotDefect An Annotated Dataset for Identifying Spot Defects in Different Fabric Types]] | Shares dataset | This paper evaluates STDAN on FabricSpotDefect, while the earlier paper introduces that dataset and its annotations. |
| [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] | Shares dataset and task | This paper evaluates STDAN on Lusitano, while the earlier paper introduces Lusitano for one-class fabric anomaly detection. |
| [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] | Shares method family | Both address unsupervised or self-supervised anomaly localization by separating normal features from synthetic or amplified abnormal representations. |

### Backlinks Updated

- [[FD_Dataset]] links this paper as a dataset user and records the FD_Dataset result values.
- [[Textile defect detection]] links this paper as a self-supervised fabric anomaly-detection method.
- [[Textile and fiber inspection]] links this paper as a textile inspection research contribution.
- [[Unsupervised anomaly detection]] and [[Self-supervised learning]] link this paper through its normal-only, contrastive anomaly-detection setup.
- The paper-specific metric notes link back to this paper and the anomaly-detection metric family.

## Questions

- Which exact split counts were used for FabricSpotDefect, FD_Dataset, and Lusitano in the STDAN experiments?
- Does the reported Zenodo DOI correspond to Lusitano, another evaluated dataset, or experiment artifacts?
- How sensitive is STDAN to contamination in normal training images on real production datasets?
