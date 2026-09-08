---
title: "Defect-GAN: High-Fidelity Defect Synthesis for Automated Defect Inspection"
aliases:
  - "Defect-GAN"
paper_key: "sha256:1babf23e0b2b520e4f08ce2b39eac2d3f6b6f1c8572f02d30503b34d80ec22e3"
paper_type: research
year: 2021
venue: "WACV 2021"
authors:
  - "Gongjie Zhang"
  - "Kaiwen Cui"
  - "Tzu-Yi Hung"
  - "Shijian Lu"
status: processed
processed_at: 2026-05-20
topics:
  - defect synthesis
  - automated defect inspection
  - generative adversarial networks
  - data augmentation
tasks:
  - "[[Defect synthesis]]"
  - "[[Defect classification]]"
domains:
  - "[[Construction inspection]]"
  - "[[Industrial visual inspection]]"
datasets:
  - "[[CODEBRIM]]"
methods:
  - "[[GAN]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "Defect-GAN"
  - "spatial and categorical control"
  - "adaptive noise insertion"
  - "layer-wise composition"
metrics:
  - "[[FID]]"
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  FID: "Lower is better; used to compare the generated defect image distribution with real defect images."
  Accuracy: "Higher is better; used for CODEBRIM multi-label defect inspection networks trained with and without synthetic augmentation."
baselines:
  - "StackGAN++"
  - "Conditional StackGAN++"
  - "StyleGAN v2"
  - "StyleGAN v2 + DiffAug"
  - "CycleGAN"
  - "StarGAN"
  - "StarGAN + SPADE"
  - "ResNet34 without augmentation"
  - "DenseNet121 without augmentation"
doi: "not reported"
arxiv: "not reported"
related_papers:
  - "[[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]]"
  - "[[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Defect synthesis]]"
related_methods:
  - "[[GAN]]"
related_datasets: []
related_tasks:
  - "[[Defect classification]]"
concept_notes_created_or_updated:
  - "[[GAN]]"
  - "[[Defect synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Defect classification]]"
  - "[[Construction inspection]]"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2021 - Zhang - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Zhang - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Zhang - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Zhang - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection.txt"
artifact_status: "processed"
tags:
  - paper
  - gan
  - defect-synthesis
---

# Defect-GAN: High-Fidelity Defect Synthesis for Automated Defect Inspection

## Summary

- Defect-GAN generates realistic and diverse defect samples from normal surface images to improve automated defect inspection training.
- It learns paired defacement and restoration processes and uses a compositional layer-based architecture to preserve background appearance.
- It provides spatial and categorical control over generated defects and introduces stochastic variation through adaptive noise insertion.
- The paper evaluates synthesis and augmentation on [[CODEBRIM]], a concrete-bridge defect dataset with crack, spallation, efflorescence, exposed-bar, corrosion, and normal classes.

## Contribution

- Claimed: Defect-GAN improves defect synthesis fidelity, diversity, transferability, and usefulness for downstream inspection.
- Shown: Defect-GAN reports lower FID than compared synthesis methods and improves classification accuracy for ResNet34 and DenseNet121 on CODEBRIM.
- Inferred: Background-preserving layer composition is central because it lets defects transfer to unseen normal samples.

## Method

- Uses normal samples as inputs.
- Defacement branch synthesizes defects; restoration branch removes defects to generate normal images.
- Spatial and categorical control maps specify where and what kind of defect to generate.
- Adaptive noise insertion models stochastic defect variation.
- Layer-wise composition treats defects as foreground over normal backgrounds.
- Generator training uses adversarial, category-classification, reconstruction, spatial-distribution cycle-consistency, and region-constraint losses.
- The inspection-stage classifier mixes generated defect samples with original training data and adds a source classifier with a gradient reversal layer to reduce the real/synthetic feature-domain gap.

## Data And Training Details

| Component | Source-backed detail |
|---|---|
| Dataset | [[CODEBRIM]] concrete-bridge defect imagery with six mutually non-exclusive labels: crack, spallation, efflorescence, exposed bars, corrosion, and normal. |
| Defect-GAN inputs | All classification images plus 50,000 normal patches cropped from original full-resolution images. |
| Synthesis image size | 128 x 128 during Defect-GAN training. |
| Synthesis optimizer | Adam with beta1 = 0.5, beta2 = 0.999, learning rate reduced from 2e-4 to 1e-6. |
| Synthesis schedule | Batch size 4, 500,000 iterations, one generator update per five discriminator updates. |
| Synthesis compute | About one day on a single NVIDIA 2080Ti GPU. |
| Inspection augmentation | 50,000 synthesized defect samples mixed with the original training data; restored normal samples are also included to avoid data imbalance. |
| Inspection training | Images resized to 224 x 224; SGD learning rate 1e-3; batch size 16; best model selected on validation set and reported on test set. |

