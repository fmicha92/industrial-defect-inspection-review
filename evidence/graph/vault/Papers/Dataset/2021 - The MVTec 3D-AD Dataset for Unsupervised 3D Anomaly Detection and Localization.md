---
title: "The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization"
aliases:
  - "The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization"
paper_key: "arxiv:2112.09045"
paper_type: dataset
year: 2021
venue: "VISAPP"
authors:
  - "Paul Bergmann"
  - "Xin Jin"
  - "David Sattlegger"
  - "Carsten Steger"
status: processed
processed_at: 2026-05-22
topics:
  - "3D anomaly detection"
  - "industrial visual inspection"
  - "RGB-D inspection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec3D]]"
methods:
  - "[[Unsupervised learning]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[GAN]]"
  - "[[Variational Autoencoder]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures:
  - "Voxel f-AnoGAN"
  - "Voxel autoencoder"
  - "Depth f-AnoGAN"
  - "Depth autoencoder"
metrics:
  - "[[AU-PRO]]"
  - "[[AU-ROC]]"
primary_metric: "[[AU-PRO]]"
metric_definitions:
  - "PRO averages relative overlap between a thresholded anomaly prediction and each connected ground-truth component."
  - "AU-PRO is integrated only up to false-positive-rate 0.3 in the paper's main localization benchmark."
baselines:
  - "Voxel f-AnoGAN"
  - "Voxel autoencoder"
  - "Voxel variation model"
  - "Depth f-AnoGAN"
  - "Depth autoencoder"
  - "Depth variation model"
benchmarks:
  - "[[MVTec3D]]"
code: "evaluation scripts promised with dataset release; code otherwise not reported"
data: "public dataset release announced at https://www.mvtec.com/company/research/datasets"
doi: "not reported"
arxiv: "2112.09045"
url: "https://www.mvtec.com/company/research/datasets"
pdf: "paper-inbox/00_incoming/2112.09045v1.pdf"
related_papers:
  - "[[2021 - The MVTec Anomaly Detection Dataset]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[Unsupervised learning]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[GAN]]"
  - "[[Variational Autoencoder]]"
related_datasets:
  - "[[MVTec3D]]"
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec3D]]"
source_file: "paper-inbox/00_incoming/2112.09045v1.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Bergmann - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Bergmann - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization.txt"
artifact_status: "dataset promised as public; evaluation scripts promised with release"
tags:
  - paper
---
# The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization

## Summary

The paper introduces [[MVTec3D]], a 3D industrial anomaly-detection and localization dataset with 4147 high-resolution 3D scans from 10 real-world object categories. Training and validation splits contain only anomaly-free scans, while the test split contains both good samples and 948 anomalous samples with 41 defect types and 1148 annotated anomaly regions.

The benchmark shows that then-current 3D anomaly-localization methods leave substantial room for improvement. Voxel f-AnoGAN is the strongest mean localization baseline in the reported AU-PRO table, but the authors conclude that all evaluated methods are insufficient for practical industrial deployment, especially at low false-positive rates.

## Paper Type

- Type: dataset and benchmark.
- Why: The main contribution is a new public 3D industrial anomaly dataset with precise anomaly annotations, plus an initial benchmark of 3D and depth-image anomaly-localization methods.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]] for 3D scans.
- Setting: unsupervised anomaly detection and localization from normal-only training data.
- Inputs: cropped `(x, y, z)` images from a structured-light 3D sensor, with complementary RGB values per pixel.
- Outputs: real-valued anomaly scores per `(x, y, z)` pixel for localization; image-level anomaly scores for sample-level detection.
- Motivation: 3D defects such as dents, holes, deformations, missing material, or geometry changes may be poorly captured by RGB-only inspection, while labeled defect examples are difficult to acquire.
- Assumptions: objects are scanned from a fixed camera angle in a setup similar to industrial inspection; training and validation data are anomaly-free.

## Contribution

