---
title: "Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN"
aliases:
  - "Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN"
paper_key: "doi:10.1109/access.2020.3024554"
paper_type: research
year: 2020
venue: "IEEE Access"
authors:
  - "Minsu Kim"
  - "Hoon Jo"
  - "Moonsoo Ra"
  - "Whoi-Yul Kim"
status: processed
processed_at: 2026-06-12
topics:
  - "weakly supervised defect segmentation"
  - "periodic textures"
  - "GAN augmentation"
tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Semiconductor and electronics]]"
  - "[[Textile and fiber inspection]]"
application_area: "semiconductor and textile periodic texture inspection"
datasets:
  - "private SEM semiconductor periodic-texture defect dataset"
  - "[[TILDA]]"
dataset_sizes:
  - "private semiconductor dataset: 264 grayscale defect images, 480 x 480"
  - "TILDA C3R1/C3R3: 397 and 323 defect patches after ROI extraction"
splits:
  - "private semiconductor dataset: 200 images selected for training; remaining samples used for evaluation"
modalities:
  - "SEM grayscale images"
  - "textile grayscale images"
methods:
  - "[[CycleGAN]]"
  - "[[DCGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[PatchMatch]]"
  - "[[PSGAN]]"
model_family:
  - "generative adversarial networks"
architectures:
  - "[[DCGAN]]"
  - "[[CycleGAN]]"
losses:
  - "adversarial loss"
  - "cycle consistency loss"
  - "identity mapping loss"
optimizers: []
training_regime: "weakly supervised segmentation with image-level labels"
augmentation:
  - "synthetic defect image generation"
  - "synthetic non-defect image generation"
synthetic_data: "DCGAN creates low-resolution synthetic defects; CycleGAN performs super-resolution; PatchMatch removes defect regions; PSGAN synthesizes non-defect periodic textures."
metrics:
  - "[[IoU]]"
  - "[[mIoU]]"
primary_metric: "[[mIoU]]"
metric_definitions:
  - "mIoU is computed over defective regions"
baselines:
  - "CAM with DenseNet"
  - "CAM with ResNet"
  - "CAM with SqueezeNet"
  - "FCN"
  - "AdapNet++"
benchmarks: []
evaluation_protocol: "compare weakly supervised CycleGAN framework against CAM weakly supervised localization and supervised FCN/AdapNet++ segmentation"
parameters: "not reported"
compute: "local workstation"
hardware: "AMD Ryzen 7 2700X CPU and NVIDIA RTX 2080Ti GPU with CUDA 10.0"
training_time: "not reported"
inference_cost: "golden template generation about 16 ms and defect segmentation about 2 ms"
url: "https://doi.org/10.1109/ACCESS.2020.3024554"
pdf: "paper-inbox/10_processed/Research/2020 - Kim - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN.pdf"
code: "not reported"
data: "private semiconductor dataset; public TILDA textile texture database"
doi: "10.1109/access.2020.3024554"
arxiv: "2020.30245"
related_papers:
  - "[[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]]"
related_concepts:
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_methods:
  - "[[CycleGAN]]"
  - "[[DCGAN]]"
  - "[[GAN]]"
  - "[[PatchMatch]]"
  - "[[PSGAN]]"
related_datasets:
  - "[[TILDA]]"
related_domains:
  - "[[Semiconductor and electronics]]"
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
related_benchmarks: []
concept_notes_created_or_updated: []
source_file: "paper-inbox/10_processed/Research/2020 - Kim - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Kim - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Kim - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN.txt"
tables: "paper-inbox/90_processing/tables/2020 - Kim - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN.md"
artifact_status: "code not reported; TILDA is public; semiconductor dataset private/not released in extracted text"
tags:
  - paper
---

# Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN

## Summary

