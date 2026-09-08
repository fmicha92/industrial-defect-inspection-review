---
title: "Enhancing Glass Defect Detection with Diffusion Models: Addressing Imbalanced Datasets in Manufacturing Quality Control"
aliases:
  - "Enhancing Glass Defect Detection with Diffusion Models"
  - "arXiv:2505.03134"
paper_key: "sha256:d6aff6091e2ef30611645407bc73b0be9ea5c6cb3f0848f6c23d2bbcf960990d"
paper_type: research
year: 2025
venue: "Computer and Decision Making"
authors:
  - "Sajjad Rezvani Boroujeni"
  - "Hossein Abedi"
  - "Tom Bush"
status: processed
processed_at: 2026-06-03
topics:
  - "glass defect detection"
  - "diffusion data augmentation"
  - "class imbalance"
  - "manufacturing quality control"
tasks:
  - "[[Glass container defect detection]]"
  - "[[Defect classification]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[U-Net]]"
  - "[[ResNet50]]"
  - "[[EfficientNet]]"
  - "[[MobileNet]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[AU-ROC]]"
primary_metric: "[[Recall]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + TN + FP + FN)."
  - "Precision: TP / (TP + FP)."
  - "Recall: TP / (TP + FN)."
  - "F1-score: harmonic mean of precision and recall."
  - "ROC AUC: area under the receiver operating characteristic curve."
baselines:
  - "ResNet50V2 trained on real data only"
  - "EfficientNetB0 trained on real data only"
  - "MobileNetV2 trained on real data only"
benchmarks:
  - "[[MVTec AD]] bottle subset"
code: "not reported"
data: "MVTec AD reported under CC BY-NC-SA 4.0; paper uses the glass bottle category subset."
doi: "10.59543/comdem.v2i.14391"
arxiv: "2505.03134"
url: "https://doi.org/10.59543/comdem.v2i.14391"
pdf: "paper-inbox/10_processed/Research/2025 - Boroujeni - Enhancing Glass Defect Detection with Diffusion Models.pdf"
related_papers:
  - "[[2021 - The MVTec Anomaly Detection Dataset]]"
  - "[[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]"
  - "[[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]]"
  - "[[2025 - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures]]"
related_concepts:
  - "[[Class imbalance]]"
  - "[[Industrial visual inspection]]"
  - "[[Synthetic data generation]]"
related_methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
  - "[[Data augmentation]]"
  - "[[ResNet50]]"
  - "[[EfficientNet]]"
  - "[[MobileNet]]"
related_datasets:
  - "[[MVTec AD]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Glass container defect detection]]"
  - "[[Defect classification]]"
  - "[[Industrial anomaly detection]]"
related_benchmarks:
  - "[[MVTec AD]] bottle subset"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Boroujeni - Enhancing Glass Defect Detection with Diffusion Models.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Boroujeni - Enhancing Glass Defect Detection with Diffusion Models.txt"
source_file: "paper-inbox/10_processed/Research/2025 - Boroujeni - Enhancing Glass Defect Detection with Diffusion Models.pdf"
artifact_status: "code not reported; data is public through MVTec AD license terms reported by the paper"
tags:
  - paper
---

# Enhancing Glass Defect Detection with Diffusion Models

## Summary

The paper evaluates whether [[Diffusion models|DDPM]]-generated defective glass bottle images can reduce class imbalance for glass container defect classification. It trains a U-Net-based DDPM on the defective class from the [[MVTec AD]] bottle subset, generates 60 synthetic defective samples, and compares ResNet50V2, EfficientNetB0, and MobileNetV2 classifiers trained on the original versus augmented datasets. The augmented training setup improves defect recall for all three CNNs while maintaining 1.00 precision on the validation set.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a machine-learning augmentation pipeline for industrial glass defect classification, with controlled baseline and augmented-data experiments.

## Problem

- Task: [[Glass container defect detection]] as binary defective versus non-defective classification.
- Setting: [[Glass inspection]] and manufacturing quality control for glass bottle images.
- Inputs: RGB glass bottle images resized to 128 x 128 pixels.
- Outputs: binary non-defective / defective predictions.
- Motivation: defective glass products are rare, so class imbalance makes CNN classifiers favor the majority non-defective class and miss defects.
- Assumptions: synthetic defective images can add minority-class variation without creating false-positive confusion.

## Contribution

- Claimed: Demonstrates DDPM-based learned generative augmentation for industrial glass defect detection.
- Claimed: Compares three transfer-learning CNN architectures, ResNet50V2, EfficientNetB0, and MobileNetV2, before and after DDPM augmentation.
- Shown: Adding 60 synthetic defective images improves recall and F1-score across all three CNNs, with ResNet50V2 accuracy increasing from 0.78 to 0.93.

## Method

