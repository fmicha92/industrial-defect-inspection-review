---
title: "AnomalyXFusion: Multi-modal Anomaly Synthesis with Diffusion"
aliases:
  - "AnomalyXFusion: Multi-modal Anomaly Synthesis with Diffusion"
paper_key: "arxiv:2404.19444"
paper_type: research
year: 2024
venue: "arXiv"
authors:
  - "Jie Hu"
  - "Yawen Huang"
  - "Yilin Lu"
  - "Guoyang Xie"
  - "Guannan Jiang"
  - "Yefeng Zheng"
  - "Zhichao Lu"
affiliations:
  - "CATL"
  - "Tencent Youtu Lab"
  - "Xiamen University"
  - "City University of Hong Kong"
status: processed
processed_at: 2026-06-11
topics:
  - "multi-modal anomaly synthesis"
  - "diffusion models"
  - "text-conditioned anomaly generation"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[MVTec LOCO AD]]"
  - "[[MVTec Caption]]"
methods:
  - "[[AnomalyXFusion]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "[[AnomalyXFusion]]"
metrics:
  - "[[Inception Score]]"
  - "[[LPIPS]]"
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Inception Score: generation quality metric; higher is better."
  - "IC-LPIPS: intra-category LPIPS diversity metric; higher indicates greater generated-sample diversity in the paper's reporting."
  - "AUC-P/AP-P/F1-P: pixel-level localization metrics; higher is better."
  - "AUC-I/AP-I/F1-I: image-level detection metrics; higher is better."
baselines:
  - "DiffAug"
  - "CDC"
  - "Crop-P"
  - "SDGAN"
  - "DefGAN"
  - "DFMGAN"
  - "AnomalyDiffusion"
  - "DRAEM"
  - "PRN"
benchmarks:
  - "[[MVTec AD]]"
  - "[[MVTec LOCO AD]]"
  - "[[MVTec Caption]]"
code: "https://github.com/hujiecpp/MVTec-Caption"
data: "MVTec Caption construction repository reported; base MVTec datasets required separately"
doi: "not reported"
arxiv: "2404.19444"
url: "https://github.com/hujiecpp/MVTec-Caption"
pdf: "paper-inbox/10_processed/Research/2024 - Hu - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion.pdf"
related_papers:
  - "[[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[AnomalyXFusion]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[MVTec LOCO AD]]"
  - "[[MVTec Caption]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec AD]]"
  - "[[MVTec LOCO AD]]"
source_file: "paper-inbox/10_processed/Research/2024 - Hu - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Hu - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Hu - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion.txt"
artifact_status: "project repository reported"
tags:
  - paper
---
# AnomalyXFusion: Multi-modal Anomaly Synthesis with Diffusion

## Summary

AnomalyXFusion is a diffusion-based anomaly synthesis framework for industrial inspection. It conditions generated anomaly images on text, mask/location information, and anomaly texture, then uses the generated image-mask pairs for anomaly localization, detection, and anomaly-type classification. The paper also introduces [[MVTec Caption]], a 2.2k image-mask-text annotation extension over [[MVTec AD]] and [[MVTec LOCO AD]].

## Paper Type

- Type: research.
- Why: The paper proposes a new synthesis framework, introduces an annotation resource, and evaluates generation quality plus downstream anomaly detection, localization, and classification.

## Problem

- Task: [[Industrial anomaly detection]], [[Defect segmentation]], and anomaly-type classification under scarce real anomaly data.
- Setting: multi-category industrial visual inspection across MVTec AD and MVTec LOCO AD.
- Inputs: normal or base industrial images, anomaly masks, text anomaly descriptions, and masked anomaly texture images.
- Outputs: synthesized anomalous image-mask pairs and downstream anomaly predictions.
- Motivation: existing anomaly synthesis methods mainly use single-modal conditioning and struggle to control visual features, location, and semantic description together, especially for logical anomalies.
- Assumption: text, spatial masks, and texture exemplars provide complementary control signals for anomaly synthesis.

## Contribution

- Introduces [[AnomalyXFusion]], a multi-modal diffusion framework that combines semantic text, location masks, and texture images for controllable industrial anomaly synthesis.
- Proposes Multi-modal In-Fusion (MIF) to merge semantic, location, and texture embeddings into a unified X-Embedding, and Dynamic Dif-Fusion (DDF) to adjust conditioning by diffusion timestep.
- Introduces [[MVTec Caption]], containing 1,258 caption annotations for MVTec AD and 982 for MVTec LOCO AD, for a total of about 2.2k image-mask-text annotations.

## Method

