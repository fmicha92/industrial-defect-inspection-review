---
title: "Defect Transfer GAN: Diverse Defect Synthesis for Data Augmentation"
aliases:
  - "Defect Transfer GAN: Diverse Defect Synthesis for Data Augmentation"
paper_key: "arxiv:1066.69090"
paper_type: research
year: 2022
venue: "BMVC 2022"
authors:
  - "Ruyu Wang"
  - "Sabria Hoppe"
  - "Eduardo Monari"
  - "Marco F. Huber"
status: processed
processed_at: 2026-05-23
topics:
  - "defect synthesis"
  - "data augmentation"
  - "few-sample defect classification"
tasks:
  - "[[Defect classification]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[Bosch Surface Defect Inspection Dataset]]"
methods:
  - "[[Defect Transfer GAN]]"
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[Defect Transfer GAN]]"
metrics:
  - "[[FID]]"
  - "[[LPIPS]]"
primary_metric: "[[FID]]"
metric_definitions:
  - "FID: lower is better for generated-image fidelity and diversity."
  - "LPIPS: lower means generated samples are more similar to one another; used to diagnose diversity and overfitting alongside FID and classifier performance."
baselines:
  - "Mokady et al."
  - "StarGAN v2"
  - "StyleGAN2"
  - "BigGAN"
  - "traditional augmentation"
  - "CutMix"
  - "CutOut"
  - "MixUp"
benchmarks:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[Bosch Surface Defect Inspection Dataset]]"
code: "not reported"
data: "SDI dataset is public through the Bosch Research GitHub repository; MVTec AD and MTD are public datasets"
doi: "not reported"
arxiv: "1066.69090"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2022 - Wang - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Small-sample defect classification]]"
related_methods:
  - "[[Defect Transfer GAN]]"
  - "[[GAN]]"
  - "[[Synthetic data generation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[Bosch Surface Defect Inspection Dataset]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Industrial anomaly detection]]"
related_benchmarks:
  - "[[MVTec AD]]"
  - "[[Magnetic Tile Defects]]"
  - "[[Bosch Surface Defect Inspection Dataset]]"
source_file: "paper-inbox/10_processed/Research/2022 - Wang - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Wang - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Wang - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Defect Transfer GAN: Diverse Defect Synthesis for Data Augmentation

## Summary

Wang et al. propose [[Defect Transfer GAN]] (DT-GAN), a GAN framework for synthesizing diverse industrial defect images by separating background products from foreground defect shape and style. The method can generate defects under control of background, defect shape, and defect style, enabling semantic data augmentation when defective samples are scarce.

The paper evaluates defect generation on [[MVTec AD]], [[Magnetic Tile Defects]], and [[Bosch Surface Defect Inspection Dataset]]. Downstream defect classification is evaluated on the SDI dataset. DT-GAN improves ResNet-50 classifier error rates compared with no augmentation, traditional augmentation, and several GAN baselines, with the abstract reporting up to 51% error-rate reduction.

## Paper Type

- Type: research.
- Why: The paper proposes a new generative augmentation method and evaluates both image synthesis quality and downstream defect classification.

## Problem

- Task: [[Defect classification]] and industrial defect image synthesis.
- Setting: automated visual inspection with few defective samples and class imbalance.
- Inputs: normal and defective industrial inspection images, product/background labels, and defect-domain labels.
- Outputs: synthetic defective images and downstream classifier training data.
- Motivation: defective samples are rare on optimized production lines, while standard augmentation does not add semantically new defect information.
- Assumptions: at least some defect types occur across multiple products, allowing shared defect characteristics to be transferred across backgrounds.

## Contribution

- Claimed: introduces DT-GAN to learn defect types independent of background products and apply defect-specific styles to realistic defective image generation.
- Claimed: explicitly separates foreground defect shape and style from background product information.
- Claimed: supports latent-guided and reference-guided defect synthesis with control over background, defect shape, and style.
- Shown: generated DT-GAN images improve downstream defect classification on SDI compared with traditional augmentation and several GAN synthesis baselines.

## Method

DT-GAN treats defect synthesis as unpaired image-to-image translation across multiple foreground defect domains. It extends StarGAN v2 with style-defect separation, foreground/background disentanglement, auxiliary classifiers in the discriminator, an anchor normal domain, and per-pixel noise injection.

The mapping network and style-defect encoder represent domain-specific defect shape separately from a style vector. The generator splits foreground and background channels at the bottleneck, replaces the defect representation for domain transfer, and decodes background separately without style modulation. The discriminator includes a foreground defect classifier and a background classifier to strengthen disentanglement.

## Evidence

### Experimental Setup

