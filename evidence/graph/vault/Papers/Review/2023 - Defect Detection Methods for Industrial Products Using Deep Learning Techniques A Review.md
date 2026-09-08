---
title: "Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review"
aliases:
  - "Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review"
  - "Defect Detection Methods for Industrial Products Using Deep Learning Techniques: A Review"
paper_key: "doi:10.3390/a16020095"
paper_type: review
year: 2023
venue: "Algorithms"
authors:
  - "Alireza Saberironaghi"
  - "Jing Ren"
  - "Moustafa El-Gindy"
status: processed
processed_at: 2026-05-21
topics:
  - industrial defect detection
  - surface defect detection
  - X-ray defect detection
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Industrial visual inspection]]"
datasets:
  - "not applicable"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
  - "[[GAN]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[Deep convolutional neural network]]"
  - "[[GAN]]"
  - "[[Variational Autoencoder]]"
learning_paradigms:
  - "[[Supervised learning]]"
  - "[[Semi-supervised learning]]"
  - "[[Unsupervised learning]]"
metrics:
  - "[[Accuracy]]"
  - "[[mAP]]"
  - "[[AU-ROC]]"
primary_metric: "not applicable"
benchmarks:
  - "not applicable"
code: "not reported"
data: "source lists corresponding dataset websites"
doi: "10.3390/a16020095"
arxiv: "not reported"
url: "https://doi.org/10.3390/a16020095"
pdf: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
  - "[[GAN]]"
  - "[[Unsupervised anomaly detection]]"
related_datasets:
  - "not applicable"
related_domains:
  - "[[Industrial visual inspection]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/Review/2023 - Saberironaghi - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Saberironaghi - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Saberironaghi - Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review.txt"
artifact_status: "source lists dataset websites"
tags:
  - paper
---

# Defect Detection Methods for Industrial Products Using Deep Learning Techniques A Review

## Summary

This review surveys deep-learning methods for detecting defects in industrial products, with separate coverage for surface defect detection and X-ray image defect detection. It organizes learning-based surface inspection into supervised, unsupervised, and semi-supervised approaches, then discusses common problems: unbalanced samples, small sample size, and real-time processing.

The paper contrasts traditional feature-based methods with deep learning. Traditional methods can work when defect color, texture, or shape differences are stable, but they are less adaptable to complex backgrounds, noise, lighting changes, and varied defect intensity, shape, and size. Deep learning is presented as a response to these limits, but it creates its own needs for data, computation, transfer, explainability, and common reference datasets.

## Paper Type

- Type: review.
- Why: The paper summarizes and analyzes defect-detection literature and datasets; it does not introduce a new detector or benchmark.

## Problem

- Task: industrial product defect detection using machine learning and deep learning.
- Main scope: surface defect detection on industrial products, plus defect detection in X-ray images.
- Traditional feature families: texture-based, color-based, and shape-based features.
- Deep-learning families: supervised, unsupervised, and semi-supervised learning.
- Motivation: human inspection is inefficient and subjective; traditional image processing struggles with complex textures, noise, and lighting changes.

## Contribution

- Summarizes machine-learning and deep-learning surface-defect detection methods for industrial products.
- Reviews deep-learning defect detection in X-ray images, including CNN, SVM, YOLOv5, Faster R-CNN, semantic segmentation, triplet networks, GANs, and ensemble models.
- Lists common public datasets and dataset websites for industrial surface defect detection.
- Summarizes challenges and candidate solutions for unbalanced samples, small defect samples, and real-time industrial detection.

## Method

- Review type: narrative review.
- Surface-defect method taxonomy: supervised, unsupervised, and semi-supervised.
- X-ray defect method taxonomy: deep-learning and classical ML methods applied to radiographic inspection.
- Dataset coverage: a table of common surface-defect datasets with targets and links.
- Problem/solution coverage: unbalanced samples, small samples, real-time processing, lighting variation, transparent AI, multimodal sensors, continuous learning, lightweight networks, and common reference databases.

## ML / DL Extraction

### Task Formulation

- Inputs: surface images, X-ray images, or industrial inspection images.
- Outputs: defect class, bounding box, segmentation mask, anomaly score, or defective/non-defective decision.
- Supervised setting: large labeled sets of defective and defect-free samples.
- Unsupervised setting: unlabeled or normal-only data, often using reconstruction or embedding similarity.
- Semi-supervised setting: combines normal samples, unlabeled data, weak labels, active learning, self-training, or synthetic samples.

### Model And Training

