---
title: "Patch-Wise Augmentation for Anomaly Detection and Localization"
aliases:
  - "Patch-Wise Augmentation for Anomaly Detection and Localization"
paper_key: "doi:10.1109/icassp48485.2024.10446994"
paper_type: research
year: 2024
venue: "ICASSP 2024"
authors:
  - "Yiwen Ding"
  - "Lei Fan"
  - "Maurice Pagnucco"
  - "Yang Song"
status: processed
processed_at: 2026-06-12
topics:
  - "patch-wise anomaly augmentation"
  - "self-supervised anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
methods:
  - "[[PatchAnomaly]]"
  - "[[Data augmentation]]"
  - "[[Defect synthesis]]"
model_family:
  - "reconstruction-detection anomaly model"
architectures:
  - "reconstruction network"
  - "detection network"
losses:
  - "composition loss"
  - "category loss"
optimizers:
  - "not reported"
training_regime: "self-supervised training with synthetic patch anomalies"
augmentation:
  - "[[PatchAnomaly]]"
synthetic_data: "multi-scale normal-image patches transformed with rotation, jigsaw, context inpainting, sub-patch transforms, and blending"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
metric_definitions: []
baselines:
  - "DRAEM"
  - "PMAD"
  - "P-SVDD"
  - "CFLOW"
benchmarks:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
evaluation_protocol: "image-level and pixel-level AUROC on MVTec AD and BTAD"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2024 - Ding - Patch-Wise Augmentation for Anomaly Detection and Localization.pdf"
code: "not reported"
data: "not reported"
doi: "10.1109/icassp48485.2024.10446994"
arxiv: "not reported"
related_papers:
  - "[[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]]"
  - "[[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]]"
related_concepts:
  - "[[Self-supervised learning]]"
related_methods:
  - "[[PatchAnomaly]]"
  - "[[Defect synthesis]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
concept_notes_created_or_updated:
  - "[[PatchAnomaly]]"
source_file: "paper-inbox/10_processed/Research/2024 - Ding - Patch-Wise Augmentation for Anomaly Detection and Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Ding - Patch-Wise Augmentation for Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Ding - Patch-Wise Augmentation for Anomaly Detection and Localization.txt"
artifact_status: "not reported"
tags:
  - paper
---

# Patch-Wise Augmentation for Anomaly Detection and Localization

## Summary

The paper formulates unsupervised visual anomaly detection as supervised object detection by creating synthetic anomaly labels from normal images. [[PatchAnomaly]] selects multiple local patches, applies self-supervised transformations, blends them into the source image, and trains a reconstruction-detection model to localize the resulting pseudo anomalies. The strongest reported average results are 98.4% image-level AUROC and 97.0% pixel-level AUROC on [[MVTec AD]], and 95.5% image-level AUROC and 97.4% pixel-level AUROC on [[BTAD]].

## Paper Type

- Type: research.
- Why: It proposes a new augmentation method and anomaly localization model, then evaluates against anomaly-detection baselines.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: unsupervised anomaly detection where only normal images are available for training.
- Inputs: normal industrial inspection images.
- Outputs: anomaly scores and localized anomaly regions.
- Motivation: reconstruction-only anomaly detectors often require hand-crafted post-processing, while synthetic supervision can train direct localization.
- Assumptions: synthetic patch anomalies should preserve most normal-image content because many industrial defects are fine-grained and local.

## Contribution

- Claimed: [[PatchAnomaly]] synthesizes anomaly-like samples through multi-scale patch selection, sub-patch transformations, self-supervised transformations, and image blending.
- Claimed: unsupervised anomaly detection is converted into supervised object detection using generated patch labels.
- Shown: the reconstruction-detection model reaches competitive AUROC on [[MVTec AD]] and [[BTAD]].

## Method

