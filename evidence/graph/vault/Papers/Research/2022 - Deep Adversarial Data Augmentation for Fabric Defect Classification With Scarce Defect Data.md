---
title: "Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data"
aliases:
  - "Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data"
paper_key: "doi:10.1109/TIM.2022.3185609"
paper_type: research
year: 2022
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Bingyu Lu"
  - "Meng Zhang"
  - "Biqing Huang"
status: processed
processed_at: 2026-05-31
topics:
  - "fabric defect classification"
  - "scarce defect data"
  - "adversarial data augmentation"
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[ZJU-Leaper]]"
  - "[[LaceCls]]"
methods:
  - "[[Defect Transfer GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "ResNet101"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + FP + TN + FN), reported as percent; higher is better."
  - "F1-score: 2TP / (2TP + FP + FN), reported as percent; higher is better."
baselines:
  - "LG-Based BPNN"
  - "Modified AlexNet"
  - "VLSTM"
  - "Cutout"
  - "CutMix"
  - "Mixup"
  - "RandTransform"
benchmarks:
  - "[[ZJU-Leaper]]"
code: "not reported"
data: "ZJU-Leaper public; LaceCls collected by authors"
doi: "10.1109/TIM.2022.3185609"
url: "https://doi.org/10.1109/TIM.2022.3185609"
pdf: "paper-inbox/10_processed/Research/2022 - Lu - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data.pdf"
related_methods:
  - "[[Defect Transfer GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[ZJU-Leaper]]"
  - "[[LaceCls]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2022 - Lu - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Lu - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Lu - Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data.txt"
artifact_status: "public benchmark plus private author dataset"
tags:
  - paper
---

# Deep Adversarial Data Augmentation for Fabric Defect Classification With Scarce Defect Data

## Summary

The paper proposes DefectTransfer, an adversarial fabric defect data augmentation method for scarce defect classification. It evaluates the method on the public [[ZJU-Leaper]] dataset and the author-collected [[LaceCls]] dataset, showing that synthetic cut-paste defects plus adversarial transformations can outperform traditional augmentation under very low defect-data regimes. PDF Tables I-III give direct synthetic-data-assisted versus real-only or no-augmentation comparisons: on ZJU-Leaper at the 0.1% defect-image setting, ResNet101 improves from 74.91% accuracy / 1.51% F1 with no augmentation to 84.78% accuracy / 61.15% F1 with DefectTransfer; on LaceCls at the 10% defect-image setting, ResNet101 improves from 50.00% accuracy / 0.00% F1 with no augmentation to 94.44% accuracy / 94.33% F1 with DefectTransfer.

## Paper Type

- Type: research.
- Why: The paper introduces a method, evaluates it against baselines, and reports classification performance under controlled scarcity settings.

## Problem

- Task: [[Defect classification]] for fabric images.
- Setting: scarce textile defect data with many defect-free images.
- Inputs: defect images, defect-free images, optional defect masks, and image labels.
- Outputs: defective versus defect-free classification.
- Motivation: real fabric defects are rare, costly to label, and insufficient for training deep classifiers.
- Assumptions: defect position and size should not be fully tied to the background texture during classifier training.

## Contribution

- Claimed: DefectTransfer addresses defect-data scarcity by combining cut-paste defect transfer with adversarial transformations.
- Shown: ResNet101 with DefectTransfer outperforms no augmentation and several traditional augmentation methods across ZJU-Leaper scarcity settings.
- Inferred: The paper is one of the strongest textile-specific examples of synthetic defect augmentation on a public fabric dataset.

## Method

- Core idea: paste defect regions onto defect-free fabric images and adversarially transform defect attributes to create harder and more diverse training samples.
- Architecture / algorithm: DefectTransfer augmentation plus a ResNet-based fabric defect classifier.
- Objective / loss: cross-entropy classifier loss; during adversarial transformation, defect parameters are adjusted to maximize the current classifier loss before the DNN weights are updated on the harder synthetic defect image.
- Training data: ZJU-Leaper and LaceCls.
- Data pipeline: choose very small numbers of defect images per texture pattern while retaining all defect-free images; generate synthetic defect images by pasting defects onto defect-free backgrounds, preferably from the same texture.
- Augmentation / synthesis: cut-paste transferred defects; random scaling, moving, and rotation before paste; adversarial selection of transform mode and direction from loss gradients; manually annotated masks by default; Grad-CAM masks in the no-mask variant.
- Inference: trained ResNet classifies fabric images.

