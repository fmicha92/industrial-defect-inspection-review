---
title: "A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing"
aliases:
  - "Gearbox components remanufacturing inspection dataset paper"
paper_key: "arxiv:2511.15440"
paper_type: dataset
year: 2025
venue: "IEEE International Conference on Emerging Technologies and Factory Automation (ETFA)"
authors:
  - "Johannes C. Bauer"
  - "Paul Geng"
  - "Stephan Trattnig"
  - "Petr Dokladal"
  - "Rudiger Daub"
status: processed
processed_at: 2026-05-27
topics:
  - remanufacturing
  - visual quality inspection
  - gearbox components
  - distribution shift
  - supervised classification
tasks:
  - "[[Defect classification]]"
domains:
  - "[[Remanufacturing inspection]]"
  - "[[Automotive manufacturing]]"
application_area: "visual quality inspection for remanufactured automotive gearbox components"
datasets:
  - "[[Gearbox components remanufacturing inspection dataset]]"
dataset_sizes:
  - "15588 annotated RGB image patches"
  - "8334 OK patches"
  - "7254 nOK patches"
  - "46 physical components from two automotive transmissions"
splits:
  - "S1 random image split"
  - "S2 acquisition-setting split"
  - "S3 functional-part-ID split"
  - "S4 component-category split"
modalities:
  - "RGB image patches"
methods:
  - "[[Contrastive regularization loss]]"
  - "[[Deep convolutional neural network]]"
  - "[[Vision Transformer]]"
model_family:
  - "CNN"
  - "Transformer"
architectures:
  - "ResNet-50"
  - "DenseNet-121"
  - "MobileNetV3-S"
  - "EfficientNetV2-M"
  - "SwinV2-B"
  - "DINOv2 with registers"
losses:
  - "cross-entropy"
  - "[[Contrastive regularization loss]]"
training_regime: "supervised binary classification with ImageNet-pretrained or self-supervised pretrained backbones"
augmentation:
  - "random horizontal flips"
  - "random vertical flips"
  - "Gaussian noise"
synthetic_data: "none reported"
metrics:
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "The paper reports F1-Score for OK/nOK classification under class imbalance."
baselines:
  - "ResNet-50"
  - "DenseNet-121"
  - "MobileNetV3-S"
  - "EfficientNetV2-M"
  - "SwinV2-B"
  - "DINOv2 with registers"
benchmarks:
  - "[[Gearbox component distribution-shift inspection benchmark]]"
evaluation_protocol: "5-fold cross-validation for S1-S3 and 4-fold cross-validation for S4"
parameters: "not reported"
compute: "not reported"
hardware: "IDS Imaging U330C0CP-C-HQ Rev.2.2 camera with 35 mm lens and two LED light panels"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.1109/ETFA65518.2025.11205777"
pdf: "paper-inbox/10_processed/Dataset/2025 - Bauer - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing.pdf"
code: "not reported"
data: "https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection"
doi: "10.1109/ETFA65518.2025.11205777"
arxiv: "2511.15440"
related_papers:
  - "[[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]"
  - "[[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Distribution shift]]"
  - "[[Domain gap]]"
related_methods:
  - "[[Contrastive regularization loss]]"
  - "[[Deep convolutional neural network]]"
  - "[[Vision Transformer]]"
related_datasets:
  - "[[Gearbox components remanufacturing inspection dataset]]"
related_domains:
  - "[[Remanufacturing inspection]]"
  - "[[Automotive manufacturing]]"
related_tasks:
  - "[[Defect classification]]"
related_benchmarks:
  - "[[Gearbox component distribution-shift inspection benchmark]]"
concept_notes_created_or_updated:
  - "[[Gearbox components remanufacturing inspection dataset]]"
  - "[[Gearbox component distribution-shift inspection benchmark]]"
  - "[[Remanufacturing inspection]]"
  - "[[Distribution shift]]"
  - "[[Contrastive regularization loss]]"
