---
title: "Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects"
aliases:
  - "MGGAN"
  - "MG-GAN"
paper_key: "doi:10.1109/tii.2021.3092372"
paper_type: research
year: 2021
venue: "IEEE Transactions on Industrial Informatics"
authors:
  - "Jianbo Yu"
  - "Jiatong Liu"
status: processed
processed_at: 2026-05-22
topics:
  - "wafer map defect recognition"
  - "class imbalance"
  - "GAN augmentation"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[Multiple Granularities Generative Adversarial Network]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Deep convolutional neural network]]"
metrics:
  - "[[Accuracy]]"
  - "[[FID]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  Accuracy: "Higher is better; reported for wafer-map defect recognition."
  FID: "Lower is better; used to quantify generated wafer map quality."
  micro_F1: "Higher is better; micro-average F1 is reported as one of the class-imbalance evaluation metrics."
baselines:
  - "typical GANs"
  - "state-of-the-art DNNs"
  - "ResNet101"
  - "DCGAN"
  - "ACGAN"
  - "focal loss"
  - "class-balanced loss"
  - "LDAM"
code: "reported available: https://github.com/Carton6/MGGAN-TII"
data: "[[WM-811K]]"
doi: "10.1109/TII.2021.3092372"
arxiv: "not applicable"
url: "https://doi.org/10.1109/TII.2021.3092372"
pdf: "paper-inbox/10_processed/Research/2021 - Yu - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Yu - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Yu - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Yu - Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "wafer-map-defect-recognition"
  - "class-imbalance"
---

# Multiple Granularities Generative Adversarial Network for Recognition of Wafer Map Defects

## Summary

- The paper proposes MGGAN for wafer map augmentation and defect recognition under class imbalance and limited labels.
- MGGAN combines an auxiliary feature extractor, generator, and discriminator with feature matching and multi-granularity information.
- On WM-811K, MGGAN reports 88.02% accuracy on original data and a pretrained ResNet101 reaches 93.43% on MGGAN-enhanced data.
- The model uses generated minority-class wafer maps to balance the dataset before fine-tuning a ResNet101 classifier for wafer map defect recognition.

## Contribution

- Claimed: multi-granularity features from a pretrained ResNet101 guide generation and reduce instability or mode collapse.
- Claimed: generated small-class wafer maps improve recognition under imbalanced class distributions.
- Shown: MGGAN-enhanced training improves recognition performance on WM-811K.

## Method

- Auxiliary Feature Extractor extracts multi-granularity wafer map features.
- Generator reconstructs images guided by feature information and feature matching loss.
- Discriminator classifies and supports adversarial learning for wafer map generation and recognition.
- ResNet101 is used as the auxiliary feature extractor; deep features guide global reconstruction and shallow features guide local details in the generator.
- The discriminator uses group convolution, depthwise separable convolution, channel shuffle, skip connections, and two classifiers for image source and defect class.
- The generator loss includes the ordinary adversarial/class objective plus a feature-matching term with lambda set to 100.

## Data And Training Details

| Item | Source-backed detail |
|---|---|
| Dataset | [[WM-811K]], reported as 811,457 wafer map images with one normal pattern and eight defect patterns: center, donut, edge-local, edge-ring, local, near-full, random, and scratch. |
| Experiment subset | 22,418 wafer images randomly selected from WM-811K with class distribution matching the original dataset. |
| Preprocessing | Wafer maps resized to 96 x 96 pixels. |
| Initial split | Each class split into training, validation, and testing at 6:2:2. |
| Augmented split | MGGAN expands small classes to form a more balanced dataset, then the balanced data is split 6:4 into fine-tuning and testing sets. |
| Optimizer | RMSprop, learning rate 0.0001, gamma 0.9. |
| Schedule | Batch size 64, 2000 epochs; discriminator updated once while generator is updated twice. |
| Hardware/software | PyTorch and Keras on NVIDIA GeForce GTX 1080 Ti. |

## Evidence

### Performance Metrics

| Metric | Direction | Evaluation context | Reported values |
|---|---|---|---|
| [[Accuracy]] | Higher is better | WM-811K wafer map defect recognition | MGGAN auxiliary classifier reports 88.02% on original data; ResNet101 fine-tuned on MGGAN-enhanced data reports 93.43%. |
| [[FID]] | Lower is better | Generated wafer map quality | Used to compare auxiliary conditional inputs and AFE backbones during MGGAN training. |
| Micro-average recall / micro-average F1 | Higher is better | Class-imbalance evaluation | Defined by the paper for the WMDR experiments; exact aggregate values are in source tables/figures not fully exposed as text. |

### Main Results

| Experiment | Source-backed result |
|---|---|
| Feature-matching lambda | Lambda = 100 gives balanced generator/discriminator losses and the best ResNet101 recognition result on enhanced data. |
| Auxiliary input ablation | ResNet101 recognition reaches 93.43% with multigranularity features, 89.79% with label-vector input, and 87.65% with random-noise-only input. |
| Mode-collapse check | Without conditional information, discriminator loss drops to 0 around epoch 500, indicating mode collapse; multigranularity features stabilize training. |
| AFE backbone comparison | ResNet101 has the fastest and most stable FID downward trend among the tested feature-extractor backbones. |
| Class-imbalance comparison | ResNet101 on MGGAN-augmented data outperforms focal loss, class-balanced loss, and LDAM in the reported average recognition tests. |
| CNN comparison | MGGAN-enhanced ResNet101 reports 93.43% average accuracy and outperforms the compared CNNs in Table IV. |

### Failure Modes

- Misclassified wafer maps often have overlapping random/near-full or local/edge-local visual features.
- Minority classes remain difficult; the paper specifically highlights local, near-full, and scratch.
- Reported per-class accuracies include 86.89% on local, 90.03% on near-full, and 83.94% on scratch.

## Limitations

- Fine-tuning AFE and training MGGAN take longer than several compared CNN baselines.
- MGGAN is still challenged by similar wafer-map patterns and small defect patterns.
- The conclusion says further optimization of the generator's conditional priors and alternative lightweight CNN backbones remains future work.
- Image repair for low-quality real-time wafer maps is proposed as a possible application, not demonstrated as a main result.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[Multiple Granularities Generative Adversarial Network]], [[GAN]], [[Data augmentation]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[FID]], [[F1-score]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[WM-811K]] | Shares dataset | MGGAN evaluates wafer map defect recognition on WM-811K. |
| [[GAN]] | Shares method | MGGAN is a GAN variant for wafer map generation and enhancement. |
| [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] | Shares task | Both use synthetic or augmented wafer maps to improve defect classification under limited or imbalanced data. |
| [[Accuracy]] | Shares metric | MGGAN reports recognition accuracy on the original and generated-data-enhanced WM-811K settings. |

## Questions

- How visually diverse are the generated wafer maps for rare classes?
- Does MGGAN improve mixed-pattern recognition or mainly single-pattern classification?
