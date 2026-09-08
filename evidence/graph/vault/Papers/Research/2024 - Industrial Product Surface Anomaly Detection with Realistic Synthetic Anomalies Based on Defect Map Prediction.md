---
title: "Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction"
aliases:
  - "Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction"
paper_key: "sha256:dc214d9603ecc4514140d13546261951e7d2e0ca0bba191bb39dd33410316685"
paper_type: research
year: 2024
venue: "Sensors"
authors:
  - "Tao Peng"
  - "Yu Zheng"
  - "Lin Zhao"
  - "Enrang Zheng"
status: processed
processed_at: 2026-06-12
topics:
  - "realistic synthetic anomalies"
  - "defect map prediction"
  - "image reconstruction"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
architectures: []
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PR]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "DRAEM"
  - "PaDiM"
  - "STFPM"
  - "CFlow"
  - "CSFlow"
  - "FastFlow"
benchmarks:
  - "[[MVTec AD]]"
code: "not reported"
data: "uses MVTec AD and DTD as a baseline anomaly source"
doi: "10.3390/s24010264"
arxiv: "not reported"
url: "https://doi.org/10.3390/s24010264"
pdf: "paper-inbox/10_processed/Research/2024 - Peng - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction.pdf"
related_methods:
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Research/2024 - Peng - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Peng - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Peng - Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Industrial Product Surface Anomaly Detection with Realistic Synthetic Anomalies Based on Defect Map Prediction

## Summary

The paper proposes a semi-supervised industrial anomaly detection method that creates realistic synthetic anomalies using MVTec AD anomaly images as anomaly sources and trains a defect-map prediction/reconstruction model. On [[MVTec AD]], it reports 99.70% image-level AUROC and 99.87% AP in the final ablation setting, with the extracted source stating a 1.1 percentage-point AUROC gain over the previous best method and a 31.47 point AP gain over DRAEM for localization.

## Paper Type

- Type: research.
- Why: It proposes a synthetic-anomaly training method and reports benchmark comparisons and ablations on MVTec AD.

## Problem

- Task: [[Industrial anomaly detection]] and [[Defect segmentation]].
- Setting: industrial surface anomaly detection with realistic synthetic anomalies.
- Inputs: MVTec AD product images.
- Outputs: defect prediction images, heatmaps, and image-level anomaly decisions.
- Motivation: reconstruction-based methods trained only on normal images can miss realistic defect patterns; simple synthetic anomalies can be too unrealistic.
- Assumptions: synthetic defects created from MVTec anomaly sources and foreground-aware placement can improve robustness and localization.

## Contribution

- Claimed: Designs a three-stage method for generating more realistic synthetic defect images.
- Claimed: Introduces an autoencoder image reconstruction network and defect prediction network with a larger convolutional receptive field.
- Shown: The full method improves ablation AUROC/AP from 98.00/68.40 to 99.70/99.87.

## Method

