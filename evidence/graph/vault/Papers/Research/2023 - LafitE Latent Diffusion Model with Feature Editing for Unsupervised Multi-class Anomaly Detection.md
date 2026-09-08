---
title: "LafitE: Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection"
aliases:
  - "LafitE"
paper_key: "arxiv:2307.08059"
paper_type: research
year: 2023
venue: "arXiv"
authors:
  - "Haonan Yin"
  - "Guanlong Jiao"
  - "Qianhui Wu"
  - "Borje F. Karlsson"
  - "Biqing Huang"
  - "Chin-Yew Lin"
status: processed
processed_at: 2026-06-11
topics:
  - "unsupervised anomaly detection"
  - "latent diffusion"
  - "feature editing"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Unsupervised anomaly detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[MPDD]]"
methods:
  - "[[LafitE]]"
  - "[[Diffusion models]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Diffusion models]]"
optimizers:
  - "[[AdamW]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PR]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "UniAD"
  - "RevDistill"
evaluation_protocol: "normal-only unsupervised anomaly detection and localization on MVTec AD and MPDD, with five random seeds"
hardware: "one NVIDIA GeForce RTX 3090 24GB GPU"
doi: "not reported"
arxiv: "2307.08059"
url: "https://arxiv.org/abs/2307.08059"
pdf: "paper-inbox/10_processed/Research/2023 - Yin - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection.pdf"
code: "not reported"
data: "uses MPDD and MVTec AD"
related_methods:
  - "[[LafitE]]"
  - "[[Diffusion models]]"
related_datasets:
  - "[[MPDD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Yin - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Yin - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Yin - LafitE Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection.txt"
tags:
  - paper
---
# LafitE: Latent Diffusion Model with Feature Editing for Unsupervised Multi-class Anomaly Detection

## Summary

The paper proposes [[LafitE]], a latent feature-space diffusion method for unsupervised multi-class anomaly detection. It extracts hierarchical EfficientNet-b4 patch features, edits query patches through a normal-feature memory bank, reconstructs edited features with a DDIM-style diffusion model, and scores anomalies by feature reconstruction error. The paper evaluates on MVTec AD and [[MPDD]], where LafitE improves image-level detection and pixel-level localization AUROC over strong normal-only baselines.

## Paper Type

- Type: research.
- Why: The paper proposes a method and reports quantitative anomaly detection and localization results.

## Problem

- Task: [[Industrial anomaly detection]] and localization with normal-only training data.
- Setting: multi-class industrial visual inspection, including complex metal-part acquisition conditions in [[MPDD]].
- Inputs: normal training images and test images containing normal or anomalous samples.
- Outputs: image-level anomaly scores and pixel-level anomaly maps.

## Contribution

- Claimed: A latent diffusion anomaly detector with feature editing that forces reconstructed features toward normal patch neighborhoods.
- Shown: LafitE improves average Det/Loc AUROC on [[MPDD]] from UniAD's 87.5/95.6 to 96.5/99.0.
- Inferred: The feature-editing step is most important on MPDD, where LafitE without feature editing falls to 93.6/98.3 Det/Loc AUROC.

## Method

- Feature extraction: an ImageNet-pretrained EfficientNet-b4 produces hierarchical patch features aggregated to a 32x32 feature tensor.
- Synthesis / diffusion: a U-Net diffusion model learns to denoise latent feature tensors with a cosine noise schedule and DDIM-style inference.
- Feature editing: each query patch representation is replaced by a weighted combination of top-K nearest normal memory-bank patches before denoising.
- Anomaly scoring: L2 reconstruction error between denoised and original feature tensors is upsampled and Gaussian-smoothed for localization; image-level scores use average pooling and max pooling.
- Pseudo-validation: pseudo anomalies are synthesized from normal images with masks and fragments inspired by CutPaste for hyperparameter selection.

## ML / DL Extraction

- Architecture: EfficientNet-b4 feature extractor and U-Net diffusion model with base channel 256 and channel multipliers 1, 2, 3, and 4.
- Optimizer: [[AdamW]], weight decay 1e-4, initial learning rate 1e-4, learning-rate drop by 0.1 after 800 epochs.
- Training: 1000 epochs, batch size 64, max diffusion step T=1000, 10% memory core-set keep rate, Gaussian kernel deviation 4.
- Preprocessing: images resized to 224x224; no other enhancement is reported.
- Compute: one NVIDIA GeForce RTX 3090 24GB GPU.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| Main comparison | [[MPDD]] detection | [[AU-ROC]] | UniAD 87.5 | LafitE 96.5 +/- 0.08 | Higher is better. |
| Main comparison | [[MPDD]] localization | [[AU-ROC]] | UniAD 95.6 | LafitE 99.0 +/- 0.01 | Higher is better. |
| Ablation | [[MPDD]] detection | [[AU-ROC]] | LafitE without feature editing 93.6 | LafitE 96.5 | Feature editing improves detection. |
| Ablation | [[MPDD]] localization | [[AU-ROC]] | LafitE without feature editing 98.3 | LafitE 99.0 | Feature editing improves localization. |
| Main comparison | MVTec AD detection | [[AU-ROC]] | UniAD 96.5 | LafitE 98.5 +/- 0.03 | Higher is better. |
| Main comparison | MVTec AD localization | [[AU-ROC]] | UniAD 96.8 | LafitE 97.6 +/- 0.02 | Higher is better. |

## Dataset / Benchmark Details

- [[MPDD]]: six metal-part classes, 888 normal training images, 176 normal test images, 282 anomalous test images, 1024x1024 resolution, and pixel-level anomaly masks.
- MVTec AD: 3629 normal train/validation images and 1725 test images across 15 categories.

## Limitations

- The pseudo-validation set has a gap from real test behavior, and the authors identify pseudo-validation improvement as future work.
- Code availability: not reported.
- MPDD licensing: not reported in the paper text.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Unsupervised anomaly detection]]
- Methods: [[LafitE]], [[Diffusion models]], [[Data augmentation]]
- Datasets: [[MPDD]]
- Domains: [[Metal inspection]]
- Metrics: [[AU-ROC]], [[AU-PR]]

### Relationship Notes

- Shares dataset: [[MPDD]].
- Shares method: [[Diffusion models]] and [[LafitE]].
- Shares metric: [[AU-ROC]] and [[AU-PR]].
- Application/domain: [[Metal inspection]].

## Questions

- Can feature editing be made less dependent on memory-bank nearest-neighbor quality under large pose and lighting shifts?
- Does pseudo-validation select the same hyperparameters as real anomalous validation data when real anomalies are available?
