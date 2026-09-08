---
title: "Defect Spectrum"
aliases:
  - "Defect Spectrum"
  - "Defect Spectrum benchmark"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://envision-research.github.io/Defect_Spectrum/"
data_sources:
  - "Project site"
  - "Hugging Face"
  - "GitHub"
introduced_by: "[[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]]"
availability: "public"
licenses: "not reported"
---
# Defect Spectrum

## Definition

Defect Spectrum is a large-scale industrial defect benchmark with richer semantic annotations built from four existing industrial benchmarks. It refines annotations, distinguishes multiple defect types within a single image, and adds descriptive captions for samples.

## Why It Matters

It supports granular [[Defect segmentation]] and [[Defect classification]] research across multiple industrial sources. The benchmark also anchors Defect-Gen, a diffusion-based synthetic defect generator evaluated on Defect Spectrum subsets.

## Used In These Papers


- [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]] uses or reports [[Defect Spectrum]] for industrial defect benchmark, semantic defect annotation.

## Source Anchors

- Project page: [Defect Spectrum](https://envision-research.github.io/Defect_Spectrum/).
- Dataset host: [Hugging Face dataset](https://huggingface.co/datasets/DefectSpectrum/Defect_Spectrum).
- Code: [GitHub repository](https://github.com/EnVision-Research/DefectSpectrum).
- Introducing paper: [[2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics]].

## Dataset Details

- Domain: [[Multi-industry anomaly detection]].
- Task: [[Defect segmentation]] and [[Defect classification]].
- Source benchmarks: the paper reports Defect Spectrum subsets as DS-MVTec, DS-VISION, DS-DAGM2007, and DS-Cotton-Fabric. [[MVTec AD]] and [[DAGM2007]] are represented as existing dataset notes; VISION V1 and Cotton-Fabric are not yet represented as standalone dataset notes.
- Size: 3,518 real images plus 1,920 synthetic images.
- Labels: 125 defect labels and 552 images with multiple defect types.
- Annotation: refined pixel masks, semantic defect labels, multi-defect labels, and manually refined captions.
- Synthetic data: [[Defect-Gen]] generates synthetic images for DS-MVTec, DS-Cotton, and DS-VISION; the paper reports no extra synthetic data for DS-DAGM2007 because DAGM2007 is already synthetic.
- License: not reported.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Semantic defect annotation]]
