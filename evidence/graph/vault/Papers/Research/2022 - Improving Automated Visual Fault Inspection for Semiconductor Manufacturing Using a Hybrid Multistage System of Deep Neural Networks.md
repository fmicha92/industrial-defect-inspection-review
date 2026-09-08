---
title: "Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks"
aliases:
  - "Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks"
  - "SH-DNN semiconductor visual fault inspection"
paper_key: "doi:10.1007/s10845-021-01906-9"
paper_type: research
year: 2022
venue: "Journal of Intelligent Manufacturing"
authors:
  - "Tobias Schlosser"
  - "Michael Friedrich"
  - "Frederik Beuth"
  - "Danny Kowerko"
status: processed
processed_at: 2026-05-22
topics:
  - "semiconductor manufacturing"
  - "visual fault inspection"
  - "wafer dicing"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[Semiconductor visual inspection dataset]]"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Feature extraction]]"
  - "[[Autoencoder-decoder data augmentation]]"
model_family:
  - "[[Deep convolutional neural network]]"
  - "hybrid multistage system"
architectures:
  - "SH-DNN"
  - "VGG-inspired custom CNN"
  - "SWWAE with residual learning"
metrics:
  - "[[F1-score]]"
  - "[[Accuracy]]"
primary_metric: "[[F1-score]]"
baselines:
  - "chip-based single-DNN classification"
  - "conventional machine learning classifiers"
  - "reimplemented semiconductor visual inspection CNNs"
benchmarks:
  - "[[Semiconductor visual inspection dataset]]"
code: "not reported in paper note source"
data: "private real-world semiconductor wafer dicing imagery from third-party manufacturers"
doi: "10.1007/s10845-021-01906-9"
arxiv: "not reported"
url: "https://doi.org/10.1007/s10845-021-01906-9"
pdf: "paper-inbox/10_processed/Research/2022 - Schlosser - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Netw....pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Schlosser - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Netw....pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Schlosser - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Netw....md"
extracted_text: "paper-inbox/90_processing/text/2022 - Schlosser - Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Netw....txt"
artifact_status: "data redistribution restricted; code not reported"
tags:
  - paper
---

# Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks

## Summary

The paper introduces a hybrid multistage system of stacked deep neural networks (SH-DNN) for semiconductor wafer dicing inspection. The central idea is to localize task-relevant regions with a classical computer-vision pipeline, then classify progressively smaller structures with deep neural networks so tiny defects are not lost by downsampling whole high-resolution wafer imagery.

On a private real-world wafer dicing dataset, the best street-based SH-DNN configuration reports 99.5% F1-score. Compared with single-DNN chip classification, the paper reports up to 3.8 percentage-point F1 improvement for DL approaches and an 8.6-fold reduction in the fault-detection error rate. A production-oriented MobileNetV2-based configuration reports about 5.2 ms per chip image sample on consumer-grade hardware while keeping final F1 above 99%.

## Paper Type

- Type: research.
- Why: proposes and evaluates a multistage inspection system, including dataset construction, processing pipeline, model comparisons, runtime analysis, and visualization.

## Problem

- Task: [[Defect classification]] for wafer dicing defects, with localization of streets and street segments.
- Setting: semiconductor manufacturing after wafer cutting.
- Inputs: wafer/chip/street grayscale microscope imagery.
- Outputs: chip, street, and segment states such as flawless, anomalous, and faulty; visual overlays resembling wafer maps.
- Motivation: pixel-sized defects can be only a few micrometers wide within very large wafer images, making whole-image single-network processing either too expensive or too lossy.

## Contribution

- Proposes SH-DNN, a hybrid multistage pipeline combining classical image-processing localization with deep-learning classification.
- Introduces chip, street, and street-segment addressing to map local inspection decisions back to wafer positions.
- Uses CNNs for inside/border chip classification and street classification, plus a Stacked What-Where Autoencoder with residual learning for unsupervised street-segment anomaly analysis.
- Benchmarks conventional ML classifiers, reimplemented domain CNNs, and general DL architectures.
- Evaluates runtime and model complexity for deployment under millisecond-level manufacturing constraints.

## Method

- Chip stage: separates inside chips from border/outside chips; border chips are excluded from further processing.
- Street localization: applies OpenCV histogram equalization, binary thresholding over grayscale values, contour detection, erosion, and bounding-rectangle selection to localize street centers.
- Street classification: crops a street ROI around each chip border and classifies it as flawless or faulty with a CNN or alternative classifier.
- Street segment classification: separates streets into segments and uses an unsupervised SWWAE-style autoencoder to flag anomalous/faulty segments from reconstruction loss.
- Backtracing: maps faulty streets and street segments back to chip status; a chip is faulty when at least one side is classified faulty.
- Visualization: maps flawless, anomalous, and faulty chips/streets/segments into wafer overlays with color transitions by faultiness.

## Evidence

### Dataset

