---
title: "Unveiling Patterns: A Study on Semi-Supervised Classification of Strip Surface Defects"
aliases:
  - "Unveiling Patterns"
paper_key: "doi:10.1109/access.2023.3326843"
paper_type: research
year: 2023
venue: "IEEE Access"
authors:
  - "Yongfei Liu"
  - "Haoyu Yang"
  - "Chenwei Wu"
status: processed
processed_at: 2026-05-31
topics:
  - "strip steel surface defect classification"
  - "semi-supervised learning"
  - "synthetic image generation"
tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-CLS]]"
dataset_sizes:
  - "NEU-CLS: 1800 images, six defect classes, 300 images per class, 200x200 pixels"
splits:
  - "NEU-CLS: 6:4 train/test split; 1080 training images and 720 test images"
methods:
  - "[[Semi-supervised learning]]"
  - "[[Image synthesis model]]"
  - "[[Double uncertainty weighting technique]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "ResNet-34"
metrics:
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: percentage of correctly classified NEU-CLS test images; higher is better."
baselines:
  - "traditional fully supervised ResNet-34"
  - "traditional semi-supervised ResNet-34"
benchmarks:
  - "[[NEU-CLS]]"
evaluation_protocol: "NEU-CLS classification with different labeled-sample ratios and generated-data expansion multiples."
parameters: "not reported"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.1109/access.2023.3326843"
pdf: "paper-inbox/10_processed/Research/2023 - Liu - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects.pdf"
code: "not reported"
data: "NEU-CLS is used; host URL not reported by the paper text."
doi: "10.1109/access.2023.3326843"
arxiv: "not applicable"
related_papers:
  - "[[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]]"
  - "[[2023 - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[Semi-supervised learning]]"
  - "[[Image synthesis model]]"
  - "[[Double uncertainty weighting technique]]"
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
  - "[[Image synthesis model]]"
  - "[[Double uncertainty weighting technique]]"
source_file: "paper-inbox/10_processed/Research/2023 - Liu - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Liu - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Liu - Unveiling Patterns A Study on Semi-Supervised Classification of Strip Surface Defects.txt"
artifact_status: "code not reported; uses NEU-CLS"
tags:
  - paper
---
# Unveiling Patterns: A Study on Semi-Supervised Classification of Strip Surface Defects

## Summary

The paper studies strip steel surface defect classification under limited labels. It combines a semi-supervised teacher-student setup with an image synthesis model that improves DCGAN-style generation by changing the discriminator loss, then applies double uncertainty weighting to supervised and unsupervised losses. The evaluation uses [[NEU-CLS]], a hot-rolled steel surface defect dataset, and reports that synthetic samples can improve semi-supervised classification when generated data are mixed carefully with the original training set.

## Paper Type

- Type: research.
- Why: The paper proposes a model, trains it on a public steel surface defect dataset, and reports comparative classification accuracy.

## Problem

- Task: [[Defect classification]] for strip steel surface defects.
- Setting: [[Metal inspection]] in the iron and steel industry.
- Inputs: NEU-CLS RGB defect images.
- Outputs: six-way defect class labels.
- Motivation: fully supervised models depend on labeled samples, while industrial strip-steel datasets often have few labeled examples and many unlabeled examples.
- Assumptions: unlabeled samples and generated samples can improve classification when they are weighted and mixed into training.

## Contribution

- Claimed: A semi-supervised strip surface defect classification model with an improved image synthesis model and a double uncertainty weighting technique.
- Shown: The semi-supervised model improves over a fully supervised ResNet-34 at low labeled-sample ratios, and generated NEU-CLS-like images improve performance for selected expansion multiples.
- Inferred: The synthesis component is useful only when generated images retain class-relevant defect appearance; the paper notes weaker generation quality for some classes.

## Method

