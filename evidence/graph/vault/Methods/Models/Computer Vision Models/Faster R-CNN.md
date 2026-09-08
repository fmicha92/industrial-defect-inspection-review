---
title: "Faster R-CNN"
aliases:
  - "Faster RCNN"
tags:
  - method
  - model
  - object-detection
---
# Faster R-CNN

## Definition

Faster R-CNN is a two-stage object detection model family used as a baseline in industrial defect detection papers.

## Why It Matters

It provides a common region-proposal baseline for comparing detection accuracy and throughput against one-stage and task-specific detectors.

## Used In These Papers

- [[2021 - Industrial Machine Tool Component Surface Defect Dataset]] describes [[Mask R-CNN]] as including a Faster R-CNN detection stage for pitting segmentation on [[BSData]].
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] compares against Faster R-CNN on metallic surface defect detection.
- [[2022 - MSFT-YOLO Improved YOLOv5 Based on Transformer for Detecting Defects of Steel Surface]] reports improvement over Faster R-CNN on NEU-DET.
- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] compares against Faster RCNN on [[OGD-DET benchmark]].
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] benchmarks CNN and Transformer variants under Faster R-CNN.
- [[2024 - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection]] uses Faster R-CNN with FPN as the baseline for [[CE-SGNet]].
- [[2019 - Structured Domain Randomization Bridging the Reality Gap by Context-Aware Synthetic Data]] trains Faster R-CNN on SDR-generated road scenes for KITTI vehicle detection.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] compares DDN against Faster R-CNN on [[NEU-DET]] and reports higher mAP for DDN under VGG16 and ResNet34/50 settings.

## Related Concepts

- [[Single Shot MultiBox Detector]]
- [[YOLOv5]]
- [[Mask R-CNN]]
- [[Average precision]]
- [[Object detection]]
- [[CE-SGNet]]
