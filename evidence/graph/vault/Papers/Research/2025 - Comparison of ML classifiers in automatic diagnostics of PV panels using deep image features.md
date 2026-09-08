---
title: "Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features"
aliases:
  - "Comparison of ML classifiers in automatic diagnostics of PV panels"
paper_key: "sha256:db962ff1b9e352c5568ab951a19ab0605ee603fbebedfb4d16cbe78d4c2cc3cb"
paper_type: "research"
year: 2025
venue: "Przeglad Elektrotechniczny"
authors:
  - "Alicja Lenarczyk"
status: "processed"
topics:
  - "photovoltaic panel diagnostics"
  - "deep image features"
  - "hybrid CNN classifier"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PV Panel Defect Dataset]]"
methods:
  - "[[ResNet-18]]"
  - "[[MobileNet]]"
  - "[[Support vector machine]]"
  - "[[Random forest]]"
  - "[[XGBoost]]"
  - "[[LIME]]"
model_family:
  - "[[Computer Vision Models]]"
  - "[[Classical ML]]"
architectures:
  - "[[ResNet-18]]"
  - "[[MobileNet]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Accuracy, macro precision, macro recall, and macro F1-score are reported for model comparison."
baselines:
  - "SVM on RGB color histograms"
  - "Random Forest on RGB color histograms"
  - "GridSearch Random Forest"
  - "XGBoost on ResNet18 features with PCA"
  - "Keras CNN"
benchmarks:
  - "[[PV Panel Defect Dataset]]"
code: "not reported"
data: "https://www.kaggle.com/datasets/alicjalena/pv-panel-defect-dataset"
doi: "10.15199/48.2025.10.25"
arxiv: "not reported"
url: "https://doi.org/10.15199/48.2025.10.25"
pdf: "paper-inbox/10_processed/Research/2025 - Lenarczyk - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features.pdf"
source_file: "paper-inbox/10_processed/Research/2025 - Lenarczyk - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Lenarczyk - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Lenarczyk - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features.txt"
related_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
  - "[[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]]"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[ResNet-18]]"
  - "[[MobileNet]]"
  - "[[Support vector machine]]"
  - "[[Random forest]]"
  - "[[XGBoost]]"
  - "[[LIME]]"
related_datasets:
  - "[[PV Panel Defect Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[PV Panel Defect Dataset]]"
processed_at: "2026-06-04"
---
# Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features

## Summary

The paper introduces and evaluates [[PV Panel Defect Dataset]], a 1,574-image RGB dataset for photovoltaic panel condition classification. It compares classical ML classifiers, a Keras CNN, and a hybrid CNN + SVM pipeline that uses [[ResNet-18]] for feature extraction and [[Support vector machine]] for final classification.

The best model is the hybrid CNN + SVM, which reports 0.9545 accuracy and 0.9553 macro-F1 on the model comparison table. The study argues that the hybrid design keeps strong classification performance while reducing deployment complexity for resource-constrained PV inspection settings.

## Paper Type

Research paper with a dataset contribution. It introduces the curated PV panel dataset and benchmarks ML/DL classifiers for six-class RGB photovoltaic panel diagnostics.

## Problem

PV systems need scalable visual monitoring because manual inspection is expensive and hard to scale across large installations. The paper targets automatic RGB-image classification of panel states including environmental contamination, electrical damage, physical damage, and clean panels.

## Contribution

- Introduces [[PV Panel Defect Dataset]], a 1,574-image six-class RGB dataset with train, validation, and test partitions.
- Compares classical ML, deep CNN, and hybrid CNN + classical classifier pipelines under a common evaluation protocol.
- Shows that [[ResNet-18]] feature extraction plus [[Support vector machine]] classification slightly outperforms the end-to-end Keras CNN in the reported comparison.
- Uses [[LIME]] to interpret a hybrid CNN + SVM prediction and check whether the model focuses on panel-surface evidence for a Bird-drop example.

## Method

The dataset contains RGB images of photovoltaic panels in six classes: Bird-drop, Clean, Dusty, Electrical-damage, Physical-damage, and Snow-covered. The paper reports 929 training images, 550 validation images, and 95 test images. The dataset was curated from publicly available sources, with manual inspection and class balancing.

For raw-image models, preprocessing resizes images to 224 x 224 pixels, normalizes inputs to the `[0,1]` range, and applies training-only augmentation: random rotation of +/-15 degrees, horizontal flipping, and brightness/contrast adjustment of +/-20%. Augmentation is applied on the fly and does not increase the dataset size.

The compared approaches are:

- [[Support vector machine]] and [[Random forest]] trained on RGB color histograms.
- GridSearch Random Forest.
- [[XGBoost]] trained on [[ResNet-18]] features with PCA.
- Keras CNN using [[MobileNet]]V3 transfer learning.
- Hybrid CNN + SVM using [[ResNet-18]] feature extraction and SVM classification.

## Evidence

### Dataset

