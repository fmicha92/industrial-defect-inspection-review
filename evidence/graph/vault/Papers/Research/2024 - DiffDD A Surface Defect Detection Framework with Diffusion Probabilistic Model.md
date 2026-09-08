---
title: "DiffDD: A Surface Defect Detection Framework with Diffusion Probabilistic Model"
aliases:
  - "DiffDD: A Surface Defect Detection Framework with Diffusion Probabilistic Model"
paper_key: "sha256:f2669f120eb2adc4368696ce7cf804db55c739797a8c688b8ae945e04bffac42"
paper_type: research
year: 2024
venue: "Advanced Engineering Informatics"
authors:
  - "Xin Zhou"
  - "Yongchao Zhang"
  - "Zhaohui Ren"
  - "Tianchuan Mi"
  - "Ke Feng"
  - "Shihua Zhou"
  - "Zeyu Jiang"
status: processed
processed_at: 2026-05-23
topics:
  - "diffusion defect detection"
  - "surface defect detection"
  - "semantic segmentation"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[NEU-SEG]]"
  - "[[Magnetic Tile Defects]]"
  - "[[KolektorSDD2]]"
  - "[[DAGM2007]]"
methods:
  - "[[DiffDD]]"
  - "[[Diffusion models]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "[[DiffDD]]"
  - "PvTv2 backbone"
losses:
  - "diffusion noise-prediction MSE"
  - "mask loss"
optimizers:
  - "[[AdamW]]"
metrics:
  - "[[F1-score]]"
  - "[[mAP]]"
  - "[[AU-ROC]]"
  - "[[IoU]]"
  - "[[Recall]]"
primary_metric: "[[mAP]]"
metric_definitions:
  - "F1-score, mAP, AUROC, and IoU are defined in the paper; higher is better for all reported metrics."
baselines:
  - "AE spatial"
  - "AE dense"
  - "VAE"
  - "cmSalGAN"
  - "f-AnoGAN"
  - "Trans-GAN"
  - "U-Net variants"
  - "CSEPNet"
  - "SegNet"
benchmarks:
  - "[[NEU-SEG]]"
  - "[[Magnetic Tile Defects]]"
  - "[[KolektorSDD2]]"
  - "[[DAGM2007]]"
code: "not reported"
data: "[[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], and [[DAGM2007]]"
doi: "10.1016/j.aei.2024.102637"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.aei.2024.102637"
pdf: "paper-inbox/10_processed/Research/2024 - Zhou - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model.pdf"
related_papers:
  - "[[2020 - Denoising Diffusion Probabilistic Models]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[DiffDD]]"
  - "[[Diffusion models]]"
related_datasets:
  - "[[NEU-SEG]]"
  - "[[Magnetic Tile Defects]]"
  - "[[KolektorSDD2]]"
  - "[[DAGM2007]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[NEU-SEG]]"
  - "[[Magnetic Tile Defects]]"
  - "[[KolektorSDD2]]"
  - "[[DAGM2007]]"
source_file: "paper-inbox/10_processed/Research/2024 - Zhou - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Zhou - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Zhou - DiffDD A Surface Defect Detection Framework with Diffusion Probabilistic Model.txt"
artifact_status: "paper available; code not reported"
tags:
  - paper
---
# DiffDD: A Surface Defect Detection Framework with Diffusion Probabilistic Model

## Summary

DiffDD is a diffusion-based semantic segmentation framework for surface defect detection. It combines a pre-trained PvTv2 backbone, pyramid feature guidance, a denoising diffusion probabilistic model, conditional image prior, and semantic restoration module so the diffusion model reconstructs segmentation masks corresponding to inspection images rather than unconstrained generated samples. The paper evaluates on [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], and [[DAGM2007]], reporting strongest overall mAP/AUROC performance among the compared generative, U-shaped, and defect-detection models, but also acknowledges weaker recall on several datasets and high computational cost.

## Paper Type

- Type: research.
- Why: The paper introduces and evaluates a new diffusion-based segmentation architecture for industrial surface defect detection.

## Problem

- Task: [[Surface defect detection]], [[Defect segmentation]], [[Defect classification]].
- Setting: Pixel-level segmentation of product surface defects in industrial inspection images.
- Inputs: RGB inspection images and pixel-wise defect labels during training.
- Outputs: reconstructed binary defect segmentation masks.
- Motivation: Existing generative models often require postprocessing to segment defective regions, and generic diffusion models struggle to preserve semantic correspondence between inspection image and generated mask.
- Assumptions: Feature guidance from a supervised backbone plus conditional image prior can reduce diffusion randomness enough to reconstruct semantically aligned defect masks.

## Contribution

- Claimed: DiffDD is the first diffusion-based framework in the paper's framing for accurately segmenting defects in surface inspection images.
- Claimed: Conditional image prior mitigates semantic discrepancy between inspection images and reconstructed masks.
- Claimed: Feature guidance from a pre-trained backbone improves segmentation-map accuracy by injecting ground-truth-supervised multi-scale features.
- Shown: DiffDD outperforms listed generative models and most defect-detection baselines across the four benchmark datasets, especially on mAP and AUROC.

