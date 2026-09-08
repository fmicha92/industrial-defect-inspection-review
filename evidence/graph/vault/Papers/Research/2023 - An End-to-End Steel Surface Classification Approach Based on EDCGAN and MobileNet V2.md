---
title: "An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2"
aliases:
  - "EDCGAN and MobileNet V2 steel surface classification"
paper_key: "sha256:3a5172d27b26501db26ec13b5d2237aa96bfcaf1b79783c109dfffe6634266b7"
paper_type: research
year: 2023
venue: "Sensors"
authors:
  - "Ge Jin"
  - "Yanghe Liu"
  - "Peiliang Qin"
  - "Rongjing Hong"
  - "Tingting Xu"
  - "Guoyu Lu"
status: processed
processed_at: 2026-05-31
topics:
  - "steel surface defect classification"
  - "GAN data augmentation"
  - "MobileNet V2"
tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-CLS]]"
dataset_sizes:
  - "NEU-CLS: 1800 images, six classes, 300 images per class, 200x200 pixels"
splits:
  - "NEU-CLS: 7:3 train/test split; 1260 original training images and 540 test images"
methods:
  - "[[EDCGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[MobileNet]]"
  - "[[VGG19]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Overall accuracy: class-wise reported percentage for six NEU-CLS defect classes; higher is better."
  - "AP: paper defines AP as (Precision + Recall) / 2; higher is better."
baselines:
  - "fully supervised learning"
  - "VGG-16"
  - "ResNet-19"
benchmarks:
  - "[[NEU-CLS]]"
evaluation_protocol: "Train EDCGAN on NEU-CLS training images, generate 8000 fake defect samples, mix original and generated samples at different proportions, then classify with MobileNet V2 and comparison classifiers."
parameters: "not reported"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "MobileNet V2 is selected partly for simpler deployment; exact inference cost not reported."
url: "https://doi.org/10.3390/s23041953"
pdf: "paper-inbox/10_processed/Research/2023 - Jin - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2.pdf"
code: "not reported"
data: "NEU-CLS URL reported as http://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm"
doi: "10.3390/s23041953"
arxiv: "not applicable"
related_papers:
  - "[[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]]"
  - "[[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[EDCGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-CLS]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
related_benchmarks:
  - "[[NEU-CLS]]"
concept_notes_created_or_updated:
  - "[[EDCGAN]]"
source_file: "paper-inbox/10_processed/Research/2023 - Jin - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Jin - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Jin - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2.txt"
artifact_status: "article is open access under CC BY 4.0; code not reported"
tags:
  - paper
---
# An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2

## Summary

The paper proposes a steel surface defect classification workflow that uses [[EDCGAN]] to synthesize additional NEU-CLS-like defect samples and [[MobileNet]] V2 for final classification. The paper trains EDCGAN on the original NEU-CLS training split, generates 8000 fake defect images, mixes generated and original samples in several proportions, and reports that adding generated data improves classification accuracy, with the best MobileNet V2 average accuracy reaching 99.11% when the training mix contains 20% original images and 80% generated images.

## Paper Type

- Type: research.
- Why: The paper proposes a GAN-based data augmentation method and evaluates downstream steel surface defect classification.

## Problem

- Task: [[Defect classification]] on steel surface images.
- Setting: [[Metal inspection]] for hot-rolled steel plates.
- Inputs: NEU-CLS steel surface defect images.
- Outputs: six defect-class predictions.
- Motivation: industrial steel surface datasets have too few labeled samples for robust supervised deep learning.
- Assumptions: generated defect samples can be mixed with original samples to improve classifier training, but fully synthetic training data cannot fully replace original examples.

## Contribution

- Claimed: EDCGAN generates useful steel surface defect samples, and MobileNet V2 provides an efficient classifier for industrial scenarios.
- Shown: adding generated samples improves overall classification accuracy, with the highest MobileNet V2 average accuracy at 99.11% when 80% of the mixed training set is generated.
- Inferred: generated samples are most useful as augmentation rather than full replacement because accuracy drops when the training set contains only generated samples.

