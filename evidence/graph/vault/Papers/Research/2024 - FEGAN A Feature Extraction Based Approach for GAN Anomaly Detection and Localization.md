---
title: "FEGAN: A Feature Extraction Based Approach For GAN Anomaly Detection And Localization"
aliases:
  - "FEGAN"
  - "FEGAN: A Feature Extraction Based Approach For GAN Anomaly Detection And Localization"
paper_key: "doi:10.1109/access.2024.3406438"
paper_type: research
year: 2024
venue: "IEEE Access"
authors:
  - "Fu-You Fan"
  - "Lin Zhang"
  - "Yang Dai"
status: processed
processed_at: 2026-07-09
topics:
  - "GAN anomaly detection"
  - "feature extraction"
  - "anomaly localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Bottle-Cap Dataset]]"
methods:
  - "[[FEGAN]]"
  - "[[GAN]]"
  - "[[Feature extraction]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[FEGAN]]"
  - "VGG19"
losses:
  - "feature loss"
  - "content loss"
  - "adversarial loss"
optimizers:
  - "Adam"
metrics:
  - "[[AU-ROC]]"
  - "[[IoU]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "Image-level AUC-ROC evaluates anomaly detection per image."
  - "Pixel-level AUC-ROC evaluates anomaly localization per pixel."
  - "IoU evaluates overlap between predicted and ground-truth anomalous regions."
baselines:
  - "GeoTrans"
  - "GANomaly"
  - "ITAE"
  - "DAGAN"
  - "ST-m"
  - "DFR"
  - "SCGAN"
  - "AE-ssim"
  - "AnoGAN"
  - "VAE-grad"
  - "SPADE"
  - "PatchSVDD"
  - "DFC"
benchmarks:
  - "[[MVTec AD]]"
  - "[[Bottle-Cap Dataset]]"
code: "not reported"
data: "public datasets used: MVTec AD and Bottle-Cap"
doi: "10.1109/access.2024.3406438"
arxiv: "not reported"
url: "https://doi.org/10.1109/access.2024.3406438"
pdf: "paper-inbox/10_processed/Research/2024 - Fan - FEGAN A Feature Extraction Based Approach For GAN Anomaly Detection And Localization.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[FEGAN]]"
  - "[[GAN]]"
  - "[[Feature extraction]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[Bottle-Cap Dataset]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Fan - FEGAN A Feature Extraction Based Approach For GAN Anomaly Detection And Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Fan - FEGAN A Feature Extraction Based Approach For GAN Anomaly Detection And Localization.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Fan - FEGAN A Feature Extraction Based Approach For GAN Anomaly Detection And Localization.txt"
artifact_status: "code not reported; public datasets used"
tags:
  - paper
---

# FEGAN: A Feature Extraction Based Approach For GAN Anomaly Detection And Localization

## Summary

Fan et al. propose [[FEGAN]], a normal-only industrial anomaly detection and localization method that combines a VGG19-based Feature Extraction Network (FEN) with an Improved Generative Adversarial Network (IGAN). The method detects anomalies through a combined anomaly score in deep feature space and image space, and uses Multi-scale Self-Enhancement (M-SE) to simulate irregular anomaly-like perturbations from normal images.

On [[MVTec AD]], FEGAN reports 0.978 average image-level AUC-ROC, 0.982 average pixel-level AUC-ROC, and 0.399 average IoU. On [[Bottle-Cap Dataset]], it reports 0.956 image-level AUC-ROC, 0.979 pixel-level AUC-ROC, and 0.231 IoU. The authors state that FEGAN is strong for anomaly classification on both datasets but has weaker Bottle-Cap localization than DFC.

## Paper Type

- Type: research.
- Why: The paper introduces a new unsupervised/normal-only anomaly detection architecture, evaluates it on public industrial anomaly datasets, and provides ablations on enhancement, losses, and anomaly-score weights.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]] for industrial product surface images.
- Setting: normal training samples are available, while abnormal samples and labels are scarce or hard to collect.
- Inputs: RGB industrial inspection images resized to 256 x 256.
- Outputs: image-level anomaly score, anomaly heat map, and binarized anomaly segmentation.
- Motivation: traditional surface inspection is slow, low-precision, and hard to automate reliably; industrial anomalies vary by product, shape, texture, and random occurrence.

## Contribution

- Proposes [[FEGAN]], composed of a Feature Extraction Network and an Improved Generative Adversarial Network.
- Introduces Multi-scale Self-Enhancement (M-SE), which copies multi-scale regions from a normal image, applies color perturbation, and pastes them into arbitrary positions to approximate anomaly-like changes.
- Defines an anomaly score from both deep feature residuals and image-space reconstruction residuals.
- Demonstrates image-level detection, pixel-level localization, and IoU results on [[MVTec AD]] and [[Bottle-Cap Dataset]].

## Method

### Architecture

