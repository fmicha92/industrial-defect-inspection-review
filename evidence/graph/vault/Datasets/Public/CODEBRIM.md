---
title: "CODEBRIM"
aliases:
  []
availability: "public"
status: stable
concept_type: dataset
related_domain: "[[Construction inspection]]"
url: "https://doi.org/10.5281/zenodo.2620293"
data_sources: "Zenodo"
introduced_by: "not reported"
---
# CODEBRIM

## Definition

CODEBRIM is a concrete-bridge defect inspection dataset used by Defect-GAN for defect synthesis and multi-label defect classification experiments. The Defect-GAN paper reports six mutually non-exclusive classes: crack, spallation, efflorescence, exposed bars, corrosion, and normal samples.

## Why It Matters

It anchors Defect-GAN evaluation to a named construction-inspection dataset with both image patches and original full-resolution images from which patches are cropped.

## Used In These Papers

- [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] uses CODEBRIM to train Defect-GAN and to evaluate whether synthesized defect images improve ResNet34 and DenseNet121 inspection accuracy.

## Dataset Details

- Domain: [[Construction inspection]]
- Task: [[Defect classification]]
- Classes reported in Defect-GAN: crack, spallation, efflorescence, exposed bars, corrosion, and normal.
- Data form reported in Defect-GAN: image patches for multi-label classification plus full-resolution source images.
- Availability: public DOI reported by the paper.

## Source Anchors

- Hosting source: https://doi.org/10.5281/zenodo.2620293
- Introducing paper: not reported.

## Related Concepts

- [[Construction inspection]]
- [[Defect classification]]
- [[Defect synthesis]]
