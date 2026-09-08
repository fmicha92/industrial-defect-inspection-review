---
title: "Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things"
aliases:
  - "Fabric Defect Segmentation System Based on a Lightweight GAN for IIoT"
paper_key: "doi:10.1155/2022/9680519"
paper_type: research
year: 2022
venue: "Wireless Communications and Mobile Computing"
authors:
  - "Bo Li"
  - "Yongkai Zou"
  - "Rongbo Zhu"
  - "Wei Yao"
  - "Jun Wang"
  - "Shaohua Wan"
status: processed
processed_at: 2026-05-31
topics:
  - "fabric defect segmentation"
  - "GAN repair"
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[AITEX]]"
  - "enterprise fabric dataset"
  - "expanded artificial defect dataset"
methods:
  - "[[GAN]]"
  - "[[Defect synthesis]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "lightweight GAN repair model"
metrics:
  - "[[IoU]]"
  - "[[Accuracy]]"
  - "[[SSIM]]"
primary_metric: "[[IoU]]"
baselines:
  - "FCN"
  - "U-Net"
  - "SegNet"
  - "FCNGAN"
  - "U-NetGAN"
  - "SegNetGAN"
benchmarks:
  - "[[AITEX]]"
code: "not reported"
data: "AITEX public; enterprise and expanded datasets not reported as public"
doi: "10.1155/2022/9680519"
url: "https://doi.org/10.1155/2022/9680519"
pdf: "paper-inbox/10_processed/Research/2022 - Li - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things.pdf"
related_methods:
  - "[[GAN]]"
  - "[[Defect synthesis]]"
related_datasets:
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2022 - Li - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Li - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Li - Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things.txt"
artifact_status: "AITEX public; other data not public"
tags:
  - paper
---

# Fabric Defect Segmentation System Based on a Lightweight GAN for Industrial Internet of Things

## Summary

The paper proposes a lightweight GAN-based fabric defect segmentation system. It repairs defective fabric samples, computes the difference between the original and repaired samples, and post-processes the difference map into a defect mask. Experiments use an enterprise fabric dataset, public AITEX, and an expanded artificial-defect dataset.

## Paper Type

- Type: research.
- Why: The paper introduces a segmentation system and evaluates it on multiple fabric datasets.

## Problem

- Task: [[Defect segmentation]] for fabric defects.
- Setting: IIoT textile inspection with weak and small defects.
- Inputs: fabric images with possible defects.
- Outputs: repaired image and binary defect mask.
- Motivation: conventional segmentation networks struggle with weak and small fabric defects and can be heavy for industrial deployment.
- Assumptions: repairing defective regions and differencing against the original can reveal defect areas.

## Contribution

- Claimed: a lightweight three-module system for sample synthesis, defect repair, and defect segmentation without manual annotation for the repair stage.
- Shown: IoU of 77.84% on enterprise fabric samples, 77.85% on AITEX, and 73.6% on an expanded artificial-defect set.
- Inferred: the GAN is used for defect repair and segmentation, not primarily for increasing detector training data.

## Method

- Core idea: train a GAN repair module to reconstruct a defect-free version of a defective fabric image, then segment defects by differencing the original and repaired images.
- Architecture / algorithm: lightweight GAN repair model followed by image-processing operations: difference, denoise, enhance, and binarize.
- Objective / loss: adversarial loss plus MSE-style repair loss; detailed objective equations are in the source.
- Training data: enterprise fabric samples, cropped AITEX samples, and artificial extended defects.
- Data pipeline: enterprise images are cleaned, augmented by rotation/flip/transpose, cut to 128 x 128 patches; AITEX large images are also cropped to 128 x 128.
- Augmentation / synthesis: enterprise set is enlarged by geometric operations and sliding cutting; expanded dataset uses artificial defect samples.
- Inference: repair image, difference from input, threshold/process into mask.
- Deployment constraints: model size 14.4 MB; 7,200 samples processed in about 56 seconds on GPU for repair, about 128 FPS before CPU post-processing.

