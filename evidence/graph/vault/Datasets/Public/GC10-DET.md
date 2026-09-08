---
title: "GC10-DET"
aliases:
  - "GC10-DET Metallic Surface Defect Dataset"
  - "Defects location for metal surface"
related_domain: "[[Metal inspection]]"
url: "https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets"
data_sources:
  - "GitHub"
  - "Kaggle"
additional_sources:
  - "https://www.kaggle.com/datasets/zhangyunsheng/defects-class-and-location"
introduced_by: "[[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]"
---
# GC10-DET

## Definition

GC10-DET is a public steel sheet surface defect dataset for [[Metallic surface defect detection]] and [[Object detection]]. The dataset contains 3,570 grayscale images collected in a real industrial setting and covers 10 annotated surface defect categories.

## Dataset Details

- Task: defect class localization on metal surface images.
- Surface and material: steel sheet surfaces.
- Collection setting: real industry.
- Image count: 3,570 grayscale images.
- Defect classes: punching, weld line, crescent gap, water spot, oil spot, silk spot, inclusion, rolled pit, crease, and waist folding.
- Primary host: [GitHub](https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets).
- Additional host: [Kaggle Defects location for metal surface](https://www.kaggle.com/datasets/zhangyunsheng/defects-class-and-location), listed with the subtitle "The GC10-DET dataset."
- Kaggle dataset reference: `zhangyunsheng/defects-class-and-location`.
- Kaggle owner: Via. (`zhangyunsheng`).
- Kaggle access: public/free metadata page; Kaggle structured metadata marks the distribution as requiring a Kaggle subscription/account for download.
- Kaggle license: Unknown.
- Kaggle package size: 967,813,910 bytes.
- Kaggle last updated: 2020-06-21.

## Defect Classes

- Punching: unwanted punched regions caused by mechanical failure during strip production.
- Weld line: a strip-change weld seam that is not strictly a defect but must be detected and tracked to avoid downstream cuts.
- Crescent gap: a half-circle-like cutting defect in steel strip production.
- Water spot: a low-contrast drying-related surface mark that can resemble an oil spot.
- Oil spot: lubricant-contamination marks that affect surface appearance.
- Silk spot: local or continuous wave-like plaque on strip surfaces, with uneven density along the strip length.
- Inclusion: irregular spot, fish-scale, strip, or block-like defects, often rough or pockmarked.
- Rolled pit: periodic bulges or pits on the steel plate surface, mainly linked to roll damage.
- Crease: transverse fold patterns across or near the edge of the strip.
- Waist folding: obvious folds or wrinkles caused by excessive local deformation.

## Why It Matters

GC10-DET expands metallic surface inspection beyond smaller steel defect datasets by combining 10 industrial defect categories with localization annotations. It is useful for evaluating detectors on low-contrast classes, visually similar classes such as water spots and oil spots, and defect categories with different shapes and spatial scales.

## Used In These Papers

- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] introduces GC10-DET and evaluates EDDN, SSD, Faster R-CNN, and YOLO baselines.
- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] evaluates automatic data augmentation on GC10-DET and reports ALADA mAP of 71.23 with FRCNN and 67.91 with RetinaNet.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] uses GC10-DET to compare FID scores for generated images across 10 metal surface defect categories.
- [[2023 - Metal Surface Defect Detection Based on Improved YOLOv5]] evaluates an augmented GC10-DET object-detection split and reports 82.8% [[mAP@0.50]] for the CSPLayer + Global Attention Mechanism detector.
- [[2024 - Resilient Machine Learning for Steel Surface Defect Detection Based on Lightweight Convolution]] evaluates a YOLOv8n-derived detector on GC10-DET, improving [[mAP@0.50]] from 56.7% to 62.2%.
- [[2024 - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network]] evaluates FOHR Net on GC10-DET and reports 70.5% [[mAP]].
- [[2025 - CSDD A Benchmark Dataset for Casting Surface Defect Detection and Segmentation]] compares CSDD against GC10-DET and uses GC10-DET for detector generalization experiments.

## Source Anchors

- Primary hosting source: https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets.
- Additional hosting source: https://www.kaggle.com/datasets/zhangyunsheng/defects-class-and-location.
- Introducing paper: [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]].
- Related Kaggle package: [[Metal Surface Defects Dataset]] is derived from [[GC10-DET]] and online metal defect images; treat it as a subset or repackaging rather than a standalone dataset.

## Related Concepts

- [[Metallic surface defect detection]]
- [[Object detection]]
- [[Metal inspection]]
- [[Average precision]]
- [[mAP]]
- [[NEU-DET]]
- [[CSDD]]
- [[Metal Surface Defects Dataset]]

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] supports steel surface defect detection, object detection.

## Questions

- The Kaggle mirror reports an unknown license; verify the authoritative license before redistribution or commercial use.
- The Kaggle metadata available without authentication does not report file-level structure or train/test splits.
