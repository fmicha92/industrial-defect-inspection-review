---
title: "EID-GAN: Generative Adversarial Nets for Extremely Imbalanced Data Augmentation"
aliases:
  - "EID-GAN: Generative Adversarial Nets for Extremely Imbalanced Data Augmentation"
paper_key: "doi:10.1109/tii.2022.3182781"
paper_type: research
year: 2023
venue: "IEEE Transactions on Industrial Informatics"
authors:
  - "Wei Li"
  - "Jinlin Chen"
  - "Jiannong Cao"
  - "Chao Ma"
  - "Jia Wang"
  - "Xiaohui Cui"
  - "Ping Chen"
status: processed
processed_at: 2026-05-23
topics:
  - "extremely imbalanced data augmentation"
  - "GAN augmentation"
  - "tiny outlier synthesis"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Fabric Dataset]]"
  - "[[Piston Dataset]]"
  - "[[DAGM]]"
methods:
  - "[[EID-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[EID-GAN]]"
  - "[[DCGAN]]"
metrics:
  - "[[F1-score]]"
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[False alarm rate]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Error-Escape, False-Alarm, and F1-score are used to evaluate whether generated images improve outlier detection."
baselines:
  - "SMOTE"
  - "[[DCGAN]]"
  - "BAGAN"
  - "SN-GAN"
  - "WGAN-GP"
  - "horizontal flipping"
  - "mixup"
  - "Gaussian noise"
  - "VAE"
  - "Augmentor"
benchmarks:
  - "[[Fabric Dataset]]"
  - "[[Piston Dataset]]"
  - "[[DAGM]]"
code: "not reported"
data: "Fabric and Piston dataset availability not reported; DAGM is described as public"
doi: "10.1109/tii.2022.3182781"
arxiv: "not applicable"
url: "https://doi.org/10.1109/TII.2022.3182781"
pdf: "paper-inbox/10_processed/Research/2023 - Li - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation.pdf"
related_papers: []
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[EID-GAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[DCGAN]]"
related_datasets:
  - "[[Fabric Dataset]]"
  - "[[Piston Dataset]]"
  - "[[DAGM]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
related_benchmarks: []
source_file: "paper-inbox/10_processed/Research/2023 - Li - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Li - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Li - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation.txt"
artifact_status: "code not reported; Fabric and Piston source availability not reported"
tags:
  - paper
---
# EID-GAN: Generative Adversarial Nets for Extremely Imbalanced Data Augmentation

## Summary

Li et al. propose [[EID-GAN]], a GAN-based augmentation method for industrial datasets where the defective region is tiny relative to the image. The paper defines the Fabric and Piston datasets as extremely imbalanced because the outlier occupies roughly 1/2000 of a negative image; it treats DAGM category 1 as a general imbalanced comparison where the outlier occupies a larger region.

The method adds an outlier-focused norm penalty to a GAN generator loss. It extracts outlier regions from negative samples, crops a similar-sized region from each generated image, and penalizes the difference between that crop and a sampled real outlier. The goal is to force the generator to synthesize visible outliers rather than only matching the dominant normal-region distribution.

## Paper Type

- Type: research.
- Why: the paper introduces a new GAN training loss and evaluation protocol, then tests generated data for industrial outlier-detection augmentation.

## Problem

- Task: [[Surface defect detection]] and [[Defect classification]].
- Setting: industrial quality inspection with very few defective samples and extremely small outlier regions.
- Inputs: positive nondefective images, negative defective images, pixel masks for outliers in negative samples, and random latent vectors.
- Outputs: synthetic negative images containing outliers, filtered generated samples, and downstream Faster R-CNN outlier detection results.
- Motivation: vanilla GANs and common augmentation methods can match the image distribution while failing to synthesize tiny defect regions, making generated negative samples unusable.
- Assumption: outlier masks are available for negative samples so the method can construct an outlier dataset.

## Contribution

- Claimed: EID-GAN addresses extremely imbalanced data augmentation by integrating an outlier norm penalty into GAN training.
- Claimed: the paper proposes an evaluation method using two outlier detectors and k-fold cross-validation because ordinary classification, clustering, and FID do not assess tiny-outlier usefulness.
- Shown: only EID-GAN generates visible outliers in the Fabric, Piston, and DAGM qualitative comparisons, while SMOTE, DCGAN, WGAN-GP, SN-GAN, and BAGAN do not synthesize the desired outliers.
- Shown: generated EID-GAN samples improve Faster R-CNN outlier-detection evaluation on Fabric, Piston, and DAGM according to lower Error-Escape/False-Alarm and higher F1-score trends reported in Tables I-III.

