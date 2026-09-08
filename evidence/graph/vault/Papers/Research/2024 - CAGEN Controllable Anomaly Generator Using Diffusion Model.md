---
title: "CAGEN: Controllable Anomaly Generator Using Diffusion Model"
aliases:
  - "CAGEN: Controllable Anomaly Generator Using Diffusion Model"
paper_key: "doi:10.1109/icassp48485.2024.10447663"
paper_type: research
year: 2024
venue: "ICASSP 2024"
authors:
  - "Bolin Jiang"
  - "Yuqiu Xie"
  - "Jiawei Li"
  - "Naiqi Li"
  - "Yong Jiang"
  - "Shu-Tao Xia"
status: processed
processed_at: 2026-05-23
topics:
  - "controllable anomaly generation"
  - "diffusion models"
  - "industrial anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
dataset_sizes:
  - "MVTec AD: standard 15-category benchmark; CAGen fine-tunes on three images from each defect type in each category."
  - "BTAD: three industrial product categories are reported in Table 2."
methods:
  - "[[CAGen]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
  - "[[ControlNet]]"
model_family:
  - "[[Diffusion models]]"
  - "[[Generative Models]]"
architectures:
  - "[[ControlNet]]"
  - "[[CAGen]]"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUROC and AP are reported for anomaly localization; higher is better."
baselines:
  - "CutPaste"
  - "DRAEM"
benchmarks:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
code: "not reported"
data: "[[MVTec AD]] and [[BTAD]] benchmarks"
doi: "10.1109/icassp48485.2024.10447663"
arxiv: "not reported"
url: "https://doi.org/10.1109/ICASSP48485.2024.10447663"
pdf: "paper-inbox/10_processed/Research/2024 - Jiang - CAGEN Controllable Anomaly Generator Using Diffusion Model.pdf"
related_papers:
  - "[[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]]"
  - "[[2021 - The MVTec Anomaly Detection Dataset]]"
  - "[[2020 - Denoising Diffusion Probabilistic Models]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[CAGen]]"
  - "[[Diffusion models]]"
  - "[[Synthetic data generation]]"
  - "[[ControlNet]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[MVTec AD]]"
  - "[[BTAD]]"
source_file: "paper-inbox/10_processed/Research/2024 - Jiang - CAGEN Controllable Anomaly Generator Using Diffusion Model.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Jiang - CAGEN Controllable Anomaly Generator Using Diffusion Model.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Jiang - CAGEN Controllable Anomaly Generator Using Diffusion Model.txt"
artifact_status: "paper available; code not reported; generated samples/models not reported"
tags:
  - paper
---
# CAGEN: Controllable Anomaly Generator Using Diffusion Model

## Summary

CAGen is a two-stage diffusion-based anomaly data augmentation method for industrial anomaly localization. It fine-tunes Stable Diffusion v1.5 with ControlNet so a binary mask controls anomaly location and a text prompt controls anomaly style, then fuses generated anomalous features with normal-image features to make the generated samples resemble normal industrial objects. On MVTec AD, using CAGen-generated images in a DRAEM-style training pipeline raises mean localization AUROC/AP from 97.3/68.4 to 97.7/71.5; on BTAD it raises mean AUROC/AP from 88.3/20.3 to 91.2/26.3.

## Paper Type

- Type: research.
- Why: The paper introduces and evaluates a new controllable anomaly-generation method for anomaly detection and localization.

## Problem

- Task: [[Industrial anomaly detection]], [[Defect segmentation]].
- Setting: Industrial visual inspection with scarce anomalous training examples.
- Inputs: Normal industrial images, anomaly location masks, text prompts such as defect-type/category prompts, and Gaussian diffusion noise.
- Outputs: Synthetic anomalous images for training anomaly localization models.
- Motivation: Image-level cut-and-paste anomaly augmentation can be unrealistic and limited to predefined patterns; text-guided diffusion can generate richer anomalies but needs location control and better resemblance to target-domain normal images.
- Assumptions: Synthetic anomalies closer to real anomaly distributions should provide better supervisory signals for anomaly localization.

