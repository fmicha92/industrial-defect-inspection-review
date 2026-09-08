---
title: "KolektorSDD"
aliases:
  - "KolektorSDD"
availability: "public"
status: stable
concept_type: dataset
related_domain: "[[Metal inspection]]"
url: "https://www.vicos.si/resources/kolektorsdd/"
data_sources: "Kolektor Group"
introduced_by: "[[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]]"
related_papers:
  - "[[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]]"
---
# KolektorSDD

## Definition

KolektorSDD is a public surface-defect dataset of grayscale electrical commutator images. It contains 400 images at 1408 x 512 resolution, including 50 defect-positive images and 350 defect-negative images, with pixel-wise masks for cracks or microscopic fractions on the inspected commutator surfaces.

## Why It Matters

It supports public evaluation or training for metal surface defect detection, localization, classification, segmentation, generation, or benchmark construction.

## Dataset Details

- Source: images of defected electrical commutators provided and annotated by Kolektor Group d.o.o. and Kolektor Orodjarna d.o.o.
- Collection: 50 defective commutators, each represented by 8 non-overlapping surface images captured in a controlled environment.
- Size: 400 grayscale images; each physical item has one image with a visible defect and seven non-defective images.
- Labels: every image has a detailed pixel-wise defect mask.
- Evaluation protocol: the introducing paper uses threefold cross-validation and keeps images from the same physical product in the same fold.
- Availability: public.
- License: not reported.
- Domain: [[Metal inspection]].

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] introduces KolektorSDD and reports a 99.9% [[Average precision]] result with one false negative using a [[Segmentation-decision network]].
- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[KolektorSDD]] for industrial defect benchmark, semantic defect annotation.
- [[2024 - Efficient and Accurate Semi-Supervised Semantic Segmentation for Industrial Surface Defects]] evaluates semi-supervised defect segmentation on KolektorSDD and reports a 4.39% [[mIoU]] improvement over the current SOTA.
- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses KolektorSDD as a source dataset for [[Industrial-5i]].
- [[2022 - A New Cycle-Consistent Adversarial Networks With Attention Mechanism for Surface Defect Classification With Small Samples]] uses KolektorSDD for small-sample defect classification; the paper reports 399 electrical commutator images, 50 visible-defect images, and 98.53% AttenCGAN accuracy with eight defect samples.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] evaluates weak, mixed, and fully supervised learning on KolektorSDD and reports AP improving from 93.4 with weak labels only to 99.1 with five pixel-annotated positive samples.

## Source Anchors

- Hosting source: https://www.vicos.si/resources/kolektorsdd/.
- Paper-reported public download: http://www.vicos.si/Downloads/KolektorSDD.
- Introducing paper: [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]].

## Related Concepts

- [[Metal inspection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
