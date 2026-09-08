---
title: "AnomalyDiffusion: Few-Shot Anomaly Image Generation with Diffusion Model"
aliases:
  - "AnomalyDiffusion"
paper_key: "arxiv:2312.05767"
paper_type: research
year: 2024
venue: "arXiv"
authors:
  - "Teng Hu"
  - "Jiangning Zhang"
  - "Ran Yi"
  - "Yuzhen Du"
  - "Xu Chen"
  - "Liang Liu"
  - "Yabiao Wang"
  - "Chengjie Wang"
status: processed
processed_at: 2026-05-23
audited_at: 2026-06-11
topics:
  - "few-shot anomaly generation"
  - "diffusion anomaly synthesis"
  - "industrial anomaly localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[AnomalyDiffusion]]"
  - "[[Diffusion models]]"
  - "[[Few-shot zero-shot learning]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
architectures:
  - "[[AnomalyDiffusion]]"
  - "Latent Diffusion Model"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "IS: generation quality; higher is better"
  - "IC-LPIPS: generation diversity; higher is better"
  - "AUROC/AP/F1-max: downstream anomaly localization and detection; higher is better"
baselines:
  - "DRAEM"
  - "PRN"
  - "DFMGAN"
  - "DiffAug"
  - "CDC"
  - "Crop&Paste"
  - "SDGAN"
  - "Defect-GAN"
benchmarks:
  - "[[MVTec AD]]"
code: "https://github.com/sjtuplayer/anomalydiffusion"
data: "code and generated data reported available"
doi: "not reported"
arxiv: "2312.05767"
url: "https://arxiv.org/abs/2312.05767"
pdf: "paper-inbox/10_processed/Research/2024 - Hu - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model.pdf"
related_methods:
  - "[[AnomalyDiffusion]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[MVTec AD]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2024 - Hu - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Hu - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Hu - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model.txt"
artifact_status: "code and data reported available"
tags:
  - paper
---
# AnomalyDiffusion: Few-Shot Anomaly Image Generation with Diffusion Model

## Summary

AnomalyDiffusion is a few-shot diffusion-based anomaly generation model for industrial anomaly inspection. It uses a pretrained latent diffusion model, Spatial Anomaly Embedding, masked textual inversion, and Adaptive Attention Re-weighting to generate anomalous image-mask pairs from a few anomaly examples. The generated data improves downstream anomaly localization, detection, and classification on MVTec AD.

## Paper Type

- Type: research.
- Why: The paper proposes a new generative method and evaluates both generation quality and downstream inspection performance.

## Problem

- Task: anomaly image-mask generation for [[Industrial anomaly detection]], [[Defect segmentation]], and [[Defect classification]].
- Setting: few-shot industrial anomaly generation from scarce defect samples.
- Motivation: model-free crop/paste methods lack authenticity, while GAN-based methods need many anomaly samples or produce poor mask alignment.

## Contribution

- Claimed: AnomalyDiffusion generates authentic and diverse few-shot industrial anomaly images by using pretrained LDM priors.
- Claimed: Spatial Anomaly Embedding disentangles anomaly appearance from anomaly location.
- Claimed: Adaptive Attention Re-weighting improves alignment between generated anomalies and input masks.
- Shown: downstream U-Net localization trained on generated data reaches 99.1 pixel-level AUROC and 81.4 AP on MVTec AD.

## Method

- Inputs: an anomaly-free sample and an anomaly mask.
- Output: an anomalous image whose anomaly appears in the mask area while the remaining image stays consistent with the normal input.
- Anomaly embedding: learned textual embedding for anomaly appearance type, initialized with 8 tokens.
- Spatial embedding: encoded from the anomaly mask using ResNet-50 plus FPN and fully connected networks, with 4 tokens.
- Mask embedding: learned with textual inversion using 4 random tokens to generate more anomaly masks.
- Masked textual inversion: optimizes the diffusion loss only over anomaly regions.
- Adaptive Attention Re-weighting: computes a weight map from differences between the denoised image and the normal sample, then reweights cross-attention toward less noticeable anomaly regions.

