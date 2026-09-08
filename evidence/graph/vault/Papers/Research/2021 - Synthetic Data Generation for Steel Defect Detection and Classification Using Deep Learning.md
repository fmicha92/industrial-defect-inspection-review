---
title: "Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning"
aliases:
  - "Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning"
paper_key: "sha256:9b7bdc5bc7142edfb4c9aef06d2508b05a4af423f38fa101878ba7fbe3c3a560"
paper_type: research
year: 2021
venue: "Symmetry"
authors:
  - "Aleksei Boikov"
  - "Vladimir Payor"
  - "Roman Savelev"
  - "Alexandr Kolesnikov"
status: processed
processed_at: 2026-05-23
topics:
  - "procedural defect synthesis"
  - "steel defect detection"
  - "synthetic training data"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Synthetic steel defect dataset]]"
  - "[[Severstal Steel Defect Dataset]]"
dataset_sizes:
  - "6000 synthetic defect images, 1500 per defect class"
  - "7095 Severstal samples used for real-data comparison"
methods:
  - "[[Procedural steel defect synthesis]]"
  - "[[Procedural generation]]"
  - "[[U-Net]]"
  - "[[Xception]]"
model_family:
  - "[[U-Net]]"
  - "[[Xception]]"
architectures:
  - "[[U-Net]]"
  - "[[Xception]]"
metrics:
  - "[[Dice score]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Dice score]]"
metric_definitions:
  - "Precision = TP / (TP + FP)"
  - "Recall = TP / (TP + FN)"
  - "Dice = 2 * |X intersect Y| / (|X| + |Y|)"
baselines:
  - "Same U-Net and Xception architectures trained on the real Severstal dataset"
benchmarks:
  - "[[Severstal Steel Defect Dataset]]"
code: "not reported"
data: "not applicable per source data availability statement"
doi: "10.3390/sym13071176"
arxiv: "not reported"
url: "https://doi.org/10.3390/sym13071176"
pdf: "paper-inbox/10_processed/Research/2021 - Boikov - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Procedural steel defect synthesis]]"
  - "[[Procedural generation]]"
  - "[[U-Net]]"
  - "[[Xception]]"
related_datasets:
  - "[[Synthetic steel defect dataset]]"
  - "[[Severstal Steel Defect Dataset]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[Severstal Steel Defect Dataset]]"
source_file: "paper-inbox/10_processed/Research/2021 - Boikov - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Boikov - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Boikov - Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning.txt"
artifact_status: "data not applicable per source"
tags:
  - paper
---
# Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning

## Summary

The paper tests whether procedurally generated steel-surface defect images can train deep neural networks for segmentation and classification when real production data are hard to collect and annotate. It generates 6000 synthetic steel defect images in Blender, with masks produced automatically alongside photorealistic renders, then trains [[U-Net]] for segmentation and [[Xception]] for defect classification. The trained models are evaluated on real images from the [[Severstal Steel Defect Dataset]]. Synthetic training reaches validation Dice 0.63 for U-Net and validation precision/recall 0.81/0.89 for Xception; when the same models are trained on real Severstal data, the reported Dice is 0.56 and precision/recall are 0.87/0.91.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a synthetic-data generation methodology for steel surface-defect segmentation and classification.

## Problem

- Task: [[Surface defect detection]], [[Defect segmentation]], and [[Defect classification]].
- Setting: steel workpiece and rolled-steel inspection where real labeled data are expensive, slow to collect, and difficult to annotate.
- Inputs: rendered steel-surface images for training; real Severstal steel defect images for validation and comparison.
- Outputs: segmentation masks from U-Net and defect-class predictions from Xception.
- Motivation: industrial automation teams often lack enough representative production defect data, and manual markup requires specialized competence.
- Assumption: procedural rendering can generate enough defect shape and texture variation to train useful segmentation and classification models.

## Contribution