- Semantic conditioning: a frozen CLIP text encoder embeds anomaly descriptions. The semantic embedding is replicated multiple times and L2-normalized.
- Location conditioning: anomaly masks are passed through a pretrained mask encoder, with a one-layer CNN adapting dimensions. The paper states that the mask encoder and CNN are fine-tuned.
- Texture conditioning: a frozen CLIP image encoder embeds the masked anomaly region from the defect image. The image embedding initializes textual embedding before fusion.
- Multi-modal In-Fusion: semantic, location, and texture embeddings are concatenated and passed through self-attention and an MLP with residual connections to produce an X-Embedding.
- Dynamic Dif-Fusion: an MLP conditions the X-Embedding on the current diffusion timestep, and cross-attention injects the dynamic condition into the denoising process.
- Diffusion objective: training minimizes the standard noise-prediction loss between sampled diffusion noise and predicted noise.
- Synthesis use: the paper synthesizes 1,000 images per category for generation-quality and downstream evaluations.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[MVTec LOCO AD]], and [[MVTec Caption]].
- MVTec AD: more than 5,000 images across 15 object and texture classes with pixel-level anomaly masks.
- MVTec LOCO AD: 3,644 images across five categories with structural and logical anomalies plus pixel-level ground truth.
- MVTec Caption: 1,258 MVTec AD captions and 982 MVTec LOCO captions.
- Generation baselines: DiffAug, CDC, Crop-P, SDGAN, DefGAN, DFMGAN, and [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model|AnomalyDiffusion]].
- Downstream baselines: DRAEM, PRN, DFMGAN, and AnomalyDiffusion in the reported U-Net localization/detection comparison.
- Classification model: ResNet-34 trained on generated samples for anomaly classification.
- Metrics: [[Inception Score]], IC-LPIPS, pixel-level AUC/AP/F1, image-level AUC/AP/F1, and classification [[Accuracy]].
- FID and KID are explicitly not used because the available anomaly data is limited.
- Compute, optimizer, batch size, and training time: not reported.

### Main Results

- MVTec AD generation: AnomalyXFusion reports mean IS 1.82 and mean IC-LPIPS 0.33, compared with AnomalyDiffusion at 1.80 and 0.32.
- MVTec LOCO generation: AnomalyXFusion reports mean IS 1.69 and mean IC-LPIPS 0.33, compared with AnomalyDiffusion at 1.44 and 0.28 and DFMGAN at 1.27 and 0.22.
- MVTec AD downstream localization with U-Net trained on generated data: AnomalyXFusion reports mean AUC-P 99.3, AP-P 86.1, and F1-P 80.6.
- MVTec AD downstream image-level detection: AnomalyXFusion reports mean AUC-I 99.2, AP-I 99.8, and F1-I 98.7.
- MVTec AD anomaly classification: AnomalyXFusion reports 74.70% mean accuracy, compared with 66.09% for AnomalyDiffusion and 49.61% for DFMGAN.
- MVTec LOCO anomaly classification: AnomalyXFusion reports 50.95% mean accuracy, compared with 45.44% for AnomalyDiffusion.
- Ablation: the no-component setting reports IS 1.63, IC-LPIPS 0.23, and 65.38% accuracy; the full Text+MIF+DDF setting reports IS 1.82, IC-LPIPS 0.33, and 74.70% accuracy.

### Performance Metrics

| Metric | Used for | Direction | Reported values |
|---|---|---|---|
| [[Inception Score]] | generation quality | higher is better | MVTec AD mean 1.82; MVTec LOCO mean 1.69 |
| [[LPIPS]] / IC-LPIPS | intra-category generated diversity | higher is better in this paper's IC-LPIPS reporting | MVTec AD mean 0.33; MVTec LOCO mean 0.33 |
| [[AU-ROC]] | localization and image-level detection | higher is better | AUC-P 99.3; AUC-I 99.2 on MVTec AD downstream evaluation |
| [[Average precision]] | localization and image-level detection | higher is better | AP-P 86.1; AP-I 99.8 on MVTec AD downstream evaluation |
| [[F1-score]] | localization and image-level detection | higher is better | F1-P 80.6; F1-I 98.7 on MVTec AD downstream evaluation |
| [[Accuracy]] | anomaly classification | higher is better | MVTec AD mean 74.70%; MVTec LOCO mean 50.95% |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB industrial images, binary anomaly masks, masked anomaly texture images, and text anomaly descriptions.
- Output target: synthetic anomalous image-mask pairs; downstream anomaly localization, image-level detection, and anomaly classification.
- Supervision: uses image-mask-text annotations from MVTec Caption for controllable synthesis.
- Objective: diffusion noise-prediction loss for conditional generation.

### Model And Training

- Model family: [[Diffusion models]].
- Architecture: AnomalyXFusion with MIF and DDF conditioning modules.
- Text encoder: CLIP text encoder, frozen.
- Image encoder: CLIP image encoder, frozen.
- Mask branch: pretrained mask encoder plus one-layer CNN, both fine-tuned.
- Parameters: not reported.
- Pretraining: CLIP encoders and mask encoder are pretrained; exact checkpoints are not reported.
- Fine-tuning: mask encoder and the one-layer CNN are fine-tuned; full optimizer settings are not reported.
- Losses: diffusion noise-prediction loss.
- Optimizer, learning rate, seeds, batch size, hardware, and environment: not reported.

