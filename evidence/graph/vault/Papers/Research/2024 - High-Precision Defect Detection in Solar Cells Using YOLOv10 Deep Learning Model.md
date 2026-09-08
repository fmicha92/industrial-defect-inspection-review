---
title: "High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model"
aliases:
  - "High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model"
paper_key: "sha256:89659bc837c6a2c7704efd7e0957879dc4bb82c823585ab46354621d94dd6942"
paper_type: research
year: 2024
venue: "Solar"
authors:
  - "Lotfi Aktouf"
  - "Yathin Shivanna"
  - "Mahmoud Dhimish"
status: processed
processed_at: 2026-07-09
topics:
  - photovoltaic manufacturing
  - electroluminescence inspection
  - object detection
tasks:
  - "[[Solar cell defect detection]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[EL Solar Cells Dataset]]"
methods:
  - "[[YOLOv10]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[YOLOv10]]"
  - "YOLOv10x"
losses:
  - "Cross-Entropy loss"
  - "Bounding Box loss"
optimizers:
  - "SGD"
  - "Adam"
metrics:
  - "[[mAP@0.50]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.5 is mean average precision across classes at IoU threshold 0.5."
  - "Precision, recall, accuracy, and F1-score are computed from TP, TN, FP, and FN."
baselines:
  - "Faster R-CNN + attention mechanism"
  - "Bidirectional Attention Feature Pyramid Network"
  - "ResNet152-Xception ensemble"
  - "Random Forest"
  - "k-NN"
  - "SVM"
  - "PD-DETR"
benchmarks:
  - "[[EL Solar Cells Dataset]]"
code: "not reported"
data: "available on responsible request to the corresponding author"
doi: "10.3390/solar4040030"
arxiv: "not reported"
url: "https://doi.org/10.3390/solar4040030"
related_concepts:
  - "[[Surface defect detection]]"
related_methods:
  - "[[YOLOv10]]"
related_datasets:
  - "[[EL Solar Cells Dataset]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
source_file: "paper-inbox/10_processed/Research/2024 - Aktouf - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Aktouf - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Aktouf - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model.txt"
artifact_status: "data available on responsible request; code not reported"
tags:
  - paper
---

# High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model

## Summary

Aktouf, Shivanna, and Dhimish apply [[YOLOv10]] to electroluminescence-based [[Solar cell defect detection]]. The paper uses a 10,500-image [[EL Solar Cells Dataset]] with 12 defect classes and evaluates the trained model on an unseen 6,000-image test set containing 500 samples per defect class.

The reported YOLOv10x model achieves 98.5% mAP@0.5 on the EL Solar Cells dataset. The authors frame this as the first application of YOLOv10 to electroluminescence photovoltaic defect detection and argue that Compact Inverted Blocks and Partial Self-Attention support high-accuracy, real-time defect detection.

## Paper Type

- Type: research.
- Why: The paper trains and evaluates a YOLOv10 object detector for solar-cell defect localization and classification, with dataset details, training settings, metrics, and comparison to prior EL defect-detection models.

## Problem

- Task: [[Solar cell defect detection]] in electroluminescence images.
- Setting: photovoltaic manufacturing quality control.
- Inputs: EL images of solar cells.
- Outputs: bounding boxes and defect labels for 12 defect types.
- Motivation: manual solar-cell inspection is error-prone, and subtle defects can reduce solar-panel performance and reliability.

## Contribution

- Applies YOLOv10x to EL solar-cell defect detection.
- Uses Compact Inverted Blocks and Partial Self-Attention modules for feature extraction and representation refinement.
- Reports 98.5% mAP@0.5 on a 10,500-image dataset and evaluates generalization on an unseen 6,000-image test set.
- Compares the reported accuracy with recent EL defect detection studies using Faster R-CNN, attention feature pyramids, ensemble CNNs, classical ML, PD-DETR, and custom deep learning models.

## Method

### YOLOv10 Architecture

