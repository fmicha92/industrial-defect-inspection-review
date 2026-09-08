---
title: "Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection"
paper_key: "doi:10.3390/s24186016"
paper_type: research
year: 2024
venue: "Sensors"
authors:
  - "Jon Leinena"
  - "Fatima A. Saiz"
  - "Inigo Barandiaran"
status: processed
processed_at: 2026-06-11
topics:
  - "visual defect segmentation"
  - "latent diffusion"
  - "LoRA"
tasks:
  - "[[Defect segmentation]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-SEG]]"
methods:
  - "[[LoRA-adapted diffusion augmentation]]"
  - "[[Diffusion models]]"
  - "[[Data augmentation]]"
architectures:
  - "[[DeepLabV3+]]"
  - "[[FPN]]"
metrics:
  - "[[mIoU]]"
primary_metric: "[[mIoU]]"
doi: "10.3390/s24186016"
url: "https://doi.org/10.3390/s24186016"
pdf: "paper-inbox/10_processed/Research/2024 - Leinena - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection.pdf"
code: "not reported"
data: "NEU-SEG is used; generated synthetic dataset is reported as publicly published, but URL is not captured in the extracted text"
related_methods:
  - "[[LoRA-adapted diffusion augmentation]]"
  - "[[Diffusion models]]"
related_datasets:
  - "[[NEU-SEG]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Leinena - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Leinena - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Leinena - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection.txt"
tags:
  - paper
---
# Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection

## Summary

The paper fine-tunes Stable Diffusion with LoRA to generate steel surface defect images for [[NEU-SEG]] segmentation augmentation. Generated masks are produced with a DeepLabV3+ model trained on original data and then manually reviewed. The strongest reported setting uses 37% synthetic data, improving DeepLabV3+ from 71.31 to 76.20 mIoU and FPN from 72.39 to 76.70 mIoU.

## Paper Type

- Type: research.
- Why: The paper proposes a generative augmentation workflow and reports segmentation performance under synthetic-data ratios.

## Problem

- Task: [[Defect segmentation]] for steel surface inspection.
- Setting: limited pixel-level defect masks in [[NEU-SEG]].
- Inputs: 200x200 steel surface defect images.
- Outputs: pixel-level defect segmentation masks.

## Contribution

- Claimed: LoRA-adapted latent diffusion can generate useful steel defect training images for segmentation networks.
- Shown: Moderate synthetic ratios improve DeepLabV3+ and FPN mIoU, while high synthetic ratios can degrade performance.
- Inferred: Synthetic-data proportion is a key control variable; the best ratio in this paper is 37%.

## Method

- Generator: Stable Diffusion fine-tuned with LoRA on NEU-SEG defect classes.
- Masking: a DeepLabV3+ model trained on original data predicts masks for synthetic images; masks are manually reviewed and corrected.
- Downstream models: [[DeepLabV3+]] and [[FPN]].
- Conventional augmentation: horizontal/vertical flips, Gaussian noise, CLAHE, brightness, gamma, sharpening, and blurring.
- Synthetic ratios: 0%, 16%, 28%, 37%, 50%, 56%, 63%, 72%, 84%, and 100%.

## Evidence

| Result | Dataset / task | Metric | Baseline | Paper result | Notes |
|---|---|---|---:|---:|---|
| DeepLabV3+ augmentation | [[NEU-SEG]] segmentation | [[mIoU]] | original only 71.31 | 37% synthetic 76.20 | Higher is better. |
| FPN augmentation | [[NEU-SEG]] segmentation | [[mIoU]] | original only 72.39 | 37% synthetic 76.70 | Higher is better. |
| Excess synthetic data | [[NEU-SEG]] segmentation | [[mIoU]] | DeepLabV3+ original only 71.31 | 84% synthetic 66.12 | Too much synthetic data degrades performance. |
| Synthetic-only training | [[NEU-SEG]] segmentation | [[mIoU]] | DeepLabV3+ original only 71.31 | 100% synthetic 63.80 | Synthetic-only underperforms mixed training. |

## Dataset / Benchmark Details

- [[NEU-SEG]]: 3,630 grayscale 200x200 steel surface images with pixel-level annotations for inclusion, patches, and scratches.
- Split: 2,541 train, 1,089 validation, and 840 test images.

## Limitations

- The paper identifies the need to compare against other augmentation methods on the same NEU-SEG test set.
- It proposes testing Transformer architectures and other datasets as future work.
- Too much synthetic data can distort the training distribution.
- Code URL: not reported in the extracted text.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]]
- Methods: [[LoRA-adapted diffusion augmentation]], [[Diffusion models]], [[Data augmentation]]
- Datasets: [[NEU-SEG]]
- Domains: [[Metal inspection]]
- Metrics: [[mIoU]]
- Models: [[DeepLabV3+]], [[FPN]]

### Relationship Notes

- Shares dataset: [[NEU-SEG]].
- Shares method: [[LoRA-adapted diffusion augmentation]], [[Diffusion models]], and [[Data augmentation]].
- Shares metric: [[mIoU]].
- Application/domain: [[Metal inspection]].

## Questions

- Are the manually corrected synthetic masks reproducible enough for independent comparison?
- Does the optimal synthetic ratio transfer across other steel defect segmentation datasets?
