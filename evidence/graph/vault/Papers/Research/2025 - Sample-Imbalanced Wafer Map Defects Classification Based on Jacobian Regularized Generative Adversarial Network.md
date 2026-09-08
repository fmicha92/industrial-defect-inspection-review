---
title: "Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network"
aliases:
  - "Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network"
  - "JRGAN wafer map defects"
paper_key: "doi:10.1088/1361-6501/adb327"
paper_type: research
year: 2025
venue: "Measurement Science and Technology"
authors:
  - "Jialin Li"
  - "Ran Tao"
  - "Shirong Li"
  - "Yuxiong Li"
  - "Xianzhen Huang"
status: processed
processed_at: 2026-05-22
topics:
  - "wafer map defect classification"
  - "class imbalance"
  - "GAN augmentation"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
methods:
  - "[[JRGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[ResNet-18]]"
model_family:
  - "[[GAN]]"
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[ResNet-18]]"
losses:
  - "adversarial loss"
  - "auxiliary classification loss"
  - "Jacobian regularization"
optimizers:
  - "[[Adam]]"
  - "SGDM"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "precision = TP / (TP + FP)"
  - "recall = TP / (TP + FN)"
  - "F1 = 2 * precision * recall / (precision + recall)"
  - "accuracy is computed over N defect types"
baselines:
  - "Original imbalanced data"
  - "ACGAN"
  - "Data down sampling"
  - "Data up sampling"
  - "CAE"
  - "CVAE"
  - "ACDDPM-ResNet"
benchmarks:
  - "[[WM-811K]]"
  - "[[MixedWM38]]"
code: "not reported"
data: "[[WM-811K]], [[MixedWM38]]"
doi: "10.1088/1361-6501/adb327"
arxiv: "2022.10155"
url: "https://doi.org/10.1088/1361-6501/adb327"
pdf: "paper-inbox/10_processed/Research/2025 - Li - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network.pdf"
related_methods:
  - "[[JRGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[ResNet-18]]"
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
source_file: "paper-inbox/10_processed/Research/2025 - Li - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Li - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Li - Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network.txt"
artifact_status: "code not reported; evaluates public wafer-map datasets"
tags:
  - paper
---
# Sample-Imbalanced Wafer Map Defects Classification Based on Jacobian Regularized Generative Adversarial Network

## Summary

Li et al. propose [[JRGAN]], a Jacobian-regularized auxiliary-classifier GAN for generating wafer-map defect samples under class imbalance, then train [[ResNet-18]] classifiers on balanced MIR-WM811K and [[MixedWM38]] data. The method adds Jacobian regularization to both the generator and discriminator to reduce sensitivity to small input changes, stabilize adversarial training, and improve generated sample diversity.

On MIR-WM811K, JRGAN-balanced data reaches 97.24% accuracy, compared with 95.14% on original imbalanced data and 96.32% with ACGAN balancing. On MixedWM38, JRGAN Trial 3 reaches 97.38% accuracy after artificially imbalanced training data are rebalanced, compared with 94.19% for the imbalanced Trial 2 and 96.91% for the original balanced Trial 1.

## Paper Type

- Type: research.
- Why: The paper proposes a GAN-based data augmentation method and evaluates downstream wafer-map classification on two wafer datasets.

## Problem

- Task: [[Wafer map defect classification]] under severe class imbalance.
- Setting: wafer quality inspection in [[Semiconductor and electronics]].
- Inputs: wafer maps resized to 64 x 64 and converted to three-channel one-hot/RGB tensors.
- Outputs: wafer defect class labels from a ResNet classifier.
- Core difficulty: rare defect types provide too few samples for robust deep classifier training; simple geometric augmentation can produce near-duplicates, while ordinary GANs can be unstable and generate mixed or low-quality defect patterns.

## Contribution