- The paper proposes weakly supervised defect segmentation for periodic textures by translating defective images into golden-template images with CycleGAN and segmenting differences.
- Synthetic data is central: [[DCGAN]]/[[CycleGAN]] generate defect images, and [[PatchMatch]]/[[PSGAN]] generate non-defect textures when clean samples are unavailable.
- Rendered PDF tables show that the strongest weakly supervised setting reaches 82.33% mIoU on the private semiconductor dataset, below supervised AdapNet++ at 92.91% but above CAM baselines at 34.34-60.84%.

## Paper Type

- Type: research.
- Why: it proposes a segmentation framework and data-augmentation pipeline, then evaluates it on semiconductor and textile periodic textures.

## Problem

- Task: pixel-wise defect segmentation on periodic textures.
- Setting: defect samples are scarce, clean images may be unavailable, and pixel-wise labels are expensive.
- Inputs: grayscale defect images of periodic textures.
- Outputs: binary defect masks derived from a golden-template comparison.
- Motivation: semiconductor and textile inspection often needs defect localization with limited labeled data.
- Assumptions: periodic texture can be reconstructed as a defect-free golden template.

## Contribution

- Claimed: a weakly supervised framework segments periodic texture defects with only image-level labels and generated synthetic data.
- Shown: augmentation improves the golden-template generator and segmentation; the syn-subset setting reports 82.33% mIoU on the private semiconductor dataset versus 63.77% with real-only training and 80.98% with real+syn training.
- Inferred: the augmentation benefit is clearest on the private semiconductor dataset; TILDA is more difficult because texture periodicity is looser and defects are less distinct.

## Method

- Core idea: generate a defect-free golden template from a defect image, compute patch-wise absolute difference, then threshold to segment defects.
- Architecture / algorithm: [[DCGAN]] for low-resolution defect synthesis, [[CycleGAN]] for defect super-resolution and golden-template generation, [[PatchMatch]] for defect removal, [[PSGAN]] for non-defect texture synthesis, pSAD for image differencing, and hysteresis thresholding for mask extraction.
- Objective / loss: adversarial, cycle consistency, and identity mapping losses; identity mapping is important for preserving periodicity.
- Optimization: not reported in extracted text.
- Training data: private semiconductor defect images and generated non-defect/defect images; TILDA subsets C3R1 and C3R3.
- Data pipeline: generate synthetic defect and non-defect images, train CycleGAN domains, then post-process pSAD differences with hysteresis thresholding.
- Augmentation / synthesis: learned generative and patch-based synthesis.
- Inference: CycleGAN golden-template generation plus pSAD and hysteresis thresholding.
- Complexity / deployment constraints: inference is reported as about 16 ms for template generation and 2 ms for segmentation.

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale SEM or textile texture image.
- Output target: defect mask.
- Supervision: image-level labels for the proposed method; pixel-wise labels are used for supervised comparators and evaluation.
- Objective: segment defects without region-level training labels.

### Model And Training

- Model family: GAN-based image-to-image translation plus image processing.
- Architecture: [[DCGAN]], [[CycleGAN]], [[PSGAN]], [[PatchMatch]], pSAD, hysteresis thresholding.
- Parameters: NFD latent dimension 100; NSR trained 200 epochs; NGT trained 200 epochs or 50 epochs for syn subset mapping; lambda_cyc = 10; identity loss coefficients vary in experiments.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Losses: adversarial, cycle consistency, identity mapping.
- Optimizer: not reported.
- Hyperparameters: defect images 64 x 64 for NFD; 256 x 256 for super-resolution and golden-template generation; random flips and +/-5 deg rotations during NGT training.
- Seeds: not reported.
- Training compute: AMD Ryzen 7 2700X and RTX 2080Ti.

### Data

