---
title: "Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection"
aliases:
  - "Procedural synthetic training data generation for AI-based defect detection"
paper_key: "doi:10.1016/j.procir.2022.05.115"
paper_type: research
year: 2022
venue: "Procedia CIRP 107; 55th CIRP Conference on Manufacturing Systems"
authors:
  - "Ole Schmedemann"
  - "Melvin Baaß"
  - "Daniel Schoepflin"
  - "Thorsten Schüppstuhl"
status: processed
processed_at: 2026-05-20
topics:
  - synthetic training data
  - surface inspection
  - industrial quality control
  - domain randomization
  - physically based rendering
tasks:
  - defect detection
  - image classification
  - object segmentation
domains:
  - "[[Automotive manufacturing]]"
  - "[[Metal inspection]]"
  - "[[Industrial visual inspection]]"
application_area: "Endoscopic inspection of turbocharger housing cavities"
datasets:
  - "[[Synthetic turbocharger housing defect dataset]]"
  - "[[Real-world endoscopic defect image training dataset]]"
  - "[[Real-world endoscopic defect image test dataset]]"
dataset_sizes:
  - "4,906 synthetic images"
  - "110 real-world training images"
  - "110 real-world test images"
splits:
  - "Synthetic dataset split 80/20 into training and validation"
  - "Real-world training dataset split equally into training and validation"
modalities:
  - image
methods:
  - domain randomization
  - physically based rendering
  - procedural textures
  - 3D defect modeling
  - transfer learning
model_family:
  - convolutional neural network
architectures:
  - "18-layer ResNet"
losses:
  - "not reported"
training_regime: "ImageNet-pretrained ResNet; synthetic pretraining followed by real-world fine-tuning, compared with real-world-only training"
augmentation:
  - "randomized defect position, orientation, size, and shape"
  - "randomized illumination position, orientation, intensity, spectral distribution, and shape"
  - "randomized camera position and orientation"
  - "randomized texture roughness, base color, and normal map"
synthetic_data: "Procedurally generated images from Blender/Cycles/BlenderProc using 3D defect tools, procedural textures, physically based rendering, and domain randomization"
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
  - "[[Specificity]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "accuracy: classification correctness percentage; higher is better"
  - "recall: percentage reported by the paper; higher is better"
  - "specificity: percentage reported by the paper; higher is better"
baselines:
  - "18-layer ResNet trained directly on the real-world training dataset without synthetic pretraining"
benchmarks:
  - "Turbocharger housing endoscopic blowhole classification use case"
evaluation_protocol: "Select best model by validation accuracy, then evaluate on the real-world test dataset"
parameters: "not reported"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.1016/j.procir.2022.05.115"
pdf: "paper-inbox/10_processed/Other/2022 - Schmedemann - Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection.pdf"
code: "not reported"
data: "not reported"
doi: "10.1016/j.procir.2022.05.115"
arxiv: "not applicable"
related_papers:
  - "[[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]]"
  - "[[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]"
  - "[[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Domain gap]]"
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
  - "[[Transfer learning]]"
related_methods:
  - "[[Domain randomization]]"
  - "[[Physically based rendering]]"
  - "[[Procedural generation]]"
related_datasets:
  - "[[ImageNet]]"
related_tasks:
  - "[[Defect classification]]"
concept_notes_created_or_updated:
  - "[[Synthetic data generation]]"
  - "[[Domain randomization]]"
  - "[[Physically based rendering]]"
  - "[[Procedural generation]]"
  - "[[Domain gap]]"
  - "[[Transfer learning]]"
  - "[[Industrial visual inspection]]"
source_file: "paper-inbox/10_processed/Other/2022 - Schmedemann - Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Schmedemann - Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Schmedemann - Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection.txt"
artifact_status: "processed"
tags:
  - paper
  - synthetic-data
  - defect-detection
---

# Procedural synthetic training data generation for AI-based defect detection in industrial surface inspection