- Claimed: The paper introduces the first comprehensive dataset for unsupervised anomaly detection and localization in three-dimensional data.
- Shown: [[MVTec3D]] contains 4147 point-cloud scans across 10 object categories, with normal-only training/validation splits, anomalous and normal test samples, and precise ground-truth annotations for each anomalous test sample.
- Shown: An initial benchmark compares voxel-grid and depth-image variants of f-AnoGAN, autoencoder, and variation-model baselines, with and without RGB information.
- Shown: Existing baselines do not solve the benchmark; even the best mean AU-PRO values at false-positive-rate 0.3 remain far from practical industrial requirements.

## Method

- Dataset acquisition: scans were captured with a Zivid One+ Medium structured-light industrial 3D sensor at 1920 x 1200 resolution.
- Sensor output: each scan is represented as a three-channel image containing local camera-frame `x`, `y`, and `z` coordinates, with associated RGB values for each valid point.
- Cropping: each category uses a fixed rectangular crop to reduce background pixels while leaving a margin for augmentation.
- Object placement: the sensor was statically mounted and each category was viewed from the same angle; objects were recorded on a dark background under indirect diffuse illumination.
- Annotation: anomalies were annotated in the 3D point clouds and exported as 2D regions through the one-to-one mapping from 3D points to `(x, y, z)` image pixels.
- Invalid-pixel handling: annotations can include invalid sensor pixels when anomalies cause missing 3D reconstruction; RGB-visible anomalous pixels are also appended when not already covered by the 3D annotation.

## ML / DL Extraction

### Task Formulation

- Input modality: 3D coordinate images, point clouds, depth images derived from `(x, y, z)`, voxel grids, and optional RGB channels.
- Output target: pixel-level anomaly score maps for localization and image-level anomaly scores for sample classification.
- Supervision: [[Unsupervised learning]]; models train on anomaly-free samples.
- Objective: benchmarked reconstruction-style and variation-model methods estimate normal structure and score deviations at test time.

### Model And Training

- Voxel representation: category-specific global training-set bounding box; 64 x 64 x 64 voxel grid centered on the bounding box.
- Voxel values: occupied and empty voxels are encoded as 1 and -1 for 3D-only input; RGB variants assign occupied voxels the average RGB of points in the cell and empty voxels (-1, -1, -1).
- Depth representation: depth is computed as Euclidean distance to the camera center for each valid `(x, y, z)` pixel; invalid pixels are assigned 0; RGB channels are appended for RGB variants.
- Voxel autoencoder loss: occupied/empty imbalance is handled with a loss weight based on the fraction of empty voxels in the training set.
- Depth f-AnoGAN and depth autoencoder resolution: 256 x 256 pixels, resized from original inputs.
- Augmentation: each training sample is augmented 20 times by random rotations around the estimated background-plane normal with angles sampled from [-5 degrees, 5 degrees].
- Hyperparameters: detailed training parameters and model architectures are in the paper appendix, which is not included in the compact source input.
- Compute: not reported in the compact source input.

### Data

- Dataset: [[MVTec3D]].
- Total scans: 4147.
- Categories: bagel, cable gland, carrot, cookie, dowel, foam, peach, potato, rope, and tire.
- Split totals: 2656 training scans, 294 validation scans, 249 good test scans, and 948 anomalous test scans.
- Defect coverage: 41 defect types and 1148 annotated regions.
- Natural variation categories: bagel, carrot, cookie, peach, and potato.
- Deformable standardized categories: foam, rope, and tire.
- Rigid categories: cable gland and dowel.
- Example anomalies: cracks, geometrical deformations, holes, contaminations, and cut-off parts.
- License: not reported in the compact source input.

### Evaluation

