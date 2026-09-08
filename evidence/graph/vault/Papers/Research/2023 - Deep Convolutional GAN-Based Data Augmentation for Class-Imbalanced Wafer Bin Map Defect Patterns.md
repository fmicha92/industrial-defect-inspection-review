---
title: "Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in Wafer Bin Map"
aliases:
  - "Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in Wafer Bin Map"
paper_key: "sha256:da029fac51ab3ee6b21347ac6e045c39e73700733838c413fd77f8120139981a"
paper_type: research
year: 2023
venue: "Applied Sciences"
authors:
  - "Sangwoo Park"
  - "Cheolwoo You"
status: processed
processed_at: 2026-05-23
topics:
  - "wafer bin map classification"
  - "DCGAN augmentation"
  - "class imbalance"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[DCGAN wafer map augmentation]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[DCGAN]]"
metrics:
  - "[[Accuracy]]"
  - "[[PGI]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "PGI is the polymorphic generative index proposed to compare augmentation methods for sparse wafer-map classes."
baselines:
  - "CAE-based augmentation"
benchmarks:
  - "[[WM-811K]]"
code: "not reported"
data: "uses publicly available WM-811K"
doi: "10.3390/app13095507"
arxiv: "not reported"
url: "https://doi.org/10.3390/app13095507"
pdf: "paper-inbox/10_processed/Research/2023 - Park - Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in....pdf"
related_papers: []
related_concepts:
  - "[[Wafer map defect classification]]"
  - "[[Semiconductor and electronics]]"
related_methods:
  - "[[DCGAN wafer map augmentation]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2023 - Park - Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in....pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Park - Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in....md"
extracted_text: "paper-inbox/90_processing/text/2023 - Park - Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in....txt"
artifact_status: "public dataset used; code not reported"
tags:
  - paper
---
# Deep Convolutional Generative Adversarial Networks-Based Data Augmentation Method for Classifying Class-Imbalanced Defect Patterns in Wafer Bin Map

## Summary

Park and You propose a [[DCGAN wafer map augmentation]] method for class-imbalanced wafer bin map defect pattern classification. The method trains DCGAN augmentation models on selected 26 x 26 [[WM-811K]] wafer bin maps, refines generated wafer maps with a masking process, and uses the generated maps to train a CNN defect-pattern classifier. The paper compares DCGAN augmentation against CAE-based augmentation and proposes [[PGI]], the polymorphic generative index, for evaluating class-specific generative diversity.

## Paper Type

- Type: research.
- Why: The paper proposes an augmentation method, a masking refinement process, and a generative evaluation index, then compares them experimentally.

## Problem

- Task: [[Wafer map defect classification]], [[Defect classification]]
- Setting: [[Semiconductor and electronics]]
- Inputs: wafer bin maps showing good, failed, and non-wafer dies.
- Outputs: wafer defect pattern labels and generated wafer bin maps for classifier training.
- Motivation: WM-811K has extreme class imbalance, and sparse defect classes make classifier training unreliable.
- Assumptions: generated wafer maps should preserve pattern semantics while increasing diversity within sparse classes.

## Contribution

- Claimed: A DCGAN-based WBM augmentation model forms more varied defect patterns than CAE augmentation.
- Claimed: A masking process refines generated wafer maps by correcting outside-wafer regions.
- Claimed: [[PGI]] provides a domain-specific quantitative index for comparing augmentation models when ImageNet-based metrics are unsuitable.
- Shown: A CNN trained with DCGAN-generated wafer maps outperforms one trained with CAE-generated wafer maps for every defect pattern, with about 5.31% higher pattern-specific accuracy on average.

## Method

- Core idea: train a DCGAN generator/discriminator for each selected defect pattern, refine generated maps with a circular wafer mask, and use augmented maps to train a CNN classifier.
- Architecture / algorithm: [[DCGAN wafer map augmentation]], [[DCGAN]], [[Data augmentation]].
- Generated image shape: generator outputs WBM images of shape 64 x 64 x 3.
- Classifier: CNN with three convolutional layers, three max-pooling layers, and two fully connected layers.
- Masking process: a circular mask identifies the wafer area and removes or corrects generated bits outside the wafer area.
- Baseline: CAE-based augmentation with noise added to the latent vector.
- Implementation: Keras 2.5.1 with TensorFlow 2.5 and Python 3.8.5.

## ML / DL Extraction

### Task Formulation

- Input modality: wafer bin maps.
- Output target: center, donut, edge-location, edge-ring, location, near-full, random, scratch, and none labels.
- Supervision: supervised classifier training with labeled WM-811K maps; class-conditional augmentation models are trained from selected examples.
- Objective: improve classifier accuracy under extreme class imbalance.

