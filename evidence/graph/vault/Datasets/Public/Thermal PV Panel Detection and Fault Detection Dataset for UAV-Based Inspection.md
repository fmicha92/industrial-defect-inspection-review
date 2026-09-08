---
title: "Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection"
aliases:
  - "Thermal PV Panel Detection Dataset for UAV Inspection"
  - "Synthetic PV fault dataset"
  - "UAV thermal PV panel detection dataset"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://zenodo.org/records/16420123"
doi: "10.5281/zenodo.16420123"
data_sources:
  - "Zenodo"
  - "Centre for Research and Technology Hellas"
licenses: "CC BY 4.0"
introduced_by: "[[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]]"
related_tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
related_methods:
  - "[[Infrared thermography]]"
  - "[[Synthetic data generation]]"
  - "[[Poisson defect image augmentation]]"
---
# Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection

## Definition

Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection is an open Zenodo dataset for photovoltaic panel detection and synthetic PV fault detection from UAV thermal imagery.

## Why It Matters

The dataset supports [[PV panel fault detection]] and [[Object detection]] for renewable-energy inspection. It provides annotated thermal images from a real PV farm and synthetic fault overlays for training fault detectors when real fault annotations are scarce.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Tasks: [[Object detection]] for PV panels and [[PV panel fault detection]] for synthetic fault categories.
- Modality: UAV thermal images.
- Host-reported source: DJI Mavic 3T UAV imagery from a photovoltaic farm in Sindos, Thessaloniki.
- Host-reported image resolution: 640 x 512.
- Host-reported split: 235 training images, 83 validation images, and 35 test images.
- Host-reported panel annotations: 18,487 training panels, 5,828 validation panels, and 2,363 test panels, for 26,678 total annotated PV panels.
- Host page count note: the Zenodo description says the processed subset contains 351 images but its split table totals 353 images; preserve the split table total until the release metadata is clarified.
- Paper-reported captured set: 713 thermal images and 713 RGB images were collected.
- Paper-reported refined set: 353 non-overlapping thermal images with 26,678 annotated panels.
- Paper-reported original panel annotations: 61,316 panel annotations before overlap reduction.
- Synthetic fault masks: 65 unique fault and damage masks generated with an MLLM.
- Synthetic fault instances: 638 total instances across damage, crack, snail trail, dust, delamination, and hotspots.
- File: `Thermal PV Panel Detection Dataset for UAV Inspection.zip`.
- File size: 15,172,606 bytes, shown as 15.2 MB on Zenodo.
- Checksum: `md5:c7c8b85ed4dbe6d7422e45b1776d3fa7`.
- License: CC BY 4.0.
- Zenodo DOI: `10.5281/zenodo.16420123`.

## Source Anchors

- Hosting source: [Zenodo record 16420123](https://zenodo.org/records/16420123).
- Dataset DOI: [10.5281/zenodo.16420123](https://doi.org/10.5281/zenodo.16420123).
- Introducing paper: [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]].

## Used In These Papers

- [[2025 - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging]] introduces the dataset, generates synthetic PV fault overlays, and evaluates YOLOv11 models on panel detection and synthetic fault detection.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[PV panel fault detection]]
- [[Infrared thermography]]
- [[Synthetic data generation]]
- [[Defect synthesis]]
- [[Poisson defect image augmentation]]
