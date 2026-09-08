---
title: "Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation"
aliases:
  - "Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation"
paper_key: "sha256:46aff253929882b434092f09c20ab59c73f732ae728c3230cd9fb86841d2eaa2"
paper_type: research
year: 2025
venue: "IJCAI 2025"
authors:
  - "Xiangyue Li"
  - "Xiaoyang Wang"
  - "Zhibin Wan"
  - "Quan Zhang"
  - "Yupei Wu"
  - "Tao Deng"
  - "Mingjie Sun"
status: processed
processed_at: 2026-06-12
topics:
  - "image-mask aligned anomaly generation"
  - "diffusion augmentation"
tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Real-IAD]]"
methods:
  - "[[Image-mask aligned diffusion synthesis]]"
  - "[[Diffusion models]]"
  - "[[Defect synthesis]]"
model_family:
  - "[[Diffusion models]]"
architectures:
  - "Stable Diffusion"
  - "Segformer"
losses:
  - "Alignment Regularization loss"
  - "Generative Feedback loss"
optimizers:
  - "AdamW"
metrics:
  - "[[mIoU]]"
  - "[[Dice score]]"
  - "[[FID]]"
  - "[[Inception Score]]"
  - "[[LPIPS]]"
primary_metric: "[[mIoU]]"
baselines:
  - "AnomalyDiffusion"
  - "ArSDM"
benchmarks:
  - "[[MVTec AD]]"
  - "[[Real-IAD]]"
evaluation_protocol: "synthetic image quality metrics and downstream segmentation mDice/mIoU after training Segformer with real plus synthetic samples"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2025 - Li - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation.pdf"
code: "https://github.com/huanyin/anomaly-alignment"
data: "not reported"
doi: "not reported"
arxiv: "not reported"
related_methods:
  - "[[Image-mask aligned diffusion synthesis]]"
  - "[[Diffusion models]]"
  - "[[Defect synthesis]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[Real-IAD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
concept_notes_created_or_updated:
  - "[[Image-mask aligned diffusion synthesis]]"
source_file: "paper-inbox/10_processed/Research/2025 - Li - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Li - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Li - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation.txt"
artifact_status: "code reported"
tags:
  - paper
---

# Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation

## Summary

The paper addresses label drift in mask-guided anomaly generation, where generated defects do not align with their conditioning masks. It trains a dual-branch Stable Diffusion generator to denoise both images and masks and adds an Alignment Regularization loss to improve image-mask correspondence. It also uses the trained generator during segmentation training through a Generative Feedback loss. Compared with AnomalyDiffusion, the method improves downstream segmentation mIoU by 1.07 points on [[MVTec AD]], 5.03 points on [[Real-IAD]], and 16.63 points on Floor Dirty.

## Paper Type

- Type: research.
- Why: It proposes diffusion-training losses and evaluates synthetic data quality plus downstream segmentation performance.

## Problem

- Task: anomaly image generation and [[Defect segmentation]].
- Setting: limited real anomaly samples and mask labels.
- Inputs: real images, anomaly masks, noisy latent image features, and text embeddings.
- Outputs: synthetic anomaly images for training and improved segmentation masks from a downstream model.
- Motivation: mask-guided generation can create false training signals when generated anomaly pixels do not align with conditioning masks.
- Assumptions: the denoising loss of a well-aligned diffusion generator can act as a feedback signal for segmentation-mask quality.

## Contribution

- Claimed: introduces dual-branch training that generates anomaly images and masks simultaneously.
- Claimed: introduces Alignment Regularization loss to improve image-mask correspondence.
- Claimed: introduces Generative Feedback loss that uses the trained generator to fine-tune a segmentation model.
- Shown: improves downstream segmentation on industrial, medical, and indoor anomaly datasets.

## Method

- Core idea: train a diffusion model to learn image-mask alignment and use that learned alignment both for synthetic data generation and segmentation feedback.
- Architecture / algorithm: Stable Diffusion with LoRA-based image conditioning; Segformer is the baseline segmentation model.
- Objective / loss: Stable Diffusion denoising loss, Alignment Regularization loss, cross-entropy segmentation loss, and Generative Feedback loss.
- Optimization: AdamW.
- Training data: real image-mask pairs; 100 image-mask pairs are used in the polyp synthetic-quality comparison.
- Data pipeline: fine-tune Stable Diffusion on real samples, use real masks to generate synthetic samples, combine real and synthetic samples to train Segformer, then refine with Generative Feedback.
- Augmentation / synthesis: [[Image-mask aligned diffusion synthesis]].
- Inference: only the image-generation branch is activated for synthetic sample generation.

## Evidence