### Model And Training

- Model family: [[GAN]], [[Generative Models]].
- Architecture: [[DCGAN]] augmentation model plus CNN classifier.
- Baseline architecture: convolutional autoencoder augmentation.
- Losses: standard DCGAN and classifier losses are implied by model descriptions; exact loss equations are not summarized in this note.
- Training compute: not reported beyond software versions.

### Data

- Dataset: [[WM-811K]].
- Full WM-811K context: approximately 811,000 WBMs; 172,950 labeled wafers; 25,519 wafers labeled with defect patterns.
- Experimental subset: only 26 x 26 wafer maps are selected because they were labeled by domain experts and uniformly refined.
- Selected 26 x 26 counts: center 90, donut 1, edge-location 296, edge-ring 31, location 290, near-full 16, random 74, scratch 72, none 13,489.
- License: public dataset; this paper states WM-811K is publicly available.

### Evaluation

- Protocol: compare CNN classifiers trained with DCGAN-generated maps versus CAE-generated maps; compare cross-classification of generated maps; compute [[PGI]].
- Used performance metrics: [[Accuracy]], [[PGI]].
- Primary metric: [[Accuracy]] for classifier performance.
- Metric direction / units: higher is better.
- Statistical tests: not reported.
- Failure cases: PGI has limitations when a defect class has only one original example, such as donut.

## Evidence

### Experimental Setup

- Dataset: [[WM-811K]] 26 x 26 subset.
- Baseline: CAE-based augmentation.
- Used performance metrics: [[Accuracy]], [[PGI]].

### Main Results

| Evaluation | Baseline | Paper result | Notes |
|---|---:|---:|---|
| Original WBM classification with augmented-data classifiers | CAE-trained classifier | DCGAN-trained classifier higher for every defect pattern | Difference ranges from 0.57% to 10.81% by defect pattern. |
| Average pattern-specific accuracy | CAE augmentation | DCGAN about 5.31% higher | Reported for classifiers trained with augmented maps. |
| Misclassification rate for original WBMs | CAE augmentation | DCGAN 1.41% lower | Normal-vs-abnormal discrimination is emphasized as industrially important. |
| Cross-evaluation of generated maps | CAE-generated maps | DCGAN-generated maps 14.26% higher on average | Paper interprets this as evidence DCGAN forms more diverse defect patterns. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | defect-pattern classifier | percentage or fraction correctly classified | higher | yes | Reported per defect pattern. |
| [[PGI]] | augmentation model comparison | class-specific polymorphic generative index | higher | no | Proposed to avoid ImageNet-pretrained-model dependence for sparse industrial data. |

### Ablations

- CAE latent-noise augmentation produces maps similar to the original examples, especially under sparse classes.
- DCGAN-generated maps are reported as more diverse while maintaining defect pattern labels.
- Masking corrects generated maps outside the wafer area.

## Dataset / Benchmark Details

- Source: [[WM-811K]] public dataset.
- Collection: real-world wafer maps from semiconductor manufacturing.
- Annotation: one defect pattern per wafer map in the paper's selected setting.
- Bias / coverage: severe class imbalance; selected 26 x 26 subset contains only one donut map.
- Leakage risks: no explicit leakage checks reported.

## Limitations

- Stated: [[PGI]] cannot exceed 1 when a class has only one original sample; PGI may not indicate how many additional diverse patterns an augmentation model can form in extreme scarcity.
- Stated: PGI depends on classifier performance and should be compared using the same classifier structure.
- Inferred: The experiment is constrained to the 26 x 26 WM-811K subset.

## Reproducibility

- Code: not reported.
- Data: [[WM-811K]] public dataset.
- Hyperparameters: model architectures and software versions are reported in tables.
- Random seeds: not reported.
- Environment: Keras 2.5.1, TensorFlow 2.5, Python 3.8.5.
- Artifact status: public dataset used; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Defect classification]]
- Methods: [[DCGAN wafer map augmentation]], [[DCGAN]], [[Data augmentation]]
- Datasets: [[WM-811K]]
- Benchmarks: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[PGI]]
- Concepts: [[Wafer map defect classification]], [[Semiconductor and electronics]]

### Shares Dataset

- [[WM-811K]]: source of 26 x 26 wafer bin maps.

### Shares Method

- [[DCGAN wafer map augmentation]]: proposed augmentation approach.
- [[DCGAN]]: generator/discriminator model family.
- [[Data augmentation]]: class-imbalance mitigation.

### Shares Task

- [[Wafer map defect classification]]: primary task.
- [[Defect classification]]: general classification framing.

### Shares Metric

- [[Accuracy]]: classifier performance metric.
- [[PGI]]: proposed augmentation evaluation index.
