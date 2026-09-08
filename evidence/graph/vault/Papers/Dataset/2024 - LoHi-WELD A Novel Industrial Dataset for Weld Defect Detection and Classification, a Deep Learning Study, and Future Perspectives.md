---
title: "LoHi-WELD: A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives"
aliases:
  - "LoHi-WELD"
paper_key: "doi:10.1109/access.2024.3407019"
paper_type: dataset
year: 2024
venue: "IEEE Access"
authors:
  - "Sylvio B. Block"
  - "Ricardo D. da Silva"
  - "Andre E. Lazzaretti"
  - "Rodrigo Minetto"
status: processed
processed_at: 2026-05-22
audited_at: 2026-06-11
topics:
  - "weld defect detection"
  - "weld bead dataset"
  - "visual nondestructive inspection"
tasks:
  - "[[Weld defect detection]]"
  - "[[Defect classification]]"
  - "[[Defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[LoHi-WELD]]"
dataset_sizes:
  - "LoHi-WELD: 3022 weld bead images, 2000 low-resolution lweld images and 1022 high-resolution hweld images"
  - "Defect annotations: 3950 pores, 2935 deposits, 7220 discontinuities, and 8307 stains"
splits:
  - "Each subset uses 80% image samples for training and 20% for testing; training uses 5-fold cross-validation and evaluates the best validation-fold model on the holdout test set"
methods:
  - "[[YOLOv7]]"
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[YOLOv7]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
  - "[[mAP@0.50]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.50: mean average precision at IoU 0.50 using the PASCAL VOC object-detection criterion; higher is better"
  - "F-score: harmonic mean of precision and recall; higher is better"
baselines:
  - "YOLOv7-tiny"
  - "YOLOv7"
benchmarks:
  - "[[LoHi-WELD]]"
parameters: "YOLOv7-tiny: 6.2M parameters; YOLOv7: 36.9M parameters"
compute: "Intel i7-10700 2.9GHz, 128GB RAM, NVIDIA RTX 3090 24GB"
hardware: "Intel i7-10700 2.9GHz, 128GB RAM, NVIDIA RTX 3090 24GB"
training_time: "50 epochs per fold, best validation-fold model saved"
inference_cost: "The paper cites YOLOv7 authors' Jetson AGX Xavier and Jetson Nano speed examples for 640x640 images, but does not report measured LoHi-WELD deployment latency"
code: "public GitHub repository reported by the paper"
data: "public LoHi-WELD dataset reported by the paper"
doi: "10.1109/ACCESS.2024.3407019"
arxiv: "not applicable"
url: "https://doi.org/10.1109/ACCESS.2024.3407019"
pdf: "paper-inbox/10_processed/Dataset/2024 - Block - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives.pdf"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
related_methods:
  - "[[YOLOv7]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[LoHi-WELD]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Weld defect detection]]"
  - "[[Defect classification]]"
  - "[[Defect detection]]"
related_benchmarks:
  - "[[LoHi-WELD]]"
source_file: "paper-inbox/10_processed/Dataset/2024 - Block - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Block - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Block - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives.txt"
artifact_status: "dataset, architecture, and trained models reported as publicly available on GitHub upon acceptance"
tags:
  - paper
---
# LoHi-WELD: A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives

## Summary

The paper introduces [[LoHi-WELD]], a public weld bead image dataset for visual nondestructive inspection of Metal Active Gas robotic welding. It contains 3,022 real weld bead images with manual axis-aligned bounding boxes for four defect categories: pores, deposits, discontinuities, and stains. The paper also provides YOLOv7 and YOLOv7-tiny baselines and shows that the lightweight model reaches 0.64 mAP@0.50 on the low-resolution subset and 0.69 mAP@0.50 on the high-resolution subset for fine-grained four-class detection.

## Paper Type

- Type: dataset.
- Why: The primary contribution is a public weld defect dataset with manual annotations, plus baseline detector experiments and future research directions.

## Problem

- Task: [[Weld defect detection]] and [[Defect classification]].
- Setting: visual nondestructive inspection for robotic gas metal arc welding / Metal Active Gas welding.
- Inputs: grayscale weld bead images acquired from an industrial robot line.
- Outputs: bounding boxes and classes for pore, deposit, discontinuity, and stain defects.
- Motivation: deep models for weld inspection need public datasets with real visual defects and detailed annotations.
- Assumptions: defect presence does not directly imply industrial non-conformity; bead integrity depends on manufacturer-specific parameters such as defect count and extension.

## Contribution