- Image synthesis datasets: [[MVTec AD]], [[Magnetic Tile Defects]], and Surface Defect Inspection (SDI).
- Defect grouping: defects are reorganized into Normal, Scratches-like, and Spotslike classes.
- Defective images per category: 8 to 620 across the three datasets.
- Image size: all images resized to 128 x 128 for GAN and classifier training.
- Defect generation baselines: Mokady et al., StarGAN v2, StyleGAN2, and BigGAN.
- Downstream classifier: ResNet-50 with ImageNet-pretrained weights.
- Synthetic-data classifier setup: auxiliary classifier attached through a Gradient Reversal Layer to encourage real/synthetic invariant features.
- Evaluation repeats: downstream error rates reported over five runs with different random seeds.

### Defect Generation Results

| Method | MVTec carpet | MVTec tile | MVTec wood | MTD | SDI A | SDI B | SDI C | All |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mokady et al. | 68.69 | 66.90 | 36.21 | 41.87 | 60.26 | 275.12 | 81.71 | 87.38 |
| StarGAN v2 | 96.85 | 58.28 | 50.95 | 354.31 | 336.63 | 434.77 | 411.37 | 228.46 |
| StyleGAN2 | 90.10 | 52.95 | 138.09 | 51.37 | 51.60 | 225.96 | 140.01 | 100.18 |
| BigGAN | 218.74 | 134.41 | 270.89 | 34.47 | 101.70 | 391.54 | 113.32 | 166.62 |
| DT-GAN | 65.62 | 53.62 | 37.94 | 27.33 | 78.01 | 352.15 | 77.11 | 96.27 |

### Downstream Classification Results

| Augmentation | Synthetic data | Product A error | Product B error | Product C error |
|---|---|---:|---:|---:|
| None | none | 14.91 +/- 1.52 | 8.2 +/- 1.49 | 15.24 +/- 1.51 |
| Traditional | none | 13.81 +/- 2.36 | 6.8 +/- 1.64 | 16.57 +/- 3.20 |
| Traditional | Mokady et al. | 20.72 +/- 1.49 | 5.8 +/- 2.77 | 24.76 +/- 10.1 |
| Traditional | StarGAN v2 | 10.60 +/- 1.99 | 7.4 +/- 3.44 | 15.81 +/- 1.44 |
| Traditional | StyleGAN2 | 29.45 +/- 9.13 | 6.8 +/- 2.05 | 13.14 +/- 3.12 |
| Traditional | BigGAN | 12.17 +/- 1.99 | 5.8 +/- 1.93 | 15.62 +/- 3.06 |
| Traditional | DT-GAN | 6.72 +/- 1.65 | 4.6 +/- 0.89 | 12.76 +/- 1.97 |

### Limited-Data Results

| Dataset size | Product | Traditional augmentation error | DT-GAN augmentation error |
|---|---|---:|---:|
| 20A | A | 34.18 +/- 4.39 | 28.55 +/- 7.32 |
| 20A | B | 5.8 +/- 0.45 | 5.6 +/- 1.14 |
| 20A | C | 16.95 +/- 1.17 | 10.86 +/- 1.28 |
| All | A | 13.81 +/- 2.36 | 6.72 +/- 1.65 |
| All | B | 6.8 +/- 1.64 | 4.6 +/- 0.89 |
| All | C | 16.57 +/- 3.20 | 12.76 +/- 1.97 |

### Cross-Product Defect Transfer

| Product | Traditional augmentation | Same-product defects | Other-product defects | All-product defects |
|---|---:|---:|---:|---:|
| A | 13.81 +/- 2.36 | 11.81 +/- 2.65 | 11.99 +/- 1.63 | 11.09 +/- 3.49 |
| B | 6.8 +/- 1.64 | 6.6 +/- 1.52 | 6.4 +/- 1.34 | 5.6 +/- 1.34 |
| C | 16.57 +/- 3.20 | 14.85 +/- 1.73 | 11.23 +/- 0.80 | 11.42 +/- 0.96 |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[FID]] | Generated defect image fidelity and diversity | Frechet Inception Distance | Lower is better | yes for image synthesis | DT-GAN gives best or near-best scores in several dataset/product cases and overall FID 96.27. |
| [[LPIPS]] | Similarity among synthetic samples | Perceptual similarity distance | Lower means more similarity | secondary diagnostic | Used with nearest-neighbor analysis and classifier performance to diagnose overfitting/diversity. |
| Error rate | Defect classification | Percentage classification error over five runs | Lower is better | yes for downstream task | DT-GAN reduces Product A error from 13.81 to 6.72 under traditional augmentation. |

## ML / DL Extraction

### Task Formulation