- Source: real-world dicing processes from different semiconductor wafers provided by third-party manufacturers.
- Capture: wafers are mounted on taped frames, expanded after cleaving, and scanned with wide-field light microscopy.
- Wafer types: six.
- Chip image resolution range: 224 x 224 up to 960 x 1024 pixels per chip.
- Total inside chips: 8325.
- Total inside faulty chips: 1026.
- Total streets: 33,136.
- Total faulty streets: 1917.
- Fault/anomaly examples: small holes, scratches, bubbles, and other defects on wafer and street surfaces.
- Availability: the paper notes semiconductor manufacturing datasets often have privacy and redistribution restrictions; public release is not reported.

### Training Setup

- Data split: random 50/25/25 train/validation/test.
- Class balancing: faulty classes are sampled and duplicated before training.
- Augmentation: rotation, translation, scaling, and x-axis mirroring through imgaug.
- Preprocessing: chip-wise histogram equalization and sample-wise standardization.
- Frameworks: Keras with TensorFlow backend; scikit-learn for ML baselines; OpenCV for localization.
- Optimizer for DNNs: Adam, learning rate 0.001, beta values 0.9 and 0.999.
- Batch size: 32.
- DNN evaluation: 100 training epochs, averaged over five runs.

### Main Results

| Comparison | Baseline result | SH-DNN result | Source-supported claim |
|---|---:|---:|---|
| Conventional baseline approaches | up to 95.0% F1 | up to 98.9% F1 | +3.9 percentage points and up to 4.6-fold error-rate reduction |
| Single-DNN / DL approaches | up to 95.7% F1 for ResNet152V2 chip classification | 99.5% F1 for ResNet152V2 street-based classification | +3.8 percentage points and 8.6-fold error-rate reduction |
| Production-oriented multistage configuration | not applicable | above 99% final F1 and about 5.2 ms per chip image sample | MobileNetV2 chosen as accuracy/runtime compromise |

### Runtime And Complexity

| Stage | Trainable parameters | Time per sample |
|---|---:|---:|
| Chip-based localization | 0 | <0.1 ms |
| Chip-based classification | 2,260,546 | 1.00 ms |
| Street-based localization | 0 | 3.20 ms |
| Street-based classification | 2,260,546 | 0.32 ms |
| Segment-based localization | 0 | <0.1 ms |
| Segment-based classification | 251,931 | 0.41 ms |
| Fault backtracing | 0 | <0.1 ms |
| Total | 4,773,023 | 5.2 ms |

## Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[F1-score]] | chip and street classification | F1-score percentage over flawless/faulty classification | higher | yes | main reported performance metric |
| [[Accuracy]] | training/test stability and simple inside/border chip classification | classification accuracy | higher | no | inside/border chip classification exceeds 99% in the source |

## Dataset / Benchmark Details

- The dataset is not a wafer map prober dataset; it is visual microscope imagery captured after dicing.
- The paper distinguishes chips, streets, and street segments because defects occur around dicing streets and may continue into chips.
- Anomaly cases are treated as faulty for classification, then can be manually inspected through visualization.
- The authors explicitly contrast their real-world wafer dicing imagery with synthesized or single-manufacturer wafer datasets.

## Limitations

- Direct comparison with other semiconductor datasets is difficult because manufacturing data often have privacy and redistribution restrictions.
- Positive predictive value depends strongly on the faulty street ratio of a new wafer type; for very low fault ratios below 0.2%, higher recall/specificity or wafer-specific training may be required.
- The reported runtime comparison to region-based DNNs is shallow because image resolution, hardware, and inspection requirements differ.
- Future work includes adding other sensors such as audio or heat signatures and tuning camera/lighting settings.

## Reproducibility

- Code: not reported in the source text used for this note.
- Data: private real-world wafer dicing imagery; redistribution not reported.
- Software stack: OpenCV, imgaug, Keras/TensorFlow, and scikit-learn are reported.
- Hardware for runtime tests: Intel Core i9-9900K CPU, TITAN RTX GPU, 128 GB RAM, and Samsung 970 EVO Plus SSD.
- Model/training details: custom CNN layer tables, optimizer settings, data split, augmentation, epochs, and batch size are reported.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Wafer map defect classification]]
- Methods: [[Deep convolutional neural network]], [[Feature extraction]], [[Autoencoder-decoder data augmentation]]
- Datasets: [[Semiconductor visual inspection dataset]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[F1-score]], [[Accuracy]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[Semiconductor visual inspection dataset]] | Evaluation dataset | The paper evaluates on private real-world wafer dicing imagery. |
| [[Semiconductor and electronics]] | Application domain | The method targets semiconductor manufacturing inspection after wafer dicing. |
| [[Deep convolutional neural network]] | Method family | CNNs are used for chip and street classification. |
| [[Autoencoder-decoder data augmentation]] | Related model family | The segment stage uses an autoencoder-style model for unsupervised anomaly scoring. |

## Questions

- Would a public wafer dicing dataset reproduce the same localization advantage?
- How much wafer-specific adaptation is required for fault ratios below 0.2%?
- Can the street-segment anomaly visualization be calibrated into actionable defect categories for process engineers?
