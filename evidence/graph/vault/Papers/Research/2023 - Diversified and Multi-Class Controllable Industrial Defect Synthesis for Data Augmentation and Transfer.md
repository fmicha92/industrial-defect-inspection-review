---
title: "Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer"
aliases:
  - "Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer"
paper_key: "sha256:0601348c486bba84eee11b712b7449110aaf8ed348b36e8ce0bf82064e078c58"
paper_type: research
year: 2023
venue: "CVPR Workshops 2023"
authors:
  - "Jing Wei"
  - "Fei Shen"
  - "Chengkan Lv"
  - "Zhengtao Zhang"
  - "Feng Zhang"
  - "Huabin Yang"
status: processed
processed_at: 2026-05-23
topics:
  - "controllable defect synthesis"
  - "multi-class defect generation"
  - "data augmentation transfer"
tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Metal Phone Band Dataset]]"
methods:
  - "[[Diversified controllable defect synthesis]]"
  - "[[Poisson defect image augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "DCDGANc"
  - "OD-SPADE"
metrics:
  - "[[AU-ROC]]"
  - "[[F1-score]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUC and F1 are used for segmentation test performance; higher is better."
baselines:
  - "Raw real training set"
  - "Traditional augmentation"
  - "CycleGAN"
  - "AdaIN"
  - "InstanceNorm"
  - "StyleGAN2"
  - "StarGAN"
benchmarks:
  - "[[MVTec AD]]"
  - "[[Metal Phone Band Dataset]]"
code: "not reported"
data: "MVTec AD is public; metal phone band dataset availability is not reported"
doi: "not reported"
arxiv: "not reported"
url: "https://openaccess.thecvf.com/content/CVPR2023W/VAND/html/Wei_Diversified_and_Multi-Class_Controllable_Industrial_Defect_Synthesis_for_Data_Augmentation_CVPRW_2023_paper.html"
pdf: "paper-inbox/10_processed/Research/2023 - Wei - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer.pdf"
related_papers:
  - "[[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]]"
  - "[[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Diversified controllable defect synthesis]]"
  - "[[Poisson defect image augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[Metal Phone Band Dataset]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "[[MVTec AD]]"
source_file: "paper-inbox/10_processed/Research/2023 - Wei - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wei - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wei - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer.txt"
artifact_status: "code not reported; uses public MVTec AD and an availability-unspecified metal phone band dataset"
tags:
  - paper
---
# Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer

## Summary

Wei et al. propose DCDGANc, a controllable industrial defect synthesis pipeline that separates defect-content generation from compositing onto normal backgrounds. The method trains on extracted defect contents rather than whole defect images, generates class-controlled and style-diverse defect contents with OD-SPADE, obtains masks from pure-background generated defects, and uses improved Poisson blending plus mask refinement to create pixel-labeled synthetic segmentation samples.

The paper evaluates the synthetic data on MVTec AD carpet and wood categories, on a metal phone band dataset, and in a zero-shot transfer setting where generated wood defects are blended into MVTec tile backgrounds. The strongest reported zero-shot tile result is 0.9919 AUC and 0.8376 F1, depending on defect type and segmentation backbone.

## Paper Type

- Type: research.
- Why: the paper introduces a generative defect synthesis method and evaluates synthetic data as training augmentation for industrial defect segmentation.

## Problem

- Task: [[Defect segmentation]] and [[Surface defect detection]].
- Setting: few-sample industrial visual inspection with scarce defective samples and expensive pixel-level annotation.
- Inputs: real defect images with masks, extracted defect contents, class labels, random latent codes, and normal background images.
- Outputs: synthetic defect images and refined pixel-level masks used to train segmentation models.
- Motivation: existing industrial data augmentation methods either provide only image-level labels, depend on paired inputs, preserve too little background, or fail to generate diverse complex defects with pixel-level annotations.
- Assumption: real defect masks are available for extracting defect contents during DCDGANc training.

## Contribution

- Claimed: DCDGANc trains only on extracted defect contents, reducing interference from non-defective background information.
- Claimed: class constant maps control generated defect categories without paired training inputs.
- Claimed: OD-SPADE modulates random codes into the generator to produce diversified defect styles.
- Claimed: improved Poisson blending avoids content loss during compositing while retaining real normal backgrounds.
- Shown: synthetic samples from DCDGANc improve segmentation over raw data and traditional augmentation in carpet, wood, and metal phone band experiments.
- Shown: defect transfer from wood to MVTec tile supports zero-shot tile defect segmentation without collecting real tile defect training samples.

