---
title: "Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images"
aliases:
  - "Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images"
paper_key: "doi:10.1038/s41598-025-14478-y"
paper_type: research
year: 2025
venue: "Scientific Reports"
authors:
  - "Mostafa A. Ebied"
  - "Amr Munshi"
  - "Shakir A. Alhuzali"
  - "Mohamed M. El-sotouhy"
  - "Amr I. Shehta"
  - "M. S. Elborlsy"
status: processed
processed_at: 2026-06-11
topics:
  - "photovoltaic defect classification"
  - "GAN oversampling"
  - "transfer learning"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
application_area: "photovoltaic module quality inspection"
datasets:
  - "[[ELPV Dataset]]"
dataset_sizes:
  - "ELPV: 2,624 EL solar-cell images; paper also evaluates four-class and eight-class categorizations"
splits:
  - "80% training / 20% testing"
modalities:
  - "electroluminescence images"
methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
model_family:
  - "convolutional neural networks"
architectures:
  - "DenseNet169"
  - "DenseNet201"
  - "ResNet101"
  - "ResNet152"
  - "SENet154"
  - "[[VGG-16]]"
  - "[[VGG19]]"
losses:
  - "cross-entropy"
optimizers:
  - "[[Adam]]"
training_regime: "transfer learning with regression-to-classification thresholding"
augmentation:
  - "GAN-based oversampling"
synthetic_data: "AUG300 generates 300 synthetic images for underrepresented or weakly predicted classes"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[Accuracy]]"
primary_metric: "[[Recall]]"
metric_definitions:
  - "Class recall mean is the main comparison table metric"
baselines:
  - "4C-AUG without extra AUG300 oversampling"
  - "8C-AUG without extra AUG300 oversampling"
benchmarks: []
evaluation_protocol: "compare seven CNN architectures across four-class/eight-class categorizations, with and without AUG300, before and after fastai find_lr learning-rate selection"
parameters: "not reported"
compute: "Google Colab Linux server"
hardware: "CPU, Tesla K80 GPU, or TPU options reported"
training_time: "reported in time tables for selected approaches; exact extracted table cells are incomplete"
inference_cost: "not reported"
url: "https://doi.org/10.1038/s41598-025-14478-y"
pdf: "paper-inbox/10_processed/Research/2025 - Ebied - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images.pdf"
code: "not reported"
data: "public ELPV-style EL image dataset; paper data availability section points to cited source"
doi: "10.1038/s41598-025-14478-y"
arxiv: "not applicable"
related_papers:
  - "[[2024 - Improved Hybrid Solar Cell Defect Detection Using GANs and Weighted Classification]]"
related_concepts:
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_methods:
  - "[[GAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[ELPV Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks: []
concept_notes_created_or_updated: []
source_file: "paper-inbox/10_processed/Research/2025 - Ebied - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Ebied - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Ebied - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images.txt"
artifact_status: "code not reported; data source public by cited dataset"
tags:
  - paper
---

# Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images

## Summary

- The paper evaluates GAN-based oversampling for EL solar-cell defect classification using multiple CNN backbones.
- The best extracted result is ResNet152 with 4C-AUG300 after learning-rate tuning, reaching 0.9013 class recall mean.
- The main experimental claim is that balanced GAN oversampling and validation-driven threshold selection improve defect/non-defect classification compared with non-AUG300 variants.

## Paper Type

- Type: research.
- Why: it proposes and evaluates a photovoltaic defect-classification pipeline with synthetic oversampling, model comparisons, and quantitative results.

## Problem

- Task: classify photovoltaic cells as defective or non-defective from EL images after mapping regression outputs to classes.
- Setting: scarce and imbalanced EL defect data, with four defect-probability classes and an eight-class variant that separates monocrystalline and polycrystalline cells.
- Inputs: EL solar-cell images resized for CNN backbones.
- Outputs: regression estimates thresholded into defect/non-defect decisions.
- Motivation: PV defects are hard to inspect manually and EL datasets are imbalanced.
- Assumptions: validation-set threshold tuning can correct model bias without using the test set.

