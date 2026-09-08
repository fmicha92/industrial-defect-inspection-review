---
title: "Deep CNN-Based Visual Defect Detection Survey of Current Literature"
aliases:
  - "Deep CNN-Based Visual Defect Detection Survey of Current Literature"
  - "Deep CNN-based visual defect detection: Survey of current literature"
paper_key: "doi:10.1016/j.compind.2023.103911"
paper_type: review
year: 2023
venue: "Computers in Industry"
authors:
  - "Shashi Bhushan Jha"
  - "Radu F. Babiceanu"
status: processed
processed_at: 2026-05-21
topics:
  - automatic optical inspection
  - industrial defect detection
  - CNN survey
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
  - "[[U-Net]]"
  - "[[Unsupervised anomaly detection]]"
model_family:
  - "[[Deep convolutional neural network]]"
  - "[[GAN]]"
  - "[[Variational Autoencoder]]"
learning_paradigms:
  - "[[Unsupervised learning]]"
  - "[[Semi-supervised learning]]"
metrics:
  - "[[mAP]]"
  - "[[Dice score]]"
  - "[[Segmentation metrics]]"
primary_metric: "not applicable"
benchmarks:
  - "not applicable"
code: "not reported"
data: "not applicable; no data was used for the research described in the article"
doi: "10.1016/j.compind.2023.103911"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.compind.2023.103911"
pdf: "not reported"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
  - "[[GAN]]"
  - "[[U-Net]]"
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
source_file: "paper-inbox/10_processed/Review/2023 - Jha - Deep CNN-Based Visual Defect Detection Survey of Current Literature.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Jha - Deep CNN-Based Visual Defect Detection Survey of Current Literature.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Jha - Deep CNN-Based Visual Defect Detection Survey of Current Literature.txt"
artifact_status: "no research data used"
tags:
  - paper
---

# Deep CNN-Based Visual Defect Detection Survey of Current Literature

## Summary

This survey reviews deep CNN-based visual defect detection for automated industrial quality inspection. It frames defect inspection methods as manual inspection, traditional automatic optical inspection, and modern CNN-based automatic optical inspection, then organizes modern methods by dense versus sparse deep networks and by supervised, semi-supervised, and unsupervised learning.

The paper emphasizes that supervised CNNs are widely used for defect classification and segmentation, but they require large labeled datasets and pixel-level annotation for segmentation. It highlights unsupervised CNN approaches, including autoencoders and GAN-based methods, as a response to labeling and annotation costs, while noting that unsupervised localization remains less reliable than supervised methods.

## Paper Type

- Type: review.
- Why: The paper is a narrative survey of current literature on deep CNN-based visual defect detection and open challenges; it does not introduce a new model, dataset, or benchmark.

## Problem

- Task: visual defect detection for automated industrial quality control.
- Setting: automatic optical inspection of manufactured components, including internal radiographic inspection and external surface inspection.
- Inputs: images from production-line cameras, X-ray/radiographic images, or existing image datasets depending on the application.
- Outputs: defective/non-defective labels, defect classes, defect regions, bounding boxes, or pixel-level masks.
- Motivation: manual inspection is tedious, time-consuming, subjective, and labor-intensive; traditional AOI reduces some labor but depends on expert-designed features and controlled conditions.

## Contribution

- Surveys the transition from manual and traditional AOI to modern deep CNN-based AOI.
- Classifies deep learning inspection methods into dense networks and sparse CNN networks, and into supervised, semi-supervised, and unsupervised learning paradigms.
- Reviews supervised CNN classification and segmentation, unsupervised anomaly detection, GAN-based defect generation/scoring, object detection, pixel-level segmentation, and application areas.
- Identifies open challenges in algorithms, application/data handling, and high-performance computing.

## Method

- Review type: narrative literature survey.
- Method categories: manual inspection, traditional computer vision/AOI, and modern CNN-based AOI.
- Traditional AOI pipeline: data acquisition, preprocessing, feature extraction, and defect detection.
- Generic modern AOI architecture: products move on a conveyor with lighting; industrial cameras capture images; an industrial computer runs the machine-vision model; defective products are signaled for removal from the conveyor.
- Camera/interface details: area scan, line scan, 3D, and smart cameras; GigE Vision and USB3 Vision are described as direct camera-to-computer interfaces.

## ML / DL Extraction

### Task Formulation

- Classification: image-level defective/non-defective or defect-type labels.
- Object detection: defect localization with detection boxes; the survey highlights YOLO and R-CNN families.
- Segmentation: pixel-level defect maps; the survey treats pixel-level segmentation as state-of-the-art for AOI when precise defect localization is needed.
- Anomaly detection: defect identification with unlabeled or normal-only data.

### Model And Training

