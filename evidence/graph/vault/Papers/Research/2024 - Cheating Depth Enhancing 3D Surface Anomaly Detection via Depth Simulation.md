---
title: "Cheating Depth: Enhancing 3D Surface Anomaly Detection via Depth Simulation"
aliases:
  - "3DSR"
  - "DADA"
paper_key: "doi:10.1109/wacv57701.2024.00216"
paper_type: research
year: 2024
venue: "WACV 2024"
authors:
  - "Vitjan Zavrtanik"
  - "Matej Kristan"
  - "Danijel Skocaj"
status: processed
processed_at: 2026-05-22
topics:
  - "3D surface anomaly detection"
  - "depth simulation"
  - "discrete autoencoder"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec3D]]"
  - "[[Eyecandies]]"
dataset_sizes:
  - "MVTec3D: 4147 RGB+3D scans; 894 anomalous scans reported by the paper."
  - "Eyecandies: 10 object classes, 10000 anomaly-free training examples and 500 test examples, 250 anomalous."
methods:
  - "[[3DSR]]"
  - "[[Depth simulation]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Simulation-based data augmentation]]"
model_family:
  - "[[3DSR]]"
  - "Depth-Aware Discrete Autoencoder"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
  - "[[FPS]]"
primary_metric: "[[AU-PRO]]"
baselines:
  - "M3DM"
  - "AST"
  - "PatchCore + FPFH"
  - "DSR"
  - "Depth AE"
  - "Depth GAN"
  - "Voxel AE"
code: "https://github.com/VitjanZ/3DSR"
data: "[[MVTec3D]] and [[Eyecandies]]"
doi: "10.1109/WACV57701.2024.00216"
arxiv: "not reported"
url: "https://doi.org/10.1109/WACV57701.2024.00216"
pdf: "paper-inbox/10_processed/Research/2024 - Zavrtanik - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation.pdf"
related_papers:
  - "[[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]]"
  - "[[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[3DSR]]"
  - "[[Depth simulation]]"
  - "[[Simulation-based data augmentation]]"
related_datasets:
  - "[[MVTec3D]]"
  - "[[Eyecandies]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec3D]]"
  - "[[Eyecandies]]"
source_file: "paper-inbox/10_processed/Research/2024 - Zavrtanik - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Zavrtanik - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Zavrtanik - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "3d-surface-anomaly-detection"
  - "depth-simulation"
---

# Cheating Depth: Enhancing 3D Surface Anomaly Detection via Depth Simulation

## Summary

The paper proposes [[3DSR]], a fast RGB+3D surface anomaly detection method built around a Depth-Aware Discrete Autoencoder (DADA) and simulated industrial depth data. It addresses the lack of large industrial depth datasets by generating depth maps with Perlin noise plus affine scaling/translation, then uses the resulting depth representation in a DSR-style dual subspace reprojection detector. On [[MVTec3D]], 3DSR reports the best mean image-level AUROC in 3D-only and RGB+3D settings, the best mean pixel-level AUROC in RGB+3D, the best mean PRO in RGB+3D, and 33 FPS on an NVIDIA RTX A4500.

## Paper Type

- Type: research.
- Why: The paper introduces a new RGB+3D anomaly detection architecture, training procedure, and evaluation against prior 3D industrial anomaly detection methods.

## Problem

- Task: [[Industrial anomaly detection]], [[Defect segmentation]].
- Setting: RGB+3D industrial surface inspection where some defects are nearly invisible in RGB but detectable in depth.
- Inputs: RGB images and depth maps or sorted point-cloud-derived depth images.
- Outputs: Image-level anomaly scores and pixel-level anomaly segmentation masks.
- Motivation: Existing 3D anomaly methods rely on point-cloud backbones that are slow and poorly matched to industrial depth distributions; industrial depth data is too small to train large depth backbones directly.
- Assumptions: Simulated depth maps can capture enough industrial depth statistics to pretrain useful depth representations.

## Contribution

