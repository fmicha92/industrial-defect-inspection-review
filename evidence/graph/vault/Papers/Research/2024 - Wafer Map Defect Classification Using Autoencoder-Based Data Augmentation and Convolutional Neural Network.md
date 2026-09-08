---
title: "Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network"
aliases:
  - "Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network"
paper_key: "arxiv:2411.11029"
paper_type: research
year: 2024
venue: "arXiv"
authors:
  - "Yin-Yin Bao"
  - "Er-Chao Li"
  - "Hong-Qiang Yang"
  - "Bin-Bin Jia"
status: processed
processed_at: 2026-05-22
topics:
  - "wafer map defect classification"
  - "class imbalance"
  - "autoencoder data augmentation"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[Autoencoder-decoder data augmentation]]"
  - "[[Data augmentation]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "CNN-AUG"
losses:
  - "mean squared error"
  - "categorical cross-entropy"
optimizers:
  - "[[Adam]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[AU-ROC]]"
  - "[[Average precision]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "precision = TP / (TP + FP)"
  - "recall = TP / (TP + FN)"
  - "F1 = 2 * precision * recall / (precision + recall)"
  - "accuracy = (TP + TN) / (TP + FN + TN + FP)"
baselines:
  - "Logistic Regression"
  - "SVM"
  - "Random Forest"
  - "Voting Classifier"
benchmarks:
  - "[[WM-811K]]"
code: "not reported"
data: "WM-811K; paper also states data available on reasonable request"
doi: "not reported"
arxiv: "2411.11029"
url: "https://arxiv.org/abs/2411.11029"
pdf: "paper-inbox/10_processed/Research/2024 - Bao - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network.pdf"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Autoencoder-decoder data augmentation]]"
  - "[[Data augmentation]]"
  - "[[Deep convolutional neural network]]"
related_datasets:
  - "[[WM-811K]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Wafer map defect classification]]"
related_benchmarks:
  - "[[WM-811K]]"
source_file: "paper-inbox/10_processed/Research/2024 - Bao - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Bao - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Bao - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network.txt"
artifact_status: "code not reported; WM-811K public; paper states data available on reasonable request"
tags:
  - paper
---
# Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network

## Summary

Bao et al. combine [[Autoencoder-decoder data augmentation]] with a [[Deep convolutional neural network]] for eight-class [[Wafer map defect classification]] on [[WM-811K]]. The autoencoder encodes 26 x 26 x 3 wafer maps, adds Gaussian noise in the latent space, decodes reconstructed samples, and balances every defect class to 10,000 samples before training the CNN classifier.

The paper reports 98.56% accuracy for the augmented CNN, compared with 81.25% for Random Forest, 77.70% for SVM, 71.76% for Logistic Regression, and 79.51% for a soft Voting Classifier. The claimed improvement over traditional baselines is therefore about +17.31 accuracy points over the strongest listed classical baseline and +26.80 points over Logistic Regression.

## Paper Type

- Type: research.
- Why: The paper proposes a data augmentation and CNN classification pipeline, evaluates it on WM-811K, compares against classical baselines, and reports ablations.

## Problem

- Task: classify wafer defect maps into eight defect classes: Center, Donut, Edge-Loc, Edge-Ring, Loc, Near-Full, Random, and Scratch.
- Setting: semiconductor wafer-map failure pattern recognition in [[Semiconductor and electronics]].
- Challenge: labeled defect samples are scarce and heavily imbalanced, and noisy wafer maps can obscure failure patterns.
- Inputs: 26 x 26 x 3 wafer-map tensors.
- Outputs: eight-way softmax defect class probabilities.

## Contribution

- Proposes latent-space autoencoder augmentation for WM-811K defect classes: encode wafer maps, inject Gaussian noise, decode synthetic/reconstructed wafer maps, and train a CNN on the balanced set.
- Uses an augmented training distribution with 10,000 samples per defect class to reduce class imbalance.
- Shows a CNN-AUG classifier outperforming Logistic Regression, SVM, Random Forest, and Voting Classifier on accuracy, precision, recall, F1, AUC, and AP.

## Dataset

### WM-811K

- Full dataset: 811,457 wafer images with supplementary wafer core dimensions, batch numbers, and wafer indices.
- Collection: 47,543 physical fabrication lots, with up to 25 wafers per lot; the paper notes missing wafers may reflect sensor failures or other unknown issues.
- Labeled subset: 172,950 manually labeled images.
- Defective patterned subset used for eight-class classification: the paper text gives 25,519 defective wafers, but Table 1 sums to 25,519 while the prose says 24,519 in one sentence; the class counts support 25,519.
- Defect-free/normal wafers: 147,431 non-pattern wafers.
- Unlabeled share: 78.7% of wafers.

