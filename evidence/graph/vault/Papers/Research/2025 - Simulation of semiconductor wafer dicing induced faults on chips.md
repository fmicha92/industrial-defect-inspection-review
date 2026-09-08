---
title: "Simulation of semiconductor wafer dicing induced faults on chips and their application as augmentation method for a deep learning based visual inspection system"
aliases:
  - "Simulation of semiconductor wafer dicing induced faults on chips"
paper_key: "doi:10.1007/s10845-024-02559-0"
paper_type: research
year: 2025
venue: "Journal of Intelligent Manufacturing"
authors:
  - "Michael Friedrich"
  - "Tobias Schlosser"
  - "Danny Kowerko"
status: processed
processed_at: 2026-06-17
topics:
  - "semiconductor wafer dicing faults"
  - "procedural synthetic data"
  - "visual inspection"
  - "data augmentation"
tasks:
  - "[[Semiconductor wafer dicing fault classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[Semiconductor visual inspection dataset]]"
methods:
  - "[[Spline-based wafer dicing fault synthesis]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[Domain randomization]]"
  - "[[Data augmentation]]"
model_family:
  - "[[ResNet152V2]]"
architectures:
  - "[[ResNet152V2]]"
  - "18 evaluated Keras deep-learning classifiers"
metrics:
  - "[[F1-score]]"
  - "[[Recall]]"
  - "[[Specificity]]"
  - "[[Relative improvement]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Macro-average F1-score: main classification metric, reported as percent and averaged over five runs; higher is better."
  - "Relative improvement factor I_O,C = (1 - F1_O) / (1 - F1_C), comparing original-data and composite-data F1 scores; higher indicates more error reduction."
  - "TPR/Recall: true positive rate for faulty chips; higher is better."
  - "TNR/Specificity: true negative rate for flawless chips; higher is better."
baselines:
  - "Original wafer data"
  - "O-LOOCV with original wafer data"
  - "Simple conventional augmenter"
  - "Complex conventional augmenter"
benchmarks:
  - "[[Semiconductor visual inspection dataset]]"
code: "Hexnet reported available: https://github.com/TSchlosser13/Hexnet"
data: "Data availability reported as not applicable; original wafer data availability not reported."
doi: "10.1007/s10845-024-02559-0"
url: "https://doi.org/10.1007/s10845-024-02559-0"
pdf: "paper-inbox/10_processed/Research/2025 - Friedrich - Simulation of semiconductor wafer dicing induced faults on chips and their application as augmentation method for a deep learnin....pdf"
related_papers:
  - "[[2022 - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks]]"
  - "[[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]"
  - "[[2017 - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Synthetic data generation]]"
  - "[[Domain randomization]]"
related_methods:
  - "[[Spline-based wafer dicing fault synthesis]]"
  - "[[Procedural and simulation-based synthesis]]"
  - "[[Domain randomization]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[Semiconductor visual inspection dataset]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Semiconductor wafer dicing fault classification]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[Semiconductor visual inspection dataset]]"
source_file: "paper-inbox/10_processed/Research/2025 - Friedrich - Simulation of semiconductor wafer dicing induced faults on chips and their application as augmentation method for a deep learnin....pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Friedrich - Simulation of semiconductor wafer dicing induced faults on chips and their application as augmentation method for a deep learnin....md"
extracted_text: "paper-inbox/90_processing/text/2025 - Friedrich - Simulation of semiconductor wafer dicing induced faults on chips and their application as augmentation method for a deep learnin....txt"
artifact_status: "code available; data availability not applicable"
tags:
  - paper
---

# Simulation of Semiconductor Wafer Dicing Induced Faults on Chips

## Summary

The paper builds a procedural synthesis system for semiconductor wafer dicing faults and evaluates whether synthetic chip imagery improves deep-learning visual inspection. It uses wafer and dicing-path templates to generate labeled flawless and faulty chip and dicing-street images, then trains classifiers on original data versus composite data that supplements original imagery with synthetic samples. The main evidence is that composite training improves macro-average F1-score over original-data baselines, with up to 3.98x relative improvement in wafer-type baseline experiments and up to 5.99x in synthetic-composite leave-one-out cross-validation.