- Core idea: Combine semi-supervised learning, synthetic image generation, and sample-specific uncertainty weighting for strip steel defect classification.
- Architecture / algorithm: [[Semi-supervised learning]], [[Image synthesis model]] based on [[DCGAN]], [[Double uncertainty weighting technique]], and ResNet-34 classification.
- Objective / loss: the generator uses the DCGAN generator loss; the discriminator loss is modified by adding a factor on real-sample loss to make generated false samples more realistic. Double uncertainty weighting scales supervised and unsupervised losses differently for correctly/incorrectly predicted or teacher-student inconsistent samples.
- Optimization: not reported beyond the loss formulations.
- Training data: [[NEU-CLS]].
- Data pipeline: split NEU-CLS into train/test, divide training samples into labeled and mixed samples, generate additional samples with the image synthesis model, and train the semi-supervised classifier.
- Augmentation / synthesis: generated samples are created from labeled NEU-CLS training samples and used to fill or expand unlabeled training data.
- Inference: classify NEU-CLS test images into six steel surface defect categories.
- Complexity / deployment constraints: not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: 200x200 steel surface defect images.
- Output target: one of six NEU-CLS defect classes: rolled-in scale, patches, crazing, pitted surface, inclusion, or scratches.
- Supervision: semi-supervised learning with labeled and unlabeled training samples.
- Objective: improve classification accuracy under limited labeled data.

### Model And Training

- Model family: [[GAN]], [[Semi-supervised learning]].
- Architecture: ResNet-34 classifier; DCGAN-like generator and discriminator for image synthesis.
- Parameters: generator receives 100-dimensional random noise and generates 64x64x3 images in the described DCGAN section; exact full model parameter count is not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: supervised classification loss, unsupervised loss, modified discriminator loss, and generator loss.
- Optimizer: not reported.
- Hyperparameters: labeled ratios tested include 5%, 25%, 50%, 75%, and 100%; generated-data expansion multiples include 0 through 5.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[NEU-CLS]].
- Data source: Northeastern University.
- Dataset size: 1800 images, six categories, 300 images per category.
- Labels / annotations: image-level defect class labels.
- Splits: 6:4 train/test split; 1080 training images and 720 test images. Each class has 180 training images and 120 test images.
- Preprocessing: not reported.
- Augmentation: [[Image synthesis model]] generates artificial NEU-CLS samples.
- Synthetic data: generated samples are mixed with labeled and unlabeled training data; the paper tests generated-data expansion multiples from 1 to 5.
- Leakage checks: not reported.
- License: the article is distributed under CC BY-NC-ND 4.0; NEU-CLS dataset license is not reported.

### Evaluation

- Protocol: compare traditional supervised and semi-supervised ResNet-34 models at different labeled ratios, then add generated samples at different multiples and evaluate accuracy on the NEU-CLS test set.
- Used performance metrics: [[Accuracy]].
- Primary metric: [[Accuracy]].
- Metric definitions: classification accuracy on the test set.
- Metric direction / units: higher percentage is better.
- Baselines: traditional supervised ResNet-34; traditional semi-supervised model without generated samples.
- Benchmarks: [[NEU-CLS]].
- Statistical tests: not reported.
- Failure cases: generated samples for crazing and rolled-in scale are described as less detailed than real samples; generated samples for inclusion, patches, pitted surface, and scratches are reported as more realistic.

## Evidence

### Experimental Setup

- Datasets: [[NEU-CLS]].
- Splits: 1080 training images and 720 test images, split 6:4 by class.
- Baselines: fully supervised ResNet-34 and semi-supervised ResNet-34 without generated expansion.
- Used performance metrics: [[Accuracy]].
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Semi-supervised model at 5% labeled samples | [[NEU-CLS]] classification | [[Accuracy]] | higher | 74.54% | 85.73% | Same ResNet-34 backbone; mixed sample count 1080. |
| Semi-supervised model at 25% labeled samples | [[NEU-CLS]] classification | [[Accuracy]] | higher | 82.67% | 89.92% | Uses labeled plus mixed samples. |
| Semi-supervised model at 50% labeled samples | [[NEU-CLS]] classification | [[Accuracy]] | higher | 86.72% | 91.44% | Uses labeled plus mixed samples. |
| Semi-supervised model at 75% labeled samples | [[NEU-CLS]] classification | [[Accuracy]] | higher | 91.37% | 92.06% | Improvement is smaller as labels increase. |
| Generated-data expansion at 25% labeled samples, k=3 | [[NEU-CLS]] classification | [[Accuracy]] | higher | 89.92% | 91.73% | Best reported value for the 25% row in Table 4. |
| Generated-data expansion at 50% labeled samples, k=3 | [[NEU-CLS]] classification | [[Accuracy]] | higher | 91.44% | 92.84% | Best reported value for the 50% row in Table 4. |
| Generated-data expansion at 75% labeled samples, k=3 | [[NEU-CLS]] classification | [[Accuracy]] | higher | 92.06% | 94.71% | Best reported value visible in Table 4. |
| Generated-data expansion at 100% labeled samples, k=3 | [[NEU-CLS]] classification | [[Accuracy]] | higher | 92.87% | 96.35% | Uses generated samples in addition to all original training samples. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Six-class defect classification | Percent correctly classified test images | higher | yes | Reported across labeled ratios and generated-data multiples. |