### Experimental Setup

- Datasets: medical polyp datasets, [[MVTec AD]], [[Real-IAD]], and Floor Dirty.
- Baselines: AnomalyDiffusion and ArSDM for generation/synthetic data; Segformer for segmentation.
- Used performance metrics: FID, Inception Score, LPIPS, mIoU, and Dice.
- Implementation: inputs and outputs are 512 x 512; learning rate 1e-5; batch size 4; classifier-free guidance scale 7; Alignment Regularization factor alpha 0.7.
- Code: `https://github.com/huanyin/anomaly-alignment`.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Synthetic quality | Polyp generation | FID | lower | ArSDM 361.55 | 162.01 | 100 real image-mask pairs. |
| Synthetic quality | Polyp generation | Inception Score | higher | ArSDM 1.98 | 3.25 | 100 real image-mask pairs. |
| Synthetic quality | Polyp generation | LPIPS | lower | ArSDM 0.869 | 0.698 | 100 real image-mask pairs. |
| Segmentation | MVTec AD | mIoU | higher | AnomalyDiffusion 71.84 | 72.91 | +1.07 points. |
| Segmentation | MVTec AD | mDice | higher | AnomalyDiffusion 77.60 | 78.62 | +1.02 points. |
| Segmentation | Real-IAD average | mIoU | higher | AnomalyDiffusion 65.13 | 70.16 | +5.03 points. |
| Segmentation | Floor Dirty average | mIoU | higher | AnomalyDiffusion 34.87 | 51.50 | +16.63 points. |

### Ablations

- Alignment Regularization alone improves polyp average mDice from 81.21 to 87.11 and mIoU from 73.65 to 80.46.
- Generative Feedback alone improves mDice to 87.28 and mIoU to 80.51.
- Combining both reaches 87.59 mDice and 81.34 mIoU, a +6.38 mDice and +7.69 mIoU improvement over the baseline.
- Increasing generative-model training samples from 50 to 150 improves mIoU from 78.80 to 82.22; 20 samples drops to 47.27 mIoU.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mIoU]] | downstream anomaly segmentation | mean intersection over union, percent | higher | yes | Reported for MVTec AD, Real-IAD, Floor Dirty, and polyp ablations. |
| [[Dice score]] / mDice | downstream segmentation | mean Dice coefficient, percent | higher | no | Reported with mIoU in segmentation comparisons and ablations. |
| [[FID]] | synthetic image quality | distribution distance | lower | no | Ours 162.01 versus ArSDM 361.55 on polyp generation. |
| [[Inception Score]] | synthetic image quality | image quality/diversity score | higher | no | Ours 3.25 versus ArSDM 1.98 on polyp generation. |
| [[LPIPS]] | synthetic image quality | perceptual distance | lower | no | Ours 0.698 versus ArSDM 0.869 on polyp generation. |

## Dataset / Benchmark Details

- [[MVTec AD]] and [[Real-IAD]] are the reported industrial anomaly segmentation datasets.
- Floor Dirty is used as an indoor anomaly dataset.
- Polyp datasets are used for medical anomaly segmentation and synthetic quality comparisons.
- License: not reported.

## Limitations

- Stated: with only 20 training samples for the generative model, segmentation mIoU drops substantially due to insufficient diffusion fine-tuning and synthetic misalignment.
- Inferred: the method depends on available masks to guide generation; it is less directly applicable when no anomaly masks exist.

## Reproducibility

- Code: `https://github.com/huanyin/anomaly-alignment`.
- Optimizer: AdamW.
- Hyperparameters: learning rate 1e-5, batch size 4, 512 x 512 images, classifier-free guidance scale 7, alpha 0.7.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Industrial anomaly detection]]
- Methods: [[Image-mask aligned diffusion synthesis]], [[Diffusion models]], [[Defect synthesis]]
- Datasets: [[MVTec AD]], [[Real-IAD]]
- Benchmarks: [[MVTec AD]], [[Real-IAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mIoU]], [[Dice score]], [[FID]], [[Inception Score]], [[LPIPS]]

### Shares Dataset

- [[MVTec AD]] and [[Real-IAD]] anchor the industrial anomaly segmentation evaluation.

### Shares Method

- [[Image-mask aligned diffusion synthesis]]: central method introduced here.
- [[Diffusion models]]: used as the generative model family.
- [[Defect synthesis]]: generated samples augment downstream segmentation training.

### Shares Task

- [[Defect segmentation]]: downstream segmentation is the main evaluated task.

## Questions

- How well does Generative Feedback work with segmentation models other than Segformer?
- Can image-mask alignment regularization help when masks are noisy or weak labels rather than ground truth?