- Presents a Blender-based procedural generation pipeline for steel slab surface defects and masks.
- Generates a balanced synthetic dataset with 6000 defect images across four defect classes.
- Trains two neural-network types on synthetic data: [[U-Net]] for semantic segmentation and [[Xception]] for classification.
- Evaluates synthetic-trained models on real Severstal steel defect data and compares them with the same architectures trained on real Severstal data.

## Method

- Generation tool: Blender 3 with built-in shader tools and Blender API automation.
- Scene: a parallelepiped slab model with shader material, camera mounted vertically above the slab, and lighting placed slightly above the camera to mimic machine-vision camera illumination.
- Rendering process: set a 3D scene, procedurally generate surface texture defects, render the image, and render the corresponding mask.
- Defect generation: shader programs transform original noise textures; separate shaders are written for each defect type.
- Defect variety: detorsion and noise parameters adjust generated defect shape variation.
- Example defect construction: crack generation starts from a spherical gradient resembling an ellipse, then deforms UV coordinates, symmetry, and boundaries; chipping textures are created from transformed Perlin noise.
- Dataset balancing: the generation process controls class distribution, producing 1500 images per defect class.
- Model sequence: U-Net first segments steel defects; Xception classifies defect types on image regions previously recognized by U-Net.

## Evidence

### Experimental Setup

- Synthetic dataset: [[Synthetic steel defect dataset]] with 6000 images and four defect classes.
- Synthetic class balance: 1500 generated images per defect class.
- Real validation/comparison dataset: [[Severstal Steel Defect Dataset]], reported as 7095 samples with four defect classes.
- Real split for comparison: 80% training and 20% test.
- Segmentation model: [[U-Net]], trained for 30 epochs.
- Classification model: [[Xception]], trained for 15 epochs.
- Framework: Keras with Python.
- Synthetic validation: models trained on synthetic data and tested on real data.
- Real-data comparison: same U-Net and Xception settings trained on real Severstal data.

### Main Results

- U-Net trained on synthetic data reaches Dice 0.815 on the synthetic training sample and Dice 0.632 on real validation images.
- Xception trained on synthetic data is reported to classify training and validation samples with high precision; validation recall does not exceed 0.81 in the graph discussion, indicating many false positives.
- Table 1 reports real-trained versus synthetic-trained model metrics:
  - U-Net Dice: 0.56 when trained on real data, 0.63 when trained on synthetic data.
  - Xception precision: 0.87 when trained on real data, 0.81 when trained on synthetic data.
  - Xception recall: 0.91 when trained on real data, 0.89 when trained on synthetic data.
- The paper concludes that synthetic data can train neural networks for segmentation and classification but that classification quality is lower than segmentation because artificial defect images are not realistic enough.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Dice score]] | U-Net segmentation mask overlap | `2 * |X intersect Y| / (|X| + |Y|)` | Higher is better | yes | Synthetic-trained U-Net: 0.815 training, 0.632 real validation; Table 1 real-trained 0.56 vs synthetic-trained 0.63 |
| [[Precision]] | Xception defect classification | `TP / (TP + FP)` | Higher is better | no | Table 1 real-trained 0.87 vs synthetic-trained 0.81 |
| [[Recall]] | Xception defect classification | `TP / (TP + FN)` | Higher is better | no | Table 1 real-trained 0.91 vs synthetic-trained 0.89; graph discussion says validation recall does not exceed 0.81 |

## ML / DL Extraction

### Task Formulation

- Input modality: steel surface images.
- Segmentation target: pixel masks for defect regions.
- Classification target: defect class for regions recognized by U-Net.
- Supervision: synthetic images and masks generated automatically; real Severstal data used for validation and comparison.
- Objective: test whether synthetic renders can substitute for or augment difficult-to-collect real steel-defect data.

### Model And Training

- Segmentation architecture: [[U-Net]], with contraction and expansion paths for context and localization.
- Classification architecture: [[Xception]], a compact Inception-style classifier using depthwise separable convolutions.
- U-Net epochs: 30.
- Xception epochs: 15.
- Framework: Keras.
- Programming language: Python.
- Optimizer, learning rate, batch size, hardware, and seeds: not reported.

