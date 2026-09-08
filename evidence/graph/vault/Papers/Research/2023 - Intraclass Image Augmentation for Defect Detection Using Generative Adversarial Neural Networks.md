---
title: "Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks"
aliases:
  - "Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks"
paper_key: "sha256:dc16b34b08bf5426ed902268a10403a5641eeddf372215cf4404092e2908410b"
paper_type: research
year: 2023
venue: "Sensors"
authors:
  - "Vignesh Sampath"
  - "Inaki Maurtua"
  - "Juan Jose Aguilar Martin"
  - "Ander Iriondo"
  - "Iker Lluvia"
  - "Gotzone Aizpurua"
status: processed
processed_at: 2026-05-23
topics:
  - "intraclass augmentation"
  - "magnetic particle inspection"
  - "GAN defect generation"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Magnetic Particle Inspection Dataset]]"
methods:
  - "[[Magna-Defect-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Defect synthesis]]"
  - "[[Pix2Pix]]"
  - "[[CycleGAN]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[Magna-Defect-GAN]]"
  - "[[U-Net]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
  - "[[FID]]"
  - "[[Inception Score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Precision = TP / (TP + FP)"
  - "Recall = TP / (TP + FN)"
  - "F1 = 2 * precision * recall / (precision + recall)"
  - "Accuracy = (TP + TN) / (TP + FP + TN + FN)"
baselines:
  - "[[Pix2Pix]]"
  - "[[CycleGAN]]"
  - "ResNet"
  - "[[EfficientNet]]"
benchmarks:
  - "[[Magnetic Particle Inspection Dataset]]"
code: "not reported"
data: "available upon request from the corresponding author"
doi: "10.3390/s23041861"
url: "https://doi.org/10.3390/s23041861"
pdf: "paper-inbox/10_processed/Research/2023 - Sampath - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Defect synthesis]]"
related_methods:
  - "[[Magna-Defect-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Defect synthesis]]"
  - "[[Pix2Pix]]"
  - "[[CycleGAN]]"
related_datasets:
  - "[[Magnetic Particle Inspection Dataset]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2023 - Sampath - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Sampath - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Sampath - Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks.txt"
artifact_status: "data available upon request; code not reported"
tags:
  - paper
---
# Intraclass Image Augmentation for Defect Detection Using Generative Adversarial Neural Networks

## Summary

This paper proposes [[Magna-Defect-GAN]], a conditional mask-to-image GAN for generating high-resolution magnetic particle inspection defect images with controlled intraclass variation. The method uses defect masks, latent noise, and a three-part guide vector for background, defect thickness, and brightness to synthesize defect samples, then uses those samples to improve binary defect classification on a line-scan fastener inspection dataset.

## Paper Type

Research paper. It contributes a synthetic-data method, collects an inspection dataset, compares generated-image quality against image-to-image GAN baselines, and evaluates whether generated samples improve downstream defect classification.

## Problem

Magnetic particle inspection produces visible defect indications on ferromagnetic parts, but collecting many defective images with varied background, lighting, particle concentration, defect size, defect shape, and defect position is expensive because defects are rare. A classifier trained on a small, low-diversity dataset can overfit and generalize poorly.

## Contribution

- Introduces a line-scan magnetic particle inspection dataset for cylindrical fastener defect detection.
- Proposes [[Magna-Defect-GAN]], a conditional mask-to-image GAN that combines mask embeddings, latent noise, and fine-grained guide labels for background, thickness, and brightness.
- Shows that Magna-Defect-GAN improves generative quality over [[Pix2Pix]] and [[CycleGAN]] on the reported [[Inception Score]] and [[FID]] metrics.
- Shows that downstream classifiers perform best when ImageNet pretraining, conventional augmentation, and GAN-generated synthetic images are combined.

## Method

Magna-Defect-GAN maps a defect mask, guide vector, and latent noise vector to a synthetic defect image. The generator uses a U-Net-style design with two branches. The mask projection branch encodes the input mask into a 32-dimensional embedding through seven stride-2 convolution layers with Leaky ReLU activations. The latent projection branch combines that mask embedding with a 132-dimensional latent noise vector and a guide vector that controls background, defect thickness, and brightness.