### Ablations

- Labeled-sample ratio ablation: 5%, 25%, 50%, 75%, and 100% labeled data.
- Generated-data expansion ablation: expansion multiples 0 through 5.
- Component ablation: the paper compares the teacher-based semi-supervised baseline, TE+ISM, TE+SUW, and TE+ISM+SUW. TE+ISM+SUW reports 89.57%, 91.14%, 92.87%, 96.77%, and 98.85% accuracy across the listed labeled-sample proportions, outperforming the corresponding baseline row.
- Qualitative generation comparison: generated images are visually compared with DCGAN outputs and real NEU-CLS samples.

## Dataset / Benchmark Details

- Source: Northeastern University.
- Collection: images captured by CCD camera on hot-rolled steel plate surfaces.
- Annotation: image-level class labels for six defect types.
- Size: 1800 images, 300 per class.
- Splits: 6:4 split, 180 train and 120 test images per class.
- Modalities: 2D visual surface images, 200x200 pixels.
- License: not reported.
- Leakage risks: not reported; generated samples are derived from training samples and evaluated on the held-out test set.
- Bias / coverage: limited to six representative hot-rolled steel surface defect classes.
- Maintenance: not reported.

## Limitations

- Stated: generated samples are less convincing for more complex defect types such as crazing and rolled-in scale.
- Stated: synthetic data improves accuracy only for some mixing proportions; performance does not increase monotonically with generated-data volume.
- Inferred: the reported synthesis quality is partly qualitative, and no leakage-specific checks or random-seed sensitivity are reported.

## Reproducibility

- Code: not reported.
- Data: [[NEU-CLS]] is used; source URL is not reported in the paper text.
- Hyperparameters: labeled ratios and generated-data multiples are reported; optimizer, learning rate, and seeds are not reported in the extracted text.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: not reported.
- Artifact status: dataset named, code not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Metallic surface defect detection]]
- Methods: [[Semi-supervised learning]], [[Image synthesis model]], [[Double uncertainty weighting technique]], [[DCGAN]], [[Data augmentation]]
- Datasets: [[NEU-CLS]]
- Benchmarks: [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]]
- Concepts: [[Industrial visual inspection]], [[Surface defect detection]]
- Dataset-domain links: [[NEU-CLS]] supports [[Metal inspection]] because the paper describes it as a hot-rolled steel plate surface defect dataset.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning]] | Shares dataset / Shares method | Both use NEU-CLS and synthetic data augmentation for surface defect classification. |
| [[2023 - An End-to-End Steel Surface Classification Approach Based on EDCGAN and MobileNet V2]] | Shares dataset / Shares method | Both use NEU-CLS and GAN-style synthesis to improve steel surface defect classification. |

### Backlinks Updated

- [[NEU-CLS]]
- [[Metal inspection]]
- [[Image synthesis model]]
- [[Double uncertainty weighting technique]]
- [[Semi-supervised learning]]

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Image synthesis model]] | Created | Paper method section and experiments. |
| [[Double uncertainty weighting technique]] | Created | Paper method section. |

## Questions

- Does the implementation release code or exact random seeds outside the paper?
- How sensitive are the results to the generated-data multiple beyond the tested range?
- Are there class-specific confusion matrices for the synthetic-data experiments?
