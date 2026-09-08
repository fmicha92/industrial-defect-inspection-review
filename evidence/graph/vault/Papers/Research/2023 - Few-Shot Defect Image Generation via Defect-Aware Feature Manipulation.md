---
title: "Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation"
aliases:
  - "Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation"
paper_key: "sha256:392c918e8c501e0f0ff460f0a6cc0bb8174a6df100257d2a55df60067a969c22"
paper_type: research
year: 2023
venue: "AAAI 2023"
authors:
  - "Yuxuan Duan"
  - "Yan Hong"
  - "Li Niu"
  - "Liqing Zhang"
status: processed
processed_at: 2026-05-23
topics:
  - "few-shot defect generation"
  - "defect-aware feature manipulation"
  - "GAN synthesis"
tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "[[Defect-aware feature manipulation]]"
  - "[[DFMGAN]]"
  - "[[StyleGAN2]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[StyleGAN2]]"
  - "[[DFMGAN]]"
metrics:
  - "[[KID]]"
  - "[[LPIPS]]"
  - "[[Accuracy]]"
primary_metric: "[[KID]]"
metric_definitions:
  - "KID x10^3 @5k: lower is better; clustered LPIPS @1k: higher is better; classification accuracy: higher is better."
baselines:
  - "Finetune"
  - "DiffAug"
  - "CDC"
  - "Crop&Paste"
  - "SDGAN"
  - "Defect-GAN"
benchmarks:
  - "[[MVTec AD]]"
code: "https://github.com/Ldhlwh/DFMGAN"
data: "MVTec AD: https://www.mvtec.com/company/research/datasets/mvtec-ad"
doi: "not reported"
arxiv: "not reported"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/25135"
pdf: "paper-inbox/10_processed/Research/2023 - Duan - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation.pdf"
related_papers:
  - "[[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]]"
  - "[[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Defect-aware feature manipulation]]"
  - "[[DFMGAN]]"
  - "[[StyleGAN2]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[MVTec AD]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "[[MVTec AD]]"
source_file: "paper-inbox/10_processed/Research/2023 - Duan - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Duan - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Duan - Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation.txt"
artifact_status: "code reported available"
tags:
  - paper
---
# Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation

## Summary

Duan et al. introduce [[DFMGAN]], a few-shot defect image generation method that starts from a StyleGAN2 backbone trained on defect-free images and then learns defect-aware residual blocks from a handful of defect images. The added blocks generate defect masks and manipulate only the masked feature regions, allowing the model to generate paired defect-free images, defect masks, and defect images.

The main experiments use [[MVTec AD]], especially the hazelnut object category with crack, cut, hole, and print defects. DFMGAN reports the best KID/LPIPS combination in all four hazelnut defect categories and the best downstream defect-classification accuracy across three random train/test partitions.

## Paper Type

- Type: research.
- Why: the paper proposes a generative model and evaluates generated images for both visual generation quality and downstream defect classification.

## Problem

- Task: few-shot defect image generation for [[Defect classification]] and [[Surface defect detection]] support.
- Setting: industrial inspection where only a handful of defect images are available but more defect-free images exist.
- Inputs: defect-free MVTec AD images, limited defect images, pixel-level defect masks, object latent code `zobject`, and defect latent code `zdefect`.
- Outputs: generated defect images, generated masks, and optionally paired defect-free images.
- Motivation: unsupervised defect inspection methods trained on defect-free data cannot distinguish defect categories, while direct defect generation is hard because defect samples are rare and defects occupy specific regions rather than entire images.

## Contribution

- Claimed: first few-shot defect image generation method tested on modern multi-object/multi-texture MVTec AD categories.
- Claimed: transfers critical defect regions rather than whole-image distributions.
- Claimed: defect-aware residual blocks generate plausible masks and manipulate object features only inside defect regions.
- Shown: DFMGAN outperforms Finetune, DiffAug, CDC, Crop&Paste, SDGAN, and Defect-GAN on hazelnut KID/LPIPS and downstream defect classification.
- Shown: generated masks precisely delimit defect regions in examples, enabling future mask-based tasks even though the paper evaluates downstream classification.

## Method

