---
title: "Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation"
aliases:
  - "Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation"
paper_key: "doi:10.1049/cit2.12126"
paper_type: research
year: 2023
venue: "CAAI Transactions on Intelligence Technology"
authors:
  - "Naigong Yu"
  - "Huaisheng Chen"
  - "Qiao Xu"
  - "Mohammad Mehedi Hasan"
  - "Ouattara Sie"
status: processed
processed_at: 2026-05-21
topics:
  - "wafer map defect classification"
  - "lightweight neural networks"
  - "class imbalance"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
methods:
  - "[[WM-PeleeNet]]"
  - "[[Autoencoder-decoder data augmentation]]"
  - "[[Convolutional Block Attention Module]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[WM-PeleeNet]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[Parameter count]]"
  - "[[GFLOPs]]"
  - "[[Inference time]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy, precision, recall, and F1-score are defined from TP, TN, FP, and FN in the paper."
  - "Model complexity is reported with parameter count and FLOPs; CPU test time for 1000 wafer maps is reported as an efficiency metric."
benchmarks:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
baselines:
  - "DTE-WMFPR"
  - "WMDPI"
  - "WMFPR"
  - "T-DenseNet"
  - "Jiang MixedWM38 model"
  - "LeNet"
  - "AlexNet"
  - "VGG16"
  - "ResNet18"
  - "SqueezeNet"
  - "DenseNet121"
  - "MobileNetV2"
  - "ShuffleNetV2"
  - "PeleeNet"
code: "not reported"
data: "WM-811K and MixedWM38 are public; the paper's data availability statement points to http://mirlab.org/dataSet/public/"
doi: "10.1049/cit2.12126"
arxiv: "not reported"
related_concepts:
  - "[[Class imbalance]]"
related_methods:
  - "[[WM-PeleeNet]]"
  - "[[Autoencoder-decoder data augmentation]]"
  - "[[Convolutional Block Attention Module]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Wafer map defect classification]]"
related_benchmarks:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
source_file: "paper-inbox/10_processed/Research/2023 - Yu - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Yu - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Yu - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation.txt"
artifact_status: "data public; code not reported"
tags:
  - paper
---

# Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation

## Summary

Yu et al. propose [[WM-PeleeNet]], a pruned PeleeNet-style lightweight convolutional model for [[Wafer map defect classification]], and pair it with an autoencoder-based augmentation pipeline for class-imbalanced wafer maps. The paper targets embedded or production-line wafer inspection where conventional deep models can be too large or slow.

The method is evaluated on [[WM-811K]] and [[MixedWM38]]. On WM-811K, the paper reports 95.4% average accuracy after convolutional-autoencoder augmentation, 173.643 KB of parameters, 316.194 M FLOPs, and 22.99 s to classify 1000 wafer maps on CPU. The paper also reports 97.5% average accuracy on MixedWM38.

## Paper Type

- Type: research.
- Why: The paper proposes a lightweight CNN architecture and a wafer-map data augmentation method, then evaluates classification accuracy, class-wise behavior, and deployment-oriented efficiency.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: semiconductor wafer testing and production-line yield analysis.
- Inputs: wafer maps whose pixels encode background, normal dies, and defective dies.
- Outputs: wafer defect-pattern classes.
- Motivation: wafer defect patterns can indicate production-line fault sources, but deep models are often too complex for embedded deployment and WM-811K has severe class imbalance.
- Assumptions: wafer defect pattern shape and spatial location are useful for classification; adding diversity to minority-class wafer maps can improve generalization.

## Contribution

- Claimed: prunes PeleeNet into [[WM-PeleeNet]], a lightweight wafer-map classifier with two dense blocks, transition layers, a Stem block, [[Convolutional Block Attention Module]], global average pooling, fully connected classification, and Softmax output.
- Claimed: augments wafer maps with a convolutional autoencoder by adding Gaussian noise to the hidden feature map before decoding.
- Shown: CAE-based augmentation improves WM-811K average accuracy from 93.6% to 95.4%, with larger gains for minority classes such as Scratch and Donut.
- Shown: WM-PeleeNet keeps accuracy competitive while reducing parameters and FLOPs versus unpruned PeleeNet and larger CNN baselines.

## Method

The workflow has an offline modeling stage and an online detection stage. Offline, the paper applies median filtering, augments the wafer dataset with a convolutional autoencoder, and trains [[WM-PeleeNet]]. Online, it applies the same filtering operation to input wafer maps and classifies them with the trained network.

[[WM-PeleeNet]] is derived from PeleeNet and DenseNet-style dense connectivity. It uses a Stem block, two dense blocks, two transition layers, CBAM before final pooling and classification, and a 9-class Softmax head for the WM-811K experiment. The dense blocks use parallel branches to capture different receptive fields, matching small and large wafer defect patterns such as Centre, Loc, Scratch, Donut, and Edge-Ring.

The augmentation model is an encoder-decoder convolutional autoencoder. The encoder uses a 3 x 3 convolution and two-dimensional max pooling to form latent wafer features. Gaussian noise is added to the latent feature maps to increase generated diversity. The decoder uses a 3 x 3 deconvolution and upsampling. The reconstruction objective is mean squared error.

