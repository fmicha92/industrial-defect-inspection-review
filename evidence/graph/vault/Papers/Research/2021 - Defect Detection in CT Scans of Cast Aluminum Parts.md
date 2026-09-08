---
title: "Defect detection in CT scans of cast aluminum parts: A machine vision perspective"
aliases:
  - "Defect detection in CT scans of cast aluminum parts"
paper_key: "sha256:d156e2f050ef05c18b83269be18f52cde19796faf0e023c3d04bc6f37d330b99"
paper_type: research
year: 2021
venue: "Neurocomputing"
authors:
  - "Patrick Fuchs"
  - "Thorben Kröger"
  - "Christoph S. Garbe"
status: processed
processed_at: 2026-05-20
topics:
  - computed tomography
  - cast aluminum inspection
  - simulated training data
  - semantic segmentation
tasks:
  - "[[Defect segmentation]]"
  - "3D CT defect segmentation"
  - "pore and cavity detection"
domains:
  - "[[Metal inspection]]"
  - "[[Nondestructive testing]]"
datasets:
  - "[[Simulated CT defect scans]]"
  - "[[Hand-labeled real CT defect scans]]"
methods:
  - "[[Simulation-based data augmentation]]"
  - "[[Synthetic data generation]]"
  - "3D convolutional segmentation network"
  - "[[U-Net]]"
  - refinement stage
metrics:
  - "[[Probability of detection]]"
  - "[[IoU]]"
primary_metric: "[[IoU]]"
metric_definitions:
  - "Probability of detection estimates how likely defects of a given equivalent sphere diameter are found with a given confidence."
  - "IoU measures voxel-level overlap as TP / (TP + FP + FN)."
baselines:
  - "filter-based ADR candidate selection"
  - "voxel random forest classifier"
  - "deep two-stage 3D segmentation model"
doi: "not reported"
arxiv: "not reported"
related_papers:
  - "[[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Simulation-based data augmentation]]"
  - "[[Domain gap]]"
  - "[[Transfer learning]]"
related_methods:
  - "[[U-Net]]"
related_datasets: []
related_tasks:
  - "[[Defect segmentation]]"
concept_notes_created_or_updated:
  - "[[Synthetic data generation]]"
  - "[[Simulation-based data augmentation]]"
  - "[[Domain gap]]"
  - "[[Nondestructive testing]]"
  - "[[Defect segmentation]]"
  - "[[U-Net]]"
url: "https://doi.org/10.1016/j.neucom.2021.04.094"
pdf: "paper-inbox/10_processed/Other/2021 - Fuchs - Defect detection in CT scans of cast aluminum parts A machine vision perspective.pdf"
source_file: "paper-inbox/10_processed/Other/2021 - Fuchs - Defect detection in CT scans of cast aluminum parts A machine vision perspective.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Fuchs - Defect detection in CT scans of cast aluminum parts A machine vision perspective.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Fuchs - Defect detection in CT scans of cast aluminum parts A machine vision perspective.txt"
artifact_status: "processed"
tags:
  - paper
  - computed-tomography
  - semantic-segmentation
  - synthetic-data
---

# Defect detection in CT scans of cast aluminum parts

## Summary

- The paper addresses defect detection in industrial CT scans of cast aluminum parts under tight in-line inspection constraints.
- It trains deep segmentation models only on realistically simulated CT data with precise per-voxel ground truth.
- Evaluation compares traditional algorithms and the trained segmentation network on simulated and real validation data using probability of detection and IoU.

## Contribution

- Claimed: Realistically simulated CT scans can provide enough labeled data to train a 3D defect segmentation network that transfers to real CT scans.
- Shown: Learning-based methods trained solely on simulated data outperform a filter-based approach, and deep learning is more robust to noise and artifact variation.
- Inferred: The simulation pipeline is useful because obtaining precise labels in real 3D CT data requires expert work and high-quality scans.

## Method

- Generate realistic simulated CT scans with known defect geometry and precise voxel labels.
- Train a two-stage segmentation model: a U-Net-like 3D encoder-decoder for high recall and a refinement stage for high precision.
- Compare against filter-based and traditional machine learning approaches.
- Evaluate on simulated validation scans and real lower-quality CT scans with high-quality hand-labeled reference ground truth.
- The simulation pipeline procedurally creates virtual die-cast meshes and defect meshes, simulates realistic CT projections with ray casting, reconstructs CT scans, and derives per-voxel ground truth from the known defect meshes.
- Simulated defects include gas pores, shrinkage cavities, and solidification cracks, with model diameters ranging from 0.2 mm to 3 mm.
- The training set contains 675 simulated CT scans from 25 virtual die casts scanned with 27 configurations each; the simulated validation set contains 54 scans from two separate virtual die casts.
- The deep model uses fully 3D convolutions, residual layers, skip connections, deep supervision, and a final refinement stage.

## Evidence

| Evidence | Reported detail |
|---|---|
| Simulated training scale | 27 million samples from simulated CT scans |
| Patch size | 128^3 voxel patches |
| Robustness | Filter-based method drops by almost 35% between best and worst simulated scan quality; traditional ML drops about 6%; deep learning drops about 2% |
| In-line speed | NVIDIA TITAN RTX processes a 1000^3 voxel volume in about 8 minutes with 320^3 voxel blocks |
| Scan-time robustness | Machine learning methods maintain better IoU as simulated scan time drops from 3600 s toward 36 s |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Probability of detection]] | instance-level CT defect detection | probability that a defect of a given equivalent sphere diameter is found at a given confidence | higher | no | Evaluated on simulated test specimens and used because it is meaningful to domain experts. |
| [[IoU]] | voxel-level CT defect segmentation | TP / (TP + FP + FN), ignoring true negatives in highly imbalanced volumes | higher | yes | Reported for simulated validation scans and two real CT scans. |