- Claimed: DADA learns a general discrete latent space jointly modeling RGB and depth data for 3D surface anomaly detection.
- Claimed: A parameterized industrial depth simulation process can compensate for the shortage of large industrial depth datasets.
- Shown: 3DSR improves MVTec3D image-level AUROC over M3DM by 4.8 points in 3D-only and 3.3 points in RGB+3D mean scores.
- Shown: 3DSR runs at 33 FPS versus M3DM at 0.6 FPS and AST at 18 FPS on an NVIDIA RTX A4500.

## Method

- Core idea: Pretrain DADA on ImageNet RGB images paired with simulated depth images, then use the DADA representation inside a discriminative anomaly detector that compares anomaly-free and anomaly-preserving reprojections.
- DADA architecture: A 4-channel RGB+depth input is encoded with grouped convolutions to keep RGB and depth features separated, then quantized through a two-stage vector-quantized latent space.
- DADA loss: Modified VQ-VAE loss combining RGB reconstruction, depth reconstruction, codebook losses, and commitment terms; `lambda_I = 1`, `lambda_D = 1`, and `lambda_K = 0.25` unless otherwise stated.
- Depth simulation: Generate Perlin noise `P`, normalize it to 0-1, scale with `alpha` sampled from `(0, 1)`, translate with `beta` sampled from `(0, 1 - alpha)`, producing `D = alpha P + beta`.
- 3DSR detector: Integrates DADA into DSR. During training, simulated feature-level anomalies are produced by replacing codebook vectors in Perlin-noise mask regions. At inference, input features are passed through a subspace restriction module and compared through decoders and an anomaly detection module.
- Image-level anomaly score: Smooth the output anomaly mask with a Gaussian filter, then use the maximum value of the smoothed mask.

## Evidence

### Experimental Setup

- Datasets: [[MVTec3D]] and [[Eyecandies]].
- Problem setups: 3D-only, RGB-only, and RGB+3D. For RGB-only, the paper reports DSR rather than 3DSR.
- MVTec3D size reported by the paper: 4147 RGB+3D scans, including 894 anomalous scans, across 10 classes.
- Eyecandies size reported by the paper: 10 classes, 10000 anomaly-free training examples, and 500 test examples with 250 anomalous.
- DADA training: ImageNet RGB images plus simulated depth images; batch size 64; 100K iterations; learning rate 0.0002.
- Codebook: 2048 embeddings with dimension 256.
- 3DSR training: class-specific training on each dataset; batch size 16; 30K iterations; learning rate 0.0002.
- Depth preprocessing: Normalize depth maps to 0-1; replace missing values with the average of valid pixels in a 3 x 3 neighborhood, or 0 when no surrounding valid pixels exist; derive foreground masks by distance to a background plane.
- Used performance metrics: image-level [[AU-ROC]], pixel-level AUROC, [[AU-PRO]], and [[FPS]].
- Hardware for FPS: NVIDIA RTX A4500 GPU.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| 3D-only detection improves over M3DM | [[MVTec3D]] 3D setup | mean image AUROC | higher | 87.4 | 92.2 | 3DSR ranks first in 7/10 classes. |
| RGB+3D detection improves over M3DM | [[MVTec3D]] RGB+3D setup | mean image AUROC | higher | 94.5 | 97.8 | 3DSR ranks first in 5/10 classes and top-three in every class. |
| RGB+3D localization improves over M3DM | [[MVTec3D]] RGB+3D setup | mean PRO | higher | 96.4 | 97.2 | 3DSR ranks first in mean RGB+3D PRO. |
| RGB+3D pixel localization improves over M3DM | [[MVTec3D]] RGB+3D setup | pixel AUROC | higher | 99.2 | 99.5 | Table 3 mean pixel AUROC. |
| 3D-only Eyecandies improves over M3DM | [[Eyecandies]] 3D setup | mean image AUROC | higher | 72.5 | 77.6 | Table 4. |
| RGB+3D Eyecandies slightly improves over M3DM | [[Eyecandies]] RGB+3D setup | mean image AUROC | higher | 89.7 | 90.9 | Table 4. |
| Inference is much faster than point-cloud-heavy M3DM | MVTec3D-style inference | FPS | higher | 0.6 | 33 | AST reports 18 FPS on the same GPU. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level anomaly detection and pixel-level localization | Area under ROC curve; percent values in tables | higher is better | yes | Image-level AUROC is the headline detection metric. |
| [[AU-PRO]] | anomaly localization | Per-region overlap metric; percent values in tables | higher is better | yes | Used for localization on MVTec3D. |
| [[FPS]] | inference efficiency | frames per second on NVIDIA RTX A4500 | higher is better | no | 3DSR reports 33 FPS. |