| Class | Class name | Total | Train | Test |
|---:|---|---:|---:|---:|
| 0 | Center | 4,294 | 3,238 | 1,056 |
| 1 | Donut | 555 | 404 | 151 |
| 2 | Edge-Loc | 5,189 | 3,860 | 1,329 |
| 3 | Edge-Ring | 9,680 | 7,299 | 2,381 |
| 4 | Loc | 3,593 | 2,677 | 916 |
| 5 | Near-Full | 866 | 640 | 226 |
| 6 | Random | 1,193 | 905 | 288 |
| 7 | Scratch | 149 | 116 | 33 |

- Split protocol: 4:1 train/test split before augmentation.
- Augmentation target: every defect class is expanded to 10,000 samples.
- Leakage control: the source says the split is made before augmentation, but it does not explicitly state whether no augmented variants of test-set samples can enter training.
- License: not reported.

## Method

### Autoencoder Augmentation

- Encoder input: $X \in R^{26 \times 26 \times 3}$.
- Latent representation: $Z \in R^{13 \times 13 \times 64}$.
- Encoder operation: convolution plus bias followed by ReLU.
- Decoder target: reconstruct $X$ from $Z$ using transposed convolution layers.
- Autoencoder loss: mean squared error between input wafer map and reconstruction.
- Synthesis step: add Gaussian noise $\epsilon \sim N(0, \sigma^2)$ to the latent representation, then decode $Z + \epsilon$ into a new wafer map.
- Class balancing: repeat the latent-noise decoding process per class until each of the eight defect classes has 10,000 samples.
- Training duration for the autoencoder: 30 epochs; the paper reports reconstruction loss decreasing over training.

### CNN-AUG Classifier

- Input: 26 x 26 x 3 wafer map.
- Convolutional stack: three 3 x 3 convolution layers with 16, 64, and 128 filters, ReLU activation, and same padding.
- Flattened feature vector: 86,528 features after the third convolution layer.
- Dense layers: 512-unit ReLU layer, then 128-unit ReLU layer.
- Output: 8-unit softmax layer.
- Total parameters: 44,504,840.
- Loss: categorical cross-entropy.
- Optimizer: Adam.
- Training duration: 30 epochs in the reported before/after augmentation comparison.

### Classical Baselines

- Logistic Regression, SVM, and Random Forest use engineered features.
- Voting Classifier combines Logistic Regression, SVM, and Random Forest with soft voting.
- Feature set for classical models: 59 features, consisting of 13 density features from central/peripheral wafer regions, 40 Radon-transform features, and 6 size/geometric features from the largest defect region.

## Evidence

### Main Results

| Model | Accuracy | Precision | Recall | F1 | AUC | AP |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7176 | 0.5172 | 0.5147 | 0.5137 | 0.9345 | 0.5653 |
| SVM | 0.7770 | 0.7627 | 0.7244 | 0.7283 | 0.9638 | 0.8141 |
| Random Forest | 0.8125 | 0.8482 | 0.7090 | 0.7318 | 0.9759 | 0.8476 |
| Voting Classifier | 0.7951 | 0.8050 | 0.7322 | 0.7519 | 0.9709 | 0.8397 |
| CNN-AUG | 0.9856 | 0.9877 | 0.9878 | 0.9877 | 1.0000 | 1.0000 |

### Baseline Vs Improvement

| Comparison | Accuracy gain | F1 gain | Notes |
|---|---:|---:|---|
| CNN-AUG vs Logistic Regression | +0.2680 | +0.4740 | Largest listed baseline gap. |
| CNN-AUG vs SVM | +0.2086 | +0.2594 | SVM is stronger than Logistic Regression but far below CNN-AUG. |
| CNN-AUG vs Random Forest | +0.1731 | +0.2559 | Strongest classical baseline by accuracy and AP. |
| CNN-AUG vs Voting Classifier | +0.1905 | +0.2358 | Soft-voting ensemble remains below Random Forest accuracy. |

The abstract frames the improvements as CNN-AUG outperforming Random Forest, SVM, and Logistic Regression by 19%, 21%, and 27%, respectively. Using Table 4 absolute accuracy differences gives +17.31, +20.86, and +26.80 percentage points.

### Augmentation Effect

- Before augmentation, the training accuracy approaches nearly 99%, while validation accuracy plateaus around 85%, indicating overfitting under the imbalanced data distribution.
- After autoencoder augmentation, validation accuracy reaches about 98%, with validation loss tracking training loss more closely.
- Confusion matrix examples:
  - Center improves from 96% to 99%.
  - Donut reaches 100% after augmentation.
  - Edge-Loc improves to 95%.
  - Loc improves from 80% to 97%.
  - Random improves from 39% to 100%.

