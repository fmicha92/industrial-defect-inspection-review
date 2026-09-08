---
title: "SolarDK"
aliases:
  - "SolarDK dataset"
  - "SolarDK: A high-resolution urban solar panel image classification and localisation dataset"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://osf.io/aj539/overview"
data_sources: "OSF"
introduced_by: "[[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]]"
related_papers:
  - "[[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]]"
related_tasks:
  - "[[Solar panel classification]]"
  - "[[Solar panel localization]]"
  - "[[Urban semantic segmentation]]"
licenses: "CC BY 4.0"
---
# SolarDK

## Definition

SolarDK is a public high-resolution aerial-imagery dataset for classifying and localizing photovoltaic systems in Denmark. It includes manually labelled urban classification examples, segmentation masks for the same positive instances, and a larger BBR-derived classification set.

## Why It Matters

SolarDK supports [[Solar panel classification]] and [[Solar panel localization]] in a geographic setting where models trained on one region can fail to generalize to another. The dataset is designed for benchmarking solar-panel mapping from aerial imagery rather than surface-defect inspection.

## Used In These Papers

- [[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]] introduces SolarDK and reports baseline classification and segmentation results.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Tasks: [[Solar panel classification]], [[Solar panel localization]], and [[Urban semantic segmentation]].
- Host: https://osf.io/aj539/overview.
- Platform: OSF.
- License: CC BY 4.0.
- Copyright holder: Otovo AS.
- Dataset repository title: "SolarDK: A high-resolution urban solar panel image classification and localisation dataset".
- Description: images and masks with binary labels for whether a PV system exists in the image and which pixels contain PV.
- Public status: public OSF project; OSF wiki says contributors do not need to register to download the files.
- Stored files: `dataset_v2` folder with 20 split archive parts named `solardk_dataset_part_00` through `solardk_dataset_part_19`.
- Hosted file size: 20,799,894,869 bytes across the 20 OSF file parts.
- Download method: OSF wiki recommends `osf -p aj539 clone <output_directory>`, then concatenating `solardk_dataset_part_*` and extracting with `tar`.
- Dataset tree: `bbr/positive`, `gentofte_trainval/train/{mask,negative,positive}`, `gentofte_trainval/val/{mask,negative,positive}`, and `herlev_test/test/{mask,negative,positive}`.
- Source imagery: GeoDanmark aerial images with variable ground sample distance between 10 cm and 15 cm, sampled between March 1 and May 1, 2021.
- Geographic coverage: Gentofte and Herlev municipalities for the manually labelled classification and segmentation data; BBR-derived positive examples span Denmark.
- Manual classification examples: 23,417 hand-labelled images, with 22,537 negative examples and 880 positive examples.
- Segmentation labels: 880 segmentation masks for the same positive instances used in the manually labelled classification set.
- BBR classification set: 104,397 positive examples gathered from the Danish national building registry.
- Area reported in the paper: Herlev 12.07 km2, Gentofte 25.70 km2, BBR 3,853.02 km2, total 3,890.79 km2.
- Split: Gentofte provides training and validation examples; Herlev is used as the test set.
- Training split: 10,376 negatives and 323 positives.
- Validation split: 5,113 negatives and 159 positives.
- Test split: 7,048 negatives and 398 positives.
- Privacy handling: geospatial coordinates of images and PV systems are not included; BBR metadata is aggregated at municipal level.

## Source Anchors

- Hosting source: https://osf.io/aj539/overview.
- OSF API: https://api.osf.io/v2/nodes/aj539/.
- Introducing paper: [[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]].
- Citation requested by OSF wiki: Khomiakov, Radzikowski, Schmidt, Sørensen, Andersen, Andersen, and Frellsen, 2022, arXiv:2212.01260.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar panel classification]]
- [[Solar panel localization]]
- [[Urban semantic segmentation]]
- [[SolarDK benchmark]]
