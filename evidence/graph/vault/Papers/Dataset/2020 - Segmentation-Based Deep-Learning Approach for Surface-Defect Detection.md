---
title: "Segmentation-Based Deep-Learning Approach for Surface-Defect Detection"
aliases:
  - "Segmentation-based deep-learning approach for surface-defect detection"
paper_key: "doi:10.1007/s10845-019-01476-x"
paper_type: dataset
year: 2020
venue: "Journal of Intelligent Manufacturing"
authors:
  - "Domen Tabernik"
  - "Samo Sela"
  - "Jure Skvarc"
  - "Danijel Skocaj"
status: processed
processed_at: 2026-06-05
topics:
  - "surface-defect detection"
  - "industrial visual inspection"
  - "small-sample defect learning"
tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Metal inspection]]"
application_area: "electrical commutator surface inspection"
datasets:
  - "[[KolektorSDD]]"
dataset_sizes:
  - "400 images"
  - "50 defective images"
  - "350 non-defective images"
splits:
  - "threefold cross-validation with images from the same physical product kept in the same fold"
modalities:
  - "grayscale surface images"
methods:
  - "[[Segmentation-decision network]]"
  - "[[Deep convolutional neural network]]"
model_family:
  - "[[Segmentation Models]]"
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[Segmentation-decision network]]"
  - "[[U-Net]]"
  - "[[DeepLabV3+]]"
losses:
  - "cross-entropy"
  - "mean squared error"
optimizers:
  - "[[Stochastic gradient descent]]"
training_regime: "segmentation network trained first, then frozen while the decision network is trained"
augmentation:
  - "random 90-degree rotations evaluated but not helpful"
synthetic_data: "not applicable"
metrics:
  - "[[Average precision]]"
  - "[[F-measure]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  - "Average precision is the area under the precision-recall curve and is used because the dataset is imbalanced."
  - "False positives and false negatives are counted at the threshold with the best F-measure."
baselines:
  - "Cognex ViDi Suite v2.1"
  - "[[DeepLabV3+]]"
  - "[[U-Net]]"
  - "segmentation-only logistic regression"
benchmarks:
  - "[[KolektorSDD]]"
evaluation_protocol: "threefold cross-validation"
parameters: "15.7 million for the proposed segmentation/decision network"
compute: "not reported"
hardware: "single NVIDIA TITAN X Pascal GPU for forward-pass timing"
training_time: "100 epochs, 6600 training steps per network"
inference_cost: "110 ms per full-resolution image and 33 ms per half-resolution image"
url: "https://doi.org/10.1007/s10845-019-01476-x"
pdf: "paper-inbox/10_processed/Dataset/2020 - Tabernik - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection.pdf"
code: "not reported"
data: "http://www.vicos.si/Downloads/KolektorSDD"
doi: "10.1007/s10845-019-01476-x"
related_papers:
  - "[[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial anomaly detection]]"
related_methods:
  - "[[Segmentation-decision network]]"
  - "[[Deep convolutional neural network]]"
  - "[[U-Net]]"
  - "[[DeepLabV3+]]"
related_datasets:
  - "[[KolektorSDD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[KolektorSDD]]"
concept_notes_created_or_updated:
  - "[[KolektorSDD]]"
  - "[[Segmentation-decision network]]"
  - "[[Metal inspection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
  - "[[Average precision]]"
source_file: "paper-inbox/10_processed/Dataset/2020 - Tabernik - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Tabernik - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Tabernik - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection.txt"
artifact_status: "public dataset reported; code not reported"
tags:
  - paper
---
# Segmentation-Based Deep-Learning Approach for Surface-Defect Detection

## Summary

- The paper introduces [[KolektorSDD]], a public surface-defect dataset for electrical commutator inspection, and proposes a two-stage [[Segmentation-decision network]] for detecting whether an image contains a visible defect.
- The dataset contains 400 grayscale 1408 x 512 images: 50 defect-positive images and 350 defect-negative images from 50 defective commutators, with pixel-wise masks for each image.
- The best reported model reaches 99.9% [[Average precision]] on [[KolektorSDD]], with zero false positives and one false negative at the best F-measure threshold.

