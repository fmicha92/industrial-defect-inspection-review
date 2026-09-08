---
title: "An improved hybrid solar cell defect detection approach using Generative Adversarial Networks and weighted classification"
aliases:
  - "Improved hybrid solar cell defect detection using GANs and weighted classification"
paper_key: "sha256:1d5ef170337099eff96c54785c1c7d05de186a4b376da538ae6c4545fde2606e"
paper_type: research
year: 2024
venue: "Expert Systems With Applications"
authors:
  - "Mustafa Yusuf Demirci"
  - "Nurettin Besli"
  - "Abdulkadir Gumuscu"
status: processed
processed_at: 2026-06-11
topics:
  - "solar cell defect detection"
  - "electroluminescence images"
  - "GAN augmentation"
  - "weighted classification"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[ELPV Dataset]]"
  - "[[Demirci custom EL dataset]]"
methods:
  - "[[WGAN-GP solar cell augmentation]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[VGG-16]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
baselines:
  - "ELPV only with default class weights"
  - "ELPV only with calculated class weights"
  - "Training Dataset 2 without GAN augmentation"
  - "GAN augmented dataset"
  - "cGAN augmented dataset"
  - "baseline VGG-16"
doi: "10.1016/j.eswa.2024.124230"
url: "https://doi.org/10.1016/j.eswa.2024.124230"
data: "[[ELPV Dataset]], [[Demirci custom EL dataset]]"
code: "not reported"
related_methods:
  - "[[WGAN-GP solar cell augmentation]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[VGG-16]]"
related_datasets:
  - "[[ELPV Dataset]]"
  - "[[Demirci custom EL dataset]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2024 - Demirci - An improved hybrid solar cell defect detection approach using Generative Adversarial Networks and weighted classification.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Demirci - An improved hybrid solar cell defect detection approach using Generative Adversarial Networks and weighted classification.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Demirci - An improved hybrid solar cell defect detection approach using Generative Adversarial Networks and weighted classification.txt"
artifact_status: "custom data confidential; code not reported"
tags:
  - paper
---
# An improved hybrid solar cell defect detection approach using Generative Adversarial Networks and weighted classification

## Summary

The paper combines GAN-based synthetic electroluminescence image generation, online augmentation, class-weighted loss, and a customized [[VGG-16]] classifier for binary [[Solar cell defect detection]]. It evaluates [[ELPV Dataset]] and a confidential custom real-world EL dataset. The strongest reported variant uses WGAN-GP generated images and reaches 94.11% accuracy, 96.70% recall, and 95.71% F-score on ELPV.

## Paper Type

- Type: research.
- Why: The paper proposes a data augmentation and classifier training pipeline and evaluates it quantitatively.

## Problem

- Task: binary defective/non-defective solar cell classification from electroluminescence images.
- Setting: small and imbalanced EL image datasets.
- Motivation: CNNs overfit or underperform when few defective samples are available.

## Contribution

- Claimed: GAN-based augmentation plus online augmentation improves solar-cell defect detection under limited data.
- Claimed: WGAN-GP is the best generator among GAN, cGAN, and WGAN-GP for this dataset.
- Claimed: weighted classification improves performance under ELPV class imbalance.
- Shown: WGAN-GP augmentation improves accuracy by 4.41 percentage points and recall by 17.83 percentage points relative to the original ELPV-only setting.

## Method

- Offline synthetic data: GAN, cGAN, and WGAN-GP variants trained on defective samples from ELPV plus custom EL training data.
- Online augmentation: random X/Y flipping, random scaling within +/-5%, and random shearing within +/-5% on training data.
- Final classifier: customized VGG-16 backbone with frozen early layers, 32- and 16-dimensional fully connected layers, 20% dropout, and weighted classification layer.
- Weighted loss: majority/minority weights computed from the ELPV imbalance ratio; reported values are about 0.32 for majority and 0.68 for minority.
- Training: MATLAB R2022b, RTX 3080 Ti, 30 epochs, mini-batch size 64, learning rate 1e-3, L2 regularization 1e-4, SGD with momentum 0.9.

## Data

- [[ELPV Dataset]]: 2,624 PV-cell EL images; the paper uses binary labels from original defect probabilities.
- Custom real-world EL dataset: 668 training images and 468 test images from a local manufacturer; data availability is confidential.
- Splits: ELPV is split 80/20 in 5-fold stratified cross validation; each fold uses 1,778 ELPV training images and 445 ELPV test images.
- Synthetic images: 577 generated defective images are randomly selected and added to Training Dataset 2 to form Training Dataset 3.

## Evidence

### Weighted Classification

| Setting | Accuracy | Precision | Recall | F-score | Notes |
|---|---:|---:|---:|---:|---|
| ELPV only, default weights | 89.70 | 88.16 | 78.59 | 83.00 | Baseline class weights |
| ELPV only, calculated weights | 91.54 | 93.75 | 78.87 | 85.64 | Weighted classification |

### GAN Augmentation

| Dataset / generator | Accuracy | Precision | Recall | F-score |
|---|---:|---:|---:|---:|
| Training Dataset 2, no GAN synthetic images | 93.25 | 94.69 | 83.66 | 88.77 |
| Training Dataset 3, GAN augmented | 92.31 | 94.23 | 94.43 | 94.33 |
| Training Dataset 3, cGAN augmented | 93.21 | 92.34 | 98.21 | 95.17 |
| Training Dataset 3, WGAN-GP augmented | 94.11 | 94.76 | 96.70 | 95.71 |

### Baseline vs Improvement

| Baseline result | Result after synthesis / augmentation | Metric | Delta |
|---:|---:|---|---:|
| 89.70 | 94.11 | accuracy | +4.41 |
| 78.87 | 96.70 | recall | +17.83 |
| 91.54 baseline VGG-16 | 94.11 proposed customized VGG-16 | accuracy | +2.57 |

### Custom EL Test Dataset

| Dataset | Images | Accuracy | Precision | Recall | F-score |
|---|---:|---:|---:|---:|---:|
| [[Demirci custom EL dataset]] | 468 | 93.08 | 92.05 | 94.36 | 93.17 |

## ML / DL Extraction

- Task formulation: binary classification of solar cell EL images.
- Model: customized [[VGG-16]] transfer-learning classifier.
- Synthetic data: WGAN-GP, GAN, and cGAN generated defective images.
- Evaluation protocol: 5-fold stratified cross validation.
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], and [[F1-score]].
- Code: not reported.
- Data availability: custom data confidential.

## Limitations

- GAN training is computationally complex; WGAN-GP training took 9 h 19 min in the reported setup.
- The custom dataset is confidential.
- The paper reports binary classification only and leaves multi-class defect typing and localization for future work.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[WGAN-GP solar cell augmentation]], [[GAN]], [[Data augmentation]], [[VGG-16]]
- Datasets: [[ELPV Dataset]], [[Demirci custom EL dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Relationship Notes

- Shares dataset: [[ELPV Dataset]].
- Shares task: [[Solar cell defect detection]] and [[Defect classification]].
- Shares method: [[GAN]], [[Data augmentation]], [[VGG-16]], and [[WGAN-GP solar cell augmentation]].
- Application/domain: [[Solar cells and photovoltaic]].

## Questions

- Can the reported WGAN-GP gains reproduce with a public-only training setup?
- How do generated images affect specific defect types such as cracks, finger defects, and soldering faults?
- Would a lighter classifier trained from scratch match the frozen VGG-16 model if more labeled data were available?