### Data

- Datasets: MVTec AD, MVTec LOCO AD, and MVTec Caption.
- Dataset size: MVTec Caption contains 1,258 MVTec AD captions and 982 MVTec LOCO captions.
- Labels / annotations: anomaly masks and text anomaly captions.
- Splits: not reported.
- Preprocessing: masked anomaly texture is formed by multiplying the anomaly image with the location mask.
- Synthetic data: 1,000 synthesized anomalous images per category are generated for evaluation.
- Leakage checks: not reported.
- License: not reported for AnomalyXFusion; MVTec Caption's repository points to the underlying MVTec datasets.

### Evaluation

- Generation protocol: compares generated anomaly quality and diversity using IS and IC-LPIPS.
- Perception protocol: trains downstream anomaly localization/detection models on generated data and evaluates on MVTec AD.
- Classification protocol: trains ResNet-34 for anomaly-type classification on generated data.
- Statistical tests: not reported.
- Failure cases: the paper states that removing text, MIF, or DDF weakens controllability and generation quality; detailed failure-category analysis is not reported.

## Dataset / Benchmark Details

- [[MVTec Caption]] extends MVTec AD and MVTec LOCO AD with image-mask-text triplets.
- The MVTec AD caption subset contains 1,258 captions.
- The MVTec LOCO caption subset contains 982 captions.
- The paper motivates captions especially for logical anomalies, where a mask alone does not state whether an object is missing, duplicated, misplaced, or wrong-colored.
- The project page is reported as https://github.com/hujiecpp/MVTec-Caption.

## Limitations

- Optimizer settings, learning rate, training batch size, hardware, random seeds, and training time are not reported in the available source text.
- FID and KID are not used because the paper treats the available anomaly data as too limited for those metrics.
- Dataset splits and leakage controls are not reported.
- The evaluation concentrates on MVTec AD and MVTec LOCO AD; transfer to non-MVTec industrial datasets is not demonstrated in the available source text.

## Reproducibility

- Code / project page: https://github.com/hujiecpp/MVTec-Caption.
- Data: MVTec Caption construction is reported; base MVTec AD and MVTec LOCO AD datasets are required separately.
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[AnomalyXFusion]], [[Diffusion models]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[MVTec LOCO AD]], [[MVTec Caption]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Inception Score]], [[LPIPS]], [[AU-ROC]], [[Average precision]], [[F1-score]], [[Accuracy]]

### Builds On

- [[2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model]]: shares diffusion-based anomaly image generation and downstream evaluation on MVTec AD; AnomalyXFusion adds multi-modal text-mask-texture conditioning and reports higher MVTec AD classification accuracy.

### Shares Dataset

- [[MVTec AD]]: used for anomaly synthesis, generation-quality evaluation, downstream localization/detection, and classification.
- [[MVTec LOCO AD]]: used for logical and structural anomaly synthesis and generation/classification evaluation.
- [[MVTec Caption]]: introduced as the image-mask-text annotation resource for the method.

### Shares Method

- [[AnomalyXFusion]]: central method introduced by the paper.
- [[Diffusion models]]: the generative backbone family used for conditional anomaly synthesis.
- [[Synthetic data generation]]: generated anomaly image-mask pairs are the primary output used for downstream training.
- [[Data augmentation]]: generated anomalies act as training data for downstream localization, detection, and classification.

### Shares Task

- [[Industrial anomaly detection]]: downstream image-level anomaly detection is evaluated on generated-data training.
- [[Defect segmentation]]: pixel-level anomaly localization is evaluated through AUC-P, AP-P, and F1-P.

### Shares Metric

- [[Inception Score]]: used for generation quality, with mean 1.82 on MVTec AD and 1.69 on MVTec LOCO.
- [[LPIPS]]: IC-LPIPS is used for generated-sample diversity, with mean 0.33 on both MVTec AD and MVTec LOCO.
- [[AU-ROC]]: reports AUC-P 99.3 and AUC-I 99.2 in downstream MVTec AD evaluation.
- [[Average precision]]: reports AP-P 86.1 and AP-I 99.8 in downstream MVTec AD evaluation.
- [[F1-score]]: reports F1-P 80.6 and F1-I 98.7 in downstream MVTec AD evaluation.
- [[Accuracy]]: reports 74.70% MVTec AD and 50.95% MVTec LOCO anomaly classification accuracy.

### Application / Domain

- [[Multi-industry anomaly detection]]: MVTec AD and MVTec LOCO AD span multiple industrial object and texture categories.

### Follow-up Reading

- Read the project repository to verify released annotation files, construction scripts, license metadata, and any training configuration not reported in the paper text.

## Questions

- What exact optimizer, learning-rate schedule, batch size, hardware, and number of training iterations were used?
- Which split protocol prevents overlap between generated-training supervision and downstream test anomalies?
- How does AnomalyXFusion transfer to industrial datasets outside MVTec AD and MVTec LOCO AD?