## Summary

- Schmedemann et al. propose a procedural training data generator for industrial surface defect detection that renders 3D object models with generated 3D defects, procedural textures, physically based rendering, and domain randomization.
- The paper demonstrates the generator on endoscopic inspection of turbocharger housing cavities, focusing on blowhole defects in cast iron surfaces.
- In the reported experiment, an ImageNet-pretrained 18-layer ResNet trained with synthetic pretraining and real-world fine-tuning outperformed the same architecture trained only on the small real-world dataset.

## Paper Type

- Type: research
- Why: The paper proposes and implements a new synthetic data generation pipeline, then evaluates it experimentally on an industrial defect detection use case.

## Problem

- Tasks: Detect surface defects in industrial visual inspection images.
- Setting: Automated optical inspection for industrial quality control, with a demonstration on endoscopic turbocharger housing inspection.
- Inputs: Rendered synthetic images and real-world endoscopic images of defective and defect-free surfaces.
- Outputs: Defective versus defect-free classification in the reported ResNet experiment; the generator also outputs segmentation maps that can support segmentation and object detection tasks.
- Motivation: Defective samples are rare, expensive to collect, biased toward observed defect types, and laborious to annotate manually.
- Assumptions: A 3D model of the inspected object is available, procedural textures can approximate the relevant material appearance, and randomization intervals can be chosen for defects, camera, illumination, and textures.

## Contribution

- Claimed: A procedural synthetic data generation pipeline for CNN-assisted defect detection using 3D object models, 3D defect tools, procedural textures, physically based rendering, and extensive domain randomization.
- Shown: On a turbocharger housing blowhole classification use case, synthetic pretraining followed by real-world fine-tuning improved reported test accuracy, recall, and specificity over real-world-only training.
- Inferred: The approach is most immediately useful when CAD/3D object models are available and defect geometry can be represented with defect tools; this follows from the pipeline requirements described by the authors.

## Method

- Core idea: Generate synthetic inspection images by modifying a 3D object mesh with randomized 3D defect tools, rendering the result under randomized texture, illumination, and camera settings, and exporting images plus segmentation maps.
- Architecture / algorithm: Training data generator implemented in Blender with Python scripting, Cycles for physically based rendering, and BlenderProc for segmentation maps.
- Objective / loss: not reported.
- Optimization: Model training used SGD in the reported experiment.
- Training data: 4,906 synthetic images, plus two real-world datasets of 110 images each for training and testing.
- Data pipeline: Choose object model and procedural textures; create defects using Boolean mesh operations with negative defect tools; randomize defect, camera, illumination, and texture parameters; render images and segmentation maps; filter generated images by visible defect size.
- Augmentation / synthesis: Synthetic defects and scene parameters are randomized instead of using ordinary image-space augmentation alone.
- Inference: Best model by validation accuracy was evaluated on the real-world test dataset.
- Complexity / deployment constraints: Requires a 3D model, procedural material setup, defect tool modeling, and randomization interval selection; compute and runtime are not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: Endoscopic RGB-like inspection images.
- Output target: Defective or defect-free class in the reported experiment; generated segmentation maps also provide pixel-level defect labels.
- Supervision: Supervised image classification, with synthetic labels generated automatically and real-world labels implied but annotation details not reported.
- Objective: Improve defect detection when few real-world defect images are available.

### Model And Training