The discriminator is a modified PatchGAN discriminator. Instead of classifying the whole image as real or fake, it evaluates local image patches; the paper uses 16 x 16 patches because smaller patches combined with style-transfer losses produced sharper images and reduced tiling artifacts for this task.

The generator loss combines adversarial, reconstruction, and style losses:

- Adversarial loss encourages local realism.
- Reconstruction loss is an L2 pixel-wise loss between generated and target images.
- Style loss uses a pretrained VGG feature extractor and Gram-matrix feature correlations to preserve visual texture and color.
- Loss weights are reported as lambda1 = 10 for adversarial loss and lambda2 = lambda3 = 0.1 for reconstruction and style loss.

## Dataset

The [[Magnetic Particle Inspection Dataset]] was collected with a DALSA Linea 2k 7.04 um 2048 x 2-26 kHz color line-scan camera on a magnetic particle inspection apparatus at Erreka Fastening Solutions. The camera used a 12 mm fixed focal length lens and 600 mm field of view. The dataset contains 1050 RGB images. The paper reports 780 nondefective and 270 defective images used to train Magna-Defect-GAN.

Experienced quality engineers annotated ground-truth masks and guide labels. The annotations include defect shape, location, number, thickness, brightness, and background so the generator can condition outputs on both mask geometry and visual appearance.

## Evidence

### Experimental Setup

- Train/test split: random 80% training and 20% test split.
- GAN training: average of 200 epochs.
- Learning rate: constant for the first 100 epochs, then exponentially decayed to zero.
- Initialization: Gaussian weights with mean 0 and standard deviation 0.01.
- Hardware: Google Cloud infrastructure with a single Nvidia 12 GB Titan X GPU.
- Generation speed: 0.0265 ms per image.
- Downstream classifiers: ResNet and EfficientNet-B7.
- Classification training schemes: original only; conventional augmentation; synthetic pretraining plus original fine-tuning; ImageNet pretraining plus conventional augmentation; ImageNet pretraining plus synthetic data; ImageNet pretraining plus mixed conventional and synthetic augmentation.

### Generated-Image Quality

| Model | Inception Score | FID |
|---|---:|---:|
| [[CycleGAN]] | 2.88 +/- 0.25 | 91.56 |
| [[Pix2Pix]] | 3.08 +/- 0.31 | 65.09 |
| [[Magna-Defect-GAN]] | 3.88 +/- 0.36 | 50.03 |

Higher [[Inception Score]] is better; lower [[FID]] is better. The paper also uses t-SNE visualization to argue that generated samples overlap with and extend the real training-data distribution.

## Performance Metrics

Primary downstream metric: [[F1-score]], with [[Accuracy]], [[Precision]], and [[Recall]] reported for defect classification. Generative quality is evaluated with [[Inception Score]] and [[FID]].

| Scheme | Classifier | Recall | Precision | F1-score | Accuracy |
|---|---|---:|---:|---:|---:|
| Original dataset only | ResNet | 0.684 | 0.969 | 0.801 | 0.808 |
| Original dataset only | EfficientNet-B7 | 0.847 | 0.945 | 0.893 | 0.898 |
| Conventional augmentation | ResNet | 0.873 | 0.865 | 0.868 | 0.835 |
| Conventional augmentation | EfficientNet-B7 | 0.895 | 0.943 | 0.918 | 0.918 |
| Synthetic pretraining + original fine-tuning | ResNet | 0.863 | 0.907 | 0.880 | 0.875 |
| Synthetic pretraining + original fine-tuning | EfficientNet-B7 | 0.909 | 0.942 | 0.925 | 0.925 |
| ImageNet pretraining + conventional augmentation | ResNet | 0.942 | 0.898 | 0.919 | 0.898 |
| ImageNet pretraining + conventional augmentation | EfficientNet-B7 | 0.958 | 0.935 | 0.946 | 0.947 |
| ImageNet pretraining + synthetic fine-tuning | ResNet | 0.945 | 0.934 | 0.939 | 0.927 |
| ImageNet pretraining + synthetic fine-tuning | EfficientNet-B7 | 0.961 | 0.972 | 0.966 | 0.964 |
| ImageNet pretraining + mixed conventional and synthetic augmentation | ResNet | 0.955 | 0.940 | 0.947 | 0.935 |
| ImageNet pretraining + mixed conventional and synthetic augmentation | EfficientNet-B7 | 0.969 | 0.977 | 0.973 | 0.972 |

