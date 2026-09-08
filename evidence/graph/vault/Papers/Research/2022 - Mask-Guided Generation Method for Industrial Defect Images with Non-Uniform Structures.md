---
title: "Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures"
aliases:
  - "Mask-Guided Generation Method for Industrial Defect Images with Non-uniform Structures"
paper_key: "sha256:27c0d2bb7ac86a7e3d89c37e3f14390e978960c475f28bc2f71dd5fe0608a116"
paper_type: research
year: 2022
venue: "Machines"
authors:
  - "Jing Wei"
  - "Zhengtao Zhang"
  - "Fei Shen"
  - "Chengkan Lv"
status: processed
processed_at: 2026-05-23
topics:
  - "mask-guided defect generation"
  - "non-uniform structures"
  - "industrial defect synthesis"
tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Metal Phone Band Dataset]]"
methods:
  - "[[MDGAN]]"
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
  - "[[CycleGAN]]"
  - "[[U-Net]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[MDGAN]]"
  - "UNet-like generator"
  - "PatchGAN discriminator"
metrics:
  - "[[mIoU]]"
  - "[[F1-score]]"
  - "[[FID]]"
  - "[[SSIM]]"
  - "[[AU-ROC]]"
primary_metric: "[[mIoU]]"
baselines:
  - "CycleGAN with L1 loss"
  - "traditional brightness/rotation/noise augmentation"
benchmarks:
  - "[[MVTec AD]]"
code: "not reported"
data: "not applicable per source data availability statement"
doi: "10.3390/machines10121239"
arxiv: "not reported"
url: "https://doi.org/10.3390/machines10121239"
pdf: "paper-inbox/10_processed/Research/2022 - Wei - Mask-Guided Generation Method for Industrial Defect Images with Non-uniform Structures.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Wei - Mask-Guided Generation Method for Industrial Defect Images with Non-uniform Structures.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Wei - Mask-Guided Generation Method for Industrial Defect Images with Non-uniform Structures.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Wei - Mask-Guided Generation Method for Industrial Defect Images with Non-uniform Structures.txt"
artifact_status: "data not applicable per source"
tags:
  - paper
---

# Mask-Guided Generation Method for Industrial Defect Images with Non-Uniform Structures

## Summary

The paper proposes MDGAN, a mask-guided defect generation adversarial network for industrial defect images with non-uniform structures. MDGAN is designed to preserve real normal backgrounds, control defect shape with binary masks, control defect texture through per-defect training, and output synthetic defect images with pixel-level annotations.

The paper evaluates MDGAN on MVTec AD-derived grid, zipper, capsule, and metal nut items plus a phone-band production-line dataset. Compared with CycleGAN plus L1 loss, MDGAN reports lower FID for most defect types, high background mSSIM in ablations, and improved downstream segmentation when MDGAN-generated samples are added to real training data.

## Paper Type

- Type: research.
- Why: proposes a generative model and evaluates synthesis quality, ablations, downstream segmentation, and transfer experiments.

## Problem

- Task: [[Defect segmentation]], [[Surface defect detection]], and defect image synthesis.
- Setting: industrial products with non-uniform structures and few defective samples.
- Inputs: pseudo-normal background, binary mask, and Gaussian noise.
- Outputs: generated defect image; the input mask serves as pixel-level annotation.
- Motivation: existing learning-based defect generation may falsify background textures, lack independent control of background/shape/texture, and fail to provide accurate segmentation annotations.

## Contribution

- Constructs pseudo-normal backgrounds for defective images to create paired training inputs without relying on CycleGAN.
- Proposes a Background Replacement Module (BRM) to preserve normal backgrounds and control where defects appear.
- Proposes a Double Discrimination Module (DDM) to judge whole-image realism and local defect realism with one discriminator.
- Shows MDGAN-generated samples improve segmentation compared with real-only training and traditional augmentation.
- Demonstrates zero-shot-style defect transfer between datasets with similar defect contents but different backgrounds.

## Method

- Pseudo-normal background: selects a similar normal image, aligns it to the defective image with affine transformation, and replaces defect regions using the binary mask.
- Generator: UNet-like conditional generator taking Gaussian noise, pseudo-normal background, and a 0-1 binary mask.
- Discriminator: PatchGAN-style discriminator that takes a defect image and binary mask.
- BRM: fuses real background features into feature maps at mask-specified positions so output backgrounds are preserved outside defect regions.
- DDM: uses the mask to extract local defect information while retaining whole-image features, helping one discriminator judge both local and global realism.
- Losses: defect reconstruction, diversity, normal-background reconstruction, gradient boundary loss, WGAN-GP-style gradient penalty, and adversarial loss.

## Evidence

### Experimental Setup

