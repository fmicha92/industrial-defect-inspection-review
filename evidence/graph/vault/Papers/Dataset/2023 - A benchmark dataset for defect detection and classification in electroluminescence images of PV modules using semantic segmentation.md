---
title: "A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation"
aliases:
  - "Benchmark dataset for defect detection and classification in EL images of PV modules"
paper_key: "sha256:51e13055e62ae617098591374e2be639ef0e1498d7cc36fb3c3ee00e4d87a83d"
paper_type: "dataset"
year: 2023
venue: "Systems and Soft Computing"
authors:
  - "Lawrence Pratt"
  - "Jana Mattheus"
  - "Richard Klein"
affiliations:
  - "CSIR"
  - "University of the Witwatersrand"
status: "processed"
topics:
  - "electroluminescence inspection"
  - "solar-cell defect segmentation"
  - "semantic segmentation benchmark"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[BenchmarkELimages]]"
methods:
  - "[[U-Net]]"
  - "[[PSPNet]]"
  - "[[DeepLabV3+]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Segmentation Models]]"
metrics:
  - "[[mIoU]]"
  - "[[Recall]]"
primary_metric: "[[mIoU]]"
baselines:
  - "U-Net_12"
  - "U-Net_25"
  - "PSPNet"
  - "DeepLabv3+"
doi: "10.1016/j.sasc.2023.200048"
url: "https://doi.org/10.1016/j.sasc.2023.200048"
data: "https://github.com/TheMakiran/BenchmarkELimages"
licenses:
  - "article: CC BY-NC-ND 4.0"
  - "dataset: not reported"
related_papers:
  - "[[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]]"
  - "[[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]]"
related_concepts:
  - "[[Defect segmentation]]"
  - "[[Solar cell defect detection]]"
related_methods:
  - "[[U-Net]]"
  - "[[PSPNet]]"
  - "[[DeepLabV3+]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[BenchmarkELimages]]"
  - "[[ELPV Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Pratt - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Pratt - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation.txt"
source_file: "paper-inbox/10_processed/Dataset/2023 - Pratt - A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation.pdf"
---
# A benchmark dataset for defect detection and classification in electroluminescence images of PV modules using semantic segmentation

## Summary

Pratt, Mattheus, and Klein introduce [[BenchmarkELimages]], a public benchmark dataset for multi-class semantic segmentation in electroluminescence images of crystalline silicon solar cells. The paper reports 593 labelled 512 x 512 cell images with pixel-level masks for 24 classes, then evaluates U-Net, PSPNet, and DeepLabv3+ variants under three class-weighting schemes. DeepLabv3+ with custom class weights produces the strongest average mIoU across cracks, inactive areas, and gridline defects, while recall is high for cracks and gridline defects but precision remains limited by dilated predictions and mask alignment difficulty.

## Paper Type

Dataset paper. The central contribution is [[BenchmarkELimages]], including pixel-level ground-truth masks for EL defect segmentation, plus baseline semantic-segmentation results across twelve model/class-weight combinations.

## Problem

Electroluminescence images reveal cracks, inactive areas, gridline defects, corrosion, and other solar-cell problems that may not be visible to the naked eye. Image-level classification does not quantify defect location or extent, so the paper frames pixel-level semantic segmentation as a way to detect, localize, and measure multiple defects on the same solar cell.

## Contribution

- Introduces a public benchmark dataset of 593 EL solar-cell images with pixel-level labels for 12 intrinsic cell features and 12 extrinsic defects.
- Compares four semantic-segmentation architectures, each trained with equal, inverse, and custom class weights.
- Reports baseline mIoU and recall behavior for cracks, inactive areas, gridline defects, ribbon interconnects, and cell spacing.

## Method

### Dataset Construction

- Sources: three private sources and two public sources.
- Private sources: CSIR Energy Centre, CFV Labs, and ARTsolar.
- Public sources: CWRU SDLE Research Center and ZAE Bayern.
- Candidate pool: more than 80,000 images across the five data sources.
- Final labelled set: 593 cell-level EL images.
- Image preparation: final images are 512 x 512, with a full solar cell centered and adjacent cells, module edge, or padding included depending on source and cell location.
- Crystal types: roughly equal mono-crystalline and multi-crystalline wafers.
- Annotation process: a PV expert curated images and identified 12 intrinsic features plus 12 extrinsic defects. Labelers used GIMP to create RGB ground-truth masks with unique color codes, followed by pixel-code correction and expert review.
- Split: 50 images with cracks, gridline defects, and inactive areas assigned to test; 54 images selected for validation; the remaining images assigned for training.
- Augmentation: training images were augmented with 180-degree rotation, mirror, and flip, yielding 896 mono-crystalline and 1,016 multi-crystalline training images, for 1,912 training images total.

### Models

The paper trains twelve fully supervised models:

