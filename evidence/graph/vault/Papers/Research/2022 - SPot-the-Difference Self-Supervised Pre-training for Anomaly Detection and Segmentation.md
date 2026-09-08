---
title: "SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation"
aliases:
  - "SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation"
  - "SPD"
paper_key: "arxiv:2207.14315"
paper_type: research
year: 2022
venue: "arXiv"
authors:
  - "Yang Zou"
  - "Jongheon Jeong"
  - "Latha Pemula"
  - "Dongqing Zhang"
  - "Onkar Dabeer"
status: processed
processed_at: 2026-05-22
topics:
  - self-supervised pre-training
  - industrial anomaly detection
  - anomaly segmentation
  - industrial anomaly dataset
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
application_area: "Industrial visual anomaly detection and segmentation across multiple object categories"
datasets:
  - "[[VisA]]"
  - "[[MVTec AD]]"
  - "[[ImageNet]]"
dataset_sizes:
  - "VisA: 10,821 high-resolution RGB images; 9,621 normal and 1,200 anomalous"
  - "MVTec AD: 5,354 images"
  - "ImageNet 2012: 1,000 classes and 1.28 million training images"
splits:
  - "VisA 1-class: 90% normal images for training; 10% normal plus all anomalous images for testing"
  - "VisA 2-class high-shot: 60% train and 40% test for normal and anomalous images"
  - "VisA 2-class low-shot: 20%/80% train/test pool, then k=5 or k=10 samples from both classes for training; average over 5 random runs"
modalities:
  - RGB image
  - pixel-level anomaly mask
methods:
  - "[[Self-supervised learning]]"
  - "[[SmoothBlend]]"
  - "[[Data augmentation]]"
model_family:
  - contrastive self-supervised pre-training
  - supervised ImageNet pre-training
  - anomaly detection
  - anomaly segmentation
architectures:
  - "ResNet-50"
  - "Wide ResNet-50"
  - "ResNet-18"
  - "U-Net with ResNet-50 encoder"
losses:
  - "InfoNCE for SimCLR/MoCo-style baselines"
  - "cosine-distance positive-pair loss for SimSiam-style baselines"
  - "SPD loss: cosine similarity to local-perturbation negative minus cosine similarity to weak-global positive"
  - "cross-entropy for supervised SPD auxiliary classifier"
  - "focal loss for 2-class U-Net segmentation"
training_regime: "Regularize ImageNet supervised or contrastive self-supervised pre-training with SPD, then evaluate transfer to 1-class and 2-class anomaly detection/segmentation"
augmentation:
  - "SmoothBlend local perturbation from a color-jittered patch pasted through a Gaussian-blurred alpha mask"
  - "weak random cropping"
  - "Gaussian blurring"
  - "horizontal flipping"
  - "color jittering"
synthetic_data: "SPD creates synthetic local spot-the-difference perturbations for pre-training, but the downstream anomalies in VisA and MVTec AD are real or manually generated dataset defects as reported by the paper."
metrics:
  - "[[AU-PR]]"
  - "[[AU-ROC]]"
primary_metric: "[[AU-PR]]"
metric_definitions:
  - "AU-PR: area under the precision-recall curve; emphasized because anomaly data and anomaly pixels are imbalanced"
  - "AU-ROC: area under the receiver operating characteristic curve; reported with AU-PR but described as potentially inflated for imbalanced anomaly tasks"
baselines:
  - "supervised ImageNet pre-training"
  - "SimSiam"
  - "MoCo"
  - "SimCLR"
  - "PaDiM"
  - "PatchCore"
benchmarks:
  - "[[VisA]]"
  - "[[MVTec AD]]"
evaluation_protocol: "Evaluate ImageNet pre-training variants on 1-class anomaly detection/segmentation with PaDiM or PatchCore, 2-class high-shot VisA classification and segmentation, and 2-class 5/10-shot VisA classification and segmentation."
parameters: "ResNet-50 is the main backbone; SPD loss weight eta=0.1 is selected as the default in ablations."
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "http://arxiv.org/abs/2207.14315"
pdf: "paper-inbox/10_processed/Research/2022 - Zou - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation.pdf"
code: "http://github.com/amazon-research/spot-diff"
data: "VisA is reported as released by the paper."
doi: "not reported"
arxiv: "2207.14315"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Self-supervised learning]]"
  - "[[SmoothBlend]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[VisA]]"
  - "[[MVTec AD]]"
  - "[[ImageNet]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[VisA]]"
  - "[[MVTec AD]]"