## Method

- Core idea: train a GAN with an added penalty that compares a generated crop against a real outlier crop, forcing generator attention toward tiny defects.
- Outlier extraction: each original negative sample is multiplied by its mask to construct an outlier dataset.
- Per-iteration penalty: after generating an image, the method crops a generated region with a size similar to a randomly selected real outlier and computes `lambda * |anoi - Gcrop(z)|`.
- Loss integration: the norm penalty is combined with the original generator loss and minimized through backpropagation.
- Architecture: EID-GAN uses a vanilla DCGAN-style architecture with Conv-BatchNorm-ReLU in the generator and Conv-BatchNorm-LeakyReLU in the discriminator.
- Selected penalty setting: the Fabric experiment reports `lambda = 0.01` as producing high-quality generated images with clear outliers; larger values reduced image quality and `lambda = 0.001` produced no outlier.
- Evaluation detector: Faster R-CNN is used as the outlier detector in the proposed evaluation protocol.

## ML / DL Extraction

### Task Formulation

- Input modality: industrial RGB or grayscale images with tiny outlier regions.
- Output target: generated negative images containing outliers; downstream detector predictions over outlier boxes.
- Supervision: negative-sample outlier masks are used to build the outlier dataset for the penalty.
- Objective: GAN minimax objective plus outlier norm penalty.

### Model And Training

- Model family: [[GAN]] and [[Generative Models]].
- Architecture: DCGAN-style EID-GAN.
- Fabric training: batch size 1; discriminator trained on real data while freezing generator, discriminator trained on generated data, then generator trained with discriminator output plus outlier penalty.
- Main experiment training epochs: 100 for all augmentation models.
- Faster R-CNN detector training in Fabric evaluation: 1000 epochs.
- Hyperparameter explicitly reported: `lambda = 0.01` for the main EID-GAN norm penalty in Fabric.
- Parameters, optimizer, hardware, seeds, and training time: not reported in the extracted source.

### Data

- [[Fabric Dataset]]: 100 negative samples, image size 3 x 1024 x 1024; treated as extremely imbalanced.
- [[Piston Dataset]]: 70 negative samples, image size 3 x 480 x 480; treated as extremely imbalanced.
- [[DAGM]]: public DAGM category 1, 150 negative images, image size 1 x 512 x 512; treated as general imbalanced because the outlier is larger than in Fabric and Piston.
- Evaluation splitting: the Fabric evaluation uses training:test = 0.6:0.4 for original negative samples and three-fold cross-validation with Faster R-CNN.
- Synthetic filtering: in the Fabric experiment, EID-GAN synthesizes 100 instances; Faster R-CNN detects outliers in 60 synthetic instances, which are then aggregated with the training data.
- Dataset licenses and full collection details: not reported.

### Evaluation

- Proposed evaluation: train an outlier detector on original negative training data, test it, generate synthetic samples, filter generated samples whose outliers are detected, aggregate detected synthetic samples with original training data, retrain a detector, and compare results on the same test set with k-fold cross-validation.
- Metrics: Error-Escape, False-Alarm, and F1-score.
- Metric direction: lower is better for Error-Escape and False-Alarm; higher is better for F1-score.
- Baselines: SMOTE, DCGAN, BAGAN, SN-GAN, WGAN-GP, flipping, Gaussian noise, mixup, VAE, and Augmentor.
- Traditional metrics rejected: classification accuracy, K-Means clustering, and FID are shown as unsuitable for this setting because positive and negative images have similar distributions and FID can rate images without useful outliers favorably.

## Evidence

### Experimental Setup