## Paper Type

- Type: research.
- Why: The paper proposes a synthesis pipeline, creates synthetic wafer/chip datasets, evaluates many classifiers and augmentation baselines, and reports quantitative performance and runtime results.

## Problem

- Task: [[Semiconductor wafer dicing fault classification]].
- Setting: semiconductor wafer separation with thermal laser cleaving, where dicing-street deviations can reduce chip quality.
- Inputs: high-resolution wafer/chip imagery, chip templates, and measured faulty dicing paths.
- Outputs: flawless/faulty chip labels and classifier predictions for visual inspection.
- Motivation: dicing faults are rare, small in pixel extent, and expensive to annotate; the resulting data are sparse and imbalanced.
- Assumption: synthetic wafer imagery can improve classification without changing the classifier architecture when the synthesis preserves task-relevant dicing-street geometry.

## Contribution

- Claimed: A domain-specific wafer synthesis pipeline simulates dicing-induced chip faults using chip templates and spline-interpolated dicing path deviations.
- Claimed: Composite datasets can supplement original wafer imagery for classifier training while testing remains on original wafer data.
- Shown: ResNet152V2 baseline experiments improve from 93.80 +/- 0.36% F1 on all original wafer data to 95.14 +/- 0.47% F1 on all composite wafer data.
- Shown: SC-LOOCV improves mean F1-score from 51.70 +/- 19.13% to 75.01 +/- 18.34% over O-LOOCV, with a mean relative improvement factor of 2.83 +/- 2.03.

## Method

- Synthesis input: digitized defect point sets and chip templates; optional texture mappings for wafer, chip, and street surfaces.
- Defect approximation: faulty dicing paths are fitted from measured real-world defect paths using B-spline interpolation with degree k = 3.
- Synthesis pipeline: template mapping, dicing-path map generation, dicing simulation with morphological/masking operations, dicing-tape stretching, wafer border generation, label assignment, and output cropping.
- Labeling rule: chips adjacent to at least one faulty dicing street are labeled faulty; otherwise they are labeled flawless.
- Classifier framework: Hexnet with Keras and TensorFlow.
- Main classifier: [[ResNet152V2]], selected for comparability with earlier semiconductor visual inspection work and stable standard deviations.
- Training setup: Glorot initialization, Adam optimizer, learning rate 0.001, beta values 0.9 and 0.999, batch size 32, 50 epochs, five training runs per result, randomized 80/20 train/test split for baseline experiments.

## ML / DL Extraction

### Data

- Original data source: wafer imagery from earlier Beuth et al. and Schlosser et al. semiconductor visual inspection studies.
- Wafer types: five wafer types with different integrated circuit structures, illumination, noise, texture, and chip image resolutions from 224 x 224 to 912 x 908 pixels.
- Raw original class counts: 5,963 flawless chips and 1,026 faulty chips.
- Oversampled original class counts: 6,438 flawless chips and 6,438 faulty chips.
- Original baseline experiment size: 12,876 chips, with 10,292 train and 2,584 test samples.
- Synthetic generation inputs: 245 chip templates and 78 faulty dicing paths containing 2,274 measurement points.
- Generated synthetic set before oversampling: 23 generated wafers and 27,144 generated chips, with 16,794 flawless and 10,350 faulty chips.
- Generated synthetic set after oversampling: 33,768 generated chips.
- Composite experiment size: 46,644 chips, with 44,060 train and 2,584 original test samples.
- Fault classes: chipping, undersize, and border are treated as faulty; nose and oversize are included in the flawless class because the faulty class is defined around reduced chip geometry.
- Availability: data availability is reported as not applicable; public release of original wafer data is not reported.

### Evaluation