- Core idea: synthesize local patch anomalies from normal images, then train a model to reconstruct and detect those local regions.
- Architecture / algorithm: PatchAnomaly plus a reconstruction network and a detection network akin to an object detector.
- Objective / loss: composition loss and category loss are reported; full objective details are not reported in the extracted text.
- Optimization: not reported.
- Training data: normal training images from [[MVTec AD]] and [[BTAD]].
- Data pipeline: choose several multi-scale patches, split each into sub-patches, apply transforms such as rotation, jigsaw, or context inpainting, and blend the transformed patches back into the image.
- Augmentation / synthesis: patch-wise synthetic anomaly generation with labels.
- Inference: the trained model directly localizes anomalous regions, avoiding complex hand-crafted post-processing.
- Complexity / deployment constraints: not reported.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]] and [[BTAD]].
- Splits: MVTec AD has 3629 training and 1725 test images; BTAD has 1799 training images.
- Baselines: P-SVDD, CFLOW, PMAD, DRAEM, and other reconstruction / augmentation methods.
- Used performance metrics: image-level AUROC and pixel-level AUROC.
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Full model | MVTec AD | image-level AUROC | higher | source baseline value absent | 98.4% | Average over categories. |
| Full model | MVTec AD | pixel-level AUROC | higher | source baseline value absent | 97.0% | Average over categories. |
| Full model | BTAD | image-level AUROC | higher | DRAEM 94.4% | 95.5% | Table 2. |
| Full model | BTAD | pixel-level AUROC | higher | PMAD 97.4% | 97.4% | Ties PMAD in Table 2. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level anomaly detection | area under ROC curve, percent | higher | yes | Reported on MVTec AD and BTAD. |
| [[AU-ROC]] | pixel-level anomaly localization | area under ROC curve, percent | higher | yes | Reported on MVTec AD and BTAD. |

### Ablations

- Removing sub-patch transformations decreased performance by about 2.6% on average.
- Combining rotation, jigsaw, and context transformations improved textures by about 2.7% and objects by about 0.9% relative to single transformation variants.
- Image blending added about 0.5% improvement.
- The best patch count in the reported sweep was T = 4, and patch ratios in [0.05, 0.4] worked best.
- The final framework ablation improved from 81.2/68.9 image-/pixel-level AUROC without the reconstruction network to 98.4/97.0 with the full model.

## ML / DL Extraction

### Data

- Datasets: [[MVTec AD]], [[BTAD]].
- Dataset size: MVTec AD reports 3629 training and 1725 test images; BTAD reports 1799 training images.
- Labels / annotations: anomaly masks are used for evaluation; synthetic patch boxes provide training supervision.
- Splits: standard benchmark splits, exact split construction not further reported.
- Augmentation: [[PatchAnomaly]].
- Synthetic data: transformed and blended normal-image patches.
- Leakage checks: not reported.

### Evaluation

- Protocol: image-level and pixel-level AUROC.
- Metric direction / units: higher AUROC is better.
- Failure cases: not reported.

## Limitations

- Stated: not reported.
- Inferred: the synthetic anomaly distribution may still mismatch real logical anomalies or anomalies that are not local patch-like perturbations.

## Reproducibility

- Code: not reported.
- Data: public benchmarks.
- Hyperparameters: T and patch-ratio sweeps are reported; full training recipe is not reported.
- Random seeds: not reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[PatchAnomaly]], [[Defect synthesis]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[BTAD]]
- Benchmarks: [[MVTec AD]], [[BTAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]]

### Shares Dataset

- [[MVTec AD]] and [[BTAD]]: used for image-level and pixel-level AUROC evaluation.

### Shares Method

- [[Defect synthesis]]: synthetic pseudo-defects provide supervision.
- [[Data augmentation]]: patch-wise augmentation is the training-signal mechanism.
- [[PatchAnomaly]]: central method introduced by the paper.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]]: the model detects and localizes defects from industrial images.

## Questions

- How stable is PatchAnomaly across logical defects where local visual perturbations are not sufficient?
- Does direct detection remain competitive when compared against newer memory-bank or foundation-feature methods on VisA or Real-IAD?
