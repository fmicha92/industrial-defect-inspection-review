---
title: "Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach"
aliases:
  - "Automated steel surface defect detection and classification using a new deep learning-based approach"
paper_key: "doi:10.1007/s00521-022-08112-5"
paper_type: research
year: 2023
venue: "Neural Computing and Applications"
authors:
  - "Kursat Demir"
  - "Mustafa Ay"
  - "Mehmet Cavas"
  - "Fatih Demir"
status: processed
processed_at: 2026-06-05
topics:
  - "steel surface defect detection"
  - "steel surface defect classification"
  - "deep feature selection"
tasks:
  - "[[Defect classification]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[Severstal Steel Defect Dataset]]"
methods:
  - "[[Parallel attention-residual CNN]]"
  - "[[NCA-ReliefF Matched Index feature selection]]"
  - "[[Support vector machine]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[Parallel attention-residual CNN]]"
optimizers:
  - "[[Stochastic gradient descent]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F-measure]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  accuracy: "Classification accuracy; higher is better."
  sensitivity: "Class sensitivity/recall; higher is better."
  specificity: "Class specificity; higher is better."
  precision: "Positive predictive value; higher is better."
  f_score: "F-score; higher is better."
baselines:
  - "PAR-CNN with softmax"
  - "PAR-CNN features with SVM"
  - "PAR-CNN with NCA feature selection and SVM"
  - "PAR-CNN with ReliefF feature selection and SVM"
  - "CNN, A-CNN, and R-CNN variants"
benchmarks:
  - "[[Severstal Steel Defect Dataset]]"
  - "[[NEU-CLS]]"
doi: "10.1007/s00521-022-08112-5"
url: "https://doi.org/10.1007/s00521-022-08112-5"
pdf: "paper-inbox/10_processed/Research/2023 - Demir - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Demir - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Demir - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Demir - Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach.txt"
code: "not reported"
data: "https://www.kaggle.com/c/severstal-steel-defect-detection"
artifact_status: "dataset URL reported; code not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Parallel attention-residual CNN]]"
  - "[[NCA-ReliefF Matched Index feature selection]]"
  - "[[Support vector machine]]"
related_datasets:
  - "[[Severstal Steel Defect Dataset]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
tags:
  - paper
---
# Automated Steel Surface Defect Detection and Classification Using a New Deep Learning-Based Approach

## Summary

- The paper proposes a four-step steel surface defect classification pipeline: train [[Parallel attention-residual CNN]], extract 500 deep features from its `fc4` layer, select features with [[NCA-ReliefF Matched Index feature selection]], and classify with [[Support vector machine]].
- It evaluates binary defect/no-defect classification and five-class defect classification on [[Severstal Steel Defect Dataset]], then tests the same pipeline on [[NEU-CLS]].
- The strongest reported Severstal results are 97.90% binary accuracy and 94.50% multi-class accuracy with PAR-CNN + NRMI + SVM.

## Paper Type

Research paper. It introduces a neural feature extractor, a feature-selection algorithm, and experimental comparisons for steel surface defect classification.

## Problem

- Task: classify steel surface images as defective or non-defective, and classify defective images into pitted surface, crazing, scratches, patches, or multi-defect classes.
- Setting: [[Metal inspection]] for flat-rolled steel surface quality control.
- Input: JPG steel surface images resized from 1600 x 256 to 200 x 32 to reduce hardware requirements.
- Output: binary class label or five-class defect label.
- Motivation: automatic defect inspection can reduce reliance on expert visual supervision, which is time-consuming and accuracy-limited.

## Contribution

- Proposes [[Parallel attention-residual CNN]], where residual blocks and an attention structure are trained in parallel.
- Extracts 500 deep features from PAR-CNN and replaces the softmax classifier with SVM for final classification.
- Introduces [[NCA-ReliefF Matched Index feature selection]], which selects matched high-weight features from NCA and ReliefF rankings.
- Reports that NRMI reduces feature dimensionality to 100 features for binary classification and 66 features for multi-class classification while improving accuracy.

## Method

- PAR-CNN combines six residual blocks with a parallel attention branch. The paper reports that seven residual blocks caused out-of-memory errors on the available hardware, so the architecture is constrained to six residual blocks.
- The attention module computes pixel-wise attention weights from feature maps and a coarser gating signal, then multiplies the attention map by the input feature map.
- After PAR-CNN training, 500 activations are extracted from the fully connected `fc4` layer.
- NRMI computes feature-importance rankings with Neighborhood Component Analysis and ReliefF, then selects features whose indexes match among the top 200 features from both methods.
- The selected features are classified with a polynomial-kernel SVM. The reported SVM hyperparameters are kernel scale 5 and box constraint 1.

## Evidence

### Data