## ML / DL Extraction

### Data

- Enterprise dataset: 4,360 original samples at 371 x 257 pixels; after removing duplicate and invalid samples, 90 labeled defect samples remain; augmented by seven new forms.
- AITEX: 245 images of 4096 x 256 pixels, seven fabric structures, 140 nondefect images, and 105 images of 12 textile defect types.
- Expanded dataset: 64 artificial defect samples used to test unseen/limited defect types.
- Splits: enterprise test set uses 720 original defect samples and 6,480 normal samples after the described processing; AITEX split details are not fully reported in extracted text.
- Labels / annotations: masks/ground truth used for evaluation.

### Evaluation

- Protocol: compare against FCN, U-Net, SegNet, and their GAN-trained variants.
- Used performance metrics: pixel accuracy, [[IoU]], MAE for repair, [[SSIM]], FPS, model size.
- Primary metric: [[IoU]].
- Statistical tests: not reported.
- Failure cases: image difference can become discontinuous when defect area is very similar to background.

## Evidence

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Proposed model | Enterprise fabric dataset | Pixel accuracy | higher | 0.9968 SegNetGAN | 0.9968 | Same pixel accuracy as SegNetGAN in table |
| Proposed model | Enterprise fabric dataset | IoU | higher | 0.7034 SegNetGAN | 0.7784 | Best table result |
| Proposed model | AITEX | Pixel accuracy | higher | not reported | 99.94% | Cropped AITEX samples |
| Proposed model | AITEX | IoU | higher | not reported | 77.85% | Cropped AITEX samples |
| Proposed model | expanded artificial set | Pixel accuracy | higher | not reported | 99.3% | 64 artificial samples |
| Proposed model | expanded artificial set | IoU | higher | not reported | 73.6% | Tests unseen artificial defects |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[IoU]] | segmentation | TP / (TP + FN + FP) | higher | yes | Source gives formula |
| [[Accuracy]] | pixel accuracy | correctly classified pixels / total pixels | higher | no | Includes background pixels |
| MAE | repair quality | average pixel error | lower | no | Not currently linked as a metric note |
| [[SSIM]] | repair similarity | structural similarity | context-dependent | no | Used for repair analysis |

## Dataset / Benchmark Details

- Source: enterprise assembly-line images, public AITEX, and author-created artificial defects.
- Collection: enterprise samples come from high-speed cameras monitoring production quality.
- Annotation: enterprise valid samples are labeled for defects; AITEX has defect/nondefect structure; evaluation uses ground truth masks.
- Size: 90 valid enterprise defect samples after cleaning; 245 AITEX images; 64 expanded artificial samples.
- Modalities: fabric images.
- License: AITEX public; others not reported.
- Leakage risks: not reported.
- Bias / coverage: enterprise set is small after cleaning; artificial defects are used for unseen-defect testing.

## Limitations

- Stated: discontinuous segmentation can occur when defects are very similar to background.
- Inferred: artificial expanded defects may not fully represent real production defect distributions.

## Reproducibility

- Code: not reported.
- Data: AITEX public; other datasets not reported as public.
- Hyperparameters: crop size 128 x 128; additional hyperparameters are in source equations but not fully extracted here.
- Hardware: GPU speed reported, exact GPU not captured in extracted text.
- Artifact status: partial public dataset support.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect segmentation]]
- Methods: [[GAN]], [[Defect synthesis]], [[Data augmentation]]
- Datasets: [[AITEX]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[IoU]], [[Accuracy]], [[SSIM]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Conditional image-to-image translation generative adversarial network cGAN for fabric defect data augmentation]] | Shares dataset / shares method | Both use AITEX and GAN-based fabric defect processing, but this paper repairs defects while the other synthesizes them for augmentation. |

### Backlinks Updated

- not reported

## Questions

- Are the enterprise and expanded datasets available outside the paper?
- Which exact AITEX defect classes are present after cropping?
