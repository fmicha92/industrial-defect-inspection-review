---
title: "OmniAL: A Unified CNN Framework for Unsupervised Anomaly Localization"
aliases:
  - "OmniAL"
paper_key: "doi:10.1109/cvpr52729.2023.00382"
paper_type: research
year: 2023
venue: "CVPR 2023"
authors:
  - "Ying Zhao"
status: processed
processed_at: 2026-05-22
topics:
  - "unsupervised anomaly localization"
  - "multi-class anomaly detection"
  - "synthetic anomalies"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
methods:
  - "[[OmniAL]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Defect synthesis]]"
  - "[[Adam]]"
model_family:
  - "convolutional neural network"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[SSIM]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "Draem"
  - "JNLD"
  - "separate class models"
  - "unified class models"
code: "not reported"
data:
  - "[[MVTec AD]]"
  - "[[VisA]]"
optimizers:
  - "[[Adam]]"
losses:
  - "MSE loss"
  - "[[SSIM]] loss"
  - "[[Focal loss]]"
evaluation_protocol: "unified and separate unsupervised anomaly localization; image-level AUROC, pixel-level AUROC, pixel AP, PSNR, and SSIM"
doi: "10.1109/CVPR52729.2023.00382"
arxiv: "not reported"
url: "https://doi.org/10.1109/CVPR52729.2023.00382"
pdf: "paper-inbox/10_processed/Research/2023 - Zhao - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Zhao - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Zhao - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Zhao - OmniAL A Unified CNN Framework for Unsupervised Anomaly Localization.txt"
artifact_status: "processed"
tags:
  - "paper"
  - "unsupervised-anomaly-localization"
  - "multi-class-anomaly-detection"
---

# OmniAL: A Unified CNN Framework for Unsupervised Anomaly Localization

## Summary

- OmniAL is a unified CNN framework for unsupervised anomaly localization across many object classes.
- It combines panel-guided synthetic anomaly data, DCSA blocks, and DiffNeck to avoid shortcut reconstruction and improve localization.
- On MVTec AD and VisA unified settings it reports 97.2/87.8 image-AUROC, 98.3/96.6 pixel-AUROC, and 73.4/41.7 pixel-AP.
- The paper also evaluates adversarial robustness against PGD-based anomaly attacks at multiple perturbation levels.

## Paper Type

Research paper. It proposes a CNN architecture and training procedure for one-model-many-classes unsupervised industrial anomaly localization.

## Contribution

- Claimed: a single unified CNN can handle multi-class unsupervised anomaly localization without the severe degradation seen in prior unified models.
- Shown: panel-guided anomaly synthesis improves Draem under unified setting from 88.7/87.1/49.4 to 92.5/94.5/57.4 image-AUROC/pixel-AUROC/pixel-AP.
- Shown: OmniAL includes a robustness study against multi-level adversarial attacks.
- Shown: OmniAL improves over UniAD on MVTec AD by 0.7 image-AUROC points and 1.5 pixel-AUROC points under the unified setting.

## Method

- **Panel-guided anomaly synthesis:** five panel types (`left`, `right`, `top`, `bottom`, `all`) control where synthetic anomalies are placed. Non-`all` panels are randomly sized in `[0.5, 0.8] * ImageWidth` and `[0.5, 0.8] * ImageHeight`.
- **Anomaly texture source:** the anomaly source is selected from augmented normal images or the Describable Textures Dataset; augmentations include resize, crop, flip, and color jitter.
- **Defect levels:** JND-derived fusion weights synthesize easy, medium, and hard anomalies; segmentation masks are refined using SSIM between the anomaly-free image and synthesized anomaly.
- **Reconstruction sub-network:** encoder-decoder CNN with alternating basic blocks and DCSA blocks. Basic blocks use two 3x3 convolutions, instance normalization, and ReLU because unified batches contain multiple classes.
- **DCSA block:** channel attention uses average pooling and two 1x1 convolutions; spatial attention combines average/max pooled features with standard and dilated 3x3 convolution paths, weighted by a factor of 0.1.
- **DiffNeck and localization:** DiffNeck compares reconstructed normal map, reconstructed JND map, and input image through separate and unified paths before the localization sub-network. The localization sub-network uses six scales, skip connections, dilated convolutions from scale 3 to 6, and batch normalization.
- **Training objective:** reconstruction uses MSE and SSIM losses for the JND map and normal image; anomaly localization uses focal loss for the predicted anomaly mask.

## Experimental Setup

- Datasets: [[MVTec AD]] and [[VisA]].
- Training paradigms: separate models per class and a single unified model trained with all-class batches.
- Input sizes: 256 x 256 for MVTec AD and 256 x 320 for VisA, with pixel values in `[0, 1]`.
- Batch sizes: 20 for MVTec AD and 12 for VisA.
- Optimizer: [[Adam]] with initial learning rate `1e-4`.
- Metrics: image-level AUROC, pixel-level AUROC, pixel-level AP, PSNR, and SSIM. The paper notes that pixel-AUROC can favor large anomalous regions, motivating pixel AP.

