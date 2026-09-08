---
title: "Few-shot semantic segmentation for industrial defect recognition"
aliases:
  - "IndustrialNet paper"
paper_key: "doi:10.1016/j.compind.2023.103901"
doi: "10.1016/j.compind.2023.103901"
url: "https://doi.org/10.1016/j.compind.2023.103901"
pdf: "paper-inbox/10_processed/Dataset/2023 - Shi - Few-shot semantic segmentation for industrial defect recognition.pdf"
source_file: "paper-inbox/10_processed/Dataset/2023 - Shi - Few-shot semantic segmentation for industrial defect recognition.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Shi - Few-shot semantic segmentation for industrial defect recognition.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Shi - Few-shot semantic segmentation for industrial defect recognition.txt"
authors:
  - "Xiangwen Shi"
  - "Shaobing Zhang"
  - "Miao Cheng"
  - "Lian He"
  - "Xianghong Tang"
  - "Zhe Cui"
year: 2023
venue: "Computers in Industry"
paper_type: "dataset"
status: "processed"
processed_at: "2026-06-03"
topics:
  - "few-shot semantic segmentation"
  - "industrial defect recognition"
  - "industrial defect datasets"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Industrial-5i]]"
  - "[[MVTec AD]]"
  - "[[KolektorSDD]]"
  - "[[KolektorSDD2]]"
  - "[[Magnetic Tile Defects]]"
  - "[[RSDDs]]"
  - "[[BSData]]"
methods:
  - "[[IndustrialNet]]"
  - "[[Few-shot anomaly detection]]"
  - "[[ResNet50]]"
  - "[[U-Net]]"
model_family:
  - "[[Segmentation Models]]"
architectures:
  - "[[IndustrialNet]]"
  - "[[ResNet50]]"
  - "[[U-Net]]"
losses:
  - "cross-entropy"
metrics:
  - "[[mIoU]]"
  - "[[FB-IoU]]"
primary_metric: "[[mIoU]]"
baselines:
  - "FSS-1000"
  - "MMNet"
  - "MSNet"
  - "HSNet"
benchmarks:
  - "[[Industrial-5i few-shot segmentation benchmark]]"
code: "https://github.com/Alex-ShiLei/IndustrialNet"
data: "https://doi.org/10.57760/sciencedb.06908"
data_sources:
  - "MVTec AD"
  - "KolektorSDD"
  - "KolektorSDD2"
  - "Magnetic Tile Defect"
  - "RSDDs"
  - "BSData"
licenses: "Industrial-5i dataset: CC BY-NC-SA 4.0"
related_papers: []
related_concepts:
  - "[[Few-shot anomaly detection]]"
  - "[[Defect segmentation]]"
related_methods:
  - "[[IndustrialNet]]"
  - "[[ResNet50]]"
  - "[[U-Net]]"
related_datasets:
  - "[[Industrial-5i]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[Industrial-5i few-shot segmentation benchmark]]"
---

# Few-shot semantic segmentation for industrial defect recognition

## Summary

The paper introduces [[Industrial-5i]], a 20-product industrial surface-defect dataset for k-shot image segmentation, and evaluates a few-shot segmentation model for recognizing defects in products not seen during training. The proposed [[IndustrialNet]] compares normal support images with a defective query image, estimates abnormal regions from feature-distance maps, and reports stronger mIoU and [[FB-IoU]] than FSS-1000, MMNet, MSNet, and HSNet on the Industrial-5i folds.

## Paper Type

Dataset paper with a benchmarked method. The dataset contribution is central: Industrial-5i defines the products, normal/abnormal sample pools, pixel-level masks, fold protocol, and few-shot evaluation setting. The paper also proposes IndustrialNet and reports comparative segmentation experiments.

## Problem

Industrial defect recognition often faces new product categories and scarce labeled defect masks. The paper formulates this as few-shot semantic segmentation: train on one set of product categories, then segment defects on held-out categories using K normal support images and one defective query image.

## Contribution

- Constructs [[Industrial-5i]] from common industrial datasets and organizes it for k-shot image segmentation across 20 products.
- Applies a comparison-based few-shot segmentation approach to industrial defect detection, using normal support samples and abnormal query samples.
- Reports that an L2 distance feature-comparison design outperforms cosine, prototype, and merged variants in the paper's ablation.

## Method

[[IndustrialNet]] uses a two-branch few-shot segmentation architecture based on MSNet. An ImageNet-pretrained [[ResNet50]] extracts multi-scale support and query features. Support and query features are normalized, each query feature point is matched to the most similar support feature point by cosine similarity, and the L2 distance between the original and replacement features estimates likely defect regions.

Transformation Blocks merge multi-layer, multi-block, and multi-shot distance information. A U-Net-like decoder combines multi-scale features into a binary defect mask. The model is optimized with cross-entropy loss.

## Evidence

### Dataset And Protocol

- Industrial-5i contains 20 product classes.
- Each product has normal samples without defects and abnormal samples with pixel-level binary masks.
- The dataset is split into four folds of five products each.
- Cross-validation uses one fold as the test set and the remaining product categories as training categories.
- Test-time evaluation randomly samples 1000 episodes per test fold.

