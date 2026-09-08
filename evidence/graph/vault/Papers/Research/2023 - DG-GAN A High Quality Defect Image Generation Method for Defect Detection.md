---
title: "DG-GAN: A High Quality Defect Image Generation Method for Defect Detection"
aliases:
  - "DG-GAN: A High Quality Defect Image Generation Method for Defect Detection"
paper_key: "sha256:af4f908ba80d15a0679160c931bda08e74f1069895ab157985f6cbf81f60f8f8"
paper_type: research
year: 2023
venue: "Sensors"
authors:
  - "Xiangjie He"
  - "Zhongqiang Luo"
  - "Quanyang Li"
  - "Hongbo Chen"
  - "Feng Li"
status: processed
processed_at: 2026-05-23
topics:
  - "defect image generation"
  - "GAN augmentation"
  - "defect detection"
tasks:
  - "[[Surface defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Metal inspection]]"
  - "[[Electrical power equipment inspection]]"
datasets:
  - "[[NEU-CLS]]"
  - "[[IP-def]]"
methods:
  - "[[DG-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[DG-GAN]]"
metrics:
  - "[[FID]]"
  - "[[mAP@0.50]]"
primary_metric: "[[FID]]"
metric_definitions:
  - "FID measures distributional similarity between real and generated images; lower is better."
baselines:
  - "ProGAN"
  - "CycleGAN"
  - "YOLOX without generated images"
benchmarks:
  - "[[NEU-CLS]]"
  - "[[IP-def]]"
code: "not reported"
data: "not publicly available; source data availability statement says the research institute cannot disclose the data"
doi: "10.3390/s23135922"
arxiv: "not reported"
url: "https://doi.org/10.3390/s23135922"
pdf: "paper-inbox/10_processed/Research/2023 - He - DG-GAN A High Quality Defect Image Generation Method for Defect Detection.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[DG-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-CLS]]"
  - "[[IP-def]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Object detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - He - DG-GAN A High Quality Defect Image Generation Method for Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - He - DG-GAN A High Quality Defect Image Generation Method for Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - He - DG-GAN A High Quality Defect Image Generation Method for Defect Detection.txt"
artifact_status: "data unavailable per source"
tags:
  - paper
---
# DG-GAN: A High Quality Defect Image Generation Method for Defect Detection

## Summary

He et al. propose [[DG-GAN]], a defect-image generator for surface defect detection under scarce defect samples. The method builds on progressive GAN ideas and adds D2 adversarial loss, cyclic consistency loss, a data augmentation module, and self-attention. It is evaluated on [[NEU-CLS]] hot-rolled strip steel defects and a self-collected [[IP-def]] insulation-partition defect dataset using [[FID]] for generation quality and YOLOX mAP for downstream detection.

## Paper Type

- Type: research.
- Why: The paper proposes a new GAN architecture, reports ablations, and tests generated images in downstream defect detection.

## Problem

- Task: [[Surface defect detection]], [[Object detection]]
- Setting: [[Metal inspection]] for NEU, with an additional [[Electrical power equipment inspection]] case study on insulation partitions.
- Inputs: defect-free and defect images.
- Outputs: generated pseudo-defect images and object-detection predictions.
- Motivation: industrial defect images are difficult to collect in sufficient quantity, causing overfitting and low detection accuracy.
- Assumptions: pseudo-defect images that are similar to real defects can improve detector training when manually labeled for detection experiments.

## Contribution

- Claimed: DG-GAN generates high-quality and high-diversity defect images for surface defect detection.
- Claimed: D2 adversarial loss and cyclic consistency loss improve generated image quality/diversity; self-attention improves high-resolution generation; a data augmentation module stabilizes training.
- Shown: DG-GAN lowers FID relative to ProGAN and CycleGAN across NEU and IP-def classes and improves YOLOX mAP@0.5 from 72.1 to 78.2 on NEU and from 75.2 to 95.6 on IP-def.

## Method

- Core idea: learn mappings between defect-free and defective images using two generators and four discriminators, optimizing D2 adversarial and cyclic consistency losses.
- Architecture / algorithm: [[DG-GAN]], [[GAN]], [[Data augmentation]].
- Generator/discriminator design: two generators G and C and four discriminators D1f, D1i, D2f, D2i.
- D2 adversarial loss: adds a diversity-oriented adversarial term to balance quality and diversity.
- Cyclic consistency loss: supports defect-free-image-assisted defect image generation.
- Self-attention: inserted in high-resolution generator/discriminator layers, especially 256 x 256 and 512 x 512 layers.
- Detection case study: generated images are used to train YOLOX.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial surface defect images.
- Output target: generated pseudo-defect images; detector boxes/classes in the YOLOX case study.
- Supervision: GAN training uses defect and defect-free image distributions; downstream YOLOX uses manually labeled true and generated defect images.
- Objective: improve generated image realism/diversity and downstream detection mAP.

### Model And Training

