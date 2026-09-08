---
title: "SeaS: Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning"
aliases:
  - "SeaS"
  - "SeaS: Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning"
paper_key: "doi:10.48550/arxiv.2410.14987"
paper_type: research
year: 2025
venue: "arXiv"
authors:
  - "Zhewei Dai"
  - "Shilei Zeng"
  - "Haotian Liu"
  - "Xurui Li"
  - "Feng Xue"
  - "Yu Zhou"
status: processed
processed_at: 2026-05-22
topics:
  - "few-shot anomaly generation"
  - "industrial anomaly image generation"
  - "diffusion-based synthetic data"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MVTec3D]]"
methods:
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
  - "[[Few-shot zero-shot learning]]"
  - "[[Diffusion models]]"
  - "[[U-Net]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "Stable Diffusion v1-4"
  - "U-Net"
  - "VAE decoder"
  - "BiSeNet V2"
  - "UPerNet"
  - "LFD"
metrics:
  - "[[Inception Score]]"
  - "[[LPIPS]]"
  - "[[KID]]"
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
  - "[[IoU]]"
primary_metric: "[[IoU]]"
metric_definitions:
  - "IS: Inception Score for generated anomaly-image authenticity; higher is better."
  - "IC-LPIPS: intra-cluster pairwise LPIPS for generated-image diversity; higher is better."
  - "KID: Kernel Inception Distance for generated normal-image authenticity; lower is better."
  - "IC-LPIPS(a): intra-cluster pairwise LPIPS computed only inside anomaly regions; higher is better."
  - "AUROC, AP, and F1-max: anomaly detection or segmentation metrics; higher is better."
  - "IoU: segmentation overlap between predicted and target anomaly mask; higher is better."
baselines:
  - "Crop&Paste"
  - "SDGAN"
  - "Defect-GAN"
  - "DFMGAN"
  - "AnomalyDiffusion"
  - "DRAEM"
  - "GLASS"
  - "HVQ-Trans"
  - "PatchCore"
  - "MambaAD"
benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MVTec3D]]"
code: "reported available: https://github.com/HUST-SLOW/SeaS"
data: "uses MVTec AD, VisA, and RGB images from MVTec 3D AD"
doi: "10.48550/arxiv.2410.14987"
arxiv: "2410.14987"
url: "https://arxiv.org/abs/2410.14987"
pdf: "paper-inbox/10_processed/Research/2025 - Dai - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
  - "[[Few-shot zero-shot learning]]"
  - "[[Diffusion models]]"
  - "[[U-Net]]"
  - "[[AnomalyDiffusion]]"
  - "[[GLASS]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MVTec3D]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec AD]]"
  - "[[VisA]]"
  - "[[MVTec3D]]"
source_file: "paper-inbox/10_processed/Research/2025 - Dai - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Dai - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Dai - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning.txt"
artifact_status: "code reported available"
tags:
  - paper
---

# SeaS: Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning

## Summary

SeaS is a few-shot industrial anomaly image generation method built by fine-tuning Stable Diffusion v1-4. It trains one shared U-Net per product rather than one model per anomaly type, separates normal-product and anomaly tokens with an Unbalanced Abnormal text prompt, and adds a Refined Mask Prediction branch to generate paired anomaly images and masks. The paper evaluates generation quality and downstream anomaly detection / segmentation on [[MVTec AD]], [[VisA]], and RGB images from [[MVTec3D]].

## Paper Type

- Type: research.
- Why: The paper proposes a generation and mask-prediction method, compares it against synthesis and anomaly-detection baselines, reports ablations, and releases code.

## Problem