- Model family: Convolutional neural network.
- Architecture: 18-layer ResNet pretrained on ImageNet.
- Parameters: not reported.
- Pretraining: ImageNet pretraining; in one experiment, additional pretraining on synthetic data.
- Fine-tuning: Synthetic-pretrained model was fine-tuned on the real-world training dataset.
- Losses: not reported.
- Optimizer: SGD.
- Hyperparameters: Synthetic pretraining used learning rate 1e-4, batch size 64, and 45 epochs. Hyperparameter search considered learning rates 1e-2, 1e-3, and 1e-4 with batch sizes 16, 32, and 64. Training ran for 25 epochs in both real-world experiments.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: Synthetic turbocharger housing dataset; real-world endoscopic training dataset; real-world endoscopic test dataset.
- Data source: Synthetic images from the proposed generator and real-world endoscopic images of turbocharger housing cavities.
- Dataset size: 4,906 synthetic images; 110 real-world training images; 110 real-world test images.
- Labels / annotations: Synthetic labels and segmentation maps generated by the pipeline; real-world label process not reported.
- Splits: Synthetic data split 80/20 into train/validation; real-world training data split equally into train/validation; separate real-world test dataset of 110 images.
- Preprocessing: Synthetic images with defects larger than 50 px were assigned to the defective class; images without visible defects were defect-free; images with very small defects were excluded.
- Augmentation: Domain randomization over defects, illumination, camera, and texture.
- Synthetic data: 137 manually chosen inspection poses, 100 defects per part, 822 images per part, repeated 6 times before filtering.
- Leakage checks: not reported.
- License: Paper is open access under CC BY-NC-ND 4.0; dataset license not reported.

### Evaluation

- Protocol: Select the best network using validation accuracy, then evaluate on the real-world test dataset.
- Used performance metrics: accuracy, recall, specificity.
- Primary metric: accuracy.
- Metric definitions: not formally defined in the paper; all are reported as percentages and higher is better.
- Metric direction / units: percentage, higher is better.
- Baselines: Same 18-layer ResNet trained directly on the real-world training dataset without synthetic pretraining.
- Benchmarks: Turbocharger housing blowhole inspection use case.
- Statistical tests: not reported.
- Failure cases: not reported.

## Evidence

### Experimental Setup

- Datasets: 4,906 synthetic images, 110 real-world training images, and 110 real-world test images.
- Splits: Synthetic 80/20 train/validation; real-world train/validation split equally; separate real-world test set.
- Baselines: Real-world-only ResNet training.
- Used performance metrics: accuracy, recall, specificity.
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Synthetic pretraining plus real-world fine-tuning improved classification | Real-world turbocharger housing test set | Accuracy | higher | 93.6% | 98.2% | Best model selected by validation accuracy |
| Synthetic pretraining plus real-world fine-tuning improved recall | Real-world turbocharger housing test set | Recall | higher | 94.2% | 96.2% | Definition not reported |
| Synthetic pretraining plus real-world fine-tuning improved specificity | Real-world turbocharger housing test set | Specificity | higher | 93.1% | 100% | Definition not reported |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| Accuracy | Model selection and final test evaluation | Percentage classification accuracy | higher | yes | Validation accuracy used to choose the best network |
| Recall | Final test evaluation | Percentage; formal definition not reported | higher | no | Reported for real-world test set |
| Specificity | Final test evaluation | Percentage; formal definition not reported | higher | no | Reported for real-world test set |

### Ablations

- The paper compares training with synthetic pretraining plus real-world fine-tuning against training directly on the real-world dataset.
- No ablation is reported for individual randomization groups, procedural textures, defect tool design, PBR, or BlenderProc segmentation output.

## Dataset / Benchmark Details

- Source: Synthetic data generated from a turbocharger housing 3D model and real-world endoscopic images of a turbocharger housing cavity.
- Collection: 137 manually chosen inspection poses were used as input to the generator; real-world collection procedure is not reported in detail.
- Annotation: Synthetic images receive generated segmentation maps; real-world annotation process is not reported.
- Size: 4,906 synthetic images after filtering; 110 real-world training images; 110 real-world test images.
- Splits: Synthetic 80/20 training/validation; real-world training set split equally into training and validation.
- Modalities: Images.
- License: not reported for datasets.
- Leakage risks: not reported; the relationship between real-world training and test acquisition conditions is not described in enough detail to assess leakage.
- Bias / coverage: The demonstration focuses on one component and one defect type, blowholes.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Future work will apply models trained with synthesized data directly to real-world data without fine-tuning and will use pixelwise ground truth for object detection and segmentation.
- Inferred: Evidence is limited to a single industrial component, one defect type, small real-world datasets, and a comparison against one model family. Compute, seeds, code, data availability, and statistical uncertainty are not reported.

