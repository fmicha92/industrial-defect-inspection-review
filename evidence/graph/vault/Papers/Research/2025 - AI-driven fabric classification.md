---
title: "AI-driven fabric classification: real-time implementation for sustainable textile practices in industry 5.0"
aliases:
  - "AI-driven fabric classification"
  - "PSRT50 fabric classification"
paper_key: "doi:10.1088/2053-1591/add98f"
paper_type: research
year: 2025
venue: "Materials Research Express"
authors:
  - "Noreen Akram"
  - "Rizwan Aslam Butt"
  - "Muhammad Amir Qureshi"
status: processed
processed_at: "2026-06-05"
topics:
  - "fabric classification"
  - "textile inspection"
  - "edge deployment"
tasks:
  - "[[Defect classification]]"
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "real-time textile quality control"
datasets:
  - "[[DME Fabric Defect Detection Dataset]]"
dataset_sizes:
  - "300 raw fabric samples; 3,000 augmented images for Dataset2"
splits:
  - "Dataset2: 2,700 training images and 300 test images"
modalities:
  - "RGB microscopy images"
methods:
  - "[[Particle Swarm Optimization]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Residual network]]"
architectures:
  - "[[PSRT50]]"
  - "[[ResNet50]]"
  - "[[Deep convolutional neural network]]"
  - "[[VGG-16]]"
  - "[[MobileNet]]"
losses:
  - "categorical cross-entropy"
optimizers:
  - "[[Stochastic gradient descent]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
baselines:
  - "CNN"
  - "DenseNet121"
  - "DenseNet201"
  - "[[VGG-16]]"
  - "[[ResNet50]]"
evaluation_protocol: "train/test evaluation on self-built and augmented fabric image datasets, with real-time deployment demo on Raspberry Pi 4"
hardware:
  - "NVIDIA GeForce 2016"
  - "Raspberry Pi 4"
  - "18MP Digital HDMI VGA Industrial Microscope Camera Model 2362#"
training_time: "35 min 29 s for the best PSRT50 case"
code: "not reported"
data: "[[DME Fabric Defect Detection Dataset]]"
doi: "10.1088/2053-1591/add98f"
url: "https://doi.org/10.1088/2053-1591/add98f"
related_concepts:
  - "[[Industry 5.0]]"
related_methods:
  - "[[Particle Swarm Optimization]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[DME Fabric Defect Detection Dataset]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Research/2025 - Akram - AI-driven fabric classification.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Akram - AI-driven fabric classification.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Akram - AI-driven fabric classification.txt"
artifact_status: "paper and dataset public; code not reported; trained weights not reported"
tags:
  - paper
---

# AI-driven fabric classification: real-time implementation for sustainable textile practices in industry 5.0

## Summary

- The paper proposes [[PSRT50]], a [[ResNet50]] model whose learning rate and momentum are tuned with [[Particle Swarm Optimization]] for textile fabric classification.
- The study documents the microscopy-image recording process behind the related public textile dataset, then trains and evaluates CNN, DenseNet, VGG16, ResNet50, and PSRT50 classifiers on the paper's experiment labels.
- The best reported PSRT50 configuration reaches 98.32% accuracy on the augmented three-class fabric dataset and is deployed for real-time inference on a Raspberry Pi 4 with a digital microscope camera.

## Paper Type

- Type: research.
- Why: the paper introduces a model optimization and deployment workflow, reports a custom dataset contribution, and evaluates classification performance against neural-network baselines.

## Problem

- Task: classify fabric images into weave-pattern categories.
- Setting: textile inspection with microscopy images and real-time edge deployment.
- Inputs: RGB fabric microscopy images, originally captured at 1920 x 1080 pixels for the larger dataset.
- Outputs: fabric class labels: plain, satin, or twill.
- Motivation: reduce time-consuming and error-prone manual fabric inspection while supporting Industry 5.0 quality-control practices.
- Assumptions: the real-time camera setup captures images close enough to the training distribution for fixed PSRT50 weights to classify new fabric samples.