| Class | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| Bird-drop | 177 | 104 | 17 | 298 |
| Clean | 169 | 102 | 18 | 289 |
| Dusty | 162 | 97 | 16 | 275 |
| Electrical-damage | 135 | 77 | 13 | 225 |
| Physical-damage | 132 | 78 | 15 | 225 |
| Snow-covered | 154 | 92 | 16 | 262 |
| Total | 929 | 550 | 95 | 1574 |

### Model Comparison

| Model | Accuracy | Macro precision | Macro recall | Macro F1 |
|---|---:|---:|---:|---:|
| SVM | 0.9200 | 0.9225 | 0.9200 | 0.9210 |
| Random Forest | 0.9418 | 0.9463 | 0.9423 | 0.9438 |
| RF GridSearch | 0.9491 | 0.9520 | 0.9490 | 0.9502 |
| XGBoost | 0.7327 | 0.7516 | 0.7271 | 0.7281 |
| Keras CNN | 0.9527 | 0.9555 | 0.9541 | 0.9546 |
| CNN + SVM | 0.9545 | 0.9578 | 0.9536 | 0.9553 |

The paper identifies CNN + SVM as the best variant by macro-F1 and accuracy. It reports ideal precision, recall, and F1-score for Physical-damage and Snow-covered in the per-class test results, F1 = 0.96 for Electrical-damage, and lower performance for Bird-drop, Clean, and Dusty where single errors occur.

### Explainability

The paper applies [[LIME]] to a Bird-drop example from the CNN + SVM model. The interpretation highlights image regions corresponding to visible spots and streaks on the panel, while background and panel frames are reported as ignored in that example.

## ML/DL Extraction

- Task formulation: six-class RGB photovoltaic panel condition classification.
- Inputs: RGB images from [[PV Panel Defect Dataset]].
- Outputs: Bird-drop, Clean, Dusty, Electrical-damage, Physical-damage, or Snow-covered.
- Feature extraction: [[ResNet-18]] for the hybrid CNN + SVM and XGBoost feature pipeline; [[MobileNet]]V3 in the Keras CNN pipeline.
- Classical classifiers: [[Support vector machine]], [[Random forest]], GridSearch Random Forest, and [[XGBoost]].
- Training data: 929 training images; training-only augmentation with rotation, horizontal flip, and brightness/contrast changes.
- Validation/test: 550 validation images and 95 independent test images.
- Evaluation metrics: [[Accuracy]], [[Precision]], [[Recall]], and [[F1-score]], plus confusion matrices and learning curves.
- Explainability: [[LIME]] for image-level interpretation of a CNN + SVM prediction.
- Artifacts: dataset URL is reported; code, trained weights, hardware, training time, and seeds are not reported.

## Limitations

- The dataset is relatively small, especially for fine-grained defect classes.
- Background elements such as vegetation and sky may introduce spurious correlations, and the paper cannot fully exclude their influence.
- Dusty and Clean panels are harder to separate because the visual differences are subtle and low contrast.
- The validation split is larger than usual because it is used for hyperparameter monitoring across multiple classifiers; the independent test split contains only 95 images.
- Future work is needed for larger datasets, cropped or segmented panel images, deeper fine-tuned architectures, and deployment tests on edge hardware.

## Connections

### Graph Hubs

- Datasets: [[PV Panel Defect Dataset]]
- Source subset: pythonafroz Kaggle solar-panel-images.
- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Domains: [[Solar cells and photovoltaic]]
- Methods: [[ResNet-18]], [[MobileNet]], [[Support vector machine]], [[Random forest]], [[XGBoost]], [[LIME]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Introduces Dataset

- [[PV Panel Defect Dataset]]: the paper defines the 1,574-image six-class PV panel dataset and reports its class-level train, validation, and test counts.

### Shares Dataset

- Source subset: the paper cites the pythonafroz Kaggle solar-panel-images data as a public source used for dataset curation.
- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] also studies [[PV Panel Defect Dataset]], but with an 875-image selected subset and an explainability-focused audit.

### Shares Task

- [[Solar cell defect detection]]: the study classifies RGB photovoltaic panel visual conditions and defects.
- [[Defect classification]]: the model predicts one of six defect or condition classes.

### Shares Method

- [[ResNet-18]]: used as the deep feature extractor in the hybrid CNN + SVM pipeline.
- [[Support vector machine]]: used as the final classifier in the best reported model.
- [[Random forest]] and [[XGBoost]]: evaluated as classical ML baselines.
- [[MobileNet]]: used in the Keras CNN transfer-learning baseline.
- [[LIME]]: used to interpret a Bird-drop prediction from the hybrid model.

### Follow-up Reading

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] is the closest follow-up because it tests shortcut-learning risk on the same dataset.
- [[2026 - IncepViTH-Net for Solar Panel Fault Detection and Classification]] evaluates related solar-panel fault classification with a hybrid deep architecture.

## Questions

- Would the reported CNN + SVM ranking hold under cross-site data collection or panel-only cropping?
- How much of the model performance depends on background context rather than panel-surface evidence?
- Would segmentation masks or object-level panel crops reduce the Dusty/Clean confusion?
- Are the dataset files versioned so later Kaggle changes can be matched to the paper's 1,574-image split?