- Baseline experiments: train on original data or composite data; test only on original data.
- Comprehensive model comparison: 18 Keras classifiers evaluated on original and composite data.
- Wafer-type experiments: five wafer-type subsets evaluated with [[ResNet152V2]].
- Conventional augmentation comparison: simple and complex image augmenters compared against composite wafer data using ResNet152V2.
- O-LOOCV: leave-one-wafer-type-out cross-validation using only original wafer data.
- SC-LOOCV: leave-one-wafer-type-out cross-validation where the held-out wafer type is supplemented with synthetic samples in the training set, while testing remains on original data.
- Primary metric: macro-average [[F1-score]], averaged over five runs.
- Secondary metrics: [[Recall]]/TPR, [[Specificity]]/TNR, and [[Relative improvement]].

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| All-wafer baseline with ResNet152V2 | Original vs composite wafer data | Macro F1-score | higher | 93.80 +/- 0.36% | 95.14 +/- 0.47% | Table 5; relative improvement factor 1.28. |
| Wafer type 1 baseline | Original vs composite wafer data | Macro F1-score | higher | 84.18 +/- 5.92% | 92.99 +/- 0.65% | Table 5; relative improvement factor 2.26. |
| Wafer type 3 baseline | Original vs composite wafer data | Macro F1-score | higher | 84.94 +/- 25.80% | 96.22 +/- 1.81% | Table 5; relative improvement factor 3.98. |
| Wafer type 4 baseline | Original vs composite wafer data | Macro F1-score | higher | 49.38 +/- 22.43% | 79.98 +/- 6.06% | Table 5; relative improvement factor 2.53. |
| Mean wafer-type baseline | Original vs composite wafer data | Macro F1-score | higher | 81.04 +/- 14.87% | 88.95 +/- 7.96% | Table 5; mean relative improvement 1.99 +/- 1.08. |
| Mean baseline TPR | Original vs composite wafer data | TPR / recall | higher | 77.30 +/- 34.59% | 87.37 +/- 16.56% | Source narrative after Table 5; relative improvement 1.80. |
| Mean baseline TNR | Original vs composite wafer data | TNR / specificity | higher | 89.57 +/- 10.52% | 90.43 +/- 6.09% | Source narrative after Table 5; relative improvement 1.28. |
| Mean LOOCV | O-LOOCV vs SC-LOOCV | Macro F1-score | higher | 51.70 +/- 19.13% | 75.01 +/- 18.34% | Table 5; mean relative improvement 2.83 +/- 2.03. |
| Wafer type 3 LOOCV | O-LOOCV vs SC-LOOCV | Macro F1-score | higher | 37.69 +/- 6.45% | 89.60 +/- 1.94% | Table 5; relative improvement factor 5.99. |
| Conventional augmentation comparison | ResNet152V2 | Macro F1-score | higher | best conventional augmenter: 93.65 +/- 0.13% | composite data: 95.64 +/- 0.23% | Table 6; original no augmentation is 94.22 +/- 0.45%. |

### Model Comparison

Table 4 reports that many architectures improve when trained on composite data. Examples include DenseNet169 from 94.66 +/- 0.21% to 96.28 +/- 0.44%, ResNet152V2 from 93.80 +/- 0.36% to 95.14 +/- 0.47%, and Xception from 94.24 +/- 0.51% to 95.47 +/- 0.43%. NASNetLarge and NASNetMobile have very large improvement factors because they perform poorly on original data and much better on composite data.

### Runtime

