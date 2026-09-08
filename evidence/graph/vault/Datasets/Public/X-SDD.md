---
title: "X-SDD"
aliases:
  - "Xsteel Surface Defect Dataset"
  - "X-SDD Database"
  - "strip steel surface defect dataset"
related_domain: "[[Metal inspection]]"
url: "https://www.kaggle.com/datasets/sayelabualigah/x-sdd"
data_sources:
  - "Kaggle"
  - "https://github.com/Fighter20092392/X-SDD-A-New-benchmark"
introduced_by: "[[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]]"
related_papers:
  - "[[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]]"
  - "[[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]]"
availability: "public"
access: "Kaggle dataset page is public; Kaggle download requires Kaggle access"
licenses:
  - "Kaggle license: Unknown"
---
# X-SDD

## Definition

X-SDD is a public hot-rolled strip steel surface defect dataset for defect classification and downstream detection experiments. The introducing paper defines it as the Xsteel Surface Defect Dataset and reports 1,360 three-channel JPG defect images at 128 x 128 pixels across seven defect categories.

## Why It Matters

It supplements [[NEU-CLS]] with one additional defect class and stronger class imbalance. That makes it useful for evaluating steel surface defect classifiers, imbalance-aware training, and augmentation methods such as [[GT-CutMix]].

## Used In These Papers

- [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]] introduces X-SDD and evaluates RepVGG+SA and multiple CNN baselines for seven-class hot-rolled steel strip defect classification.
- [[2024 - Surface Defect Detection of Strip Steel Based on GT-CutMix Augmentation Algorithm and Improved DSSD Model]] uses X-SDD for GT-CutMix augmentation and improved DSSD object detection experiments.

## Dataset Details

- Size: 1,360 defect images.
- Image format: 128 x 128 pixel, three-channel JPG images.
- Source setting: hot-rolled steel strip production field with an acquisition setup similar to a machine-vision steel surface inspection system.
- Classes: slag inclusions/inclusion, red iron sheet, iron sheet ash, scratches, oxide scale of plate system, finishing roll printing, and oxide scale of temperature system.
- Class counts: inclusion 238, red iron sheet 397, iron sheet ash 122, scratches 134, oxide scale of plate system 63, finishing roll printing 203, oxide scale of temperature system 203.
- Classification split in the introducing paper: 70% train and 30% test, reported as 952 training images and 408 test images.
- Detection split in the later GT-CutMix paper: 940 training images and 420 test images.
- Annotation type: the introducing paper supports image-level defect classification; the later GT-CutMix paper uses X-SDD with bounding-box annotations for object detection.
- Availability: public Kaggle dataset page and introducing-paper GitHub link.
- Kaggle distribution: zip file, 6,430,967 bytes in the structured page metadata.
- License: Kaggle license is listed as Unknown.

## Source Anchors

- Kaggle host: https://www.kaggle.com/datasets/sayelabualigah/x-sdd.
- Kaggle title: X-SDD Database.
- Kaggle creator: Sayel Abualigah.
- Introducing paper: [[2021 - X-SDD A New Benchmark for Hot Rolled Steel Strip Surface Defects Detection]].
- Paper-reported data availability: https://github.com/Fighter20092392/X-SDD-A-New-benchmark.

## Related Concepts

- [[Metal inspection]]
- [[Metallic surface defect detection]]
- [[Defect classification]]
- [[NEU-CLS]]
- [[Accuracy]]
