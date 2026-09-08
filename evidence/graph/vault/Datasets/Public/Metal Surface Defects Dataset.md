---
title: "Metal Surface Defects Dataset"
aliases:
  - "C5Data2"
  - "c5data2"
  - "niclinn/c5data2"
related_domain: "[[Metal inspection]]"
url: "https://www.kaggle.com/datasets/niclinn/c5data2"
data_sources: "Kaggle"
license: "CC0: Public Domain"
availability: "public"
owner: "Nick Lin"
tasks:
  - "[[Metallic surface defect detection]]"
  - "[[Object detection]]"
  - "[[Surface defect detection]]"
source_datasets:
  - "[[GC10-DET]]"
introduced_by: "not reported"
related_papers:
  - "[[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]]"
status: "subset"
---
# Metal Surface Defects Dataset

## Definition

Metal Surface Defects Dataset is a public Kaggle package derived from [[GC10-DET]], not a standalone dataset in the metal-inspection graph. The Kaggle metadata reports 693 images with one XML label file per image and six defect types: crease, inclusion, oil spot, rolled pit, waist folding, and burrs.

## Why It Matters

The package is useful as a smaller public packaging of GC10-DET-style metal surface defect images, but [[GC10-DET]] should be treated as the canonical dataset. It should not be counted as a separate metal-inspection dataset in domain summaries.

## Used In These Papers

- No direct introducing or usage paper for the Kaggle package was found during the audit.
- [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]] is the relevant source-dataset paper because the Kaggle metadata reports that images are partly collected from [[GC10-DET]].

## Dataset Details

- Dataset reference: `niclinn/c5data2`.
- Creator/owner: Nick Lin.
- Availability: public Kaggle dataset; Kaggle reports `isPrivate: false`.
- License: CC0: Public Domain.
- Size: 445,075,963 bytes.
- Last updated: 2022-09-01.
- Images: 693.
- Labels: each image has a corresponding XML label file marking the defect region with a box.
- Defect types: crease, inclusion, oil spot, rolled pit, waist folding, and burrs.
- Source composition: collected from a combination of [[GC10-DET]] and metal defect images collected online.
- Standalone status: not standalone; treat as a subset or repackaging of [[GC10-DET]] unless a source demonstrates independent collection and evaluation protocol.
- Host tags: image, deep learning, manufacturing, CNN.
- Splits: not reported.
- Introducing publication: not reported.

## Source Anchors

- Hosting source: https://www.kaggle.com/datasets/niclinn/c5data2.
- Kaggle API reference: `niclinn/c5data2`.
- Source dataset named by the host: [[GC10-DET]].
- Introducing publication: not reported.
- Related source-dataset paper: [[2020 - Deep Metallic Surface Defect Detection The New Benchmark and Detection Network]].

## Related Concepts

- [[Metal inspection]]
- [[Metallic surface defect detection]]
- [[Object detection]]
- [[Surface defect detection]]
- [[GC10-DET]]

## Questions

- The Kaggle metadata does not report train, validation, or test splits.
- The Kaggle metadata does not report the full online image sources beyond naming [[GC10-DET]] and online metal defect images.
