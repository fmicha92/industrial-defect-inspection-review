---
title: "A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples"
aliases:
  - "A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples"
paper_key: "doi:10.1109/tii.2022.3168432"
paper_type: research
year: 2022
venue: "IEEE Transactions on Industrial Informatics"
authors:
  - "Long Wen"
  - "You Wang"
  - "Xinyu Li"
status: processed
processed_at: 2026-05-23
topics:
  - "small-sample defect classification"
  - "cycle-consistent GAN"
  - "attention mechanism"
tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[KolektorSDD]]"
  - "[[DAGM2007]]"
methods:
  - "[[AttenCGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[AttenCGAN]]"
  - "CycleGAN"
  - "Inception V3"
metrics:
  - "[[Accuracy]]"
  - "[[FID]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: classification accuracy for surface defect classification."
  - "FID: Frechet Inception Distance for generated defect image quality; lower is better."
baselines:
  - "MobileNet-V2"
  - "ResNet-50"
  - "VGG16"
  - "SDCNN without synthetic defect images"
  - "GAN"
  - "StarGAN"
benchmarks:
  - "[[KolektorSDD]]"
  - "[[DAGM2007]]"
code: "not reported"
data: "public benchmark datasets used"
doi: "10.1109/tii.2022.3168432"
arxiv: "not reported"
url: "https://doi.org/10.1109/TII.2022.3168432"
pdf: "paper-inbox/10_processed/Research/2022 - Wen - A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Small-sample defect classification]]"
related_methods:
  - "[[AttenCGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[KolektorSDD]]"
  - "[[DAGM2007]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "[[KolektorSDD]]"
  - "[[DAGM2007]]"
source_file: "paper-inbox/10_processed/Research/2022 - Wen - A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Wen - A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Wen - A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples.txt"
artifact_status: "not reported"
tags:
  - paper
---
# A New Cycle-consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples

## Summary

Wen et al. propose [[AttenCGAN]] for small-sample surface defect classification. The method uses CycleGAN to synthesize pseudo defect samples from very few real defect images, then trains an attention-enhanced surface defect CNN that highlights discriminative defect regions through bilinear attention pooling and attention-guided cropping/dropping augmentation.

The paper evaluates AttenCGAN on [[KolektorSDD]] and [[DAGM2007]]. With eight defect samples on KolektorSDD, AttenCGAN reports 98.53% accuracy. With forty defect samples per class on DAGM2007 classes 1-6, it reports 99.57% average accuracy. The source also reports degradation under extreme one-sample settings but shows AttenCGAN remains above the compared MobileNet-V2, ResNet-50, VGG16, and SDCNN baselines.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a new GAN-based augmentation and classification method for surface defect classification with small samples.

## Problem

- Task: [[Defect classification]] and [[Surface defect detection]].
- Setting: industrial visual inspection where defect samples are scarce and normal/defect differences can be small.
- Inputs: surface defect images and defect-free images from KolektorSDD and DAGM2007.
- Outputs: generated pseudo defect images and defect classification predictions.
- Motivation: supervised deep learning SDC models need large training sets, but many industrial environments provide fewer than ten defect samples.
- Assumptions: at least one real defect sample is available; zero-shot defect classification is not handled.

## Contribution

- Claimed: combines CycleGAN-based pseudo defect synthesis with an attention mechanism for small-sample SDC.
- Claimed: uses attention to find discriminative defect regions and enlarge small interclass differences.
- Shown: AttenCGAN outperforms MobileNet-V2, ResNet-50, VGG16, and SDCNN without synthetic defect images across the reported small-sample settings.
- Shown: AttenCGAN produces better FID values than GAN and StarGAN in the reported GAN comparison.

## Method

AttenCGAN first trains a CycleGAN image-translation model between nondefect and defect domains. The CycleGAN uses adversarial least-squares loss plus cycle consistency loss; lambda is set to 10. Before CycleGAN training, standard augmentation is applied, including center crop, color jitter, random grayscale, random rotation, and combinations of these transforms.