- Core idea: train a [[Diffusion models|DDPM]] only on real defective bottle images, generate additional defective samples, then use those synthetic defects to rebalance classifier training.
- Architecture / algorithm: U-Net-based diffusion model using `UNet2DModel`, `DDPMScheduler`, and `DDPMPipeline`; classifiers are ResNet50V2, EfficientNetB0, and MobileNetV2 with ImageNet-pretrained backbones.
- Objective / loss: DDPM trains by predicting sampled noise with MSE loss; classifiers use binary cross-entropy.
- Optimization: DDPM uses AdamW with learning rate 1e-4 for 1,300 epochs. Classifiers use Adam with learning rate reported as `1e4` in the source text; this may be a typographic error, but the note preserves the reported value.
- Training data: defective bottle images from [[MVTec AD]] for DDPM training; original and DDPM-augmented bottle subsets for classifier training.
- Data pipeline: images resized to 128 x 128 pixels, converted to tensors, and normalized with mean and standard deviation 0.5 for DDPM training.
- Augmentation / synthesis: 60 DDPM-generated defective glass bottle images are added to the 63 real defective images.
- Inference: CNN classifiers predict non-defective versus defective glass bottle images.
- Complexity / deployment constraints: MobileNetV2 is discussed as attractive for resource-constrained deployment; exact latency is not reported.

## Evidence

### Experimental Setup

- Dataset: [[MVTec AD]] bottle category subset.
- Original class distribution: 209 non-defective images and 63 defective images.
- Augmented class distribution: 209 non-defective images and 123 defective images, with 63 real defective plus 60 DDPM-generated defective images.
- Imbalance shift: defective class representation increases from 23.2% to 37.0%; imbalance ratio changes from about 3:1 to 1.7:1.
- Standard classifier augmentations: random horizontal and vertical flips, random rotation +/-20%, random zoom +/-20%, and random contrast adjustment +/-20%.
- Baselines: the same CNN architectures trained on the original real-only dataset.
- Used performance metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], and [[AU-ROC]].
- Threshold: classification threshold set to 0.4.
- Compute: DDPM trained on a CUDA-enabled GPU.
- Hardware: exact GPU model not reported.
- Training time: not reported.

### Main Results

| Model | Training data | Accuracy | Precision | Recall | F1-score | ROC AUC |
|---|---|---:|---:|---:|---:|---:|
| ResNet50V2 | RealData | 0.78 | 0.53 | 0.80 | 0.64 | 0.899 |
| ResNet50V2 | AugmentedData | 0.93 | 1.00 | 0.84 | 0.91 | 0.973 |
| EfficientNetB0 | RealData | 0.8395 | 1.00 | 0.35 | 0.52 | 0.9672 |
| EfficientNetB0 | AugmentedData | 0.8485 | 1.00 | 0.65 | 0.79 | 0.9801 |
| MobileNetV2 | RealData | 0.9012 | 1.00 | 0.60 | 0.75 | 0.9508 |
| MobileNetV2 | AugmentedData | 0.8586 | 1.00 | 0.6744 | 0.8056 | 0.9805 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Recall]] | missed-defect reduction | TP / (TP + FN) | higher | yes | emphasized because missed defects matter in manufacturing quality control |
| [[Precision]] | false-alarm control | TP / (TP + FP) | higher | no | augmented runs maintain 1.00 precision for all three CNNs |
| [[F1-score]] | precision-recall balance | harmonic mean of precision and recall | higher | no | improves for all three CNNs |
| [[Accuracy]] | overall classification correctness | (TP + TN) / total | higher | no | improves for ResNet50V2 and EfficientNetB0, decreases for MobileNetV2 |
| [[AU-ROC]] | discrimination across thresholds | area under ROC curve | higher | no | improves for all three CNNs |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB images of glass bottles.
- Output target: binary defect classification.
- Supervision: supervised classifier training with non-defective and defective labels; DDPM trained on defective-class images.
- Objective: improve minority-class defect detection under class imbalance.

### Model And Training

- Model family: [[Diffusion models]] for synthetic data generation and [[Deep convolutional neural network|CNNs]] for classification.
- DDPM architecture: U-Net with 128 x 128 sample size and 3 input/output channels.
- DDPM scheduler: 14,000 training timesteps, linear beta schedule from 0.0001 to 0.02.
- DDPM optimizer: AdamW, learning rate 1e-4.
- DDPM epochs: 1,300.
- Classifier backbones: ImageNet-pretrained ResNet50V2, EfficientNetB0, and MobileNetV2.
- Classifier loss: binary cross-entropy.
- Classifier batch size: 32.
- Classifier maximum epochs: 5.
- Early stopping: patience 5, monitoring validation loss.
- Learning-rate schedule: ReduceLROnPlateau with factor 0.2 and patience 3.
- Class weighting: paper reports higher weighting for defective samples using `Ntotal / (NDefective x 2.1)` and non-defective weighting using `Ntotal / (NNonDefective x 1.2)`.
- Seeds: not reported.