| Model group | Architecture | Trainable parameters | Class weights |
|---|---:|---:|---|
| 1-a/b/c | U-Net, Divam implementation | 12,333,720 | equal, inverse, custom |
| 2-a/b/c | U-Net, Tomar implementation | 25,858,887 | equal, inverse, custom |
| 3-a/b/c | PSPNet, Kamikawa implementation | 58,038,784 | equal, inverse, custom |
| 4-a/b/c | DeepLabv3+, Yakubovskiy and Kawakita implementation | 22,443,368 | equal, inverse, custom |

The loss is weighted cross entropy. The custom class weights emphasize cracks, gridlines, inactive regions, and ribbons to improve detection of small or inspection-relevant structures.

## Evidence

### Metrics

- Primary reported metric: median intersection over union, abbreviated as mIoU in the paper.
- Secondary reported metric: median recall, abbreviated as mRcl.
- Focus classes: cracks, inactive areas, gridline defects, ribbon interconnects, and cell spacing.
- Direction: higher is better for both mIoU and recall.

### Results

- Features are segmented more accurately than defects across all models. The paper attributes this to feature pixel area: spacing and ribbons occupy roughly 10 to 20 times more pixels than cracks, inactive areas, and gridline defects.
- DeepLabv3+ with custom class weights has the highest average mIoU for the three selected defect classes.
- Highest reported average defect mIoU: 0.28 for DeepLabv3+ with custom class weights.
- Crack mIoU remains low even for the best model: 25%.
- DeepLabv3+ with custom class weights reports high recall for narrow defects: 0.86 for cracks and 0.85 for gridline defects.
- Models with inverse and custom class weights tend to produce dilated cracks and gridline defects.
- Equal class weights reduce dilation but also predict fewer or smaller cracks.
- The paper states that low precision is driven more by dilated predictions of the correct features and defects than by spurious detections.

## ML/DL Extraction

- Task formulation: multi-class semantic segmentation of solar-cell EL images.
- Input: 512 x 512 electroluminescence images of crystalline silicon solar cells.
- Output: per-pixel class labels from 0 to 23.
- Training regime: fully supervised semantic segmentation.
- Architectures: U-Net_12, U-Net_25, PSPNet, DeepLabv3+.
- Loss: weighted cross entropy.
- Class weighting: equal weights, inverse median-pixel-percentage weights, and custom engineering-judgment weights.
- Augmentation: 180-degree rotation, mirroring, and flipping.
- Evaluation set: 50 test images.
- Hardware/compute: CHPC South Africa provided computational resources; detailed GPU/CPU configuration is not reported.
- Code availability: model code was adapted from GitHub repositories; exact training-code release from the authors is not reported.
- Data availability: [[BenchmarkELimages]] is published on GitHub.

## Limitations

- The dataset is relatively small for dense segmentation: 593 labelled images before augmentation.
- Ground-truth alignment errors are especially damaging for long, narrow defects such as cracks and gridline defects.
- mIoU is low for defects even when recall is high, because predicted masks are often dilated relative to the ground truth.
- The paper focuses detailed quantitative analysis on three defects and two features rather than all 24 classes.
- Future work is needed to use the larger unlabelled pool, improve ground-truth masks, and add newer defect or feature classes such as half-cut cells, scuffs, and edge corrosion.
- Dataset license is not reported by the GitHub repository.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect segmentation]]
- Methods: [[U-Net]], [[PSPNet]], [[DeepLabV3+]], [[Data augmentation]]
- Datasets: [[BenchmarkELimages]], [[ELPV Dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[mIoU]], [[Recall]]

### Introduces Dataset

- [[BenchmarkELimages]] - public benchmark for EL solar-cell semantic segmentation with labelled and unlabelled releases.

### Shares Task

- [[Solar cell defect detection]] - the paper detects cracks, inactive areas, gridline defects, corrosion, and other defects in solar-cell EL images.
- [[Defect segmentation]] - the output is a pixel-level defect and feature mask.

### Shares Method

- [[U-Net]] - two U-Net implementations are evaluated as semantic segmentation baselines.
- [[PSPNet]] - evaluated as a pyramid-pooling segmentation baseline.
- [[DeepLabV3+]] - best reported architecture for average defect mIoU when combined with custom class weights.
- [[Data augmentation]] - training images are expanded by rotation, mirroring, and flipping.

### Shares Metric

- [[mIoU]] - primary segmentation performance metric.
- [[Recall]] - secondary metric used to evaluate defect detection sensitivity.

### Application/domain

- [[Solar cells and photovoltaic]] - the dataset and experiments target PV module EL inspection.

### Follow-up reading

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] - evaluates later solar-cell EL segmentation models and datasets.
- [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] - another solar-cell EL segmentation and augmentation paper.

## Questions

- How should later repository releases with 29 labels be benchmarked against the 24-class setup reported in the paper?
- Would boundary-aware metrics better represent useful crack localization than pixel-exact mIoU alone?
- How much do results change if the unlabelled Dropbox-linked data is used for semi-supervised or self-supervised pretraining?
