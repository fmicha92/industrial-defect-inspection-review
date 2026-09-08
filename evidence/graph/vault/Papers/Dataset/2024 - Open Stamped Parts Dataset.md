---
title: "Open Stamped Parts Dataset"
aliases:
  - "OSPD paper"
  - "Open Stamped Parts Dataset"
paper_key: "arxiv:2403.10369"
paper_type: "dataset"
year: 2024
venue: "arXiv"
authors:
  - "Sarah Antiles"
  - "Sachin Talathi"
status: "processed"
topics:
  - "automotive manufacturing"
  - "stamped metal inspection"
  - "synthetic data"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Defect segmentation]]"
datasets:
  - "[[Open Stamped Parts Dataset]]"
methods:
  - "[[YOLOv7]]"
  - "[[Simulation-based data augmentation]]"
  - "[[Contrastive unpaired translation]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Modified recall]]"
  - "[[Modified F0.9 score]]"
primary_metric: "[[Modified F0.9 score]]"
related_domains:
  - "[[Automotive manufacturing]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Synthetic data generation]]"
  - "[[Domain gap]]"
arxiv: "2403.10369"
url: "https://arxiv.org/abs/2403.10369"
pdf: "paper-inbox/10_processed/Dataset/2024 - Antiles - Open Stamped Parts Dataset.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Antiles - Open Stamped Parts Dataset.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Antiles - Open Stamped Parts Dataset.txt"
---
# Open Stamped Parts Dataset

## Summary

The paper introduces [[Open Stamped Parts Dataset]], a public automotive stamped-sheet inspection dataset with real and synthetic grayscale images. It frames missing-hole inspection as hole detection: models detect expected holes, and missing holes are inferred when expected holes are absent. The paper also benchmarks YOLOv7 models trained on synthetic and image-to-image translated synthetic data, reporting that the plain synthetic multi-class model achieved the best modified recall and precision among the tested variants.

## Paper Type

Dataset paper. The main contribution is the release of real and synthetic stamped metal-sheet image sets, annotations, evaluation metrics, and baseline object-detection results for automotive hole inspection.

## Problem

Manual inspection of stamped metal sheets is time-consuming and error-prone because stamped parts contain many holes, some of which are small or low contrast. Missing stamped holes are rare but costly. The paper targets real-time localization of stamped holes so that missing-hole defects can be inferred in an automotive manufacturing setting.

## Contribution

- Releases OSPD with synthetic and real stamped metal-sheet images, including real labeled, real unlabeled, reference, masked-hole, and synthetic split variants.
- Provides bounding-box annotations for real and synthetic holes, segmentation masks for synthetic holes, and metadata such as camera name, trigger distance, grading status, and masked-hole status.
- Defines a modified recall metric and modified F0.9 score to penalize false positives on masked holes, reflecting the production preference against declaring a missing hole as present.
- Benchmarks YOLOv7 detectors trained on synthetic data and on CUT-translated synthetic data.

## Method

### Dataset Construction

- Real data was collected from stamped sheet-metal inspections using seven left-side cameras in a fixture with 40 cameras across entrance, exit, left, and right sides.
- Images were captured with infrared lighting and infrared camera filters.
- Synthetic data was generated in Unreal Engine with configured camera angle, focal length, lighting, random camera shift, part shift, and lighting changes.
- Synthetic data includes seven distinct hole categories.
- Missing-hole defects are simulated by masking 10% of holes.
- Five labelers annotated real stamped holes in Label Studio, with each person's labels reviewed by two others.
- Six labelers annotated polygon masks for masked holes, again with review by two others.

### Dataset Splits

- Synthetic data: 7,980 training images, 1,680 validation images, and 1,680 test images.
- Real labeled data: 1,680 images.
- Real unlabeled data: 7,980 images over 12 inspection days in August and September 2023.
- Real labeled 10% masked data: created by applying inpainting masks to a subset of holes for testing missing-hole inference.
- The paper reports 665 masked holes in the real masked set and 4,964 masked holes in synthetic data.

### Baseline Model

- YOLOv7 was trained for 1,000 epochs with batch size 8 on an NVIDIA A100 GPU.
- Images were resized to 640 x 640 with padding to preserve aspect ratio.
- Binary models used a post-processing protocol to assign predicted holes to expected reference holes.
- Large-hole filtering used SSIM, local binary patch, and template matching thresholds; small-hole filtering kept the nearest predicted center.
- A minimum-cost assignment step mapped predictions to reference holes.
- CUT image-to-image translation was tested to make synthetic images more like real factory-floor images.

