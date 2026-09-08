---
title: "Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection"
aliases:
  - "OCR-GAN"
  - "Omni-frequency Channel-selection Reconstruction"
paper_key: "doi:10.1109/tip.2023.3293772"
paper_type: research
year: 2023
venue: "IEEE Transactions on Image Processing"
authors:
  - "Yufei Liang"
  - "Jiangning Zhang"
  - "Shiwei Zhao"
  - "Runze Wu"
  - "Yong Liu"
  - "Shuwen Pan"
status: processed
processed_at: 2026-05-22
topics:
  - "unsupervised anomaly detection"
  - "frequency decoupling"
  - "reconstruction-based anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[DAGM2007]]"
  - "[[KolektorSDD]]"
  - "[[CIFAR-10]]"
methods:
  - "[[OCR-GAN]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Adam]]"
model_family:
  - "reconstruction-based network"
  - "generative adversarial network"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "Skip-GANomaly"
  - "DGAD"
  - "DifferNet"
  - "CutPaste"
  - "Draem"
code: "available in additional materials"
data:
  - "[[MVTec AD]]"
  - "[[DAGM2007]]"
  - "[[KolektorSDD]]"
  - "[[CIFAR-10]]"
optimizers:
  - "[[Adam]]"
losses:
  - "content loss"
  - "adversarial loss"
  - "latent loss"
evaluation_protocol: "image-level anomaly detection with AU-ROC from normalized anomaly scores"
hardware: "TITAN RTX GPU"
doi: "10.1109/TIP.2023.3293772"
arxiv: "not applicable"
url: "https://doi.org/10.1109/TIP.2023.3293772"
pdf: "paper-inbox/10_processed/Research/2023 - Liang - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Liang - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Liang - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Liang - Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection.txt"
artifact_status: "processed"
tags:
  - "paper"
  - "unsupervised-anomaly-detection"
  - "frequency-decoupling"
---

# Omni-Frequency Channel-Selection Representations for Unsupervised Anomaly Detection

## Summary

- The paper proposes OCR-GAN, a reconstruction-based unsupervised anomaly detection network that reconstructs low- and high-frequency image components with parallel generators.
- Frequency Decoupling separates an input image into omni-frequency images, while Channel Selection adaptively exchanges channel information among frequency-specific encoders.
- OCR-GAN is trained from scratch on normal samples, uses CutPaste and CutOut to create forged abnormal samples for discriminator training, and scores anomalies with a weighted combination of image-space and latent-space reconstruction errors.
- Reported image-level AU-ROC reaches 98.3 on [[MVTec AD]], 99.3 on [[DAGM2007]], 91.4 on [[KolektorSDD]], and 79.5 on [[CIFAR-10]] Setting 1.

## Paper Type

Research paper. It introduces a reconstruction-based GAN architecture for unsupervised sensory anomaly detection and evaluates it against reconstruction-, density-, and classification-based baselines on public anomaly-detection datasets.

## Contribution

- Claimed: normal and abnormal sensory anomaly images differ in frequency distribution, so reconstruction should model frequency components explicitly.
- Claimed: channel selection enables interaction among frequency-specific encoders.
- Shown: two-frequency OCR-GAN reaches 98.3 mean detection AU-ROC on MVTec AD without pretrained models or extra training data.
- Shown: FD and CS drive most of the ablation gain over Skip-GANomaly, while forged abnormal samples from CutPaste and CutOut provide additional training signal.

## Method

- **Frequency Decoupling:** the input image is repeatedly blurred, downsampled, upsampled, and differenced to produce frequency-specific images. The default model uses two branches, interpreted as low- and high-frequency branches.
- **Parallel reconstruction:** separate generators reconstruct the decoupled frequency images; abnormal test images are expected to reconstruct poorly because training uses normal samples only.
- **Channel Selection:** global average pooled channel statistics from frequency branches are passed through a fully connected layer and branch-specific softmax-style weights. The resulting attention vectors reweight frequency-branch feature maps at each encoder stage.
- **Training:** the model is trained end-to-end from scratch with normal images. CutPaste and CutOut generate forged abnormal samples; forged samples and generator reconstructions are positive discriminator inputs, while original normal samples are negative inputs.
- **Losses:** total loss combines content loss, adversarial loss, and latent loss with weights reported as `lambda_rec = 50`, `lambda_adv = 1`, and `lambda_lat = 1`.
- **Inference:** anomaly score combines reconstruction error and latent representation error with `lambda = 0.9`, then scales test-set scores to `[0, 1]`.

## Experimental Setup

- Implementation: PyTorch 1.2.0 and CUDA 10.2.
- Hardware: TITAN RTX GPU.
- Optimizer: [[Adam]] with `beta1 = 0.5`, `beta2 = 0.999`, `weight_decay = 1e-4`, and learning rate `0.002`.
- Batch sizes: 32 for MVTec AD; 64 for DAGM, KolektorSDD, and CIFAR-10.
- Default branches/channels: two frequency branches and 64 feature channels per generator, except the parameter-count ablation.
- Metric: image-level AU-ROC; higher is better.

