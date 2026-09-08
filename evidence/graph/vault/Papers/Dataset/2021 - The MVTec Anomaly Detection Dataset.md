---
title: "The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection"
aliases:
  - "The MVTec Anomaly Detection Dataset"
paper_key: "doi:10.1007/s11263-020-01400-4"
paper_type: dataset
year: 2021
venue: "International Journal of Computer Vision"
authors:
  - "Paul Bergmann"
  - "Kilian Batzner"
  - "Michael Fauser"
  - "David Sattlegger"
  - "Carsten Steger"
status: processed
processed_at: 2026-05-20
topics:
  - anomaly detection
  - unsupervised anomaly detection
  - defect segmentation
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
methods:
  - "convolutional autoencoders"
  - "[[GAN]]"
  - "pretrained CNN feature descriptors"
  - "student-teacher anomaly detection"
  - "variation model"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
  - "[[IoU]]"
primary_metric: "[[AU-PRO]]"
metric_definitions:
  - "AU-PR, AU-ROC, AU-PRO, and AU-IoU are compared as threshold-independent anomaly-segmentation metrics."
  - "PRO averages true-positive overlap over connected ground-truth anomaly regions."
  - "IoU is computed for the anomalous class from thresholded anomaly predictions."
baselines:
  - "f-AnoGAN"
  - "CNN Feature Dictionary"
  - "Student-Teacher anomaly detection"
  - "L2 autoencoder"
  - "SSIM autoencoder"
  - "GMM-based Texture Inspection"
  - "Variation Model"
data: "reported available: https://www.mvtec.com/company/research/datasets"
artifact_status: "dataset reported available"
doi: "10.1007/s11263-020-01400-4"
url: "https://doi.org/10.1007/s11263-020-01400-4"
related_concepts:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
related_datasets:
  - "[[MVTec AD]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Bergmann - The MVTec Anomaly Detection Dataset A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Bergmann - The MVTec Anomaly Detection Dataset A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection.txt"
pdf: "paper-inbox/10_processed/2021 - Bergmann - The MVTec Anomaly Detection Dataset A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection.pdf"
source_file: "paper-inbox/10_processed/2021 - Bergmann - The MVTec Anomaly Detection Dataset A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection.pdf"
tags:
  - paper
  - dataset
  - anomaly-detection
---

# The MVTec Anomaly Detection Dataset

## Summary

- Introduces [[MVTec AD]], a real-world industrial anomaly detection dataset with 5,354 high-resolution color images across object and texture categories.
- The dataset uses normal images for training and anomalous plus defect-free images for testing, with pixel-precise anomaly annotations.
- The paper benchmarks unsupervised anomaly detection methods and reports that pretrained network feature descriptors outperform the evaluated autoencoder, GAN, and classical methods.
- It also analyzes threshold-independent metrics, threshold estimation from anomaly-free validation data, and inference-time/memory trade-offs for the benchmarked methods.

## Paper Type

Dataset paper. The central contribution is a public benchmark dataset and its evaluation protocol.

## Contribution

- Claimed: MVTec AD fills a gap for large-scale, high-resolution, real-world unsupervised anomaly detection data.
- Shown: The dataset contains 15 categories, 3,629 training images, 1,725 test images, over 70 defect types, and 1,888 annotated anomalous regions.
- Shown: Only 2.7% of test pixels are anomalous, so the paper discusses threshold-independent and false-positive-sensitive metrics.

## Method

The paper constructs a one-class training setup where training images are defect-free and test images contain both normal and anomalous examples. It evaluates convolutional autoencoders, GAN-based approaches, pretrained CNN feature descriptors, a student-teacher descriptor-regression method, a GMM-based texture inspection model, and a variation model.

The dataset contains five texture categories and ten object categories. Textures include regular and random surfaces, while object categories include rigid, deformable, naturally variable, aligned, and randomly rotated objects. Images were acquired with a high-resolution industrial RGB sensor and bilateral telecentric lenses, then cropped to output sizes between 700 x 700 and 1024 x 1024 pixels. Three categories, grid, screw, and zipper, are provided as grayscale images.

Defects were manually generated to resemble real industrial inspection anomalies. The authors annotate all defective image regions pixel-precisely, including deformed regions and expected locations for missing parts when the defect is an absence.

## Evidence

| Evidence | Reported detail |
|---|---|
| Dataset size | 5,354 images; 3,629 training and 1,725 testing |
| Annotation | Pixel-precise ground truth for all anomalies |
| Categories | 15 object and texture categories |
| Anomaly types | More than 70 defect types |
| Metric concern | Test pixels are highly imbalanced, with 2.7% anomalous pixels |

### Dataset Statistics