The strongest downstream result is EfficientNet-B7 with ImageNet pretraining and mixed conventional plus synthetic augmentation: 0.973 F1 and 0.972 accuracy.

## ML / DL Extraction

### Task Formulation

- Input: MPI line-scan RGB images and defect masks.
- Output: generated defect images for augmentation; binary defect/nondefect predictions for downstream classification.
- Supervision: supervised mask-to-image generation and supervised binary classification.
- Synthetic-data role: pixel-level intraclass augmentation to increase variation in defect size, shape, position, thickness, brightness, and background.

### Model And Training

- Generator: U-Net-style conditional generator with mask projection and latent projection branches.
- Discriminator: modified PatchGAN discriminator with 16 x 16 local patches.
- Losses: adversarial, L2 reconstruction, and VGG-based style loss.
- GAN epochs: average 200.
- Classifiers: ResNet and EfficientNet-B7.
- Compute: single Nvidia 12 GB Titan X GPU on Google Cloud.

### Evaluation

- Generative quality: [[Inception Score]], [[FID]], and t-SNE visualization.
- Classifier performance: [[Precision]], [[Recall]], [[F1-score]], and [[Accuracy]].
- Baselines: [[CycleGAN]], [[Pix2Pix]], original-only classification, conventional augmentation, synthetic-only fine-tuning, and mixed augmentation settings.

## Limitations

- The dataset is not public in the paper; the data availability statement says it is available upon request from the corresponding author.
- The extracted source text does not report a code repository.
- The paper notes that GAN-generated images can interpolate between discrete training-data points and bridge holes in the data manifold, but cannot expand the distribution beyond the extremes of the training dataset.
- The evaluation uses one MPI fastener dataset, so transfer to other materials, part geometries, and inspection setups remains untested in the source.

## Reproducibility

- Code: not reported.
- Data: available upon request from the corresponding author.
- License: paper is open access under CC BY 4.0; dataset license is not reported.
- Funding: DIGIMAN4.0 Horizon 2020 and 5R Red Cervera support are reported.
- Conflicts of interest: none declared.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]]
- Methods: [[Magna-Defect-GAN]], [[GAN]], [[Data augmentation]], [[Defect synthesis]], [[Pix2Pix]], [[CycleGAN]]
- Datasets: [[Magnetic Particle Inspection Dataset]]
- Domains: [[Metal inspection]]
- Metrics: [[Precision]], [[Recall]], [[F1-score]], [[Accuracy]], [[FID]], [[Inception Score]]

### Shares Dataset

- [[Magnetic Particle Inspection Dataset]]: the paper introduces and evaluates on this line-scan MPI fastener dataset.

### Shares Method

- [[Magna-Defect-GAN]]: this is the proposed method for mask-conditioned defect image synthesis.
- [[Defect synthesis]]: the paper uses generated defect images to improve classifier training under limited real data.
- [[Pix2Pix]] and [[CycleGAN]]: used as generated-image quality baselines.

### Shares Task

- [[Surface defect detection]]: downstream classifiers distinguish defective from nondefective MPI images.
- [[Defect classification]]: the downstream task is binary defect/nondefect classification.

### Shares Metric

- [[F1-score]] and [[Accuracy]]: primary downstream classifier metrics.
- [[Precision]] and [[Recall]]: reported for downstream classifiers.
- [[FID]] and [[Inception Score]]: used for generative image quality.

### Application / Domain

- [[Metal inspection]]: the dataset is based on magnetic particle inspection of fasteners made from magnetic materials.

## Questions

- Would Magna-Defect-GAN improve segmentation or localization performance, not only binary classification?
- How does the method transfer to public MPI, steel, or casting datasets with different part geometry and lighting?
- What is the exact access process and license for the acquired MPI dataset?