## Method

- Core idea: Use a diffusion model to reconstruct defect masks while constraining each denoising process with image prior and PvTv2 feature guidance.
- Backbone: PvTv2 extracts four-scale features `(F_r1, F_r2, F_r3, F_r4)` from RGB inspection images.
- Semantic restoration: Higher-level features `F_r3` and `F_r4` are fused and restored to compute a mask loss against ground truth.
- Conditional image prior: The RGB image and noisy label/mask are concatenated into a four-channel tensor so the model learns a one-to-one semantic relation between image and noisy mask input.
- Feature guidance: Upsampled lower-level backbone features `F_r1` and `F_r2` are fused into the U-Net diffusion process to guide reconstruction.
- Loss: The total loss combines diffusion noise-prediction loss with `lambda * mask loss`, where `lambda = 10`.

## Evidence

### Experimental Setup

- Datasets: [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], [[DAGM2007]].
- Image size: all images resized to 256 x 256.
- Framework: PyTorch.
- Hardware: NVIDIA 3090 GPU.
- Optimizer: [[AdamW]].
- Learning rate: `1e-4`.
- Diffusion iterative steps: 40000.
- Time steps: 1000.
- Metrics: [[F1-score]], [[mAP]], [[AU-ROC]], [[IoU]], [[Recall]].

### Main Results

| Dataset | mAP | Recall | AUROC | F1 | IoU | Notes |
|---|---:|---:|---:|---:|---:|---|
| [[NEU-SEG]] | 87.75 | 81.94 | 97.68 | 85.14 | 76.53 | Highest mAP among compared models in Tables 1-2; F1/IoU slightly below CSEPNet in Table 2. |
| [[Magnetic Tile Defects]] | 68.41 | 71.38 | 95.21 | 67.72 | 59.44 | Strong mAP/F1/IoU gains over CSEPNet; recall and AUROC below SegNet. |
| [[KolektorSDD2]] | 78.90 | 58.90 | 95.44 | 74.57 | 64.73 | Higher mAP/F1/IoU than CSEPNet in Table 2. |
| [[DAGM2007]] | 73.24 | 62.08 | 90.45 | 68.28 | 62.00 | Higher mAP/F1/IoU than CSEPNet; AUROC below SegNet in Table 2. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[F1-score]] | segmentation quality | harmonic combination of precision and recall | higher is better | no | Defined in the paper. |
| [[mAP]] | segmentation precision-recall performance | average AP across images | higher is better | yes | The paper emphasizes mAP gains across datasets. |
| [[AU-ROC]] | positive/negative separability | area under ROC curve | higher is better | no | Reported for each dataset. |
| [[IoU]] | overlap between predicted and ground-truth masks | `TP / (TP + FP + FN)` | higher is better | no | Defined in the paper. |
| [[Recall]] | missed-defect sensitivity | `TP / (TP + FN)` | higher is better | no | Weaker than some baselines on MT, KolektorSDD2, and DAGM2007. |

### Ablations

- Backbone choice: PvTv2-b2 with pretraining performs best overall; random initialization substantially reduces PR performance.
- Semantic restoration: A skip connection refines some mask edges but hurts several aggregate metrics, so the simpler SR module is selected.
- Feature guidance: Removing feature guidance causes large drops, especially on Magnetic Tile, with reported decreases around 3% mAP, 8% recall, 5% AUROC, 12% F1, and 9% IoU.
- Hyperparameters: The paper selects 40000 training iterations and 1000 time steps after grid-search experiments on Magnetic Tile and KolektorSDD2.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB surface inspection images.
- Output target: pixel-wise defect segmentation mask.
- Supervision: supervised pixel-level labels.
- Objective: reconstruct accurate defect masks through diffusion while preserving image-mask semantic alignment.

### Model And Training

- Model family: [[Diffusion models]], semantic segmentation, generative model.
- Architecture: PvTv2 backbone, semantic restoration module, U-Net denoising diffusion model, conditional image prior, feature-guidance fusion.
- Parameters: 123.65M.
- Pretraining: PvTv2 backbone uses pre-trained weights in the selected model.
- Fine-tuning: trained on each benchmark dataset.
- Losses: diffusion noise-prediction MSE and mask loss; total loss uses `lambda = 10` for mask loss.
- Optimizer: [[AdamW]].
- Hyperparameters: learning rate `1e-4`; 40000 diffusion iterative steps; 1000 time steps; 256 x 256 input images.
- Seeds: not reported.
- Training compute: NVIDIA 3090 GPU is reported; training time is not reported.

### Data