## Contribution

- Claimed: combines GAN oversampling, CNN transfer learning, dynamic learning-rate selection, and adaptive thresholding for PV EL defect detection.
- Shown: AUG300 variants outperform several non-AUG300 variants in class recall mean; the best reported extracted value is 0.9013 for ResNet152 in 4C-AUG300 after LR tuning.
- Inferred: the clearest source-supported augmentation effect is the comparison between 4C-AUG and 4C-AUG300 / 8C-AUG and 8C-AUG300 conditions.

## Method

- Core idea: generate synthetic samples for underrepresented or weakly predicted classes and train CNN regressors whose outputs are thresholded into binary defect decisions.
- Architecture / algorithm: DenseNet169, DenseNet201, ResNet101, ResNet152, SENet154, VGG16, and VGG19 are compared.
- Objective / loss: cross-entropy is reported for CNN optimization; regression metrics MSE, RMSE, and MAE are also reported.
- Optimization: Adam with beta1 = 0.9 and beta2 = 0.999; learning-rate variants include fixed 1e-4 and fastai `find_lr`.
- Training data: four-class and eight-class EL image categorizations.
- Data pipeline: 80/20 train/test split; regression outputs are converted to binary defect/non-defect labels through thresholds derived from validation data.
- Augmentation / synthesis: GAN oversampling and AUG300 add 300 images to selected classes.
- Inference: CNN regression followed by thresholding.
- Complexity / deployment constraints: deeper ResNet and DenseNet variants require more compute; timing tables are reported but the extracted table cells are incomplete.

## ML / DL Extraction

### Task Formulation

- Input modality: electroluminescence solar-cell image.
- Output target: defect / non-defect classification after thresholding.
- Supervision: supervised labels derived from defect-percentage classes.
- Objective: improve PV EL defect classification under imbalance.

### Model And Training

- Model family: CNN transfer-learning models.
- Architecture: DenseNet169, DenseNet201, ResNet101, ResNet152, SENet154, VGG16, VGG19.
- Parameters: not reported.
- Pretraining: ImageNet pretraining is reported for ResNet variants.
- Fine-tuning: models trained for the PV EL classification/regression task.
- Losses: cross-entropy and regression-error reporting.
- Optimizer: Adam.
- Hyperparameters: GAN batch size 32, 100 epochs, learning rate 0.0002; CNN batch size 16 in one approach; CNN epochs set to 70.
- Seeds: not reported.
- Training compute: Google Colab with CPU, Tesla K80 GPU, or TPU options.

### Data

- Datasets: [[ELPV Dataset]]-style public solar-cell EL images.
- Data source: public high-resolution EL solar-cell image dataset cited by the paper.
- Dataset size: source dataset has 2,624 samples; the paper uses four-class and eight-class categorizations.
- Labels / annotations: defect percentages/classes and cell type.
- Splits: 80% train and 20% test.
- Preprocessing: resizing to CNN input sizes; threshold analysis on validation data.
- Augmentation: GAN oversampling.
- Synthetic data: AUG300 creates 300 added images for selected classes.
- Leakage checks: threshold optimization is stated to use validation performance only, not training data directly.
- License: not reported.

### Evaluation

- Protocol: compare model families under 4C-AUG, 4C-AUG300, 8C-AUG, and 8C-AUG300 before and after LR tuning.
- Used performance metrics: precision, recall, F1-score, MSE, RMSE, MAE, and class recall mean.
- Primary metric: class recall mean in the extracted main comparison tables.
- Metric definitions: recall, precision, and F1 formulas are provided.
- Metric direction / units: higher class recall mean is better; lower MSE/RMSE/MAE is better.
- Baselines: 4C-AUG and 8C-AUG without AUG300.
- Benchmarks: not reported as a named benchmark.
- Statistical tests: not reported.
- Failure cases: VGG models remain biased after thresholding in some settings.

## Evidence

### Experimental Setup