## Evidence

### Performance Metrics

| Metric | Direction | Evaluation context | Reported values |
|---|---|---|
| [[FID]] | Lower is better | Defect synthesis fidelity on [[CODEBRIM]] | Defect-GAN reports 65.6, compared with StarGAN + SPADE at 103.0 and the ideal split-real-data estimate at 25.0. |
| [[Accuracy]] | Higher is better | Downstream multi-label defect inspection on [[CODEBRIM]] | ResNet34 improves from 70.25% to 75.48% with Defect-GAN augmentation; DenseNet121 improves from 70.77% to 75.79%. |

### Synthesis Results

| Method | FID |
|---|---:|
| StackGAN++ | 111.1 |
| Conditional StackGAN++ | 132.1 |
| StyleGAN v2 | 148.2 |
| StyleGAN v2 + DiffAug | 142.4 |
| CycleGAN | 94.5 |
| StarGAN | 295.1 |
| StarGAN + SPADE | 103.0 |
| Defect-GAN | 65.6 |
| Ideal defect synthesizer | 25.0 |

### Ablation Results

| Design setting | FID |
|---|---:|
| StarGAN-style base without SCC, ANI, LWC, or SC | 295.1 |
| + spatial and categorical control | 103.0 |
| + adaptive noise insertion without layer-wise composition | 99.7 |
| + layer-wise composition without adaptive noise insertion | 76.8 |
| + spatial constraints | 69.5 |
| Full Defect-GAN | 65.6 |

### Inspection Results

| Network | Augmentation method | Accuracy |
|---|---|---:|
| ResNet34 | None | 70.25% |
| ResNet34 | Conditional StackGAN++ | 62.59% |
| ResNet34 | StarGAN + SPADE | 71.90% |
| ResNet34 | Defect-GAN | 75.48% |
| DenseNet121 | None | 70.77% |
| DenseNet121 | Conditional StackGAN++ | 58.68% |
| DenseNet121 | StarGAN + SPADE | 72.61% |
| DenseNet121 | Defect-GAN | 75.79% |

### Interpretation

- Conditional StackGAN++ augmentation reduces inspection accuracy, which the paper attributes to unrealistic defect samples.
- StarGAN + SPADE gives a smaller gain than Defect-GAN because it can generate realistic samples on training backgrounds but fails to transfer learned defects to unseen normal backgrounds.
- Defect-GAN's layer-wise composition is the largest ablated contributor after adding spatial and categorical control.

## Limitations

- Evaluation centers on [[CODEBRIM]] concrete-bridge imagery; transfer to industrial sensor modalities beyond RGB image patches is not shown.
- The method assumes access to many normal samples and at least enough defect images to train the unpaired translation setup.
- The source reports categorical and spatial control qualitatively, but downstream inspection is reported with accuracy only.
- DOI and public code link were not present in the extracted metadata.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]]
- Methods: [[GAN]], [[Defect synthesis]], [[Synthetic data generation]]
- Datasets: [[CODEBRIM]]
- Domains: [[Construction inspection]], [[Industrial visual inspection]], [[Surface defect detection]]
- Metrics: [[FID]], [[Accuracy]]
- Concepts: [[Domain gap]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] | Shares method | Both use GAN-based synthetic defect imagery for scarce visual inspection data; this paper focuses on controllable defect synthesis and downstream classification accuracy. |
| [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] | Shares method | Both use GAN variants for defect imagery; this paper centers on Defect-GAN synthesis while Upadhyay et al. also combine DCGAN with deblurring and U-Net segmentation. |
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Contrasts with | Both generate synthetic training data, but this paper uses image-generation GANs while Schmedemann et al. use procedural 3D rendering and domain randomization. |

### Backlinks Updated

- [[GAN]] links this paper as the central GAN-based defect synthesis example.
- [[Defect synthesis]] links this paper as the high-fidelity controllable synthesis example.
- [[Synthetic data generation]] links this paper as a GAN-based augmentation example.
- [[Defect classification]] links this paper for downstream classification evaluation.
- [[Construction inspection]] stages this paper as the current construction-oriented inspection example.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[GAN]] | Created | Processed paper notes |
| [[Defect synthesis]] | Created | Processed paper notes |
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[Defect classification]] | Created | Processed paper notes |

## Questions

- Is Defect-GAN code or trained weights available?
- How well does categorical control scale to many fine-grained industrial defect types?
- Can the method synthesize defects for depth, CT, or laser line scan modalities?