- Datasets: private semiconductor periodic-texture dataset; [[TILDA]] textile texture database.
- Data source: semiconductor images captured by scanning electron microscope; TILDA public textile texture database.
- Dataset size: 264 private semiconductor defect images; TILDA C3R1/C3R3 patches include 397 and 323 defect patches.
- Labels / annotations: private dataset has defect categories and ground truth for evaluation; TILDA defects are manually labeled for patch extraction/evaluation.
- Splits: private dataset uses 200 selected images for training; remaining data for evaluation.
- Preprocessing: resize/crop to 256 x 256; manual defect localization for PatchMatch and TILDA ROI extraction.
- Augmentation: random flip and small rotation during training; synthetic defect/non-defect generation.
- Synthetic data: real+syn subset and syn subset; syn subset contains 10,000 synthetic defect and non-defect images.
- Leakage checks: not reported.
- License: private semiconductor data not released; TILDA license not reported.

### Evaluation

- Protocol: compare against CAM variants and supervised FCN/AdapNet++ on private semiconductor dataset; evaluate TILDA subsets.
- Used performance metrics: IoU and mIoU.
- Primary metric: mIoU over defective regions.
- Metric definitions: IoU and mIoU formulas are provided.
- Metric direction / units: higher is better.
- Baselines: CAM DenseNet/ResNet/SqueezeNet, FCN, AdapNet++.
- Benchmarks: private dataset and TILDA subset evaluations.
- Statistical tests: not reported.
- Failure cases: small foreign bodies between line patterns, broken/bridged lines with weak intensity change, and loosely periodic TILDA textures.

## Evidence

### Experimental Setup

- Datasets: private SEM semiconductor dataset and TILDA C3R1/C3R3 textile subsets.
- Splits: 200 private dataset images for training; TILDA 300/250 arbitrary training images for C3R1/C3R3 and remaining test data.
- Baselines: CAM, FCN, AdapNet++.
- Used performance metrics: IoU and mIoU.
- Compute: local CPU/GPU workstation.
- Hardware: AMD Ryzen 7 2700X and NVIDIA RTX 2080Ti.
- Training time: not reported.
- Inference cost: about 18 ms total for template generation and segmentation.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Augmentation effect | Private semiconductor defect segmentation | mIoU | higher | Ours with real subset: 63.77 | Ours with syn subset: 82.33 | Synthetic training improves mIoU by +18.56 points over real-only training; real+syn reports 80.98. |
| Weak vs CAM | Private semiconductor defect segmentation | mIoU | higher | CAM DenseNet 60.84; CAM ResNet 34.34; CAM SqueezeNet 49.44 | Ours with syn subset: 82.33 | The proposed weakly supervised approach exceeds the strongest CAM baseline by +21.49 points. |
| Weak vs supervised | Private semiconductor defect segmentation | mIoU | higher | FCN 86.15; AdapNet++ 92.91 | Ours with syn subset: 82.33 | The best weakly supervised result is -3.82 points below FCN and -10.58 points below AdapNet++. |
| Inference cost | Private semiconductor defect segmentation | time | lower | FCN 42.12 ms; AdapNet++ 34.31 ms | Ours 17.84 ms | Paper text decomposes this as about 16 ms for golden-template generation plus 2 ms for segmentation. |
| Cross-domain C3R1 | [[TILDA]] textile defect segmentation | mIoU | higher | FCN 69.39; AdapNet++ 78.26 | Ours with augmentation: 12.27 | The paper attributes poor TILDA performance to looser periodicity, direction variation, indistinct defects, and poor synthetic defect quality. |
| Cross-domain C3R3 | [[TILDA]] textile defect segmentation | mIoU | higher | FCN 42.01; AdapNet++ 69.33 | Ours with augmentation: 14.84 | TILDA segmentation remains much weaker than supervised baselines. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[IoU]] | mask overlap | intersection over union | higher | no | Formula provided. |
| [[mIoU]] | defective-region segmentation | mean IoU over test images | higher | yes | Measured only with defective region. |

### Baseline Vs Improvement

