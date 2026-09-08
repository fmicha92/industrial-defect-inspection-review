---
title: "Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation"
aliases:
  - "Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation"
paper_key: "doi:10.1109/access.2021.3124525"
paper_type: research
year: 2021
venue: "IEEE Access"
authors:
  - "Seungdong Yoa"
  - "Seungjun Lee"
  - "Chiyoon Kim"
  - "Hyunwoo J. Kim"
status: processed
processed_at: 2026-05-23
topics:
  - "self-supervised anomaly detection"
  - "dynamic local augmentation"
  - "pixel-level anomaly localization"
tasks:
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Dynamic Local Augmentation]]"
  - "[[Self-supervised learning]]"
  - "[[Data augmentation]]"
  - "[[Monte Carlo dropout uncertainty scoring]]"
  - "[[Regression-error anomaly scoring]]"
model_family:
  - "[[ResNet-18]]"
architectures:
  - "[[ResNet-18]]"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "Pixel-wise localization AUROC on MVTec AD."
baselines:
  - "AESSIM"
  - "AEL2"
  - "VAE"
  - "AnoGAN"
  - "U-Student"
benchmarks:
  - "[[MVTec AD]]"
code: "not reported"
data: "[[MVTec AD]]"
doi: "10.1109/access.2021.3124525"
arxiv: "not reported"
url: "https://doi.org/10.1109/access.2021.3124525"
pdf: "paper-inbox/10_processed/Research/2021 - Yoa - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation.pdf"
related_papers:
  - "[[2021 - The MVTec Anomaly Detection Dataset]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Dynamic Local Augmentation]]"
  - "[[Self-supervised learning]]"
  - "[[Data augmentation]]"
  - "[[Monte Carlo dropout uncertainty scoring]]"
  - "[[Regression-error anomaly scoring]]"
related_datasets:
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
related_benchmarks:
  - "[[MVTec AD]]"
source_file: "paper-inbox/10_processed/Research/2021 - Yoa - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Yoa - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Yoa - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation.txt"
artifact_status: "paper reports no code release"
tags:
  - paper
---
# Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation

## Summary

The paper proposes a self-supervised framework for pixel-level anomaly detection on normal-only training images. It extends a SimSiam-style representation-learning setup with [[Dynamic Local Augmentation]], which creates locally altered pseudo-abnormal samples by weighting hard local transformations according to how strongly they change the selected region. At test time, the method scores pixels with feature-map regression error and Monte Carlo dropout uncertainty. On [[MVTec AD]], the paper reports competitive pixel-wise localization AUROC against reconstruction, generative, and teacher-student baselines, with especially large gains on wood and zipper.

## Paper Type

- Type: research.
- Why: The paper proposes a training method, two anomaly scoring functions, and an experimental evaluation for unsupervised image anomaly localization.

## Problem

- Task: [[Industrial anomaly detection]] with pixel-level anomaly localization.
- Setting: normal training images only; anomalies are absent during training and appear only at test time.
- Inputs: MVTec AD industrial object and texture images resized to 256 x 256 for experiments.
- Outputs: anomaly score maps for segmenting anomalous pixels.
- Motivation: reconstruction-based GAN and autoencoder methods can miss subtle defects because they focus on low-level reconstruction, while pixel-level anomaly localization needs dense representations that preserve spatial detail.
- Assumption: each MVTec AD category is trained and tested separately, so training samples within a category are treated as same-category positives.

## Contribution

- Proposes [[Dynamic Local Augmentation]], a category- and location-adaptive way to generate local pseudo-abnormal negative samples from normal images.
- Combines global SimSiam-style self-supervised learning, dense positive-pair representation learning, and a negative-pair objective between normal images and locally augmented images.
- Introduces two pixel-level scoring functions: regression error between test and average training feature maps, and uncertainty-map difference computed with Monte Carlo dropout.
- Reports that the method trained from scratch achieves the best average MVTec AD pixel-wise localization AUROC among the compared baselines in the paper.

## Method

