---
title: "Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images: A Multi-Method Explainability Audit"
aliases:
  - "Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition"
paper_key: "doi:10.3390/ai7030094"
paper_type: "research"
year: 2026
venue: "AI"
authors:
  - "Bogdan Marian Diaconu"
status: "processed"
topics:
  - "shortcut learning"
  - "explainable AI"
  - "photovoltaic fault recognition"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PV Panel Defect Dataset]]"
methods:
  - "[[LIME]]"
  - "[[Occlusion sensitivity]]"
  - "[[Integrated Gradients]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[LIME surrogate fidelity]]"
  - "[[IoU@Top10%]]"
  - "[[Occlusion entropy]]"
  - "[[Hoyer sparsity]]"
  - "[[Faithfulness gap]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "LIME R2w: kernel-weighted local surrogate coefficient of determination"
  - "IoU@Top10%: overlap between top 10% occlusion relevance pixels and proxy defect mask"
  - "Faithfulness gap: insertion AUC minus deletion AUC"
baselines:
  - "Baseline CNN"
  - "VGG16"
  - "ResNet50"
  - "InceptionV3"
  - "EfficientNetB0"
benchmarks:
  - "[[PV Panel Defect Dataset]]"
code: "not reported"
data: "https://www.kaggle.com/datasets/alicjalena/pv-panel-defect-dataset"
doi: "10.3390/ai7030094"
arxiv: "not reported"
url: "https://doi.org/10.3390/ai7030094"
pdf: "paper-inbox/10_processed/Research/2026 - Diaconu - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images A Multi-Method Explainability Audit.pdf"
source_file: "paper-inbox/10_processed/Research/2026 - Diaconu - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images A Multi-Method Explainability Audit.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2026 - Diaconu - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images A Multi-Method Explainability Audit.md"
extracted_text: "paper-inbox/90_processing/text/2026 - Diaconu - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images A Multi-Method Explainability Audit.txt"
related_papers:
  - "[[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]]"
  - "[[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]]"
related_concepts:
  - "[[Shortcut learning]]"
  - "[[Distribution shift]]"
related_methods:
  - "[[LIME]]"
  - "[[Occlusion sensitivity]]"
  - "[[Integrated Gradients]]"
related_datasets:
  - "[[PV Panel Defect Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[PV Panel Defect Dataset]]"
processed_at: "2026-05-29"
---
# Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images

## Summary

The paper audits CNN classifiers for photovoltaic panel fault recognition on [[PV Panel Defect Dataset]]. It compares a Baseline CNN, VGG16, ResNet50, InceptionV3, and EfficientNetB0 under a common preprocessing and training setup, then uses [[LIME]], [[Occlusion sensitivity]], and [[Integrated Gradients]] to test whether predictions are grounded in panel-intrinsic evidence or in [[Shortcut learning]] cues such as background, borders, viewpoints, and acquisition artifacts.

ResNet50 reports the strongest predictive performance among the tested models, with 82.3% accuracy and 0.825 macro-F1. EfficientNetB0 shows the strongest overall explainability evidence in the paper's analysis, with more stable panel-centered attribution and the largest average deletion-insertion faithfulness gap.

## Paper Type

Research paper. It is primarily an explainability and failure-mode audit of CNN-based photovoltaic fault classification rather than a new classifier architecture.

## Problem

Vision-based photovoltaic fault recognition can achieve useful classification scores while relying on contextual shortcuts. The paper asks whether common CNN backbones classify six RGB PV panel conditions using physically relevant panel evidence or spurious context correlated with class labels.

## Contribution

- Defines a multi-method explainability audit for PV fault recognition combining [[LIME]], [[Occlusion sensitivity]], and [[Integrated Gradients]].
- Reports quantitative reliability metrics for explanations: [[LIME surrogate fidelity]], [[IoU@Top10%]], [[Occlusion entropy]], [[Hoyer sparsity]], and [[Faithfulness gap]].
- Shows that predictive accuracy and explanation faithfulness are only partially aligned.
- Identifies Clean, Electrical-damage, and Physical-damage as shortcut-sensitive classes under the studied dataset and models.

## Method

The experiment uses [[PV Panel Defect Dataset]], selecting 875 RGB images across six classes: Clean, Dusty, Bird-drop, Electrical damage, Physical damage, and Snow-covered. Images are resized to 224 x 224 for Baseline CNN, EfficientNetB0, ResNet50, and VGG16, and 299 x 299 for InceptionV3. Inputs are RGB-normalized to `[0, 1]`. No data augmentation is applied so the audit reflects the original heterogeneous data distribution.

The dataset is split into stratified 80/20 training and validation subsets. The paper also performs 30 repeated stratified hold-out runs to test robustness to partitioning.

## Evidence

### Predictive Performance

The source text reports that the Baseline CNN reaches 63.8% accuracy and 0.618 macro-F1. Transfer-learning models outperform it, and ResNet50 is the best reported classifier with 82.3% accuracy and 0.825 macro-F1. The full per-architecture tables are provided as supplementary files rather than in the extracted main text.

### LIME Audit

The paper uses superpixel LIME with a local Ridge surrogate and reports [[LIME surrogate fidelity]]. Baseline CNN has the highest mean local surrogate fidelity but lower predictive performance, while VGG16 has high confidence but poor local surrogate fidelity.