## ML / DL Extraction

- Base model: latent diffusion model.
- Training data: one-third of the MVTec AD anomaly data with the lowest IDs.
- Test data: remaining two-thirds of MVTec AD anomaly data.
- Generated data: 1,000 anomalous image-mask pairs per anomaly category for downstream tasks.
- Downstream localization model: U-Net trained on generated anomalies plus normal samples.
- Downstream classification model: ResNet-34 trained on generated data for anomaly classification.
- Seeds, GPU, optimizer, and learning rates: not reported in the available source text.

## Evidence

### Generation Quality

| Metric | AnomalyDiffusion average | Best comparison noted |
|---|---:|---:|
| IS | 1.80 | DFMGAN 1.72 |
| IC-LPIPS | 0.32 | DFMGAN 0.20 |

### Downstream Localization

| Method generating training data | Pixel AUROC | AP | F1-max |
|---|---:|---:|---:|
| DRAEM | 92.2 | 54.1 | 53.1 |
| PRN | 96.9 | 66.2 | 64.7 |
| DFMGAN | 90.0 | 62.7 | 62.1 |
| AnomalyDiffusion | 99.1 | 81.4 | 76.3 |

### Downstream Image-Level Detection

| Method generating training data | AUROC | AP | F1-max |
|---|---:|---:|---:|
| DRAEM | 94.6 | 97.0 | 94.4 |
| PRN | 91.6 | 96.6 | 92.4 |
| DFMGAN | 87.2 | 94.8 | 94.7 |
| AnomalyDiffusion | 99.2 | 99.7 | 98.7 |

### Downstream Classification

- ResNet-34 trained on AnomalyDiffusion-generated data reaches 66.09% average anomaly classification accuracy.
- The next best reported generator in the table is DFMGAN at 49.61%.

### Ablation

| Components | AUROC | AP | F1-max |
|---|---:|---:|---:|
| none of SAE, masked loss, AAR | 81.3 | 31.1 | 46.5 |
| SAE only | 90.3 | 51.2 | 60.7 |
| SAE + masked loss | 95.0 | 64.9 | 68.8 |
| masked loss + AAR | 95.5 | 67.5 | 68.9 |
| full model | 99.1 | 81.4 | 76.3 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | anomaly detection and localization | area under ROC curve | higher | yes | reported at pixel and image level |
| [[Average precision]] | anomaly localization/detection | area under precision-recall ranking | higher | yes | downstream localization AP 81.4 |
| [[F1-score]] | anomaly localization/detection | maximum F1 over thresholds | higher | no | downstream localization F1-max 76.3 |
| [[Accuracy]] | anomaly classification | average classification accuracy | higher | no | 66.09% average classification accuracy |

## Dataset / Benchmark Details

- Main dataset: [[MVTec AD]].
- Training split: one-third of anomaly data with the lowest IDs.
- Testing split: remaining two-thirds of anomaly data.
- Generated masks: mask embeddings are learned to expand scarce real anomaly masks.

## Limitations

- The paper proposes future work using a more potent diffusion model to enhance generated anomaly resolution.
- The source does not report full optimizer, GPU, random seed, or training-time details in the available analysis input.
- Evaluation centers on MVTec AD; cross-dataset generality is not established in the main source text.

## Reproducibility

- Code and data: https://github.com/sjtuplayer/anomalydiffusion.
- Generated pairs: 1,000 anomalous image-mask pairs per anomaly category.
- Hardware: not reported.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]], [[Defect classification]]
- Methods: [[AnomalyDiffusion]], [[Diffusion models]], [[Few-shot zero-shot learning]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]], [[F1-score]], [[Accuracy]]

### Relationship Notes

- Shares dataset: [[MVTec AD]].
- Shares method: [[Diffusion models]] and [[Synthetic data generation]].
- Shares task: few-shot anomaly generation for downstream anomaly localization and classification.

## Questions

- How well does AnomalyDiffusion transfer beyond MVTec AD categories?
- What optimizer, compute, and training time are required for each anomaly type?
