---
title: "Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets"
aliases:
  - "G2LGAN wafer map classification"
paper_key: "doi:10.1186/s13640-025-00666-3)/author(tsung-han"
paper_type: research
year: 2025
venue: "EURASIP Journal on Image and Video Processing"
authors:
  - "Tsung-Han Tsai"
  - "Chieng-Yang Wang"
status: processed
processed_at: 2026-05-22
topics:
  - "wafer map defect classification"
  - "class imbalance"
  - "GAN data augmentation"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
  - "[[Taiwan company 21-defect wafer map dataset]]"
methods:
  - "[[G2LGAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[DCGAN wafer map augmentation]]"
  - "[[One-hot multi-label wafer defect decoding]]"
model_family:
  - "[[GAN]]"
  - "[[MobileNet]]"
architectures:
  - "[[G2LGAN]]"
  - "[[MobileNet]]"
losses:
  - "Hinge loss for GAN discriminator/generator training"
  - "Cross-entropy loss for classifier"
optimizers:
  - "[[Adam]]"
training_regime:
  - "GAN pretraining on all classes followed by class-specific fine-tuning"
  - "random undersampling for majority classes"
  - "G2LGAN augmentation for minority classes"
augmentation:
  - "[[G2LGAN]]"
synthetic_data:
  - "minority wafer-map classes generated to 5000 training samples when original training data are below 5000"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Inception Score]]"
  - "[[FID]]"
  - "[[MMD]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Classification metrics are macro-averaged because each category is treated as equally important under imbalance."
  - "GAN metrics include IS/MS higher-is-better; FID, kernel MMD, and Wasserstein distance lower-is-better; 1-NN accuracy closer to 0.5 is better."
baselines:
  - "ACGAN"
  - "BAGAN"
  - "CGAN"
  - "TSM'15"
  - "TII'22"
  - "ISQED'19"
  - "CSPA'20"
  - "DAC'20"
  - "TSM'20"
  - "TIE'21"
benchmarks:
  - "[[WM-811K]]"
  - "[[Taiwan company 21-defect wafer map dataset]]"
code: "not reported"
data: "WM-811K public; 21-Defect non-public industrial dataset"
doi: "10.1186/s13640-025-00666-3"
arxiv: "not reported"
url: "https://doi.org/10.1186/s13640-025-00666-3"
pdf: "paper-inbox/10_processed/Research/2025 - Tsai - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets.pdf"
related_papers:
  - "[[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]]"
  - "[[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]]"
  - "[[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[G2LGAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[WM-811K]]"
  - "[[Taiwan company 21-defect wafer map dataset]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Wafer map defect classification]]"
source_file: "paper-inbox/10_processed/Research/2025 - Tsai - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Tsai - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Tsai - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets.txt"
artifact_status: "code not reported; WM-811K public; 21-Defect non-public"
tags:
  - paper
---
# Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets

## Summary

Tsai and Wang propose [[G2LGAN]], a global-to-local GAN augmentation strategy for imbalanced [[Wafer map defect classification]]. The method first trains a generator on all wafer-map classes to learn global wafer-map structure, then fine-tunes separate class generators to learn local class-specific patterns. Generated minority-class wafer maps are combined with modified random undersampling of majority classes and a lightweight MobileNetV2-style classifier. On [[WM-811K]], the full pipeline reports 98.39% accuracy and 93.01% macro F1-score, improving over the same classifier without G2LGAN by +9.16 accuracy points and +8.76 F1 points.

## Paper Type

Research paper. It proposes a GAN augmentation method and classifier for imbalanced wafer-map defect classification, then evaluates both generated-sample quality and downstream classification.

## Problem

- Task: classify wafer maps into defect-pattern classes for semiconductor yield and root-cause analysis.
- Main challenge: labeled wafer-map data are scarce and strongly imbalanced. In WM-811K, the paper reports 811,457 wafer maps, but only 25,519 have actual defect patterns, 147,431 are labeled "None", and 638,570 are unlabeled.
- Class imbalance example: the paper reports that "None" accounts for 85.24% of the entire dataset while "Near-Full" accounts for 0.086%.
- Practical motivation: wafer-map labels are expensive and commercially sensitive, so companies do not easily disclose labeled wafer maps.

## Contribution

- Introduces [[G2LGAN]], a two-stage generator that separates global wafer-map features from local class features.
- Uses modified random undersampling to suppress majority-class dominance without permanently discarding majority-class data.
- Uses generated minority-class samples to balance training data before MobileNetV2 classification.
- Evaluates both generated data quality and downstream classification on [[WM-811K]] and the non-public [[Taiwan company 21-defect wafer map dataset]].

## Method

### Dataset Preprocessing

- Wafer-map cells have three states: 0 for none, 1 for pass, and 2 for fail.
- The paper maps these one-dimensional values into three-dimensional one-hot coordinates so the distance between states is fixed at 1 and the classifier receives balanced loss penalties.
- All WM-811K maps are resized to 64 x 64.
- Data split: 70% training and 30% testing for both WM-811K and 21-Defect.
- Leakage control: the test set is independent and is not used to train the GAN or augmented with generated samples.