- Feature Extraction Network: VGG19 pretrained on ImageNet, using the fifth convolution block to extract high-level feature representations.
- Improved GAN: generator plus discriminator.
- Generator: asymmetric encoder-decoder with five convolutional blocks and one deconvolution block; the encoder resembles VGG19 but replaces max pooling with average pooling and removes fully connected layers.
- Decoder: reconstructs encoded features back into RGB image space with transposed convolution.
- Discriminator: distinguishes original normal images from generator reconstructions during adversarial training.

### Training And Inference

- Training uses only normal samples.
- Normal images are passed through VGG19 for depth features and through M-SE before generator reconstruction.
- During inference, normal samples should have small residuals between FEN and encoder features and between input and reconstruction.
- Abnormal samples should produce larger feature and content residuals because the generator is trained to reconstruct normal patterns.
- Pixel-level anomaly scores are binarized for localization.

### Multi-scale Self-Enhancement

- M-SE copies a randomly sampled region from the original image and pastes it at an arbitrary position in the same image.
- The copied region area is controlled as a proportion of original image area.
- Individual patches are constrained to no more than 1% of the original image, encouraging sensitivity to small anomalies.
- The paper selects area = 20% after ablation because it gives the best image-level AUC-ROC and IoU among the tested ratios.

### Objective And Anomaly Score

- Feature loss: L2 distance between the fifth VGG19 feature module and the corresponding encoder feature module.
- Content loss: L1 distance between the input image and generator reconstruction.
- Adversarial loss: GAN discriminator/generator objective.
- Total loss weights: feature loss 30, content loss 30, adversarial loss 1.
- Pixel anomaly score: weighted sum of feature-space residual and image-space residual.
- Anomaly-score weight: lambda = 0.6.
- Image-level anomaly score: maximum pixel-level anomaly score.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB industrial product surface images.
- Output target: image anomaly classification and pixel-level anomaly localization.
- Supervision: normal-only training; abnormal examples are used for testing/evaluation.
- Objective: learn normal feature/reconstruction behavior so abnormal regions produce high residual scores.

### Model And Training

- Framework: PyTorch.
- Input size: 256 x 256 RGB.
- Optimizer: Adam.
- Initial learning rate: 2e-4.
- Weight decay: 1e-5.
- Batch size: 16.
- Epochs: 200.
- Hardware: Intel i7-12700 and NVIDIA 3090 24GB GPU.
- Operating system: Windows 10.
- Pretraining: VGG19 pretrained on ImageNet.
- Random seeds: not reported.

### Data

- [[MVTec AD]]: 5,354 high-resolution color images across 15 industrial object/texture classes, with pixel-level anomaly labels.
- [[Bottle-Cap Dataset]]: more than 1,100 high-resolution color bottle-cap images from real production lines, with seven distinct real anomalies.
- Splits: exact train/test counts for this paper's runs are not reported.
- Labels: MVTec provides pixel-level anomaly labels; Bottle-Cap contains carefully labeled images according to the paper.
- License: paper is under CC BY-NC-ND 4.0; dataset licenses are not restated beyond use of public datasets.

### Evaluation

- Image-level AUC-ROC: image anomaly detection.
- Pixel-level AUC-ROC: pixel anomaly localization.
- IoU: overlap between predicted anomalous regions and ground-truth anomalous regions.
- Baselines include GeoTrans, GANomaly, ITAE, DAGAN, ST-m, DFR, SCGAN, AE-ssim, AnoGAN, VAE-grad, SPADE, PatchSVDD, and DFC.
- Statistical tests: not reported.

## Evidence

### Main Results

| Dataset | Metric | FEGAN | Best comparison described | Notes |
|---|---:|---:|---:|---|
| [[MVTec AD]] | Image-level AUC-ROC | 0.978 | SCGAN 0.951 average | FEGAN is 2.7 percentage points higher than SCGAN on average. |
| [[MVTec AD]] | Pixel-level AUC-ROC | 0.982 | SPADE 0.965 average | FEGAN is 1.7 percentage points higher than the stated state-of-the-art comparison. |
| [[MVTec AD]] | IoU | 0.399 | DFC 0.323 average | FEGAN is 0.076 higher than DFC on average. |
| [[Bottle-Cap Dataset]] | Image-level AUC-ROC | 0.956 | DFC 0.941 | Highest among the six methods in Table 4. |
| [[Bottle-Cap Dataset]] | Pixel-level AUC-ROC | 0.979 | DFC 0.971 | Highest among the six methods in Table 4. |
| [[Bottle-Cap Dataset]] | IoU | 0.231 | DFC 0.289 | FEGAN ranks second; 0.058 lower than DFC. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level anomaly detection | area under ROC curve over image anomaly scores | higher is better | yes | MVTec: 0.978; Bottle-Cap: 0.956 |
| [[AU-ROC]] | pixel-level anomaly localization | area under ROC curve over pixel anomaly scores | higher is better | yes | MVTec: 0.982; Bottle-Cap: 0.979 |
| [[IoU]] | anomaly segmentation overlap | intersection over union of predicted and true anomaly regions | higher is better | no | MVTec: 0.399; Bottle-Cap: 0.231 |