- Model family: [[GAN]], [[Generative Models]].
- Architecture: [[DG-GAN]] with progressive generation, data augmentation, self-attention, D2 adversarial loss, and cyclic consistency loss.
- Hyperparameters: generator input is a 512-dimensional normal random vector; batch size 8; Adam with beta1 0.9, beta2 0.999, epsilon 1e-8; generator/discriminator learning rate 0.001; 1000 epochs.
- Training compute: PyTorch on Windows with three Titan X 12GB GPUs and CUDA 11.5.
- YOLOX detector setup: 400 iterations, batch size 16, SGD, weight decay 0.0005, momentum 0.9, initial learning rate 0.01, final learning rate 0.001, cosine annealing.

### Data

- [[NEU-CLS]]: six hot-rolled strip steel surface defect types, 300 images per type, 200 x 200 images, manually marked defect location and category.
- NEU defect classes: rolled-in scale, patches, crazing, pitted surface, inclusion, scratches.
- [[IP-def]]: self-collected insulation partition defect dataset with scratches, pit points, ablation, and voltage breakdown.
- IP-def size: 100 images per class, 400 total, 512 x 512 jpg images.
- Generated data: 5400 false NEU defect images and 2000 IP-def generated defect images are used in downstream detection experiments.
- License: not publicly available per the paper's data availability statement.

### Evaluation

- Protocol: compare FID for ProGAN, CycleGAN, intermediate ablations, and DG-GAN; then train YOLOX with original versus generated data.
- Used performance metrics: [[FID]], [[mAP@0.50]], mAP@0.5:0.95.
- Primary metric: [[FID]] for generation quality; mAP@0.5 for detection case studies.
- Metric direction / units: lower FID is better; higher mAP is better.
- Statistical tests: not reported.
- Failure cases: training time is longer than ProGAN and CycleGAN; data unavailable externally.

## Evidence

### Experimental Setup

- Generation datasets: [[NEU-CLS]], [[IP-def]].
- Generation baselines: ProGAN and CycleGAN.
- Detector: YOLOX.
- Used performance metrics: [[FID]], [[mAP@0.50]].

### Main Results

| Dataset / Task | Metric | Baseline | Paper result | Notes |
|---|---|---:|---:|---|
| [[NEU-CLS]] generation | mean FID reduction | ProGAN/CycleGAN comparisons | 16.17 lower on average | Abstract-level summary across NEU classes. |
| [[IP-def]] generation | mean FID reduction | ProGAN/CycleGAN comparisons | 20.06 lower on average | Abstract-level summary across IP-def classes. |
| [[NEU-CLS]] detection | mAP@0.5 | 72.1 with original data | 78.2 with Fake5400 | mAP@0.5:0.95 rises from 38.6 to 45.4. |
| [[IP-def]] detection | mAP@0.5 | 75.2 with original data | 95.6 with Fake2000 | mAP@0.5:0.95 rises from 39.4 to 75.8. |
| Training time | hours | ProGAN 8.15, CycleGAN 6.53 | DG-GAN 8.32 | All at 1000 epochs and data volume 2200. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[FID]] | generated defect image quality | distribution distance between real and generated image features | lower | yes | Paper states lower FID means higher-quality generated images closer to real distribution. |
| [[mAP@0.50]] | YOLOX defect detection | mAP at IoU 0.5 | higher | no | Used in downstream case studies. |

### Ablations

- Base loss improvements reduce FID compared with CycleGAN.
- Adding the data augmentation module stabilizes loss curves and improves training.
- Self-attention in low-resolution layers has little effect; self-attention at 256 x 256 and above improves generated image quality.

## Dataset / Benchmark Details

- [[NEU-CLS]]: public hot-rolled strip steel defect dataset with six classes.
- [[IP-def]]: paper-collected insulation partition defect dataset from production/sales manufacturers and power companies.
- License: data not disclosed according to the data availability statement.
- Leakage risks: no explicit leakage checks reported.

## Limitations

- Stated: DG-GAN training time is relatively lengthy, and future work should reduce model parameters and build lighter networks.
- Stated: data cannot be disclosed by the research institute.
- Inferred: downstream detection uses manually labeled generated images, so labeling cost remains part of the pipeline.

## Reproducibility

- Code: not reported.
- Data: not publicly available.
- Hyperparameters: GAN and YOLOX training settings are reported.
- Random seeds: not reported.
- Environment: PyTorch, Windows, CUDA 11.5, three Titan X 12GB GPUs.
- Artifact status: data unavailable per source.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Object detection]]
- Methods: [[DG-GAN]], [[GAN]], [[Data augmentation]]
- Datasets: [[NEU-CLS]], [[IP-def]]
- Benchmarks: [[NEU-CLS]], [[IP-def]]
- Domains: [[Metal inspection]], [[Electrical power equipment inspection]]
- Metrics: [[FID]], [[mAP@0.50]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[NEU-CLS]]: hot-rolled strip steel generation and detection case study.
- [[IP-def]]: insulation partition generation and detection case study.

### Shares Method

- [[DG-GAN]]: proposed model.
- [[GAN]]: generative model family.
- [[Data augmentation]]: generated pseudo-defect images expand detector training data.

### Shares Metric

- [[FID]]: primary generation-quality metric.
- [[mAP@0.50]]: downstream detector metric.