### Ablations

| Variant | I-AUROC | P-AUROC | PRO | Interpretation |
|---|---:|---:|---:|---|
| DSR naive | 87.6 | 96.5 | 92.3 | Training a naive RGB+depth VQ-VAE on MVTec3D is weak. |
| 3DSR no Perlin | 90.0 | 98.3 | 93.3 | Replacing Perlin depth with grayscale ImageNet drops image AUROC by about 8 points. |
| 3DSR no affine | 94.8 | 99.2 | 95.9 | Removing alpha/beta depth scaling/translation hurts results. |
| 3DSR VQ-VAE | 95.8 | 99.3 | 96.3 | Replacing DADA with a VQ-VAE hurts image AUROC by about 2 points. |
| 3DSR weighted | 96.5 | 99.4 | 96.7 | Reweighting depth loss in VQ-VAE is not enough to match DADA. |
| 3DSR | 97.8 | 99.5 | 97.2 | Full method. |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB images, depth images, and RGB+depth pairs.
- Output target: anomaly segmentation mask and image-level anomaly score.
- Supervision: unsupervised anomaly detection with normal training data; simulated feature-level anomalies are used during detector training.
- Objective: Detect and localize RGB-visible and depth-visible surface anomalies efficiently.

### Model And Training

- Model family: discrete autoencoder plus discriminative anomaly segmentation.
- Architecture: DADA with grouped convolution separation of RGB/depth features, two-stage vector quantization, subspace restriction module, object-specific decoder, general appearance decoder, and anomaly detection module.
- Parameters: codebooks contain 2048 embeddings of dimension 256.
- Pretraining: DADA trained on ImageNet RGB images paired with simulated depth maps.
- Fine-tuning: 3DSR trained per object class on MVTec3D or Eyecandies.
- Losses: DADA uses a modified VQ-VAE loss; subspace restriction uses L1 loss; anomaly detection module uses focal loss.
- Optimizer: not reported.
- Hyperparameters: DADA batch size 64, 100K iterations, learning rate 0.0002; 3DSR batch size 16, 30K iterations, learning rate 0.0002; `lambda_I = 1`, `lambda_D = 1`, `lambda_K = 0.25`.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec3D]], [[Eyecandies]], ImageNet for RGB supervision during DADA training.
- Data source: MVTec3D industrial RGB+3D scans; Eyecandies rendered RGB+3D anomaly benchmark; simulated depth maps for DADA pretraining.
- Dataset size: MVTec3D 4147 scans with 894 anomalous; Eyecandies 10000 training and 500 test examples.
- Labels / annotations: Anomaly masks for evaluation; simulated anomaly masks during training.
- Splits: Standard per-dataset splits are used; exact train/test counts beyond the paper's size summary are not fully restated.
- Preprocessing: depth normalization, missing-depth imputation, foreground masking from background-plane distance.
- Augmentation: feature-level anomalies generated by codebook-vector replacement in Perlin-noise mask regions.
- Synthetic data: simulated depth maps from Perlin noise with affine intensity scaling and translation.
- Leakage checks: not reported.
- License: not reported by this paper.

### Evaluation