- Claimed: LoHi-WELD provides one of the largest public visual weld defect datasets by number of defects, with low- and high-resolution subsets and manual four-class annotations.
- Shown: YOLOv7-tiny performs similarly to YOLOv7 while using far fewer parameters, supporting an edge-device-oriented baseline.
- Shown: Fine-grained mAP@0.50 reaches 0.64 on `lweld` and 0.69 on `hweld`; coarse defect/non-defect mAP@0.50 reaches 0.75 and 0.77, respectively.

## Method

- Dataset collection: images were acquired during a standard robotic welding production cycle after the robot left the capture scene; the process used GMAW/MAG welding.
- Imaging: both subsets use CMOS global-shutter cameras, grayscale JPEG encoding, and white LED panel illumination.
- Annotation: each defect is manually labeled with an axis-aligned bounding box and one of four defect classes; each weld bead region of interest is also delimited by a rectangle.
- Detection baseline: YOLOv7-tiny and YOLOv7 are trained for object detection and defect classification.
- Resizing: letterbox resizing preserves aspect ratio and pads the shorter side with gray values.
- Augmentation: mosaic probability 100%, scale gain +/-50%, up/down flip probability 50%, left/right flip probability 50%, copy-paste probability 50%, translate fraction +/-20%, and HSV variation `(0.015, 0.7, 0.4)`.

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale weld bead visual inspection images.
- Output target: object boxes and class labels for pores, deposits, discontinuities, and stains.
- Supervision: fully supervised object detection with manually annotated bounding boxes.
- Objective: provide a public benchmark and baseline performance for weld defect detection and classification.

### Model And Training

- Model family: [[Deep convolutional neural network]] object detectors.
- Architectures: [[YOLOv7]] and YOLOv7-tiny.
- Parameters: YOLOv7-tiny has 6.2M parameters; YOLOv7 has 36.9M parameters.
- Image sizes tested: 320x320, 640x640, and 1280x1280.
- Training protocol: each subset uses 80% image samples for training and 20% for testing; training uses 5-fold cross-validation and saves the best model in 50 epochs based on validation-fold performance.
- Hardware: Intel i7-10700 2.9GHz, 128GB RAM, NVIDIA RTX 3090 24GB.

### Data

- Dataset: [[LoHi-WELD]].
- `lweld`: 2,000 low-resolution weld bead images from a 640x480 sensor; it includes two weld bead region sizes, approximately 40 mm and 60 mm.
- `hweld`: 1,022 high-resolution weld bead images from a 2048x1080 sensor; it focuses on the larger bead because defects concentrated there during robot positioning.
- Defect counts: 3,950 pores, 2,935 deposits, 7,220 discontinuities, and 8,307 stains.
- Total annotated defects: more than 22,000.
- License: the article is under CC BY-NC-ND 4.0; dataset license is reported in the dataset note from repository evidence, not in the extracted paper text.

### Evaluation

- Protocol: evaluate YOLOv7-tiny under image-size and augmentation settings; compare YOLOv7-tiny against YOLOv7; evaluate cross-resolution transfer, fused training, and coarse versus fine classification.
- Metrics: [[Precision]], [[Recall]], [[F1-score]], and [[mAP@0.50]].
- True positive criterion: IoU at least 0.50 with a ground-truth region and correct class.
- False positives: predicted regions below IoU threshold or with incorrect class.
- False negatives: undetected ground-truth regions.

## Evidence

### Main Results

| Result | Dataset / task | Metric | Direction | Baseline / setting | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Best fine-grained low-resolution baseline | `lweld` four-class detection | [[mAP@0.50]] | higher | YOLOv7-tiny, 640x640, augmentation | 0.64 | F-score 0.64. |
| Best fine-grained high-resolution baseline | `hweld` four-class detection | [[mAP@0.50]] | higher | YOLOv7-tiny, 1280x1280, augmentation | 0.69 | F-score 0.67. |
| Larger model comparison | `lweld` four-class detection | [[mAP@0.50]] | higher | YOLOv7-tiny 0.64 | YOLOv7 0.63 | Same 640x640 augmented setting. |
| Larger model comparison | `hweld` four-class detection | [[mAP@0.50]] | higher | YOLOv7-tiny 0.69 | YOLOv7 0.70 | Same 1280x1280 augmented setting. |
| Coarse classification | `lweld` defect/non-defect detection | [[mAP@0.50]] | higher | fine four-class 0.64 | coarse binary 0.75 | F-score rises from 0.64 to 0.72. |
| Coarse classification | `hweld` defect/non-defect detection | [[mAP@0.50]] | higher | fine four-class 0.69 | coarse binary 0.77 | F-score rises from 0.67 to 0.74. |

