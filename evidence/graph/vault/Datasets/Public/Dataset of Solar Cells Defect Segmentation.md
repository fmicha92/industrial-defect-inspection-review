---
title: "Dataset of Solar Cells Defect Segmentation"
aliases:
  - "Dataset_of_solar_cells-defect_segmentation"
  - "SolarCells"
  - "SolarCells-S"
  - "PVEL-S"
  - "xiaoyunchen666 dataset-of-solar-cells-defect-segmentation"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://www.kaggle.com/datasets/xiaoyunchen666/dataset-of-solar-cells-defect-segmentation"
data_sources: "Kaggle"
introduced_by: "[[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]]"
related_papers:
  - "[[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect segmentation]]"
licenses: "Unknown"
---
# Dataset of Solar Cells Defect Segmentation

## Definition

Dataset of Solar Cells Defect Segmentation is a Kaggle-hosted release of three electroluminescence solar-cell defect segmentation datasets: SolarCells, SolarCells-S, and PVEL-S.

## Why It Matters

The dataset provides refined pixel-level defect labels for training semantic segmentation networks on photovoltaic-cell electroluminescence imagery. It supports [[Solar cell defect detection]] as a localization task rather than only image-level classification.

## Used In These Papers

- [[2025 - Lightweight Multiscale Feature Fusion Network for Solar Cell Defect Detection]] introduces SolarCells, SolarCells-S, and PVEL-S as refined-label datasets for segmentation networks and links the Kaggle release.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Tasks: [[Solar cell defect detection]], [[Defect segmentation]].
- Hosting source: Kaggle.
- Kaggle owner: `xiaoyunchen666`.
- Modality: electroluminescence solar-cell images.
- Annotation type: refined defect labels; PVEL-S is described as pixel-level defective-region labeling.
- Dataset components: SolarCells, SolarCells-S, and PVEL-S.
- SolarCells: 190 monocrystalline silicon-cell EL defect images collected from the web, resolution 448 x 448; 152 training images and 38 test images.
- SolarCells-S: 36 monocrystalline EL defect images from a partner company; original split of 28 training and 8 test images; augmented by 180-degree rotation, mirroring, darkening, and brightening to 144 training images and 36 test images.
- PVEL-S: subset of [[PVEL-AD]] with 1200 polysilicon defect images selected and pixel-level labeled; 960 training images and 240 test images.
- PVEL-AD source context: [[PVEL-AD]] contains 36,543 polysilicon abnormal-defect images with 12 categories including cracks, broken grids, black cores, thick lines, scratches, fragments, and broken angles.
- Split: 8:2 train/test split reported for all three dataset components on the current Kaggle owner page.
- License: Unknown.
- Availability: public Kaggle dataset; download requires Kaggle access/session.

## Source Anchors

- Hosting source: https://www.kaggle.com/datasets/xiaoyunchen666/dataset-of-solar-cells-defect-segmentation.
- Introducing paper: https://doi.org/10.32604/cmc.2024.058063.
- Host-page facts recorded here: dataset title, Kaggle owner, component dataset names, image counts, splits, image resolution for SolarCells, augmentation operations for SolarCells-S, PVEL-S relationship to [[PVEL-AD]], task, modality, and license status.
- Paper-source facts recorded here: the DOI-linked paper reports that SolarCells, SolarCells-S, and PVEL-S are made available on this Kaggle page as refined-label datasets for solar-cell defect segmentation.

## Related Datasets

- [[PVEL-AD]]: PVEL-S is a pixel-level segmentation subset derived from PVEL-AD.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar cell defect detection]]
- [[Defect segmentation]]
- [[LMFF]]