source_file: "paper-inbox/10_processed/Dataset/2025 - Bauer - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Bauer - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Bauer - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing.txt"
artifact_status: "dataset public on Kaggle; code not reported"
tags:
  - paper
  - dataset
  - remanufacturing
  - visual-inspection
---

# A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing

## Summary

- Introduces [[Gearbox components remanufacturing inspection dataset]], a public RGB image dataset of used automotive gearbox components labeled OK or nOK for visual quality inspection.
- Defines four train-test split protocols that create increasing [[Distribution shift]] from random image splits to held-out component categories.
- Benchmarks CNN and Transformer architectures and shows that adding [[Contrastive regularization loss]] to ResNet-50 improves mean [[F1-score]], especially on the hardest component-category split.

## Paper Type

- Type: dataset paper.
- Why: The central contribution is a public dataset and benchmark protocol for [[Remanufacturing inspection]], with baseline model results and one regularization baseline.

## Problem

- Task: [[Defect classification]] for OK/nOK image patches.
- Setting: visual inspection of disassembled automotive gearbox components during remanufacturing.
- Inputs: 128 x 128 RGB patches showing tooth flanks, tooth-like synchronizer features, or splines.
- Outputs: binary OK or nOK labels.
- Motivation: remanufacturing inspection is often manual, while automated visual inspection requires datasets that reflect real wear, component variation, and defect-pattern variation.
- Assumptions: component-level and category-level train-test splits are useful stress tests for model generalization under new products, components, or defect patterns.

## Contribution

- Claimed: The paper introduces a remanufacturing-specific image dataset of gearbox components from two defective automotive transmissions.
- Shown: The dataset contains 15,588 annotated patches from 46 physical components, with 8,334 OK and 7,254 nOK samples.
- Shown: The paper defines four split configurations, S1-S4, that create progressively stronger distribution shifts.
- Shown: Fully trained models exceed 96% average F1-Score on the random split S1, but fall to roughly 63%-71% on the component-category split S4.
- Shown: A ResNet-50 trained with the additional contrastive regularization term improves S4 mean F1-Score from about 71% to about 76%.

## Method

- Core idea: collect labeled image patches from worn gearbox components, benchmark common deep image classifiers under controlled split protocols, and add a supervised contrastive-style embedding regularizer to reduce component-specific shortcuts.
- Data acquisition: 46 components from a BMW E36 automatic transmission and a Mini r53 6-speed manual transmission were cleaned, assigned IDs, mounted on 3D-printed axes, rotated incrementally, and imaged with diffuse LED illumination.
- Annotation: patches were manually labeled OK or nOK based on visible wear. Small sporadic pitting, light scratches, stains, and small oil residues were labeled OK; larger pitting, scratches, scoring, scuffing, notches, ground-in surfaces, and corrosion were labeled nOK.
- Label review: the authors used confident-learning-style review with cross-validation predictions, then reviewed low-confidence samples below 0.75 confidence; 106 labels were changed in the second review step.
- Baseline models: ResNet-50, DenseNet-121, MobileNetV3-S, EfficientNetV2-M, SwinV2-B, and DINOv2 with registers.
- Regularization: the proposed loss adds an alpha-weighted soft-nearest-neighbor term to cross-entropy, using cosine distance between embedding vectors before the final classification layer.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB component image patches.
- Output target: binary OK/nOK label.
- Supervision: supervised classification labels.
- Objective: classify component patches while generalizing to held-out acquisition settings, physical parts, or component categories.

### Model And Training