## Contribution

- Claimed: a custom fabric-image dataset for training and assessing deep learning models in textile studies.
- Claimed: integration of [[Particle Swarm Optimization]] with [[ResNet50]] to tune learning rate and momentum.
- Shown: PSRT50 improves reported accuracy from 96% for ResNet50 to 98.32% in the best PSO case on the paper's augmented dataset.
- Shown: a pre-trained PSRT50 model can be loaded on Raspberry Pi 4 for real-time plain, satin, and twill classification.
- Inferred: the paper is strongest as evidence for image recording, augmentation, and PSRT50 evaluation; the current dataset description and defect-label taxonomy should come from the Mendeley host record.

## Method

- Core idea: start from ResNet50, freeze base model layers, use PSO to search learning rate and momentum, then retrain ResNet50 with the best hyperparameters.
- Architecture / algorithm: [[PSRT50]] combines [[ResNet50]] with particle updates guided by personal-best and global-best PSO positions.
- Objective / loss: categorical cross-entropy.
- Optimization: [[Stochastic gradient descent]] uses PSO-selected learning rate and momentum.
- Training data: self-built microscopy fabric images covering plain, satin, and twill fabric categories.
- Data pipeline: capture raw images, split into training and test sets, augment by rotation, zoom, flipping, and cropping, then resize/normalize for ResNet50 input.
- Augmentation / synthesis: geometric augmentation increases the dataset to 3,000 images.
- Inference: a real-time fabric image is captured with a digital microscope camera, preprocessed, passed through the loaded PSRT50 model, and classified into the highest-probability class.
- Complexity / deployment constraints: training occurs in Google Colab; inference is deployed on Raspberry Pi 4 to reduce edge-device computational load.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB microscopy images of fabric samples.
- Output target: three-class classification among plain, satin, and twill fabrics.
- Supervision: supervised classification.
- Objective: minimize categorical cross-entropy and maximize classification accuracy.

### Model And Training

- Model family: residual convolutional neural network.
- Architecture: [[ResNet50]] optimized by PSO, named [[PSRT50]].
- Parameters: not reported.
- Pretraining: ResNet50 is used as the base architecture; exact pretraining source is not reported.
- Fine-tuning: base model layers are frozen during PSO fitness evaluation; the paper does not fully specify which layers are later trainable.
- Losses: categorical cross-entropy.
- Optimizer: [[Stochastic gradient descent]] with learning rate and momentum selected by PSO.
- Hyperparameters: best case reports learning rate 0.0059587 and momentum 0.5401833 with swarm size 5, 5 iterations, and 10 epochs.
- Seeds: not reported.
- Training compute: experiments used Google Colab, TensorFlow 2.15.0, Python, and an NVIDIA GeForce 2016 GPU.

### Data

- Datasets: [[DME Fabric Defect Detection Dataset]] is the related public dataset record; use the Mendeley host record for the current dataset description and class labels.
- Data source: fabric samples imaged with digital microscope cameras.
- Dataset size: Dataset1(a) has 146 images; Dataset1(b) has 360 images; Dataset2 has 3,000 augmented images.
- Labels / annotations: the paper's experiment labels are plain, satin, and twill; the current host record describes dataset labels as Stain, Damage, Broken Thread, Holes, and Non-defective.
- Splits: Dataset2 uses 2,700 training images and 300 test images, with 900 train and 100 test images per class.
- Preprocessing: resizing, normalization, and reshaping for ResNet50 input.
- Augmentation: rotation, zoom, flipping, and cropping.
- Synthetic data: not applicable; the paper reports geometric augmentation, not generated synthetic images.
- Leakage checks: not reported.
- License: paper is CC BY 4.0; dataset host license is CC BY 4.0 in the dataset note.

### Evaluation

