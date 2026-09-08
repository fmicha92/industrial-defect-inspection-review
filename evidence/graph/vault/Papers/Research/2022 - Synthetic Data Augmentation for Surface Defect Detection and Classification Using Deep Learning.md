---
title: "Synthetic data augmentation for surface defect detection and classification using deep learning"
aliases:
  - "Synthetic data augmentation for surface defect detection and classification using deep learning"
paper_key: "doi:10.1007/s10845-020-01710-x"
paper_type: research
year: 2022
venue: "Journal of Intelligent Manufacturing"
authors:
  - "Saksham Jain"
  - "Gautam Seth"
  - "Arpit Paruthi"
  - "Umang Soni"
  - "Girish Kumar"
status: processed
processed_at: 2026-05-23
topics:
  - surface defect classification
  - synthetic data augmentation
  - GAN augmentation
  - hot-rolled steel strips
tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Metal inspection]]"
application_area: "Classification of hot-rolled steel strip surface defects"
datasets:
  - "[[NEU-CLS]]"
dataset_sizes:
  - "1,800 original NEU-CLS images; 300 images for each of six defect classes"
  - "9,000 augmented training images"
  - "1,800 validation/test images"
splits:
  - "Training/validation split of 9,000 and 1,800 images after augmentation, with balanced classes"
modalities:
  - grayscale image
methods:
  - "[[GAN-based surface defect augmentation]]"
  - "[[GAN]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
model_family:
  - convolutional neural network
  - generative adversarial network
architectures:
  - "3-layer CNN classifier"
  - "DCGAN"
  - "ACGAN"
  - "InfoGAN"
losses:
  - "softmax cross-entropy with logits for CNN classification"
training_regime: "Train GANs on classically augmented NEU-CLS subsets, generate synthetic images, train a CNN classifier on equally sized augmented datasets, and compare classic, DCGAN, ACGAN, InfoGAN, and transfer-learning settings."
augmentation:
  - "classic rotation, flipping, translation, and rescaling"
  - "DCGAN synthetic image augmentation"
  - "ACGAN synthetic image augmentation"
  - "InfoGAN synthetic image augmentation"
synthetic_data: "GANs generate additional steel surface defect images from NEU-CLS-derived training data; DCGAN trains one model per class, while ACGAN and InfoGAN use label or latent-code mechanisms."
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
  - "[[Specificity]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "accuracy: (TP+TN)/(TP+TN+FP+FN)"
  - "sensitivity/recall: TP/(TP+FN)"
  - "specificity: TN/(TN+FP)"
baselines:
  - "classic augmentation CNN"
  - "AECLBP"
  - "SCN"
  - "Overfeat"
benchmarks:
  - "[[NEU-CLS]]"
evaluation_protocol: "Compare CNN performance on classic and GAN-augmented training sets of the same size; report mean sensitivity, mean specificity, and accuracy, then compare DCGAN augmentation with feature-extraction baselines and a fine-tuned CNN."
parameters: "CNN has three convolutional layers: 32 3x3 filters, 32 3x3 filters, 64 3x3 filters, ReLU activations, and a 256-neuron fully connected layer."
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.1007/s10845-020-01710-x"
pdf: "paper-inbox/10_processed/Research/2022 - Jain - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning.pdf"
code: "not reported"
data: "NEU-CLS public dataset used; paper does not report a released augmented dataset."
doi: "10.1007/s10845-020-01710-x"
arxiv: "not applicable"
related_papers:
  - "[[2020 - Defect Image Sample Generation With GAN for Improving Defect Recognition]]"
  - "[[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[GAN-based surface defect augmentation]]"
  - "[[GAN]]"
  - "[[DCGAN]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[NEU-CLS]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "[[NEU-CLS]]"
source_file: "paper-inbox/10_processed/Research/2022 - Jain - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Jain - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Jain - Synthetic Data Augmentation for Surface Defect Detection and Classification Using Deep Learning.txt"
artifact_status: "not reported"
tags:
  - paper
---
# Synthetic data augmentation for surface defect detection and classification using deep learning

## Summary

- Jain et al. evaluate GAN-based synthetic data augmentation for hot-rolled steel surface defect classification on [[NEU-CLS]].
- The study compares classic geometric augmentation with DCGAN, ACGAN, and InfoGAN augmentation while holding the CNN classifier and augmented training-set size constant.
- DCGAN augmentation gives the best simple-CNN result, improving accuracy from 90.28% with classic augmentation to 95.78%; a fine-tuned pretrained CNN reaches 99.11%.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a GAN-based augmentation pipeline for a supervised industrial defect classification task.

## Problem

- Task: [[Defect classification]] for steel strip surface defects.
- Setting: Manufacturing inspection where defective samples are scarce and defect classes can be visually diverse within a class or similar across classes.
- Inputs: NEU-CLS grayscale steel surface defect images and GAN-generated synthetic defect images.
- Outputs: One of six defect classes: rolled-in scale, patches, crazing, pitted surface, inclusion, or scratches.
- Motivation: CNNs need large labeled datasets, while manufacturing defect data are expensive to collect and may be small or imbalanced.
- Assumptions: GAN-generated images that resemble defect images can add useful variation beyond classic affine transformations.