concept_notes_created_or_updated:
  - "[[SmoothBlend]]"
source_file: "paper-inbox/10_processed/Research/2022 - Zou - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Zou - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Zou - SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation

## Summary

- Zou et al. introduce SPot-the-Difference (SPD), a regularization method for ImageNet pre-training that makes representations more sensitive to subtle local differences needed for industrial anomaly detection and segmentation.
- The paper also introduces the Visual Anomaly (VisA) dataset with 12 objects across three domains, image-level labels, and pixel-level anomaly masks.
- Experiments on VisA and MVTec AD show that SPD improves SimSiam, MoCo, SimCLR, and supervised ImageNet pre-training in many anomaly detection and segmentation settings, with AU-PR emphasized over AU-ROC for imbalanced anomaly data.

## Paper Type

- Type: research.
- Why: The paper proposes a pre-training regularizer and a new industrial anomaly dataset, then evaluates transfer performance across multiple anomaly detection and segmentation protocols.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: Multi-object industrial quality inspection where defects are rare, small, and locally defined.
- Inputs: ImageNet images for pre-training and industrial inspection images from [[VisA]] and [[MVTec AD]] for downstream evaluation.
- Outputs: Image-level anomaly scores/classes and pixel-level anomaly segmentation maps.
- Motivation: Standard self-supervised pre-training learns invariance to global augmentations, while surface anomaly inspection often depends on small local texture or structural deviations.
- Assumptions: Pre-training can be changed to preserve local sensitivity before downstream anomaly models are trained or evaluated.

## Contribution

- Claimed: SPD regularizes supervised and contrastive self-supervised ImageNet pre-training by contrasting weak global positives against local perturbation negatives.
- Claimed: VisA provides a larger and more challenging public industrial anomaly dataset than MVTec AD, including complex PCB structures, multiple instances, object pose/location variation, and pixel-level labels.
- Shown: SPD improves AU-PR for anomaly detection and segmentation across many ImageNet pre-training baselines and downstream settings, including 2-class high-shot segmentation gains of +5.9 points over SimSiam and +6.8 points over supervised pre-training.

## Method

- Core idea: Treat local perturbations as negatives and weak global augmentations as positives during pre-training so features become invariant to small global changes but sensitive to anomalous local changes.
- Architecture / algorithm: SPD uses a shared feature extractor and MLP projection head for contrastive variants; supervised SPD adds an auxiliary classifier on top of a ResNet-50 feature layer to classify whether an SPD-augmented image has a local perturbation.
- Objective / loss: SPD minimizes cosine similarity between the anchor and local-perturbation negative while maximizing cosine similarity between the anchor and weak-global positive. For SimCLR/MoCo, SPD is added to InfoNCE; for SimSiam, the SSL positive-pair loss is combined with SPD.
- Optimization: Specific optimizer settings are not reported in the analysis input; the paper states that the same hyperparameters are used across SimSiam, MoCo, SimCLR, and supervised pre-training.
- Training data: ImageNet 2012 for pre-training; VisA and MVTec AD for downstream anomaly evaluation.
- Data pipeline: Generate an anchor image, an SPD negative using weak global augmentation followed by SmoothBlend, and an SPD positive using weak global transformations only.
- Augmentation / synthesis: [[SmoothBlend]] creates a local deformation by color-jittering a cut patch from the same image, pasting it at a random location, and blending it through a Gaussian-blurred alpha mask.
- Inference: SPD is a pre-training regularizer; downstream inference uses PaDiM, PatchCore, a binary ResNet, or U-Net depending on the evaluation protocol.
- Complexity / deployment constraints: Requires ImageNet pre-training and downstream model training/evaluation; compute and training time are not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB images.
- Output target: Image-level anomaly classification and pixel-level anomaly segmentation.
- Supervision: Self-supervised or supervised pre-training, followed by 1-class or 2-class downstream anomaly training.
- Objective: Improve transfer representations for local defect sensitivity under scarce or imbalanced anomaly data.

### Model And Training