- Input modality: industrial visual inspection images.
- Output target: synthetic defective images for augmentation and defect-classification labels for downstream evaluation.
- Supervision: weakly supervised image generation with defect domain labels and background product labels; supervised downstream classification.
- Objective: generate diverse, realistic defects that improve classifier performance under scarce defective samples.

### Model And Training

- Model family: [[GAN]] image-to-image translation.
- Base model: StarGAN v2 extended for defect transfer.
- Architecture components: mapping network, style-defect encoder, generator, multi-task discriminator, foreground defect classifier, and background classifier.
- Key mechanisms: style-defect separation, foreground/background disentanglement, separate foreground/background decoding, anchor normal domain, and per-pixel noise injection.
- Losses: adversarial loss, style-defect reconstruction loss, defect reconstruction consistency, diversity-sensitive loss, cycle consistency loss, foreground defect classification loss, and background classification loss.
- Preprocessing: images resized to 128 x 128.
- Classifier backbone: ImageNet-pretrained ResNet-50.
- Seeds: downstream classifier error rates reported over five runs.
- Compute and training time: not reported in the extracted text.

### Data

- Datasets: [[MVTec AD]], [[Magnetic Tile Defects]], and [[Bosch Surface Defect Inspection Dataset]] / SDI.
- SDI use: only the training set is used for GAN training; validation and test sets are held out for final classifier evaluation.
- Additional normal images: 4,000 normal images per product are used to generate defective samples for classifier training.
- Defect categories: Normal, Scratches-like, and Spotslike.
- Splits: the SDI dataset details released with the repository report per-product validation/test holdout counts and DT-GAN training subsets.
- Licenses: SDI is released under CC-BY-SA-4.0 in the Bosch Research repository.

### Evaluation

- Protocol: evaluate image synthesis using FID and LPIPS, then evaluate synthetic images as data augmentation for ResNet-50 defect classification.
- Baselines: Mokady et al., StarGAN v2, StyleGAN2, BigGAN, traditional augmentation, CutMix, CutOut, and MixUp.
- Statistical tests: not reported.
- Failure cases: FID can favor overfit generators; generated-image metrics alone do not reliably indicate downstream usefulness.

## Dataset / Benchmark Details

- [[MVTec AD]]: used for image synthesis experiments on selected object/texture categories.
- [[Magnetic Tile Defects]]: used for image synthesis experiments.
- [[Bosch Surface Defect Inspection Dataset]] / SDI: used for image synthesis and downstream defect classification; the dataset is public through the Bosch Research repository.
- Dataset availability: MVTec AD, MTD, and SDI are public.

## Limitations

- FID and LPIPS are imperfect for detecting overfitting or small defect-variation differences.
- SDI is central to downstream classification; exact physical product identities for Product A, Product B, and Product C are anonymized.
- The method assumes shared defect characteristics across products; transfer to unseen products is listed as future work.
- Defect localization and more explicit style representation are future directions rather than solved components.

## Reproducibility

- Code: not reported.
- Data: MVTec AD and MTD are public; SDI is public through the Bosch Research repository.
- Hyperparameters: full training details are delegated to appendix in the extracted text and are not preserved here.
- Random seeds: classifier evaluation uses five runs with different seeds.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: 128 x 128 resizing for GAN and classifier training.
- Artifact status: no code artifact reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Industrial anomaly detection]]
- Methods: [[Defect Transfer GAN]], [[GAN]], [[Synthetic data generation]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[Magnetic Tile Defects]], [[Bosch Surface Defect Inspection Dataset]]
- Benchmarks: [[MVTec AD]], [[Magnetic Tile Defects]], [[Bosch Surface Defect Inspection Dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[FID]], [[LPIPS]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]], [[Small-sample defect classification]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Builds on | The paper contrasts DT-GAN with Defect-GAN, noting that DT-GAN supports multimodality by varying defect styles. |
| [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] | Shares task and method family | Both use GAN-based defect synthesis to improve defect classification under scarce defect data. |
| [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] | Shares method family | Both address limited-data defect recognition with GAN-based augmentation. |

### Connection Rationale

- [[Defect Transfer GAN]] is the proposed method and central contribution.
- [[FID]] and [[LPIPS]] are used to evaluate generative quality and diversity.
- [[Small-sample defect classification]] is the downstream setting where synthetic images are evaluated.
- [[Bosch Surface Defect Inspection Dataset]] records the SDI dataset used for the downstream classifier experiments.

## Questions

- Which exact physical products are anonymized as Product A, Product B, and Product C?
- How do DT-GAN gains change when transferring to unseen products instead of held-out splits from known products?
- Can the model expose defect localization controls rather than only background, shape, and style controls?
- Which training hyperparameters are needed to reproduce the reported GAN and classifier experiments?