| Category | Type | Train | Test good | Test defective | Defect groups | Defect regions | Image side length |
|---|---|---:|---:|---:|---:|---:|---:|
| Carpet | texture | 280 | 28 | 89 | 5 | 97 | 1024 |
| Grid | texture | 264 | 21 | 57 | 5 | 170 | 1024 |
| Leather | texture | 245 | 32 | 92 | 5 | 99 | 1024 |
| Tile | texture | 230 | 33 | 84 | 5 | 86 | 840 |
| Wood | texture | 247 | 19 | 60 | 5 | 168 | 1024 |
| Bottle | object | 209 | 20 | 63 | 3 | 68 | 900 |
| Cable | object | 224 | 58 | 92 | 8 | 151 | 1024 |
| Capsule | object | 219 | 23 | 109 | 5 | 114 | 1000 |
| Hazelnut | object | 391 | 40 | 70 | 4 | 136 | 1024 |
| Metal nut | object | 220 | 22 | 93 | 4 | 132 | 700 |
| Pill | object | 267 | 26 | 141 | 7 | 245 | 800 |
| Screw | object, grayscale | 320 | 41 | 119 | 5 | 135 | 1024 |
| Toothbrush | object | 60 | 12 | 30 | 1 | 66 | 1024 |
| Transistor | object | 213 | 60 | 40 | 4 | 44 | 1024 |
| Zipper | object, grayscale | 240 | 32 | 119 | 7 | 177 | 1024 |
| Total | mixed | 3629 | 467 | 1258 | 73 | 1888 | mixed |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | anomaly segmentation curves | area under FPR-vs-TPR curve, normalized to FPR 0.3 unless otherwise stated | higher | no | Mean student-teacher AU-ROC is 0.922, best among evaluated methods. |
| [[AU-PRO]] | region-level anomaly segmentation | area under FPR-vs-PRO curve, normalized to FPR 0.3 unless otherwise stated | higher | yes | Mean student-teacher AU-PRO is 0.924, best among evaluated methods. |
| [[IoU]] | thresholded anomalous-pixel segmentation | intersection over union for the anomalous class | higher | no | Mean student-teacher AU-IoU is 0.190, best among evaluated methods. |
| AU-PR | anomaly segmentation under class imbalance | area under precision-recall curve | higher | no | Mean student-teacher AU-PR is 0.599, best among evaluated methods. |

### Benchmark Results

| Result | Dataset / Task | Metric | Direction | Paper result | Notes |
|---|---|---|---|---:|---|
| Best mean AU-PR | [[MVTec AD]] / anomaly segmentation | AU-PR | higher | 0.599 | Student-teacher anomaly detection. |
| Best mean AU-ROC | [[MVTec AD]] / anomaly segmentation | [[AU-ROC]] at FPR 0.3 | higher | 0.922 | Student-teacher anomaly detection. |
| Best mean AU-PRO | [[MVTec AD]] / anomaly segmentation | [[AU-PRO]] at FPR 0.3 | higher | 0.924 | Student-teacher anomaly detection. |
| Best mean AU-IoU | [[MVTec AD]] / anomaly segmentation | AU-IoU at FPR 0.3 | higher | 0.190 | Student-teacher anomaly detection. |

- Student-teacher anomaly detection ranks first across AU-PR, AU-ROC, AU-PRO, AU-IoU, and the reported AU-PRO integration variants.
- CNN Feature Dictionary ranks second for AU-PR, AU-ROC, AU-PRO at FPR 0.3, AU-IoU, and full AU-PRO, but drops under very low-FPR AU-PRO.
- f-AnoGAN ranks last for the main threshold-independent metrics in Table 3.
- The paper warns that changing the AU-PRO integration limit can change method rankings, so the false-positive-rate range must match application requirements.

## Limitations

- The paper notes threshold choice is challenging because anomalous samples are unavailable during training.
- Large class imbalance means high false-positive rates can make thresholded segmentation unusable even when area-under-curve metrics look strong.
- Threshold estimators based only on anomaly-free validation images vary substantially by method and category; conservative thresholds may miss anomalies, while permissive thresholds can create too many false positives.
- Evaluation is centered on controlled industrial image acquisition, so transfer to uncontrolled factory conditions is not established by the paper.

## Reproducibility

- Data: publicly available at https://www.mvtec.com/company/research/datasets.
- Code: f-AnoGAN uses the original public GitHub implementation; HALCON implementations are used for the texture inspection model and variation model; full benchmark code availability is not reported.
- Training details: f-AnoGAN uses latent dimension 128, 100 GAN epochs, Adam learning rate 1e-4, encoder training for 50,000 iterations with RMSProp learning rate 5e-5, and batch size 64.
- Autoencoders: L2 and SSIM autoencoders use latent dimension 128, train for 100 epochs with Adam learning rate 2e-4 and batch size 128.
- Student-teacher: uses three ImageNet-pretrained teacher networks and three student networks per teacher, trained for 100 epochs with Adam learning rate 1e-4 and batch size 1.
- Seeds: not reported.
- Environment: HALCON is named for classical-method implementations; exact software/hardware environment is not reported.

## Systems Details

- f-AnoGAN and patch-based Feature Dictionary require multiple or patch-wise evaluations and are slow relative to single-forward-pass methods.
- CNN Feature Dictionary can take several seconds per image because it evaluates patches and produces one anomaly score per patch.
- Autoencoders can run in a few milliseconds for object images when evaluated in a single forward pass, but texture evaluation with strides takes hundreds of milliseconds.
- Student-teacher inference requires multiple teacher and student forward passes and is reported as several hundreds of milliseconds per image.
- Parameter counts: f-AnoGAN 24.57M, Feature Dictionary 11.46M, Student-Teacher 26.07M, L2 autoencoder 1.20M, and SSIM autoencoder 1.20M.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect segmentation]]
- Datasets: [[MVTec AD]]
- Methods: [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]]
- Metrics: [[AU-ROC]], [[AU-PRO]], [[IoU]]
- Domains: [[Multi-industry anomaly detection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects]] | Benchmark source | Uses MVTec AD texture categories to evaluate an unsupervised inspection method. |
| [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] | Benchmark source | Uses MVTec2D/MVTec AD for anomaly localization evaluation. |
| [[2021 - The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization]] | Follow-up dataset family | Extends the MVTec anomaly-detection benchmark family from 2D RGB inspection images to 3D scans. |

## Questions

- Which MVTec categories are most relevant for the vault's target industrial domains?
- Should the vault split [[MVTec AD]] into object and texture benchmark notes later?