- Backbone: [[ResNet-18]].
- Self-supervised base: a SimSiam-like architecture with a shared encoder, projection MLP, prediction MLP, negative cosine similarity, and stop-gradient operation.
- Global loss: maximizes cosine similarity for positive image pairs; because a category contains only normal samples, positive pairs can come from the same image or different images in the same mini-batch.
- Dense loss: uses positive pairs of dense feature maps from two views of the same image, following the dense contrastive-learning idea but without negative pairs for dense representation learning.
- Negative-pair loss: contrasts a normal image with its dynamically locally augmented counterpart.
- Dynamic local augmentations: rotation, ColorJitter, local permutation, and grayscale are applied to random local regions.
- Dynamic weighting: each local augmentation is weighted by the mean-squared error between the locally augmented image and the original image, normalized across the augmentation set. Larger changes receive stronger weights.
- Final training objective: combines global loss, dense loss, and negative-pair loss with reported coefficients `lambda1 = 1`, `lambda2 = 0.1`, and `lambda3 = 0.5`.

## Evidence

### Experimental Setup

- Dataset: [[MVTec AD]].
- Dataset structure: 5 texture categories and 10 object categories; normal images are used for training, and normal plus abnormal images are used for testing.
- Image preprocessing: input images are resized to 256 x 256.
- Evaluation target: pixel-wise anomaly localization.
- Metric: [[AU-ROC]] in percent.
- Baselines: AESSIM, AEL2, VAE, AnoGAN, and U-Student.
- Runs: the paper reports average AUROC over three independent runs with different random seeds.
- Training: batch size 200, SGD with momentum 0.9, weight decay `5e-4`, 200 epochs, base learning rate 0.02.
- Local augmentation region: random region size ranges from 50 to 128 pixels; height and width may differ.
- Score coefficients: `alpha1 = 1` for regression error and `alpha2 = 0.1` for uncertainty.
- Hyperparameter selection: the paper tunes `lambda2`, `lambda3`, `alpha1`, and `alpha2` using validation data made from normal samples plus pseudo-abnormal local augmentations.

### Main Results

- The paper states that its method has the best average pixel-wise AUROC across all MVTec AD categories among the compared baselines.
- Reported improvement over the second-best baseline: 12.66 percentage points for texture categories and 2.53 percentage points for object categories.
- Wood: the method reports 89.4% AUROC, 16.4 percentage points higher than the second-best method.
- Zipper: the method reports 95.5% AUROC, 7.5 percentage points higher than the second-best method.
- The average AUROCs of the compared baselines for wood and zipper are reported as 68.52% and 80.92%, respectively.
- Qualitative examples show predicted masks for capsule, hazelnut, carpet, leather, pill, cable, and toothbrush classes.

### Ablations

- Self-supervised learning with only global and dense losses performs poorly because the model never learns from abnormal or pseudo-abnormal examples.
- Static local augmentation underperforms dynamic local augmentation; the paper reports a drop from 93.04 to 82.92 AUROC when static augmentation generates ineffective pseudo-abnormal samples.
- Dynamic local augmentation improves over fixed local augmentation by 9.90 percentage points on average.
- Dense loss is reported as important, especially for object categories.
- Static versus dynamic augmentation gaps are reported as especially large for grid, tile, bottle, and metal nut, with an average gap of 25.4 percentage points across those categories.
- Texture categories show a larger average dynamic-versus-static augmentation gap than object categories: 14.02 versus 8.17 percentage points.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | Pixel-wise MVTec AD localization | Area under ROC curve, reported as percent | Higher is better | yes | Wood 89.4%; zipper 95.5%; dynamic local augmentation ablation 93.04 vs static local augmentation 82.92 |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB industrial inspection images from MVTec AD.
- Output target: anomaly score map for pixel-level segmentation.
- Supervision: unsupervised anomaly detection; training uses only normal images and pseudo-abnormal local augmentations.
- Objective: learn global and dense normal-image representations while pushing pseudo-abnormal local transformations away from normal representations.

### Model And Training

- Model family: convolutional self-supervised representation learning.
- Architecture: [[ResNet-18]] backbone with MLP heads for global representation and dynamic local augmentation, plus convolution heads for dense representation.
- Feature maps for scoring: last layers of ResNet stages 2, 3, and 4, denoted C2, C3, and C4.
- Dense feature maps: C3 features are used for the dense representation loss.
- Feature-map upsampling: C2, C3, and C4 difference maps are upsampled to 224 x 224 and averaged per pixel.
- Optimizer: SGD.
- Momentum: 0.9.
- Weight decay: `5e-4`.
- Epochs: 200.
- Batch size: 200.
- Base learning rate: 0.02.
- Seeds: three independent runs are reported, but seed values are not reported.
- Compute and hardware: not reported.

