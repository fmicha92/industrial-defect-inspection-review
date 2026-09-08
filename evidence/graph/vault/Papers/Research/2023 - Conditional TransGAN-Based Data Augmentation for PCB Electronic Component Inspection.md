---
title: "Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection"
aliases:
  - "Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection"
paper_key: "doi:10.1155/2023/2024237"
paper_type: research
year: 2023
venue: "Computational Intelligence and Neuroscience"
authors:
  - "Chenglong Wang"
  - "Guanghan Huang"
  - "Zhiyuan Huang"
  - "Weiming He"
status: processed
processed_at: 2026-05-22
topics:
  - "PCB component inspection"
  - "generative augmentation"
tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[PCB electronic component inspection dataset]]"
  - "[[DeepPCB]]"
methods:
  - "[[cTransGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Transformers]]"
model_family:
  - "[[GAN]]"
  - "[[Transformers]]"
architectures:
  - "[[cTransGAN]]"
metrics:
  - "[[mAP]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "mAP is the mean AP over all categories in the test set; AP is derived from the interpolation precision-recall curve."
baselines:
  - "Faster R-CNN ResNet101"
  - "YOLOv3 DarkNet-53"
  - "SCNet ResNet101"
benchmarks:
  - "[[PCB electronic component inspection dataset]]"
  - "[[DeepPCB]]"
code: "reported available: https://github.com/long-deep/pcb-detect"
data: "reported available: https://github.com/long-deep/pcb-detect and https://github.com/tangsanli5201/DeepPCB"
doi: "10.1155/2023/2024237"
arxiv: "not reported"
url: "https://doi.org/10.1155/2023/2024237"
pdf: "paper-inbox/10_processed/Research/2023 - Wang - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[cTransGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[PCB electronic component inspection dataset]]"
  - "[[DeepPCB]]"
related_tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
source_file: "paper-inbox/10_processed/Research/2023 - Wang - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wang - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wang - Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# Conditional TransGAN-Based Data Augmentation for PCB Electronic Component Inspection

## Summary

Wang et al. propose [[cTransGAN]], a class-conditioned TransGAN-based data augmentation method for PCB electronic component recognition and PCB defect detection. The model conditions both generator and discriminator on learned class embeddings and uses generated images to augment object detector training. Experiments evaluate Faster R-CNN ResNet101, YOLOv3 DarkNet-53, and SCNet ResNet101 on a self-developed PCB component dataset and [[DeepPCB]], with [[mAP]] as the primary metric.

## Paper Type

- Type: research.
- Why: The paper introduces a generative augmentation method and evaluates it experimentally on two PCB detection datasets.

## Problem

- Task: [[PCB defect detection]], [[PCB defect classification]]
- Setting: [[Semiconductor and electronics]]
- Inputs: PCB component images and PCB defect images.
- Outputs: object classes and bounding boxes for PCB components or PCB defects; generated synthetic training images.
- Motivation: PCB targets are small, backgrounds are visually complex, and limited training samples reduce detector performance.
- Assumptions: generated images can be paired with source-image annotations or class labels for detector training.

## Contribution

- Claimed: [[cTransGAN]] combines conditional GAN control with TransGAN generator/discriminator design to generate class-conditioned PCB component and defect images.
- Claimed: The generated data improves detector mAP across Faster R-CNN, YOLOv3, and SCNet settings.
- Shown: On the self-developed dataset, SCNet ResNet101 with cTransGAN reaches 96.2% mAP; on DeepPCB, Faster R-CNN ResNet101 with cTransGAN reaches 98.8% mAP.

## Method

- Core idea: learn a class embedding from a modified TransGAN discriminator, then condition both the TransGAN generator and discriminator on that class embedding.
- Architecture / algorithm: [[cTransGAN]], [[GAN]], [[Transformers]], [[Data augmentation]].
- Detector training: Faster R-CNN ResNet101, YOLOv3 DarkNet-53, and SCNet ResNet101 are trained on original and augmented training sets.
- Augmentation settings: no augmentation, image-processing augmentation, TransGAN, cGAN, and cTransGAN.
- Image-processing augmentation: random combinations of blur, flip, center crop, CLAHE, color jitter, rotate, and transpose.
- Optimization: cTransGAN is trained for 240 epochs with Adam, batch size 64 for both generator and discriminator, and learning rate 0.0001; detectors are trained for 2000 epochs with momentum 0.7, verification period 4000, learning rate 0.004, weight decay 0.0004, and batch size 32.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB PCB inspection images.
- Output target: component/defect class and bounding box; generated images for augmentation.
- Supervision: supervised object detection plus GAN-based image synthesis from labeled training data.
- Objective: improve mAP by increasing training-set quantity and diversity.

### Model And Training

- Model family: [[GAN]], [[Transformers]].
- Architecture: [[cTransGAN]] with class-conditioned TransGAN generator and discriminator.
- Pretraining: SCNet uses ImageNet and PASCAL VOC 2007 keypoint pretraining as described in the detector setup; YOLOv3 uses DarkNet-53 ImageNet classification pretraining.
- Losses: paper reports standard detector losses and GAN training; exact GAN loss equations are in the source text but not expanded in this note.
- Training compute: Windows 10, 16 GB RAM, Intel Core i7-8700 CPU, TensorFlow, NVIDIA GeForce RTX 2070 GPU, and Python 3.6.7.

### Data

