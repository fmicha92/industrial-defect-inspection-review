---
title: "Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network"
aliases:
  - "TMFFNet pharmaceutical bag sealing defect detection"
paper_key: "doi:10.1371/journal.pone.0343395"
paper_type: "research"
year: 2026
venue: "PLOS One"
authors:
  - "Liqiang Wang"
  - "Ziyang Leng"
  - "Cunmin Jiang"
  - "Rui Hua"
status: "processed"
topics:
  - "thermal sealing defect detection"
  - "physics-guided defect synthesis"
tasks:
  - "[[Pharmaceutical bag sealing defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Pharmaceutical packaging inspection]]"
datasets:
  - "[[Pharmaceutical bag thermal sealing defect dataset]]"
  - "[[Glass Bangle Defect Detection Classification]]"
methods:
  - "[[TMFFNet]]"
  - "[[Physics-guided thermal defect synthesis]]"
  - "[[Ghost module]]"
model_family:
  - "[[Computer Vision Models]]"
architectures:
  - "[[TMFFNet]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + TN + FP + FN)"
  - "Precision: TP / (TP + FP)"
  - "Recall: TP / (TP + FN)"
  - "F1-score: 2 * precision * recall / (precision + recall)"
baselines:
  - "VGG16"
  - "ResNet18"
  - "EfficientNet-b3"
  - "MobileNetV3-Small"
  - "ViT-B/16"
benchmarks:
  - "Pharmaceutical bag thermal sealing defect dataset"
  - "Glass Bangle Defect Detection Classification"
  - "Leather Defect Classification"
code: "not reported"
data: "https://doi.org/10.5281/zenodo.18616983"
doi: "10.1371/journal.pone.0343395"
arxiv: "not reported"
url: "https://doi.org/10.1371/journal.pone.0343395"
pdf: "paper-inbox/10_processed/Research/2026 - Wang - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network.pdf"
source_file: "paper-inbox/10_processed/Research/2026 - Wang - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2026 - Wang - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network.md"
extracted_text: "paper-inbox/90_processing/text/2026 - Wang - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network.txt"
related_concepts:
  - "[[Class imbalance]]"
  - "[[Data augmentation]]"
  - "[[Nondestructive testing]]"
related_methods:
  - "[[TMFFNet]]"
  - "[[Physics-guided thermal defect synthesis]]"
  - "[[Ghost module]]"
related_datasets:
  - "[[Pharmaceutical bag thermal sealing defect dataset]]"
  - "[[Glass Bangle Defect Detection Classification]]"
related_domains:
  - "[[Pharmaceutical packaging inspection]]"
related_tasks:
  - "[[Pharmaceutical bag sealing defect detection]]"
  - "[[Defect classification]]"
processed_at: "2026-06-03"
---
# Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network

## Summary

The paper proposes a nondestructive thermal-imaging framework for detecting sealing defects in pharmaceutical plastic bags. It combines [[Physics-guided thermal defect synthesis]] with [[TMFFNet]], a dual-branch temporal classifier that processes three thermal frames from the same heat-sealing cycle.

The paper reports a severe class imbalance in the real data: 2281 normal heat-sealing cycles and 28 defective cycles. Physics-guided synthesis expands the defective class with 2104 generated samples, yielding 4385 total samples. TMFFNet reports 0.9809 test accuracy on the pharmaceutical-bag dataset and better balanced precision/recall than the listed baseline networks.

## Paper Type

Research paper. It introduces a thermal inspection dataset, a physics-guided augmentation method, and a dual-branch temporal classification network.

## Problem

Liquid pharmaceutical bags can have tiny heat-seal defects that leak slowly and may not be detected during manual squeezing inspection. Manual sampling is inefficient, subjective, and not suitable for full inspection. Optical cameras can miss micro-gap leakage, while X-ray equipment is costly and may affect preparation stability.

## Contribution

- Collects thermal imaging data from heat-sealed pharmaceutical plastic bags and identifies localized abnormal temperature elevation greater than 1 degree Celsius as a defect cue.
- Proposes [[Physics-guided thermal defect synthesis]] using polynomial contour modeling, dual-Gaussian thermal diffusion, and geometrically constrained fusion.
- Proposes [[TMFFNet]], a dual-branch temporal network using global-local feature fusion and SE-Dense channel-aware enhancement.
- Reports 0.9809 test accuracy and stronger balanced performance than VGG16, ResNet18, EfficientNet-b3, MobileNetV3-Small, and ViT-B/16.

## Method

The data are captured with a Hikmicro HM-TD2C68E-25/Q thermal detector during plastic-bag heat sealing. Characteristic frames are extracted from each cycle using temperature-based feature recognition, and samples with localized abnormal temperature elevation greater than 1 degree Celsius at the heat-sealed region are labeled as leakage defects.

The augmentation method extracts empirical defect contours with Sobel edge detection, fits third-order polynomials, mixes fitted curves with stochastic fourth-order curves, simulates thermal diffusion through dual-Gaussian blurring, and multiplies the resulting masks with normal images. Boundary-aware positioning and manual inspection are used to remove invalid synthetic samples.

