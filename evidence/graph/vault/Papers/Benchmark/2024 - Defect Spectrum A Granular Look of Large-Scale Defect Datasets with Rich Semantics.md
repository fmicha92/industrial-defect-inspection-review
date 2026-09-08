---
title: "Defect Spectrum: A Granular Look of Large-Scale Defect Datasets with Rich Semantics"
aliases:
  - "Defect Spectrum: A Granular Look of Large-Scale Defect Datasets with Rich Semantics"
paper_key: "arxiv:2310.17316"
paper_type: benchmark
year: 2024
venue: "arXiv"
authors:
  - "Shuai Yang"
  - "Zhifei Chen"
  - "Pengguang Chen"
  - "Xi Fang"
  - "Yixun Liang"
  - "Shu Liu"
  - "Yingcong Chen"
status: processed
processed_at: 2026-05-23
topics:
  - industrial defect benchmark
  - semantic defect annotation
  - synthetic defect generation
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Defect Spectrum]]"
  - "[[MVTec AD]]"
  - "[[DAGM2007]]"
methods:
  - "[[Semantic defect annotation]]"
  - "[[Defect-Gen]]"
  - "[[Data augmentation]]"
model_family:
  - "diffusion model"
architectures:
  - "U-Net"
metrics:
  - "[[mIoU]]"
  - "[[Recall]]"
  - "[[FID]]"
  - "[[LPIPS]]"
primary_metric: "[[mIoU]]"
metric_definitions:
  - "mIoU: mean Intersection over Union for defect segmentation."
  - "Recall: image-level recall rate in the manufacturing simulation."
  - "FPR: false positive rate in the manufacturing simulation."
  - "FID: generation fidelity metric; lower is better."
  - "LPIPS: perceptual similarity/diversity metric; higher diversity with similar FID is preferred in this paper."
baselines:
  - "UNet-small"
  - "ResNet18-PSPNet"
  - "ResNet18-DeepLabV3+"
  - "HRNetV2W18-small"
  - "BiseNetV2"
  - "ViT-Tiny-Segmenter"
  - "Segformer-MiT-B0"
  - "HRNet-Mask2Former"
benchmarks:
  - "[[Defect Spectrum]]"
code: "https://github.com/EnVision-Research/DefectSpectrum"
data: "https://huggingface.co/datasets/DefectSpectrum/Defect_Spectrum"
doi: "not reported"
arxiv: "2310.17316"
url: "https://envision-research.github.io/Defect_Spectrum/"
pdf: "paper-inbox/10_processed/Benchmark/2024 - Yang - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics.pdf"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Semantic defect annotation]]"
  - "[[Defect-Gen]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[Defect Spectrum]]"
  - "[[MVTec AD]]"
  - "[[DAGM2007]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[Defect Spectrum]]"
source_file: "paper-inbox/10_processed/Benchmark/2024 - Yang - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Yang - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Yang - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics.txt"
artifact_status: "project page, code, and dataset host reported"
tags:
  - paper
---

# Defect Spectrum: A Granular Look of Large-Scale Defect Datasets with Rich Semantics

## Summary

The paper introduces [[Defect Spectrum]], a benchmark that refines industrial defect datasets with precise pixel-level masks, richer semantic defect labels, multi-defect annotations, and manually refined captions. It targets practical defect inspection needs where defect size, location, and type determine whether products are reworked, accepted, discounted, or distributed.

The paper also introduces [[Defect-Gen]], a two-stage diffusion-based generator for producing paired defective images and masks from scarce defective samples. Synthetic data from Defect-Gen improves segmentation mIoU on Defect Spectrum subsets, with the largest reported improvement being 9.85 mIoU points for DeepLabV3+ on DS-Cotton.

## Paper Type

- Type: benchmark.
- Why: The paper introduces a dataset/benchmark, a generation method, baseline evaluations, and a manufacturing simulation comparing original annotations against Defect Spectrum annotations.

## Problem

- Task: [[Defect segmentation]], [[Defect classification]], and [[Industrial anomaly detection]].
- Setting: industrial defect inspection in closed-loop manufacturing, where quality decisions depend on defect size, position, and type.
- Inputs: industrial inspection images; Defect-Gen also uses paired defect images and masks.
- Outputs: semantic pixel-level defect masks, defect categories, captions, generated image-mask pairs, and quality-control decisions in simulation.
- Motivation: existing datasets often use binary masks, omit defects, use imprecise masks, or collapse multiple defect types into one category.

## Contribution

- Introduces [[Defect Spectrum]] with semantic-abundant, precise, and large-scale annotations.
- Refines existing annotations, fills missing defects, improves contours for subtle defects such as scratches and pits, and distinguishes multiple defect types in one image.
- Adds manually refined captions that describe objects and their defects to support future vision-language-model research.
- Introduces [[Defect-Gen]], a two-stage diffusion generator for scarce-defect data.
- Introduces Defect-Click, an interactive annotation tool tailored to industrial defects that saves about 60% annotation time while the full annotation project still takes 580 working hours.