- Protocol: compare CNN, DenseNet121, DenseNet201, VGG16, ResNet50, and PSRT50 on the self-built datasets.
- Used performance metrics: accuracy, precision, recall, F1 score, and confusion matrix.
- Primary metric: [[Accuracy]].
- Metric definitions: accuracy is defined as correct predictions divided by total predictions, though the equation formatting in the extracted text appears reversed.
- Metric direction / units: higher is better, percentage.
- Baselines: CNN, DenseNet121, DenseNet201, VGG16, ResNet50.
- Benchmarks: not reported.
- Statistical tests: not reported.
- Failure cases: the paper notes a sudden accuracy drop in one Case III epoch and attributes it to optimizer behavior, but does not provide a broader failure-case analysis.

## Evidence

### Experimental Setup

- Datasets: Dataset1(a), Dataset1(b), and Dataset2 from the paper's self-built fabric image data.
- Splits: Dataset2 has 1,000 images per class after augmentation, split into 900 training and 100 test images per class.
- Baselines: CNN, DenseNet121, DenseNet201, VGG16, and ResNet50.
- Used performance metrics: accuracy, precision, recall, F1 score, and confusion matrices.
- Compute: Google Colab with TensorFlow 2.15.0 and Python.
- Hardware: NVIDIA GeForce 2016 for experiments; Raspberry Pi 4 and an 18MP digital microscope camera for real-time deployment.
- Training time: best PSRT50 case reports 35 min 29 s.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| CNN on Dataset1(a) | Fabric classification | Accuracy | higher | not applicable | 58% | 146 images, 10 epochs |
| CNN on Dataset1(b) | Fabric classification | Accuracy | higher | not applicable | 65% | 360 images, 10 epochs |
| DenseNet121 on Dataset2 | Fabric classification | Accuracy | higher | not applicable | 86% | 3,000 images, 10 epochs |
| DenseNet201 on Dataset2 | Fabric classification | Accuracy | higher | not applicable | 92% | 3,000 images, 10 epochs |
| VGG16 on Dataset2 | Fabric classification | Accuracy | higher | not applicable | 95.67% | 3,000 images, 10 epochs |
| ResNet50 on Dataset2 | Fabric classification | Accuracy | higher | not applicable | 96% | Chosen for PSO optimization |
| PSRT50, Case V | Fabric classification | Accuracy | higher | 96% ResNet50 | 98.32% | Swarm size 5, 5 iterations, 10 epochs |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | classification performance | percent correct | higher | yes | paper's main comparison metric |
| [[Precision]] | model comparison | not defined in extracted text | higher | no | listed as part of evaluation |
| [[Recall]] | model comparison | not defined in extracted text | higher | no | listed as part of evaluation |
| [[F1-score]] | model comparison | not defined in extracted text | higher | no | listed as part of evaluation |

### Ablations

- PSO swarm size and iteration count are varied from 1 to 5 while holding epochs at 10.
- Case I: swarm size 1, 1 iteration, learning rate 0.01, momentum 0.86212395, accuracy 96.29%.
- Case II: swarm size 2, 2 iterations, learning rate 0.00551363, momentum 0.56317808, accuracy 96.29%.
- Case III: swarm size 3, 3 iterations, learning rate 0.00305841, momentum 0.9, accuracy 96.29%.
- Case IV: swarm size 4, 4 iterations, learning rate 0.0001, momentum 0.70439088, accuracy 96.66%.
- Case V: swarm size 5, 5 iterations, learning rate 0.0059587, momentum 0.5401833, accuracy 98.32%.

## Dataset / Benchmark Details