## Contribution

- Claimed: CAGen generates high-quality controllable anomalous images for anomaly detection data augmentation.
- Shown: CAGen improves DRAEM-based anomaly localization on MVTec AD and BTAD in mean AUROC/AP.
- Shown: t-SNE visualization shows CAGen synthetic anomalies closer to real anomalies than CutPaste or DRAEM synthetic anomalies in the reported feature space.
- Inferred: The method trades off realism and controllability by using ControlNet for prompt/mask-conditioned generation, then feature-level fusion to retain target-image normal structure.

## Method

- Core idea: Generate prompt- and mask-controlled anomalous features with a fine-tuned ControlNet diffusion model, then combine those features with features from a normal reference image.
- Stage 1, Anomaly-Guided Feature Generation: Fine-tune Stable Diffusion v1.5 with ControlNet using a binary anomaly mask and text prompt. The mask specifies anomaly location; the prompt specifies anomaly style.
- Training objective: With noisy anomalous feature `z_t`, timestep `t`, prompt `c_t`, mask `c_m`, and noise `epsilon`, train the ControlNet-conditioned model to predict the added noise with an L2 diffusion loss.
- Stage 2, Anomaly Feature Fusion: Encode a normal reference image, generate anomalous features, then fuse by mask: `z_f = z_g * c_m + z_i * (1 - c_m)`. Decode the fused feature to the final anomalous image.
- Augmentation procedure: Obtain an object mask for the image to augment, multiply it element-wise with a random Perlin noise mask to form the anomaly location mask, then generate the anomaly with CAGen and the text anomaly prompt.

## Evidence

### Experimental Setup

- Datasets: [[MVTec AD]], [[BTAD]].
- Training: CAGen is trained on MVTec AD by fine-tuning Stable Diffusion v1.5 with ControlNet.
- Defect examples used for CAGen fine-tuning: three images randomly selected from each defect type within each MVTec AD category.
- Text prompts: `"{defect type} {category}"`, with the paper giving "broken large bottle" as an example.
- Diffusion training length: 1000 epochs.
- Detection training setup: The paper follows DRAEM's anomaly detection setup and replaces 30% of the training set with CAGen-generated anomalous images.
- Baselines: CutPaste and DRAEM on MVTec AD; DRAEM on BTAD.
- Used performance metrics: [[AU-ROC]], [[Average precision]].
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Mean anomaly localization improves over DRAEM | [[MVTec AD]] | AUROC / AP | higher | 97.3 / 68.4 | 97.7 / 71.5 | Mean improvement is 0.4 AUROC and 3.1 AP. |
| Mean anomaly localization improves over DRAEM | [[BTAD]] | AUROC / AP | higher | 88.3 / 20.3 | 91.2 / 26.3 | Mean improvement is 2.9 AUROC and 6.0 AP. |
| CAGen synthetic anomalies cluster closer to real anomalies | MVTec AD selected categories | t-SNE visualization | qualitative | CutPaste and DRAEM synthetic anomalies | CAGen closer to real anomalies | Features are extracted from a fine-tuned ResNet-18 binary classifier. |

### Per-Category Results