## Method

- Core idea: synthesize defect content separately from the normal background, then composite generated defect content into selected normal backgrounds with refined masks.
- DCDGANc components: encoder, generator, discriminator, class constant maps, one-hot class code, random noise, OD-SPADE modulation, KL loss, reconstruction loss, latent loss, adversarial loss, and WGAN-GP stabilization.
- Category control: class labels are standardized into `[-1, 1]` and repeated into constant maps with the same spatial size as the generator output.
- Style diversity: random latent codes are modulated into middle feature maps through OD-SPADE.
- Mask creation: generated defect-content images have pure backgrounds, allowing raw masks to be obtained by watershed segmentation.
- Compositing: improved Poisson blending uses distance-transform-derived boundary masks and alpha compositing to reduce edge fractures and foreground content loss.
- Final annotation: refined binary masks are produced by simple image processing after compositing.

## ML / DL Extraction

### Task Formulation

- Input modality: 2D industrial surface images and pixel masks.
- Output target: synthetic defect samples with pixel-level segmentation masks; downstream segmentation predictions from ResNet- and U-Net-based models.
- Supervision: supervised defect-content generation from real defect contents and masks; supervised segmentation from synthetic or real pixel-level labels.
- Objective: DCDGANc combines adversarial, reconstruction, latent, KL, and WGAN-GP terms.

### Model And Training

- Model family: [[Generative Models]].
- Generator architecture: DCDGANc with encoder, generator, discriminator, class constant maps, and OD-SPADE.
- Segmentation backbones: ResNet and [[U-Net]] are used for downstream segmentation evaluation.
- Optimizer: Adam with beta values 0.5 and 0.999.
- Batch size: 20.
- Learning rate: 0.0005.
- DCDGANc training length: 500 iterations.
- Loss weights: reconstruction weight 10, latent loss weight 1, KL loss weight 0.01, WGAN-GP weight 10.
- Hardware: one NVIDIA GeForce RTX 3090 GPU on a server with Intel Xeon Gold 622306R CPU at 2.90 GHz.
- Seeds and training time: not reported.

### Data

- MVTec AD carpet and wood: the paper uses defect images from six carpet classes and five wood classes.
- MVTec AD tile: used for zero-shot transfer testing, where wood hole and scratch defects are blended into tile backgrounds to create crack and rough target training images.
- Metal phone band dataset: real industrial metal phone band images; extracted defect contents are cropped into 2,852 images of size 64 x 256 for DCDGANc training.
- Carpet original/constructed defect-content counts: color 19/1055, cut 17/1409, hole 17/1178, metal contamination 17/1016, thread 19/1580.
- Wood original/constructed defect-content counts: color 8/976, hole 10/1033, liquid 10/620, scratch 21/1115, combined 11/original only.
- Segmentation training sets: Raw contains real samples; Augment adds brightness adjustment, rotation, and noise injection; Enlarge adds synthetic samples from DCDGANc.
- Leakage checks: the zero-shot tile experiment trains only on transferred synthetic samples and tests on real tile images; broader leakage controls are not reported.
- License: not reported for the metal phone band dataset.

### Evaluation

- Metrics: [[AU-ROC]] and [[F1-score]] for segmentation.
- Downstream models: segmentation networks based on ResNet and [[U-Net]].
- Baseline training sets: Raw, Augment, and Enlarge.
- Generative baselines: CycleGAN, AdaIN, InstanceNorm, StyleGAN2, and StarGAN.
- Statistical tests: not reported.

## Evidence

### Experimental Setup