| Comparison | Baseline | Proposed / variant | Improvement |
|---|---:|---:|---:|
| Synthetic augmentation vs real-only training, private dataset | 63.77 mIoU | 82.33 mIoU | +18.56 points |
| Real+synthetic vs real-only training, private dataset | 63.77 mIoU | 80.98 mIoU | +17.21 points |
| Best weakly supervised proposed result vs best CAM baseline | 60.84 mIoU | 82.33 mIoU | +21.49 points |
| Best weakly supervised proposed result vs FCN | 86.15 mIoU | 82.33 mIoU | -3.82 points |
| Best weakly supervised proposed result vs AdapNet++ | 92.91 mIoU | 82.33 mIoU | -10.58 points |
| Inference time vs FCN | 42.12 ms | 17.84 ms | 24.28 ms faster |
| Inference time vs AdapNet++ | 34.31 ms | 17.84 ms | 16.47 ms faster |

### Ablations

- Real vs real+syn vs syn training subsets test the data-synthesis contribution.
- Identity mapping loss coefficient tests preservation of periodic texture.
- CAM/FCN/AdapNet++ comparisons separate weak supervision from supervised segmentation.

## Dataset / Benchmark Details

- Source: private semiconductor SEM data and public TILDA textile data.
- Collection: private data captured by SEM; TILDA is a textile texture database.
- Annotation: private dataset has seven defect types; TILDA ROIs are manually labeled for defect extraction.
- Size: 264 private defect images; TILDA defect patches 397/323 for C3R1/C3R3.
- Splits: described above.
- Modalities: grayscale SEM and grayscale textile images.
- License: not reported.
- Leakage risks: manual defect localization is used in synthesis and evaluation; no leakage audit is reported.
- Bias / coverage: method works better for strictly periodic textures.
- Maintenance: not reported.

## Limitations

- Stated: pSAD and hysteresis threshold parameters strongly affect defect number and area.
- Stated: some defects with weak intensity changes are missed.
- Stated: synthetic defect generation struggles with complex loosely periodic TILDA textures.
- Inferred: full reproducibility is limited because the semiconductor dataset is private and the table cells required rendered-PDF inspection rather than text-layer extraction.

## Reproducibility

- Code: not reported.
- Data: TILDA public; semiconductor dataset private.
- Hyperparameters: many training and synthesis settings are reported.
- Random seeds: not reported.
- Environment: CUDA 10.0 with RTX 2080Ti.
- Checkpoints / models: not reported.
- Exact preprocessing: partially reported.
- Artifact status: partial.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Industrial anomaly detection]].
- Methods: [[CycleGAN]], [[DCGAN]], [[GAN]], [[Synthetic data generation]], [[Data augmentation]], [[PatchMatch]], [[PSGAN]].
- Optimizers: not reported.
- Datasets: private semiconductor SEM dataset, [[TILDA]] textile texture database.
- Benchmarks: not reported as named benchmark notes.
- Domains: [[Semiconductor and electronics]], [[Textile and fiber inspection]].
- Metrics: [[IoU]], [[mIoU]].
- Concepts: weak supervision, golden template generation, periodic texture inspection.
- Dataset-domain links: private semiconductor dataset maps to [[Semiconductor and electronics]]; TILDA maps to [[Textile and fiber inspection]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2017 - Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks]] | Builds on | Uses CycleGAN losses for super-resolution and golden-template generation. |
| [[TILDA]] | Shares dataset | Uses C3R1 and C3R3 textile periodic-texture subsets for cross-domain evaluation. |

### Backlinks Updated

- Updated [[TILDA]], [[DCGAN]], [[IoU]], [[mIoU]], [[Weakly supervised learning]], [[PatchMatch]], and [[PSGAN]].

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[PatchMatch]] | Created | Central patch-based defect removal step before non-defect synthesis. |
| [[PSGAN]] | Created | Central periodic texture generator for synthetic non-defect images. |

## Questions

- The PDF table cells were not present in the text layer; exact numeric cells were recovered from rendered PDF pages and stored in the preprocessing table artifact.
- The private semiconductor dataset availability is not reported.