- Core modules: Compact Inverted Block (CIB) and Partial Self-Attention (PSA).
- CIB uses depthwise separable convolutions and pointwise convolutions to reduce computational burden while maintaining feature extraction.
- PSA uses multi-head self-attention and feed-forward layers to capture long-range dependencies and refine features.
- Overall detector includes a backbone, neck, and detection head; the head predicts bounding box coordinates, class probabilities, and object confidence.
- The paper states that YOLOv10 in this study refers to YOLOv10x.

### Training

- Training platform: Viking cluster at the University of York.
- GPUs available on the cluster: 48 A40 units and 12 H100 units.
- Epochs: 750.
- Classes: 12.
- Batch size: 32.
- Learning rate: 0.001.
- Weight decay: 0.0005.
- Optimizers: SGD/Adam.
- Input image size: 640 x 640 pixels.
- Loss: Cross-Entropy plus Bounding Box Loss.
- Confidence threshold: 0.25.
- Validation split: 20%.
- Anchor boxes: (10,13), (16,30), and (23,33).
- Non-Max Suppression threshold: 0.45.
- Backbone listed in the training table: CSPDarknet53.
- Augmentation: random flip, rotation, and scale.
- Training duration: approximately 27 minutes.

## ML / DL Extraction

### Task Formulation

- Input modality: electroluminescence solar-cell images.
- Output target: bounding boxes and class labels for solar-cell defects.
- Supervision: supervised object detection with annotated defect classes.
- Objective: detect and localize defects in photovoltaic manufacturing images.

### Model And Training

- Model family: YOLO one-stage detector.
- Architecture: YOLOv10x with CIB and PSA modules.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not reported.
- Random seeds: not reported.
- Compute: Viking cluster; available GPUs include A40 and H100.
- Inference: the paper reports an average inference speed of 25 FPS on a standard Nvidia GTX 1080.

### Data

- Dataset: [[EL Solar Cells Dataset]].
- Source: manufacturing facility at Hebei University of Technology and Beihang University.
- Training/validation size: 10,500 images.
- Class balance: 12 defect classes, each with 875 samples for training and validation.
- Unseen test set: 500 samples per defect class, 6,000 images total.
- Cell technologies: both polycrystalline and monocrystalline silicon solar cells.
- Defect classes: line crack, star crack, finger interruption, black core, vertical dislocation, horizontal dislocation, thick line, scratch, fragment, corner, short circuit, and printing error.
- Data availability: available on responsible request to the corresponding author.
- License: article is CC BY 4.0; dataset license is not reported.

### Evaluation

- Metrics: accuracy, precision, recall, F1-score, AP, and mAP@0.5.
- Confusion matrix: normalized on the unseen test set.
- Precision-Recall curve: mAP@0.5 across all classes.
- Statistical tests: not reported.

## Evidence

### Main Results

| Dataset / split | Metric | Reported value | Notes |
|---|---|---:|---|
| [[EL Solar Cells Dataset]], validation/test evaluation | mAP@0.5 | 98.5% | Overall mean Average Precision across 12 defect classes. |
| Unseen EL Solar Cells test set | Sample size | 6,000 images | 500 samples per defect class. |
| Unseen EL Solar Cells test set | Aggregate recall at confidence 0.0 | 0.99 | From the Recall-Confidence curve. |
| Standard Nvidia GTX 1080 inference | FPS | 25 FPS | Reported as suitable for real-time defect detection. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP@0.50]] | object detection | mean AP at IoU threshold 0.5 | higher is better | yes | 98.5% |
| [[Precision]] | defect prediction quality | TP / (TP + FP) | higher is better | no | class values reported; several classes near 99-100% |
| [[Recall]] | defect detection completeness | TP / (TP + FN) | higher is better | no | class values reported; aggregate curve begins at 0.99 recall |
| [[F1-score]] | precision/recall balance | harmonic mean of precision and recall | higher is better | no | class values reported in Table 2 |

### Class-Level Findings

- The narrative reports perfect or near-perfect performance for black core, corner, fragment, scratch, short circuit, printing error, horizontal dislocation, and vertical dislocation.
- The paper identifies thick line and star crack defects as more challenging; reported accuracy values include 87% for thick line and 92% for star crack in the prose.
- The extracted Table 2 maps numeric columns to defect class indices, but OCR duplication makes the class-to-column alignment partly ambiguous. The aggregate mAP@0.5 and stated hard classes are clear in the prose.

