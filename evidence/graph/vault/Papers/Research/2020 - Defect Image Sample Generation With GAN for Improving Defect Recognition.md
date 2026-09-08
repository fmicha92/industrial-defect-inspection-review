---
title: "Defect Image Sample Generation With GAN for Improving Defect Recognition"
aliases:
  - "Defect Image Sample Generation With GAN for Improving Defect Recognition"
paper_key: "doi:10.1109/tase.2020.2967415"
paper_type: research
year: 2020
venue: "IEEE Transactions on Automation Science and Engineering"
authors:
  - "Shuanlong Niu"
  - "Bin Li"
  - "Xinggang Wang"
  - "Hui Lin"
status: processed
processed_at: 2026-05-23
topics:
  - "defect image generation"
  - "GAN augmentation"
  - "defect recognition"
tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Commutator Cylinder Surface Defect Dataset]]"
methods:
  - "[[SDGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
model_family:
  - "[[GAN]]"
  - "[[Generative Models]]"
architectures:
  - "[[SDGAN]]"
metrics:
  - "[[FID]]"
  - "[[Error rate]]"
  - "[[Relative improvement]]"
primary_metric: "[[Error rate]]"
metric_definitions:
  - "FID: distance between real and generated image distributions; lower is better."
  - "Error rate: recognition error for anomaly recognition or defect classification."
  - "Relative improvement: percentage improvement compared with the CNN-only baseline."
baselines:
  - "CNN-only"
  - "WGAN augmentation"
  - "D2GAN augmentation"
  - "CycleGAN augmentation"
benchmarks:
  - "[[Commutator Cylinder Surface Defect Dataset]]"
code: "not reported"
data: "not reported"
doi: "10.1109/tase.2020.2967415"
arxiv: "not reported"
url: "https://doi.org/10.1109/TASE.2020.2967415"
pdf: "paper-inbox/10_processed/Research/2020 - Niu - Defect Image Sample Generation With GAN for Improving Defect Recognition.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[SDGAN]]"
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[Commutator Cylinder Surface Defect Dataset]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
source_file: "paper-inbox/10_processed/Research/2020 - Niu - Defect Image Sample Generation With GAN for Improving Defect Recognition.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Niu - Defect Image Sample Generation With GAN for Improving Defect Recognition.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Niu - Defect Image Sample Generation With GAN for Improving Defect Recognition.txt"
artifact_status: "code and public data availability not reported"
tags:
  - paper
---
# Defect Image Sample Generation With GAN for Improving Defect Recognition

## Summary

Niu et al. propose [[SDGAN]], a surface-defect generation adversarial network that uses abundant defect-free industrial images plus scarce defect images to synthesize defect samples for recognition training. The method is evaluated on commutator cylinder surface defect imagery in two settings: CCSD-NL for binary anomaly recognition and CCSD-L for labeled defect classification.

The main reported outcome is that VGG16 recognition models trained with SDGAN-augmented data outperform CNN-only and other GAN-augmentation baselines. The paper reports 1.77% error rate and 49.43% relative improvement for anomaly recognition on CCSD-NL, and 0.74% error rate and 57.47% relative improvement for defect classification on CCSD-L.

## Paper Type

- Type: research.
- Why: The paper contributes a generative method and evaluates it as data augmentation for industrial defect recognition.

## Problem

- Task: [[Defect classification]] and binary surface-defect anomaly recognition.
- Setting: industrial visual inspection with scarce labeled defect images and many defect-free images.
- Inputs: defect-free commutator cylinder surface images and a small set of defect images.
- Outputs: generated defect images, binary defect/non-defect predictions, and four-class defect classifications.
- Motivation: deep defect recognition needs sufficient labeled defect images, but production lines often have few defect samples and high labeling cost.
- Assumptions: defect-free regions in defect and defect-free images share common features, so generating defects on defect-free images can exploit abundant defect-free production imagery.

## Contribution

- Claimed: [[SDGAN]] generates defect images with better quality and diversity than WGAN, D2GAN, and CycleGAN for this industrial setting.
- Shown: SDGAN-augmented data reduces VGG16 recognition error on both binary anomaly recognition and four-class defect classification.
- Shown: SDGAN-trained classifiers are more robust to poor or uneven lighting than the CNN-only baseline.

## Method

SDGAN contains two generators and four discriminators. Generator G maps a defect-free image to a generated defect image, and generator F maps a defect image to a generated defect-free image. Two adversarial losses support image quality and diversity, and cycle consistency helps preserve the common non-defective image structure while adding defect features.

The pipeline has three stages: defect generation, quality evaluation, and defect recognition. Generated images are mixed with real images to train VGG16 recognition models. Anomaly recognition uses two output classes, defect-free and defect; defect classification uses five output classes, one good class plus four defect classes.

## Evidence

### Experimental Setup