### Data

- Synthetic generation software: Blender 3.
- Synthetic object: steel slab surface represented by a parallelepiped.
- Synthetic labels: black-and-white masks rendered in parallel; defect pixels are white.
- Synthetic defect types: source text says the work was limited to basic defect types including cracks, bubbles, foreign inclusions, and surface irregularities.
- Real dataset: [[Severstal Steel Defect Dataset]].
- Real dataset size in this paper: 7095 samples and four defect classes.
- Real split: 80% training, 20% test.
- Data availability statement: not applicable.
- License: the paper is open access under CC BY 4.0; dataset license is not reported.

### Evaluation

- Protocol: train U-Net and Xception on synthetic data, evaluate on real Severstal data, then compare with the same architectures trained on real Severstal data.
- Metrics: Dice coefficient for segmentation; precision and recall for classification.
- Baselines: same architectures trained on real data.
- Statistical tests: not reported.
- Failure cases: synthetic defect images are not realistic enough compared with real defects, reducing recognition and classification performance.

## Dataset / Benchmark Details

- [[Synthetic steel defect dataset]]: 6000 generated defect images, four classes, 1500 images per class, with automatically generated masks.
- [[Severstal Steel Defect Dataset]]: real steel defect dataset used as validation sample and real-data comparison set; the paper reports 7095 samples and four defect classes.
- Real defect examples named in the paper: scratch, surface crack, network cracks, and caverns.
- Operational context: steel rolling production and vision-based quality control systems.

## Limitations

- A new shader is needed for each defect type, so the generation method requires defect-specific modeling.
- Synthetic images are not realistic enough compared with real counterparts, which introduces distortion into model behavior.
- Classification quality is lower than segmentation quality.
- The paper suggests combining synthetic and real data or increasing generated-image realism to compensate for the realism gap.
- Optimizer, batch size, hardware, and random seeds are not reported.
- The data availability statement says not applicable, so no reusable generated dataset URL is reported.

## Reproducibility

- Code: not reported.
- Data: data availability statement says not applicable.
- Hyperparameters: U-Net 30 epochs and Xception 15 epochs are reported; other hyperparameters are not reported.
- Random seeds: not reported.
- Environment: Keras and Python are reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect segmentation]], [[Defect classification]]
- Methods: [[Procedural steel defect synthesis]], [[Procedural generation]], [[U-Net]], [[Xception]]
- Datasets: [[Synthetic steel defect dataset]], [[Severstal Steel Defect Dataset]]
- Benchmarks: [[Severstal Steel Defect Dataset]]
- Domains: [[Metal inspection]]
- Metrics: [[Dice score]], [[Precision]], [[Recall]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[Synthetic steel defect dataset]]: generated and used for model training.
- [[Severstal Steel Defect Dataset]]: used for real-data validation and comparison.

### Shares Method

- [[Procedural steel defect synthesis]]: central synthetic-data generation method.
- [[Procedural generation]]: the paper uses shader-based procedural texture generation in Blender.
- [[U-Net]]: used for semantic segmentation of defect regions.
- [[Xception]]: used for classification of recognized defect regions.

### Shares Task

- [[Surface defect detection]]: detects surface defects on steel workpieces.
- [[Defect segmentation]]: U-Net predicts defect masks.
- [[Defect classification]]: Xception classifies defect types.

### Shares Metric

- [[Dice score]]: segmentation metric.
- [[Precision]]: classification metric.
- [[Recall]]: classification metric.

### Application / Domain

- [[Metal inspection]]: target setting is steel slab and rolled-steel surface inspection.

### Follow-up Reading

- not reported.

## Questions

- Which optimizer, learning rate, batch size, and hardware settings were used for U-Net and Xception?
- How were the four synthetic defect classes mapped to the four Severstal real defect classes?
- How much does combining real and synthetic data improve over either source alone in this steel setting?
