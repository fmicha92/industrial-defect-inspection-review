---
title: "Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection"
aliases:
  - "Real-IAD"
paper_key: "doi:10.1109/cvpr52733.2024.02159"
paper_type: dataset
year: 2024
venue: "CVPR"
authors:
  - "Chengjie Wang"
  - "Wenbing Zhu"
  - "Bin-Bin Gao"
  - "Zhenye Gan"
  - "Jiangning Zhang"
  - "Zhihao Gu"
  - "Shuguang Qian"
  - "Mingang Chen"
  - "Lizhuang Ma"
status: processed
processed_at: 2026-05-22
audited_at: 2026-06-11
topics:
  - "industrial anomaly detection"
  - "multi-view dataset"
  - "fully unsupervised anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Real-IAD]]"
dataset_sizes:
  - "Real-IAD: 151050 images, 99721 normal images and 51329 anomalous images"
  - "30 object classes, each with 5 shooting angles"
splits:
  - "UIAD setting uses normal-only training images and normal/anomalous test images"
  - "FUIAD fixes a test set with 100 normal samples and 100 anomalous samples per category, then samples noisy training sets with anomalous ratios alpha in {0, 0.1, 0.2, 0.4}"
methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised learning]]"
  - "[[Fully unsupervised industrial anomaly detection]]"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "I-AUROC: image-level anomaly detection AUROC; higher is better"
  - "S-AUROC: sample-level AUROC after integrating multiple views; higher is better"
  - "P-AUPRO: pixel-level area under the per-region overlap curve; higher is better"
baselines:
  - "PatchCore"
  - "PaDiM"
  - "CFlow"
  - "SimpleNet"
  - "DeSTSeg"
  - "RD"
  - "UniAD"
  - "SoftPatch"
benchmarks:
  - "[[Real-IAD]]"
code: "https://realiad4ad.github.io/Real-IAD"
data: "Real-IAD dataset reported by the paper"
doi: "10.1109/cvpr52733.2024.02159"
arxiv: "not applicable"
url: "https://realiad4ad.github.io/Real-IAD"
pdf: "paper-inbox/10_processed/Dataset/2024 - Wang - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Unsupervised learning]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Fully unsupervised industrial anomaly detection]]"
related_datasets:
  - "[[Real-IAD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[Real-IAD]]"
source_file: "paper-inbox/10_processed/Dataset/2024 - Wang - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Wang - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Wang - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.txt"
artifact_status: "project website and dataset access URL reported"
tags:
  - paper
---
# Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection

## Summary

The paper introduces [[Real-IAD]], a large-scale real-world multi-view industrial anomaly detection dataset. It contains 151,050 high-resolution images from 30 object classes, with 99,721 normal images and 51,329 anomalous images, five shooting angles per object, and pixel-level anomaly masks. The paper also defines a fully unsupervised industrial anomaly detection setting in which anomalous samples may appear in the training set, then benchmarks popular IAD methods under standard unsupervised and noisy fully unsupervised settings.

## Paper Type

- Type: dataset.
- Why: The paper contributes a new benchmark dataset, evaluation settings, sample-level metrics, and baseline results.

## Problem

- Task: [[Industrial anomaly detection]] and pixel-level [[Defect segmentation]].
- Setting: multi-industry visual quality inspection with five 2D views per object.
- Inputs: high-resolution industrial object images from top and side views.
- Outputs: image-level, pixel-level, and sample-level anomaly decisions.
- Motivation: common datasets such as MVTec AD and VisA are small enough that methods saturate, making differences hard to distinguish and limiting study of deployment-like settings.

## Contribution

- Claimed: Real-IAD is a real-world, large-scale, multi-view 2D IAD dataset that better separates method performance than saturated benchmarks.
- Shown: averaged I-AUROC drops from 97.9 on MVTec AD to 87.6 on single-view Real-IAD and 85.0 on multi-view Real-IAD, indicating a harder benchmark.
- Claimed: [[Fully unsupervised industrial anomaly detection]] better models production settings where the training stream may contain abnormal products because yield is high but not perfect.

## Method

- Dataset collection: 30 industrial products covering metal, plastic, wood, ceramics, and mixed materials.
- Defect manufacturing: missing parts, dirt, deformation, pits, damage, holes, cracks, scratches, foreign objects, contamination, and related defects are represented in the source text and figures.
- Capture rig: five HIKROBOT MV-CE200-10GC cameras at 3,648 x 5,472 resolution; one top-down camera plus four symmetric cameras at approximately 45 degrees; ring light source above the object.
- Annotation: normal/anomaly status is manually confirmed; anomalous images are annotated with LabelMe pixel-level masks.
- Cleaning: data are split into three groups, each trained with cascade R-CNN using an HRNet-32w backbone for confident-learning checks; inconsistent predictions are manually inspected and reannotated until AP changes stabilize and few images require modification.

## ML / DL Extraction

### Task Formulation

- UIAD: train on normal samples only and test on normal plus anomalous samples.
- FUIAD: train on noisy production-like data that may include anomalies, with noise ratio alpha in `{0, 0.1, 0.2, 0.4}`.
- Multi-view sample evaluation: each sample has multiple views, so the paper aggregates view results for sample-level anomaly detection.

### Models And Evaluation Setup

- UIAD baselines: PatchCore, PaDiM, CFlow, SimpleNet, DeSTSeg, RD, and UniAD.
- FUIAD baselines: PatchCore, PaDiM, CFlow, SimpleNet, DeSTSeg, RD, UniAD, and SoftPatch.
- Implementation: PatchCore, PaDiM, CFlow, and RD are reproduced with Anomalib; SimpleNet, DeSTSeg, and UniAD use official code.
- Preprocessing: all images are resized to 256 x 256; PatchCore and PaDiM use a 224 x 224 center crop from resized images.
- Hyperparameters: batch size, learning rate, and other hyperparameters follow official implementations.