## ML / DL Extraction

### Data

- Datasets: [[ZJU-Leaper]] and [[LaceCls]].
- ZJU-Leaper size: 27,650 defect images and 71,127 defect-free images with 19 texture patterns.
- ZJU-Leaper annotations: image labels, bounding boxes, and pixelwise masks.
- ZJU-Leaper scarcity setting: randomly choose 1/3/5/10 defect images per texture pattern, equivalent to 0.1%/0.3%/0.5%/1.0% of the 18,434 original training defect images; retain all 47,418 defect-free training images.
- ZJU-Leaper test set: 9,216 defect images and 23,709 defect-free images.
- [[LaceCls]] size: 6,610 lace images collected on a production line; training set has 4,800 defect-free images and 10 defect images; test set has 900 defect-free and 900 defect images.
- License: ZJU-Leaper is public; LaceCls availability is not reported.

### Evaluation

- Protocol: compare ResNet101 trained with DefectTransfer, DefectTransfer without masks, and traditional augmentations under multiple scarcity settings.
- Used performance metrics: [[Accuracy]] and [[F1-score]].
- Baselines: LG-Based BPNN, Modified AlexNet, VLSTM, no augmentation, Cutout, CutMix, Mixup, RandTransform.
- Statistical tests: not reported.
- Failure cases: complex LaceCls textures are identified as an important cause of classification failure.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| ZJU-Leaper scarce defect augmentation | ZJU-Leaper / ResNet101 | Accuracy | higher | no augmentation at 0.1% defects: 74.91% | DefectTransfer at 0.1% defects: 84.78% | Table I mean accuracy; result/baseline IF = 1.13. |
| ZJU-Leaper scarce defect augmentation | ZJU-Leaper / ResNet101 | F1-score | higher | no augmentation at 0.1% defects: 1.51% | DefectTransfer at 0.1% defects: 61.15% | Table II mean F1; result/baseline IF = 40.50, but the baseline is near zero. |
| ZJU-Leaper no-mask variant | ZJU-Leaper / ResNet101 | Accuracy / F1-score | higher | no augmentation at 0.1% defects: 74.91% / 1.51% | DefectTransfer wo mask: 83.34% / 56.83% | Tables I-II; automatic masks still outperform traditional augmentations by mean metrics. |
| ZJU-Leaper higher scarce-data setting | ZJU-Leaper / ResNet101 | Accuracy / F1-score | higher | DefectTransfer at 0.1% defects: 84.78% / 61.15% | DefectTransfer at 1.0% defects: 87.32% / 69.62% | Tables I-II; this is more-data improvement, not a pure augmentation-vs-real-only comparison. |
| Full-data comparison | ZJU-Leaper | Accuracy / F1-score | higher | Modified AlexNet trained with all images: 87.31% / 69.29% | DefectTransfer with 1.0% defects: 87.32% / 69.62% | Tables I-II; useful context but not the clean IF row because the model family differs. |
| LaceCls no-augmentation collapse | LaceCls | Accuracy / F1-score | higher | no augmentation at 10% defects: 50.00% / 0.00% | DefectTransfer at 10% defects: 94.44% / 94.33% | Table III; result/baseline accuracy IF = 1.89; F1 IF is undefined because baseline F1 is 0.00. |
| LaceCls no-mask variant | LaceCls | Accuracy / F1-score | higher | no augmentation at 10% defects: 50.00% / 0.00% | DefectTransfer wo mask: 86.89% / 85.12% | Table III; automatic masks still strongly improve performance. |
| LaceCls traditional augmentation comparison | LaceCls | Accuracy / F1-score | higher | best non-DefectTransfer augmentation, CutMix: 68.11% / 66.43% | DefectTransfer at 10% defects: 94.44% / 94.33% | Table III; DefectTransfer substantially exceeds traditional augmentation. |
| Adversarial transformation ablation | ZJU-Leaper | Accuracy | higher | scaling + moving + rotating without adversarial training | +1.54 percentage points | Isolates the adversarial part of DefectTransfer. |
| Adversarial transformation ablation | ZJU-Leaper | F1-score | higher | scaling + moving + rotating without adversarial training | +8.74 percentage points | Isolates the adversarial part of DefectTransfer. |
| More defect images within scarcity range | ZJU-Leaper | Accuracy | higher | lower defect-image setting | +2.55 percentage points at higher defect-image setting | Reported when defect data increases within studied limits. |
| More defect images within scarcity range | ZJU-Leaper | F1-score | higher | lower defect-image setting | +8.47 percentage points at higher defect-image setting | Reported when defect data increases within studied limits. |
| More defect images within scarcity range | LaceCls | Accuracy / F1-score | higher | lower defect-image setting | +2.12 percentage points at higher defect-image setting | Reported for both metrics. |

