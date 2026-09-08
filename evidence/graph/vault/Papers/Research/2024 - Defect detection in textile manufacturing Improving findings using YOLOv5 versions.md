---
title: "Defect detection in textile manufacturing: Improving findings using YOLOv5 versions"
aliases:
  - "Defect detection in textile manufacturing Improving findings using YOLOv5 versions"
paper_key: "sha256:ebeddf097d0c218a1d0d57c90e3c371791d4526a00bb11a31ca7c195bd46c037"
paper_type: research
year: 2024
venue: "not reported"
authors:
  - "Rodolfo Seidel"
  - "Claudio Alberto Waiandt"
  - "Hilario Seibel Junior"
status: processed
processed_at: 2026-06-11
topics:
  - "textile defect detection"
  - "YOLOv5"
  - "data augmentation"
tasks:
  - "[[Textile defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "textile manufacturing defect detection"
datasets:
  - "[[AITEX]]"
dataset_sizes:
  - "AITEX: 245 images originally; adjusted defective-only set has 103 images; prior augmented training set reached 802 samples"
splits:
  - "approximately 65% training / 20% validation / 15% test after defective-only reorganization"
modalities:
  - "fabric images"
methods:
  - "[[YOLOv5]]"
  - "[[Data augmentation]]"
model_family:
  - "object detection"
architectures:
  - "[[YOLOv5]]"
losses:
  - "SIoU localization loss explored"
optimizers: []
training_regime: "transfer learning with pretrained and scratch/frozen variants"
augmentation:
  - "YOLOv5 native augmentation"
  - "mosaic"
  - "mixup"
  - "copy paste"
synthetic_data: "classical detector training augmentation; no generative synthesis reported"
metrics:
  - "[[mAP@0.50-0.95]]"
  - "[[mAP@0.50]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[mAP@0.50-0.95]]"
metric_definitions:
  - "mAP@0.5:0.95 averages precision-recall area across IoU thresholds from 0.5 to 0.95"
baselines:
  - "prior YOLOv5 AITEX study"
  - "YOLOv5s"
  - "baseline AITEX-derived dataset"
benchmarks:
  - "[[AITEX]]"
evaluation_protocol: "compare YOLOv5s and YOLOv5x variants on augmented/rebalanced AITEX-derived bases with transfer-learning settings"
parameters: "not reported"
compute: "Tesla T4, Tesla P100-PCIE, and NVIDIA A100-SXM4 GPUs used in experiments"
hardware: "Tesla T4 15GB; Tesla P100-PCIE 16GB; NVIDIA A100-SXM4 40GB"
training_time: "YOLOv5x about 8h vs YOLOv5s about 3h on Tesla T4 for the same setting"
inference_cost: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2024 - Seidel - Defect detection in textile manufacturing Improving findings using YOLOv5 versions.pdf"
code: "not reported"
data: "AITEX public dataset and augmented AITEX-derived bases"
doi: "not reported"
arxiv: "not applicable"
related_papers:
  - "[[2022 - Data Augmentation Method for Fabric Defect Detection]]"
related_concepts:
  - "[[Data augmentation]]"
related_methods:
  - "[[YOLOv5]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Object detection]]"
related_benchmarks: []
concept_notes_created_or_updated: []
source_file: "paper-inbox/10_processed/Research/2024 - Seidel - Defect detection in textile manufacturing Improving findings using YOLOv5 versions.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Seidel - Defect detection in textile manufacturing Improving findings using YOLOv5 versions.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Seidel - Defect detection in textile manufacturing Improving findings using YOLOv5 versions.txt"
artifact_status: "code not reported; AITEX public"
tags:
  - paper
---

# Defect detection in textile manufacturing: Improving findings using YOLOv5 versions

## Summary

- The paper extends a prior YOLOv5 study on [[AITEX]] fabric defect detection by applying transfer learning, dataset rebalancing, native YOLOv5 augmentation, and YOLOv5x comparisons.
- The best extracted result is YOLOv5x on the "Mista Completa" augmented base, with 60.12% mAP@0.5:0.95, 91.81% precision, 83.82% recall, 87.63% F1-score, and 86.9% mAP@0.5.
- The improvement is not a pure augmentation-only comparison: architecture size, pretrained weights, SIoU, native augmentation, and rebalanced/augmented bases are all entangled.