## Datasets

| Dataset | Source-reported details | Use |
|---|---|---|
| [[MVTec AD]] | 10 object and 5 texture industrial products; 3,629 normal training images and 1,725 test images; 1,258 anomalous test images with pixel-level labels; image resolution ranges from 700 x 700 to 1024 x 1024. | Unified and separate anomaly detection/localization benchmark. |
| [[VisA]] | 10,821 high-resolution RGB images, including 9,621 normal and 1,200 anomalous samples, across 12 objects and 3 domains; acquired with a 4000 x 6000 RGB sensor; anomalies include scratches, dents, color spots, cracks, misplacement, and missing parts. | More complex benchmark with structures, multiple instances, and single instances. |

## Evidence

### Performance Metrics

| Benchmark / paradigm | Image AUROC | Pixel AUROC | Pixel AP | Notes |
|---|---:|---:|---:|---|
| [[MVTec AD]] unified | 97.2 | 98.3 | 73.4 | Single model for all 15 classes. |
| [[MVTec AD]] separate | 97.0 | 97.8 | 73.5 | Per-class model setting. |
| [[VisA]] unified | 87.8 | 96.6 | 41.7 | Single model for all 12 classes. |
| [[VisA]] separate | 94.2 | 96.0 | 44.2 | Per-class model setting. |

### Ablations

| Configuration on MVTec AD | Unified image AUROC | Unified pixel AUROC | Unified pixel AP | Separate image AUROC | Separate pixel AUROC | Separate pixel AP |
|---|---:|---:|---:|---:|---:|---:|
| Baseline with channel attention only | 86.7 | 86.4 | 44.2 | 98.8 | 98.4 | 75.0 |
| Panel-guided anomaly synthesis + baseline | 94.1 | 95.9 | 68.3 | source table dash | source table dash | source table dash |
| Add instance normalization | 95.8 | 97.0 | 69.1 | source table dash | source table dash | source table dash |
| Add DCSA + DiffNeck, final OmniAL | 97.2 | 98.3 | 73.4 | 97.0 | 97.8 | 73.5 |

Panel-guided synthesis also improves existing reconstruction-based models in unified MVTec AD training:

| Method | With panel-guided synthesis I-AUROC / P-AUROC / Pixel-AP | Without panel-guided synthesis I-AUROC / P-AUROC / Pixel-AP |
|---|---|---|
| Draem | 92.5 / 94.5 / 57.4 | 88.7 / 87.1 / 49.4 |
| JNLD | 92.9 / 95.6 / 63.1 | 91.3 / 88.6 / 46.6 |
| OmniAL | 97.2 / 98.3 / 73.4 | 86.6 / 93.7 / 54.4 |

### Robustness

The paper builds adversarial datasets from the anomaly-free MVTec AD training set using PGD perturbations at `epsilon = 4/255`, `epsilon = 8/255`, and targeted `epsilon = 8/255`. The generated adversarial datasets contain 80% synthesized anomaly and 20% normal samples. The extracted text reports that OmniAL has the best robustness performance and less degradation among compared methods, but exact PSNR/SSIM and localization values are only shown in figures.

## Limitations

- Code availability is not reported in the extracted text.
- Production deployment constraints, latency, memory use, and training time are not reported in the extracted text.
- It depends on synthetic anomaly quality for training signal.
- Robustness results are mainly described through figures in the extracted text, so exact adversarial metric values are not available here.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[OmniAL]], [[Unsupervised anomaly localization]], [[Defect synthesis]], [[Adam]]
- Datasets: [[MVTec AD]], [[VisA]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]], [[SSIM]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Shares dataset | OmniAL is evaluated on all 15 MVTec AD classes under a unified model setting. |
| [[VisA]] | Shares dataset | OmniAL is evaluated on all 12 VisA classes. |
| [[Defect synthesis]] | Shares method | Panel-guided synthetic anomalies provide training signal without real defect labels. |
| [[OmniAL]] | Shares method | This paper introduces the unified CNN framework with panel-guided anomaly synthesis, DCSA, and DiffNeck. |
| [[Adam]] | Shares optimizer | OmniAL is trained with Adam at initial learning rate 1e-4. |
| [[2024 - A Diffusion-Based Framework for Multi-Class Anomaly Detection]] | Shares task | Both target multi-class anomaly detection; OmniAL uses CNN reconstruction/localization while DiAD uses diffusion-guided reconstruction. |

## Questions

- How robust is panel-guided synthesis when real anomalies differ strongly from generated panels?
- Does adversarial robustness transfer to real industrial nuisance variation?