| Architecture | Mean R2w | R2w p10 | Mean predicted-class probability | Low-fidelity fraction | Mean superpixels |
|---|---:|---:|---:|---:|---:|
| VGG16 | 0.289 | 0.171 | 0.88 | 0.425 | 159 |
| ResNet50 | 0.4159 | 0.293 | 0.81 | 0.078 | 159 |
| InceptionV3 | 0.476 | 0.386 | 0.69 | 0 | 279 |
| EfficientNetB0 | 0.558 | 0.457 | 0.67 | 0 | 159 |
| Baseline CNN | 0.915 | 0.853 | 0.60 | 0 | 159 |

### Occlusion Sensitivity Audit

Occlusion sensitivity directly masks image patches and measures confidence drops. The paper reports [[IoU@Top10%]], [[Occlusion entropy]], and [[Hoyer sparsity]] to separate localization, dispersion, and compactness.

| Architecture | IoU@Top10% | Entropy | Hoyer sparsity | Predicted probability |
|---|---:|---:|---:|---:|
| VGG16 | 0.172 +/- 0.145 | 8.391 +/- 2.700 | 0.520 +/- 0.277 | 0.887 +/- 0.165 |
| ResNet50 | 0.130 +/- 0.114 | 9.321 +/- 3.157 | 0.183 +/- 0.252 | 0.804 +/- 0.186 |
| InceptionV3 | 0.111 +/- 0.064 | 10.321 +/- 2.209 | 0.013 +/- 0.094 | 0.674 +/- 0.195 |
| EfficientNetB0 | 0.096 +/- 0.051 | 9.760 +/- 0.555 | 0.449 +/- 0.146 | 0.658 +/- 0.197 |
| Baseline CNN | 0.083 +/- 0.030 | 9.994 +/- 0.368 | 0.385 +/- 0.115 | 0.550 +/- 0.202 |

The paper cautions that compact maps are not necessarily correctly localized and that high IoU can coexist with weak faithfulness.

### Integrated Gradients Audit

The paper computes [[Integrated Gradients]] from a zero-valued baseline and evaluates the attributions with deletion-insertion tests. [[Faithfulness gap]] is defined as insertion AUC minus deletion AUC. EfficientNetB0 and ResNet50 are the only architectures reported as uniformly positive across all six classes; other architectures show negative or near-zero class-level gaps in some categories.

## ML/DL Extraction

- Task formulation: six-class RGB photovoltaic panel condition classification.
- Inputs: heterogeneous RGB PV panel images from [[PV Panel Defect Dataset]].
- Outputs: Clean, Dusty, Bird-drop, Electrical damage, Physical damage, or Snow-covered.
- Models: Baseline CNN trained from scratch; VGG16, ResNet50, InceptionV3, and EfficientNetB0 transfer-learning classifiers.
- Training details: stratified 80/20 split, no augmentation, model-specific input sizes and preprocessing.
- Evaluation protocol: classification metrics plus LIME, occlusion sensitivity, and Integrated Gradients audits.
- Artifacts: Kaggle dataset and Zenodo LIME visualization outputs are reported; model code is not reported.

## Limitations

- The dataset has 875 selected images and heterogeneous backgrounds, viewpoints, and acquisition conditions; the paper treats this as useful for auditing shortcut risk but limited for generalization.
- Quantitative localization metrics depend on automatically generated proxy masks, which are ambiguous for diffuse classes such as Dusty and Snow-covered.
- XAI outputs depend on hyperparameters and baselines, including LIME superpixel segmentation, occlusion patch size/stride, and Integrated Gradients baseline choice.
- The architecture comparison is limited to CNNs; Vision Transformer models are proposed as future work.
- Deployment-grade PV monitoring would need larger curated multi-site field data, calibration, uncertainty, domain adaptation, and context manipulation tests.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[LIME]], [[Occlusion sensitivity]], [[Integrated Gradients]], [[Deep convolutional neural network]]
- Datasets: [[PV Panel Defect Dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[LIME surrogate fidelity]], [[IoU@Top10%]], [[Occlusion entropy]], [[Hoyer sparsity]], [[Faithfulness gap]]

### Shares Dataset

- [[PV Panel Defect Dataset]]: the paper uses a selected 875-image subset from this Kaggle dataset.

### Shares Task

- [[Solar cell defect detection]]: recognizes visual PV panel fault states.
- [[Defect classification]]: predicts six panel condition classes.

### Shares Method

- [[LIME]]: superpixel surrogate explanations with kernel-weighted fidelity.
- [[Occlusion sensitivity]]: patch masking to test functional relevance.
- [[Integrated Gradients]]: gradient-based attributions evaluated with deletion-insertion faithfulness.
- [[Deep convolutional neural network]]: CNN backbones are the audited classifier family.

### Shares Metric

- [[Accuracy]], [[Precision]], [[Recall]], and [[F1-score]] evaluate classification.
- [[LIME surrogate fidelity]], [[IoU@Top10%]], [[Occlusion entropy]], [[Hoyer sparsity]], and [[Faithfulness gap]] evaluate explanation reliability, localization, concentration, and faithfulness.

### Application/Domain

- [[Solar cells and photovoltaic]]: RGB image-based PV panel monitoring and fault recognition.

### Related Concept

- [[Shortcut learning]]: the paper's central risk claim is that high accuracy can rely on contextual proxies rather than physically relevant panel evidence.

### Follow-up Reading

- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] evaluates a hybrid classifier on related clean/faulty solar panel classes.
- [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] is related PV panel defect detection work.

## Questions

- How would the CNN ranking change under PV-centric cropping or explicit background randomization?
- Would the same faithfulness patterns hold for larger curated field datasets?
- Do Vision Transformer models reduce or amplify the shortcut risks observed for CNN backbones?