- Supervised examples: two-layer neural network, ShuffleNet, ShuffleDefectNet, shallow CNN, Faster R-CNN, cascaded R-CNN, MobileNet-SSD, FCN, and U-Net.
- Unsupervised examples: autoencoders, convolutional denoising autoencoders, GANs, SOM-based detection, PatchCore, PaDiM, SPADE, DBN, and FCAE.
- Semi-supervised examples: active learning plus self-training, CAE plus GAN, weakly supervised localization/decision networks, CDCGAN plus ResNet18, and residual networks.
- X-ray examples: three-stage deep learning algorithm, ten-layer CNN, SVM, YOLOv5-based DR-image detection, lightweight semantic segmentation, Faster R-CNN with FPN/RoIAlign, triplet deep neural network, unsupervised GAN, R-CNN, and stacked generalization ensembles.

### Data

- New dataset: not applicable.
- Data availability: the paper states that corresponding dataset websites are listed in the manuscript.
- Common surface-defect datasets listed: MVTec AD, Severstal Steel Defect Detection, GC10-Det, Industrial Metallic Surface Dataset, Bridge Cracks, Fabric defect dataset, DeepPCB, PCB Defects, PCB DSLR Dataset, SDNET2018, COncrete DEfect BRidge IMage Dataset, Surface Crack Detection Dataset, Pavement crack dataset, Cracks and Potholes in Road Images Dataset, Crack Forest, Tianchi aluminum profile surface defect dataset, solar cell EL image defect detection, ELPV, Magnetic Tile Surface Defects, Dataset for Rail Surface Defects Detection, and Railway Track Fault Detection.

### Evaluation

- The review does not evaluate a new model.
- It reports representative metrics from reviewed papers, including [[Accuracy]], [[mAP]], mIoU, L-mIoU, recall, precision, F-score, AUC, and [[AU-ROC]].

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | classification and detection examples | Percentage of correctly classified/detected cases | higher is better | no | Examples include ShuffleDefectNet at 99.75% on NEU and CNN X-ray welding recognition at 98.8%. |
| [[mAP]] | object detection examples | Mean average precision across classes or object instances | higher is better | no | Examples include 89.64% mAP for YOLOv5 on solar cell EL images and 75.8% mAP over Faster R-CNN in an aluminum-profile example. |
| mIoU / L-mIoU | segmentation examples | Intersection-over-union style overlap metrics | higher is better | no | The tire X-ray segmentation example reports 97.1% mIoU and 92.4% L-mIoU. |
| [[AU-ROC]] / AUC | anomaly detection examples | Area under ROC curve | higher is better | no | PatchCore reports over 99% AUROC on MVTec; a tire X-ray dataset example reports 0.873 AUC. |

## Evidence

### Traditional Feature-Based Methods

| Feature family | Example methods | Strengths | Limits |
|---|---|---|---|
| Texture-based | LBP, GLCM, RCCR, morphology, Gabor filters | Can be fast, robust to some texture variation, and effective for patterned defects | Limited when defects do not change texture or when new defect types differ from training assumptions |
| Color-based | color histograms, color moments, FSIFT combinations | Useful for color variations, stains, and discoloration | Sensitive to low contrast and may not adapt beyond color-change defects |
| Shape-based | Fourier transform, Hough transform, template matching | Useful for periodic patterns, linear features, cracks, scratches, and small defects | Limited to specific shapes/templates and less adaptable than learned models |

### Representative Surface-Defect Results

| Method | Target | Reported result |
|---|---|---|
| Multi-block LBP | surface defects | 63 ms/image and 94.30% recognition accuracy |
| Fuzzy GLCM model | ceramic defects | 96.87% training-data accuracy and 92.31% real-time-system accuracy |
| ShuffleDefectNet | NEU | 99.75% accuracy |
| PatchCore | MVTec/STC/MTD | over 99% AUROC on MVTec |
| GAN on solar panel dataset | solar panel defects | 93.75% accuracy |
| Weakly supervised PCBA method | PCBA manufacturing defects | 98% overall defect recognition accuracy |
| YOLOv3 PCB method | PCB defects | 92.13% mAP and 63 FPS |
| CNN rail method | rails | 98.2% image-level and 97.42% pixel-level detection |
| U-Net fabric method | fabric | 99% detection accuracy |
| CNN concrete cracks | concrete cracks | about 98% accuracy on 40,000 256 x 256 images |

### X-Ray Defect Detection Results