## Method

- Dataset construction: curated 3,518 high-quality, high-resolution real images from four industrial sources and added 1,920 synthetic samples.
- Annotation improvements: pixel-level annotation for previously image-level or unlabeled data; refined masks for existing pixel-wise datasets; missing defects filled; defect classes made more granular.
- Semantic labels: 125 distinct defect classes and 552 images with multiple defect types.
- Captions: VLM-generated captions manually refined to include object and defect descriptions.
- Defect-Click: built from Focal-Click and adapted using 21 proprietary labeled industrial datasets, multi-level crop training at resolutions from 512 to 3072, and Mask2Former-style edge-sensitive losses with loss ratio 2:5:5 for classification, mask, and dice losses.
- Defect-Gen: concatenates image and one-hot mask channels, models patch-level distribution via reduced receptive field, and uses a large-receptive-field model followed by a small-receptive-field model during inference.

## Evidence

### Dataset Scale

| Dataset | Annotated defective images | Defect types | Pixel-wise label | Multiple defective label | Detailed caption |
|---|---:|---:|---|---|---|
| AITEX | 105 | 12 | yes | no | no |
| AeBAD | 346 | 4 | yes | no | no |
| BeanTech | 290 | 3 | yes | no | no |
| Cotton-Fabric | 89 | 1 | no | no | no |
| DAGM2007 | 900 | 6 | no | no | no |
| KolektorSDD2 | 356 | 1 | yes | no | no |
| MVTec | 1258 | 69 | yes | no | no |
| VISION V1 | 4165 | 44 | yes | yes | no |
| VisA | 1200 | 75 | yes | no | no |
| Defect Spectrum | 3518 + 1920 synthetic | 125 | yes | yes | yes |

### Segmentation Benchmark

| Subset | Best mIoU | Best model | Notes |
|---|---:|---|---|
| DS-MVTec mean | 51.58 | DeepLabV3+ | Best among listed mean scores over MVTec-derived classes |
| DS-VISION mean | 54.12 | HRNet-Mask2Former | Best listed mean over VISION-derived classes |
| DS-DAGM2007 | 86.82 | DeepLabV3+ | No synthetic data generated because DAGM2007 is already synthetic |
| DS-Cotton-Fabric | 64.09 | HRNet-Mask2Former | Transformer-based methods are strong on Cotton-Fabric |

### Synthetic Data Boost

| Model | DS-MVTec mIoU without/with synthetic | DS-VISION mIoU without/with synthetic | DS-Cotton mIoU without/with synthetic |
|---|---:|---:|---:|
| DeepLabV3+ | 51.58 / 55.55 | 52.33 / 53.46 | 48.73 / 58.58 |
| Mask2Former | 45.70 / 50.16 | 54.12 / 55.47 | 64.09 / 65.39 |
| MiT-B0 | 46.45 / 56.21 | 49.62 / 50.75 | 50.52 / 55.86 |

### Manufacturing Simulation

| Annotation source | Recall | False positive rate |
|---|---:|---:|
| Original annotation | 85.33% | 49.60% |
| Defect Spectrum annotation | 96.07% | 16.50% |

The simulation uses expert-defined quality-control thresholds for example classes. For zipper, teeth defects are unacceptable while fabric defects below 4800 pixels are acceptable. For pill, cracks are unacceptable, contamination below 4000 pixels and color stains below 300 pixels are acceptable. For wood, scratches and dents are unacceptable, impurities below 250 pixels and stains below 1000 pixels are acceptable.

## ML / DL Extraction

### Task Formulation

- Defect detection: determine whether an image contains a defect.
- Defect classification: identify defect type.
- Defect segmentation: identify both defect boundaries and defect type.
- Defect Spectrum focuses on the most complex of the three tasks: semantic defect segmentation.

### Model And Training

- Segmentation baselines: UNet-small, ResNet18-PSPNet, ResNet18-DeepLabV3+, HRNetV2W18-small, BiseNetV2, ViT-Tiny-Segmenter, Segformer-MiT-B0, and HRNet-Mask2Former.
- Defect-Gen model family: diffusion-based generative model with two receptive-field settings.
- Defect-Gen training setting: limited defective data, with N = 25 in the few-shot discussion.
- Defect-Gen hyperparameters: switch timestep and small-model receptive field control fidelity/diversity trade-off; detailed selection is in the appendix.

### Data