## Reproducibility

- Code: not reported.
- Data: not reported.
- Hyperparameters: Partially reported: learning rates, batch sizes, epochs, optimizer, ImageNet pretraining, and synthetic split.
- Random seeds: not reported.
- Environment: Blender, Blender Python API, Cycles, and BlenderProc are reported; versions are not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: Synthetic filtering threshold of defects larger than 50 px is reported; other preprocessing details are not reported.
- Artifact status: Local PDF was archived as processed and preprocessed with `pdftotext`; no external code or dataset artifact was reported.

## Systems Details

- Hardware / software stack: Blender, Python API, Cycles renderer, BlenderProc; hardware not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: Dataset size is described as the product of defect, camera pose, and texture loop iterations, but runtime scaling is not measured.
- Deployment assumptions: Requires object model availability and practical defect-tool modeling for the inspection task.
- Cost: not reported.
- Failure modes: not reported.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]]
- Methods: [[Synthetic data generation]], [[Domain randomization]], [[Physically based rendering]], [[Procedural generation]]
- Datasets: [[Synthetic turbocharger housing defect dataset]], [[Real-world endoscopic defect image training dataset]], [[Real-world endoscopic defect image test dataset]]
- Benchmarks: Turbocharger housing blowhole inspection use case.
- Domains: [[Automotive manufacturing]], [[Metal inspection]], [[Industrial visual inspection]]
- Metrics: [[Accuracy]], [[Recall]], [[Specificity]]
- Concepts: [[Domain gap]], [[Transfer learning]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] | Shares method | Both rely on synthetic training data to reduce real-label dependence; this paper renders 2D/endoscopic surface images while Fuchs et al. simulate CT volumes. |
| [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] | Shares method | Both use simulation to generate labeled inspection images for scarce-data industrial defect detection. |
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Contrasts with | Both synthesize defects, but this paper uses procedural 3D rendering and domain randomization while Defect-GAN learns image synthesis. |
| [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] | Contrasts with | Both target synthetic data for visual inspection, but this paper uses CAD/rendering-style procedural generation while Meister et al. use DCGAN/geometric augmentation. |

### Backlinks Updated

- [[Synthetic data generation]] links this paper as the procedural rendering example.
- [[Domain randomization]] explains the randomized defect, camera, illumination, and texture parameters.
- [[Physically based rendering]] links this paper as the Blender/Cycles example.
- [[Procedural generation]] links this paper as the central procedural synthetic-data example.
- [[Transfer learning]] links this paper for synthetic pretraining plus real fine-tuning.
- [[Domain gap]] links this paper for synthetic-to-real transfer and real-world fine-tuning.
- [[Industrial visual inspection]] links this paper as a turbocharger housing inspection use case.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[Domain randomization]] | Created | This paper note |
| [[Physically based rendering]] | Created | This paper note |
| [[Procedural generation]] | Created | This paper note and Fuchs note |
| [[Transfer learning]] | Updated | This paper note and linked notes |
| [[Domain gap]] | Created | Paper limitations and linked notes |
| [[Industrial visual inspection]] | Created | Processed paper notes |
| [[ImageNet]] | Created | This paper note |

## Questions

- How well does the generator transfer when no real-world fine-tuning data is used?
- Which randomization groups contribute most to the observed improvement?
- Does the method generalize to defect types that are harder to model as simple 3D tools?
- Are code, generator scripts, synthetic images, or real-world datasets available outside the paper?
- How sensitive are the results to the manually chosen 137 inspection poses and the 50 px defect visibility threshold?