- Model family: [[Deep convolutional neural network]] and [[Vision Transformer]] baselines.
- Architectures: ResNet-50, DenseNet-121, MobileNetV3-S, EfficientNetV2-M, SwinV2-B, and DINOv2 with registers.
- Parameters: model size is visualized in Fig. 4, but exact parameter counts are not extracted.
- Pretraining: most models use ImageNet1k initialization; DINOv2 uses self-supervised pretraining.
- Fine-tuning: DINOv2 variants include frozen feature extractors; other models are trained fully or fine-tuned as described.
- Losses: cross-entropy, plus optional [[Contrastive regularization loss]] with alpha = 0.2 and T = 2.0.
- Optimizer: Adam with cosine annealing learning-rate scheduling.
- Hyperparameters: batch size 128; random horizontal and vertical flips and Gaussian noise; normalization with ImageNet mean and standard deviation; learning rate and epochs tuned per architecture.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[Gearbox components remanufacturing inspection dataset]].
- Data source: two defective automotive transmissions, one from a BMW E36 and one from a Mini r53.
- Dataset size: 15,588 patches from 46 physical components.
- Labels / annotations: 8,334 OK and 7,254 nOK patches.
- Splits: S1 random image split, S2 acquisition-setting split, S3 functional-part-ID split, and S4 component-category split.
- Preprocessing: 128 x 128 patches extracted from focus regions of component images.
- Augmentation: random flips and Gaussian noise during model training.
- Synthetic data: none reported.
- Leakage checks: the S2-S4 split design explicitly reduces similarity between train and test sets; random S1 has low discrepancy because train and test contain images from all parts and settings.
- License: Kaggle dataset license not reported in extracted text.

### Evaluation

- Protocol: 5-fold cross-validation for S1-S3 and 4-fold cross-validation for S4.
- Model evaluation metrics: [[F1-score]].
- Primary metric: [[F1-score]].
- Metric direction / units: higher is better; reported as percentages.
- Baselines: ResNet-50, DenseNet-121, MobileNetV3-S, EfficientNetV2-M, SwinV2-B, and DINOv2 with registers.
- Benchmarks: [[Gearbox component distribution-shift inspection benchmark]].
- Statistical tests: not reported.
- Failure cases: GradCAM inspection suggests missed wear features and learned correlations that do not transfer to held-out component categories.

## Evidence

### Experimental Setup

- Dataset: [[Gearbox components remanufacturing inspection dataset]].
- Splits: S1-S4 create increasing train-test discrepancy.
- Baselines: CNN and Transformer architectures with ImageNet or self-supervised pretraining.
- Model evaluation metric: [[F1-score]].
- Compute: not reported.
- Hardware: IDS Imaging U330C0CP-C-HQ Rev.2.2 camera with 35 mm lens and two LED panels for acquisition.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Random split performance | [[Gearbox components remanufacturing inspection dataset]] / [[Defect classification]] | [[F1-score]] | higher | not reported | over 96% | All fully trained models on S1. |
| Hardest split performance | [[Gearbox component distribution-shift inspection benchmark]] / S4 | [[F1-score]] | higher | not reported | 63%-71% | Component-category split. |
| DINOv2 frozen feature extractor | [[Gearbox component distribution-shift inspection benchmark]] | [[F1-score]] | higher | not reported | 91.3% on S1; 63.3% on S4 | Frozen DINO feature extractors perform below fully trained variants. |
| Contrastive regularization on S4 | [[Gearbox component distribution-shift inspection benchmark]] / S4 | [[F1-score]] | higher | about 71% | about 76% | ResNet-50 with additional regularization term. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[F1-score]] | OK/nOK classification under class imbalance | percentage | higher is better | yes | The paper reports mean and standard deviation across CV folds. |

### Ablations

- Contrastive regularization is evaluated with ResNet-50 against the same architecture without the additional loss term.
- The improvement is marginal on S1, about one percentage point on S2 and S3, and about five percentage points on S4.
- S4 per-category results show most improvement for synchronizer bodies; performance on spline components remains poor.

## Dataset / Benchmark Details