- Source: self-built fabric samples captured with digital microscope cameras.
- Collection: 300 raw fabric samples, with 100 plain, 100 satin, and 100 twill samples.
- Annotation: class labels for fabric weave type.
- Size: 600 raw images are mentioned after capture under lighting conditions and distinct timings; augmentation produces 3,000 images.
- Splits: 90% training and 10% test for Dataset2.
- Modalities: RGB microscopy images; the Mendeley host record reports JPG format.
- License: paper is CC BY 4.0; dataset host is CC BY 4.0 in the related dataset note.
- Leakage risks: not reported; augmentation details do not state whether augmented variants from the same raw sample are kept out of both train and test.
- Bias / coverage: only plain, satin, and twill classes are evaluated; future work calls for broader texture, color, and environmental variation.
- Maintenance: not reported.
- Source precedence: use the Mendeley host record for the current [[DME Fabric Defect Detection Dataset]] description; use this paper for recording-process details and PSRT50 experiment context.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: future work should expand the dataset to more fabric textures, colors, and environmental conditions.
- Stated: edge deployment is proposed for real-time monitoring and predictive maintenance, but the paper does not report detailed latency, throughput, or memory use.
- Inferred: the classification experiment is narrow because it evaluates only three paper-reported classes and does not report defect localization or segmentation.
- Inferred: the paper does not describe leakage controls for augmented images derived from the same raw samples.
- Inferred: the dataset host has the more current public description, so benchmark comparisons should use the host's defect-class labels rather than treating the paper's experiment labels as final dataset metadata.

## Reproducibility

- Code: not reported.
- Data: related public dataset record is [[DME Fabric Defect Detection Dataset]]; the paper text supports the acquisition and experiment workflow, while the host record supplies the current dataset DOI, URL, and defect-label description.
- Hyperparameters: best PSRT50 case reports learning rate 0.0059587, momentum 0.5401833, swarm size 5, 5 iterations, and 10 epochs.
- Random seeds: not reported.
- Environment: TensorFlow 2.15.0, Python, Google Colab.
- Checkpoints / models: trained model weights are saved and transferred to Raspberry Pi, but a public checkpoint is not reported.
- Exact preprocessing: resizing, normalization, and reshaping are reported; target dimensions are not fully specified in the extracted text.
- Artifact status: paper and related dataset are public; code and trained model artifacts are not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Textile defect detection]]
- Methods: [[PSRT50]], [[ResNet50]], [[Particle Swarm Optimization]], [[Data augmentation]], [[Stochastic gradient descent]]
- Datasets: [[DME Fabric Defect Detection Dataset]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Shares Dataset

- [[DME Fabric Defect Detection Dataset]] is the related public textile dataset record; the paper supports the recording and experiment workflow, while the host record is authoritative for current dataset labels and description.

### Shares Task

- [[Defect classification]] is related through image-level textile quality classification and the host record's defect-class dataset description.
- [[Textile defect detection]] is related through the textile visual inspection domain and the associated public dataset record.

### Shares Method

- [[Particle Swarm Optimization]] tunes the ResNet50 learning rate and momentum.
- [[ResNet50]] is the base architecture optimized into [[PSRT50]].
- [[Data augmentation]] expands the captured fabric images with rotation, zoom, flipping, and cropping.
- [[Stochastic gradient descent]] trains the model using the selected learning rate and momentum.

### Shares Metric

- [[Accuracy]] is the primary reported metric.
- [[Precision]], [[Recall]], and [[F1-score]] are listed as evaluation metrics but their reported values are not extracted.

### Application / Domain

- [[Textile and fiber inspection]] is the application domain for the paper's fabric classification and real-time quality-control workflow.

### Follow-up Reading

- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] for a textile defect detection benchmark with defect categories.
- [[2022 - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods]] for broader textile defect detection methods and evaluation context.

## Questions

- How exactly do the paper's plain/satin/twill experiment labels map onto the Mendeley host record's Stain, Damage, Broken Thread, Holes, and Non-defective classes?
- Are augmented variants derived from the same raw fabric sample separated across train and test sets?
- What are the actual real-time latency, memory use, and frame-rate limits on Raspberry Pi 4?
