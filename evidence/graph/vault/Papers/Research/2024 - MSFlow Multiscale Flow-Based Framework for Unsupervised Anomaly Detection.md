---
title: "MSFlow: Multiscale Flow-Based Framework for Unsupervised Anomaly Detection"
aliases:
  - "MSFlow"
paper_key: "doi:10.1109/tnnls.2023.3344118"
paper_type: research
year: 2024
venue: "IEEE Transactions on Neural Networks and Learning Systems"
authors:
  - "Yixuan Zhou"
  - "Xing Xu"
  - "Jingkuan Song"
  - "Fumin Shen"
  - "Heng Tao Shen"
status: processed
processed_at: 2026-07-09
topics:
  - "unsupervised anomaly detection"
  - "normalizing flows"
  - "multi-scale localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
methods:
  - "[[MSFlow]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
model_family:
  - "normalizing flows"
  - "probabilistic model"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "PatchCore"
  - "CFlow-AD"
  - "CSFlow"
  - "DifferNet"
  - "SPADE"
  - "PaDiM"
  - "DRAEM"
code: "https://github.com/cool-xuan/msflow"
data: "[[MVTec AD]], [[Magnetic Tile Defects]], mini ShanghaiTech Campus"
doi: "10.1109/TNNLS.2023.3344118"
arxiv: "not applicable"
url: "https://doi.org/10.1109/TNNLS.2023.3344118"
pdf: "paper-inbox/10_processed/Research/2024 - Zhou - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection.pdf"
related_methods:
  - "[[MSFlow]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Zhou - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Zhou - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Zhou - MSFlow Multiscale Flow-Based Framework for Unsupervised Anomaly Detection.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "unsupervised-anomaly-detection"
  - "normalizing-flows"
---

# MSFlow: Multiscale Flow-Based Framework for Unsupervised Anomaly Detection

## Summary

MSFlow is a multiscale normalizing-flow framework for unsupervised anomaly detection and localization. It uses low-level multiscale feature pyramids, asymmetrical parallel flows, a fusion flow for cross-scale information exchange, and different aggregation strategies for image-wise anomaly detection and pixel-wise anomaly localization.

On [[MVTec AD]], MSFlow reports 99.7% image-wise detection AUROC, 98.8% pixel-wise localization AUROC, and 97.1% PRO. It also reports 99.2% image-wise AUROC on [[Magnetic Tile Defects]] and 93.0% violation-localization AUROC on mini ShanghaiTech Campus.

## Paper Type

- Type: research.
- Why: The paper introduces a new normalizing-flow architecture, evaluates it against prior UAD methods, and provides component ablations.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]] under normal-only training.
- Setting: anomaly types and sizes are unpredictable, and pixel-level anomaly labels are unavailable during training.
- Inputs: industrial product images or video frames.
- Outputs: image-wise anomaly score and pixel-wise anomaly localization map.
- Motivation: flow-based UAD methods struggle with large variation in defect size, from tiny defects to large structural anomalies.

## Contribution

- Builds a multiscale feature pyramid from the first three stages of a pretrained feature extractor rather than high-level-only features.
- Introduces asymmetrical parallel normalizing flows with more flow blocks on higher-level feature maps.
- Adds a lightweight fusion flow to exchange information across scales and receptive fields.
- Uses addition aggregation for pixel-wise anomaly localization and multiplication aggregation plus mean top-K scoring for image-wise anomaly detection.

## Method

### Feature Extraction

- Feature extractors: WideResNet-50 and ResNet-18 are used in experiments.
- The feature extractor weights are frozen.
- Feature maps from the first three stages are used because they preserve more spatial detail for localization.
- Feature maps are 2x downsampled with average pooling, kernel size 3 and stride 2, before flow modeling.

### Multiscale Flow Model

- Parallel flows independently model each feature scale.
- The default asymmetrical parallel-flow block counts are 2, 5, and 8 for stages 1, 2, and 3.
- st-networks use 3 x 3 convolution, ReLU, layer normalization, and another 3 x 3 convolution.
- 2D positional encodings with 64 channels are inserted into parallel flow blocks.
- A fusion flow exchanges multiscale information by shrinking all scales to the smallest feature size, concatenating, fusing through convolutions, splitting, and rescaling.

### Aggregation

- Pixel-wise anomaly localization uses addition aggregation over multiscale probability maps to preserve scale-specific information.
- Image-wise anomaly detection uses multiplication aggregation to suppress noise.
- The global image anomaly score is the mean of the top-K pixel anomaly scores; the paper selects the mean of the top 3% as the optimum.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial images for MVTec AD and Magnetic Tile Defects; sampled video frames for mini ShanghaiTech Campus.
- Output target: anomaly score and anomaly localization map.
- Supervision: normal-only training; anomalies are used only for test evaluation.
- Objective: maximize likelihood of normal feature distributions with normalizing flows, then assign low likelihood/high anomaly scores to deviations.

### Model And Training

- Feature extractors: WRN-50 and RN-18.
- Flow training: from scratch.
- Hardware: one NVIDIA 2080 Ti GPU.
- Batch size: 16.
- Optimizer: Adam.
- Initial learning rate: 1e-4.
- Learning-rate schedule: drop by factor 3 at 70% and 90% of the training schedule.
- Training epochs: 100 for MVTec AD, 30 for MTD, 10 for mSTC.
- Augmentation: no data augmentation except resizing.
- Code: https://github.com/cool-xuan/msflow.

### Data

- [[MVTec AD]]: 15 industrial product classes, 3,629 normal training images and 1,725 test images; resized to 512 x 512 except transistor, resized to 256 x 256 because misplaced transistor defects can be large.
- [[Magnetic Tile Defects]]: 952 defect-free images and 382 defective images; 80% of defect-free images for training, remaining defect-free images plus all defective images for testing; resized to 192 x 192.
- mini ShanghaiTech Campus: every fifth frame from the standard ShanghaiTech Campus training/test videos; resized to 256 x 384.

