---
title: "Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization"
aliases:
  - "Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization"
paper_key: "doi:10.1007/s11263-022-01578-9"
paper_type: dataset
year: 2022
venue: "International Journal of Computer Vision"
authors:
  - "Paul Bergmann"
  - "Kilian Batzner"
  - "Michael Fauser"
  - "David Sattlegger"
  - "Carsten Steger"
status: processed
processed_at: 2026-05-22
topics:
  - "logical anomalies"
  - "structural anomalies"
  - "unsupervised anomaly localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec LOCO AD]]"
methods:
  - "[[Global Context Anomaly Detection]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Unsupervised learning]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures:
  - "local feature-regression branch"
  - "global bottleneck branch"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
  - "[[Area Under Saturated Per-Region Overlap]]"
primary_metric: "[[Area Under Saturated Per-Region Overlap]]"
metric_definitions:
  - "AUsPRO: normalized area under the saturated per-region overlap curve up to average false positive rate per pixel of 5%."
  - "AUROC: image-level classification metric reported separately for structural and logical anomalies."
baselines:
  - "Variation Model"
  - "f-AnoGAN"
  - "MNAD"
  - "AE"
  - "VAE"
  - "SPADE"
  - "Student-Teacher"
benchmarks:
  - "[[MVTec LOCO AD]]"
  - "[[MVTec AD]]"
code: "reported available at MVTec dataset page"
data: "reported available at MVTec dataset page"
doi: "10.1007/s11263-022-01578-9"
arxiv: "not reported"
url: "https://doi.org/10.1007/s11263-022-01578-9"
pdf: "not reported"
related_concepts:
  - "[[Logical anomalies]]"
  - "[[Structural anomalies]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Global Context Anomaly Detection]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
related_datasets:
  - "[[MVTec LOCO AD]]"
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec LOCO AD]]"
  - "[[MVTec AD]]"
source_file: "paper-inbox/00_incoming/s11263-022-01578-9.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Bergmann - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Bergmann - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization.txt"
artifact_status: "dataset and evaluation code reported available"
tags:
  - paper
---
# Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization

## Summary

Bergmann et al. introduce [[MVTec LOCO AD]], a five-category industrial anomaly dataset designed to balance [[Structural anomalies]] and [[Logical anomalies]]. The paper argues that existing benchmarks such as [[MVTec AD]] are heavily biased toward local structural defects, while many industrial inspection failures require recognizing violated object, position, fill-level, count, or wiring constraints.

The paper also introduces [[Area Under Saturated Per-Region Overlap]], a localization metric that handles ambiguous logical-anomaly masks, and proposes [[Global Context Anomaly Detection]] (GCAD), a two-branch unsupervised method. GCAD combines a local feature-regression branch for structural anomalies with a global bottleneck branch for long-range logical constraints, achieving the best mean MVTec LOCO AD localization score in the reported experiments.

## Paper Type

- Type: dataset.
- Why: The main contribution is a public benchmark dataset with pixel-precise annotations, a benchmark metric, and baseline evaluations; the paper also contributes a new method.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: industrial inspection scenes where anomalies may be local visual defects or violations of logical/geometric constraints.
- Inputs: object-category images from breakfast box, screw bag, pushpins, splicing connectors, and juice bottle inspection scenarios.
- Outputs: image-level anomaly classification and pixel-level anomaly localization maps.
- Motivation: datasets biased toward dents, scratches, contaminations, and other local defects do not measure whether methods can recognize invalid object counts, missing components, misplaced objects, or inconsistent combinations.
- Assumptions: training and validation images are anomaly-free; test images include anomaly-free, structural-anomaly, and logical-anomaly cases.

## Contribution

- Claimed: defines structural anomalies as novel local visual structures and logical anomalies as violations of underlying logical constraints that can require long-range dependency modeling.
- Claimed: introduces [[MVTec LOCO AD]], with 3,644 images across five industrial-style object categories and pixel-precise ground truth for each anomalous region.
- Claimed: introduces [[Area Under Saturated Per-Region Overlap]], a generalization of PRO that accounts for localization ambiguity in logical anomalies.
- Shown: GCAD improves joint structural/logical anomaly localization on MVTec LOCO AD over Variation Model, f-AnoGAN, MNAD, AE, VAE, SPADE, and Student-Teacher baselines.

## Method

GCAD has a local branch and a global branch. The local branch uses an ImageNet-pretrained local feature encoder and a regression network; large local regression errors indicate novel structures. The global branch uses an encoder with a low-dimensional bottleneck to learn globally consistent training-data representations and a high-capacity regression network; disagreement between the encoder and regressor highlights violations of global constraints.

The local branch is intended to detect [[Structural anomalies]], while the global branch is intended to detect [[Logical anomalies]]. During inference, the paper normalizes local and global anomaly maps on anomaly-free validation images and combines them. Multiple receptive field sizes are trained and averaged for multi-scale anomaly detection.

## Evidence

### Dataset / Benchmark Setup