- Public dataset source: [[MVTec AD]].
- MVTec AD items: grid, zipper, capsule, and metal nut.
- Production-line dataset: [[Metal Phone Band Dataset]], with dirty, roll, and scratch defects.
- Synthetic-mask sources: cropped MVTec AD masks and Perlin-noise-based binary masks.
- MDGAN training: per defect type under each item; rotation, flipping, and random cropping augmentation.
- Hardware: one NVIDIA GeForce RTX 3090 GPU with an Intel Xeon Gold 6226R CPU server.
- MDGAN optimizer: Adam with beta1 = 0.5, beta2 = 0.999, batch size 20, learning rate 0.0004, and 500 iterations.

### Main Results

| Experiment | Metric | Source-supported result |
|---|---|---|
| Background preservation ablation | mSSIM | MDGAN reports higher background mSSIM than the no-BRM ablation for all listed defect types. |
| CycleGAN comparison | [[FID]] | MDGAN reports lower FID than CycleGAN + L1 for most defect types; CycleGAN is lower on grid-glue, grid-bent, and zipper-fb. |
| Downstream segmentation | [[mIoU]], [[F1-score]] | Adding MDGAN samples to real training data improves mean results over RAW and AUG across the item-level table. |
| Best reported segmentation gain | [[mIoU]], [[F1-score]] | IoU improvement up to 7.3% for UNet-capsule and F1 improvement up to 6.2% for sResNet-capsule. |
| Defect transfer | AUC | Transferred-sample-only training reaches AUC up to 0.971 for phone band2 and 0.991 for phone cover glass. |

### Segmentation Results

| Dataset | UNet RAW mIoU | UNet AUG mIoU | UNet EL mIoU | sResNet RAW mIoU | sResNet AUG mIoU | sResNet EL mIoU |
|---|---:|---:|---:|---:|---:|---:|
| Metal nut | 0.742 | 0.748 | 0.768 | 0.733 | 0.738 | 0.751 |
| Grid | 0.619 | 0.603 | 0.652 | 0.636 | 0.652 | 0.657 |
| Zipper | 0.732 | 0.719 | 0.775 | 0.745 | 0.723 | 0.764 |
| Capsule | 0.548 | 0.571 | 0.621 | 0.472 | 0.483 | 0.561 |
| Phone band | 0.656 | 0.646 | 0.666 | 0.650 | 0.653 | 0.681 |

## Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mIoU]] | downstream segmentation | mean Intersection over Union | higher | yes | reported for UNet and sResNet |
| [[F1-score]] | downstream segmentation | F1 coefficient | higher | no | reported with mIoU |
| [[FID]] | generated image quality | distance between generated and real defect feature distributions | lower | no | used against CycleGAN + L1 |
| [[SSIM]] | background preservation | background structural similarity | higher | no | reported as mSSIM in BRM ablation |
| [[AU-ROC]] | transfer segmentation evaluation | area under curve | higher | no | source table labels transfer metric as AUC |

## Dataset / Benchmark Details

- MVTec AD-derived items: metal nut, grid, zipper, and capsule.
- Phone-band defects: scratch, roll, and dirty.
- Zipper-combined samples include multiple defect classes in one image and are used only for segmentation testing.
- Training and segmentation sets are built from the same original images; separate real defect samples are preserved for segmentation testing.
- Source data availability statement: not applicable.

## Limitations

- Since binary masks are directly given by test sets, generated defect-shape feature and diversity can be limited.
- The authors propose future work on generating both defect images and annotations with networks to enrich defect shapes.
- Code availability is not reported.
- The transfer experiments require similar defect contents between source and target datasets.

## Reproducibility

- Code: not reported.
- Data: MVTec AD is named; phone-band and transfer datasets are described but availability is not reported.
- Training details: architecture, losses, optimizer, hyperparameters, iteration count, and hardware are reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Surface defect detection]]
- Methods: [[MDGAN]], [[GAN]], [[Synthetic data generation]], [[CycleGAN]], [[U-Net]]
- Datasets: [[MVTec AD]], [[Metal Phone Band Dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mIoU]], [[F1-score]], [[FID]], [[SSIM]], [[AU-ROC]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Source dataset | MDGAN constructs training and testing sets from MVTec AD items and masks. |
| [[Metal Phone Band Dataset]] | Production-line dataset | Phone-band defects are used for synthesis and segmentation tests. |
| [[CycleGAN]] | Generative baseline | MDGAN is compared against CycleGAN + L1 in qualitative and FID experiments. |
| [[U-Net]] | Downstream segmentation model | UNet is trained with RAW, AUG, and MDGAN-generated EL sets. |

## Questions

- How sensitive is MDGAN to the manually or externally supplied binary mask distribution?
- Would jointly generated masks and images preserve annotation accuracy?
- How far can the transfer setup move before source and target defect contents become too dissimilar?