## Contribution

- Claimed: GANs can serve as a standard preprocessing augmentation technique for small manufacturing defect datasets.
- Claimed: A simple CNN trained on synthetically augmented data can outperform more complex CNN-based feature extractors trained with classic augmentation.
- Shown: DCGAN augmentation improves simple-CNN accuracy by 5.5 percentage points over classic augmentation and improves sensitivity and specificity.

## Method

- Core idea: Train GAN models on augmented NEU-CLS defect images, generate additional synthetic defect samples, and use those samples to train a CNN classifier.
- Architecture / algorithm: Classic augmentation, DCGAN, ACGAN, and InfoGAN are compared as augmentation pipelines; a three-convolution-layer CNN performs classification.
- Objective / loss: CNN uses softmax cross-entropy with logits; GAN objectives are described by their standard architectures but exact losses for each implementation are not fully detailed in the analysis input.
- Optimization: CNN uses Adam with learning rate 0.0001. DCGAN and ACGAN use learning rate 0.0002 and beta1=0.5. InfoGAN uses learning rate 0.003, beta1=0.5, and beta2=0.999.
- Training data: NEU-CLS images expanded to 9,000 training images and 1,800 validation/test images.
- Data pipeline: Generate classic augmentations; train GANs on 5,400 class-balanced images from the classic augmented training set; generate 3,600 synthetic samples; train the same CNN on equally sized augmented sets.
- Augmentation / synthesis: Classic rotation, flipping, translation, and rescaling; synthetic image generation from DCGAN, ACGAN, and InfoGAN.
- Inference: CNN predicts one of six steel surface defect classes.
- Complexity / deployment constraints: DCGAN requires separate per-class models; GAN hyperparameter selection is described as difficult, so the paper uses default or out-of-box settings.

## ML / DL Extraction

### Task Formulation

- Input modality: 200 x 200 grayscale defect images, trained as RGB-channel inputs for the CNN.
- Output target: Six-class defect classification.
- Supervision: Supervised CNN classification with labels; GANs are trained to synthesize class-specific or class-conditioned samples.
- Objective: Improve classifier generalization with synthetic augmentation.

### Model And Training

- Model family: CNN classifier and GAN generators/discriminators.
- Architecture: CNN with three convolutional layers, ReLU activations, and a 256-neuron fully connected layer; DCGAN, ACGAN, and InfoGAN augmentation models.
- Parameters: CNN filter counts are reported; total parameter counts are not reported.
- Pretraining: One experiment pretrains the CNN on a smaller ImageNet subset and fine-tunes it on NEU-CLS.
- Fine-tuning: Fine-tuned CNN uses the same 9,000 training and 1,800 validation images as the other experiments.
- Losses: CNN uses softmax cross-entropy with logits.
- Optimizer: Adam for the CNN.
- Hyperparameters: CNN learning rate 0.0001, batch size 60, 20 epochs; DCGAN/ACGAN batch size 25 and 100 epochs; InfoGAN batch size 30 and 120 epochs.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[NEU-CLS]].
- Data source: Northeastern University surface defect database for hot-rolled steel strips.
- Dataset size: 1,800 original images, 300 per defect class.
- Labels / annotations: Class labels for rolled-in scale, patches, crazing, pitted surface, inclusion, and scratches.
- Splits: 9,000 augmented training images and 1,800 validation/test images, balanced across classes.
- Preprocessing: Images are resized to 200 x 200 after classic augmentation; grayscale values range from 0 to 255.
- Augmentation: Classic affine transformations and GAN-generated synthetic samples.
- Synthetic data: DCGAN, ACGAN, and InfoGAN each generate 3,600 synthetic samples from class-balanced training subsets.
- Leakage checks: not reported.
- License: not reported.

### Evaluation

- Protocol: Train the same CNN under classic, DCGAN, ACGAN, and InfoGAN augmentation settings; compare sensitivity, specificity, and accuracy; compare DCGAN-augmented CNN and fine-tuned CNN against AECLBP, SCN, and Overfeat.
- Used performance metrics: [[Accuracy]], [[Recall]]/sensitivity, and [[Specificity]].
- Primary metric: [[Accuracy]].
- Metric definitions: The paper defines accuracy, sensitivity, and specificity using TP, TN, FP, and FN.
- Metric direction / units: percentage, higher is better.
- Baselines: Classic augmentation, AECLBP, SCN, Overfeat.
- Benchmarks: [[NEU-CLS]].
- Statistical tests: not reported.
- Failure cases: Classic augmentation has low sensitivity for patches and scratches; InfoGAN image fidelity is lower than DCGAN in the reported results.

## Evidence

### Experimental Setup