- Dataset: [[Commutator Cylinder Surface Defect Dataset]].
- CCSD-NL: unlabeled binary setting, with all defect samples grouped as defective and defect-free samples as the other class.
- CCSD-L: labeled setting with defect-free, thread-line, brushing, tin-residue, and wound classes.
- Generation baselines: WGAN, D2GAN, and CycleGAN.
- Recognition model: VGG16 with ADAM.
- Defect classification training: 1000 epochs.
- Quality metric: [[FID]].

### Main Results

| Task | Dataset | Best augmentation | Error rate | Relative improvement | Notes |
|---|---|---|---:|---:|---|
| Anomaly recognition | CCSD-NL | SDGAN | 1.77% | 49.43% | Binary defect-free vs. defective recognition. |
| Defect classification | CCSD-L | SDGAN | 0.74% | 57.47% | Four defect types plus good images; SDGAN has lowest reported error rate. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Error rate]] | Anomaly recognition and defect classification | Recognition error percentage on the test set | Lower is better | yes | SDGAN: 1.77% on CCSD-NL and 0.74% on CCSD-L. |
| [[Relative improvement]] | Comparison with CNN-only baseline | Relative IMP percentage | Higher is better | no | SDGAN: 49.43% on CCSD-NL and 57.47% on CCSD-L. |
| [[FID]] | Generated image quality and diversity | Distance between real and generated image feature distributions | Lower is better | no | Exact table values are not available in the extracted text; the prose states SDGAN is lowest for all defects except thread-line. |

## ML / DL Extraction

### Task Formulation

- Input modality: RGB commutator cylinder surface imagery.
- Output target: generated defect images, binary anomaly labels, and defect class labels.
- Supervision: defect-free and defect images are used for generation; labeled classes are used for defect classification.
- Objective: improve recognition by augmenting scarce defect data with generated defect images.

### Model And Training

- Model family: [[GAN]], [[Generative Models]].
- Architecture: [[SDGAN]] for generation; VGG16 for recognition.
- Losses: D2 adversarial loss and cycle consistency loss are central to SDGAN.
- Optimizer: ADAM for SDGAN/CycleGAN and VGG16 recognition models.
- Batch size: SDGAN/CycleGAN batch size 4; WGAN/D2GAN batch size 32.
- Training epochs: WGAN and D2GAN use 2000 epochs; defect classification model uses 1000 epochs.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Dataset: [[Commutator Cylinder Surface Defect Dataset]].
- Data source: commutator cylinder surface images from industrial production.
- Labels / annotations: CCSD-NL has defect-free versus defective labels; CCSD-L has good, thread-line, brushing, tin-residue, and wound classes.
- Splits: exact split counts are not preserved in the extracted text tables.
- Augmentation: SDGAN, WGAN, D2GAN, and CycleGAN generate additional defect images for comparison.
- Synthetic data: generated defect images are mixed with real images for recognition training.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: compare generated images by FID and compare VGG16 recognition models trained on data augmented by different generation methods.
- Used performance metrics: [[FID]], [[Error rate]], [[Relative improvement]].
- Baselines: CNN-only, WGAN, D2GAN, CycleGAN.
- Statistical tests: not reported.
- Failure cases: WGAN and D2GAN sometimes fail to generate wound defects and produce images resembling defect-free samples; CNN-only can fail on all four defect types.

## Dataset / Benchmark Details

- Source: industrial commutator cylinder surface imagery.
- Collection: commutator cylinder defects appear during the production process.
- CCSD-NL: binary defect-free/defective dataset without specific defect-class labels.
- CCSD-L: labeled data with good, thread-line, brushing, tin-residue, and wound classes.
- Modalities: visual surface images.
- License: not reported.
- Public availability: not reported.
- Bias / coverage: covers commutator cylinder surface defects, not all industrial surface-defect domains.

## Limitations

- Exact FID table values, dataset split counts, and generated-data counts are not preserved in the extracted text.
- Public data availability, source code, and license terms are not reported.
- Evaluation uses commutator cylinder surface imagery, so transfer to other surface materials or defect processes is not established.
- SDGAN is used offline; training time is described as relatively long.

## Reproducibility

- Code: not reported.
- Data: not reported.
- Hyperparameters: partial GAN batch sizes and epoch counts are reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Surface defect detection]]
- Methods: [[SDGAN]], [[GAN]], [[Data augmentation]]
- Datasets: [[Commutator Cylinder Surface Defect Dataset]]
- Benchmarks: [[Commutator Cylinder Surface Defect Dataset]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[FID]], [[Error rate]], [[Relative improvement]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Shares Method

- [[SDGAN]]: central method for generating defect images from defect-free images.
- [[GAN]]: broader generative model family.
- [[Data augmentation]]: SDGAN outputs are used to expand recognition training data.

### Shares Dataset

- [[Commutator Cylinder Surface Defect Dataset]]: source imagery for both generation and recognition experiments.

### Follow-up Reading

- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]]: another GAN-based defect synthesis paper that reports FID and downstream recognition effects.

## Questions

- What are the exact CCSD-NL/CCSD-L split counts and FID table values in the formatted PDF tables?
- Are the commutator cylinder datasets or SDGAN implementation publicly available?
- How well does SDGAN transfer to defect types without shared defect-free surface structure?