- Introduces [[JRGAN]], an ACGAN-style sample generation model with Jacobian regularization on both generator and discriminator losses.
- Uses generated samples to balance MIR-WM811K and artificially imbalanced MixedWM38 training distributions.
- Evaluates generated sample quality with CAE feature extraction and t-SNE visualizations, then evaluates downstream [[ResNet-18]] classification.
- Reports improved accuracy over original imbalanced data, ACGAN, sampling, CAE, CVAE, and several published wafer-map classifiers.

## Dataset

### MIR-WM811K

- Source dataset: 811,457 real wafer images from 46,293 batches of chip manufacturing process data.
- Labeled subset: 172,950 wafers, 21.3% of the full dataset.
- Defect-free/None class: 147,431 labeled wafers, 85.2% of the labeled subset.
- Labeled defect classes: 25,519 wafers across eight defect categories.
- Image sizes: 632 different wafer-map sizes, ranging from 6 x 21 to 300 x 202.
- Preprocessing: resize to 64 x 64 and convert pixel states to three-channel one-hot encoding: outside wafer, normal inside wafer, and defective inside wafer.

| Class | Total | Test 20% | Original train 80% | ACGAN train | JRGAN train |
|---|---:|---:|---:|---:|---:|
| Center | 4,294 | 859 | 3,435 | 10,000 | 10,000 |
| Donut | 555 | 111 | 444 | 10,000 | 10,000 |
| Edge-Loc | 5,189 | 1,038 | 4,151 | 10,000 | 10,000 |
| Edge-Ring | 9,680 | 1,936 | 7,744 | 10,000 | 10,000 |
| Loc | 3,593 | 719 | 2,874 | 10,000 | 10,000 |
| Near-Full | 149 | 30 | 119 | 10,000 | 10,000 |
| Random | 866 | 173 | 693 | 10,000 | 10,000 |
| Scratch | 1,193 | 239 | 954 | 10,000 | 10,000 |
| None | 147,431 | 29,486 | 117,945 | 24,000 | 24,000 |
| Total | 172,950 | 34,591 | 138,359 | 104,000 | 104,000 |

### MixedWM38

- Dataset size: more than 38,000 wafer maps.
- Classes: 1 normal mode, 8 single-defect modes, and 29 mixed-defect modes, for 38 total classes.
- Mixed-defect structure: 13 two-defect classes, 12 three-defect classes, and 4 four-defect classes.
- Class counts: most defect classes have 1,000 examples; C7 Near-Full has 149, C9 Random has 866, and C24 (C + EL + S) has 2,000.
- Trial setup: Trial 1 uses an 80/20 original split; Trial 2 artificially imbalances the training set by sampling each defect type at a 0.2 to 1 ratio; Trial 3 uses JRGAN to rebalance Trial 2 while retaining the same test set.

## Method

### JRGAN Sample Generation

- Base structure: ACGAN-style generator, discriminator, and auxiliary classifier.
- Generator input: random noise vector and sample label.
- Discriminator output: real/fake probability and class probability.
- Generator objective: adversarial loss plus class consistency loss, with Jacobian regularization added.
- Discriminator objective: real/fake source loss plus auxiliary classification loss, with Jacobian regularization added.
- Generator regularization: penalizes the Frobenius norm of the Jacobian of generated samples with respect to the noise vector.
- Discriminator regularization: penalizes the Frobenius norm of the Jacobian of discriminator output with respect to input images.
- Intended effect: smoother gradient updates, lower sensitivity to perturbations, better convergence, and more diverse generated wafer maps.

### Generated Sample Evaluation

- Uses a convolutional autoencoder to extract low-dimensional image features.
- Uses t-SNE scatter plots to compare original samples, ACGAN-generated samples, and JRGAN-generated samples.
- Visual comparison reports that JRGAN samples have less noise, clearer defect categories, and more complex diversity than ACGAN samples.

### ResNet Classification

- Classifier: [[ResNet-18]].
- Input: 64 x 64 x 3 wafer-map tensors.
- MIR-WM811K classifier training: mini-batch size 128, initial learning rate 0.02, dropout 0.5 every 10 steps, maximum 40 epochs, SGDM optimizer.
- JRGAN training: batch size 64, images 64 x 64, learning rate 0.001, maximum 80 cycles, Adam optimizer.