### Benchmark Results

| Method | Simulated IoU | Real-data IoU | Notes |
|---|---:|---:|---|
| Filter-based ADR candidate selection | 48.5% mean; 82.1% best / 47.2% worst quality | 40.7%; 29.9% | Strongly affected by image quality and noise. |
| Traditional voxel random forest | 82.6% mean; 86.9% best / 81.0% worst quality | 56.6%; 43.5% | Uses eight hand-crafted CT features and a 128-tree random forest. |
| Deep two-stage 3D segmentation model | 85.9% mean; 86.6% best / 85.3% worst quality | 60.7%; 47.3% | Most robust to scan-quality variation among the evaluated methods. |

- Noise is the artifact type with the largest performance impact.
- Machine-learning methods are more robust to noise and beam-hardening artifacts than the filter-based method.
- The deep model is trained only on simulated CT scans and still outperforms the filter-based method on real lower-quality CT scans.
- Reducing exposure time from 3600 s toward 36 s degrades the filter-based method faster than the machine-learning methods.
- Fine-tuning with six additional simulated low-quality CT scans adapts the deep model to blurrier in-line CT scans with larger focal spots.

### Training And Data Details

- Simulated scan size: 1000 x 1000 x 1000 voxels with voxel size 110 micrometers.
- Virtual material: EN AW-2014 aluminum alloy with copper and iron admixtures.
- CT setup: 225 kV source at 1 mA, 225 micrometer x 225 micrometer focal spot, 1000 x 1000 pixel detector, 200 micrometer detector pixel size, 1000 mm source-detector distance, and 450 mm source-object distance.
- Artifact variation: exposure time controls noise, filter thickness controls beam-hardening/cupping, and detector calibration controls ring artifacts; scatter is simulated with Monte Carlo.
- Deep model training: 128^3 voxel patches, two patches at a time, 150,000 iterations, Adam optimizer, initial learning rate 1e-4 with inverse time decay, and about three days to convergence.
- Losses: dice loss for final output and generalized dice loss with higher false-negative weight for deep-supervised intermediate outputs.
- Real validation data: two cast aluminum parts scanned once at high quality for labeling and again at normal lower quality for evaluation; normal scans use 1500 projections and 15 minute scan time.

## Limitations

- The paper notes possible causes of simulated-to-real performance drops: missing real-world aspects in synthetic data or imprecise real labels.
- The method struggles when CT acquisition changes produce blurriness outside its training distribution.
- Extending to other manufacturing processes requires new procedural mesh generation and defect types.
- Real labels remain ambiguous because experts disagree about whether structural loosenings, tiny pores, and boundary voxels should be labeled as defects.
- The method currently segments defects but does not classify them into gas pores, shrinkage cavities, or solidification cracks.
- The paper reports qualitative real-world applications but only two labeled real CT scans for quantitative real-data IoU.

## Reproducibility

- Code: not reported.
- Data: simulated data generator details are described; public release of simulated or real CT data is not reported.
- Training data: 675 simulated scans and approximately 500,000 simulated defects.
- Validation data: 54 simulated scans and two real cast aluminum parts with transferred high-quality labels.
- Hyperparameters: 128^3 patches, 150,000 iterations, Adam, initial learning rate 1e-4 with inverse time decay; fine-tuning uses 25,000 iterations at learning rate 1e-5.
- Hardware: NVIDIA TITAN RTX is used for the reported 1000^3 voxel inference timing.
- Environment: VGinLINE automates CT reconstruction and ground-truth computation; VGSTUDIO MAX is used to align high-quality and normal real scans.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]]
- Methods: [[Simulation-based data augmentation]], [[U-Net]], [[Synthetic data generation]]
- Datasets: [[Simulated CT defect scans]], [[Hand-labeled real CT defect scans]]
- Domains: [[Metal inspection]], [[Nondestructive testing]], [[Industrial visual inspection]]
- Metrics: [[Probability of detection]], [[IoU]]
- Concepts: [[Domain gap]], [[Transfer learning]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Shares method | Both train defect detectors with synthetic data, but this paper uses simulated CT volumes while Schmedemann et al. use rendered surface inspection images. |
| [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] | Shares task | Both perform defect segmentation with U-Net-style models, but this paper works on 3D CT volumes and the aircraft paper works on borescope blade images. |

### Backlinks Updated

- [[Synthetic data generation]] links this paper as a simulated CT training-data example.
- [[Simulation-based data augmentation]] links this paper as a CT simulation example.
- [[Defect segmentation]] links this paper as a 3D voxel segmentation example.
- [[U-Net]] links this paper as a 3D U-Net-like segmentation example.
- [[Domain gap]] links this paper for simulated-to-real CT transfer.
- [[Nondestructive testing]] stages this paper as the current industrial CT example.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[Simulation-based data augmentation]] | Created | Processed paper notes |
| [[Domain gap]] | Created | Paper limitations and linked notes |
| [[Defect segmentation]] | Created | Processed paper notes |
| [[U-Net]] | Created | Processed paper notes |

## Questions

- Are the simulated CT generator and trained model available?
- Which artifact types are most important to simulate for transfer to a new CT system?
- How does the method perform on cracks versus pores and cavities?