## Paper Type

- Type: dataset
- Why: The paper both introduces the [[KolektorSDD]] benchmark and evaluates a new segmentation-based defect detector on it.

## Problem

- Task: binary defect/no-defect image classification supported by pixel-level defect segmentation.
- Setting: quality control for electrical commutator surfaces where cracks or microscopic fractions may be visible in high-resolution grayscale images.
- Inputs: grayscale surface images at 1408 x 512 resolution, with a half-resolution 704 x 256 setting also evaluated.
- Outputs: a segmentation map and an image-level anomaly probability score from 0 to 1.
- Motivation: industrial defect datasets with real defects and pixel-level annotation were scarce, while defective training samples are expensive.
- Assumptions: the quality-control problem can be framed as a segmentation task with pixel-wise annotations.

## Contribution

- Claimed: a two-stage segmentation and decision architecture for surface-defect detection that works with few defective samples.
- Claimed: [[KolektorSDD]] as a public benchmark dataset of real industrial surface defects.
- Shown: the proposed method outperforms Cognex ViDi Suite, [[DeepLabV3+]], and [[U-Net]] on [[KolektorSDD]] by [[Average precision]], false-positive count, false-negative count, low-sample robustness, and parameter count.
- Inferred: the method is best suited to defects that are visually localizable as surface masks; the authors explicitly limit it for quality-control problems that are not segmentation-like.

## Method

- Core idea: train a segmentation network to localize defects, then train a decision network on segmentation features and the segmentation output to predict image-level defect presence.
- Architecture / algorithm: the segmentation network has 11 convolutional layers and 3 max-pooling layers; the last segmentation feature volume is concatenated with the segmentation output and passed to the decision network.
- Objective / loss: segmentation uses cross-entropy or mean squared error; the decision network uses cross-entropy.
- Optimization: [[Stochastic gradient descent]] without momentum; learning rate 0.005 for MSE and 0.1 for cross-entropy; batch size 1.
- Training data: each fold has 33 defective training images when all training samples are used.
- Data pipeline: the sampler alternates defective and non-defective images, with defective samples on even iterations and non-defective samples on odd iterations.
- Augmentation / synthesis: random 90-degree rotations were evaluated and did not improve the best configuration.
- Inference: the model returns both a defect segmentation mask and a probability score for image-level defect presence.
- Complexity / deployment constraints: the proposed model has 15.7 million parameters; full-resolution inference takes 110 ms per image, and half-resolution inference takes 33 ms per image on a single NVIDIA TITAN X Pascal GPU.

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale industrial surface images.
- Output target: image-level defective/non-defective classification plus pixel-level defect mask.
- Supervision: pixel-wise masks for segmentation and image-level labels derived from defect presence.
- Objective: maximize defect detection performance under strong class imbalance and limited positive examples.

### Model And Training

- Model family: [[Deep convolutional neural network]], [[Segmentation Models]].
- Architecture: [[Segmentation-decision network]] with a segmentation stage and a decision stage.
- Parameters: 15.7 million for the proposed model; 31.1 million for [[U-Net]]; 41.1 million for [[DeepLabV3+]].
- Pretraining: none for the proposed model; [[DeepLabV3+]] uses pretraining.
- Fine-tuning: not reported.
- Losses: cross-entropy and MSE were compared for segmentation; cross-entropy trains the decision network.
- Optimizer: [[Stochastic gradient descent]] without momentum.
- Hyperparameters: 100 epochs, 6600 steps, batch size 1, learning rate 0.1 for cross-entropy.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[KolektorSDD]].
- Data source: images of defected electrical commutators provided and annotated by Kolektor Group d.o.o. and Kolektor Orodjarna d.o.o.
- Dataset size: 400 images from 50 defective commutators; 50 images contain visible defects and 350 images do not.
- Labels / annotations: pixel-wise defect masks; additional annotation variants are generated by dilating the masks with 5, 9, 13, and 17 pixel kernels.
- Splits: threefold cross-validation; images from the same physical product stay in the same fold.
- Preprocessing: image resizing to half resolution was evaluated; otherwise not reported.
- Augmentation: random 90-degree rotations were evaluated.
- Synthetic data: not applicable.
- Leakage checks: product-level grouping across folds prevents images from the same physical commutator appearing in both train and test.
- License: not reported.