### Scoring

- Regression-error score: computes the squared difference between a test feature map and the average training feature map for each used ResNet stage, upsamples each difference map to 224 x 224, and averages across stages.
- Uncertainty score: applies MC dropout at test time, estimates per-pixel variance for each used stage, then compares the test variance map against the average training variance map.
- Final score: weighted sum of regression error and uncertainty, with reported weights `alpha1 = 1` and `alpha2 = 0.1`.

### Data

- Dataset: [[MVTec AD]].
- Categories: 5 texture categories and 10 object categories.
- Training data: only normal images.
- Test data: normal and abnormal images with pixel-level anomaly masks.
- Dataset size: source states more than 5000 high-resolution images.
- License: not reported.
- Leakage checks: not reported.

### Evaluation

- Protocol: train a model from scratch on MVTec AD normal images and evaluate pixel-wise localization AUROC on MVTec AD test images.
- Primary metric: [[AU-ROC]].
- Baselines: AESSIM, AEL2, VAE, AnoGAN, and U-Student.
- Statistical tests: not reported.
- Failure cases: the paper indicates local augmentation can be ineffective when the selected region and transformation do not create a meaningful pseudo-defect, motivating dynamic weighting.

## Dataset / Benchmark Details

- [[MVTec AD]]: public anomaly detection and localization benchmark with 15 categories.
- Category breakdown: 5 textures and 10 objects.
- Training split: normal images only.
- Test split: normal and abnormal images.
- Labels: pixel-level annotations for anomalous regions.
- Image count: more than 5000 high-resolution images.
- Preprocessing in this paper: resize to 256 x 256.

## Limitations

- Code availability is not reported.
- Compute and hardware are not reported.
- Hyperparameter tuning uses pseudo-abnormal validation samples rather than real anomaly validation labels, which may not reflect all real anomaly patterns.
- The paper identifies the quality of generated pseudo-abnormal samples as important; static or ineffective local augmentations can harm performance.
- Future work is needed for wide-scene anomaly detection with many objects in a single image or video.
- Future work is also needed on the shape, size, and variety of dynamic local augmentations.

## Reproducibility

- Code: not reported.
- Data: [[MVTec AD]].
- Hyperparameters: batch size, optimizer, momentum, weight decay, epochs, learning rate, local region size range, loss coefficients, and scoring coefficients are reported.
- Random seeds: three runs are reported, but seed values are not reported.
- Environment: not reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]]
- Methods: [[Dynamic Local Augmentation]], [[Self-supervised learning]], [[Data augmentation]], [[Monte Carlo dropout uncertainty scoring]], [[Regression-error anomaly scoring]]
- Models: [[ResNet-18]]
- Datasets: [[MVTec AD]]
- Benchmarks: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Builds On

- [[2021 - The MVTec Anomaly Detection Dataset]]: uses MVTec AD as the benchmark for pixel-level anomaly localization.

### Shares Dataset

- [[MVTec AD]]: evaluates normal-only training and pixel-wise anomaly localization on the dataset.

### Shares Method

- [[Dynamic Local Augmentation]]: central contribution for generating pseudo-abnormal local negative samples.
- [[Self-supervised learning]]: supplies the representation-learning framework.
- [[Data augmentation]]: local hard transformations create pseudo-abnormal training samples.
- [[Monte Carlo dropout uncertainty scoring]]: used to estimate per-pixel uncertainty at test time.
- [[Regression-error anomaly scoring]]: used to compare test feature maps against average normal training feature maps.

### Shares Task

- [[Industrial anomaly detection]]: detects and localizes anomalous pixels in industrial inspection images.

### Shares Metric

- [[AU-ROC]]: primary pixel-wise localization metric.

### Application / Domain

- [[Multi-industry anomaly detection]]: MVTec AD spans object and texture categories rather than one single manufacturing line.

### Follow-up Reading

- [[2021 - The MVTec Anomaly Detection Dataset]]: read for the benchmark construction and baseline evaluation protocol.

## Questions

- How sensitive is the method to the selected local augmentation set beyond rotation, ColorJitter, permutation, and grayscale?
- Would validation with real anomalies change the selected loss and scoring coefficients?
- How well does dynamic local augmentation scale to wide-scene video inspection, the future-work setting named by the paper?