- Model family: [[Deep convolutional neural network]].
- CNN components: convolutional layers, pooling layers, fully connected layers, and output layers.
- CNN history covered: LeNet-5, AlexNet, GoogLeNet, VGGNet, ResNet, GBDNet, SENet, MobileNet-V2, FixResNeXt-101, EfficientNet-L2, and ViT-G/14 in ImageNet-era progress.
- Supervised CNN methods: CNN classifiers, attention/fusion variants, FCN, U-Net, RPN plus modified U-Net, and end-to-end classification/segmentation pipelines.
- Unsupervised CNN methods: convolutional autoencoders, fully convolutional autoencoders, Deep SVDD, GAN synthesis, GAN scoring, AnoGAN, CycleGAN plus U-Net hybrids, and bilinear/hybrid models.
- Object detection models reviewed: YOLO variants, R-CNN/Faster R-CNN, Mask R-CNN, DS-Cascade R-CNN, and FPN-based variants.

### Data

- Datasets: not applicable as a new dataset; the survey reviews many application datasets.
- Data constraints: large labeled datasets are difficult to acquire for industrial defect classification; defective samples are rare, making class imbalance common.
- Annotation constraints: pixel-level segmentation requires expensive, time-consuming human annotation.
- Data availability: the paper states that no data was used for the research described in the article.

### Evaluation

- This survey does not evaluate a new detector.
- It reports representative accuracies and metrics from reviewed studies, including accuracy, [[mAP]], MeanIoU, and [[Dice score]].
- It recommends MeanIoU or Dice coefficient rather than accuracy for comparing pixel-level segmentation models.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP]] | object detection studies | Mean average precision for detected defects | higher is better | no | Examples include 95.49% mAP for wheel hub defects and 71.3% / 72.2% mAP for YOLO-V3 steel-strip detection on GC10-DET / NEUDET. |
| MeanIoU | pixel-level segmentation studies | Mean intersection over union for predicted masks | higher is better | no | Examples include 0.850 on RSDD and 0.869 on DAGM. |
| [[Dice score]] | pixel-level segmentation studies | Dice coefficient for mask overlap | higher is better | no | Examples include 0.835 on RSDD and 0.854 on GDXray. |
| accuracy | classification or segmentation examples | Percent correct predictions | higher is better | no | The survey cautions that pixel-level segmentation should be compared with MeanIoU or Dice rather than accuracy alone. |

## Evidence

### Inspection Method Comparison

| Method group | Benefits | Drawbacks |
|---|---|---|
| Manual inspection | Can identify diverse defects | Tedious, time-consuming, inconsistent, subjective, labor-intensive, and costly |
| Traditional AOI | Reduces labor cost, human error, and inspection time | Poor feature extraction, expert feature design, limited accuracy, less flexibility and robustness |
| Modern AOI | High detection accuracy, real-time/high-speed operation, more robust, lower labor cost, automatic feature extraction | Requires large datasets, high-speed processors, GPUs, and TPUs |

### Deep CNN Categories

| Category | Representative methods | Advantages | Limitations |
|---|---|---|---|
| Supervised classification | CNN classifiers, attention/fusion variants | Image-level labels are easier than pixel masks; training and testing can be fast | Requires many defective and defect-free samples; does not localize defects |
| Supervised segmentation | FCN, U-Net, RPN plus U-Net, semantic networks | Localizes and isolates defective regions | Pixel-level annotation is labor-intensive and expensive |
| Unsupervised anomaly detection | CAE reconstruction, FCAE, Deep SVDD | Can train on defect-free samples and avoids pixel-level annotation | Localization can be difficult; tiny defects are challenging |
| GAN-based approaches | GAN synthesis, GAN scoring, AnoGAN | Can synthesize defects and reduce annotation need | Training/validation can be slow; synthesis may need screening; segmentation may be imprecise |
| Hybrid models | bilinear CNN, CycleGAN plus U-Net | Can combine image labels with localization and real-time inspection goals | Needs substantial data and may produce blurry defect areas or slow training |

### Representative Reported Results

| Area | Study context reported by survey | Metric | Reported result |
|---|---|---|---:|
| Mobile phone glass cover | Multi-DCNN for dent, scratch, chip, and other defects | accuracy | 99% |
| Commutator surface defects | Separable residual CNN | accuracy | about 93% |
| Improved SDAE wafer defect detection | Improved stacked denoising autoencoder | accuracy | 97% |
| Decorated plastic parts | One-class image completion/anomaly detection | AUROC | about 98% |
| CycleGAN plus U-Net | Machine-surface and acne-patch defect localization | accuracy | about 95% |
| DS-Cascade R-CNN | Six wheel hub defect types | mAP | 95.49% |
| YOLO-V3 steel strip | GC10-DET | mAP | 71.3% |
| YOLO-V3 steel strip | NEUDET | mAP | 72.2% |
| YOLO-attention for WAAM | Wire and arc additive manufacturing defects | mAP / FPS | 94.5 / at least 42 FPS |
| Mask R-CNN glass scratches | Transparent glass components | accuracy | 94% |
| PCB Faster R-CNN + FPN | PCB surface defects | mAP | 95% |

### Pixel-Level Segmentation Examples