### Evaluation

- Protocol: threefold cross-validation on [[KolektorSDD]].
- Used performance metrics: [[Average precision]], [[F-measure]], false positives, false negatives, and false positives at 100% [[Recall]].
- Primary metric: [[Average precision]].
- Metric definitions: [[Average precision]] is area under the precision-recall curve; false positives and false negatives are counted at the threshold with the best [[F-measure]].
- Metric direction / units: AP, precision, recall, and F-measure are higher better; false positives, false negatives, manual verifications, latency, and parameter count are lower better.
- Baselines: Cognex ViDi Suite v2.1, [[DeepLabV3+]], [[U-Net]], and segmentation-only logistic regression.
- Benchmarks: [[KolektorSDD]].
- Statistical tests: not reported.
- Failure cases: one false-negative defect remains in the best model; related methods miss that difficult example as well.

## Evidence

### Experimental Setup

- Datasets: [[KolektorSDD]] with 400 images and pixel-wise masks.
- Splits: threefold cross-validation with product-level grouping.
- Baselines: Cognex ViDi Suite, [[DeepLabV3+]], [[U-Net]], and segmentation-only logistic regression.
- Used performance metrics: [[Average precision]], false positives, false negatives, [[F-measure]], and false positives at 100% [[Recall]].
- Compute: not reported.
- Hardware: single NVIDIA TITAN X Pascal GPU for forward-pass timing.
- Training time: 100 epochs per network.
- Inference cost: 110 ms per full-resolution image; 33 ms per half-resolution image.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best proposed model | [[KolektorSDD]] defect classification | [[Average precision]] | higher | 99.0% Cognex ViDi Suite | 99.9% | Dilate=5 masks, full resolution, cross-entropy, no rotations |
| Best proposed model | [[KolektorSDD]] defect classification | False positives / false negatives | lower | 0 FP / 5 FN Cognex ViDi Suite | 0 FP / 1 FN | Counted at the best F-measure threshold |
| Proposed model at zero-miss rate | [[KolektorSDD]] industrial inspection | Manual verifications | lower | 7 Cognex, 68 DeepLabV3+, 108 U-Net | 3 | Three false positives out of 400 images at 100% recall |
| Low positive-sample setting | [[KolektorSDD]] defect classification | [[Average precision]] | higher | not reported | about 96% | Uses only 5 defective training samples |
| Parameter comparison | [[KolektorSDD]] defect classification | Learnable parameters | lower | 31.1M U-Net, 41.1M DeepLabV3+ | 15.7M | Proposed model is smaller than both standard segmentation baselines |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Average precision]] | Imbalanced image-level defect detection | area under the precision-recall curve | higher | yes | Chosen over AUC because the data are imbalanced |
| [[F-measure]] | Selecting the reporting threshold | harmonic combination of precision and recall | higher | no | FP/FN counted at the threshold with best F-measure |
| False positives | Manual verification burden | number of non-defective images predicted as defective | lower | no | Used to evaluate 100% recall operation |
| False negatives | Missed defects | number of defective images predicted as non-defective | lower | no | Critical for industrial inspection |

### Ablations

- Cross-entropy outperforms MSE by about 7 percentage points AP on average.
- Full-resolution training generally outperforms half-resolution training, although cross-entropy is less sensitive to resolution.
- The decision network improves over segmentation-only logistic regression; the segmentation-only setup reaches 98.2% AP with zero false positives and four false negatives, while the best full model reaches 99.9% AP with one false negative.
- Coarse annotations remain effective: large bounding boxes reach 98.7% AP with 3 misclassifications, and coarse rotated boxes reach 99.7% AP with 2 misclassifications.