- Datasets: [[NEU-CLS]].
- Splits: 9,000 augmented training images and 1,800 validation/test images.
- Baselines: Classic augmentation, AECLBP, SCN, Overfeat, and GAN variants.
- Used performance metrics: [[Accuracy]], [[Recall]]/sensitivity, and [[Specificity]].
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| DCGAN augmentation improves simple CNN | [[NEU-CLS]] / defect classification | Accuracy | higher | 90.28% | 95.78% | Baseline is classic augmentation |
| DCGAN augmentation improves sensitivity | [[NEU-CLS]] / defect classification | Sensitivity | higher | 90.28% | 95.33% | Mean sensitivity |
| DCGAN augmentation improves specificity | [[NEU-CLS]] / defect classification | Specificity | higher | 98.06% | 99.16% | Mean specificity |
| ACGAN augmentation result | [[NEU-CLS]] / defect classification | Accuracy | higher | 90.28% | 92.78% | Same CNN and training conditions |
| InfoGAN augmentation result | [[NEU-CLS]] / defect classification | Accuracy | higher | 90.28% | 94.86% | Lower than DCGAN, attributed to lower image fidelity |
| Fine-tuned CNN result | [[NEU-CLS]] / defect classification | Accuracy | higher | 95.78% | 99.11% | Baseline is DCGAN-augmented CNN; pretrained CNN is fine-tuned |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Six-class defect classification | Percentage of correct predictions | higher | yes | Main comparison metric |
| [[Recall]] | Class-wise sensitivity | TP/(TP+FN), reported as mean sensitivity | higher | no | Also called true positive rate |
| [[Specificity]] | Class-wise true negative rate | TN/(TN+FP), reported as mean specificity | higher | no | Used with sensitivity to interpret confusion matrices |

### Ablations

- DCGAN, ACGAN, and InfoGAN are compared under the same CNN training conditions.
- Classic augmentation expands training data to 9,000 images, but its improvement is reported to saturate because it does not add new image content.
- InfoGAN latent codes are shown to capture lighting and defect-severity variation, but the classification accuracy remains below DCGAN because of lower image fidelity.

## Dataset / Benchmark Details

- Source: NEU surface defect database, NEU-CLS subset.
- Collection: Hot-rolled steel strip defect images.
- Annotation: Six class labels, with 300 images per class.
- Size: 1,800 original images.
- Splits: 9,000 augmented training images and 1,800 validation/test images.
- Modalities: 200 x 200 grayscale images.
- License: not reported.
- Leakage risks: not reported.
- Bias / coverage: Dataset has six balanced defect classes but no non-defective class.
- Maintenance: not reported.

## Review / Survey Details

- Scope: not applicable.
- Inclusion criteria: not applicable.
- Taxonomy: not applicable.
- Major themes: not applicable.
- Gaps: not applicable.

## Limitations

- Stated: Future work could extend the methodology to segmentation, which would require synthetic defect images and corresponding ground-truth masks.
- Inferred: The evaluation uses one steel defect dataset, no reported hardware or random seeds, and no reported release of generated samples or code.

## Reproducibility

- Code: not reported.
- Data: NEU-CLS is used; release details are not reported in the analysis input.
- Hyperparameters: CNN, DCGAN, ACGAN, and InfoGAN training settings are partially reported.
- Random seeds: not reported.
- Environment: Python image_slicer is mentioned for slicing generated grids; framework versions are not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: Classic augmentation ranges and resizing are reported; full GAN implementation details are partial.
- Artifact status: not reported.

## Systems Details

- Hardware / software stack: not reported.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: not reported.
- Deployment assumptions: The paper suggests trained augmentation pipelines could be used with cameras and single-board computers, but does not report deployment measurements.
- Cost: not reported.
- Failure modes: Classic augmentation underperforms for patches and scratches; InfoGAN has lower image fidelity than DCGAN.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Surface defect detection]]
- Methods: [[GAN-based surface defect augmentation]], [[GAN]], [[DCGAN]], [[Data augmentation]]
- Datasets: [[NEU-CLS]]
- Benchmarks: [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]], [[Recall]], [[Specificity]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2020 - Defect Image Sample Generation With GAN for Improving Defect Recognition]] | Shares method | Both use GAN-generated defect images to improve defect recognition. |
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Shares method | Both study GAN-based synthetic defect augmentation for automated inspection, though this paper compares DCGAN, ACGAN, and InfoGAN on NEU-CLS. |

### Backlinks Updated

- [[NEU-CLS]] links this paper as a steel surface defect classification and synthetic augmentation study.
- [[GAN-based surface defect augmentation]] links this paper as its source method.
- [[Metal inspection]] links this paper as a hot-rolled steel strip defect classification study.
- [[Accuracy]], [[Recall]], and [[Specificity]] link this paper for reported classification metrics.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[NEU-CLS]] | Updated | Dataset and results sections |
| [[GAN-based surface defect augmentation]] | Updated | GAN augmentation method |
| [[Metal inspection]] | Updated | Application setting |

## Questions

- Would DCGAN remain the best augmentation option under stronger modern GAN or diffusion baselines?
- How stable are the reported gains across random initializations and train/test split variants?
- Can the augmentation pipeline generate pixel masks well enough for segmentation tasks?