- Localization metric: [[AU-PRO]] with PRO defined as the average relative overlap between a binary predicted anomaly region and each connected ground-truth component.
- AU-PRO integration limit: the main benchmark integrates only up to false-positive-rate 0.3 and warns against high false-positive-rate limits because anomalous regions are small relative to the images.
- Classification metric: [[AU-ROC]] for sample-level anomaly classification.
- Baselines: Voxel f-AnoGAN, Voxel autoencoder, Voxel variation model, Depth f-AnoGAN, Depth autoencoder, and Depth variation model, each tested with 3D-only input and with 3D + RGB where applicable.
- Evaluation output requirement: methods must output real-valued anomaly scores for each `(x, y, z)` pixel, not only valid 3D points.
- Statistical tests: not reported.

## Evidence

### Dataset Statistics

| Category | Train | Val | Test good | Test anomalous | Defect types | Annotated regions | Image size |
|---|---:|---:|---:|---:|---:|---:|---|
| bagel | 244 | 22 | 22 | 88 | 4 | 112 | 800 x 800 |
| cable gland | 223 | 23 | 21 | 87 | 4 | 90 | 400 x 400 |
| carrot | 286 | 29 | 27 | 132 | 5 | 159 | 800 x 800 |
| cookie | 210 | 22 | 28 | 103 | 4 | 128 | 500 x 500 |
| dowel | 288 | 34 | 26 | 104 | 4 | 131 | 400 x 400 |
| foam | 236 | 27 | 20 | 80 | 4 | 115 | 900 x 900 |
| peach | 361 | 42 | 26 | 106 | 5 | 131 | 600 x 600 |
| potato | 300 | 33 | 22 | 92 | 4 | 115 | 800 x 800 |
| rope | 298 | 33 | 32 | 69 | 3 | 72 | 900 x 400 |
| tire | 210 | 29 | 25 | 87 | 4 | 95 | 600 x 800 |
| total | 2656 | 294 | 249 | 948 | 41 | 1148 | mixed |

### Experimental Setup

- Voxel baselines use 64 x 64 x 64 grids.
- Depth baselines operate on depth images; depth f-AnoGAN and depth autoencoder use 256 x 256 resized inputs.
- RGB values are scaled to [0, 1].
- Voxel anomaly scores are projected back to original image-pixel coordinates using the calibrated camera parameters.
- Depth anomaly maps are resized to the original image size with bilinear interpolation.

### Main Results

| Result | Dataset / Task | Metric | Direction | Paper result | Notes |
|---|---|---|---|---:|---|
| Best 3D-only mean localization baseline | [[MVTec3D]] / localization | [[AU-PRO]] at FPR 0.3 | higher | 0.583 | Voxel f-AnoGAN, mean across categories. |
| Best 3D + RGB mean localization baseline | [[MVTec3D]] / localization | [[AU-PRO]] at FPR 0.3 | higher | 0.639 | Voxel f-AnoGAN, mean across categories. |
| Best depth-only mean localization baseline | [[MVTec3D]] / localization | [[AU-PRO]] at FPR 0.3 | higher | 0.374 | Depth variation model, mean across categories. |
| Best depth + RGB mean localization baseline | [[MVTec3D]] / localization | [[AU-PRO]] at FPR 0.3 | higher | 0.481 | Depth autoencoder, mean across categories. |

- Voxel f-AnoGAN performs best on average for 3D-only data and again for 3D + RGB data.
- Voxel methods generally outperform depth-image counterparts.
- Adding RGB improves all evaluated methods except the variation models.
- Depth autoencoder and depth f-AnoGAN produce many false positives around invalid pixels.
- The authors state that performance at FPR 1.0 can look misleadingly high because segmentation masks with many false positives are not practically meaningful.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-PRO]] | anomaly localization | normalized area under PRO curve up to FPR 0.3 | higher | yes | PRO averages overlap across connected anomaly components. |
| [[AU-ROC]] | sample-level anomaly classification | area under ROC curve | higher | no | Classification results are reported in the appendix, not in the compact source input. |

### Ablations

- Latent dimension ablation for compression-based methods is reported in the appendix, but appendix details are not included in the compact source input.
- Figure 6 varies the AU-PRO false-positive-rate integration limit and shows monotonic increases as the limit rises; the authors use this to argue for low integration limits.