- Dataset: [[MVTec LOCO AD]].
- Categories: Breakfast Box, Screw Bag, Pushpins, Splicing Connectors, and Juice Bottle.
- Total images: 3,644.
- Training images: 1,772 anomaly-free images.
- Validation images: 304 anomaly-free images.
- Test images: 575 anomaly-free images, 432 structural-anomaly images, and 561 logical-anomaly images.
- Defect types: 89.
- Annotations: pixel-precise ground-truth annotations for all anomalies.
- Availability: dataset and evaluation code are reported publicly available at the MVTec research datasets page.

### Dataset Statistics

| Category | Train | Validation | Test anomaly-free | Test structural | Test logical | Defect types | Width | Height |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Breakfast Box | 351 | 62 | 102 | 90 | 83 | 22 | 1600 | 1280 |
| Screw Bag | 360 | 60 | 122 | 82 | 137 | 20 | 1600 | 1100 |
| Pushpins | 372 | 69 | 138 | 81 | 91 | 8 | 1700 | 1000 |
| Splicing Connectors | 354 | 59 | 119 | 85 | 108 | 21 | 1700 | 850 |
| Juice Bottle | 335 | 54 | 94 | 94 | 142 | 18 | 800 | 1600 |
| Total | 1772 | 304 | 575 | 432 | 561 | 89 | not applicable | not applicable |

### Logical Constraints By Category

- Breakfast Box: exactly two tangerines and one nectarine on the left; fixed ratio and relative position of cereals and banana chips/almonds on the right.
- Screw Bag: exactly two washers, two nuts, one long screw, and one short screw.
- Pushpins: exactly one pushpin per box compartment.
- Splicing Connectors: exactly two matching splicing connectors linked by exactly one cable; clamp count, cable color, termination position, and mirror symmetry are constrained.
- Juice Bottle: one of three liquid colors, two labels, matching icon/liquid type, label positions, and fixed fill level.

### Evaluation Protocol

- Localization metric: normalized area under the sPRO curve up to average false positive rate per pixel of 5%.
- Image-level metric: [[AU-ROC]].
- Test split for analysis: structural anomaly test images and logical anomaly test images are evaluated separately, with anomaly-free test images included in both subsets.
- GCAD training: input images resized to 256 x 256; Adam optimizer with learning rate 1e-4 and weight decay 1e-5; 500 epochs; global context vector size g = 32; global feature depth 10; local feature depth 128; receptive fields 17 and 33.
- Baselines: Variation Model, f-AnoGAN, MNAD, AE, VAE, SPADE, and Student-Teacher.

### Main Localization Results

| Method | Breakfast Box | Screw Bag | Pushpins | Splicing Connectors | Juice Bottle | Mean |
|---|---:|---:|---:|---:|---:|---:|
| Variation Model | 0.168 | 0.253 | 0.254 | 0.125 | 0.325 | 0.225 |
| f-AnoGAN | 0.223 | 0.348 | 0.336 | 0.195 | 0.569 | 0.334 |
| MNAD | 0.080 | 0.344 | 0.357 | 0.442 | 0.472 | 0.339 |
| AE | 0.189 | 0.289 | 0.327 | 0.479 | 0.605 | 0.378 |
| VAE | 0.165 | 0.302 | 0.311 | 0.496 | 0.636 | 0.382 |
| SPADE | 0.372 | 0.331 | 0.234 | 0.516 | 0.804 | 0.451 |
| Student-Teacher | 0.496 | 0.602 | 0.523 | 0.698 | 0.811 | 0.626 |
| GCAD | 0.502 | 0.558 | 0.739 | 0.798 | 0.910 | 0.701 |

### Structural Versus Logical Localization

| Method | Structural sPRO AUC | Logical sPRO AUC | Mean |
|---|---:|---:|---:|
| Variation Model | 0.124 | 0.325 | 0.225 |
| f-AnoGAN | 0.209 | 0.460 | 0.334 |
| MNAD | 0.412 | 0.266 | 0.339 |
| AE | 0.296 | 0.460 | 0.378 |
| VAE | 0.305 | 0.459 | 0.382 |
| SPADE | 0.368 | 0.536 | 0.451 |
| Student-Teacher | 0.756 | 0.497 | 0.626 |
| GCAD | 0.692 | 0.711 | 0.701 |

### Image-Level AUROC

| Method | Structural anomalies | Logical anomalies | Mean |
|---|---:|---:|---:|
| VAE | 0.548 | 0.538 | 0.543 |
| AE | 0.565 | 0.581 | 0.573 |
| Variation Model | 0.589 | 0.565 | 0.577 |
| f-AnoGAN | 0.627 | 0.658 | 0.642 |
| MNAD | 0.702 | 0.600 | 0.651 |
| SPADE | 0.668 | 0.709 | 0.689 |
| Student-Teacher | 0.883 | 0.664 | 0.773 |
| GCAD | 0.806 | 0.860 | 0.833 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Area Under Saturated Per-Region Overlap]] | Pixel-level localization on [[MVTec LOCO AD]] | Normalized area under sPRO curve up to 5% average false positive rate per pixel | Higher is better | yes | GCAD mean 0.701; Student-Teacher mean 0.626; SPADE mean 0.451. |
| [[AU-ROC]] | Image-level anomaly classification | Area under ROC curve | Higher is better | secondary | GCAD mean 0.833; Student-Teacher mean 0.773; SPADE mean 0.689. |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB industrial inspection images.
- Output target: image-level anomaly score and pixel-level anomaly map.
- Supervision: unsupervised anomaly detection with anomaly-free training and validation images.
- Objective: jointly detect and localize structural and logical anomalies.