## Paper Type

- Type: research.
- Why: it reports object-detection experiments and quantitative comparisons on AITEX-derived textile defect data.

## Problem

- Task: localize and classify textile defects with bounding boxes.
- Setting: small and imbalanced public fabric defect dataset with irregular, small defects.
- Inputs: AITEX fabric images and augmented/rebalanced derivatives.
- Outputs: bounding boxes and defect classes.
- Motivation: automate textile manufacturing defect inspection and reduce waste.
- Assumptions: YOLOv5 transfer learning and native augmentation can adapt to small textile defects.

## Contribution

- Claimed: deeper exploration of YOLOv5 variants, transfer learning, native augmentation, and rebalanced AITEX data improves prior findings.
- Shown: YOLOv5x on the Mista Completa base outperforms YOLOv5s in the extracted comparison.
- Inferred: the strongest result depends on a larger model and augmented data; the specific marginal effect of augmentation alone is not isolated.

## Method

- Core idea: reorganize AITEX defective images, train YOLOv5 variants with transfer-learning options and native augmentations, then compare detection metrics.
- Architecture / algorithm: YOLOv5s and YOLOv5x.
- Objective / loss: YOLOv5 detection training with SIoU localization loss explored.
- Optimization: not reported in extracted text.
- Training data: AITEX-derived defective-only base and augmented bases "Mista" and "Mista Completa".
- Data pipeline: remove defect-free images, rebalance classes, augment training data, train with pretrained/frozen/scratch variants.
- Augmentation / synthesis: YOLOv5 native mosaic, mixup, and copy-paste; prior augmented bases include multiple generated training sets.
- Inference: YOLO object detection.
- Complexity / deployment constraints: YOLOv5x improves metrics but costs about 8h training vs 3h for YOLOv5s on Tesla T4.

## ML / DL Extraction

### Task Formulation

- Input modality: textile/fabric image.
- Output target: defect bounding boxes and labels.
- Supervision: supervised object detection.
- Objective: improve textile defect detection on AITEX.

### Model And Training

- Model family: YOLO object detectors.
- Architecture: YOLOv5s and YOLOv5x.
- Parameters: not reported.
- Pretraining: COCO pretrained weights used in selected variants.
- Fine-tuning: yes.
- Losses: SIoU localization loss explored.
- Optimizer: not reported.
- Hyperparameters: 300, 350, and 400 epochs; 1024px and 1280px image resolutions explored.
- Seeds: not reported.
- Training compute: Tesla T4, P100, A100.

### Data

- Datasets: [[AITEX]].
- Data source: AITEX public fabric defect database.
- Dataset size: original AITEX has 245 images; adjusted defective-only set has 103 images; prior augmented training set reached 802 samples.
- Labels / annotations: bounding boxes for defects.
- Splits: approximately 65/20/15 train/validation/test.
- Preprocessing: remove defect-free images; rebalance defective classes; use 1024px and 1280px bases.
- Augmentation: native YOLO mosaic, mixup, copy-paste; augmented bases from prior work.
- Synthetic data: not generative; augmented images from detector training and prior transformations.
- Leakage checks: not reported.
- License: see AITEX note.

### Evaluation

- Protocol: compare YOLOv5s and YOLOv5x on baseline and augmented bases; compare against prior work metrics where available.
- Used performance metrics: mAP@0.5:0.95, mAP@0.5, precision, recall, F1-score.
- Primary metric: mAP@0.5:0.95.
- Metric definitions: mAP@0.5:0.95 averages AP across IoU thresholds from 0.5 to 0.95.
- Metric direction / units: higher is better.
- Baselines: YOLOv5s and prior YOLOv5 AITEX work.
- Benchmarks: AITEX-derived textile defect detection.
- Statistical tests: not reported.
- Failure cases: small-object detection remains challenging; training cost is a constraint for YOLOv5x.

## Evidence

### Experimental Setup