The generated pseudo defect images are used to train SDCNN, an Inception V3-based classification network with attention. SDCNN contains auto data augmentation, feature extraction, bilinear attention pooling, and attention-guided data augmentation. The attention map is produced with a 1x1 convolution over the feature map. Attention-guided cropping keeps discriminative areas, while attention-guided dropping suppresses them so the classifier also learns other useful regions.

## Evidence

### Experimental Setup

- Datasets: [[KolektorSDD]] and [[DAGM2007]].
- KolektorSDD: 399 electrical commutator images, including 50 visible-defect images.
- DAGM2007: ten types of artificial surface images; each type has 1,000 defect-free images and 150 defective images. The paper uses classes 1-6.
- Synthetic data protocol: randomly select a small number of real defect images, synthesize 200 pseudo defect samples with AttenCGAN, then use those samples to train SDCNN.
- KolektorSDD defect-sample counts: 1, 2, 4, 6, and 8.
- DAGM2007 defect-sample counts: 1, 2, 4, 6, 8, 10, 20, 30, and 40.
- AttenCGAN classification training: 200 epochs, batch size 8, learning rate 0.001.
- CycleGAN training: learning rate 0.0002, 200 iterations/epochs in the extracted text, batch size 1, learning rate held for first 100 epochs then linearly decayed to zero for the next 100 epochs.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---|---:|---|
| Highest reported KolektorSDD small-sample setting | [[KolektorSDD]] / [[Defect classification]] | [[Accuracy]] | higher | MobileNet-V2, ResNet-50, VGG16, SDCNN | 98.53% | With 8 defect samples. |
| KolektorSDD two-sample setting | [[KolektorSDD]] / [[Defect classification]] | [[Accuracy]] | higher | MobileNet-V2, ResNet-50, VGG16 | 97.06% | Baselines reported as 78.41%, 79.41%, and 79.58%. |
| KolektorSDD one-sample setting | [[KolektorSDD]] / [[Defect classification]] | [[Accuracy]] | higher | MobileNet-V2, ResNet-50, VGG16 | 87.72% | Baselines reported as 62.00%, 64.45%, and 65.77%. |
| Highest reported DAGM2007 small-sample setting | [[DAGM2007]] classes 1-6 / [[Defect classification]] | [[Accuracy]] | higher | published SDC methods | 99.57% | Average over classes 1-6 with 40 defect samples. |
| DAGM2007 one-sample setting | [[DAGM2007]] classes 1-6 / [[Defect classification]] | [[Accuracy]] | higher | MobileNet-V2, ResNet-50, VGG16 | near 76% | Baselines described as near 60%. |
| GAN comparison | [[KolektorSDD]] / generated defect image quality | [[FID]] | lower | GAN, StarGAN | 122 minimum FID | GAN and StarGAN are reported as 232 and 175 in that comparison. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Accuracy]] | Surface defect classification | Percentage of correctly classified samples | Higher is better | yes | 98.53% on KolektorSDD and 99.57% average on DAGM2007 classes 1-6 in the headline settings. |
| [[FID]] | Generated defect image quality | Distance between generated and real image distributions in feature space | Lower is better | secondary | KolektorSDD minimum FID reported as 122 for AttenCGAN versus 232 for GAN and 175 for StarGAN. |

## ML / DL Extraction

### Task Formulation

- Input modality: industrial surface images.
- Output target: defect classification labels; generated pseudo defect images for augmentation.
- Supervision: supervised classification with few labeled defect samples, augmented by CycleGAN-generated pseudo defects.
- Objective: maintain defect classification accuracy as the number of real defect images decreases.

### Model And Training

- Model family: [[GAN]] and attention-based CNN classification.
- Architecture: CycleGAN generators/discriminators plus SDCNN with Inception V3 feature extraction, 1x1-convolution attention maps, bilinear attention pooling, and attention-guided augmentation.
- Losses: least-squares adversarial loss, cycle consistency loss, and classification loss implied by SDCNN training.
- Optimizer: not fully reported for every component in the extracted text.
- Hyperparameters: CycleGAN lambda 10, learning rate 0.0002, batch size 1; SDCNN learning rate 0.001, batch size 8, 200 epochs.
- Pretraining: SDCNN feature extraction uses an ImageNet-pretrained Inception V3 strategy transferred to surface defect datasets.
- Seeds: not reported.
- Compute: not reported.