### Model And Training

- Model family: [[Unsupervised anomaly localization]].
- Architecture: two-branch GCAD with local feature regression and global bottleneck feature regression.
- Feature encoder: local branch distills ResNet-18 ImageNet features into a dense patch descriptor network.
- Losses: local regression loss, global knowledge-distillation loss, and global regression loss.
- Multi-scale inference: average anomaly maps from receptive fields p = 17 and p = 33.
- Augmentation: category-dependent flips, random rotation up to 3 degrees, and color jitter.
- Optimizer: Adam.
- Hyperparameters: learning rate 1e-4, weight decay 1e-5, 500 epochs, g = 32.
- Compute: not reported.

### Data

- Dataset: [[MVTec LOCO AD]].
- Data source: industrial-style object categories acquired with machine-vision style setups.
- Splits: anomaly-free train and validation sets; test set with anomaly-free, structural, and logical anomalies.
- Labels / annotations: pixel-precise anomaly masks and anomaly type groupings.
- License: not reported in the extracted text.
- Leakage checks: physical objects in train, validation, and test are distinct and do not overlap.

### Evaluation

- Protocol: report localization separately for structural and logical anomaly subsets, then average them for joint performance.
- Primary metric: [[Area Under Saturated Per-Region Overlap]].
- Secondary metric: image-level [[AU-ROC]].
- Baselines: Variation Model, f-AnoGAN, MNAD, AE, VAE, SPADE, and Student-Teacher.
- Failure cases: GCAD struggles with very challenging logical constraints, such as subtle incorrect cable arrangements; the local and global branches can each detect some anomalies intended for the other branch.

## Dataset / Benchmark Details

- Source: MVTec research dataset page.
- Collection: five object categories inspired by real-world industrial inspection scenarios.
- Annotation: pixel-precise anomaly masks; logical anomalies use saturation thresholds to account for ambiguity.
- Size: 3,644 images.
- Splits: 1,772 train, 304 validation, 1,568 test.
- Modalities: RGB visual inspection images.
- License: not reported in the extracted text.
- Bias / coverage: intentionally balances structural and logical anomalies; still limited to five object categories.
- Maintenance: dataset and evaluation code are reported publicly available.

## Limitations

- Structural and logical anomaly classes can have corner cases and are not always sharply separable.
- AUsPRO depends on saturation thresholds selected for each defect type.
- GCAD uses category-specific augmentation choices and a benchmark-specific setup; generalization outside these object categories requires further testing.
- The paper does not report all deployment costs, hardware, or runtime constraints in the extracted text.

## Reproducibility

- Code: evaluation code reported publicly available.
- Data: dataset reported publicly available.
- Hyperparameters: GCAD and baseline settings are reported in the experiments section.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: GCAD resizes all images to 256 x 256; baselines use their reported input sizes.
- Artifact status: dataset and evaluation code reported available.

## Systems Details

- Hardware / software stack: not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: not reported.
- Deployment assumptions: machine-vision style object inspection with known object categories and anomaly-free training data.
- Cost: not reported.
- Failure modes: limited receptive-field methods miss logical anomalies; reconstruction methods can produce false positives or reconstruct anomalous features.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Global Context Anomaly Detection]], [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]], [[Unsupervised learning]]
- Datasets: [[MVTec LOCO AD]], [[MVTec AD]]
- Benchmarks: [[MVTec LOCO AD]], [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Area Under Saturated Per-Region Overlap]], [[AU-ROC]], [[AU-PRO]]
- Concepts: [[Logical anomalies]], [[Structural anomalies]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - The MVTec Anomaly Detection Dataset]] | Builds on | MVTec LOCO AD extends the MVTec industrial anomaly benchmark line by balancing logical and structural anomalies rather than mostly structural defects. |
| [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]] | Shares task | Both evaluate unsupervised anomaly localization, but this paper focuses on logical constraints and sPRO. |
| [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] | Shares metric | The later AutoVI benchmark uses AUsPRO in a related pixel-level logical-defect evaluation context. |

### Connection Rationale

- [[MVTec LOCO AD]] is introduced by this paper and is the main dataset contribution.
- [[Area Under Saturated Per-Region Overlap]] is introduced to evaluate logical anomaly localization with ambiguous valid masks.
- [[Logical anomalies]] and [[Structural anomalies]] are core definitions used to motivate the dataset and method.
- [[Global Context Anomaly Detection]] is the proposed method and strongest reported benchmark baseline.

## Questions

- What are the exact license terms for MVTec LOCO AD?
- How stable are GCAD results across random seeds and implementation variants?
- Which logical constraints transfer to less controlled, less aligned industrial image settings?
