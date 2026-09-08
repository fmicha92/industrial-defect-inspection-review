---
title: "Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection"
aliases:
  - "Video-based two-stage optical glass defect detection"
paper_key: "sha256:34655142662b233874e7b22e9a9e5b17391cceb696a41b82f8db75437504204e"
paper_type: research
year: 2022
venue: "AI"
authors:
  - "Han Zhou"
  - "Xiaoling Yang"
  - "Zhongqi Wang"
  - "Jie Zhang"
  - "Yinchao Du"
  - "Jiangpeng Chen"
  - "Xuezhe Zheng"
status: processed
topics:
  - "optical glass defect detection"
  - "industrial visual inspection"
tasks:
  - "[[Optical glass defect detection]]"
domains:
  - "[[Glass inspection]]"
datasets:
  - "[[OGD-DET]]"
methods:
  - "[[Video-based two-stage defect detection]]"
  - "[[Color Channel Separation convolution]]"
  - "[[Clustering-based image quality evaluation]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[YOLOv4]]"
  - "[[Faster R-CNN]]"
  - "[[Single Shot MultiBox Detector]]"
  - "[[YOLOv5]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP@0.25]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.75]]"
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[FPS]]"
primary_metric: "[[mAP@0.25]]"
benchmarks:
  - "[[OGD-DET benchmark]]"
baselines:
  - "Faster RCNN"
  - "SSD300"
  - "SSD512"
  - "YOLOv5"
doi: "10.3390/ai3030033"
url: "https://doi.org/10.3390/ai3030033"
pdf: "paper-inbox/10_processed/Research/2022 - Zhou - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection.pdf"
code: "not reported"
data: "https://pntehan.github.io/OGD-DET/"
related_datasets:
  - "[[OGD-DET]]"
related_domains:
  - "[[Glass inspection]]"
related_tasks:
  - "[[Optical glass defect detection]]"
related_methods:
  - "[[Video-based two-stage defect detection]]"
  - "[[Color Channel Separation convolution]]"
  - "[[Clustering-based image quality evaluation]]"
related_benchmarks:
  - "[[OGD-DET benchmark]]"
source_file: "paper-inbox/10_processed/Research/2022 - Zhou - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Zhou - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Zhou - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection.txt"
processed_at: "2026-05-29"
---
# Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection

## Summary

- Proposes a video-based, coarse-to-fine detector for sub-millimeter optical-glass defects.
- Introduces [[OGD-DET]], a dataset of 3415 images from 40 optical-glass videos captured in real industrial production.
- Reports that the full method reaches 0.9948 AP@0.25, 1.0 recall, 0.9948 precision, and 21 FPS on the image-level OGD-DET setting.

## Paper Type

Research paper with a dataset contribution. The main contribution is a detection pipeline; the paper also introduces [[OGD-DET]] for optical-glass defect detection experiments.

## Problem

Sub-millimeter optical-glass defects are difficult to detect because they are extremely small, can appear on multiple glass surfaces, and are often imaged at high resolution. Downsampling can make defects invisible, while processing full-resolution images directly increases compute and memory cost.

## Contribution

- Claimed: A coarse-to-fine two-stage detection network locates the glass region on downsampled images and detects defects in the higher-resolution glass crop.
- Claimed: A video-based detection framework fuses multiple perspectives to improve recall when defects are visible only in some frames.
- Claimed: A clustering-based image quality evaluation module filters low-quality frames before final detection.
- Shown: [[OGD-DET]] contains 3415 images from 40 videos, with defect areas ranging from 0.1 mm to 0.53 mm and 2 to 7 pixels on 1536 x 1024 images.

## Method

The detector uses a coarse stage and a fine stage. The coarse stage uses a YOLOv4-style detector with a Darknet-tiny backbone and two feature-map scales to locate optical glass regions on downsampled images. The detected glass area is restored to high resolution and passed to the fine stage for defect detection.

The fine stage uses [[Color Channel Separation convolution]] in the backbone, applying channel-specific CBL and MCBL operations to learn RGB-channel detail for tiny defects. The video framework samples multiple frames from rotating optical-glass videos and fuses frame-level outputs: a sample is treated as defective if the defective-frame ratio exceeds 0.1 or if any detected defect confidence exceeds 0.8.

The [[Clustering-based image quality evaluation]] module extracts HOG features, clusters images with K-means, manually selects high-quality clusters, and discards frames whose HOG features are closest to lower-quality clusters.

## Evidence

### Dataset and Setup

- Dataset: [[OGD-DET]].
- Videos: 40 total; 25 videos for training and 15 videos for testing.
- Images: 3415 total; 511 images for testing after sampling videos at 8 images per second.
- Image resolution: 1536 x 1024 pixels before experiment resizing.
- Experiment resizing: 416 x 416 pixels.
- Video-level test: 15 videos, including 5 normal samples and 10 defective samples.
- K-means setup for IQE: 20 initial cluster centers, 9 high-quality classes selected, 100 K-means iterations.
- Hardware: 3080ti GPU Server for image-level speed comparisons.

### Results