### Synthesis-Impact Table Fit

This paper fits a synthesis-impact table when the row is framed as scarce-data fabric defect classification with an explicit synthetic-data-assisted setup versus a same-model no-augmentation baseline. The cleanest candidate rows are:

| Candidate row | Domain | Dataset | Task | Baseline | Synthetic-data-assisted result | Metric | result/baseline IF | Fit judgment |
|---|---|---|---|---:|---:|---|---:|---|
| ZJU-Leaper 0.1% defect images | Textile inspection | [[ZJU-Leaper]] | defect classification | 74.91 | 84.78 | accuracy | 1.13 | Include if using accuracy for classification. |
| ZJU-Leaper 0.1% defect images | Textile inspection | [[ZJU-Leaper]] | rare-defect classification | 1.51 | 61.15 | F1-score | 40.50 | Include only with a caveat; the IF is dominated by a near-zero F1 baseline. |
| LaceCls 10% defect images | Textile inspection | [[LaceCls]] | defect classification | 50.00 | 94.44 | accuracy | 1.89 | Strong include if using accuracy for classification. |
| LaceCls 10% defect images | Textile inspection | [[LaceCls]] | rare-defect classification | 0.00 | 94.33 | F1-score | undefined | Do not use as a finite IF row if the table requires F1; report separately as zero-baseline collapse. |

For a Table 3 narrative that uses F1 for rare-class classification, [[LaceCls]] is strong qualitative evidence but awkward quantitatively because the real-only F1 denominator is zero. [[ZJU-Leaper]] gives a finite F1 IF, but the 1.51% baseline makes the factor numerically unstable. The most defensible finite IF entry is the accuracy-based LaceCls row, provided the table allows accuracy for classification studies.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | fabric defect classification | ratio of correctly classified images | higher | yes | Used with F1 because data distribution is imbalanced |
| [[F1-score]] | fabric defect classification | harmonic tradeoff of precision and recall | higher | yes | Preferred complement to accuracy for imbalanced tests |

## Dataset / Benchmark Details

- Source: ZJU-Leaper public fabric benchmark; [[LaceCls]] author-collected lace dataset.
- Collection: ZJU-Leaper images come from real fabrics in factory or laboratory shooting; [[LaceCls]] images are from a production line.
- Annotation: ZJU-Leaper includes image labels, boxes, and pixel masks; [[LaceCls]] has defect-free and one defect class labels.
- Size: see Data section.
- Splits: paper-defined scarce training subsets plus full testing sets.
- Modalities: fabric images.
- Leakage risks: not reported.
- Bias / coverage: LaceCls has complex lace textures and only one defect class in training.

## Limitations

- Stated: the method still has failure cases on complex textures, especially in LaceCls.
- Inferred: the public-dataset evidence is strongest for ZJU-Leaper; LaceCls is not reported as public.

## Reproducibility

- Code: not reported.
- Data: ZJU-Leaper public; LaceCls availability not reported.
- Hyperparameters: initial learning rate 0.001, momentum 0.9, weight decay 0.0005, batch size 16, 30k first-step iterations, 20k second-step iterations, and 10 adversarial transformation iterations.
- Random seeds: not reported.
- Hardware: not reported in extracted source.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect classification]]
- Methods: [[Defect Transfer GAN]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[ZJU-Leaper]], [[LaceCls]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Accuracy]], [[F1-score]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] | Shares dataset | This paper uses ZJU-Leaper as the public fabric benchmark for scarce-data augmentation. |
| [[2022 - Data Augmentation Method for Fabric Defect Detection]] | Shares task / shares method | Both evaluate synthetic or GAN-based data augmentation for fabric defect detection. |

### Backlinks Updated

- [[Defect Transfer GAN]]
- [[ZJU-Leaper]]
- [[LaceCls]]

## Questions

- The preprocessed metadata initially captured `10.1109/tpami.2019.2918284` from a DenseNet reference; the paper text reports Digital Object Identifier `10.1109/TIM.2022.3185609`.
- Is [[LaceCls]] publicly available anywhere, or only author-collected?