- Stage 1: train a data-efficient [[StyleGAN2]] with Adaptive Differentiable Augmentation on defect-free images of an MVTec object or texture category.
- Stage 2: freeze the StyleGAN2 backbone, attach defect-aware residual blocks and a defect mapping network, and train only the added modules on limited defect images.
- Defect-aware residual blocks: start manipulating features at 64 x 64 resolution, generate masks through ToMask, and add residual defect features only where the mask is nonnegative.
- Feature preservation: synthesis blocks at 32 x 32 or lower are left untouched because lower-resolution network layers control coarse object structure.
- Defect diversity: a separate defect mapping network maps `zdefect` to `wdefect`; a mode-seeking loss encourages different defect masks for different defect codes.
- Discriminators: a StyleGAN2-style image discriminator judges realism, while a smaller matching discriminator judges whether image/mask pairs match.
- Objective: StyleGAN2 loss plus matching-discriminator loss plus `lambda * Lms`, with `lambda = 0.1` generally reported as producing good results.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial RGB images from MVTec AD with pixel masks.
- Output target: generated defect images and masks; downstream ResNet-34 classification of hazelnut defect categories.
- Supervision: defect-free images for Stage 1; limited defect images and masks for Stage 2.
- Objective: adversarial image realism, image/mask matching, and defect-mask diversity through mode seeking.

### Model And Training

- Model family: [[GAN]] and [[Generative Models]].
- Backbone: [[StyleGAN2]] with Adaptive Differentiable Augmentation.
- Trainable parameters: Stage 1 StyleGAN2 backbone has 23.2M trainable parameters; Stage 2 added modules have 3.7M trainable parameters.
- Matching discriminator: 1.5M parameters, compared with 24M for the original discriminator.
- Stage 2 fixed component: the pretrained backbone is frozen.
- Stage 2 trained components: defect mapping network, defect-aware residual blocks, image discriminator finetuning, and matching discriminator.
- Losses: StyleGAN2 adversarial/path-length/R1 terms, Wasserstein adversarial loss with R1 regularization for matching, and modified mode-seeking loss.
- Hyperparameter: mode-seeking loss weight `lambda = 0.1`.
- Optimizer, hardware, seeds, and training time: not reported in the extracted source.

### Data

- Dataset: [[MVTec AD]].
- MVTec AD scope: ten object categories and five texture categories, with up to eight defect categories per object/texture category.
- Image annotations: pixel-level masks show defect regions.
- Dataset availability: the paper reports `https://www.mvtec.com/company/research/datasets/mvtec-ad` and CC BY-NC-SA 4.0.
- Experimental focus: hazelnut object category with crack, cut, hole, and print defect categories.
- Few-shot setting: most MVTec object/texture categories have 200-400 defect-free samples, while most defect categories have 10-25 defect images.
- Preprocessing: all images are resized to 256 x 256.
- Downstream classification split: one third of images from each hazelnut defect category are selected as base sets; the other two thirds are combined as the test set.
- Hazelnut classification data: each base set has five or six images per defect category; the test set has 12 images per category, 48 total.

### Evaluation

- Generation metrics: [[KID]] x10^3 @5k and clustered [[LPIPS]] @1k.
- KID direction: lower is better.
- LPIPS direction: higher is better for diversity in this clustered setting.
- Classification metric: [[Accuracy]] on held-out hazelnut defect images.
- Generation baselines: Finetune, DiffAug, CDC, Crop&Paste, SDGAN, Defect-GAN.
- Downstream classifier: ResNet-34 trained on each method's generated training set.
- Generated training size: each method generates 1,000 images for each of four defect categories, giving 4,000 generated images.
- Repeats: downstream classification is repeated three times with different base/test partitions.

## Evidence

### Experimental Setup