### Ablations

| M-SE area ratio | Image-level AUC-ROC | Pixel-level AUC-ROC | IoU |
|---:|---:|---:|---:|
| 1% | 0.921 | 0.943 | 0.347 |
| 5% | 0.944 | 0.965 | 0.366 |
| 10% | 0.965 | 0.985 | 0.381 |
| 20% | 0.978 | 0.982 | 0.399 |
| 30% | 0.967 | 0.979 | 0.389 |
| 50% | 0.942 | 0.959 | 0.352 |
| 70% | 0.901 | 0.925 | 0.328 |
| 100% | 0.873 | 0.891 | 0.286 |

| Enhancement strategy | Image-level AUC-ROC | Pixel-level AUC-ROC | IoU |
|---|---:|---:|---:|
| Cutout | 0.656 | 0.691 | 0.232 |
| Cutout (colour) | 0.762 | 0.747 | 0.279 |
| RIAD | 0.869 | 0.883 | 0.339 |
| SCADN | 0.871 | 0.892 | 0.362 |
| M-SE | 0.978 | 0.982 | 0.399 |

| Components / losses | Image-level AUC-ROC | Pixel-level AUC-ROC | IoU |
|---|---:|---:|---:|
| Generator + content loss | 0.623 | 0.637 | 0.215 |
| Generator + M-SE + content loss | 0.782 | 0.757 | 0.254 |
| Generator + discriminator + M-SE + content/adversarial loss | 0.804 | 0.815 | 0.328 |
| Generator + FEN + M-SE + content/feature loss | 0.927 | 0.953 | 0.374 |
| Full FEGAN with content/adversarial/feature loss | 0.978 | 0.982 | 0.399 |

## Dataset / Benchmark Details

- [[MVTec AD]] is used as a multi-category industrial anomaly benchmark with object and texture classes.
- [[Bottle-Cap Dataset]] is used as a focused single-product industrial anomaly dataset with real bottle-cap production defects.
- The paper evaluates both detection and localization, reporting image-level AUC-ROC, pixel-level AUC-ROC, and IoU.
- The Bottle-Cap localization limitation is attributed to low lighting, large anomaly-size changes, and complex anomaly shapes.

## Limitations

- FEGAN performs unevenly across categories, with weaker sensitivity to subtle anomaly in some classes such as capsule, screw, and carpet for image-level detection.
- Fine feature extraction is described as insufficient for categories such as bottles, capsules, and screws.
- The paper uses a uniform anomaly metric across categories even though anomaly definitions vary by image class.
- The authors report slow inference on devices with limited computing power and recommend high-performance GPU deployment.
- Code availability, random seeds, and exact dataset split counts are not reported.

## Reproducibility

- Code: not reported.
- Data: public [[MVTec AD]] and [[Bottle-Cap Dataset]].
- Hyperparameters: Adam, initial learning rate 2e-4, weight decay 1e-5, batch size 16, 200 epochs, loss weights 30/30/1, anomaly-score lambda 0.6.
- Random seeds: not reported.
- Environment: PyTorch on Windows 10.
- Hardware: Intel i7-12700 and NVIDIA 3090 24GB GPU.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[FEGAN]], [[GAN]], [[Feature extraction]]
- Datasets: [[MVTec AD]], [[Bottle-Cap Dataset]]
- Benchmarks: [[MVTec AD]], [[Bottle-Cap Dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[IoU]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Builds On

- [[GAN]]: FEGAN uses adversarial generator/discriminator training.
- [[Feature extraction]]: FEGAN's anomaly score relies on VGG19-derived deep feature residuals.

### Shares Dataset

- [[MVTec AD]]: used for image-level detection, pixel-level localization, and IoU evaluation.
- [[Bottle-Cap Dataset]]: used for detection and localization generalization evaluation.

### Shares Task

- [[Industrial anomaly detection]]: normal-only training detects anomalous industrial product surface images.
- [[Defect segmentation]]: pixel anomaly maps are binarized into segmentation masks.

### Shares Method

- [[FEGAN]]: introduced by this paper.
- [[GAN]]: the method uses an improved GAN for normal-image reconstruction.

### Shares Metric

- [[AU-ROC]]: used for image-level and pixel-level anomaly evaluation.
- [[IoU]]: used for anomaly segmentation overlap.

### Application / Domain

- [[Multi-industry anomaly detection]]: the method is evaluated on multi-category MVTec AD and the Bottle-Cap industrial inspection dataset.

### Follow-up Reading

- [[MVTec AD]]: standard multi-category benchmark used by the paper.
- [[Bottle-Cap Dataset]]: specialized bottle-cap benchmark used for generalization testing.

## Questions

- What are the exact inference latency and throughput values on the reported 3090 GPU and on lower-power deployment devices?
- Would category-specific anomaly score weights improve classes where FEGAN is less sensitive to fine defects?
- How much of the result depends on VGG19 ImageNet pretraining versus the GAN reconstruction objective?