- Model family: Contrastive self-supervised representation learning and supervised transfer learning.
- Architecture: ResNet-50 is the main backbone; Wide ResNet-50 is used for PatchCore and one ablation; ResNet-18 and ResNet-50 are used for ImageNet classification extension; U-Net with ResNet-50 encoder is used for 2-class segmentation.
- Parameters: not reported.
- Pretraining: ImageNet supervised pre-training, SimSiam, MoCo, and SimCLR with and without SPD.
- Fine-tuning: 2-class anomaly classification uses a standard binary ResNet; 2-class segmentation uses U-Net with ResNet-50 encoder.
- Losses: InfoNCE, SimSiam cosine-distance loss, SPD cosine loss, supervised auxiliary cross-entropy, and focal loss for 2-class U-Net segmentation.
- Optimizer: not reported.
- Hyperparameters: SPD loss weight eta=0.1 is selected as the default after ablation.
- Seeds: not reported; low-shot results average five random runs.
- Training compute: not reported.

### Data

- Datasets: [[ImageNet]], [[VisA]], [[MVTec AD]].
- Data source: VisA is collected by the authors; MVTec AD and ImageNet are used as existing datasets.
- Dataset size: VisA has 10,821 RGB images, with 9,621 normal and 1,200 anomalous samples; MVTec AD has 5,354 images; ImageNet has 1.28 million training images across 1,000 classes.
- Labels / annotations: VisA provides image-level and pixel-level labels; MVTec AD labels are used for anomaly detection and segmentation evaluation.
- Splits: VisA includes 1-class, 2-class high-shot, and 2-class 5/10-shot protocols.
- Preprocessing: not reported beyond the protocol and augmentation descriptions.
- Augmentation: SmoothBlend local deformation plus weak global augmentations for SPD; standard strong global augmentations for contrastive baselines.
- Synthetic data: SmoothBlend creates synthetic local perturbations for pre-training.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: 1-class PaDiM/PatchCore evaluation on VisA and MVTec AD; 2-class high-shot VisA classification/segmentation; 2-class 5-shot and 10-shot VisA classification/segmentation.
- Used performance metrics: [[AU-PR]] and [[AU-ROC]].
- Primary metric: [[AU-PR]].
- Metric definitions: AU-PR and AU-ROC are curve areas; the paper argues AU-PR is more informative for imbalanced anomaly tasks.
- Metric direction / units: higher is better.
- Baselines: supervised ImageNet pre-training, SimSiam, MoCo, SimCLR, PaDiM, PatchCore, binary ResNet, and U-Net.
- Benchmarks: [[VisA]] and [[MVTec AD]].
- Statistical tests: not reported.
- Failure cases: AU-ROC can saturate or inflate apparent performance on imbalanced anomaly segmentation, while AU-PR shows remaining difficulty.

## Evidence

### Experimental Setup

- Datasets: [[VisA]], [[MVTec AD]], and [[ImageNet]].
- Splits: VisA 1-class, 2-class high-shot, 2-class 5-shot, and 2-class 10-shot protocols.
- Baselines: supervised ImageNet, SimSiam, MoCo, SimCLR, PaDiM, PatchCore, binary ResNet, and U-Net.
- Used performance metrics: [[AU-PR]] and [[AU-ROC]].
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| SimSiam+SPD improves 1-class classification | VisA / PaDiM classification | AU-PR | higher | 80.2 | 82.8 | ResNet-50 ImageNet pre-training |
| Supervised+SPD improves 1-class segmentation | VisA / PaDiM segmentation | AU-PR | higher | 11.4 | 12.0 | Supervised ImageNet baseline |
| SimSiam+SPD improves 2-class high-shot segmentation | VisA / U-Net segmentation | AU-PR | higher | 53.8 | 59.7 | +5.9 points |
| Supervised+SPD improves 2-class high-shot segmentation | VisA / U-Net segmentation | AU-PR | higher | 65.1 | 71.9 | +6.8 points |
| Supervised+SPD improves 2-class high-shot classification | VisA / binary ResNet classification | AU-PR | higher | 97.5 | 98.3 | AU-ROC also improves from 99.5 to 99.7 |
| SimSiam+SPD improves 5-shot classification | VisA / binary ResNet classification | AU-PR | higher | 51.9 | 56.1 | Low-shot evaluation averaged over five runs |
| MoCo+SPD improves 10-shot segmentation | VisA / U-Net segmentation | AU-PR | higher | 32.3 | 32.8 | MoCo+SPD is reported as best in few-shot segmentation |
| Supervised+SPD improves PatchCore segmentation | VisA / PatchCore segmentation | AU-PR | higher | 38.4 | 39.3 | Wide ResNet-50 backbone |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-PR]] | Anomaly classification and segmentation | Area under precision-recall curve | higher | yes | Preferred because anomalies and anomalous pixels are imbalanced |
| [[AU-ROC]] | Anomaly classification and segmentation | Area under receiver operating characteristic curve | higher | no | Reported with AU-PR; paper warns it may inflate performance under class imbalance |

