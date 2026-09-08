---
title: "Pharmaceutical bag thermal sealing defect dataset"
aliases:
  - "Thermal imaging pharmaceutical bag sealing defect dataset"
related_domain: "[[Pharmaceutical packaging inspection]]"
url: "https://doi.org/10.5281/zenodo.18616983"
data_sources: "Zenodo"
introduced_by: "[[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]]"
---
# Pharmaceutical Bag Thermal Sealing Defect Dataset

## Definition

The pharmaceutical bag thermal sealing defect dataset contains thermal imaging samples from heat-sealing cycles of pharmaceutical plastic bags, labeled as normal or leakage-defective based on localized abnormal temperature elevation.

## Why It Matters

The dataset exposes an extreme class-imbalance setting: the paper reports 2309 real heat-sealing cycles with 2281 normal samples and only 28 defective samples, then expands defective training data with physics-guided synthesis.

## Used In These Papers

- [[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]] introduces the dataset and evaluates [[TMFFNet]] on it.

## Dataset Details

- Domain: [[Pharmaceutical packaging inspection]].
- Task: [[Pharmaceutical bag sealing defect detection]].
- Sensor: Hikmicro HM-TD2C68E-25/Q vanadium oxide uncooled detector.
- Sensor resolution: 640 x 512.
- Frame rate: 50 Hz.
- Focal length: 25 mm.
- Imaging distance: 10 cm.
- Real heat-sealing cycles: 2309.
- Real normal samples: 2281.
- Real defective samples: 28.
- Generated defective samples: 2104.
- Total samples after augmentation: 4385.
- Label rule: localized abnormal temperature elevation greater than 1 degree Celsius at the heat-sealed region is labeled as leakage defect.
- Preprocessing: images resized to 256 x 256 for model input.
- Availability: public Zenodo repository is reported by the paper.
- License: not reported in the processed paper text.

## Source Anchors

- Hosting source: https://doi.org/10.5281/zenodo.18616983.
- Introducing paper: [[2026 - Thermal Imaging for Sealing Defect Detection in Pharmaceutical Bags Using a Temporal Fusion Network]].

## Related Concepts

- [[Pharmaceutical bag sealing defect detection]]
- [[Pharmaceutical packaging inspection]]
- [[TMFFNet]]
- [[Class imbalance]]
- [[Data augmentation]]