| Fold | Product | Normal | Abnormal |
|---|---:|---:|---:|
| 0 | Wood | 266 | 60 |
| 0 | Pill | 293 | 141 |
| 0 | BSD | 362 | 426 |
| 0 | Railway | 105 | 94 |
| 0 | Toothbrush | 72 | 30 |
| 1 | Leather | 277 | 92 |
| 1 | Mutou | 867 | 1838 |
| 1 | Metal-Nut | 242 | 70 |
| 1 | Kolektor-SDD2 | 6235 | 436 |
| 1 | Bottle | 229 | 63 |
| 2 | Carpet | 308 | 89 |
| 2 | Hazelnut | 431 | 70 |
| 2 | Phone | 39 | 100 |
| 2 | Tile | 263 | 84 |
| 2 | Grid | 285 | 57 |
| 3 | Magnetic-Tile | 952 | 392 |
| 3 | Capsule | 242 | 109 |
| 3 | Cable | 282 | 92 |
| 3 | Kolektor-SDD | 746 | 52 |
| 3 | Zipper | 272 | 119 |

### Baseline Comparison

| Method | 1-shot mean mIoU | 1-shot FB-IoU | 5-shot mean mIoU | 5-shot FB-IoU |
|---|---:|---:|---:|---:|
| FSS-1000 | 9.81 | 51.52 | 11.51 | 52.06 |
| MMNet | 21.73 | 56.51 | 24.84 | 57.75 |
| MSNet | 24.16 | 57.16 | 24.13 | 57.46 |
| HSNet | 27.44 | 59.58 | 28.40 | 59.85 |
| IndustrialNet | 36.36 | 67.26 | 38.24 | 68.31 |

The abstract reports gains over the best baseline of 8.92 percentage points mIoU and 7.68 percentage points FB-IoU under 1-shot, and 9.84 percentage points mIoU and 8.46 percentage points FB-IoU under 5-shot.

### Support-Shot Ablation

| Support images | Mean mIoU | FB-IoU |
|---:|---:|---:|
| 1 | 36.36 | 67.26 |
| 3 | 38.07 | 68.60 |
| 5 | 38.24 | 68.31 |
| 7 | 38.87 | 69.50 |

### Distance Ablation

| Variant | 1-shot mean mIoU | 1-shot FB-IoU | 5-shot mean mIoU | 5-shot FB-IoU |
|---|---:|---:|---:|---:|
| IndustrialNet-L2 | 36.36 | 67.26 | 38.24 | 68.31 |
| IndustrialNet-Cosine | 26.26 | 58.51 | 27.41 | 59.39 |
| IndustrialNet-Proto | 22.41 | 56.33 | 22.24 | 56.42 |
| IndustrialNet-Merge | 31.57 | 62.35 | 34.30 | 64.71 |

## ML/DL Extraction

- Task formulation: k-shot binary defect segmentation for held-out industrial product categories.
- Inputs: K normal support images and one abnormal query image.
- Outputs: binary defect mask for the query image.
- Backbone: ImageNet-pretrained [[ResNet50]].
- Feature layers: last three ResNet blocks with spatial sizes reported as 55, 28, and 14 after resizing.
- Input preprocessing: support and query images resized to 440 x 440.
- Loss: weighted cross-entropy with reported background and defect weights of 0.2 and 0.8.
- Optimizer: SGD with momentum 0.9 and weight decay 0.00001.
- Metrics: [[mIoU]] and [[FB-IoU]].
- Code: https://github.com/Alex-ShiLei/IndustrialNet.
- Data: https://doi.org/10.57760/sciencedb.06908.

## Limitations

- Industrial-5i is assembled from existing public datasets, so product coverage is tied to the source datasets rather than a single controlled acquisition campaign.
- The paper states that some MVTec AD defects are unsuitable for semantic segmentation and are excluded from the constructed benchmark.
- The reported benchmark evaluates held-out product categories through four folds; deployment behavior outside these 20 product categories is not reported.
- Statistical uncertainty, repeated-run variance, and runtime cost are not reported.

## Connections

### Shares Dataset

- [[Industrial-5i]] is introduced and benchmarked as the paper's core dataset.
- [[MVTec AD]], [[KolektorSDD]], [[KolektorSDD2]], [[Magnetic Tile Defects]], [[RSDDs]], and [[BSData]] are source datasets used to construct Industrial-5i.

### Shares Task

- [[Industrial anomaly detection]] because the task is industrial surface-defect recognition under scarce labels.
- [[Defect segmentation]] because the output is a pixel-level binary mask.

### Shares Method

- [[IndustrialNet]] is the paper's proposed few-shot defect segmentation model.
- [[Few-shot anomaly detection]] captures the data-efficient inspection setting.
- [[ResNet50]] supplies the pretrained feature extractor.
- [[U-Net]] is relevant through the U-Net-like decoder.

### Shares Metric

- [[mIoU]] and [[FB-IoU]] are the reported segmentation metrics.

### Application/domain

- [[Multi-industry anomaly detection]] because Industrial-5i spans multiple products and source datasets.

### Benchmark

- [[Industrial-5i few-shot segmentation benchmark]] captures the four-fold Industrial-5i protocol and metric pair.

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[IndustrialNet]], [[Few-shot anomaly detection]], [[ResNet50]], [[U-Net]]
- Datasets: [[Industrial-5i]], [[MVTec AD]], [[KolektorSDD]], [[KolektorSDD2]], [[Magnetic Tile Defects]], [[RSDDs]], [[BSData]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[mIoU]], [[FB-IoU]]

## Questions

- What exact release files and checksums correspond to ScienceDB version V1?
- Which subsets or defect types were excluded from MVTec AD before constructing Industrial-5i?
- How stable are the reported results across different random episode samples?