## Evidence

### Experimental Setup

Four variants were evaluated:

- Synthetic multi-class YOLOv7.
- I2I-translated multi-class YOLOv7.
- Synthetic binary YOLOv7 with custom category-ID protocol.
- I2I-translated binary YOLOv7 with custom category-ID protocol.

Confidence thresholds were tested in 5% increments from 50% to 95%. Models were evaluated using checkpoints with the highest validation recall because the paper prioritizes modified recall.

### Reported Results

| Model | Confidence threshold | Average recall | Average modified recall | Average precision | F0.9 | Modified F0.9 |
|---|---:|---:|---:|---:|---:|---:|
| Synthetic multi-class | 60 | 67.2 | 67.2 | 94.4 | 79.9 | 79.9 |
| I2I multi-class | 65 | 61.6 | 58.7 | 73.1 | 67.5 | 65.9 |
| Synthetic binary + custom category ID | 75 | 61.1 | 61.1 | 81.6 | 61.1 | 70.9 |
| I2I binary + custom category ID | 65 | 60.3 | 57.7 | 86.4 | 72.4 | 70.7 |

The synthetic multi-class model had the strongest reported average modified recall and precision. The paper reports no improvement from the simple CUT-based image-to-image translation pipeline.

## ML/DL Extraction

- Task formulation: object detection of existing stamped holes, with missing holes inferred from absent expected detections.
- Input: grayscale stamped metal-sheet images.
- Output: detected hole bounding boxes and hole categories, plus inferred missing-hole status through comparison against reference holes.
- Architecture: [[YOLOv7]].
- Training recipe: 1,000 epochs, batch size 8, 640 x 640 resized padded images, NVIDIA A100 GPU.
- Synthetic generation: Unreal Engine simulation of part/camera/lighting conditions.
- Domain adaptation: CUT image-to-image translation tested on synthetic images.
- Evaluation protocol: confidence-threshold sweep and modified metrics emphasizing low false positives on masked holes.
- Code: YOLOv7 code is externally available; paper-specific code availability is not reported.
- Data: dataset download URL is reported.

## Limitations

- Real missing-hole defects were not observed in the collected real data; evaluation uses artificially masked holes.
- Synthetic images lack conveyor and background artifacts present in real images, creating a domain gap.
- CUT image-to-image translation was applied in a simple patch-based way and did not improve performance.
- Dataset focuses on missing stamped holes, not the broader set of stamped metal-sheet defects such as splits or imprints.
- License terms for the released dataset are not reported in the paper text.

## Connections

### Graph Hubs

- Tasks: [[Metallic surface defect detection]], [[Defect segmentation]]
- Datasets: [[Open Stamped Parts Dataset]]
- Methods: [[YOLOv7]], [[Simulation-based data augmentation]], [[Contrastive unpaired translation]]
- Metrics: [[Precision]], [[Recall]], [[Modified recall]], [[Modified F0.9 score]]
- Domains: [[Automotive manufacturing]]

### Shares Dataset

- [[Open Stamped Parts Dataset]]: introduced by this paper as the primary data contribution.

### Shares Task

- [[Metallic surface defect detection]]: the paper targets stamped metal-sheet inspection in automotive manufacturing.
- [[Defect segmentation]]: synthetic images include segmentation masks around holes.

### Shares Method

- [[YOLOv7]]: baseline detector used in all benchmark variants.
- [[Simulation-based data augmentation]]: synthetic data is generated in Unreal Engine to mimic production variation.
- [[Contrastive unpaired translation]]: tested for synthetic-to-real image translation.

### Shares Metric

- [[Precision]] and [[Recall]]: reported for hole-detection performance.
- [[Modified recall]] and [[Modified F0.9 score]]: source-defined metrics for missing-hole-sensitive evaluation.

### Application/domain

- [[Automotive manufacturing]]: the dataset is collected for stamped metal-sheet inspection in auto manufacturing.
- [[Industrial visual inspection]] and [[Domain gap]]: the paper explicitly studies synthetic-to-real inspection data differences.

## Questions

- What license governs the dataset ZIP and annotations?
- Are the paper-specific training scripts or trained checkpoints available outside the dataset package?
- Would a real missing-hole collection change the model ranking versus the masked-hole evaluation?