| Setting | Dataset / task | Metric | Direction | Baseline | Reported result | Notes |
|---|---|---|---|---|---|---|
| Ablation baseline | [[OGD-DET]] / [[Optical glass defect detection]] | [[mAP@0.25]] | higher | YOLOv4: 0.6230 | Full method: 0.9948 | Full method includes two-stage, CCS, and IQE. |
| Ablation baseline | [[OGD-DET]] / [[Optical glass defect detection]] | [[Recall]] | higher | YOLOv4: 0.8380 | Full method: 1.0 | IoU 0.25 and confidence 0.5. |
| Ablation baseline | [[OGD-DET]] / [[Optical glass defect detection]] | [[Precision]] | higher | YOLOv4: 0.7030 | Full method: 0.9948 | IoU 0.25 and confidence 0.5. |
| Image-level comparison | [[OGD-DET benchmark]] | [[mAP@0.25]] | higher | Faster RCNN: 0.7821; SSD300: 0.6030; SSD512: 0.8760; YOLOv5: 0.9730 | Full method: 0.9948 | Table 2. |
| Image-level comparison | [[OGD-DET benchmark]] | [[mAP@0.50]] | higher | Faster RCNN: 0.6024; SSD300: 0.0280; SSD512: 0.5246; YOLOv5: 0.7720 | Full method: 0.8616 | Table 2. |
| Image-level comparison | [[OGD-DET benchmark]] | [[mAP@0.75]] | higher | Faster RCNN: 0.4740; SSD300: 0.0; SSD512: 0.2551; YOLOv5: 0.5270 | Full method: 0.8166 | Table 2. |
| Image-level throughput | [[OGD-DET benchmark]] | [[FPS]] | higher | Faster RCNN: 10; SSD300: 46; SSD512: 22; YOLOv5: 25 | Full method: 21 | Table 2. |
| Computational cost | [[OGD-DET benchmark]] | FLOPs / params | lower | YOLOv5: 109.1 G / 46.5 M | Full method: 104.2 G / 38.4 M | Table 3. |
| Video-level comparison | [[OGD-DET benchmark]] | [[Recall]] / [[Precision]] | higher | YOLOv5: 1.0 / 0.93 | Full method: 1.0 / 1.0 | Table 4. |

## ML/DL Extraction

- Task formulation: object/defect detection on high-resolution optical-glass imagery.
- Input: multiple video frames from optical-glass rotation videos; image-level experiments use frames resized to 416 x 416.
- Output: glass-region localization in the coarse stage and defect detection in the fine stage; video-level output from fused frame detections.
- Architecture: YOLOv4-based two-stage detector with Darknet-tiny in the coarse stage and CCS convolution in the fine stage.
- Training recipe: not reported beyond dataset split and K-means IQE setup.
- Losses/objectives: not reported.
- Optimizer and hyperparameters: not reported.
- Evaluation protocol: image-level and video-level OGD-DET tests; AP, recall, precision, FPS, FLOPs, and parameters.
- Baselines: Faster RCNN, SSD300, SSD512, YOLOv5, and ablated YOLOv4 variants.
- Artifacts: dataset URL reported; code not reported.

## Limitations

- The paper reports future work to conduct more experiments on large real-world datasets.
- Defect category names and annotation format are not reported in the extracted text.
- Training hyperparameters, optimizer, and implementation details are incomplete in the available source.
- Data availability is inconsistent across sources: the paper states the dataset is available via the OGD-DET project site, while the project site describes a request-review process.

## Connections

### Graph Hubs

- Tasks: [[Optical glass defect detection]]
- Methods: [[Video-based two-stage defect detection]], [[Color Channel Separation convolution]], [[Clustering-based image quality evaluation]], [[YOLOv4]]
- Datasets: [[OGD-DET]]
- Domains: [[Glass inspection]]
- Metrics: [[mAP@0.25]], [[mAP@0.50]], [[mAP@0.75]], [[Recall]], [[Precision]], [[FPS]]

### Shares Dataset

- [[OGD-DET]]: introduced and evaluated by this paper.

### Shares Task

- [[Optical glass defect detection]]: the paper targets sub-millimeter defect detection on optical glass.

### Shares Method

- [[Video-based two-stage defect detection]]: the core detection pipeline.
- [[Color Channel Separation convolution]]: the fine-stage backbone modification.
- [[Clustering-based image quality evaluation]]: filters blurry or out-of-focus frames before defect detection.

### Shares Metric

- [[Average precision]], [[mAP@0.25]], [[mAP@0.50]], [[mAP@0.75]], [[Recall]], [[Precision]], and [[FPS]] are used to evaluate OGD-DET detection performance.

### Application/Domain

- [[Glass inspection]]: the industrial use case is optical-glass quality inspection.

### Follow-Up Reading

- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]: both address glass-surface defect detection, but this paper uses multi-frame optical-glass videos while SSGD uses smartphone screen-glass images.

## Questions

- What are the exact OGD-DET defect categories and annotation file format?
- Is implementation code available outside the dataset request workflow?
- How stable are the reported video-level results on larger or more varied optical-glass datasets?
