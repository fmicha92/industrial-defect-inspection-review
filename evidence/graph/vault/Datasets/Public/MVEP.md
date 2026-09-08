---
title: "MVEP"
aliases:
  - "MVEP version1"
  - "Multi-View Evaluation Protocol for Glass Container Inspection"
related_domain: "[[Glass inspection]]"
tasks:
  - "[[Glass container defect detection]]"
  - "[[Defect classification]]"
url: "https://datasets.projet.liris.cnrs.fr/mvep-version1"
data_sources: "LIRIS datasets library"
license: "Creative common"
introduced_by: "https://hal.science/hal-05494004v1"
---
# MVEP

## Definition

MVEP is a public multi-view glass-container inspection benchmark for evaluating multi-view fusion methods in industrial quality control of transparent materials. It contains 16,000 synchronized multi-view images of glass containers captured from six calibrated viewpoints under controlled industrial lighting.

## Why It Matters

The dataset supports [[Glass container defect detection]] and [[Defect classification]] where specular reflections, refractions, and transparency effects make single-view inspection unreliable. It includes object-level bounding boxes and ordinal severity labels for surface degradation defects, supporting multi-view fusion, ordinal classification, cross-view consistency, and robustness to annotation noise.

## Used In These Papers

- [HAL preprint placeholder](https://hal.science/hal-05494004v1) is the planned host for the MVEP introducing paper.

## Dataset Details

- Domain: [[Glass inspection]].
- Tasks: [[Glass container defect detection]], [[Defect classification]].
- Hosting source: LIRIS datasets library.
- Canonical URL: https://datasets.projet.liris.cnrs.fr/mvep-version1.
- Version: version1.
- Publication date: 04/02/2026 as displayed by the source.
- Authors: Gwendal Bernardi, Godefroy Brisebarre, Sebastien Roman, Mohsen Ardabilian, Emmanuel Dellandrea.
- License: Creative common.
- Access status: public download links provided through FTP and HTTPS.
- FTP download root: ftp://datasets.liris.cnrs.fr/mvep.
- HTTPS download root: https://dataset-dl.liris.cnrs.fr/mvep.
- Dataset size: 12.9 Go.
- Image count: 16,000 synchronized multi-view images.
- Object type: glass containers.
- Viewpoints: six calibrated viewpoints.
- Lighting: controlled industrial lighting.
- Annotation types: object-level bounding boxes and ordinal severity labels.
- Defect focus: erasure-type surface degradation defects.
- Excluded defect terminology: scuffing.
- Quality labels: ordinal severity grades from minimal visual alteration to critical damage requiring rejection.
- Split structure: `train` and `test` directories.
- Sample structure: each article is represented by 12 images captured from multiple viewpoints, with a corresponding annotation file for each image.
- Image naming convention: `timestamp_modality_view_camera.extension`.
- Camera codes: `E` denotes a top-down camera; `C` denotes a front-facing camera.
- Annotation format: YOLO-style text lines with `class_id x_center y_center width height`, using normalized bounding-box coordinates.
- Metadata file: root-level `dataset.json`.
- `dataset.json` fields include image identifier, file name and path, image resolution, view index, camera type, capture configuration, article position, defect class information, and absolute-pixel bounding boxes.
- Example resolution in metadata snippet: 1008 x 1008 pixels.
- Keywords: Multi-View Object Detection, Ordinal Classification, Industrial Inspection, Glass Container Quality Control, Defect Detection, Severity Assessment, Transparent Material Inspection.
- Related paper: HAL preprint placeholder at https://hal.science/hal-05494004v1.
- DOI: not reported.

## Source Anchors

- Hosting source: https://datasets.projet.liris.cnrs.fr/mvep-version1.
- FTP download root: ftp://datasets.liris.cnrs.fr/mvep.
- HTTPS download root: https://dataset-dl.liris.cnrs.fr/mvep.
- Introducing paper placeholder: https://hal.science/hal-05494004v1.

## Related Concepts

- [[Glass container defect detection]]
- [[Defect classification]]
- [[Glass inspection]]
- [[Industrial visual inspection]]
- [[Surface defect detection]]