- Datasets: public EL solar-cell images, split into four-class and eight-class categorizations.
- Splits: 80/20 train/test.
- Baselines: non-AUG300 variants and fixed-learning-rate variants.
- Used performance metrics: recall, precision, F1-score, MSE, RMSE, MAE.
- Compute: Google Colab.
- Hardware: CPU, Tesla K80 GPU, or TPU options.
- Training time: reported but not fully extracted.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best before LR tuning | PV EL defect classification | Class recall mean | higher | 4C-AUG max 0.8892 | 8C-AUG300 max 0.8950 | DenseNet201 is the standout model for 8C-AUG300 before LR tuning. |
| Best after LR tuning | PV EL defect classification | Class recall mean | higher | 4C-AUG max 0.8903 | 4C-AUG300 max 0.9013 | ResNet152 is the best extracted result after `find_lr`. |
| Mean after LR tuning | PV EL defect classification | Class recall mean | higher | 4C-AUG mean 0.8360 | 4C-AUG300 mean 0.8657 | Shows the clearest average improvement from AUG300 in the extracted table. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Recall]] | Class-level defect/non-defect evaluation | TP / (TP + FN) | higher | yes | Main extracted table uses class recall mean. |
| [[Precision]] | Class-level evaluation | TP / (TP + FP) | higher | no | Reported with recall and F1. |
| [[F1-score]] | Balanced classification metric | harmonic mean of precision and recall | higher | no | Reported for classes. |
| MSE/RMSE/MAE | Regression outputs before thresholding | regression error | lower | no | Used to report regression model behavior. |

### Ablations

- 4C-AUG vs 4C-AUG300 isolates extra GAN oversampling in the four-class setup.
- 8C-AUG vs 8C-AUG300 isolates extra GAN oversampling in the eight-class setup.
- Fixed learning rate vs `find_lr` isolates learning-rate selection.

## Dataset / Benchmark Details

- Source: public EL solar-cell image dataset.
- Collection: high-resolution EL images from monocrystalline and polycrystalline PV modules.
- Annotation: defect percentage / class and cell type.
- Size: source dataset has 2,624 samples.
- Splits: 80/20 train/test.
- Modalities: electroluminescence images.
- License: not reported in extracted text.
- Leakage risks: validation thresholds are tuned on validation data; no explicit leakage audit beyond this statement.
- Bias / coverage: class imbalance and model bias toward class one are explicitly discussed.
- Maintenance: not reported.

## Limitations

- Stated: deeper models require more computational resources and time.
- Stated: some models remain biased after threshold adjustment.
- Inferred: the source does not fully isolate GAN oversampling from every other design choice because class grouping, thresholding, and learning-rate changes also affect performance.

## Reproducibility

- Code: not reported.
- Data: public dataset cited.
- Hyperparameters: GAN and selected CNN settings are reported.
- Random seeds: not reported.
- Environment: Python, Colab, Ubuntu 16.04.
- Checkpoints / models: not reported.
- Exact preprocessing: partially reported.
- Artifact status: partial reproducibility; code and seeds not reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]].
- Methods: [[GAN]], [[Data augmentation]], [[Synthetic data generation]].
- Optimizers: [[Adam]].
- Datasets: [[ELPV Dataset]].
- Benchmarks: not reported.
- Domains: [[Solar cells and photovoltaic]].
- Metrics: [[Recall]], [[Precision]], [[F1-score]], [[Accuracy]].
- Concepts: class imbalance, regression-to-classification thresholding.
- Dataset-domain links: [[ELPV Dataset]] is associated with [[Solar cells and photovoltaic]].

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2024 - Improved Hybrid Solar Cell Defect Detection Using GANs and Weighted Classification]] | Shares dataset / shares method | Both use GAN-based augmentation for solar-cell EL defect classification. |

### Backlinks Updated

- Pending graph audit.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| not applicable | not applicable | Existing graph nodes cover the central concepts. |

## Questions

- The extracted tables do not preserve every timing value; check the PDF table if training time is needed.
- The exact data URL is cited indirectly through the paper's dataset reference and should be verified before downstream reuse.