### Ablations

- SPD loss weight eta=0.1 gives the best reported overall performance among eta=0.1, 0.5, and 1.0 in the SimSiam/PaDiM ablation.
- SmoothBlend with SPD loss outperforms CutPaste-style perturbations and a cross-entropy alternative in the reported ablation.
- SPD still improves SimSiam when Wide ResNet-50 replaces ResNet-50.
- PatchCore evaluation shows SPD can improve supervised pre-training on VisA segmentation AU-PR and MVTec AD segmentation AU-PR.

## Dataset / Benchmark Details

- Source: VisA is introduced by this paper; MVTec AD is used as an existing benchmark.
- Collection: VisA images are acquired with a 4000 x 6000 high-resolution RGB sensor.
- Annotation: VisA provides image-level and pixel-level anomaly labels.
- Size: VisA contains 12 object subsets: PCB1-4, Capsules, Candle, Macaroni1, Macaroni2, Cashew, Chewing gum, Fryum, and Pipe fryum.
- Splits: VisA defines 1-class, 2-class high-shot, and 2-class 5/10-shot protocols.
- Modalities: RGB industrial inspection imagery.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: VisA covers complex structures, multiple instances, single instances, object pose/location variation, and 5-20 images per defect type.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Bridging the performance gap between 1-class and 2-class VisA settings remains an open challenge; extending SPD to fine-grained classification, small object detection, and downstream 1-class anomaly training is proposed as future work.
- Inferred: Hardware, optimizer details, full training time, and dataset licensing are not reported in the analysis input.

## Reproducibility

- Code: http://github.com/amazon-research/spot-diff.
- Data: VisA is reported as released by the paper.
- Hyperparameters: SPD eta=0.1 is reported as default; many implementation details are deferred to supplementary material.
- Random seeds: not reported; low-shot averages over five random runs.
- Environment: not reported.
- Checkpoints / models: not reported in the analysis input.
- Exact preprocessing: SPD augmentation details are reported; downstream image preprocessing details are not reported.
- Artifact status: Code and VisA release are reported.

## Systems Details

- Hardware / software stack: not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: not reported.
- Deployment assumptions: SPD requires a pre-training stage before downstream anomaly evaluation.
- Cost: not reported.
- Failure modes: Standard AU-ROC can obscure weak anomaly segmentation performance under extreme pixel imbalance.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Self-supervised learning]], [[SmoothBlend]], [[Data augmentation]]
- Datasets: [[VisA]], [[MVTec AD]], [[ImageNet]]
- Benchmarks: [[VisA]], [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-PR]], [[AU-ROC]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] | Shares setting | Both evaluate self-supervised or pretrained representations for industrial anomaly detection. |
| [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] | Shares method family | Both use synthetic local perturbations to improve anomaly-oriented self-supervision, though SPD regularizes ImageNet pre-training. |

### Backlinks Updated

- [[VisA]] links this paper as its introducing and benchmark paper.
- [[MVTec AD]] links this paper as a benchmark comparison.
- [[SmoothBlend]] links this paper as the source method.
- [[Multi-industry anomaly detection]] links this paper as a multi-object industrial anomaly benchmark and method study.
- [[AU-PR]] and [[AU-ROC]] link this paper for anomaly detection and segmentation evaluation.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[SmoothBlend]] | Created | SPD method section |
| [[VisA]] | Updated | VisA dataset section |
| [[Multi-industry anomaly detection]] | Updated | VisA benchmark scope |

## Questions

- How much of SPD's benefit comes from ImageNet-scale pre-training versus the specific local perturbation objective?
- How sensitive are downstream results to defect type, object subset, and low-shot sampling seed?
- What license and long-term maintenance model apply to VisA and the released code?