- Fabric and Piston are used as extremely imbalanced industrial datasets; DAGM is used as a general imbalanced dataset.
- The paper compares generated images qualitatively and evaluates whether generated images improve a Faster R-CNN outlier detector.
- The same training epoch count, 100, is used for all augmentation models in the main comparison.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---|---|---|
| Generated-image quality | [[Fabric Dataset]] | visible tiny outlier | qualitative | SMOTE, DCGAN, WGAN-GP, SN-GAN, BAGAN fail to synthesize outliers | EID-GAN synthesizes visible outliers | Figure 7. |
| Generated-image quality | [[Piston Dataset]] | visible tiny outlier | qualitative | SMOTE, DCGAN, WGAN-GP, SN-GAN, BAGAN fail to synthesize outliers | EID-GAN synthesizes visible outliers | Figure 11. |
| Generated-image quality | [[DAGM]] | visible outlier | qualitative | SMOTE, DCGAN, WGAN-GP, SN-GAN, BAGAN fail to synthesize desired outliers | EID-GAN synthesizes expected outliers | Figure 13. |
| Fabric synthetic filtering | [[Fabric Dataset]] / generated-sample utility | detected generated outliers | higher | not applicable | 60 of 100 EID-GAN synthetic instances are detected by Faster R-CNN | Used before aggregation and detector retraining. |
| Detector improvement | [[Fabric Dataset]] | Error-Escape / False-Alarm / F1-score | lower/lower/higher | without synthetic, flipping, mixup | EID-GAN row is reported best | Numeric table values were not preserved by the extractor. |
| Detector improvement | [[Piston Dataset]] | Error-Escape / False-Alarm / F1-score | lower/lower/higher | original detector and non-EID-GAN augmentation | EID-GAN improves detection | Numeric table values were not preserved by the extractor. |
| Detector improvement | [[DAGM]] | Error-Escape / False-Alarm / F1-score | lower/lower/higher | original detector and non-EID-GAN augmentation | EID-GAN improves detection | Numeric table values were not preserved by the extractor. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| Error-Escape | Outlier detector evaluation | exact formula not preserved in extracted text | lower | no | Used with False-Alarm and F1-score. |
| [[False alarm rate]] | Outlier detector evaluation | exact formula not preserved in extracted text | lower | no | The paper calls this False-Alarm. |
| [[F1-score]] | Outlier detector evaluation | harmonic mean of recall and precision | higher | yes | Used to assess whether synthetic samples improve outlier detection. |
| [[Recall]] | F1-score definition | fraction of target instances retrieved | higher | no | Mentioned in metric definition. |
| [[Precision]] | F1-score definition | fraction of detections that are target instances | higher | no | Mentioned in metric definition. |

## Dataset / Benchmark Details

- Fabric: industrial fabric inspection images; defective outliers occupy approximately 1/2000 of the image.
- Piston: industrial piston inspection images; defective outliers occupy approximately 1/2000 of the image.
- DAGM: public synthetic textured-surface defect dataset; category 1 is used.
- Extremely imbalanced definition: Fabric and Piston are extremely imbalanced because outliers are tiny compared with full image size.
- General imbalanced definition: DAGM is general imbalanced because its outlier occupies a larger image region, roughly 1/23 according to Figure 1.
- Source availability: DAGM is described as public; Fabric and Piston sources are not reported in the extracted text.

## Limitations

- The extracted source does not preserve the numeric entries of Tables I-III; only the comparative conclusions around those tables are available.
- Code and implementation release are not reported.
- Fabric and Piston dataset source, license, and collection details are not reported.
- The method depends on masks for original negative samples to extract outliers.
- The paper does not report repeated-run variance or statistical significance.

## Reproducibility

- Code: not reported.
- Data: DAGM is public; Fabric and Piston availability is not reported.
- Hyperparameters: lambda = 0.01 for the Fabric EID-GAN norm penalty; training epoch 100 for all augmentation models; Faster R-CNN epoch 1000 in Fabric detector evaluation.
- Random seeds: not reported.
- Environment/hardware: not reported.
- Checkpoints/models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]]
- Methods: [[EID-GAN]], [[GAN]], [[DCGAN]], [[Data augmentation]]
- Datasets: [[Fabric Dataset]], [[Piston Dataset]], [[DAGM]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[F1-score]], [[Recall]], [[Precision]], [[False alarm rate]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - Diversified and Multi-Class Controllable Industrial Defect Synthesis for Data Augmentation and Transfer]] | Shares method family | Both generate industrial defect samples for augmentation; EID-GAN focuses on tiny outlier synthesis, while DCDGANc focuses on controllable pixel-labeled defect-content synthesis and compositing. |
| [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] | Shares method family | Both use GAN-based augmentation for limited industrial defect data, but this paper targets extremely tiny outliers in generated negative samples. |
| [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] | Shares method family | Both add GAN training constraints for industrial defect data generation; this paper adds an explicit outlier norm penalty. |

### Backlinks Updated

- [[EID-GAN]], [[Fabric Dataset]], [[Piston Dataset]], and [[DAGM]] were reviewed or updated during audit.

## Questions

- Are the Fabric and Piston datasets publicly available or proprietary?
- Are EID-GAN code, masks, or generated examples released outside the IEEE paper?
- Can the missing table values be recovered from direct PDF table extraction if exact Error-Escape, False-Alarm, and F1 values are needed?