- Datasets: AITEX-derived augmented/rebalanced bases.
- Splits: 65/20/15 approximate after reorganization.
- Baselines: YOLOv5s and prior AITEX YOLOv5 study.
- Used performance metrics: mAP@0.5:0.95, mAP@0.5, precision, recall, F1.
- Compute: multiple GPUs.
- Hardware: Tesla T4, Tesla P100-PCIE, A100-SXM4.
- Training time: YOLOv5x about 8h vs YOLOv5s about 3h on Tesla T4.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| YOLOv5x on Mista Completa | AITEX textile defect detection | mAP@0.5:0.95 | higher | YOLOv5s lower by 2.96 points in same scenario | 60.12% | Best extracted primary result. |
| YOLOv5x on Mista Completa | AITEX textile defect detection | Precision | higher | YOLOv5s lower by 2.39 points | 91.81% | Best extracted precision. |
| YOLOv5x on Mista Completa | AITEX textile defect detection | Recall | higher | YOLOv5s lower by 5.22 points | 83.82% | Still below some non-YOLO related work. |
| YOLOv5x on Mista Completa | AITEX textile defect detection | F1-score | higher | related work [17] 82.58% | 87.63% | Extracted comparison. |
| YOLOv5x on Mista Completa | AITEX textile defect detection | mAP@0.5 | higher | related work [19] 71.7% | 86.9% | Extracted comparison. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP@0.50-0.95]] | object detection | AP averaged across IoU thresholds 0.5 to 0.95 | higher | yes | Main metric. |
| [[mAP@0.50]] | object detection | AP at IoU 0.5 | higher | no | Reported in comparison. |
| [[Precision]] | object detection | correct detections among predictions | higher | no | 91.81% best extracted value. |
| [[Recall]] | object detection | detected objects among ground-truth objects | higher | no | 83.82% best extracted value. |
| [[F1-score]] | object detection summary | harmonic mean of precision and recall | higher | no | 87.63% best extracted value. |

### Ablations

- YOLOv5s vs YOLOv5x compares model size.
- Pretrained, scratch, and frozen-backbone variants compare transfer-learning setup.
- Native augmentation on/off is discussed, but exact numeric graph values are not extracted.
- Mista vs Mista Completa compares augmented base composition.

## Dataset / Benchmark Details

- Source: [[AITEX]].
- Collection: factory textile images.
- Annotation: bounding boxes in the derivative experiments.
- Size: original 245 images; adjusted defective-only base 103 images.
- Splits: approximately 65/20/15.
- Modalities: fabric images.
- License: see dataset note.
- Leakage risks: not reported.
- Bias / coverage: all defect-free images are removed for the adjusted defective-only object-detection setup.
- Maintenance: not reported.

## Limitations

- Stated: YOLOv5x is viable mainly when training time and hardware are not restrictive.
- Stated: source code/datasets from related works were unavailable, preventing unified metric comparison.
- Inferred: augmentation effects are entangled with transfer learning, model scale, rebalancing, and loss changes.

## Reproducibility

- Code: not reported.
- Data: AITEX public; derivative bases from prior work are referenced.
- Hyperparameters: epochs and image resolutions partially reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: partially reported.
- Artifact status: partial.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Object detection]].
- Methods: [[YOLOv5]], [[Data augmentation]].
- Optimizers: not reported.
- Datasets: [[AITEX]].
- Benchmarks: AITEX-derived object detection setup.
- Domains: [[Textile and fiber inspection]].
- Metrics: [[mAP@0.50-0.95]], [[mAP@0.50]], [[Precision]], [[Recall]], [[F1-score]].
- Concepts: transfer learning, native detector augmentation, small-object detection.
- Dataset-domain links: [[AITEX]] is associated with [[Textile and fiber inspection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Data Augmentation Method for Fabric Defect Detection]] | Shares task / shares method | Both address fabric defect detection with data augmentation. |

### Backlinks Updated

- Pending graph audit.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| not applicable | not applicable | Existing AITEX, YOLOv5, augmentation, task, and metric nodes cover central graph links. |

## Questions

- Venue and year are not explicit in the extracted title-page metadata; year is inferred from the source filename/date and nearby bibliography context, not a DOI.
- Exact native augmentation on/off graph values require manual figure inspection.
