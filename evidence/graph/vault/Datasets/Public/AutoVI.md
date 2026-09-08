---
title: "AutoVI"
aliases:
  - "AutoVI"
  - "Automotive Visual Inspection Dataset"
  - "The Automotive Visual Inspection Dataset"
related_domain: "[[Automotive manufacturing]]"
url: "https://zenodo.org/records/10459003"
official_website: "https://autovi.utc.fr/"
doi: "10.5281/zenodo.10459003"
paper_doi: "10.1016/j.compind.2024.104151"
data_sources:
  - "Zenodo"
  - "Renault Group automotive production lines"
licenses:
  - "CC-BY-NC-SA-4.0"
version: "1.0.0"
access: "open"
modalities:
  - "image"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Surface defect detection]]"
methods:
  - "[[Unsupervised anomaly detection]]"
code: "https://github.com/phcarval/autovi_evaluation_code"
related_papers:
  - "[[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]]"
introduced_by: "[[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]]"
---
# AutoVI

## Definition

AutoVI is an automotive production-line visual inspection dataset for unsupervised anomaly detection. It contains images acquired on Renault Group assembly lines under genuine production conditions, including moving components and variations in brightness and lighting.

## Why It Matters

AutoVI gives anomaly-detection methods a public benchmark closer to real automotive inspection conditions than highly controlled industrial-image datasets. It targets non-listed defects: defects that were not available when the inspection system was developed.

## Dataset Details

- Dataset purpose: benchmark advanced unsupervised anomaly detection algorithms under real automotive production conditions.
- Zenodo creators: Philippe Carvalho, Meriem Lafou, Alexandre Durupt, Antoine Leblanc, and Yves Grandvalet.
- Website contributor statement: Renault Group, OPMobility, Continental, and Universite de technologie de Compiegne through the Roberval and Heudiasyc laboratories.
- Production context: Renault Group automotive production lines.
- Modality: photographs of inspected production-line items.
- Paper categories: engine_wiring, pipe_clip, pipe_staple, tank_screw, underbody_pipes, and underbody_screw.
- Paper split: 1530 normal-only training images, 1533 non-defective test images, and 887 defective test images.
- Paper image sizes: engine_wiring, pipe_clip, and pipe_staple are 400 x 400; tank_screw, underbody_pipes, and underbody_screw are 1000 x 750.
- Defect types: both structural and logical defects, including missing or misplaced items, incorrectly fastened cables, misplaced hoops, contaminants, and operators blocking inspection areas.
- Labels and annotations: non-defective images are stored under `good`; defective images are organized by defect folders; defective items have one or more segmentation masks locating the defect.
- Datasheet categories: engine wiring, pipe clip, pipe staple, tank screw, underbody pipes, and underbody screw.
- Datasheet image count: 3950 images across the six item categories.
- Zenodo v1.0.0 image count: 3950 images split into 1530 training images and 2420 testing images.
- Official-website landing-page count: 11 classes and 7184 images split into training and testing images.
- Source discrepancy: Zenodo v1.0.0 and the datasheet report 3950 images, while the official website landing page reports 7184 images and 11 classes. Preserve both counts until the release relationship is clarified.
- Splits: training and test folders are provided; the datasheet states training data contains only non-defective data, while test and ground-truth folders are subdivided by defect typology.
- License: CC-BY-NC-SA-4.0.
- Access: open dataset record on Zenodo.
- Distribution: Zenodo dataset DOI `10.5281/zenodo.10459003`; total listed files are about 4.0 GB.
- Distributed files: `engine_wiring.zip`, `pipe_clip.zip`, `pipe_staple.zip`, `tank_screw.zip`, `underbody_pipes.zip`, `underbody_screw.zip`, plus `readme.md`, `license.txt`, and `changelog.txt`.
- Evaluation code: [https://github.com/phcarval/autovi_evaluation_code](https://github.com/phcarval/autovi_evaluation_code)
- Earlier/raw versions: the datasheet links older versions at Zenodo, including an initial eight-class set and a raw uncropped image release.

## Used In These Papers

- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] introduces AutoVI and benchmarks CFlow, DRAEM, DSR, EfficientAD, PaDiM, and Patchcore on six real automotive assembly-line inspection tasks.

## Source Anchors

- Zenodo record: [https://zenodo.org/records/10459003](https://zenodo.org/records/10459003)
- Official website: [https://autovi.utc.fr/](https://autovi.utc.fr/)
- Croissant metadata: [https://autovi.utc.fr/download/croissant.json](https://autovi.utc.fr/download/croissant.json)
- Datasheet: [https://autovi.utc.fr/download/datasheet.md](https://autovi.utc.fr/download/datasheet.md)
- Dataset DOI: [10.5281/zenodo.10459003](https://doi.org/10.5281/zenodo.10459003)
- Introducing paper DOI: [10.1016/j.compind.2024.104151](https://doi.org/10.1016/j.compind.2024.104151)

## Related Concepts

- [[Automotive manufacturing]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
- [[Industrial anomaly detection]]
- [[Unsupervised anomaly detection]]
- [[Patch-based anomaly detection]]
