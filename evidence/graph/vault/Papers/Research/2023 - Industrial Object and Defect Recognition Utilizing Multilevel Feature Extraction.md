---
title: "Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction from Industrial Scenes with Deep Learning Approach"
aliases:
  - "Industrial object and defect recognition utilizing multilevel feature extraction"
paper_key: "doi:10.1007/s12652-021-03688-7"
paper_type: research
year: 2023
venue: "Journal of Ambient Intelligence and Humanized Computing"
authors:
  - "Ioannis D. Apostolopoulos"
  - "Mpesiana A. Tzani"
status: processed
processed_at: 2026-05-20
topics:
  - industrial object recognition
  - defect recognition
  - multilevel feature extraction
tasks:
  - "[[Industrial object recognition]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[Six public industrial image datasets]]"
methods:
  - "[[Multipath VGG19]]"
  - "[[VGG19]]"
  - "[[Transfer learning]]"
  - "[[Data augmentation]]"
architectures:
  - "[[Multipath VGG19]]"
  - "[[VGG19]]"
optimizers:
  - "[[Adam]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[AU-ROC|AUC]]"
primary_metric: "[[Accuracy]]"
baselines:
  - "[[VGG19]]"
  - "Xception"
  - "ResNet-152"
  - "InceptionV3"
  - "MobileNetV2"
  - "DenseNet-169"
  - "EfficientNet-B0"
evaluation_protocol: "tenfold cross-validation; metrics averaged over ten independent train-test phases"
hardware: "Intel Core i5-9400F CPU at 2.90 GHz, 6 GB RAM, GeForce RTX 2060 Super"
doi: "10.1007/s12652-021-03688-7"
url: "https://doi.org/10.1007/s12652-021-03688-7"
related_methods:
  - "[[Multipath VGG19]]"
  - "[[VGG19]]"
  - "[[Adam]]"
related_datasets:
  - "[[Six public industrial image datasets]]"
related_tasks:
  - "[[Industrial object recognition]]"
  - "[[Defect classification]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Apostolopoulos - Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction from Industrial Scenes with Deep Learning....md"
extracted_text: "paper-inbox/90_processing/text/2023 - Apostolopoulos - Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction from Industrial Scenes with Deep Learning....txt"
pdf: "paper-inbox/10_processed/Research/2023 - Apostolopoulos - Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction from Industrial Scenes with Deep Learning....pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Apostolopoulos - Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction from Industrial Scenes with Deep Learning....pdf"
tags:
  - paper
  - industrial-vision
  - classification
---

# Industrial Object and Defect Recognition Utilizing Multilevel Feature Extraction

## Summary

- Proposes [[Multipath VGG19]], a VGG19-based CNN that concatenates early and late feature paths for industrial object and defect recognition.
- Evaluates the model on six public industrial-related image datasets covering defected materials, industrial tools, machine parts, bridges, and solar cell defects.
- Reports top classification performance on five of six datasets and an average classification improvement of 6.95% over baseline VGG19.

## Paper Type

Research paper. It contributes a model architecture modification and evaluates it across multiple classification datasets.

## Contribution

- Claimed: Multilevel feature extraction helps a VGG-style model recognize industrial objects and defects across varied datasets.
- Shown: MVGG19 fuses outputs from extra paths after VGG19 convolutional blocks and reports top accuracy on five of six datasets compared with baseline VGG19.
- Shown: The evaluation uses tenfold cross-validation, with each fold using a different held-out test partition and reporting mean metrics across the ten phases.
- Claimed: MVGG19 is intended as a general industrial image classification model for manufacturing and transport settings.

## Method

Multipath VGG19 keeps the VGG19-style convolutional hierarchy but adds processing paths after the second, third, and fourth max-pooling layers. Each branch uses batch normalization, 50% dropout, and global average pooling to reduce intermediate feature maps to one-dimensional feature vectors. The branch outputs and the final sequential output are concatenated and fed into a 2500-neuron classifier with a softmax output layer.

The model uses ImageNet-initialized VGG19 weights and fine-tunes only the final convolution layer while freezing the remaining layers. Training uses Adam with default parameters. The paper applies data augmentation only to training sets: random Gaussian noise, random rotations, horizontal and vertical flips, and height and width shifts via Keras ImageDataGenerator.

## Datasets