## Datasets

| Dataset | Use in paper | Source-reported details |
|---|---|---|
| [[MVTec AD]] | sensory anomaly detection | 5,354 high-resolution color images across 10 object and 5 texture categories; training samples per category range from 60 to 320; test abnormalities include cracks, scratches, deformation, and holes; images are downscaled to 256 x 256. |
| [[DAGM2007]] | sensory surface defect detection | 10 surface/defect classes with artificially generated defects; 8,050 training and 8,050 testing images; positive:negative ratio approximately 1:7; OCR-GAN trains only on anomaly-free training samples. |
| [[KolektorSDD]] | sensory defect detection | 399 images of electrical commutator surfaces, including 347 defect-free and 52 defective images; anomalies are tiny cracks or microscopic fractions similar to background. |
| [[CIFAR-10]] | semantic anomaly detection stress test | 60,000 32 x 32 color images; one class is normal and the other classes are abnormal under Setting 1, with a second Skip-GANomaly-style setting using 45,000 normal training images and a 9,000:6,000 normal-anomaly test split. |

## Evidence

### Performance Metrics

| Dataset / setting | Metric | Reported OCR-GAN result | Comparison reported by paper |
|---|---:|---:|---|
| [[MVTec AD]] | AU-ROC | 98.3 | +18.3 over DGAD without extra training data, +3.6 over DifferNet, +1.2 over CutPaste, +0.3 over Draem; the abstract also states +38.1 over the reconstruction-based baseline. |
| [[DAGM2007]] | AU-ROC | 99.3 | Comparable to supervised methods, while previous unsupervised methods perform worse. |
| [[KolektorSDD]] | AU-ROC | 91.4 | +5.5 over Draem despite Draem using extra data. |
| [[CIFAR-10]] Setting 1 | AU-ROC | 79.5 | +7.0 over the suboptimal compared method. |
| [[CIFAR-10]] Setting 2 | AU-ROC | not reported as absolute value in extracted text | +16.3 over Skip-GANomaly. |

### Ablations

- Skip-GANomaly baseline obtains 60.2 AU-ROC on MVTec AD.
- Training the baseline with forged abnormal images from CutOut and CutPaste adds +8.3 AU-ROC.
- Adding the FD module to the baseline adds +14.6 AU-ROC.
- Adding CS after FD improves the score by +22.1 to 96.9 AU-ROC.
- Using three frequency branches adds +0.6 AU-ROC, but the paper keeps two branches as the default trade-off between effectiveness and efficiency.
- Reducing generator feature channels can improve performance; the channel-count ablation reports best performance at 4 channels with 98.7 AU-ROC on MVTec AD, while the main comparisons use 64 channels for fairness.

## Limitations

- The method is evaluated mainly as an image-level anomaly detector; the extracted text does not report pixel-level segmentation metrics.
- The lightweight 4-channel configuration outperforms the standard channel count in one ablation, but the paper leaves the design of lightweight anomaly models for future work.
- Semantic anomaly detection is treated as supporting evidence rather than the central task; the paper states that frequency-band differences are less suitable for semantic anomalies.
- Code is described as available in additional materials, but the extracted text does not provide a repository URL.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[OCR-GAN]], [[Unsupervised anomaly detection]], [[Adam]]
- Datasets: [[MVTec AD]], [[DAGM2007]], [[KolektorSDD]], [[CIFAR-10]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Shares dataset | OCR-GAN reports its headline sensory anomaly detection result on MVTec AD with 98.3 AU-ROC. |
| [[DAGM2007]] | Shares dataset | OCR-GAN evaluates unsupervised surface-defect detection on DAGM and reports 99.3 AU-ROC. |
| [[KolektorSDD]] | Shares dataset | OCR-GAN evaluates small commutator-surface defects and reports 91.4 AU-ROC. |
| [[CIFAR-10]] | Shares dataset | CIFAR-10 is used to test whether the reconstruction architecture also improves semantic anomaly detection. |
| [[Unsupervised anomaly detection]] | Shares method | The method learns from normal data and reconstructs images to expose anomalies. |
| [[OCR-GAN]] | Shares method | This paper introduces OCR-GAN's frequency-decoupled reconstruction and channel-selection encoder interaction. |
| [[Adam]] | Shares optimizer | OCR-GAN is trained with Adam using beta1 0.5, beta2 0.999, weight decay 1e-4, and learning rate 0.002. |
| [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] | Shares task | Both are reconstruction-centered anomaly detection methods; OCR-GAN focuses on frequency reconstruction while DiAD uses diffusion-guided reconstruction. |

## Questions

- Which frequency bands carry the most discriminative anomaly evidence?
- Does OCR-GAN retain performance under multi-class unified training?