| Dataset | Source-backed details |
|---|---|
| [[Severstal Steel Defect Dataset]] | Kaggle dataset used for binary and multi-class classification. Binary classification uses 6666 defect images and 5902 no-defect images. Multi-class classification uses 6668 steel defect images containing pitted surface, crazing, scratches, patches, and multi-defect labels. |
| [[NEU-CLS]] | Used as an additional reliability test with 1800 samples, 300 samples in each of six defect classes: crazing, inclusion, patches, pitted surface, rolled-in scale, and scratches. |

### Training Setup

| Setting | Reported detail |
|---|---|
| Software/hardware | MATLAB 2020a on Windows 10; Intel i7-5500U, 8 GB RAM, 2 GB graphics card. |
| Optimizer | Stochastic Gradient Descent with momentum. |
| Learning rate | 0.001. |
| Epochs | 50. |
| Validation | Tenfold cross-validation. |
| Loss | Cross-entropy. |
| PAR-CNN training time | About 2 hours on the reported hardware. |
| SVM estimation time | About 15 seconds. |

### Results

| Experiment | Result |
|---|---|
| PAR-CNN training/validation accuracy, binary | 99.23% training accuracy and 92.79% validation accuracy. |
| PAR-CNN training/validation accuracy, multi-class | 98.70% training accuracy and 84.52% validation accuracy. |
| Classifier comparison after NRMI features | SVM gives the best accuracy among Decision Tree, SVM, KNN, Boosted Trees, Bagged Trees, Subspace KNN, Subspace Discriminant, and RUSBoosted Trees: 97.9% binary and 94.5% multi-class accuracy. |
| Binary classification, PAR-CNN softmax | 92.44% accuracy. |
| Binary classification, PAR-CNN + SVM | 95.52% accuracy. |
| Binary classification, PAR-CNN + NRMI + SVM | 97.90% accuracy. |
| Multi-class classification, PAR-CNN softmax | 84.50% accuracy. |
| Multi-class classification, PAR-CNN + SVM | 89.70% accuracy. |
| Multi-class classification, PAR-CNN + NRMI + SVM | 94.50% accuracy. |
| NEU-CLS test | 99.72% classification accuracy. |

### Ablations

| Comparison | Source-backed finding |
|---|---|
| Attention/residual strategy | A-CNN improves over CNN, R-CNN improves over A-CNN, and PAR-CNN improves over R-CNN for both binary and multi-class classification. |
| Feature selection | NRMI improves binary accuracy by 1.8 points over NCA and 1.2 points over ReliefF; it improves multi-class accuracy by 1.8 points over NCA and 1.0 point over ReliefF. |
| SVM versus softmax | Replacing softmax with SVM improves binary accuracy by 3.08 points and multi-class accuracy by 5.2 points before NRMI selection. |

## ML/DL Extraction

| Field | Extracted detail |
|---|---|
| Task formulation | Binary defect detection and multi-class defect classification. |
| Architecture | PAR-CNN with six residual blocks and a parallel attention structure. |
| Feature layer | 500 deep features from fully connected layer `fc4`. |
| Feature selection | NRMI selects 100 binary-classification features and 66 multi-class features. |
| Classifier | Polynomial-kernel SVM. |
| Preprocessing | Severstal images resized from 1600 x 256 to 200 x 32. |
| Metrics | Accuracy, sensitivity, specificity, precision, and F-score. |
| Code | not reported. |
| Dataset availability | [[Severstal Steel Defect Dataset]] is a public Kaggle dataset. |

## Limitations

- The paper states that PAR-CNN uses only six residual blocks because seven caused out-of-memory errors on the available hardware.
- Input images are downsampled to 200 x 32, which reduces hardware requirements but may discard fine spatial detail.
- The authors state that it is not correct to claim absolute superiority over all compared methods because training parameters differ across studies.
- Future work is to try deeper network models and higher-dimensional input data.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]]
- Methods: [[Parallel attention-residual CNN]], [[NCA-ReliefF Matched Index feature selection]], [[Support vector machine]]
- Datasets: [[Severstal Steel Defect Dataset]], [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F-measure]]

### Shares Dataset

- [[Severstal Steel Defect Dataset]]: the main benchmark dataset for binary and multi-class steel surface defect classification.

### Shares Task

- [[Defect classification]]: the paper evaluates binary and multi-class image-level classification.

### Shares Method

- [[Parallel attention-residual CNN]]: the paper's proposed neural feature extractor.
- [[NCA-ReliefF Matched Index feature selection]]: the paper's proposed feature-selection algorithm.
- [[Support vector machine]]: used as the final classifier over PAR-CNN deep features.

### Application/Domain

- [[Metal inspection]]: the paper targets steel surface quality inspection.

### Shares Metric

- [[Accuracy]], [[Precision]], [[Recall]], and [[F-measure]]: used to report classification performance.

## Questions

- Would the reported gains hold with the original 1600 x 256 image resolution rather than 200 x 32 resized inputs?
- How sensitive is NRMI to the fixed top-200 feature matching choice?
- Would the PAR-CNN + NRMI + SVM pipeline still outperform end-to-end fine-tuned CNN classifiers under matched training conditions?