## Evidence

### Experimental Setup

- Datasets: [[WM-811K]] and [[MixedWM38]].
- WM-811K size: 811,457 wafer images; 172,950 are expert-labeled in the paper's description.
- WM-811K labels: Centre, Donut, Edge-Loc, Edge-Ring, Loc, Random, Scratch, NearFull, and None.
- WM-811K imbalance: None accounts for 85.2% of the labeled images.
- MixedWM38 size: more than 38,000 simulated wafer images with 38 classes, including normal, single-defect, and mixed-defect categories.
- Split: WM-811K is divided 60% training, 15% validation, and 25% test.
- Sampling: the None class is downsampled to 5000 training images.
- Preprocessing: median filtering is used to reduce random defects/noise.
- WM-811K training: 100 epochs/batches in the extracted text, learning rate 0.0001, RAdam optimizer with parameters 0.9 and 0.999, label smoothing, input size 224 x 224, and random rotation augmentation.
- MixedWM38 training: 50 epochs/batches; convergence is reported by the 30th round.
- Hardware: Dell T7920 server, 64 GB memory, dual NVIDIA 2080Ti GPUs.
- Software: Ubuntu 16.04, Python, and PyTorch.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| CAE augmentation | [[WM-811K]] / [[Wafer map defect classification]] | [[Accuracy]] | higher | 93.6% | 95.4% | Average accuracy improves by 1.8 percentage points. |
| Lightweight model | [[WM-811K]] | [[Accuracy]] | higher | PeleeNet 93.7% | 93.6% | Accuracy drops 0.1 point while parameters/FLOPs fall strongly. |
| Lightweight model | [[MixedWM38]] | [[Accuracy]] | higher | PeleeNet 97.7% | 97.5% | Accuracy drops 0.2 point relative to PeleeNet. |
| Mixed defect recognition | [[MixedWM38]] | [[Accuracy]] | higher | Jiang 93.2% | 97.5% | WM-PeleeNet is higher in 31 of 38 categories. |
| Efficiency | 1000 wafer maps | [[Inference time]] | lower | PeleeNet 40.52 s | 22.99 s | CPU classification time reported in the model comparison table. |
| Complexity | model | [[Parameter count]] | lower | PeleeNet 2.309 M | 0.169 M | Abstract reports 173.643 KB of parameters. |
| Complexity | model | [[GFLOPs]] | lower | PeleeNet 0.768 G | 0.316 G | Abstract reports 316.194 M FLOPs. |

### WM-811K Class Results

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Centre | 98.2 | 95.5 | 96.8 |
| Donut | 90.8 | 93.5 | 92.1 |
| Edge-Loc | 90.1 | 90.9 | 90.5 |
| Edge-Ring | 97.8 | 97.6 | 97.7 |
| Loc | 87.2 | 88.5 | 87.8 |
| NearFull | 87.2 | 91.9 | 89.5 |
| Random | 89.6 | 95.4 | 92.4 |
| Scratch | 92.3 | 88.9 | 90.6 |
| None | 100 | 100 | 100 |

### Comparison With Wafer Classification Methods

| Model | Average accuracy on WM-811K |
|---|---:|
| DTE-WMFPR | 90.5 |
| WMDPI | 90.7 |
| WMFPR | 83.1 |
| T-DenseNet | 80.8 |
| Proposed WM-PeleeNet | 93.6 |

### Augmentation And Imbalance Results

| Method | WM-811K average accuracy |
|---|---:|
| LW-based reweighting | 94.0 |
| Class-balanced sampling | 94.5 |
| Transformation-based augmentation | 93.8 |
| GAN-based augmentation | 94.1 |
| Baseline without augmentation | 93.6 |
| CAE augmentation | 95.4 |

The paper reports that Donut accuracy increases by 3.3 percentage points and Scratch accuracy increases by 5.8 percentage points after CAE augmentation. For generated-image quality, CAE exceeds GAN on SMD, Laplacian, and Tenengrad measures in the extracted comparison table.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Accuracy]] | Classification performance | (TP + TN) / (TP + FP + FN + TN) | higher | yes | 95.4% on WM-811K with CAE augmentation; 97.5% on MixedWM38. |
| [[Precision]] | Per-class WM-811K classification | TP / (TP + FP) | higher | no | Reported for all nine WM-811K classes. |
| [[Recall]] | Per-class WM-811K classification | TP / (TP + FN) | higher | no | Reported for all nine WM-811K classes. |
| [[F1-score]] | Per-class WM-811K classification | 2 * precision * recall / (precision + recall) | higher | no | Reported for all nine WM-811K classes. |
| SMD / Laplacian / Tenengrad | Generated wafer-map definition | image sharpness/definition indicators | higher | no | CAE: 51 / 84 / 233; GAN: 15 / 37 / 149. |
| [[Parameter count]] | Model compactness | model parameters | lower | no | 0.169 M in Table 7; abstract reports 173.643 KB. |
| [[GFLOPs]] | Computational complexity | multiplication-add operations | lower | no | 0.316 G / 316.194 M. |
| [[Inference time]] | CPU deployment speed | seconds per 1000 wafer maps | lower | no | 22.99 s. |