- Datasets: [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], [[DAGM2007]].
- Data source: industrial surface defect segmentation benchmarks.
- Dataset size: NEU-SEG has 3630 training and 840 test images; Magnetic Tile has 1344 images; DAGM2007 uses 911 defect images for training and 135 for testing; KolektorSDD2 has over 2000 training images and 1000 test images, with 356 defective and 2979 defect-free total images.
- Labels / annotations: pixel-level labels or defect masks.
- Splits: Magnetic Tile selects about 10% from each class for test; DAGM2007 allocates 10% of selected defect images to test; NEU-SEG and KolektorSDD2 use the reported train/test splits.
- Preprocessing: resize to 256 x 256.
- Augmentation: not reported as data augmentation; diffusion reconstructs segmentation masks.
- Synthetic data: not applicable for dataset creation; the method is generative but outputs masks for detection.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: Compare against generative models, U-Net variants, and existing defect-detection models on four datasets.
- Used performance metrics: F1-score, mAP, AUROC, IoU, Recall.
- Primary metric: mAP is treated as the main summary because it is emphasized across comparisons.
- Metric definitions: F1, mAP, IoU, and AUROC are defined in the paper; recall is standard and reported in tables.
- Metric direction / units: higher is better; values are percentages.
- Baselines: AE spatial, AE dense, VAE, cmSalGAN, f-AnoGAN, Trans-GAN, Unet variants, CSEPNet, EMINet, DACNet, EDRNet, SegNet, FDSNet, RFMNet.
- Benchmarks: [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], [[DAGM2007]].
- Statistical tests: not reported.
- Failure cases: Weak recall on MT, KolektorSDD2, and DAGM2007 relative to some discriminative/U-shaped models; difficulty with complex or ambiguous small defective regions.

## Dataset / Benchmark Details

- [[NEU-SEG]]: hot-rolled steel strip defect segmentation benchmark with patches, scratches, and inclusions; 3630 train and 840 test images at 200 x 200.
- [[Magnetic Tile Defects]]: 1344 images with break, blowhole, fray, crack, uneven, and defect-free classes; low contrast and complex backgrounds make detection harder; about 10% per class randomly selected as test.
- [[DAGM2007]]: ten classes of synthetic defects including grooves, dents, scratches, and spots; this paper selects all defect images, using 911 train and 135 test images at 512 x 512.
- [[KolektorSDD2]]: more than 2000 train and 1000 test images around 230 x 630; 356 defective and 2979 defect-free images in total.

## Limitations

- Stated: Recall is weaker than specific defect detection and U-shaped models on several datasets.
- Stated: Reconstruction from pure Gaussian noise can miss complex or ambiguous small defective regions when training data or iterative steps are insufficient.
- Stated: DiffDD is computationally heavy: 123.65M parameters, 67.22G FLOPs, and 471.68 MB model size.
- Stated: The authors identify lighter model volume and stronger reconstruction as future work.
- Inferred: Code availability is not reported, so exact reproduction depends on reimplementation.

## Reproducibility

- Code: not reported.
- Data: four public/known benchmark datasets are named; the paper's data availability statement says no data was used for the research described, which conflicts with the experimental use of benchmark datasets.
- Hyperparameters: image size, optimizer, learning rate, iterative steps, time steps, and mask-loss weight are reported.
- Random seeds: not reported.
- Environment: PyTorch on NVIDIA 3090 GPU.
- Checkpoints / models: not reported.
- Exact preprocessing: resize images to 256 x 256.
- Artifact status: paper available; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect segmentation]], [[Defect classification]]
- Methods: [[DiffDD]], [[Diffusion models]]
- Datasets: [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], [[DAGM2007]]
- Benchmarks: [[NEU-SEG]], [[Magnetic Tile Defects]], [[KolektorSDD2]], [[DAGM2007]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[F1-score]], [[mAP]], [[AU-ROC]], [[IoU]], [[Recall]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[NEU-SEG]] - evaluated for hot-rolled steel strip defect segmentation.
- [[Magnetic Tile Defects]] - evaluated as a low-contrast industrial defect benchmark.
- [[KolektorSDD2]] - evaluated as a real-world production surface-defect segmentation benchmark.
- [[DAGM2007]] - evaluated as a synthetic surface-defect segmentation benchmark.

### Shares Method

- [[DiffDD]] - the paper introduces this diffusion-based segmentation framework.
- [[Diffusion models]] - the segmentation masks are reconstructed through a denoising diffusion process.

### Shares Task

- [[Surface defect detection]] - the paper targets surface defect detection in industrial products.
- [[Defect segmentation]] - the primary output is pixel-level segmentation masks.
- [[Defect classification]] - classification-style metrics and defect-class benchmarks are part of the evaluation, though segmentation is central.

### Shares Metric

- [[F1-score]], [[mAP]], [[AU-ROC]], [[IoU]], and [[Recall]] - all are reported in the quantitative comparisons.

## Questions

- Can DiffDD be compressed enough for practical deployment without losing mask quality?
- How sensitive are the results to random train/test selection on Magnetic Tile and DAGM2007?
- Would a deterministic or latent diffusion variant reduce missed small-defect recall while preserving mAP?
