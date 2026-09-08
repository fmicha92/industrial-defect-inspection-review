---
title: "mAP@0.50"
aliases:
  - "mean average precision at IoU 0.50"
tags:
  - metric
  - detection
---

# mAP@0.50

## Definition

mAP@0.50 is mean average precision evaluated at an IoU threshold of 0.50.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] reports 81.5% mAP@0.50 for [[YOLO-AL]] on [[APDDD]].
- [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] reports YOLOX mAP@0.5 improvements after adding DG-GAN-generated pseudo-defect images.
- [[2023 - Deep Learning Based Online Metallic Surface Defect Detection Method for Wire and Arc Additive Manufacturing]] reports 94.5 mAP@0.5 for YOLO-attention on the WAAM metallic surface defect dataset.
- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] uses mAP@0.50 as the primary metric and reports a 3.1% improvement in the abstract.
- [[2021 - Generative Adversarial Networks for Data Augmentation in Structural Adhesive Inspection]] reports GAN-augmented YOLOv4-Tiny mAP@0.50 of 0.7708 on validation and 0.5788 on holdout structural adhesive defect images.
- [[2023 - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data]] reports mAP@.5 for YOLO-v5 and YOLO-v8 defect detection on SAPF and NEU-CLS after adding generated defect images.
- [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] reports AP50 for CNN and Transformer detectors on [[SSGD benchmark]].
- [[2022 - Video-Based Two-Stage Network for Optical Glass Sub-Millimeter Defect Detection]] reports AP@0.50 for image-level comparison on [[OGD-DET benchmark]].
- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] reports mAP50 on [[MSDD]], with YOLOv8-l reaching 0.854 and TSCM/vector-quantization ablations ranging from 0.759 to 0.784.
- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] reports 0.951 mAP50 for YOLOv11l panel detection and 0.769 mAP50 for YOLOv11x synthetic PV fault detection.
- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] reports [[DsPCBSD+]] AP50 of 0.848 for [[Co-DETR]] and 0.851 for [[YOLOv6-L6]].
- [[2024 - LoHi-WELD A Novel Industrial Dataset for Weld Defect Detection and Classification, a Deep Learning Study, and Future Perspectives]] uses mAP@0.50 for YOLOv7 weld defect detection, reporting 0.64 on `lweld` and 0.69 on `hweld` for fine-grained detection.
- [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] uses mAP@0.50 as the primary metric for RUOD, CARPK, and CarDD under 1/5/10-shot cross-domain detection settings.
- [[2024 - High-Precision Defect Detection in Solar Cells Using YOLOv10 Deep Learning Model]] reports 98.5% mAP@0.5 for YOLOv10x on [[EL Solar Cells Dataset]].

## Related Metrics

- [[mAP@0.15]]
- [[mAP@0.30]]
- [[Detection metrics]]