- Datasets: [[Defect Spectrum]], [[MVTec AD]], [[DAGM2007]], VISION V1, and Cotton-Fabric are directly involved in the benchmark construction or subsets.
- Size: 3,518 real images plus 1,920 synthetic images.
- Labels: 125 distinct defect classes, pixel-wise masks, multi-defect labels, and detailed captions.
- Multi-defect images: 552.
- Synthetic data: generated for DS-MVTec, DS-VISION, and DS-Cotton; no extra data generated for DS-DAGM2007 because DAGM2007 is already synthetic.
- License: not reported in the analysis input.

### Evaluation

- Segmentation metric: [[mIoU]], higher is better.
- Manufacturing simulation metrics: [[Recall]] higher is better; false positive rate lower is better.
- Generation quality: [[FID]] for fidelity and [[LPIPS]] for perceptual diversity/similarity analysis.
- Baseline protocol: evaluate lightweight segmentation methods on each Defect Spectrum subset.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mIoU]] | semantic defect segmentation | Mean Intersection over Union over defect classes | higher is better | yes | Primary segmentation benchmark metric. |
| [[Recall]] | manufacturing simulation | image-level true positive rate | higher is better | no | DS annotations improve recall from 85.33% to 96.07%. |
| FPR | manufacturing simulation | false positive rate | lower is better | no | DS annotations reduce FPR from 49.60% to 16.50%. |
| [[FID]] | generation fidelity | distribution distance between generated and reference images | lower is better | no | Used to select Defect-Gen fidelity/diversity settings. |
| [[LPIPS]] | generation diversity/similarity | perceptual distance between images | context-dependent | no | The paper seeks higher diversity with similar FID. |

## Dataset / Benchmark Details

- Source: project page at https://envision-research.github.io/Defect_Spectrum/.
- Dataset host: https://huggingface.co/datasets/DefectSpectrum/Defect_Spectrum.
- Code: https://github.com/EnVision-Research/DefectSpectrum.
- Collection: curated from four key industrial benchmarks; source-supported subset names are DS-MVTec, DS-VISION, DS-DAGM2007, and DS-Cotton-Fabric.
- Annotation: refined pixel-wise masks, missing-defect completion, multi-class defect labels, and manually refined captions.
- Bias / coverage: multi-industry coverage, but source subsets remain limited to the included industrial image sources.
- Maintenance: not reported in the analysis input.

## Limitations

- Existing source datasets often miss defects, use coarse binary masks, or collapse multiple defect classes in a single image.
- Defective images are scarce; examples given include 900 defective images in DAGM and 1,258 defective images among 5,354 total images in MVTec.
- Vanilla DDPM overfits under scarce-defect settings and can reproduce training samples.
- Patch-level generation improves diversity but loses global structure unless combined with the two-stage large/small receptive-field process.
- The analysis input does not report license terms for Defect Spectrum.

## Reproducibility

- Code: https://github.com/EnVision-Research/DefectSpectrum.
- Data: https://huggingface.co/datasets/DefectSpectrum/Defect_Spectrum.
- Project page: https://envision-research.github.io/Defect_Spectrum/.
- Hyperparameters: switch timestep and small-model receptive field are appendix-level details.
- Annotation effort: 580 working hours with Defect-Click assistance.
- Hardware / training time: not reported in the analysis input.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]], [[Defect classification]]
- Methods: [[Semantic defect annotation]], [[Defect-Gen]], [[Data augmentation]]
- Datasets: [[Defect Spectrum]], [[MVTec AD]], [[DAGM2007]]
- Benchmarks: [[Defect Spectrum]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mIoU]], [[Recall]], [[FID]], [[LPIPS]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[Defect Spectrum]]: introduced and benchmarked with segmentation baselines, synthetic-data augmentation, and manufacturing simulation.
- [[MVTec AD]]: source-supported subset family for DS-MVTec.
- [[DAGM2007]]: source-supported subset family for DS-DAGM2007.

### Shares Method

- [[Semantic defect annotation]]: central dataset contribution.
- [[Defect-Gen]]: two-stage diffusion generator introduced by the paper.
- [[Data augmentation]]: Defect-Gen synthetic image-mask pairs improve downstream segmentation.

### Shares Task

- [[Industrial anomaly detection]]: defect inspection setting and related benchmark context.
- [[Defect segmentation]]: primary benchmark task.
- [[Defect classification]]: supported by semantic defect categories and multi-defect labels.

### Shares Metric

- [[mIoU]]: primary segmentation metric.
- [[Recall]]: manufacturing simulation metric.
- [[FID]] and [[LPIPS]]: generation-quality and diversity metrics.

### Application / Domain

- [[Multi-industry anomaly detection]]: Defect Spectrum combines multiple industrial defect sources and product families.

### Follow-Up Reading

- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]]
- [[2023 - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review]]

## Questions

- Should VISION V1 and Cotton-Fabric be added as standalone dataset notes if later source pages or primary papers are processed?
- What license terms apply to the hosted Defect Spectrum data?