- Source: defective BMW E36 and Mini r53 automotive transmissions.
- Collection: cleaned parts mounted on 3D-printed axes and rotated to capture tooth flanks or tooth-like features.
- Annotation: manual OK/nOK labels, with iterative label review using model predictions and low-confidence sample inspection.
- Size: 15,588 annotated patches.
- Components: 46 physical components, 19 from the BMW transmission and 27 from the Mini transmission.
- Classes: 8,334 OK and 7,254 nOK.
- Component categories: gear wheel, synchronizer ring/cone, synchronizer body, synchronizer collar, and spline.
- Splits: S1 random image split, S2 acquisition-setting split, S3 functional-part-ID split, S4 component-category split.
- Modalities: RGB images.
- Artifact: https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection.
- License: not reported in extracted text.
- Leakage risks: random S1 contains images from all parts and acquisition settings in both train and test; S2-S4 are designed to reduce component and acquisition similarity.
- Bias / coverage: only 46 parts from two gearboxes; gear wheels are about 71% of samples; synchronizer rings/cones have about 22% OK samples.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: 46 physical parts from two gearboxes do not cover the full range of possible component and defect types.
- Stated: performance varies strongly depending on the selected test components, making cross-validation important and computationally expensive.
- Stated: OK/nOK judgments are subjective for borderline cases, so different annotators might disagree.
- Inferred: no code release is reported in the extracted text.
- Inferred: the benchmark is classification-only; anomaly detection and segmentation reuse are proposed as future opportunities rather than evaluated tasks.

## Reproducibility

- Code: not reported.
- Data: https://www.kaggle.com/datasets/jhnnsbr/gearboxcomponents-remanufacturing-inspection.
- Hyperparameters: batch size 128; alpha = 0.2 and T = 2.0 for the contrastive term; learning rate and epochs tuned per architecture but exact values are not reported in the extracted text.
- Random seeds: not reported.
- Environment: PyTorch torchvision and Hugging Face transformers are used.
- Checkpoints / models: not reported.
- Exact preprocessing: 128 x 128 patches extracted from focus regions of RGB component images.
- Artifact status: dataset public on Kaggle; code not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]]
- Datasets: [[Gearbox components remanufacturing inspection dataset]]
- Methods: [[Contrastive regularization loss]], [[Deep convolutional neural network]], [[Vision Transformer]]
- Metrics: [[F1-score]]
- Domains: [[Remanufacturing inspection]], [[Automotive manufacturing]], [[Industrial visual inspection]]
- Benchmarks: [[Gearbox component distribution-shift inspection benchmark]]
- Concepts: [[Distribution shift]], [[Domain gap]]

### Builds On

- The paper builds its regularization term on soft-nearest-neighbor-style contrastive representation learning, but no existing paper note for those sources is present.

### Contrasts With

- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]: both address automotive-oriented visual quality inspection, but this paper contributes real remanufacturing gearbox images and split protocols, while the adhesive paper focuses on simulation-based synthetic augmentation.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]: both concern automotive part inspection, but this paper uses real worn gearbox components and supervised classification rather than procedurally generated turbocharger defect imagery.

### Shares Dataset

- [[Gearbox components remanufacturing inspection dataset]]: introduced by this paper.

### Shares Task

- [[Defect classification]]: the benchmark classifies image patches as OK or nOK.

### Shares Method

- [[Contrastive regularization loss]]: the paper adds a soft-nearest-neighbor loss term to cross-entropy for improved generalization.
- [[Deep convolutional neural network]]: CNN baselines include ResNet-50, DenseNet-121, MobileNetV3-S, and EfficientNetV2-M.
- [[Vision Transformer]]: Transformer-style baselines include SwinV2-B and DINOv2 with registers.

### Shares Metric

- [[F1-score]]: the paper uses mean F1-Score to handle class imbalance in split-specific classification results.

### Application / Domain

- [[Remanufacturing inspection]]: the dataset targets inspection of worn components before reuse.
- [[Automotive manufacturing]]: the physical objects are automotive gearbox components.
- [[Industrial visual inspection]]: the paper frames the task as automated visual quality inspection.

### Follow-Up Reading

- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]: useful for comparing real-data and simulation-based automotive inspection datasets.
- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]: useful for contrasting real remanufacturing components with procedural inspection-image generation.

## Questions

- What license applies to the Kaggle dataset?
- Are the authors planning to release training code and exact tuned hyperparameters?
- How do anomaly detection and segmentation methods perform on the same images when trained with only OK samples or with weaker labels?