| Method | Target | Reported result |
|---|---|---|
| Three-stage deep learning algorithm | engines | above 90% accuracy |
| Ten-layer CNN | welding X-ray images | 98.8% classification accuracy with ReLU |
| SVM | welding | 99.4% accuracy in one example; about 99.1% detection rate in another |
| YOLOv5-based DR image detection | insert molding | 93.6% recognition accuracy |
| Lightweight semantic segmentation | tire X-ray images | 97.1% mIoU and 92.4% L-mIoU for 512 x 512 inputs |
| Faster R-CNN + FPN/RoIAlign | automobile aluminum casting parts | FPN increased mAP by 40.9%; RoIAlign improved bounding-box accuracy by 23.6% |
| Unsupervised GAN | tire X-ray dataset | 0.873 AUC |
| Stacked generalization ensemble | hard-metal production samples | recall 100%, precision 60%, F-score 75%, accuracy 88.24% |

## Review / Survey Details

- Scope: industrial product defect detection with deep learning, including surface images and X-ray/radiographic images.
- Publication status: Algorithms 2023, 16, 95; published 8 February 2023.
- License: CC BY 4.0.
- Data statement: corresponding websites are listed in the manuscript.
- Funding: Natural Sciences and Engineering Research Council of Canada (NSERC), grant 210471.

## Limitations

- Supervised methods need balanced labeled datasets, which are uncommon in real production because normal samples dominate and defective samples are scarce.
- Feature-based methods are less adaptable to complex backgrounds, low contrast, noise, and new defect types than deep learning methods.
- GAN and autoencoder methods can struggle when training data are small or poor quality.
- Semi-supervised methods can depend strongly on unlabeled-data quality and may not work well with intricate backgrounds.
- X-ray image methods can be limited to particular defect types or image domains and may have high false-positive rates because benign structures can resemble defects.
- Real-time industrial deployment requires reducing detection time while keeping accuracy roughly stable.
- Future work should address lighting variation, explainability, multimodal sensor fusion, continuous learning, lightweight networks, and common reference databases.

## Reproducibility

- Code: not reported.
- Data: source lists corresponding dataset websites.
- Search protocol: not reported as a systematic review protocol.
- Models/checkpoints: not applicable.
- Hyperparameters: not applicable to the review.
- Environment: not applicable.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]], [[Object detection]], [[Defect segmentation]]
- Methods: [[Deep convolutional neural network]], [[Data augmentation]], [[GAN]], [[Unsupervised anomaly detection]]
- Learning paradigms: [[Supervised learning]], [[Semi-supervised learning]], [[Unsupervised learning]]
- Domains: [[Industrial visual inspection]]
- Datasets: not applicable; the paper is a review and introduces no dataset
- Metrics: [[Accuracy]], [[mAP]], [[AU-ROC]]

### Builds On

- [[Deep convolutional neural network]]: the review treats CNNs and related deep-learning models as the main modern approach for industrial product defect detection.

### Contrasts With

- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]]: both review deep-learning inspection methods, but this paper explicitly includes X-ray defect detection and a problem/solution section on unbalanced samples, small samples, and real-time processing.
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]]: this paper is broader and includes X-ray images and traditional feature methods; the systematic review is more tightly scoped to supervised CNN image studies.

### Shares Dataset

- not applicable

### Shares Task

- [[Surface defect detection]]: the main surface-image review scope.
- [[Defect classification]]: many reviewed supervised methods classify defect type or defective/non-defective status.
- [[Object detection]]: Faster R-CNN, MobileNet-SSD, YOLOv3, YOLOv5, and Mask-style detectors recur in the reviewed studies.
- [[Defect segmentation]]: FCN, U-Net, lightweight semantic segmentation, and pixel-level methods are reviewed.

### Shares Method

- [[Deep convolutional neural network]]: central deep-learning family.
- [[Data augmentation]]: discussed as a solution for unbalanced and small defect samples.
- [[GAN]]: reviewed for unsupervised detection, image generation, and small-sample anomaly detection.
- [[Unsupervised anomaly detection]]: discussed through PatchCore, autoencoders, GANs, and normal-only detection settings.

### Shares Metric

- [[Accuracy]], [[mAP]], and [[AU-ROC]] appear in the representative reviewed results.

### Application / Domain

- [[Industrial visual inspection]]: the review covers industrial product surface inspection and X-ray/radiographic defect inspection.

### Follow-Up Reading

- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]]
- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]]

## Questions

- Should X-ray/radiographic industrial inspection become a separate domain note if more NDT papers are processed?
- Which dataset links from the review’s dataset table are already represented in the vault and which should be added only when supported by a dataset host or primary paper?
