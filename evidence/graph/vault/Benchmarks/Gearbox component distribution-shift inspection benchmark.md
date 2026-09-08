---
title: "Gearbox component distribution-shift inspection benchmark"
aliases:
  - "Gearbox remanufacturing inspection benchmark"
  - "S1-S4 gearbox component split benchmark"
tags:
  - benchmark
  - dataset
  - remanufacturing
---

# Gearbox Component Distribution-Shift Inspection Benchmark

## Definition

Gearbox component distribution-shift inspection benchmark is the OK/nOK classification protocol introduced with [[Gearbox components remanufacturing inspection dataset]]. It uses four split configurations to evaluate visual quality inspection models under increasing train-test discrepancy.

## Why It Matters

Random splits can overstate inspection performance when train and test images share the same components or acquisition settings. This benchmark stresses generalization to new component sides, physical parts, and component categories in [[Remanufacturing inspection]].

## Used In These Papers

- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] introduces the S1-S4 protocol and reports baseline [[F1-score]] results.

## Benchmark Protocol

- Dataset: [[Gearbox components remanufacturing inspection dataset]].
- Task: [[Defect classification]].
- Training data: RGB image patches labeled OK or nOK.
- Test data: held-out patches defined by split protocol.
- S1: random image split.
- S2: acquisition-setting split.
- S3: functional-part-ID split.
- S4: component-category split, holding out synchronizer rings/cones, synchronizer bodies, synchronizer collars, and splines in separate folds while keeping gear wheels in training.
- Methods: ResNet-50, DenseNet-121, MobileNetV3-S, EfficientNetV2-M, SwinV2-B, DINOv2 with registers, and ResNet-50 with [[Contrastive regularization loss]].
- Metrics: [[F1-score]].
- Evaluation: 5-fold cross-validation for S1-S3 and 4-fold cross-validation for S4.

## Reported Results

| Method / Setting | Split | F1-score | Notes |
|---|---|---:|---|
| Fully trained model architectures | S1 | over 96% | All fully trained models exceed this level with standard deviation below 0.4%. |
| Baseline model range | S4 | 63%-71% | Component-category split creates the strongest reported shift. |
| DINOv2 frozen feature extractor | S1 | 91.3% | Reported as worse than fully trained versions. |
| DINOv2 frozen feature extractor | S4 | 63.3% | Indicates a domain gap between pretraining data and gearbox component patches. |
| ResNet-50 with [[Contrastive regularization loss]] | S4 | about 76% | Improves from about 71% without the added term. |

## Related Concepts

- [[Gearbox components remanufacturing inspection dataset]]
- [[Remanufacturing inspection]]
- [[Distribution shift]]
- [[Defect classification]]
- [[F1-score]]
- [[Contrastive regularization loss]]