### Evaluation

- Image-wise AD: AUROC per class and class-average AUROC.
- Pixel-wise anomaly localization: AUROC per class and class-average AUROC.
- Region-wise localization on MVTec AD: PRO score up to an average per-pixel false-positive rate of 30%.

## Evidence

### Main Results

| Dataset | Task | Metric | Reported value | Notes |
|---|---|---|---:|---|
| [[MVTec AD]] | image-wise anomaly detection | [[AU-ROC]] | 99.7% | Class-average, WRN-50 feature extractor. |
| [[MVTec AD]] | pixel-wise anomaly localization | [[AU-ROC]] | 98.8% | Class-average localization AUROC. |
| [[MVTec AD]] | region-wise localization | [[AU-PRO]] | 97.1% | Reported as 2.5% higher than previous SOTA in PRO. |
| [[Magnetic Tile Defects]] | image-wise anomaly detection | [[AU-ROC]] | 99.2% | Second-best, 0.1% below detection-only CSFlow. |
| mini ShanghaiTech Campus | violation localization | [[AU-ROC]] | 93.0% | 1.2% higher than PatchCore on the reported setup. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-wise anomaly detection | area under ROC curve | higher is better | yes | MVTec AD 99.7%; MTD 99.2% |
| [[AU-ROC]] | pixel-wise localization | area under ROC curve over pixel anomaly scores | higher is better | no | MVTec AD 98.8%; mSTC 93.0% |
| [[AU-PRO]] | region-wise anomaly localization | area under per-region overlap curve up to 30% false-positive rate | higher is better | no | MVTec AD 97.1% |

### Ablations

- Adding stage-1 low-level features improves both detection and localization relative to using stages 2 and 3 only; adding stage-4 high-level features worsens performance.
- Average pooling outperforms max pooling for region-wise localization; average pooling with kernel size 3 is selected as the detection/localization tradeoff.
- ResNet-18 features still outperform prior methods, but WRN-50 features produce higher performance.
- The 2/5/8 asymmetrical parallel-flow setting gives a favorable performance/efficiency tradeoff compared with symmetric flow-block counts.
- Fusion flow improves all evaluation metrics and raises PRO by 2.3%; replacing CSFlow's cross-scale flows with the fusion flow reduces flow-model computational cost by 93% without sacrificing detection accuracy.
- Layer normalization improves detection, localization, and PRO relative to no normalization and outperforms batch normalization in the reported setting.
- Multiplication aggregation is better for image-wise anomaly scoring and noise suppression; addition aggregation is better for pixel-wise localization AUROC.
- Mean top-3% pixel scores is the selected image anomaly score; using the full mean drops detection AUROC to 86.46%.

## Dataset / Benchmark Details

- [[MVTec AD]] is the primary industrial benchmark and is used for detection, localization, and ablations.
- [[Magnetic Tile Defects]] tests generality on a specialized magnetic-tile image anomaly dataset.
- mini ShanghaiTech Campus tests generality outside image industrial inspection; it is included as a reported result but not routed as an industrial dataset note.

## Limitations

- The paper focuses on normal-only training and still depends on the coverage of normal feature distributions.
- Fusion flow can reduce screw detection accuracy because tiny defects can be overshadowed by features with larger receptive fields.
- The source does not report direct inference latency in the checked text.
- MTD evaluation is image-wise only in the reported comparison table.

## Reproducibility

- Code: https://github.com/cool-xuan/msflow.
- Data: [[MVTec AD]], [[Magnetic Tile Defects]], and mini ShanghaiTech Campus.
- Hyperparameters: batch size 16, Adam, initial learning rate 1e-4, LR drops by 3 at 70% and 90%, 100/30/10 epochs for MVTec/MTD/mSTC.
- Random seeds: not reported.
- Hardware: one 2080 Ti GPU.
- Feature extractor weights: frozen.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[MSFlow]], [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]]
- Datasets: [[MVTec AD]], [[Magnetic Tile Defects]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Builds On

- [[Unsupervised anomaly detection]]: MSFlow trains only on anomaly-free samples and detects deviations.
- [[Unsupervised anomaly localization]]: MSFlow produces pixel-wise anomaly localization maps without anomaly labels during training.
- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]]: both use normalizing flows for UAD; MSFlow adds multiscale parallel/fusion flows and top-K anomaly scoring.

### Shares Dataset

- [[MVTec AD]]: primary industrial AD benchmark for detection, localization, and ablation.
- [[Magnetic Tile Defects]]: used for additional image-wise anomaly detection generality.

### Shares Task

- [[Industrial anomaly detection]]: normal-only image anomaly detection.
- [[Defect segmentation]]: pixel-wise anomaly localization on MVTec AD.

### Shares Method

- [[MSFlow]]: method introduced by the paper.
- [[Unsupervised anomaly detection]] and [[Unsupervised anomaly localization]]: learning setup and output task.

### Shares Metric

- [[AU-ROC]]: used for image-wise and pixel-wise evaluation.
- [[AU-PRO]]: used for MVTec AD region-wise localization.

### Application / Domain

- [[Multi-industry anomaly detection]]: MVTec AD spans multiple product and texture categories.

### Follow-up Reading

- [[2021 - FastFlow Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows]]: a prior flow-based UAD method for comparison.

## Questions

- How does the fusion flow affect inference latency relative to single-scale or independent parallel-flow methods?
- Can the screw-class drop under fusion flow be mitigated with defect-size-aware aggregation?
- How stable is top-K anomaly scoring across datasets with very different defect-area distributions?