### Ablation

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| CNN-AUG | 0.9856 | 0.9855 | 0.9856 | 0.9855 |
| No Conv3 | 0.9796 | 0.9795 | 0.9795 | 0.9794 |
| No Dense1 | 0.9784 | 0.9785 | 0.9785 | 0.9784 |

- Removing the third convolution layer lowers accuracy by 0.0060.
- Removing the first dense layer lowers accuracy by 0.0072.
- The ablation supports the third convolution layer and first dense layer as useful, but the performance drops are modest.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported value |
|---|---|---|---|---|---|
| [[Accuracy]] | eight-class [[Wafer map defect classification]] | $(TP + TN) / (TP + FN + TN + FP)$ | higher is better | yes | CNN-AUG: 0.9856 |
| [[Precision]] | eight-class [[Wafer map defect classification]] | $TP / (TP + FP)$ | higher is better | no | CNN-AUG: 0.9877 in Table 4; 0.9855 in ablation table |
| [[Recall]] | eight-class [[Wafer map defect classification]] | $TP / (TP + FN)$ | higher is better | no | CNN-AUG: 0.9878 in Table 4; 0.9856 in ablation table |
| [[F1-score]] | eight-class [[Wafer map defect classification]] | harmonic mean of precision and recall | higher is better | no | CNN-AUG: 0.9877 in Table 4; 0.9855 in ablation table |
| [[AU-ROC]] | one-vs-rest multi-class discrimination | mean area under ROC curve across classes | higher is better | no | CNN-AUG: 1.0000 |
| [[Average precision]] | one-vs-rest multi-class precision-recall performance | mean average precision across classes | higher is better | no | CNN-AUG: 1.0000 |

## ML/DL Extraction

- Task formulation: supervised eight-class wafer-map defect classification.
- Input/output: 26 x 26 x 3 wafer-map tensors to eight-class softmax labels.
- Architecture: autoencoder for latent-space augmentation plus CNN-AUG classifier.
- Losses: MSE for autoencoder reconstruction; categorical cross-entropy for classification.
- Optimizer: Adam for CNN-AUG; autoencoder optimizer not separately reported.
- Hyperparameters: 30 training epochs reported; Gaussian noise distribution is reported but the standard deviation value is not reported.
- Compute: Ubuntu, Python 3.8, TensorFlow 2.4, PyTorch 1.9, NVIDIA V100 GPU, Intel Xeon CPU.
- Seeds/statistical testing: not reported.

## Limitations

- The source contains an internal inconsistency: one sentence states 24,519 defective samples, while the listed defect-class totals sum to 25,519.
- The method resizes wafer maps to a uniform shape; the paper states this may distort defect patterns, especially for extreme aspect ratios.
- Scratch and Near-Full remain highlighted as minority categories needing better adaptive/class-specific augmentation and cost-sensitive learning.
- Code is not reported.
- The paper does not report random seeds, variance over repeated runs, or confidence intervals.
- Data availability is stated as available on reasonable request, even though the experiment uses the public WM-811K dataset.

## Reproducibility

- Code: not reported.
- Data: WM-811K; data availability statement says data available on reasonable request.
- Environment: Ubuntu, Python 3.8, TensorFlow 2.4, PyTorch 1.9.
- Hardware: NVIDIA V100 GPU and Intel Xeon CPU.
- Model checkpoints: not reported.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[Autoencoder-decoder data augmentation]], [[Data augmentation]], [[Deep convolutional neural network]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[AU-ROC]], [[Average precision]]

### Shares Dataset

- [[WM-811K]]: the only reported benchmark dataset.

### Shares Task

- [[Wafer map defect classification]]: the paper evaluates eight-class wafer-map failure pattern classification.

### Shares Method

- [[Autoencoder-decoder data augmentation]]: the paper uses latent-space Gaussian noise and decoder reconstruction to synthesize balanced training samples.
- [[Data augmentation]]: augmentation is the main mechanism for reducing class imbalance.
- [[Deep convolutional neural network]]: the final classifier is a CNN with three convolutional layers and two dense layers.

### Application/Domain

- [[Semiconductor and electronics]]: the wafer maps come from semiconductor fabrication quality diagnosis.

### Follow-Up Reading

- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]]: also targets WM-811K class imbalance but uses GAN-based augmentation and compares baseline-vs-augmentation gains.

## Questions

- What exact Gaussian noise standard deviation was used in the latent space?
- Were augmented variants generated only from training samples, with the test split fully isolated from augmentation?
- How stable are the reported near-perfect AUC/AP results across random seeds?
- Would the large 44.5M-parameter CNN still outperform smaller wafer-map classifiers under the same augmented data?