## ML / DL Extraction

### Task Formulation

- Input modality: wafer map images / wafer bin maps.
- Output target: wafer defect-pattern class.
- Supervision: supervised classification on labeled wafer maps.
- Objective: accurate and fast wafer defect-pattern classification under class imbalance.

### Model And Training

- Architecture: [[WM-PeleeNet]] with Stem block, two dense blocks, transition layers, CBAM, GAP, FC, and Softmax.
- Augmentation model: convolutional autoencoder with Gaussian noise added to latent feature maps.
- Losses: CAE uses mean squared error; classifier loss is not fully specified beyond cross-entropy variants for reweighting comparisons.
- Optimizer: RAdam.
- Learning rate: 0.0001.
- Regularization/noise handling: median filtering and label smoothing.
- Input size: 224 x 224.
- Compute: dual NVIDIA 2080Ti GPUs for experiments; CPU timing reported for 1000 wafer maps.
- Code: not reported.

### Data

- Datasets: [[WM-811K]] and [[MixedWM38]].
- WM-811K: real production wafer-map dataset with 811,457 images and 172,950 expert-labeled images.
- WM-811K classes: Centre, Donut, Edge-Loc, Edge-Ring, Loc, Random, Scratch, NearFull, and None.
- MixedWM38: simulated mixed-type wafer map dataset with 38 categories.
- Splits: WM-811K 60/15/25 train/validation/test.
- Class imbalance handling: downsample None to 5000 training images and use CAE-based augmentation to bring class counts closer to balance.
- Data availability: paper states the data are derived from a public MIR Lab resource.

### Evaluation

- Protocol: compare class-wise classification metrics, baseline wafer-map classifiers, imbalance handling strategies, generated-image quality, model complexity, and CPU inference time.
- Baselines: DTE-WMFPR, WMDPI, WMFPR, T-DenseNet, Jiang MixedWM38 model, LeNet, AlexNet, VGG16, ResNet18, SqueezeNet, DenseNet121, MobileNetV2, ShuffleNetV2, PeleeNet, GAN augmentation, transformation augmentation, class-balanced sampling, and reweighting.
- Statistical tests: not reported.
- Failure cases: Loc and Edge-Loc are confused because their shapes are similar.

## Dataset / Benchmark Details

- [[WM-811K]] is the main real semiconductor wafer-map benchmark. The paper reports its 9 basic wafer modes, the 85.2% None-class imbalance, and a 60/15/25 train/validation/test split.
- [[MixedWM38]] is used to test mixed-type wafer defect patterns with 38 categories.
- The paper reports that random defects/noise are filtered with a median filter before training and evaluation.
- Public data source: `http://mirlab.org/dataSet/public/`.

## Limitations

- Loc and Edge-Loc remain difficult to separate; the confusion matrix shows Loc samples are often misclassified as Edge-Loc and Edge-Loc samples can be confused with Edge-Ring or Loc.
- The method still requires a large amount of wafer-map data during training.
- The conclusion states that new defective wafer patterns with small sample counts cannot be effectively identified.
- Code availability is not reported.

## Reproducibility

- Code: not reported.
- Data: public WM-811K / MIR Lab source and public MixedWM38 source.
- Hyperparameters: WM-811K uses 100 training rounds, 0.0001 learning rate, RAdam parameters 0.9 and 0.999, input size 224 x 224, label smoothing, and random rotation.
- Hardware: Dell T7920, 64 GB memory, dual NVIDIA 2080Ti GPUs.
- Environment: Ubuntu 16.04, Python, PyTorch.
- Random seeds: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: median filtering.
- Artifact status: data public; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[WM-PeleeNet]], [[Autoencoder-decoder data augmentation]], [[Convolutional Block Attention Module]], [[Data augmentation]]
- Datasets: [[WM-811K]], [[MixedWM38]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[Parameter count]], [[GFLOPs]], [[Inference time]]

### Builds On

- PeleeNet and DenseNet-style dense connectivity: WM-PeleeNet prunes PeleeNet to reduce wafer-map classification complexity.
- [[Convolutional Block Attention Module]]: used before the final pooling/classifier to improve feature representation.

### Shares Dataset

- [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] introduces [[WM-811K]].
- [[2020 - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition]] introduces [[MixedWM38]].
- [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] also studies lightweight wafer-map classification and augmentation.

### Shares Task

- [[Wafer map defect classification]]

### Shares Method

- [[Autoencoder-decoder data augmentation]]
- [[Data augmentation]]
- [[Convolutional Block Attention Module]]

### Shares Metric

- [[Accuracy]]
- [[Precision]]
- [[Recall]]
- [[F1-score]]
- [[Parameter count]]
- [[GFLOPs]]
- [[Inference time]]

### Application / Domain

- [[Semiconductor and electronics]]

## Questions

- Is the reported "100 batches" wording equivalent to 100 epochs in the implementation, or a translation/extraction artifact?
- Can the authors' implementation be recovered, or is only the public data available?
- How robust is the CAE augmentation when an entirely new wafer defect pattern appears with only a few examples?