- DFMGAN trains a separate model for each MVTec defect category associated with an object or texture category.
- The main paper focuses on hazelnut because it has high natural variation and complex appearance.
- The paper omits Crop&Paste KID values because Crop&Paste images have almost the same appearance distribution as the source dataset.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Generation quality/diversity | MVTec hazelnut crack | KID / LPIPS | lower / higher | Defect-GAN 19.73 / 0.1905; DiffAug 24.69 / 0.0570 | 19.73 / 0.2600 | DFMGAN ties best KID among reported non-Crop&Paste values and has best LPIPS. |
| Generation quality/diversity | MVTec hazelnut cut | KID / LPIPS | lower / higher | Defect-GAN 16.88 / 0.1734; DiffAug 19.84 / 0.0456 | 16.88 / 0.2073 | DFMGAN best LPIPS and tied/best KID among reported values. |
| Generation quality/diversity | MVTec hazelnut hole | KID / LPIPS | lower / higher | DiffAug 22.43 / 0.0466; Defect-GAN 36.30 / 0.2007 | 20.78 / 0.2391 | DFMGAN best KID and LPIPS. |
| Generation quality/diversity | MVTec hazelnut print | KID / LPIPS | lower / higher | Finetune 28.75 / 0.1526; Defect-GAN 33.35 / 0.2007 | 27.25 / 0.2649 | DFMGAN best KID and LPIPS among reported values. |
| Downstream classification | MVTec hazelnut partition P1 | Accuracy | higher | Finetune 70.83; Crop&Paste 66.67 | 83.33 | ResNet-34 trained on generated images. |
| Downstream classification | MVTec hazelnut partition P2 | Accuracy | higher | Finetune 72.91; Defect-GAN 68.75 | 81.25 | ResNet-34 trained on generated images. |
| Downstream classification | MVTec hazelnut partition P3 | Accuracy | higher | Finetune 70.83; DiffAug 68.75 | 81.25 | ResNet-34 trained on generated images. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[KID]] | Few-shot defect image generation | KID x10^3 @5k between 5,000 generated images and corresponding real defect images | lower | yes | Chosen because it is unbiased and more descriptive on small datasets than FID. |
| [[LPIPS]] | Diversity of generated images | clustered LPIPS @1k, averaged over clusters assigned to nearest real defect image | higher | no | Used because KID/FID can prefer realism over diversity. |
| [[Accuracy]] | Downstream defect classification | percentage accuracy on held-out defect images | higher | no | ResNet-34 classification across hazelnut defect categories. |

## Dataset / Benchmark Details

- MVTec AD categories: ten object and five texture categories; most have 200-400 defect-free images and 10-25 defect images per defect category.
- Main category: hazelnut.
- Main defect classes: crack, cut, hole, print.
- Image size: 256 x 256 after resizing.
- Labels/annotations: pixel-level masks are used by DFMGAN and available in MVTec AD.
- License: CC BY-NC-SA 4.0 for MVTec AD, as reported by the paper.
- Leakage risks: downstream classification uses random base/test partitions repeated three times; no additional leakage audit is reported.

## Limitations

- The paper leaves 5-shot and 1-shot generation results, other object/texture categories, implementation details, and ablation details to supplementary material.
- Downstream evaluation is classification, not localization, because most baselines do not produce clear masks.
- The paper does not report optimizer, hardware, seed, or training-time details in the extracted main text.
- DOI is not reported in the extracted paper text.

## Reproducibility

- Code: `https://github.com/Ldhlwh/DFMGAN`.
- Data: [[MVTec AD]], reported at `https://www.mvtec.com/company/research/datasets/mvtec-ad`.
- Hyperparameters: images resized to 256 x 256; `lambda = 0.1` for mode-seeking loss; 1,000 generated images per defect category for classification.
- Random seeds: not reported.
- Environment/hardware: not reported.
- Checkpoints/models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Surface defect detection]]
- Methods: [[Defect-aware feature manipulation]], [[DFMGAN]], [[StyleGAN2]], [[GAN]], [[Data augmentation]]
- Learning setup: [[Few-shot zero-shot learning]]
- Datasets: [[MVTec AD]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[KID]], [[LPIPS]], [[Accuracy]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]] | Shares method family and dataset | Both use MVTec AD and generate industrial defect images for augmentation; DFMGAN manipulates defect-aware features in a StyleGAN2 backbone, while DCDGANc separates defect content generation and compositing. |
| [[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]] | Shares augmentation objective | Both address scarce industrial defect data with GAN-based generation; EID-GAN targets tiny outliers with an outlier penalty, while DFMGAN targets few-shot defect generation with masks. |
| [[2022 - Defect Transfer GAN Diverse Defect Synthesis for Data Augmentation]] | Shares defect-synthesis theme | Both synthesize defect images for augmentation, but this paper emphasizes few-shot object/texture defect generation and paired mask output. |

### Backlinks Updated

- [[DFMGAN]], [[Defect-aware feature manipulation]], [[StyleGAN2]], [[MVTec AD]], and [[Few-shot zero-shot learning]] were reviewed or updated during audit.

## Questions

- Do supplementary materials report optimizer, hardware, training time, ablation values, and 5-shot/1-shot results?
- Is there a stable DOI for the AAAI proceedings version not captured in the preprocessed source?