| Model / approach | Dataset | Accuracy | MeanIoU | Dice coefficient |
|---|---|---:|---:|---:|
| Pixel-level segmentation | RSDD | not listed | 0.850 | not listed |
| NDD-Net | RSDD | 0.997 | not listed | 0.835 |
| Semantic segmentation of EL images | UCF EL Defect Dataset | 95.4% | 0.573 | not listed |
| U-Net GMP + SCLDice | Kolektor | not listed | 0.56 | not listed |
| Regression-based pixel segmentation | DAGM | not listed | 0.845 | not listed |
| TAS2-Net | DAGM | not listed | 0.869 | not listed |
| Automatic deep segmentation | GDXray | 0.998 | not listed | 0.854 |
| CycleGAN | Machine surfaces | 91.11% | not listed | not listed |
| Pixel-wise semi-supervised model | FID | 91.85% | 0.825 | not listed |

## Review / Survey Details

- Scope: deep CNN-based visual defect detection for automated optical inspection.
- Major method families: supervised CNNs, semi-supervised approaches, unsupervised anomaly detection, autoencoders, GANs, object detectors, and segmentation networks.
- Application split: internal defect detection and external surface defect detection.
- Internal examples: aerospace welding, pipe welding, laser welding, radiographic images, and composite materials.
- External textured examples: mobile phone screens, LCD, PCB, glass panels, concrete/building cracks, machined surfaces, die casting, steel, aluminum profiles, polycrystalline alloy, bottles, wood, resin casting, wafers, and voltage-dependent resistors.
- External patterned example: fabric defect detection.

## Limitations

- Supervised CNN methods require large labeled image datasets and are vulnerable to scarce defective samples, class imbalance, and poor generalization.
- Industrial image acquisition can involve non-uniform illumination, motion blur, camera noise, low-contrast defects, and manufacturer-specific quality standards.
- Pixel-level segmentation improves localization but requires costly pixel-wise annotation.
- Unsupervised methods reduce labeling demands but are less reliable and less accurate for localization than supervised models.
- Algorithm choice and hyperparameter tuning are hard because sample size affects accuracy, training time, feature count, data distribution, and computing requirements.
- CNN explainability remains an open concern, especially for safety-critical applications.
- Application/data challenges include data privacy, data cleaning, labeling, annotation, sharing restrictions, and scarce abnormal images.
- HPC and cloud challenges include cost, security, data transfer, cloud performance, and restrictions on moving proprietary data.
- Federated learning is presented as promising but challenged by data heterogeneity, communication overhead, privacy, and quality control.

## Reproducibility

- Code: not reported.
- Data: not applicable; the paper states no data was used for the research described in the article.
- Search protocol: not reported as a systematic search protocol.
- Hyperparameters: not applicable to the review.
- Models/checkpoints: not applicable.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]], [[Object detection]], [[Defect segmentation]]
- Methods: [[Deep convolutional neural network]], [[Data augmentation]], [[GAN]], [[U-Net]], [[Unsupervised anomaly detection]]
- Learning paradigms: [[Unsupervised learning]], [[Semi-supervised learning]]
- Domains: [[Industrial visual inspection]]
- Datasets: not applicable; the paper is a literature survey and introduces no dataset
- Metrics: [[mAP]], [[Dice score]], [[Segmentation metrics]]

### Builds On

- [[Deep convolutional neural network]]: the survey centers modern AOI around sparse CNN-based networks for classification, detection, segmentation, and anomaly detection.

### Contrasts With

- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]]: both review CNN-based defect detection, but this paper is a broader narrative survey covering AOI architecture, unsupervised models, object detection, pixel segmentation, applications, and open challenges.

### Shares Dataset

- not applicable

### Shares Task

- [[Surface defect detection]]: the survey covers visual defect detection across internal and external industrial inspection.
- [[Defect classification]]: supervised CNN classification is one of the main reviewed task families.
- [[Object detection]]: YOLO and R-CNN methods are reviewed as localization approaches.
- [[Defect segmentation]]: pixel-level segmentation is treated as the state-of-the-art direction for precise AOI localization.

### Shares Method

- [[Deep convolutional neural network]]: central model family for modern AOI.
- [[Data augmentation]]: presented as a response to small industrial datasets.
- [[GAN]]: reviewed for defect synthesis, scoring, AnoGAN, and hybrid defect-localization methods.
- [[U-Net]]: reviewed as a segmentation network used across defect-localization applications.
- [[Unsupervised anomaly detection]]: discussed as a way to reduce labeling and pixel-annotation burden.

### Shares Metric

- [[mAP]]: used in object-detection examples.
- [[Dice score]] and [[Segmentation metrics]]: used in pixel-level segmentation comparisons.

### Application / Domain

- [[Industrial visual inspection]]: the survey focuses on automatic optical inspection for manufacturing quality assurance.

### Follow-Up Reading

- [[2023 - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection]]
- [[2024 - A Systematic Review of Deep Learning Approaches for Surface Defect Detection in Industrial Applications]]

## Questions

- Which reviewed unsupervised AOI methods should be represented as standalone method notes if they recur in processed papers?
- Which internal-defect NDT applications should be separated from external surface defect detection in the domain taxonomy?