### Data

- Dataset: [[MVTec AD]], bottle category subset.
- Data source: MVTec Anomaly Detection Dataset.
- Dataset size used: 272 images total.
- Labels / annotations: binary non-defective and defective labels; pixel masks from MVTec AD are not used in the reported classifier setup.
- Splits: exact train/validation split counts are not reported, though validation confusion matrices are shown.
- License: CC BY-NC-SA 4.0 is reported for MVTec AD.
- Preprocessing: resize to 128 x 128 pixels; architecture-specific preprocessing for classifiers.
- Synthetic data: 60 generated defective images.
- Leakage checks: not reported.

### Evaluation

- Protocol: train each CNN on real-only data, train the same architecture on augmented data, then compare binary classification metrics.
- Used performance metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], and [[AU-ROC]].
- Primary metric: [[Recall]] for missed-defect reduction.
- Baselines: real-only ResNet50V2, EfficientNetB0, and MobileNetV2.
- Benchmarks: [[MVTec AD]] bottle subset.
- Statistical tests: not reported.
- Failure cases: MobileNetV2 accuracy decreases under augmentation despite improved recall, F1-score, and AU-ROC; the paper attributes caution to changed class distributions.

## Dataset / Benchmark Details

- Dataset source: [[MVTec AD]].
- Category used: bottle / glass bottle images.
- Collection: described as real-world glass bottle images from an operational production line.
- Size used by the paper: 209 non-defective and 63 defective images.
- Defects: source text names cracks, breaks, discoloration, structural irregularities, and contamination near the bottle base.
- Availability: public through MVTec AD under the license reported above.
- Task difference from standard MVTec use: the paper uses a supervised binary classification framing, not the normal-only anomaly localization protocol commonly associated with MVTec AD.

## Limitations

- Stated: binary classification does not distinguish specific defect types.
- Stated: synthetic image realism and diversity could be improved with better DDPM architectures or conditioning.
- Stated: evaluation is on a held-out validation set, not a live production deployment.
- Stated: explainability is not addressed.
- Stated: generalization to other manufacturing domains remains future work.
- Inferred: the small 272-image dataset and generated-sample evaluation leave open whether the DDPM learned robust defect variation or overfit narrow bottle-defect appearances.

## Reproducibility

- Code: not reported.
- Data: [[MVTec AD]] is public; the exact subset and split are not fully specified.
- Hyperparameters: DDPM scheduler, optimizer, epochs, classifier augmentations, classifier batch size, and early stopping are reported.
- Random seeds: not reported.
- Environment: PyTorch and CUDA-enabled GPU are reported for DDPM training; exact environment and GPU model are not reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Glass container defect detection]], [[Defect classification]], [[Industrial anomaly detection]]
- Methods: [[Diffusion models]], [[Learned generative synthesis]], [[Data augmentation]]
- Datasets: [[MVTec AD]]
- Domains: [[Glass inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[AU-ROC]]
- Models: [[ResNet50]], [[EfficientNet]], [[MobileNet]], [[U-Net]]

### Builds On

- [[2021 - The MVTec Anomaly Detection Dataset]]: uses the MVTec AD bottle subset as the real-data source.
- [[2020 - Denoising Diffusion Probabilistic Models]]: uses the DDPM modeling family for synthetic defective-image generation.

### Shares Dataset

- [[MVTec AD]]: evaluates a supervised glass bottle defect-classification setup using the bottle category subset.

### Shares Method

- [[Diffusion models]]: uses a U-Net-based DDPM to generate synthetic defective samples.
- [[Learned generative synthesis]]: generates model-learned defective bottle images rather than procedural defects.
- [[Data augmentation]]: adds generated defective images to rebalance the training set.

### Shares Task

- [[Glass container defect detection]]: the paper classifies defective versus non-defective glass bottle images.
- [[Defect classification]]: the evaluation target is binary defect classification.

### Contrasts With

- [[2024 - Defect Detection in Automotive Glass Based on Modified YOLOv5]]: both target glass inspection, but this paper uses diffusion-generated training samples for bottle defect classification while the YOLOv5 paper targets automotive glass detection with a lightweight detector.
- [[2024 - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model]]: both use diffusion in defect inspection, but DiffDD is a diffusion-based detection framework across surface-defect datasets, while this paper uses diffusion as a synthetic-data augmenter for CNN classifiers.

## Questions

- Does the reported classifier split keep synthetic images out of validation/test data?
- How well do DDPM-generated defects generalize to defect types beyond the 63 real defective bottle images?
- Would conditioning the generator by defect type improve multi-class glass defect classification?
- How would the method compare against classical oversampling, GAN augmentation, or cost-sensitive learning under the same split?
