---
title: "Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks"
paper_key: "doi:10.48550/arxiv.2605.11898"
paper_type: research
year: 2026
venue: "arXiv"
authors:
  - "Daniil Dushenev"
  - "Nazariy Karpov"
  - "Daniil Zinovjev"
  - "Konstantin Kulikov"
  - "Alexander Gorin"
status: processed
processed_at: 2026-06-11
topics:
  - "few-shot synthetic data generation"
  - "diffusion augmentation"
tasks:
  - "[[Small-sample defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Magnetic Tile Defects]]"
methods:
  - "[[LoRA-adapted diffusion augmentation]]"
  - "[[Diffusion models]]"
  - "[[Data augmentation]]"
optimizers:
  - "[[AdamW]]"
metrics:
  - "[[F1-score]]"
  - "[[AU-PR]]"
  - "[[Recall]]"
primary_metric: "[[F1-score]]"
doi: "10.48550/arxiv.2605.11898"
arxiv: "2605.11898"
url: "https://arxiv.org/abs/2605.11898"
pdf: "paper-inbox/10_processed/Research/2026 - Dushenev - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks.pdf"
hardware: "NVIDIA A100 80GB GPU"
code: "not reported"
data: "uses NIH ChestX-ray14 and Magnetic Tile Surface Defect Dataset"
related_methods:
  - "[[LoRA-adapted diffusion augmentation]]"
  - "[[Diffusion models]]"
related_datasets:
  - "[[Magnetic Tile Defects]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Small-sample defect classification]]"
source_file: "paper-inbox/10_processed/Research/2026 - Dushenev - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2026 - Dushenev - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks.md"
extracted_text: "paper-inbox/90_processing/text/2026 - Dushenev - Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks.txt"
tags:
  - paper
---
# Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks

## Summary

The paper studies rare-class synthetic data generation with LoRA-adapted diffusion models. It fine-tunes FLUX.2-dev adapters on few real examples, generates synthetic rare-class images without post-hoc curation, and trains ResNet-18 classifiers. On [[Magnetic Tile Defects]], mixed real-plus-synthetic training improves positive-class F1 from 0.051 to 0.296 at a 4x synthetic ratio, with recall increasing further at higher ratios.

## Paper Type

- Type: research.
- Why: The paper proposes a lightweight diffusion augmentation protocol and reports quantitative downstream classification results.

## Problem

- Task: rare-class binary classification under severe class imbalance.
- Setting: medical and industrial defect classification; the industrial evaluation uses [[Magnetic Tile Defects]].
- Inputs: few real positive-class examples and generated synthetic positive-class examples.
- Outputs: binary class predictions.

## Contribution

- Claimed: LoRA-adapted text-to-image diffusion can provide useful rare-class synthetic data under few-shot constraints.
- Shown: Magnetic Tiles F1 improves from 0.051 without synthetic data to 0.296 at 4x synthetic data.
- Shown: Magnetic Tiles recall improves from 0.063 to 0.658 at 20x synthetic data, while F1 peaks at a lower mixed ratio.

## Method

- Generator: LoRA-adapted FLUX.2-dev text-to-image diffusion model.
- Adaptation: DreamBooth-style LoRA on the DiT transformer backbone; text encoders frozen; rank 64, alpha 8, dropout 0.08.
- Optimization: 200 steps, 8-bit AdamW, learning rate 5e-3, bf16 mixed precision, NF4 quantized transformer.
- Sampling: about 1,000 synthetic images per adapter at 512x512 with 20-24 denoising steps and CFG scale 1.5-2.5.
- Downstream classifier: ImageNet-pretrained ResNet-18 with binary head and BCEWithLogitsLoss with positive-class weighting.
- Evaluation: synthetic-to-real ratios 0.5x, 1x, 2x, 4x, 10x, and 20x; five-fold cross-validation; held-out real-only test sets.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| Mixed synthetic augmentation | [[Magnetic Tile Defects]] binary classification | [[F1-score]] | 0x synthetic 0.051 | 4x synthetic 0.296 | Higher is better; best mixed F1 reported. |
| Mixed synthetic augmentation | [[Magnetic Tile Defects]] binary classification | [[AU-PR]] | 0x synthetic 0.141 | 4x synthetic 0.313 | Higher is better. |
| High-recall setting | [[Magnetic Tile Defects]] binary classification | [[Recall]] | 0x synthetic 0.063 | 20x synthetic 0.658 | F1 drops to 0.235 at 20x. |
| 1x synthetic setting | [[Magnetic Tile Defects]] binary classification | [[F1-score]] | 0x synthetic 0.051 | 1x synthetic 0.242 | Higher is better. |

## Dataset / Benchmark Details

- [[Magnetic Tile Defects]]: industrial magnetic tile surface defect dataset used for rare-class binary classification.
- NIH ChestX-ray14 is also evaluated for medical rare-class classification.
- Detailed Magnetic Tile split sizes are not reported in the extracted text.

## Limitations

- Excessive synthetic ratios can degrade F1 despite increasing recall.
- The evaluation covers two datasets and does not use prompt augmentation or post-hoc sample filtering.
- Code and generated-data release status: not reported in the extracted text.

## Connections

### Graph Hubs

- Tasks: [[Small-sample defect classification]], [[Defect classification]]
- Methods: [[LoRA-adapted diffusion augmentation]], [[Diffusion models]], [[Data augmentation]]
- Datasets: [[Magnetic Tile Defects]]
- Domains: [[Metal inspection]]
- Metrics: [[F1-score]], [[AU-PR]], [[Recall]]

### Relationship Notes

- Shares dataset: [[Magnetic Tile Defects]].
- Shares method: [[LoRA-adapted diffusion augmentation]], [[Diffusion models]], and [[Data augmentation]].
- Shares metric: [[F1-score]], [[AU-PR]], and [[Recall]].
- Application/domain: [[Metal inspection]].

## Questions

- How stable are the optimal synthetic ratios across defect types inside Magnetic Tile Defects?
- Does manual filtering improve or weaken the no-curation claim?