### Augmentation And Resolution Findings

- For `lweld`, YOLOv7-tiny with augmentation improves from 0.54 mAP at 320x320 to 0.64 mAP at 640x640.
- For `hweld`, YOLOv7-tiny with augmentation improves from 0.35 mAP at 320x320 to 0.64 mAP at 640x640 and 0.69 mAP at 1280x1280.
- The paper states that data augmentation generally improves all metrics across image sizes, except for `hweld` at 320x320, where downsampling likely removes small details.

### Cross-Resolution And Fusion Findings

- Cross-resolution transfer is weak: training on `lweld` and testing on `hweld` gives 0.25 to 0.29 mAP, while training on `hweld` and testing on `lweld` gives 0.18 to 0.19 mAP.
- Fusion experiments maintain similar performance but do not produce a clear gain over subset-specific training; the paper reports up to 0.69 mAP in the fused settings.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[mAP@0.50]] | Object detection | Mean average precision at IoU 0.50 | higher | yes | Reported as the main benchmark result. |
| [[F1-score]] | Detection/classification | Harmonic mean of precision and recall | higher | no | Reported with precision and recall. |
| [[Precision]] | Detection/classification | Correct positive detections among detections | higher | no | Weighted by confidence score. |
| [[Recall]] | Detection/classification | Detected ground-truth defects among all ground-truth defects | higher | no | Weighted by confidence score. |

## Dataset / Benchmark Details

- Source: robotic GMAW/MAG welding industrial process.
- Collection: images triggered by a PLC after the robot left the capture scene.
- Low-resolution subset: 2,000 weld bead images, 640x480 sensor, two bead region widths of roughly 40 mm and 60 mm.
- High-resolution subset: 1,022 weld bead images, 2048x1080 sensor, larger weld bead only.
- Defect categories: pore, deposit, discontinuity, stain.
- Annotation: manual axis-aligned bounding boxes for defects and weld bead regions of interest.
- Bias / coverage: the dataset was collected during initial fine-tuning tests of a welding machine, producing many defects that may be scarce in stable production.
- Leakage risks: not reported.

## Limitations

- `hweld` has fewer bead images than `lweld`, and the paper proposes augmenting high-resolution data with super-resolution or generative methods.
- Cross-resolution generalization is poor, indicating strong dependence on image scale and acquisition configuration.
- Pores are rare in `hweld`, which the paper connects to weaker pore-class behavior and confusion with stains.
- Stains and deposits are visually confusable, especially when stains are light-colored or surface irregularities resemble the background.

## Reproducibility

- Data: public LoHi-WELD dataset reported by the paper.
- Code / trained models: reported as public on GitHub upon acceptance.
- Hyperparameters: augmentation probabilities and tested input sizes are reported.
- Random seeds: not reported.
- Environment: CPU, RAM, and GPU hardware are reported; software stack is not reported.

## Systems Details

- Deployment motivation: the low-resolution subset and YOLOv7-tiny baseline target reduced bandwidth, lower compute, and possible edge-device use.
- Parameters: YOLOv7-tiny 6.2M; YOLOv7 36.9M.
- Measured LoHi-WELD latency: not reported.
- External speed reference cited by the paper: YOLOv7 authors reported YOLOv7-tiny at 40 FPS on Jetson AGX Xavier and 16 FPS on Jetson Nano for 640x640 images, versus YOLOv7 at 17 FPS and 3 FPS.

## Connections

### Graph Hubs

- Tasks: [[Weld defect detection]], [[Defect classification]], [[Defect detection]]
- Methods: [[YOLOv7]], [[Deep convolutional neural network]], [[Data augmentation]]
- Datasets: [[LoHi-WELD]]
- Benchmarks: [[LoHi-WELD]]
- Domains: [[Metal inspection]]
- Metrics: [[Precision]], [[Recall]], [[F1-score]], [[mAP@0.50]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

- Follow-up reading: papers using [[LoHi-WELD]] for weld defect detection should compare against the YOLOv7-tiny 0.64/0.69 fine-grained mAP baselines and the 0.75/0.77 coarse mAP baselines.

### Relationship Notes

- Shares dataset: [[LoHi-WELD]].
- Shares task: [[Weld defect detection]] and [[Defect classification]].
- Shares method/model: [[YOLOv7]] and [[Data augmentation]].
- Application/domain: [[Metal inspection]].

## Questions

- Which exact GitHub release contains the final dataset, trained models, and code referenced as available upon acceptance?
- How stable are LoHi-WELD baselines under different train/test splits or random seeds?
- Can super-resolution or generative augmentation improve `hweld` without distorting subtle surface defects?