| Dataset | Category | Baseline | Baseline AUROC / AP | CAGen AUROC / AP |
|---|---|---|---:|---:|
| MVTec AD | bottle | DRAEM | 99.1 / 86.5 | 99.2 / 89.8 |
| MVTec AD | cable | DRAEM | 94.7 / 52.4 | 95.1 / 63.0 |
| MVTec AD | capsule | DRAEM | 94.3 / 49.4 | 95.6 / 49.4 |
| MVTec AD | hazelnut | DRAEM | 99.7 / 92.9 | 99.8 / 95.9 |
| MVTec AD | metal nut | DRAEM | 99.5 / 96.3 | 99.5 / 96.1 |
| MVTec AD | pill | DRAEM | 97.6 / 48.5 | 98.0 / 51.4 |
| MVTec AD | screw | DRAEM | 97.6 / 58.2 | 99.4 / 64.7 |
| MVTec AD | toothbrush | DRAEM | 98.1 / 44.7 | 98.5 / 61.9 |
| MVTec AD | transistor | DRAEM | 90.9 / 50.7 | 91.5 / 45.7 |
| MVTec AD | zipper | DRAEM | 98.8 / 81.5 | 99.0 / 81.8 |
| MVTec AD | carpet | DRAEM | 95.5 / 53.5 | 95.9 / 55.9 |
| MVTec AD | grid | DRAEM | 99.7 / 65.7 | 99.6 / 76.1 |
| MVTec AD | leather | DRAEM | 98.6 / 75.3 | 99.1 / 71.4 |
| MVTec AD | tile | DRAEM | 99.2 / 92.3 | 99.4 / 95.8 |
| MVTec AD | wood | DRAEM | 96.4 / 77.7 | 96.1 / 74.8 |
| BTAD | 01 | DRAEM | 91.8 / 18.8 | 92.7 / 19.8 |
| BTAD | 02 | DRAEM | 77.9 / 31.8 | 85.5 / 45.6 |
| BTAD | 03 | DRAEM | 95.1 / 10.4 | 95.4 / 13.5 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Anomaly localization | Area under ROC curve; unit not otherwise defined in the paper | higher is better | yes | Reported for MVTec AD and BTAD. |
| [[Average precision]] | Anomaly localization | Average precision; exact implementation not reported | higher is better | yes | Reported alongside AUROC. |

### Ablations

- The source text does not report a separate component ablation for Anomaly-Guided Feature Generation versus Anomaly Feature Fusion.

## ML / DL Extraction

### Task Formulation

- Input modality: Industrial RGB inspection images plus masks and text prompts for generation.
- Output target: Synthetic anomalous images; downstream anomaly localization maps/scores from the detection model.
- Supervision: CAGen uses selected anomaly-mask pairs for fine-tuning; downstream anomaly localization uses generated anomalous images as synthetic supervision in a DRAEM-style setup.
- Objective: Improve anomaly localization by generating realistic controllable anomaly samples.

### Model And Training

- Model family: [[Diffusion models]], [[Generative Models]].
- Architecture: Stable Diffusion v1.5 with [[ControlNet]]; Denoising U-Net weights are frozen while ControlNet is trained.
- Parameters: not reported.
- Pretraining: Stable Diffusion v1.5 pretrained model.
- Fine-tuning: ControlNet fine-tuned on MVTec AD anomaly-mask/prompt examples.
- Losses: L2 noise-prediction diffusion objective.
- Optimizer: not reported.
- Hyperparameters: 1000 training epochs are reported; optimizer, learning rate, batch size, and resolution are not reported.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[MVTec AD]], [[BTAD]].
- Data source: Standard anomaly detection benchmarks.
- Dataset size: not restated by the paper for MVTec AD or BTAD.
- Labels / annotations: Anomaly masks are used for ControlNet fine-tuning and anomaly localization evaluation.
- Splits: Standard benchmark splits are implied; exact split counts are not reported.
- Preprocessing: Object masks are multiplied with Perlin noise masks to form final anomaly location masks for augmentation.
- Augmentation: 30% of the downstream training set is replaced with CAGen-generated anomalous images.
- Synthetic data: CAGen-generated anomalous images controlled by binary masks and text prompts.
- Leakage checks: The paper states CAGen uses a small portion of the test set for training, then reports that after removing the images used for CAGen training the MVTec AD average AUROC/AP remains 97.7/71.5; it also says the anomaly detection phase does not directly encounter real anomalies.
- License: not reported.

### Evaluation