- DCDGANc is trained on extracted defect contents rather than full images.
- Synthetic samples are composited onto normal backgrounds and paired with refined pixel masks.
- Downstream segmentation is evaluated on the same test sets for Raw, Augment, and Enlarge.
- The paper reports results separately for MVTec carpet, MVTec wood, metal phone band, and zero-shot MVTec tile.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Synthetic augmentation with ResNet backbone | MVTec wood segmentation | AUC/F1 | higher | Raw 0.9891/0.8462; Augment 0.9891/0.8227 | 0.9903/0.8486 | Enlarge training set. |
| Synthetic augmentation with U-Net backbone | MVTec wood segmentation | AUC/F1 | higher | Raw 0.9936/0.8784; Augment 0.9943/0.8778 | 0.9945/0.8896 | Enlarge training set. |
| Synthetic augmentation with ResNet backbone | MVTec carpet segmentation | AUC/F1 | higher | Raw 0.9812/0.7497; Augment 0.9862/0.7833 | 0.9901/0.7961 | Enlarge training set. |
| Synthetic augmentation with U-Net backbone | MVTec carpet segmentation | AUC/F1 | higher | Raw 0.9846/0.7776; Augment 0.9851/0.7967 | 0.9903/0.8135 | Enlarge training set. |
| DCDGANc versus synthesis baselines | MVTec carpet/wood segmentation | AUC/F1 | higher | CycleGAN, AdaIN, InstanceNorm, StyleGAN2, StarGAN | best across listed rows | Table 5 reports DCDGANc as the strongest augmentation source. |
| Metal phone band synthetic augmentation | Metal phone band segmentation | AUC/F1 | higher | Raw 0.978/0.544 Res; Raw 0.908/0.678 U-Net | Enlarge 0.993/0.660 Res; 0.944/0.701 U-Net | Table 6. |
| Zero-shot transfer with ResNet | MVTec tile crack / rough | AUC/F1 | higher | not applicable | crack 0.9896/0.6876; rough 0.9688/0.8376 | Trained only with transferred synthetic defects. |
| Zero-shot transfer with U-Net | MVTec tile crack / rough | AUC/F1 | higher | not applicable | crack 0.9919/0.7279; rough 0.9790/0.8129 | Best AUC is 0.9919. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | Segmentation test performance | Area Under Curve; exact computation details not expanded in the source text | higher | yes | Reported as AUC in tables. |
| [[F1-score]] | Segmentation test performance | F1 coefficient; exact thresholding details not reported | higher | no | Reported with AUC in all main result tables. |

## Dataset / Benchmark Details

- MVTec carpet and wood: used for training DCDGANc on extracted defect contents and evaluating synthetic-data augmentation.
- MVTec tile: used as target for zero-shot transfer from wood defects to tile backgrounds.
- Metal phone band dataset: used for engineering application; original images are 5472 x 10980, real defect crops are extracted, generated defects are 64 x 256, and segmentation images are 128 x 128.
- Raw/Augment/Enlarge protocol: Raw uses real training samples, Augment adds traditional transformations, and Enlarge adds DCDGANc synthetic samples.
- Test sets: Table 3 reports real/cropped test counts for carpet and wood; Table 7 reports real/cropped tile test counts for crack and rough.
- Availability: [[MVTec AD]] is public; the metal phone band dataset source is not reported.

## Limitations

- Stated: effectiveness on weak defects with inconspicuous texture changes still needs improvement.
- Reproducibility limitation: code availability is not reported in the extracted source.
- Data limitation: the metal phone band dataset source, license, and release status are not reported.
- Evaluation limitation: no statistical uncertainty or repeated-run variance is reported.

## Reproducibility

- Code: not reported.
- Public data: [[MVTec AD]].
- Private or availability-unspecified data: [[Metal Phone Band Dataset]].
- Hyperparameters: Adam beta values 0.5 and 0.999, batch size 20, learning rate 0.0005, 500 DCDGANc iterations, loss weights 10/1/0.01 plus WGAN-GP weight 10.
- Hardware: one NVIDIA GeForce RTX 3090 GPU and Intel Xeon Gold 622306R CPU at 2.90 GHz.
- Random seeds: not reported.
- Checkpoints/models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Surface defect detection]]
- Methods: [[Diversified controllable defect synthesis]], [[Poisson defect image augmentation]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[Metal Phone Band Dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[F1-score]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] | Shares method | Both synthesize and transfer industrial defects for data augmentation, but this paper decouples defect-content generation from compositing and targets pixel-level masks. |
| [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] | Contrasts with | SIGAN is cited as a CycleGAN/L1-loss approach for solar-cell defect augmentation; this paper aims for diversified multi-class generation with pixel masks. |
| [[2023 - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation]] | Shares dataset and theme | Both use MVTec AD for few-shot defect generation or augmentation, but this paper focuses on controllable content generation plus Poisson-style compositing. |

### Backlinks Updated

- [[Diversified controllable defect synthesis]], [[Poisson defect image augmentation]], [[MVTec AD]], and [[Metal Phone Band Dataset]] were reviewed or updated during audit.

## Questions

- Is the metal phone band dataset publicly available, proprietary, or only available through the authors?
- Are DCDGANc source code, trained models, or generated samples released outside the paper?
- How sensitive are the segmentation gains to the watershed/mask-refinement steps?