### G2LGAN Augmentation

G2LGAN modifies DCGAN-style training for imbalanced wafer maps:

- It avoids checkerboard artifacts from deconvolution by resizing images first and using convolutional feature extraction.
- It replaces the original GAN loss with hinge loss to avoid generator-gradient disappearance under JS-divergence saturation.
- Stage 1 trains a pre-generative model on all classes to learn global features such as wafer outlines and random defects.
- Stage 2 fine-tunes the pre-trained generator separately by class to learn local class features.
- Minority classes are expanded to 5000 training samples when their original training count is below 5000.

### Classifier

- Backbone: MobileNetV2-style inverted residual blocks.
- Input: 64 x 64 x 3 one-hot wafer maps.
- Architecture change: removes the first full convolution of MobileNetV2 and directly uses inverted residual blocks for downsampling.
- Design emphasis: stacks bottleneck layers when feature-map depth is 8 and 16 to preserve shallow shape features because defect shape is treated as more important than absolute location.
- Model size: 46,772 parameters on WM-811K and 48,932 parameters on 21-Defect.

## Evidence

### Datasets

| Dataset | Source / access | Size and classes | Split | Role |
|---|---|---|---|---|
| [[WM-811K]] | public wafer-map dataset | 811,457 maps; 25,519 patterned, 147,431 None, 638,570 unlabeled; 9 classes for experiments | 70% train / 30% test | main benchmark |
| [[Taiwan company 21-defect wafer map dataset]] | non-public industrial dataset | 16,388 wafer maps in 21 categories | 70% train / 30% test | robustness / harder imbalance test |

### WM-811K Balancing

| Defect pattern | Train before | Test before | Train after | Test after |
|---|---:|---:|---:|---:|
| Center | 3006 | 1288 | 5000 | 1288 |
| Donut | 389 | 166 | 5000 | 166 |
| Edge-Local | 3633 | 1556 | 5000 | 1556 |
| Edge-Ring | 6776 | 2904 | 6776 | 2904 |
| Local | 2516 | 1077 | 5000 | 1077 |
| Random | 621 | 265 | 5000 | 265 |
| Scratch | 836 | 357 | 5000 | 357 |
| Near-Full | 105 | 44 | 5000 | 44 |
| None | 103202 | 44229 | 103202 | 44229 |

### GAN Quality

| Method | IS | MS | FID | Kernel MMD | WD | 1-NN accuracy |
|---|---:|---:|---:|---:|---:|---:|
| ACGAN | 8.231 | 3.316 | 16.934 | 0.493 | 7.931 | 0.691 |
| BAGAN | 9.251 | 3.513 | 16.524 | 0.512 | 8.134 | 0.724 |
| G2LGAN | 8.763 | 3.759 | 15.241 | 0.478 | 7.402 | 0.531 |

The paper cautions that IS and MS are weak for wafer maps because an ImageNet-pretrained InceptionNet classifies more than 90% of WM-811K images into only four ImageNet classes. It therefore emphasizes distance metrics and 1-NN accuracy, where G2LGAN is closest to the ideal 0.5.

### Classification Results On WM-811K

| Method | Accuracy (%) | F1-score (%) | Precision (%) | Recall (%) | Parameters |
|---|---:|---:|---:|---:|---:|
| TSM'15 | 94.63 | 73.77 | 66.34 | 83.09 | not reported |
| TII'22 | 93.42 | 94.28 | not reported | 93.27 | not reported |
| ISQED'19 | 94.70 | 73.40 | not reported | not reported | 16,285,760 |
| CSPA'20 | 98.00 | 90.00 | 90.00 | 90.00 | 2,395,520 |
| DAC'20 | 93.69 | 65.86 | 69.54 | 62.78 | 39,744 |
| TSM'20 | 97.00 | 80.66 | 78.37 | 83.11 | 113,769 |
| TIE'21 | 97.27 | not reported | not reported | not reported | not reported |
| Ours without G2LGAN | 89.23 | 84.25 | 84.59 | 83.82 | 46,772 |
| Ours with G2LGAN | 98.39 | 93.01 | 90.90 | 95.21 | 46,772 |

### Baseline vs Improvement

| Comparison | Accuracy gain | F1 gain | Precision gain | Recall gain |
|---|---:|---:|---:|---:|
| Ours with G2LGAN vs Ours without G2LGAN on WM-811K | +9.16 points | +8.76 points | +6.31 points | +11.39 points |
| Ours with G2LGAN vs Ours without G2LGAN on 21-Defect | +15.01 points | +14.87 points | +14.61 points | +15.14 points |

### Per-Class WM-811K Results

