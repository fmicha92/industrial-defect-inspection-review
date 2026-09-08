---
title: "PV Panel Defect Dataset"
aliases:
  - "PV panel defect dataset"
  - "Alicja Lenarczyk PV Panel Defect Dataset"
  - "Solar PV panel defect dataset"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://www.kaggle.com/datasets/alicjalena/pv-panel-defect-dataset"
data_sources: "Kaggle"
introduced_by: "[[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]]"
related_papers:
  - "[[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]]"
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
  - "[[2025 - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
licenses: "CC BY-NC-SA 4.0"
---
# PV Panel Defect Dataset

## Definition

PV Panel Defect Dataset is a Kaggle-hosted photovoltaic panel image dataset by Alicja Lenarczyk for classifying panel conditions and defects across six classes. It is introduced by [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]].

## Why It Matters

It gives [[Solar cell defect detection]] and [[Defect classification]] a public RGB-image dataset for panel-level condition classification, including environmental obstruction and physical or electrical damage categories.

## Used In These Papers

- [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]] introduces the 1,574-image six-class dataset and benchmarks ML/DL classifiers on it.
- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] uses an 875-image selected subset for a CNN performance and explainability audit.
- [[2025 - Comparative Deep Learning for RGB-Based PV Surface Fault Classification Using ResNet50 and EfficientNetB0]] benchmarks ResNet50, EfficientNetB0, MobileNetV3Small, and DenseNet121 on the 1,574-image six-class RGB dataset with training-data augmentation.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Task: [[Solar cell defect detection]], [[Defect classification]].
- Creator: Alicja Lenarczyk.
- Modality: photovoltaic panel images.
- Total images: 1,574.
- Split: 929 training images, 550 validation images, and 95 test images.
- Classes: Bird-drop, Clean, Dusty, Electrical-damage, Physical-damage, and Snow-covered.
- Class totals: Bird-drop 298, Clean 289, Dusty 275, Electrical-damage 225, Physical-damage 225, and Snow-covered 262.
- Source composition: the Kaggle page reports the pythonafroz Kaggle solar-panel-images subset as a source plus supplementary images manually collected from public web sources.
- License: CC BY-NC-SA 4.0.
- Availability: public Kaggle dataset; download requires a Kaggle session.

## Source Anchors

- Hosting source: https://www.kaggle.com/datasets/alicjalena/pv-panel-defect-dataset.
- Introducing paper: [[2025 - Comparison of ML classifiers in automatic diagnostics of PV panels using deep image features]].
- Source subset: pythonafroz Kaggle solar-panel-images.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar cell defect detection]]
- [[Defect classification]]
- [[Shortcut learning]]