- Protocol: Follow DRAEM's anomaly detection process and compare localization AUROC/AP after replacing 30% of training images with CAGen-generated anomalies.
- Used performance metrics: [[AU-ROC]], [[Average precision]].
- Primary metric: [[AU-ROC]] and AP are both reported in the main tables.
- Metric definitions: not formally defined beyond metric names.
- Metric direction / units: higher is better.
- Baselines: CutPaste, DRAEM.
- Benchmarks: [[MVTec AD]], [[BTAD]].
- Statistical tests: not reported.
- Failure cases: Some categories decline relative to DRAEM in AP or AUROC, including MVTec AD transistor AP, leather AP, wood AUROC/AP, grid AUROC, and metal nut AP.

## Dataset / Benchmark Details

- Source: [[MVTec AD]] and [[BTAD]] benchmark datasets.
- Collection: not reported by this paper.
- Annotation: Anomaly masks are used; details are inherited from the benchmarks and not restated.
- Size: not reported by this paper.
- Splits: not reported beyond the CAGen fine-tuning subset and downstream generated-image replacement ratio.
- Modalities: industrial visual inspection images.
- License: not reported by this paper.
- Leakage risks: CAGen fine-tunes on a small portion of MVTec AD test anomalies; the paper reports a removal check with unchanged mean AUROC/AP.
- Bias / coverage: CAGen is trained on MVTec AD and evaluated on MVTec AD and BTAD; generalization beyond these benchmarks is not reported.
- Maintenance: not applicable.

## Limitations

- Stated: Directly using Stable Diffusion prompt-generated images lacks annotation information and differs substantially from real target-domain samples.
- Stated: Generated features from the first stage differ significantly from normal-sample features, motivating feature fusion.
- Inferred: Fine-tuning CAGen on a small portion of MVTec AD test anomalies creates a leakage concern, partially addressed by the paper's removal check.
- Inferred: The method is evaluated on two benchmarks and lacks reported compute, optimizer, code, and broad deployment evidence.

## Reproducibility

- Code: not reported.
- Data: [[MVTec AD]] and [[BTAD]] are named; generated samples are not released in the source text.
- Hyperparameters: 1000 CAGen fine-tuning epochs and 30% generated-image training replacement are reported; most other hyperparameters are not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: Stable Diffusion v1.5 is used; released CAGen checkpoint is not reported.
- Exact preprocessing: Object mask multiplied by random Perlin noise mask for anomaly location mask.
- Artifact status: Paper available; code/model artifacts not reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[CAGen]], [[Diffusion models]], [[Synthetic data generation]], [[ControlNet]]
- Datasets: [[MVTec AD]], [[BTAD]]
- Benchmarks: [[MVTec AD]], [[BTAD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Dataset

- [[MVTec AD]] - CAGen is fine-tuned and evaluated on this benchmark.
- [[BTAD]] - CAGen is evaluated on this benchmark against DRAEM.

### Shares Method

- [[CAGen]] - the paper introduces this two-stage controllable anomaly generator.
- [[Diffusion models]] - CAGen builds on Stable Diffusion and a diffusion noise-prediction objective.
- [[ControlNet]] - CAGen uses ControlNet to condition Stable Diffusion on anomaly location masks and prompts.
- [[Synthetic data generation]] - generated anomalies are used as training augmentation for anomaly localization.

### Shares Task

- [[Industrial anomaly detection]] - the generated images train anomaly localization models for industrial benchmarks.
- [[Defect segmentation]] - the paper reports localization metrics using anomaly masks.

### Shares Metric

- [[AU-ROC]] - reported as the main localization metric on MVTec AD and BTAD.
- [[Average precision]] - reported alongside AUROC in both result tables.

### Related Papers

- [[2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization]] - CutPaste is a synthetic anomaly baseline for MVTec AD.
- [[2020 - Denoising Diffusion Probabilistic Models]] - diffusion model background for the generative component.

## Questions

- How much of the reported improvement depends on using real MVTec AD test anomalies to fine-tune CAGen?
- Would CAGen improve anomaly localization when fine-tuned only on training-set normal images plus synthetic or externally sourced anomaly masks?
- How sensitive are the results to the 30% generated-image replacement ratio and to prompt wording?