- Hardware: Intel Core i9-9900K CPU, NVIDIA TITAN RTX with 24 GB VRAM, and 128 GB RAM.
- Deployment target discussed by prior work: 50 ms per image sample.
- All analyzed models have testing time below 5 ms per sample.
- ResNet152V2 inference time: 2.83 ms per chip.
- Estimated wafer processing time with ResNet152V2: 0.88 s for wafer type 4 and 16.53 s for wafer type 5.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[F1-score]] | chip-level flawless/faulty classification | macro-average F1-score in percent, averaged over five training runs | higher | yes | selected as the main performance and error metric after balancing via oversampling |
| [[Relative improvement]] | original-data versus composite-data comparison | `I_O,C = (1 - F1_O) / (1 - F1_C)` | higher | no | measures relative reduction in F1 error when synthetic composite training data are used |
| [[Recall]] | faulty-chip detection | true positive rate / sensitivity | higher | no | baseline mean TPR improves from 77.30 +/- 34.59% to 87.37 +/- 16.56% |
| [[Specificity]] | flawless-chip recognition | true negative rate / specificity | higher | no | baseline mean TNR changes from 89.57 +/- 10.52% to 90.43 +/- 6.09% |

## Dataset / Benchmark Details

- Dataset identity: [[Semiconductor visual inspection dataset]].
- Domain: [[Semiconductor and electronics]].
- Modalities: high-resolution wafer/chip imagery and derived chip/street crops.
- Labels: flawless and faulty chip classes; dicing-street deviations define fault status.
- Defect path inputs: 78 faulty dicing paths with 2,274 measurement points.
- Synthetic labels: generated automatically from dicing-path geometry and chip adjacency to faulty streets.
- Leakage control: baseline and SC-LOOCV experiments test only on original wafer data.

## Limitations

- Stated: the synthesis system is domain-specific to wafer dicing faults.
- Stated: preserving plausible neighbor relationships between chips and streets has not been fully explored.
- Stated: optical components such as camera and lighting parameters require future application-specific examination.
- Stated: future work should examine newer image classification and generation methods, including vision transformers, GANs, and diffusion models.
- Inferred: wafer types 2 and 5 do not benefit consistently; wafer type 5 decreases in both baseline and SC-LOOCV settings.

## Reproducibility

- Code: Hexnet is reported available at https://github.com/TSchlosser13/Hexnet.
- Data: not publicly specified; data availability says not applicable.
- Software: Python 3.7, Keras 2.3.1, TensorFlow 2.1, NumPy, OpenCV, and SciPy.
- Hardware: Intel Core i9-9900K, TITAN RTX 24 GB VRAM, 128 GB RAM.
- Training hyperparameters: Glorot initialization, Adam learning rate 0.001, beta values 0.9 and 0.999, batch size 32, 50 epochs.
- Repetitions: five training runs per reported mean and standard deviation.

## Connections

### Graph Hubs

- Tasks: [[Semiconductor wafer dicing fault classification]]
- Datasets: [[Semiconductor visual inspection dataset]]
- Domains: [[Semiconductor and electronics]]
- Methods: [[Spline-based wafer dicing fault synthesis]], [[Procedural and simulation-based synthesis]], [[Domain randomization]], [[Data augmentation]]
- Model: [[ResNet152V2]]
- Metrics: [[F1-score]], [[Recall]], [[Specificity]], [[Relative improvement]]

### Builds On

- [[2022 - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks]]: provides the earlier visual inspection pipeline context and comparable ResNet152V2-based evaluation setup.

### Shares Method

- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]: both use procedural synthetic data for defect detection, but this paper simulates full wafer/chip/dicing-street imagery and labels from wafer geometry.
- [[2017 - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World]]: the paper frames synthetic-to-real classifier transfer through domain randomization.

### Contrasts With

- [[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]]: both address semiconductor class imbalance with synthetic data, but this paper uses geometry-driven wafer image synthesis rather than GAN-generated wafer maps.
- [[2024 - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification]]: both improve wafer-related classification with augmentation, but this paper targets chip-level dicing faults rather than wafer-map failure-pattern classes.

## Questions

- Are the original wafer imagery and defect measurement templates available under any restricted-access agreement, despite the paper's "not applicable" data availability statement?
- How sensitive is the synthesis quality to the 78 measured dicing paths and the selected B-spline degree?
- Would a learned generator improve realism without losing chip/street adjacency constraints?