- Core idea: synthesize realistic defect images, reconstruct them toward normality, and learn defect maps from differences between original and reconstructed features/images.
- Architecture / algorithm: autoencoder reconstruction network, deep feature extractor, large-kernel convolution encoder inspired by RepLKNet, and defect prediction network.
- Objective / loss: multi-term loss with lambda1=1, lambda2=0.8, lambda3=0.2.
- Optimization: learning rate 1e-4 with drops by 0.1 at 400 and 600 epochs; 700 training epochs.
- Training data: [[MVTec AD]].
- Data pipeline: synthetic anomalies are made in foreground-relevant locations; MVTec AD anomaly images replace DTD as a defect source in the reported synthesis ablation.
- Augmentation / synthesis: image rotation for sample scarcity plus realistic synthetic anomalies using MVTec AD anomaly sources, random linear interpolation, affine transformations, and image enhancement.
- Inference: defect prediction maps and heatmaps are thresholded for image-level detection and pixel-level localization.
- Complexity / deployment constraints: average inference time 0.041 s per sample; NVIDIA RTX 3090 used.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]].
- Splits: not fully reported in the extracted text.
- Baselines: CFlow, CSFlow, FastFlow, PaDiM, DRAEM, STFPM, and ablations over anomaly source and model components.
- Used performance metrics: image-level AUROC and AP for localization.
- Hardware: NVIDIA RTX 3090 GPU.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Full method vs previous best | MVTec AD image-level anomaly detection | AUROC (%) | higher | 98.6 | 99.70 | Source states the method is 1.1 percentage points higher than the previous best. |
| Full method vs DRAEM | MVTec AD defect localization | AP (%) | higher | not fully extracted | not fully extracted | Source states +31.47 AP over DRAEM in all 15 categories. |
| Full method vs baseline ablation | MVTec AD ablation | AUROC / AP (%) | higher | 98.00 / 68.40 | 99.70 / 99.87 | Table 4 ablation; baseline item is the first listed configuration. |
| MVTec anomaly source plus modules | MVTec AD ablation | AUROC / AP (%) | higher | 99.25 / 99.54 | 99.70 / 99.87 | Compares source/method ablation against full model. |
| Parameter copying vs gradient update | MVTec AD ablation | AUROC / AP (%) | higher | 99.33 / 99.69 | 99.70 / 99.87 | Full method uses parameter copying. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Image-level anomaly detection | Percent AUROC | higher | yes | Main detection metric. |
| [[AU-PR]] | Defect localization AP | Average precision percent | higher | yes | Used for localization comparison. |

### Ablations

- Replacing DRAEM's DTD anomaly source with MVTec AD anomaly images slightly improves detection performance.
- Adding the deep feature extractor and large-kernel convolution encoder improves the full model.
- Parameter copying for the deep feature extractor outperforms direct gradient-update training.

## ML / DL Extraction

### Data

- Datasets: [[MVTec AD]]; DTD appears as the baseline anomaly source used by DRAEM.
- Dataset size: source describes MVTec AD as about 5000 images across 15 categories and 13 sectors, with about 2500 defective images; this conflicts with the canonical dataset note, so preserve the paper-specific wording here.
- Labels / annotations: pixel-level masks indicate defect locations and shapes.
- Preprocessing: affine transformations, image enhancement, and rotation augmentation are reported.
- Augmentation: image rotation and realistic synthetic anomalies.
- Synthetic data: MVTec AD anomaly images are used as anomaly sources; random linear interpolation keeps residual original-image information.
- Leakage checks: not reported.

### Evaluation

- Protocol: quantitative comparison with reproduced anomalib methods and recent pixel-level anomaly detection methods.
- Baselines: listed above.
- Statistical tests: not reported.
- Failure cases: several categories perform poorly because the synthetic defect method creates relatively realistic abnormal images that make detection harder.

## Limitations

- Stated: some categories remain difficult because realistic synthetic anomalies create challenging abnormal samples.
- Inferred: using MVTec AD anomaly images as anomaly sources may reduce the purity of a normal-only anomaly detection setting; the exact train/test separation for anomaly sources should be checked before strong claims.

## Reproducibility

- Code: not reported.
- Data: MVTec AD public.
- Hyperparameters: 700 epochs, lr 1e-4, drops at 400 and 600 epochs, lambda1=1, lambda2=0.8, lambda3=0.2.
- Random seeds: not reported.
- Environment: NVIDIA RTX 3090 GPU.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Defect synthesis]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PR]]

### Shares Dataset

- [[MVTec AD]]: primary benchmark and anomaly source.

### Shares Method

- [[Defect synthesis]], [[Synthetic data generation]], and [[Data augmentation]]: realistic synthetic anomalies are central to training.

### Shares Task

- [[Industrial anomaly detection]] and [[Defect segmentation]].

### Shares Metric

- [[AU-ROC]] and [[AU-PR]].

## Questions

- Which exact MVTec AD anomalous images are used as synthesis sources, and are they isolated from test evaluation?
- Is code available for the three-stage defect synthesis and parameter-copying procedure?