- Datasets: [[PCB electronic component inspection dataset]], [[DeepPCB]].
- Self-developed dataset: 2544 images with optocoupler, diode, and capacitor classes; data availability points to the project repository.
- Self-developed split: table reports 1780 training images; the test column sums to 764 even though the table's total line appears as 164 in the extracted text.
- Self-developed acquisition: BASLER a2A5320-7gcBAS camera, OPT C161610M lens, Haoli HLFL478408K-K50 light source, camera/lens height 460 mm.
- Self-developed preprocessing: images are resized or zero-padded to 418 x 418.
- DeepPCB: 1500 image pairs with defect-free template and aligned testing image; six defect classes are open, short, mousebite, spur, pin hole, and spurious copper.
- DeepPCB split: 1000 training images and 500 test images.

### Evaluation

- Protocol: compare three detectors under original, image-processed, TransGAN, cGAN, and cTransGAN augmentation settings on both datasets.
- Used performance metrics: [[mAP]].
- Primary metric: [[mAP]].
- Metric direction / units: higher percentage is better.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Experimental Setup

- Datasets: [[PCB electronic component inspection dataset]], [[DeepPCB]].
- Baselines: Faster R-CNN ResNet101, YOLOv3 DarkNet-53, SCNet ResNet101, image-processing augmentation, TransGAN, cGAN; DeepPCB also compares against the GPP max-pooling SOTA reported by Tang et al.
- Used performance metrics: [[mAP]].

### Main Results

| Dataset / Task | Detector | Baseline setting | Baseline mAP | cTransGAN mAP | Notes |
|---|---|---:|---:|---:|---|
| [[PCB electronic component inspection dataset]] / component detection | Faster R-CNN ResNet101 | no augmentation | 91.5% | 93.4% | cTransGAN improves all three component APs. |
| [[PCB electronic component inspection dataset]] / component detection | YOLOv3 DarkNet-53 | no augmentation | 93.3% | 95.3% | Best YOLOv3 setting in the table. |
| [[PCB electronic component inspection dataset]] / component detection | SCNet ResNet101 | no augmentation | 94.1% | 96.2% | Best self-developed-dataset result. |
| [[DeepPCB]] / PCB defect detection | Faster R-CNN ResNet101 | no augmentation | 97.7% | 98.8% | Best DeepPCB result; paper states 0.1% above GPP max-pooling SOTA. |
| [[DeepPCB]] / PCB defect detection | YOLOv3 DarkNet-53 | no augmentation | 93.4% | 96.1% | Largest DeepPCB gain among the three detectors. |
| [[DeepPCB]] / PCB defect detection | SCNet ResNet101 | no augmentation | 96.2% | 98.2% | cTransGAN improves over all SCNet augmentation settings. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | PCB component and defect detection | mean AP over all classes in the test set | higher | yes | Reported as percentages. |

### Ablations

- The detector comparisons are framed as ablations over augmentation choices.
- On the self-developed dataset, TransGAN or cGAN raises mAP by 0.7%-1.3% over no augmentation across detectors; cTransGAN adds a further 0.7%-1.0%.
- On DeepPCB, cTransGAN gains range from 1.1% for Faster R-CNN to 2.7% for YOLOv3 over no augmentation.

## Dataset / Benchmark Details

- [[PCB electronic component inspection dataset]]: 1349 optocoupler images, 396 diode images, and 799 capacitor images.
- [[DeepPCB]]: 1500 aligned PCB template/test pairs; source text describes defect annotations and a 1000/500 train/test split.
- License: DeepPCB license not reported in this paper note; the paper itself is open access under CC BY.
- Leakage risks: no explicit leakage analysis reported.

## Limitations

- Stated: not reported.
- Data availability: the article reports project data at the cTransGAN project repository and DeepPCB data at the DeepPCB repository.
- Inferred: The self-developed dataset split table appears internally inconsistent in the extracted text for the total test-set row.

## Reproducibility

- Code: https://github.com/long-deep/pcb-detect.
- Data: self-developed data and DeepPCB are reported available through the two GitHub URLs in the article data-availability statement.
- Hyperparameters: cTransGAN and detector training hyperparameters are reported.
- Random seeds: not reported.
- Environment: Windows 10, 16 GB RAM, Intel Core i7-8700 CPU, TensorFlow, NVIDIA GeForce RTX 2070 GPU, Python 3.6.7.
- Artifact status: code reported available.

## Connections

### Graph Hubs

- Tasks: [[PCB defect detection]], [[PCB defect classification]]
- Methods: [[cTransGAN]], [[GAN]], [[Data augmentation]], [[Synthetic data generation]], [[Transformers]]
- Datasets: [[PCB electronic component inspection dataset]], [[DeepPCB]]
- Benchmarks: [[PCB electronic component inspection dataset]], [[DeepPCB]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[mAP]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[PCB electronic component inspection dataset]]: self-developed PCB component dataset used for component detection.
- [[DeepPCB]]: public PCB defect dataset used for defect detection.

### Shares Method

- [[cTransGAN]]: proposed class-conditioned TransGAN augmentation method.
- [[GAN]]: generative model family.
- [[Data augmentation]]: training-set expansion objective.

### Shares Task

- [[PCB defect detection]]: DeepPCB object detection setting.
- [[PCB defect classification]]: defect classes include open, short, mousebite, spur, pin hole, and spurious copper.

### Shares Metric

- [[mAP]]: primary detector-performance metric.

### Application / Domain

- [[Semiconductor and electronics]]: PCB manufacturing inspection.