| Class | F1-score (%) | Precision (%) | Recall (%) |
|---|---:|---:|---:|
| Center | 93.16 | 89.37 | 97.28 |
| Donut | 83.73 | 83.73 | 83.73 |
| Edge-Loc | 93.56 | 90.26 | 97.11 |
| Edge-Ring | 96.33 | 94.88 | 97.83 |
| Local | 93.03 | 88.58 | 97.96 |
| Random | 89.84 | 85.14 | 95.09 |
| Scratch | 93.87 | 93.61 | 94.13 |
| Near-full | 93.97 | 92.86 | 95.12 |
| None | 99.16 | 99.69 | 98.63 |
| Average | 93.01 | 90.90 | 95.21 |

Donut is the weakest WM-811K class in the reported per-class table, which the paper attributes to its small test count and sensitivity to a small number of misclassifications.

### 21-Defect Results

| Method | Accuracy (%) | F1-score (%) | Precision (%) | Recall (%) | Parameters |
|---|---:|---:|---:|---:|---:|
| TSM'20 | 95.09 | 95.35 | 95.72 | 95.33 | 165,376 |
| Ours without G2LGAN | 80.23 | 80.58 | 81.16 | 80.01 | 48,932 |
| Ours with G2LGAN | 95.24 | 95.45 | 95.77 | 95.15 | 48,932 |

The paper also tests overlapping classes between WM-811K and 21-Defect by applying the WM-811K-trained classifier to overlapping 21-Defect categories. It claims most overlapping categories are accurately classified, supporting robustness rather than overfitting.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? |
|---|---|---|---|---|
| [[F1-score]] | imbalanced multi-class wafer-map classification | macro F1-score, percent | higher is better | yes |
| [[Accuracy]] | classification comparison | percent correct | higher is better | secondary |
| [[Precision]] | macro class precision | percent | higher is better | secondary |
| [[Recall]] | macro class recall | percent | higher is better | secondary |
| [[Inception Score]] | generated wafer-map quality | ImageNet-Inception based score | higher is better | no |
| [[FID]] | generated wafer-map distance to real maps | Inception feature distance | lower is better | no |
| [[MMD]] | generated wafer-map distance to real maps | kernel MMD | lower is better | no |

## ML / DL Extraction

- Input modality: wafer maps encoded from none/pass/fail cells into 64 x 64 x 3 one-hot maps.
- Output target: nine WM-811K classes or 21 21-Defect categories.
- Model family: GAN-based synthetic data generation plus lightweight CNN classification.
- GAN architecture: modified DCGAN-style generator/discriminator with hinge loss and two-stage global-to-local training.
- Classifier architecture: MobileNetV2-style network with inverted residual blocks and 46,772 parameters for WM-811K.
- Optimizer: Adam.
- G2LGAN optimizer: beta1 = 0, beta2 = 0.9; discriminator learning rate 0.0004; generator learning rate 0.0001.
- Classifier optimizer: Adam with beta1 = 0.9, beta2 = 0.999, initial learning rate 0.1.
- G2LGAN training: 3 epochs on all data, then 10 epochs per class; 10,000 iterations per epoch; batch size 64.
- Classifier training: 1000 epochs with step decay by factor 10 at epochs 200, 500, and 800.
- Losses: hinge loss for GAN; cross-entropy for classifier.
- Compute and hardware: not reported.

## Limitations

- Code is not reported.
- The 21-Defect dataset is non-public, limiting external reproducibility.
- The paper reports that Inception-based IS and MS are poorly matched to wafer-map images, so generated-image quality metrics require caution.
- The augmentation method is validated on wafer maps; transfer to optical inspection images is not shown.
- Seeds and variance across runs are not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[G2LGAN]], [[Data augmentation]], [[Synthetic data generation]], [[DCGAN wafer map augmentation]], [[One-hot multi-label wafer defect decoding]]
- Models: [[GAN]], [[MobileNet]]
- Datasets: [[WM-811K]], [[Taiwan company 21-defect wafer map dataset]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[F1-score]], [[Precision]], [[Recall]], [[Inception Score]], [[FID]], [[MMD]]

### Shares dataset

- [[WM-811K]] - common wafer-map benchmark also used by MGGAN and related augmentation papers.
- [[Taiwan company 21-defect wafer map dataset]] - non-public industrial validation dataset shared with earlier lightweight wafer-map augmentation work.

### Shares method

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]] - both generate synthetic wafer maps for imbalanced classification, but G2LGAN separates global all-class pretraining from local class fine-tuning.
- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] - both use generated wafer maps to improve minority-class classification on WM-811K.
- [[2025 - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network]] - both address sample-imbalanced wafer-map classification with GAN augmentation.

### Shares metric

- [[F1-score]], [[Accuracy]], [[Precision]], and [[Recall]] are used for downstream classification.
- [[FID]], [[MMD]], and [[Inception Score]] are used for generated-image quality.

## Questions

- How sensitive is G2LGAN to the chosen 5000-sample balancing target?
- Would wafer-map-specific feature extractors give more meaningful generative metrics than ImageNet Inception?
- Are generated wafer maps visually or statistically inspected by process engineers?

## Source Anchors

- DOI: https://doi.org/10.1186/s13640-025-00666-3
- Local source: `paper-inbox/90_processing/analysis-inputs/2025 - Tsai - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets.md`