## Evidence

### MIR-WM811K Results

| Training condition | Recall | Precision | F1 | Accuracy |
|---|---:|---:|---:|---:|
| Original imbalanced data | 81.18 | 82.87 | 81.11 | 95.14 |
| ACGAN balanced data | 82.89 | 84.87 | 83.35 or 83.85 | 96.32 |
| JRGAN balanced data | 88.72 | 88.54 | 88.51 | 97.24 |

The source contains a minor inconsistency for ACGAN F1: Table 2 gives 83.35 average F1, while Table 3 gives 83.85. JRGAN improves MIR-WM811K accuracy by +2.10 points over original imbalanced data and +0.92 points over ACGAN in Table 3.

### MIR-WM811K Per-Class Effects

| Class | Original recall | ACGAN recall | JRGAN recall | Original F1 | ACGAN F1 | JRGAN F1 |
|---|---:|---:|---:|---:|---:|---:|
| Center | 90.34 | 92.55 | 94.18 | 91.51 | 92.17 | 93.91 |
| Donut | 88.29 | 86.49 | 90.09 | 83.76 | 80.67 | 86.20 |
| Edge-Loc | 82.18 | 82.66 | 85.29 | 77.72 | 80.22 | 84.95 |
| Edge-Ring | 95.35 | 98.19 | 96.07 | 95.11 | 96.42 | 95.28 |
| Loc | 53.69 | 65.09 | 83.23 | 63.38 | 73.88 | 85.85 |
| Near-Full | 96.67 | 83.33 | 93.33 | 93.55 | 90.91 | 96.55 |
| Random | 94.80 | 94.80 | 92.49 | 87.23 | 87.47 | 86.26 |
| Scratch | 30.54 | 44.35 | 65.27 | 40.37 | 49.81 | 69.49 |
| None | 98.78 | 98.52 | 98.50 | 97.14 | 97.57 | 98.21 |

### MIR-WM811K Augmentation Baselines

| Method | Recall | Precision | F1 | Accuracy |
|---|---:|---:|---:|---:|
| Data down sampling | 83.36 | 84.25 | 83.80 | 96.12 |
| Data up sampling | 82.02 | 83.36 | 83.70 | 95.85 |
| CAE | 82.21 | 83.96 | 83.08 | 94.92 |
| CVAE | 84.23 | 85.35 | 84.71 | 96.20 |
| ACDDPM-ResNet | 90.84 | 86.93 | 88.71 | 97.13 |
| ACGAN balanced | 82.89 | 84.87 | 83.85 | 96.32 |
| JRGAN balanced | 88.72 | 88.54 | 88.51 | 97.24 |

JRGAN has the highest MIR-WM811K accuracy in this table, while ACDDPM-ResNet has slightly higher recall and F1.

### MixedWM38 Results

| Method / condition | Recall | Precision | F1 | Accuracy |
|---|---:|---:|---:|---:|
| Trial 1 original balanced | 96.90 | 96.80 | 96.81 | 96.91 |
| Trial 2 imbalanced | 94.23 | 93.92 | 93.92 | 94.19 |
| JRGAN Trial 3 | 97.27 | 97.23 | 97.79 | 97.38 |

### MixedWM38 Augmentation Baselines

| Method | Recall | Precision | F1 | Accuracy |
|---|---:|---:|---:|---:|
| CAE | 94.46 | 94.20 | 94.33 | 94.52 |
| CVAE | 95.68 | 94.30 | 94.98 | 96.12 |
| ACGAN | 96.38 | 96.23 | 96.30 | 95.56 |
| ACDDPM-ResNet | 97.52 | 97.88 | 97.67 | 97.84 |
| Trial 2 imbalanced | 94.23 | 93.92 | 93.92 | 94.19 |
| JRGAN Trial 3 | 97.27 | 97.23 | 97.79 | 97.38 |