- Task: few-shot industrial anomaly image generation for [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: multi-category industrial inspection where anomalies vary strongly but normal products should remain globally consistent.
- Inputs: a small set of normal images and masked anomaly images per anomaly type.
- Outputs: generated anomaly images, generated normal images, and anomaly masks paired with generated images.
- Motivation: prior industrial generation methods often focus only on anomalies or normal products, or require separate anomaly-specific models.

## Contribution

- Claimed: SeaS uses Separation and Sharing fine-tuning to represent normal products and multiple anomaly attributes in one product-level diffusion model.
- Shown: SeaS improves generation fidelity/diversity metrics, improves synthesis-based anomaly detectors when replacing their pseudo-anomalies, and improves supervised segmentation models trained on generated image-mask pairs.
- Shown: Ablations indicate that typical text prompts, removing mixed training, removing Normal-image Alignment, or removing the second term of Decoupled Anomaly Alignment reduce generation quality and downstream segmentation performance.

## Method

- Base model: pre-trained Stable Diffusion v1-4 with U-Net denoiser, CLIP text conditioning, and VAE decoder.
- Unbalanced Abnormal text prompt: `a <ob> with <df1>, <df2>, ..., <dfN>`, where one normal token represents globally consistent product appearance and multiple anomaly tokens capture varied anomaly attributes.
- Decoupled Anomaly Alignment loss: aligns anomaly-token cross-attention maps to anomaly regions and suppresses the normal-token response in anomaly regions.
- Normal-image Alignment loss: trains the normal token on normal images to preserve globally consistent but locally varied normal products.
- Mixed training: samples the same number of abnormal and normal images into each fine-tuning batch to reduce overfitting and increase anomaly diversity.
- Refined Mask Prediction branch: fuses discriminative U-Net decoder features with high-resolution VAE decoder features through cascaded Mask Refinement Modules, producing 512 x 512 anomaly masks.
- Training setup: for anomaly generation, the paper uses 60 normal images and 13 masked anomaly images per anomaly type, trains one generative model per product covering all anomaly types, and generates 1,000 anomaly image-mask pairs per anomaly type during inference.

## ML / DL Extraction

### Data

- [[MVTec AD]]: 15 product categories, each with up to 8 anomaly types.
- [[VisA]]: 12 objects in 3 domains.
- [[MVTec3D]]: 10 product categories, each with up to 4 anomaly types; the paper uses RGB images only and notes lighting and pose variation challenges.
- Synthetic outputs: anomaly images, anomaly masks, and normal images.
- License: not reported in the paper text read for this audit.

### Evaluation

- Generation baselines: Crop&Paste, SDGAN, Defect-GAN, DFMGAN, and [[AnomalyDiffusion]].
- Synthesis-based AD integration: DRAEM and [[GLASS]], where their original pseudo-anomalies are replaced with SeaS-generated anomalies.
- Normal-image augmentation integration: HVQ-Trans, PatchCore, and MambaAD, where SeaS-generated normal images supplement training.
- Supervised segmentation integration: BiSeNet V2, UPerNet, and LFD trained using generated image-mask pairs from DFMGAN, [[AnomalyDiffusion]], or SeaS.
- Metrics: IS, IC-LPIPS, KID, IC-LPIPS(a), AUROC, AP, F1-max, and IoU.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Anomaly generation quality | [[MVTec AD]] | IS | higher | [[AnomalyDiffusion]]: 1.80 | SeaS: 1.88 | Table 1; SeaS also reports IC-LPIPS 0.34 and KID 0.04. |
| Anomaly generation quality | [[VisA]] | IS | higher | DFMGAN: 1.25 | SeaS: 1.27 | Table 1; SeaS reports KID 0.02. |
| Anomaly generation quality | [[MVTec3D]] RGB | IS | higher | DFMGAN: 1.80 | SeaS: 1.95 | Table 1; SeaS reports IC-LPIPS(a) 0.09. |
| Replace DRAEM pseudo-anomalies | [[MVTec AD]] | Pixel IoU | higher | DRAEM: 60.30 | DRAEM + SeaS: 58.87 | Table 2; image-level and most pixel metrics improve, but IoU drops in this row. |
| Replace DRAEM pseudo-anomalies | [[VisA]] | Pixel IoU | higher | DRAEM: 13.57 | DRAEM + SeaS: 35.00 | Table 2; large segmentation-overlap gain. |
| Replace DRAEM pseudo-anomalies | [[MVTec3D]] RGB | Pixel IoU | higher | DRAEM: 12.42 | DRAEM + SeaS: 17.07 | Table 2. |
| Replace GLASS pseudo-anomalies | [[MVTec AD]] | Image AUROC | higher | GLASS: 99.92 | GLASS + SeaS: 99.97 | Table 2; small gain because baseline is already saturated. |
| SeaS normal-image augmentation | [[VisA]] | Image AUROC average | higher | Average of HVQ-Trans/PatchCore/MambaAD: 93.05 | Average + SeaS: 93.77 | Table 3. |
| SeaS normal-image augmentation | [[MVTec3D]] RGB | Image AUROC average | higher | Average of HVQ-Trans/PatchCore/MambaAD: 79.17 | Average + SeaS: 81.27 | Table 3. |
| Supervised segmentation with generated pairs | [[MVTec AD]] | Average IoU | higher | DFMGAN average: 45.99; AnomalyDiffusion average: 46.49 | SeaS average: 57.66 | Table 4; source narrative reports +11.17 percentage points on MVTec AD. |
| Supervised segmentation with generated pairs | [[VisA]] | Average IoU | higher | DFMGAN average: 10.52; AnomalyDiffusion average: 17.69 | SeaS average: 29.40 | Table 4; source narrative reports +11.71 percentage points on VisA. |
| Supervised segmentation with generated pairs | [[MVTec3D]] RGB | Average IoU | higher | DFMGAN average: 16.42; AnomalyDiffusion average: 19.88 | SeaS average: 35.37 | Table 4; source narrative reports +15.49 percentage points on MVTec 3D AD. |
| Image-level anomaly detection from segmentation maps | [[MVTec AD]] / [[VisA]] / [[MVTec3D]] | Image AUROC | higher | generated-pair baselines | +2.77 / +5.92 / +6.68 percentage points | Source narrative after Table 4. |

### Ablations

| Ablation | Metric set | Result |
|---|---|---|
| Generation model components | IS / IC-LPIPS / AUROC / AP / F1-max / IoU | Full SeaS reaches 1.88 IS, 0.34 IC-LPIPS, 97.21 AUROC, 69.21 AP, 66.37 F1-max, and 55.28 IoU; all ablated variants are lower in downstream IoU. |
| Typical text prompt | IoU | 50.46 versus 55.28 for full SeaS. |
| Without mixed training | IoU | 53.11 versus 55.28 for full SeaS. |
| Without Normal-image Alignment | IoU | 53.97 versus 55.28 for full SeaS. |
| Without second term of Decoupled Anomaly Alignment | IoU | 54.99 versus 55.28 for full SeaS. |
| RMP branch | IoU | Full RMP with MRM, progressive refinement, and coarse-mask supervision reaches 55.28 IoU; partial variants range from 49.42 to 53.93. |

## Dataset / Benchmark Details

- Source benchmarks: [[MVTec AD]], [[VisA]], and RGB-only [[MVTec3D]].
- Training inputs for generation: 60 normal images and 13 masked anomaly images per anomaly type.
- Generated data volume: 1,000 anomaly image-mask pairs per anomaly type during inference.
- Segmentation training: generated image-mask pairs plus all normal images from original training sets; the source states all compared generative methods use the same number of images and training settings.
- Leakage risks: the paper states supervised segmentation models are tested on remaining images not included in training; further split details are deferred to appendix material not captured in the main text.

## Limitations

- Stated: not reported as a separate limitations section in the read source.
- Inferred: some downstream improvements are small or mixed when baseline methods are already saturated; for example DRAEM + SeaS improves many metrics but lowers MVTec AD pixel IoU from 60.30 to 58.87 in Table 2.
- Inferred: the method relies on masked anomaly images for fine-tuning and mask-supervised RMP training.

## Reproducibility

- Code: https://github.com/HUST-SLOW/SeaS.
- Base model: Stable Diffusion v1-4.
- Training data per anomaly type: 60 normal images and 13 masked anomaly images.
- Generated samples: 1,000 anomaly image-mask pairs per anomaly type.
- Optimizer, learning rate, batch size, seeds, and hardware: not reported in the main text read for this audit.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Synthetic data generation]], [[Data augmentation]], [[Few-shot zero-shot learning]], [[Diffusion models]], [[U-Net]]
- Datasets: [[MVTec AD]], [[VisA]], [[MVTec3D]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Inception Score]], [[LPIPS]], [[KID]], [[AU-ROC]], [[Average precision]], [[F1-score]], [[IoU]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]] | Contrasts with / baseline | SeaS compares against AnomalyDiffusion for generation quality and generated-pair supervised segmentation, and the source states AnomalyDiffusion trains one segmentation model per product. |
| [[2024 - RealNet A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection]] | Follow-up reading | Both use synthetic anomalies for industrial anomaly detection, but SeaS focuses on diffusion generation of anomaly images, normal images, and masks. |
| [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] | Follow-up reading | Both use generated image-mask pairs for anomaly segmentation; SeaS uses Separation and Sharing fine-tuning plus RMP. |

### Backlinks Updated

- [[MVTec AD]]
- [[VisA]]
- [[MVTec3D]]
- [[Multi-industry anomaly detection]]

## Questions

- Appendix details should be checked for optimizer, learning rate, batch size, hardware, and exact split procedure.
- The main text reports code availability, but trained checkpoints and generated data releases were not confirmed in the read source.
