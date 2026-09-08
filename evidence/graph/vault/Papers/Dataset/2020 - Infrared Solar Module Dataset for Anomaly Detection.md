---
title: "Infrared Solar Module Dataset for Anomaly Detection"
aliases:
  - "InfraredSolarModules paper"
paper_key: "sha256:3ef9bb50acd5bfdf44ae18f850572b4c60608582a3f2ce7eb3863c330d093402"
authors:
  - "Matthew Millendorf"
  - "Edward Obropta"
  - "Nikhil Vadhavkar"
year: 2020
venue: "ICLR 2020 AI for Earth Sciences Workshop"
paper_type: "dataset"
status: "processed"
topics:
  - "infrared solar module imagery"
  - "solar module anomaly classification"
  - "class imbalance"
tasks:
  - "[[Solar module anomaly classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[InfraredSolarModules]]"
methods:
  - "[[Infrared thermography]]"
metrics:
  - "[[Accuracy]]"
primary_metric: "not reported"
baselines: "not reported"
benchmarks: "not reported"
code: "not reported"
data: "[[InfraredSolarModules]]"
licenses: "MIT License"
related_concepts:
  - "[[Class imbalance]]"
related_methods:
  - "[[Infrared thermography]]"
related_datasets:
  - "[[InfraredSolarModules]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar module anomaly classification]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Millendorf - Infrared Solar Module Dataset for Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Millendorf - Infrared Solar Module Dataset for Anomaly Detection.txt"
source_file: "paper-inbox/10_processed/Dataset/2020 - Millendorf - Infrared Solar Module Dataset for Anomaly Detection.pdf"
processed_at: "2026-06-04"
---
# Infrared Solar Module Dataset for Anomaly Detection

## Summary

The paper introduces [[InfraredSolarModules]], a labeled dataset of 20,000 low-resolution infrared solar-module images across 12 classes. It is intended to support machine-learning research on [[Solar module anomaly classification]] for remote solar-farm inspection.

## Paper Type

Dataset paper. The primary contribution is a public labeled dataset and class taxonomy, not a new model or benchmark result.

## Problem

Solar farms increasingly use remote sensing and infrared imaging for inspection, but expert review is still required to identify and classify anomalies. Public infrared solar-module data are scarce, limiting machine-learning research on automated inspection.

## Contribution

- Introduces [[InfraredSolarModules]], a public dataset of real-world infrared solar-module imagery.
- Defines 12 classes: 11 anomaly classes plus `No-Anomaly`.
- Highlights class imbalance in solar PV anomaly detection and provides class counts that researchers can rebalance for experiments.
- Provides repository packaging with image files and per-image metadata.

## Method

Raptor Maps aggregated real-world solar-module inspection data collected by piloted aircraft and unmanned aerial systems. The collection used midwave or longwave infrared imaging systems in the 3-13.5 micrometer range and visible-spectrum imaging systems. Anomalies were cropped to individual modules and separated into classes; corresponding visible-spectrum images were used during classification to increase labeling accuracy.

The paper does not report a trained baseline model. It proposes future work around benchmarking classification results, adding more classes, recognizing unknown anomaly types outside the 12 dataset classes, and optimizing algorithms for low-performance edge devices.

## Evidence

### Dataset

- Dataset: [[InfraredSolarModules]].
- Total images: 20,000.
- Image size: 24 x 40 pixels.
- Classes: Cell, Cell-Multi, Cracking, Hot-Spot, Hot-Spot-Multi, Shadowing, Diode, Diode-Multi, Vegetation, Soiling, Offline-Module, and No-Anomaly.
- Largest class: No-Anomaly with 10,000 images.
- Smallest class: Diode-Multi with 175 images.
- Paper-reported dataset size: 81.9 MB.
- Repository package: the GitHub README reports `2020-02-14_InfraredSolarModules.zip`, containing an `images` directory and `module_metadata.json`.

### Class Imbalance

The paper compares the dataset proportions with aerial-inspection findings and explicitly frames solar PV anomaly detection as class-imbalanced. It reports that a global aerial-inspection report found anomalies in 2.2% of modules, while the dataset includes 10,000 no-anomaly images to support broad nominal-condition classification.

### Results

- Classification baseline: not reported.
- Accuracy, precision, recall, F1-score, or mAP values: not reported.
- Benchmark protocol: not reported.

## ML/DL Extraction

- Task formulation: multiclass image classification for infrared solar-module anomaly categories.
- Inputs: 24 x 40 infrared module crops.
- Labels: one of 12 anomaly/no-anomaly classes.
- Model architecture: not reported.
- Training recipe: not reported.
- Evaluation protocol: not reported.
- Metrics: the paper proposes benchmarking classification results but does not report metric values.
- Compute/hardware: several GPUs may be needed for research projects using the data; specific hardware is not reported.
- Code: not reported.
- Data availability: GitHub repository for [[InfraredSolarModules]].

## Limitations

- The paper does not provide baseline classification performance.
- The class proportions differ from real-world proportions because more anomaly classes exist in field inspections than the 12 included classes.
- The paper calls for adding more classes and recognizing anomalies outside the provided label set.
- The images are low resolution, 24 x 40 pixels.
- The paper does not report detailed labeling agreement, train/test splits, or a benchmark protocol.

## Connections

### Graph Hubs

- Tasks: [[Solar module anomaly classification]]
- Methods: [[Infrared thermography]]
- Datasets: [[InfraredSolarModules]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]]

### Shares dataset

- [[InfraredSolarModules]] - the paper introduces and hosts the dataset.

### Shares task

- [[Solar module anomaly classification]] - the dataset is organized for classifying solar-module anomaly classes from infrared imagery.

### Shares method

- [[Infrared thermography]] - the data are collected using midwave or longwave infrared imaging from piloted aircraft and unmanned aerial systems.

### Related concept

- [[Class imbalance]] - the paper explicitly highlights anomaly-class imbalance and compares dataset proportions with field inspection findings.

### Application/domain

- [[Solar cells and photovoltaic]] - the dataset targets solar PV module inspection.

## Questions

- What train/validation/test split should be used for reproducible benchmarking?
- Which metrics best handle the class imbalance across rare anomaly classes?
- How well do models trained on 24 x 40 thermal crops transfer to higher-resolution or visible-spectrum inspection imagery?