- Protocol: Evaluate 3D-only, RGB-only, and RGB+3D setups for anomaly detection and localization.
- Used performance metrics: image-level AUROC, pixel-level AUROC, AU-PRO, FPS.
- Primary metric: AU-PRO for localization; image-level AUROC for detection.
- Metric definitions: image-level AUROC, pixel-level AUROC, and PRO are named; exact PRO thresholding details are not restated.
- Metric direction / units: higher is better; reported as percentages.
- Baselines: Voxel AE, Depth GAN, Depth AE, FPFH, 3D-ST, AST, M3DM, PatchCore, DifferNet, PADiM, CS-Flow, DSR, PatchCore+FPFH.
- Benchmarks: [[MVTec3D]], [[Eyecandies]].
- Statistical tests: not reported.
- Failure cases: Eyecandies examples with small dents at object edges, subtle depth-only deformations, and transparent-object deformations remain difficult.

## Dataset / Benchmark Details

- Source: [[MVTec3D]] and [[Eyecandies]].
- Collection: MVTec3D uses high-resolution industrial 3D sensor scans; Eyecandies is rendered.
- Annotation: anomaly masks are used for localization evaluation.
- Size: MVTec3D has 4147 scans; Eyecandies has 10000 train and 500 test examples.
- Splits: Eyecandies test split has 250 anomalous examples; MVTec3D split details are not fully restated beyond total/anomalous counts.
- Modalities: RGB and depth/3D.
- License: not reported by this paper.
- Leakage risks: not reported.
- Bias / coverage: MVTec3D and Eyecandies each contain 10 object classes; the paper's conclusions are limited to these RGB+3D benchmarks.
- Maintenance: not reported.

## Limitations

- Stated: Certain Eyecandies anomalies remain difficult, including small dents at object edges, subtle depth-only deformations, and transparent-object deformations.
- Stated: Some anomalies can be hard even for humans because they closely resemble normal object appearance.
- Inferred: The depth simulator summarizes selected depth statistics but may not cover all real industrial sensors or surface materials.
- Inferred: Optimizer, random seeds, and full training environment are not reported in the extracted source.

## Reproducibility

- Code: https://github.com/VitjanZ/3DSR.
- Data: [[MVTec3D]] and [[Eyecandies]].
- Hyperparameters: DADA and 3DSR batch sizes, iterations, learning rates, codebook size/dimension, and loss weights are reported.
- Random seeds: not reported.
- Environment: FPS measured on NVIDIA RTX A4500; training environment not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: depth maps normalized to 0-1; missing pixels replaced with 3 x 3 valid-neighbor average or 0; foreground mask derived from background plane.
- Artifact status: code reported available.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[3DSR]], [[Depth simulation]], [[Unsupervised anomaly detection]], [[Simulation-based data augmentation]]
- Datasets: [[MVTec3D]], [[Eyecandies]]
- Benchmarks: [[MVTec3D]], [[Eyecandies]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]], [[FPS]]

### Shares Dataset

- [[MVTec3D]] - the main RGB+3D industrial benchmark used for detection, localization, ablation, and speed comparisons.
- [[Eyecandies]] - second RGB+3D benchmark used for image-level AUROC comparison.

### Shares Method

- [[3DSR]] - the paper introduces this detector.
- [[Depth simulation]] - the paper trains DADA using Perlin-noise-based simulated industrial depth maps.
- [[Simulation-based data augmentation]] - feature-level anomalies and depth maps are simulated for training.

### Shares Metric

- [[AU-ROC]] - used for image-level detection and pixel-level localization.
- [[AU-PRO]] - used for anomaly localization.
- [[FPS]] - used for inference efficiency.

### Related Papers and Concepts

- [[2023 - Multimodal Industrial Anomaly Detection via Hybrid Fusion]] - contrasts with prior RGB+3D anomaly detection based on heavier point-cloud representations.
- [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] - introduces the main benchmark used in this paper.

## Questions

- How well does the Perlin-plus-affine depth simulator transfer to real sensors with different noise, missing-data, and material-response profiles?
- Which categories depend most on depth-only information versus RGB+depth fusion?
- Can DADA's simulated-depth pretraining improve other RGB anomaly detectors when adapted to depth-image input?