JRGAN has the highest F1 in this table, while ACDDPM-ResNet has higher accuracy, recall, and precision.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported value |
|---|---|---|---|---|---|
| [[Accuracy]] | wafer defect classification | accuracy over N defect types | higher is better | yes | 97.24% on MIR-WM811K; 97.38% on MixedWM38 |
| [[Precision]] | wafer defect classification | TP / (TP + FP) | higher is better | no | 88.54% on MIR-WM811K; 97.23% on MixedWM38 |
| [[Recall]] | wafer defect classification | TP / (TP + FN) | higher is better | no | 88.72% on MIR-WM811K; 97.27% on MixedWM38 |
| [[F1-score]] | wafer defect classification | harmonic mean of precision and recall | higher is better | no | 88.51% on MIR-WM811K; 97.79% on MixedWM38 |

## ML/DL Extraction

- Supervision: supervised wafer-map classification, with class-conditional GAN generation.
- Generator input: random noise plus sample labels.
- Synthetic data: generated wafer defect images for minority or imbalanced classes.
- Classifier: [[ResNet-18]] trained after data balancing.
- Quality evaluation: CAE feature extraction, t-SNE visualization, and visual comparison of generated samples.
- Optimizers: Adam for JRGAN training; SGDM for ResNet classification in the MIR-WM811K experiment.
- Seeds/statistical tests: not reported.
- Hardware: not reported.
- Code: not reported.

## Limitations

- JRGAN does not uniformly dominate all baselines: ACDDPM-ResNet has higher MIR-WM811K recall/F1 and higher MixedWM38 accuracy/recall/precision in the reported augmentation-baseline tables.
- The source relies heavily on visual/t-SNE evidence for generated sample quality and does not report FID, IS, or other standard generative quality metrics.
- Hardware, seeds, variance across runs, and code availability are not reported.
- Scratch remains difficult on MIR-WM811K even after JRGAN balancing, with recall 65.27%.
- MixedWM38 imbalance is artificially induced rather than naturally observed.

## Reproducibility

- Code: not reported.
- Data: MIR-WM811K and MixedWM38.
- JRGAN training: 64 batch size, 64 x 64 images, learning rate 0.001, max 80 cycles, Adam.
- ResNet training: 128 mini-batch size, 64 x 64 x 3 input, initial learning rate 0.02, dropout 0.5 every 10 steps, max 40 epochs, SGDM.
- Environment/hardware: not reported.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[JRGAN]], [[GAN]], [[Data augmentation]], [[Synthetic data generation]], [[ResNet-18]]
- Datasets: [[WM-811K]], [[MixedWM38]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Shares Dataset

- [[WM-811K]]: the MIR-WM811K experiment uses labeled wafer maps and balances rare defect classes.
- [[MixedWM38]]: the second experiment creates an imbalanced setting and uses JRGAN to rebalance mixed wafer defect classes.

### Shares Method

- [[JRGAN]]: the paper introduces the Jacobian-regularized GAN augmentation method.
- [[GAN]]: JRGAN is an auxiliary-classifier GAN variant.
- [[Data augmentation]] and [[Synthetic data generation]]: generated wafer images are used to rebalance training sets.
- [[ResNet-18]]: the downstream classifier used after balancing.

### Application/Domain

- [[Semiconductor and electronics]]: the datasets and task are wafer-map quality inspection in chip manufacturing.

### Follow-Up Reading

- [[2021 - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects]]: another GAN-based approach for WM-811K imbalance, using multigranularity ResNet101 features and feature matching.
- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]]: another non-GAN augmentation approach for WM-811K class balancing.

## Questions

- What values were used for the generator and discriminator Jacobian regularization coefficients?
- What hardware and wall-clock training cost are required for JRGAN?
- Would JRGAN still outperform ACGAN and sampling under repeated random train/test splits?
- How do JRGAN samples score under quantitative generative metrics such as FID or nearest-neighbor tests?
