---
title: "ELPV Dataset"
aliases:
  - "elpv-dataset"
  - "A Benchmark for Visual Identification of Defective Solar Cells in Electroluminescence Imagery"
  - "Defective solar cells in electroluminescence imagery"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://github.com/zae-bayern/elpv-dataset"
data_sources:
  - "GitHub"
  - "PyPI"
introduced_by: "https://doi.org/10.4229/35thEUPVSEC20182018-5CV.3.15"
related_papers:
  - "[[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]]"
  - "[[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
licenses:
  - "CC BY-NC-SA 4.0 for images"
  - "Apache License 2.0 for Python source code"
modalities:
  - "electroluminescence grayscale images"
dataset_sizes:
  - "2,624 images"
labels:
  - "defect probability"
  - "solar module type"
---
# ELPV Dataset

## Summary

ELPV Dataset is a public GitHub-hosted dataset of solar-cell images extracted from high-resolution electroluminescence images of photovoltaic modules. The repository describes it as a benchmark for visual identification of defective solar cells in electroluminescence imagery.

## Dataset Details

- Hosting source: [GitHub](https://github.com/zae-bayern/elpv-dataset).
- Package access: the README reports installation through `pip install elpv-dataset`.
- Size: 2,624 samples.
- Image format: 300 x 300 pixel, 8-bit grayscale images.
- Source modules: images were extracted from 44 different solar modules.
- Modality: electroluminescence images of photovoltaic solar cells.
- Labels: each image is annotated with a defect probability between 0 and 1 and the module type, reported as mono- or polycrystalline.
- Preprocessing reported by the repository: images are normalized for size and perspective, and camera-lens distortion was removed before solar-cell extraction.
- Defect scope: the repository states that annotated defects are intrinsic or extrinsic and reduce solar-module power efficiency.
- License: images are licensed under CC BY-NC-SA 4.0; accompanying Python source code is under Apache License 2.0.

## Source

- Host page: [zae-bayern/elpv-dataset](https://github.com/zae-bayern/elpv-dataset).
- Introducing publication: [A Benchmark for Visual Identification of Defective Solar Cells in Electroluminescence Imagery](https://doi.org/10.4229/35thEUPVSEC20182018-5CV.3.15).
- Additional cited publications on the host page: [Segmentation of photovoltaic module cells in uncalibrated electroluminescence images](https://doi.org/10.1007/s00138-021-01191-9) and [Automatic classification of defective photovoltaic module cells in electroluminescence images](https://doi.org/10.1016/j.solener.2019.02.067).

## Used In These Papers

- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] uses ELPV for binary and multiclass solar-cell defect classification; the paper reports 2,624 images, an 80/20 random split, and 98.15% binary accuracy with fused Inception-V3 and ResNet50 features.

- [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] reports the data URL as `https://github.com/zae-bayern/elpv-dataset` and evaluates solar-cell defect classification on 2,624 electroluminescence images.
- [[2023 - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images]] reports the same dataset URL as a public PV-defective electroluminescence image dataset used for defect classification.
- [[2024 - Improved Hybrid Solar Cell Defect Detection Using GANs and Weighted Classification]] uses ELPV for binary solar-cell defect classification and reports WGAN-GP augmentation at 94.11% accuracy, 96.70% recall, and 95.71% F-score.
- [[2025 - Advanced deep learning modeling to enhance detection of defective photovoltaic cells in electroluminescence images]] uses EL solar-cell images for GAN-oversampled defect classification with CNN backbones and reports a best extracted class recall mean of 0.9013 for ResNet152 with 4C-AUG300.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar cell defect detection]]
- [[Defect classification]]