| Dataset | Source description | Images | Classes | Notes |
|---|---:|---:|---:|---|
| Casting | Kaggle casting manufacturing product images | 8,648 | 2 | Top views of submersible pump impellers; defective vs normal. |
| Defect / GC10-DET | Metallic surface defect images | 2,306 | 10 | Punching, weld line, crescent gap, water spot, oil spot, silk spot, inclusion, rolled pit, crease, waist folding. |
| Magnetic tile | Magnetic tile defect images | 1,243 | 6 | Six common magnetic tile defect classes with segmentation annotations. |
| Tech / MVTec ITODD subset | Industrial 3D object detection dataset subset | 2,349 | 27 | Ten selected industrial object types; source dataset supports 2D/3D detection and pose estimation. |
| Bridge / SDNET2018 | Concrete bridge, deck, wall, and pavement crack images | 54,999 | 2 | Cracked vs ok; includes shadows, roughness, scaling, edges, holes, and debris. |
| Solar Cell defect / ELPV | Electroluminescence photovoltaic cell images | 2,624 | 2 | Functional vs defective; defect class derived from annotation degree above zero. |

## Evidence

| Evidence | Reported detail |
|---|---|
| Evaluation protocol | Tenfold cross-validation; metrics are fold means. |
| Datasets | Casting, Defect, Magnetic Tile, Tech, Bridge, Solar Cell defect / ELPV. |
| Reported metrics | Accuracy, precision, recall, F1, AUC. |
| Strongest MVGG19 accuracy | 99.02% on Bridge. |
| Weakest MVGG19 accuracy | 76.78% on Solar Cell defect / ELPV. |
| Baseline VGG19 comparison | MVGG19 outperforms VGG19 on all six datasets in the reported table. |
| Other CNN comparison | MVGG19 ranks first on four of six datasets and second on the other two against Xception, ResNet-152, InceptionV3, MobileNetV2, DenseNet-169, and EfficientNet-B0. |
| Average improvement claim | The abstract reports 6.95% average classification improvement over baseline VGG19. |

## Performance Metrics

Primary metric: [[Accuracy]], with [[AU-ROC|AUC]], [[Precision]], [[Recall]], and [[F1-score]] as secondary metrics where reported.

| Dataset | MVGG19 accuracy | MVGG19 precision | MVGG19 recall | MVGG19 F1 | MVGG19 AUC | VGG19 accuracy | VGG19 AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Casting | 97.88% | 96.49% | 98.57% | 97.50% | 99.59% | 87.39% | 97.88% |
| Defect / GC10-DET | 77.62% | 77.68% | not recorded | not recorded | 94.94% | 70.90% | 92.65% |
| Magnetic Tile | 92.67% | 98.49% | not recorded | not recorded | 97.61% | 77.32% | 89.16% |
| Tech / MVTec ITODD subset | 94.23% | 98.13% | not recorded | not recorded | 99.94% | 88.29% | 99.60% |
| Bridge / SDNET2018 | 99.02% | 99.50% | 99.36% | 99.43% | 99.83% | 98.72% | 99.55% |
| Solar Cell defect / ELPV | 76.78% | 75.63% | 67.02% | 70.93% | 83.36% | 73.85% | 80.18% |

Recall and F1 are not recorded for the Defect, Magnetic Tile, and Tech datasets because those experiments use several classes.

## Reproducibility and Artifacts

- Code: the paper states that source code for constructing MVGG19 is provided in a GitHub repository, but the extracted source text does not include the repository URL.
- Data: the paper lists public repositories for all six datasets, including Kaggle for Casting, GitHub repositories for GC10-DET, Magnetic Tile, and ELPV, MVTec for ITODD, and Utah State University Libraries for SDNET2018.
- Environment: Python with Keras.
- Hardware: Intel Core i5-9400F CPU at 2.90 GHz, 6 GB RAM, and GeForce RTX 2060 Super.
- Training schedule: batch size depends on dataset size with a typical value of 64; epochs depend on dataset with a typical range of 30-60.

## Limitations

- The paper reports imbalance between defect-material datasets and object-recognition datasets.
- The Defect and Solar datasets remain challenging: the paper attributes Defect difficulty to many classes with few images per class and visually subtle class differences, while Solar has low accuracy and AUC relative to the other datasets.
- The paper does not report statistical significance tests or uncertainty intervals beyond cross-validation means.
- The extracted source text does not include the exact GitHub URL for the MVGG19 code, even though the paper states that source code is provided.

## Connections

### Graph Hubs

- Tasks: [[Industrial object recognition]], [[Defect classification]]
- Methods: [[Multipath VGG19]], [[VGG19]], [[Transfer learning]], [[Data augmentation]], [[Adam]]
- Datasets: [[Six public industrial image datasets]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]], [[AU-ROC|AUC]]
- Domains: [[Multi-industry anomaly detection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods]] | Shares method family | Both discuss image-based deep learning for industrial defect recognition, but this paper contributes and tests a CNN architecture while the textile paper is a review. |
| [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] | Shares dataset family | This paper's Tech experiment uses an industrial tool/object recognition dataset, while the 2021 dataset paper focuses on industrial machine tool component surface defects. |

## Questions

- What are the exact source papers or licenses for each of the six datasets?
- Are the supplementary results needed to preserve per-dataset confusion matrices?