## Method

- Core idea: train a GAN variant on NEU-CLS steel defect images, generate synthetic samples, and mix them with real samples for MobileNet V2 classification.
- Architecture / algorithm: [[EDCGAN]] uses ELU in the discriminative layer and DropOut to improve training; [[MobileNet]] V2 is used as the classification backbone.
- Objective / loss: standard GAN minimax objective is described; exact EDCGAN loss beyond architectural changes is not reported.
- Optimization: EDCGAN uses MBGD with exponential decay parameters beta1 = 0.8 and beta2 = 0.99, learning rate 0.0001, and 800 epochs. MobileNet V2 uses SGD with learning rate 0.001, 300 initial epochs, and 600 retraining epochs.
- Training data: 1260 original NEU-CLS training images.
- Data pipeline: resize/generated image samples to 224x224, generate 8000 fake defect samples, mix real and generated samples, then train and evaluate classifiers.
- Augmentation / synthesis: [[EDCGAN]] generates fake steel defect images for six NEU-CLS defect classes.
- Inference: MobileNet V2 classifies test images into NEU-CLS defect categories.
- Complexity / deployment constraints: MobileNet V2 is described as simpler and more suitable for industrial deployment than heavier classifiers; exact latency is not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: 2D steel surface images.
- Output target: NEU-CLS defect class.
- Supervision: supervised classification with generated-data augmentation.
- Objective: maximize classification accuracy while compensating for limited original training samples.

### Model And Training

- Model family: [[GAN]] and convolutional image classification.
- Architecture: [[EDCGAN]] generator/discriminator; [[MobileNet]] V2 classifier.
- Parameters: exact parameter counts are not reported.
- Pretraining: not reported.
- Fine-tuning: retraining step of 600 epochs is reported for MobileNet V2.
- Losses: GAN minimax loss; classifier loss not explicitly reported.
- Optimizer: MBGD for EDCGAN; SGD for MobileNet V2.
- Hyperparameters: mini-batch size 128; EDCGAN learning rate 0.0001; MobileNet V2 learning rate 0.001; EDCGAN 800 epochs; classifier 300 + 600 epochs.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[NEU-CLS]].
- Data source: Northeastern University URL reported in the paper.
- Dataset size: 1800 images, 300 each for scratches, rolled-in scale, patches, pitted surface, inclusion, and crazing.
- Labels / annotations: image-level defect class labels.
- Splits: 7:3 train/test split; 1260 original training samples and 540 test samples.
- Preprocessing: generated images are 224x224; exact preprocessing for original images is not fully reported.
- Augmentation: 8000 fake defect images generated by EDCGAN.
- Synthetic data: generated samples are mixed with original samples at 100%, 75%, 50%, 30%, 20%, and 0% original-sample proportions.
- Leakage checks: not reported.
- License: paper is CC BY 4.0; dataset license is not reported.

### Evaluation

- Protocol: train classifiers on different real/generated mixtures and evaluate on the held-out 540-image NEU-CLS test set.
- Used performance metrics: [[Accuracy]], [[Precision]], [[Recall]]; AP is defined as the average of precision and recall.
- Primary metric: [[Accuracy]].
- Metric definitions: TP, FP, and FN definitions are given for precision and recall; AP is defined as `(Precision + Recall) / 2`.
- Metric direction / units: higher percentages are better.
- Baselines: fully supervised learning, VGG-16, ResNet-19, and MobileNet V2 under different generated-data ratios.
- Benchmarks: [[NEU-CLS]].
- Statistical tests: not reported.
- Failure cases: generated patches and pitted-surface images have visible gaps from real images; generated pitted-surface samples are described as significantly different from original images.

## Evidence

### Experimental Setup