### Data

- Total images: 151,050.
- Normal images: 99,721.
- Anomalous images: 51,329.
- Categories: 30 object classes.
- Views: five shooting angles for each object.
- Resolution: source table reports 2,000-5,000 image resolution after cropping from original high-resolution captures.
- Annotation levels: pixel, image, and sample.
- Defect area: source figure caption reports anomaly area proportions from 0.01% to 6.75% and defect ratios from 1:1 to 1:10; later visualization text also describes broader normalized ranges.

### Evaluation

- Metrics: image-level AUROC, pixel-level AUPRO, and sample-level AUROC.
- UIAD comparison datasets: MVTec AD and VisA.
- Real-IAD variants: single-view Real-IAD uses the top view; multi-view Real-IAD uses five views.
- FUIAD construction: fixes testing with 100 normal and 100 anomaly samples per category, then adjusts training normal/anomalous counts by noisy ratio.

## Evidence

### Dataset Scale

| Dataset | Classes | Normal images | Anomaly images | Total images | Multi-view? |
|---|---:|---:|---:|---:|---|
| BTAD | 3 | 952 | 392 | 1,344 | no |
| MVTec AD | 15 | 4,096 | 1,258 | 5,354 | no |
| VisA | 12 | 9,621 | 1,200 | 10,821 | no |
| [[Real-IAD]] | 30 | 99,721 | 51,329 | 151,050 | yes |

### UIAD Benchmark Results

| Dataset / setting | Metric | Mean over methods | Notes |
|---|---|---:|---|
| MVTec AD | I-AUROC | 97.9 +/- 1.2 | Methods are close to saturation. |
| MVTec AD | P-AUPRO | 92.4 +/- 1.8 | Pixel-level localization. |
| VisA | I-AUROC | 91.8 +/- 3.7 | Harder than MVTec. |
| VisA | P-AUPRO | 87.6 +/- 4.2 | Pixel-level localization. |
| Real-IAD single-view | I-AUROC | 87.6 +/- 2.9 | Top-view subset. |
| Real-IAD single-view | P-AUPRO | 90.0 +/- 2.6 | Pixel-level localization. |
| Real-IAD multi-view | S-AUROC | 90.3 +/- 4.0 | Sample-level multi-view metric. |
| Real-IAD multi-view | I-AUROC | 85.0 +/- 3.6 | Image-level multi-view benchmark. |
| Real-IAD multi-view | P-AUPRO | 86.3 +/- 4.4 | Pixel-level localization. |

### FUIAD Benchmark Results

| Setting | Best sample/image-level result visible in source | Notes |
|---|---|---|
| alpha 0.0 | PatchCore 94.4 / 91.3 / 92.6 for S-AUROC / I-AUROC / P-PRO | Clean-training upper bound in FUIAD table. |
| alpha 0.1 | SoftPatch 92.8 / 90.9 / 92.9 | SoftPatch slightly improves robustness over PatchCore in noisy training. |
| alpha 0.2 | SoftPatch 92.2 / 90.5 / 92.9 | Performance degrades with noise for most methods. |
| alpha 0.4 | SoftPatch 90.6 / 89.3 / 92.5 | PatchCore remains relatively robust; many methods degrade substantially. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level and sample-level anomaly detection | Area under ROC curve | higher | yes | Reported as I-AUROC and S-AUROC. |
| [[AU-PRO]] | Pixel-level anomaly localization | Area under per-region overlap curve | higher | yes | Reported as P-AUPRO or P-PRO. |

## Dataset / Benchmark Details

- Source: industrial products across multiple materials.
- Acquisition: five synchronized views, one top and four side cameras at around 45 degrees.
- Annotation: image-level normal/anomalous labels, pixel-level masks, and sample-level grouping across views.
- Availability: public project website and dataset access are reported.
- Leakage risks: not reported.
- Bias / coverage: defects are manually created, so they may not fully capture all naturally occurring production defects.

## Limitations

- The paper reports only some typical methods on Real-IAD.
- Future work includes replicating more methods and adding more settings such as zero-shot, few-shot, and semi-supervised evaluations.
- The large-scale multi-view nature of Real-IAD motivates algorithms designed specifically for multi-view sample aggregation.
- The source does not report random seeds, exact category-level splits, or all implementation hyperparameters beyond following official settings.

## Reproducibility

- Code / website: https://realiad4ad.github.io/Real-IAD.
- Data: Real-IAD dataset reported as available through the project.
- Implementations: several baselines use Anomalib or official code.
- Preprocessing: resize to 256 x 256; PatchCore and PaDiM center-crop to 224 x 224.
- Hardware: not reported.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Unsupervised learning]], [[Unsupervised anomaly detection]], [[Fully unsupervised industrial anomaly detection]]
- Datasets: [[Real-IAD]]
- Benchmarks: [[Real-IAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Relationship Notes

- Shares dataset: [[Real-IAD]].
- Shares method/paradigm: [[Unsupervised anomaly detection]] and [[Fully unsupervised industrial anomaly detection]].
- Shares metric: [[AU-ROC]] and [[AU-PRO]].
- Application/domain: [[Multi-industry anomaly detection]].

## Questions

- Which category-level splits and random seeds should be used for fully reproducible Real-IAD comparisons?
- How should multi-view sample scores be aggregated when different views disagree?
- Do methods designed explicitly for multi-view fusion outperform single-view IAD methods adapted to five-view data?