### Comparative Results

| Study / model | Dataset | Reported accuracy | Comment |
|---|---|---:|---|
| Faster R-CNN + attention | custom EL dataset, 3,629 images | 87.38% | Fine-grained defect detection; real-time processing not achieved. |
| Bidirectional Attention Feature Pyramid Network | custom EL dataset, 3,629 images | 72.53% to 100% | Better varied-size defect detection; real-time processing remains challenging. |
| ResNet152-Xception ensemble | mixed datasets, 2,223 images | 92.13% | Robust but high computational cost. |
| RF / k-NN / SVM | custom dataset, >45,000 images | 99.2% / 98.4% / 96.7% | Uses statistical parameters from EL image histograms. |
| PD-DETR | [[PVEL-AD]], 4,500 images | 64.7% | Detects small defects in complex backgrounds. |
| Custom deep learning model | ELPV and PVEL-AD, >15,000 images | 92.13% to 96.17% | Reduces prediction errors with mixed defect-type results. |
| This paper, YOLOv10 | [[EL Solar Cells Dataset]], 10,500 images | 98.5% | First reported YOLOv10 use for EL PV defect detection. |

## Dataset / Benchmark Details

- [[EL Solar Cells Dataset]] is not the same as [[ELPV Dataset]] or [[PVEL-AD]] in the paper's description.
- The dataset is described as sourced from a manufacturing facility at Hebei University of Technology and Beihang University.
- The paper uses balanced class counts for training and validation, while noting that real-world defect frequencies may be imbalanced.
- Future work is proposed to test imbalanced datasets that better reflect real manufacturing conditions.

## Limitations

- Thick lines and star cracks remain more difficult than many other classes because of subtle visual signatures and irregular shapes.
- The computational cost of YOLOv10x may limit use in smaller-scale applications without high-performance computing resources.
- The paper does not report model parameter count, exact YOLOv10x implementation source, random seeds, or code availability.
- The dataset is available by request rather than as a directly downloadable public artifact.
- Future work is needed for ablation studies isolating CIB and PSA contributions.

## Reproducibility

- Code: not reported.
- Data: available on responsible request to the corresponding author.
- Hyperparameters: 750 epochs, batch size 32, learning rate 0.001, weight decay 0.0005, confidence threshold 0.25, NMS 0.45, 640 x 640 input.
- Random seeds: not reported.
- Environment: Viking cluster at University of York; exact software versions not reported.
- Hardware: cluster has A40 and H100 GPUs; GTX 1080 inference speed is discussed.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]]
- Methods: [[YOLOv10]]
- Datasets: [[EL Solar Cells Dataset]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[mAP@0.50]], [[Precision]], [[Recall]], [[F1-score]]
- Concepts: [[Surface defect detection]]

### Builds On

- [[YOLOv10]]: the paper applies YOLOv10x to EL solar-cell defect detection.

### Shares Dataset

- [[EL Solar Cells Dataset]]: used for training, validation, and unseen testing.

### Shares Task

- [[Solar cell defect detection]]: the paper detects and localizes photovoltaic cell defects in EL imagery.

### Shares Method

- [[YOLOv10]]: the detector architecture central to the paper.

### Shares Metric

- [[mAP@0.50]], [[Precision]], [[Recall]], and [[F1-score]]: used to evaluate object detection performance.

### Application / Domain

- [[Solar cells and photovoltaic]]: the application setting is photovoltaic manufacturing inspection.

### Follow-up Reading

- [[PVEL-AD]]: compared in prior-work table through PD-DETR, but not the dataset used by this paper.
- [[ELPV Dataset]]: appears in comparative prior work, but not as the dataset used by this paper.

## Questions

- What is the exact dataset access path and license for the EL Solar Cells dataset?
- How does YOLOv10x perform under the real imbalanced class distribution expected in manufacturing?
- Which part of the 98.5% mAP@0.5 depends on CIB, PSA, augmentation, and YOLOv10x scale?