## Dataset / Benchmark Details

- Source: high-resolution industrial structured-light 3D scans.
- Collection: Zivid One+ Medium sensor, fixed per-category viewpoint, indirect diffuse lighting, dark background, category-specific rectangular crop.
- Modalities: `(x, y, z)` coordinate images, RGB image values, point clouds, and ground-truth masks for anomalous test samples.
- Annotation: 3D point-cloud annotations mapped into 2D regions, including invalid-pixel anomalies when relevant.
- Size: 4147 scans.
- Splits: normal-only train and validation; test split includes 249 good and 948 anomalous samples.
- Defect labels: 41 defect types across 10 categories; exact per-defect names are not listed in the compact source input.
- Availability: the paper states that the dataset will be made publicly available at MVTec's research dataset page.
- Evaluation scripts: promised with the dataset release.
- Leakage risks: not reported.
- Bias / coverage: industrial tabletop object categories; five natural objects, three deformable standardized objects, and two rigid objects.
- Maintenance: not reported.

## Limitations

- Stated: current baselines are insufficient for real-world industrial applications.
- Stated: integrating AU-PRO to high false-positive rates can overstate localization quality because anomalous regions are small relative to the images.
- Stated: a false-positive rate of 0.3 is hardly acceptable in actual industrial inspection.
- Not reported: dataset license, maintenance plan, exact appendix hyperparameters, and classification benchmark values are absent from the compact source input.

## Reproducibility

- Code: evaluation scripts promised with the dataset release; model code not reported.
- Data: dataset promised as publicly available at MVTec's research dataset page.
- Hyperparameters: appendix contains details, but the compact source input does not include them.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: crop per category, depth conversion, voxelization, RGB scaling, and projection of voxel scores are described.
- Artifact status: dataset and evaluation scripts announced; availability beyond that statement should be checked against the MVTec dataset host page.

## Systems Details

- Hardware / software stack: Zivid One+ Medium structured-light 3D sensor for acquisition.
- Latency: not applicable.
- Throughput: not reported.
- Memory: not reported.
- Scaling: dataset has 4147 scans; training-set augmentation multiplies training samples by 20 in the benchmark.
- Deployment assumptions: fixed inspection geometry and controlled illumination are aligned with industrial visual inspection setups.
- Cost: not reported.
- Failure modes: evaluated methods produce false positives on surfaces, object edges, and background; depth-image neural baselines are sensitive around invalid pixels.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Unsupervised learning]], [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]], [[GAN]], [[Variational Autoencoder]]
- Datasets: [[MVTec3D]], [[MVTec AD]]
- Benchmarks: [[MVTec3D]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-PRO]], [[AU-ROC]]
- Concepts: [[Industrial visual inspection]], [[Surface defect detection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - The MVTec Anomaly Detection Dataset]] | Builds on / contrasts with | The paper frames MVTec AD as a comprehensive 2D industrial anomaly benchmark and extends the benchmark family into 3D scans. |
| [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] | Follow-up reading | MVTec LOCO AD is another MVTec anomaly dataset that expands anomaly-localization scenarios beyond structural defects. |
| [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] | Shares dataset | The paper later reports results on [[MVTec3D]] as part of multimodal industrial anomaly localization. |

### Link Rationale

- [[MVTec3D]]: introduced dataset and benchmark.
- [[AU-PRO]]: primary localization metric in the paper's benchmark.
- [[AU-ROC]]: sample-level classification metric described by the evaluation section.
- [[Multi-industry anomaly detection]]: the dataset spans 10 object categories rather than one manufacturing line.
- [[Unsupervised anomaly localization]]: the benchmark requires pixel-level anomaly score maps from normal-only training data.

## Questions

- What are the exact appendix classification AU-ROC results and latent-dimension ablation values?
- What license and download conditions are stated on the current MVTec 3D-AD host page?
- Which later 3D anomaly-localization methods report strong results on this benchmark under low false-positive-rate AU-PRO integration?
