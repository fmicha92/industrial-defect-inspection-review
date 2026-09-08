---
title: "PreCaCycleGAN: Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation"
aliases:
  - "PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation"
paper_key: "sha256:060a2fd798a5213aeef1375f32ab79d279f4c90ebd86f67d72dc158679ed847d"
paper_type: research
year: 2023
venue: "Electronics"
authors:
  - "Jiaxing Yang"
  - "Ke Wang"
  - "Fengkai Luan"
  - "Yong Yin"
  - "Hu Zhang"
status: processed
processed_at: 2026-05-31
topics:
  - "industrial defect sample augmentation"
  - "CycleGAN"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[DAGM2007]]"
methods:
  - "[[PreCaCycleGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[PreCaCycleGAN]]"
  - "[[YOLOv5]]"
  - "[[Faster R-CNN]]"
metrics:
  - "[[mAP@0.50]]"
  - "[[Detection rate]]"
  - "[[False alarm rate]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "CycleGAN-TSS"
  - "Tree-CycleGAN"
  - "YOLOv5"
  - "SSD"
  - "Faster R-CNN"
benchmarks:
  - "[[DAGM2007]]"
code: "not reported"
data: "DAGM2007 public"
doi: "10.3390/electronics12163475"
url: "https://doi.org/10.3390/electronics12163475"
pdf: "paper-inbox/10_processed/Research/2023 - Yang - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation.pdf"
related_methods:
  - "[[PreCaCycleGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[DAGM2007]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/10_processed/Research/2023 - Yang - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Yang - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Yang - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation.txt"
artifact_status: "public benchmark; code not reported"
tags:
  - paper
---

# PreCaCycleGAN: Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation

## Summary

The paper proposes [[PreCaCycleGAN]], a CycleGAN-derived defect sample augmentation model that generates realistic and diverse industrial defects from defect-free samples. It evaluates on the public [[DAGM2007]] texture-defect dataset and tests the generated samples with YOLOv5, SSD, and Faster R-CNN.

## Paper Type

- Type: research.
- Why: The paper introduces a generative model and evaluates generated samples through downstream detection models.

## Problem

- Task: industrial defect detection with generated augmentation.
- Setting: sparse and imbalanced industrial defect data.
- Inputs: defect-free real samples.
- Outputs: synthetic defective samples for detector training.
- Motivation: industrial defect samples are scarce, expensive to annotate, and often confidential.
- Assumptions: CycleGAN-style domain transfer can learn defect generation from defect-free and defective domains.

## Contribution

- Claimed: PreCaCycleGAN improves defect generation with U-Net/DenseNet generator design, perceptual loss, and capsule discriminator.
- Shown: generated samples improve detector mAP and generalization on DAGM2007 compared with original-data and other generative augmentation settings.
- Inferred: this is not textile-specific, but it is relevant to public textured-surface synthesis methods.

## Method

- Core idea: map defect-free images to defective images while preserving non-defective regions and increasing defect detail diversity.
- Architecture / algorithm: CycleGAN framework; U-Net plus DenseNet generator; PatchGAN plus capsule-network discriminator.
- Objective / loss: least-squares loss, perceptual loss, cyclic consistency loss, identity mapping loss, and capsule margin loss components.
- Optimization: Adam; 150 iterations; batch size 1; initial learning rate 0.0002 with decay from iteration 100.
- Training data: DAGM2007 classes.
- Augmentation / synthesis: De-Train B uses synthetic defects only with defect-free samples; De-Train C mixes real and synthetic defects.

## ML / DL Extraction

### Data

- Dataset: [[DAGM2007]].
- Dataset description: public texture surface images with multiple defect classes.
- Training-set designs: De-Train A has 700 defect-free samples and 100 real defect samples; De-Train B has 700 defect-free real samples and 100 synthetic defect samples; De-Train C has 700 defect-free samples, 50 real defect samples, and 50 synthetic defect samples.
- Splits: train/test sets designed per class; exact per-table values are extensive and not fully transcribed.
- License: public dataset; exact license not reported.

### Evaluation

- Protocol: generate defects with PreCaCycleGAN, Tree-CycleGAN, and CycleGAN-TSS, then train YOLOv5, SSD, and Faster R-CNN.
- Used performance metrics: [[mAP@0.50]], data detection accuracy, defect detection rate, false detection rate.
- Hardware: single NVIDIA GeForce GTX 3060 GPU.
- Statistical tests: not reported.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| PreCaCycleGAN ranking | DAGM2007 detection | mAP@0.5 | higher | Tree-CycleGAN / CycleGAN-TSS | 51 top scores out of 60 De-Train B/C results | Summary across tables |
| Synthetic-only training | DAGM2007 detection | detection accuracy | higher | De-Train A | +3-5% | De-Train B vs De-Train A |
| Mixed real/synthetic training | DAGM2007 detection | detection accuracy | higher | De-Train A | +8-10% | De-Train C vs De-Train A |
| YOLOv5 with PreCaCycleGAN | DAGM2007 detection | detection accuracy | higher | other generators | about +4% on selected classes; +1-2% on remaining classes | Reported versus Tree-CycleGAN and CycleGAN-TSS |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP@0.50]] | detection model performance | mAP at IoU 0.5 | higher | yes | Used for YOLOv5, SSD, Faster R-CNN |
| Data detection accuracy | overall detection accuracy | correct defect and defect-free detections / total | higher | no | Not yet a metric note |
| [[Detection rate]] | defect detections | correctly detected defects / total defects | higher | no | Called DDR |
| [[False alarm rate]] | false positives | defect-free samples detected as defective among defective detections | lower | no | Called FDR |

## Dataset / Benchmark Details

- Source: DAGM2007.
- Collection: simulated texture-defect benchmark.
- Annotation: defect labels/regions as provided by dataset.
- Size: ten classes are used.
- Modalities: texture surface images.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: synthetic texture benchmark, not direct textile production imagery.

## Limitations

- Stated: not explicitly captured beyond the need for realistic and diverse generated samples.
- Inferred: results on DAGM2007 do not establish performance on textile-specific datasets.

## Reproducibility

- Code: not reported.
- Data: DAGM2007 public.
- Hardware: NVIDIA GeForce GTX 3060.
- Hyperparameters: 150 iterations, batch size 1, learning rate 0.0002 with decay from iteration 100; lambda values 10, 0.5, 0.02, capsule margins 0.9 and 0.1, lambda 0.5.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[PreCaCycleGAN]], [[GAN]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[DAGM2007]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mAP@0.50]], [[Detection rate]], [[False alarm rate]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Using ISU-GAN for unsupervised small sample defect detection]] | Shares dataset / shares method | Both use DAGM2007 and CycleGAN-derived GANs; this paper synthesizes training data, while ISU-GAN performs unsupervised repair-based detection. |

### Backlinks Updated

- [[PreCaCycleGAN]]

## Questions

- Which DAGM class-level results correspond to textile-like textures?
- Are generated samples or code available outside the paper?