- Datasets: [[NEU-CLS]].
- Splits: 1260 training images and 540 test images.
- Baselines: fully supervised learning, VGG-16, ResNet-19.
- Used performance metrics: [[Accuracy]], [[Precision]], [[Recall]].
- Compute: PyTorch 1.13.0; hardware not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| MobileNet V2 with only original samples | [[NEU-CLS]] classification | Average [[Accuracy]] | higher | not applicable | 95.74% | 100% original training set. |
| MobileNet V2 with 20% original / 80% generated samples | [[NEU-CLS]] classification | Average [[Accuracy]] | higher | 95.74% | 99.11% | Best MobileNet V2 result in Table 3. |
| MobileNet V2 with only generated samples | [[NEU-CLS]] classification | Average [[Accuracy]] | higher | 95.74% | 97.92% | Generated data alone underperforms the 20% original mix. |
| ResNet-19 with 20% original / 80% generated samples | [[NEU-CLS]] classification | Average [[Accuracy]] | higher | 97.62% | 99.23% | Highest classifier average in Table 3. |
| Class-level result at 20% original / 80% generated samples | [[NEU-CLS]] classification | Overall class accuracy | higher | 97.42-97.82% at 100% original for Sc/Rs | 99.94% for Sc, 99.67% for Rs | Table 2 reports class-wise overall accuracy by class. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Six-class steel defect classification | Percent correct | higher | yes | Reported for class-wise and average classifier results. |
| [[Precision]] | Classification evaluation formula | TP / (TP + FP) | higher | no | Used to define AP. |
| [[Recall]] | Classification evaluation formula | TP / (TP + FN) | higher | no | Used to define AP. |

### Ablations

- Real/generated mixture ablation: 100%, 75%, 50%, 30%, 20%, and 0% original samples.
- Classifier comparison: fully supervised learning, VGG-16, ResNet-19, and MobileNet V2.
- Qualitative synthetic-image inspection: generated quality is better for scratches, rolled-in scale, patches, and inclusion than for pitted surface and some other categories.

## Dataset / Benchmark Details

- Source: NEU-CLS from Northeastern University.
- Collection: CCD camera images from hot-rolled steel plate surfaces, manually filtered and cropped.
- Annotation: six image-level defect classes.
- Size: 1800 images, 300 per class.
- Splits: 7:3 train/test; 1260 train and 540 test.
- Modalities: 2D visual surface images.
- License: not reported.
- Leakage risks: not reported; generated samples are created from the training split and evaluated against the test split.
- Bias / coverage: six representative steel surface defects only.
- Maintenance: not reported.

## Limitations

- Stated: EDCGAN-generated images are weaker for some classes, especially pitted surface, and generated data alone does not fully express all features of the original dataset.
- Stated: the method targets the insufficient-sample setting but still uses original samples; replacing all original data with generated data lowers accuracy.
- Inferred: the paper reports no random-seed sensitivity, statistical tests, or leakage audit.

## Reproducibility

- Code: not reported.
- Data: [[NEU-CLS]] URL reported.
- Hyperparameters: mini-batch size, learning rates, epochs, beta values, and dataset ratios are reported.
- Random seeds: not reported.
- Environment: PyTorch 1.13.0.
- Checkpoints / models: not reported.
- Exact preprocessing: original crop details come from the dataset description; generated image size is 224x224.
- Artifact status: paper open access; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Metallic surface defect detection]]
- Methods: [[EDCGAN]], [[GAN]], [[Data augmentation]]
- Datasets: [[NEU-CLS]]
- Benchmarks: [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]]
- Concepts: [[Industrial visual inspection]], [[Surface defect detection]]
- Dataset-domain links: [[NEU-CLS]] supports [[Metal inspection]] because it contains hot-rolled steel plate surface defects.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] | Shares dataset / Shares method | Both use NEU-CLS and GAN-based augmentation for surface defect classification. |
| [[2023 - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects]] | Shares dataset / Shares task | Both classify NEU-CLS steel surface defects with synthetic data support. |

### Backlinks Updated

- [[NEU-CLS]]
- [[Metal inspection]]
- [[EDCGAN]]

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[EDCGAN]] | Created | Paper method and experiments. |

## Questions

- Is the reported 1260 training sample count intended as total images rather than per class?
- Are the generated samples balanced equally across all six classes?
- Does a code release exist outside the paper?