TMFFNet uses three temperature matrices sampled every other frame. The global input is center-cropped from 640 x 512 and resized to 256 x 256; the local input is cropped around the sealing-line region. The primary branch uses Ghost-Residual Blocks and hierarchical global-local attention fusion. The secondary branch uses SE-Dense blocks to emphasize defect-sensitive channels and suppress wrinkle-like background features. The fused features are classified with cross-entropy loss.

## Evidence

### Dataset

| Dataset | Size | Split/protocol | Notes |
|---|---:|---|---|
| [[Pharmaceutical bag thermal sealing defect dataset]] | 4385 samples after augmentation | normal samples split 8:2 train/test; all synthetic defects used for training; all 28 real defects retained for testing | 2281 real normal, 28 real defective, 2104 synthetic defective |
| [[Glass Bangle Defect Detection Classification]] | 1080 images | generalization benchmark | three classes: good, broken, defect |
| Leather Defect Classification | not reported in extracted text | generalization benchmark | five-class leather defect classification dataset |

### Performance Metrics

| Metric | Definition | Direction | Primary | Context |
|---|---|---|---|---|
| [[Accuracy]] | `(TP + TN) / (TP + TN + FP + FN)` | higher | yes | binary defect classification |
| [[Precision]] | `TP / (TP + FP)` | higher | no | false-alarm control |
| [[Recall]] | `TP / (TP + FN)` | higher | no | missed-defect control |
| [[F1-score]] | harmonic mean of precision and recall | higher | no | balance under class imbalance |

### Reported Results

| Dataset | Model | Accuracy | Precision | Recall | F1-score |
|---|---|---:|---:|---:|---:|
| Pharmaceutical bag thermal sealing defect dataset | TMFFNet | 0.9809 | 0.3077 | 0.6667 | 0.4211 |
| Pharmaceutical bag thermal sealing defect dataset | VGG16 | 0.5903 | 0.0248 | 1.0000 | 0.0484 |
| Pharmaceutical bag thermal sealing defect dataset | ResNet18 | 0.6493 | 0.0288 | 1.0000 | 0.0561 |
| Pharmaceutical bag thermal sealing defect dataset | EfficientNet-b3 | 0.8785 | 0.00294 | 0.3333 | 0.0541 |
| Pharmaceutical bag thermal sealing defect dataset | MobileNetV3-Small | 0.8090 | 0.0357 | 0.6667 | 0.0678 |
| Pharmaceutical bag thermal sealing defect dataset | ViT-B/16 | 0.7292 | 0.0240 | 1.0000 | 0.0449 |

On [[Glass Bangle Defect Detection Classification]], TMFFNet reports 0.8750 accuracy, 0.8736 precision, 0.8823 recall, and 0.8750 F1-score. On Leather Defect Classification, TMFFNet reports 0.9929 accuracy, 0.9928 precision, 0.9927 recall, and 0.9927 F1-score.

## ML/DL Extraction

- Task formulation: binary classification of normal versus defective heat-sealed pharmaceutical plastic bags.
- Inputs: three thermal frames sampled within one heat-sealing cycle, using global and local crops.
- Outputs: normal or leakage-defective class.
- Architecture: dual-branch temporal network with Ghost-Residual global-local fusion branch and SE-Dense channel-aware branch.
- Loss: cross-entropy.
- Data synthesis: hybrid polynomial defect contours, dual-Gaussian thermal diffusion, geometric fusion into normal thermal samples.
- Baselines: VGG16, ResNet18, EfficientNet-b3, MobileNetV3-Small, and ViT-B/16.
- Artifacts: Zenodo data repository is public; code is not reported.

## Limitations

- Only three sampled frames from a single cycle are used, and the paper states that this weakens temporal modeling.
- The real defective sample count is extremely small, which can cause large fluctuations in experimental results.
- Future work is needed to collect more real defect samples, add stronger temporal models such as bidirectional LSTM or Transformer, and improve compatibility with high-speed production lines.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Pharmaceutical bag sealing defect detection]], [[Defect classification]]
- Methods: [[TMFFNet]], [[Physics-guided thermal defect synthesis]], [[Ghost module]]
- Datasets: [[Pharmaceutical bag thermal sealing defect dataset]], [[Glass Bangle Defect Detection Classification]]
- Domains: [[Pharmaceutical packaging inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Shares Dataset

- [[Pharmaceutical bag thermal sealing defect dataset]]: introduced and used for the main thermal sealing-defect experiments.
- [[Glass Bangle Defect Detection Classification]]: used as a generalization benchmark.

### Shares Task

- [[Pharmaceutical bag sealing defect detection]]: primary application.
- [[Defect classification]]: the network performs class prediction rather than localization.

### Shares Method

- [[Physics-guided thermal defect synthesis]]: used to address class imbalance from scarce real defective samples.
- [[Ghost module]]: used inside Ghost-Residual Blocks for efficient feature extraction.

### Application/Domain

- [[Pharmaceutical packaging inspection]]: drug packaging quality inspection is the application domain.

## Questions

- Code release is not reported.
- License for the Zenodo dataset is not reported in the processed text.
- The extracted text does not identify the Leather Defect Classification dataset host or license.