## Dataset / Benchmark Details

- Source: images of defected electrical commutators provided and annotated by Kolektor Group d.o.o. and Kolektor Orodjarna d.o.o.
- Collection: each commutator surface is captured as 8 non-overlapping grayscale images in a controlled environment.
- Annotation: every image has a pixel-wise defect mask; dilated annotation variants with 5, 9, 13, and 17 pixel kernels are used in experiments.
- Size: 400 images, with 50 positive images and 350 negative images.
- Splits: threefold cross-validation with images from the same physical product kept in one fold.
- Modalities: grayscale high-resolution surface images at 1408 x 512.
- License: not reported.
- Leakage risks: the product-level split reduces leakage from surfaces of the same commutator crossing fold boundaries.
- Bias / coverage: one specific industrial product and one defect family, microscopic fractions or cracks on electrical commutator surfaces.
- Maintenance: not reported.

## Limitations

- Stated: the architecture is limited to quality-control tasks that can be framed as segmentation with pixel-wise annotation.
- Stated: complex 3D quality-control problems involving broken or missing parts may require detection methods such as Mask R-CNN.
- Stated: the evaluation demonstrates one crack-detection task on one surface type; additional real-world datasets are needed to evaluate broader generalization.
- Inferred: the dataset is highly valuable for controlled metal inspection but does not by itself cover multiple industries, materials, defect types, or acquisition conditions.

## Reproducibility

- Code: not reported.
- Data: [[KolektorSDD]] is reported as publicly available at http://www.vicos.si/Downloads/KolektorSDD.
- Hyperparameters: 100 epochs, 6600 steps, batch size 1, learning rate 0.1 for cross-entropy and 0.005 for MSE.
- Random seeds: not reported.
- Environment: TensorFlow.
- Checkpoints / models: not reported.
- Exact preprocessing: half-resolution resizing evaluated; other preprocessing not reported.
- Artifact status: public dataset reported; code and trained models not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Defect segmentation]]
- Methods: [[Segmentation-decision network]], [[Deep convolutional neural network]], [[U-Net]], [[DeepLabV3+]]
- Optimizers: [[Stochastic gradient descent]]
- Datasets: [[KolektorSDD]]
- Benchmarks: [[KolektorSDD]]
- Domains: [[Metal inspection]]
- Metrics: [[Average precision]], [[F-measure]], [[Precision]], [[Recall]]
- Concepts: [[Surface defect detection]], [[Industrial anomaly detection]]
- Dataset-domain links: [[KolektorSDD]] is a public [[Metal inspection]] dataset.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] | Follow-up reading / Shares dataset | The later mixed-supervision paper evaluates weak, mixed, and full supervision on [[KolektorSDD]]. |

### Backlinks Updated

- [[KolektorSDD]]
- [[Metal inspection]]
- [[Defect classification]]
- [[Defect segmentation]]
- [[Surface defect detection]]
- [[Segmentation-decision network]]
- [[Deep convolutional neural network]]
- [[U-Net]]
- [[DeepLabV3+]]
- [[Stochastic gradient descent]]
- [[Average precision]]
- [[F-measure]]
- [[Precision]]
- [[Recall]]

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[KolektorSDD]] | Updated | Dataset size, collection, labels, public access, and introducing paper from the paper text |
| [[Segmentation-decision network]] | Created | Architecture and training description from the paper text |
| [[Metal inspection]] | Updated | Domain association from the commutator surface inspection setting |
| [[Defect classification]] | Updated | Image-level defect/no-defect task from the paper text |
| [[Defect segmentation]] | Updated | Pixel-wise mask task from the paper text |

## Questions

- The paper does not report the dataset license; verify the current dataset host page before assuming redistribution rights.
- The code and trained model availability are not reported.
- The method's generalization beyond commutator crack or fraction defects remains to be tested on additional real-world surfaces.