### Data

- Datasets: [[KolektorSDD]] and [[DAGM2007]].
- Data source: public industrial surface defect benchmark datasets.
- Dataset size: KolektorSDD has 399 images with 50 visible-defect images; DAGM2007 has 1,150 images per type, with 1,000 defect-free and 150 defective images.
- Splits: exact train/test splits are not reported in the extracted text.
- Synthetic data: 200 pseudo defect samples are synthesized for each selected small-sample setting.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: randomly select small numbers of defect images, train AttenCGAN and baselines, and compare classification accuracy; compare generated-image quality with FID.
- Baselines: MobileNet-V2, ResNet-50, VGG16, SDCNN without generated images, GAN, StarGAN, and selected published SDC methods.
- Statistical tests: not reported.
- Failure cases: performance degrades when only one defect image is available; no-defect-sample settings are not supported.

## Dataset / Benchmark Details

- [[KolektorSDD]]: 399 images of defective electrical commutators; 50 images contain visible defects; source URL reported as `https://www.vicos.si/resources/kolektorsdd/`.
- [[DAGM2007]]: weakly supervised industrial optical inspection benchmark; ten image types, each with 1,000 defect-free and 150 defective images; classes 1-6 are used in this paper.
- DAGM2007 URL: `https://hci.iwr.uni-heidelberg.de/content/weaklysupervised-learning-industrial-optical-inspection`.
- Labels / annotations: defect classification labels are used; segmentation labels are not the focus of this paper.
- License: not reported.

## Limitations

- AttenCGAN still requires at least one defect sample and does not solve zero-shot defect classification.
- One-sample settings degrade sharply compared with two or more defect samples.
- Exact train/test split construction, random seeds, and compute settings are not reported in the extracted text.
- Attention-guided augmentation is identified as an area for improvement with stronger attention mechanisms.

## Reproducibility

- Code: not reported.
- Data: public benchmark datasets are used.
- Hyperparameters: several CycleGAN and SDCNN training hyperparameters are reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: standard image augmentation and SDCNN auto augmentation are reported, but exact split files are not.
- Artifact status: no code artifact reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Surface defect detection]]
- Methods: [[AttenCGAN]], [[GAN]], [[Data augmentation]]
- Datasets: [[KolektorSDD]], [[DAGM2007]]
- Benchmarks: [[KolektorSDD]], [[DAGM2007]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Accuracy]], [[FID]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]], [[Small-sample defect classification]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] | Shares dataset and method family | Both use KolektorSDD and DAGM2007 for GAN-based defect image augmentation under limited data. |
| [[2023 - EID-GAN Generative Adversarial Nets for Extremely Imbalanced Data Augmentation]] | Shares dataset and method family | Both use DAGM2007 to evaluate GAN-based augmentation for scarce or imbalanced defect data. |
| [[2023 - PreCaCycleGAN Perceptual Capsule Cyclic Generative Adversarial Network for Industrial Defective Sample Augmentation]] | Shares method family | Both use CycleGAN-style defect sample augmentation for industrial defect tasks. |

### Connection Rationale

- [[AttenCGAN]] is the proposed method and central contribution.
- [[KolektorSDD]] and [[DAGM2007]] are the evaluation datasets.
- [[Accuracy]] is the primary classification metric, while [[FID]] evaluates generated-image realism.
- [[Small-sample defect classification]] captures the target setting: maintaining classification performance with very few defect examples.

## Questions

- Which exact dataset splits and random seeds were used for each sample-count experiment?
- How much of the gain comes from synthetic defects versus attention-guided SDCNN augmentation?
- Does AttenCGAN create synthetic artifacts that a classifier can overfit to?
- Can the method be extended to zero-shot settings where no defect examples are available?
