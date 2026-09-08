---
title: "Real-IAD D3"
aliases:
  - "Real-IAD D³"
  - "Real-IAD D3"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://realiad4ad.github.io/Real-IAD_D3"
data_sources:
  - "https://realiad4ad.github.io/Real-IAD_D3"
  - "https://huggingface.co/datasets/Real-IAD/Real-IAD_D3"
introduced_by: "[[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]]"
related_papers:
  - "[[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]]"
availability: "approval-gated"
access: "Hugging Face dataset card reports a publicly visible repository, but file access requires condition acceptance and institutional approval or email request."
license: "CC-BY-NC-SA-4.0"
modalities:
  - "RGB images"
  - "pseudo-3D photometric-stereo data"
  - "3D point clouds"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
---
# Real-IAD D3

## Definition

Real-IAD D3 is a multimodal industrial anomaly detection dataset with synchronized 2D RGB images, pseudo-3D photometric-stereo data, and 3D point-cloud data. The introducing paper reports 8,450 samples across 20 industrial product categories and 69 defect groups, with 5,000 normal samples and 3,450 abnormal samples.

## Dataset Details

- Scope: 20 industrial products across material types including metal, plastic, ceramics, and composites.
- Defects: the paper reports scratches, dents, cracks, missing parts, and deformation as manually introduced defect examples.
- Modalities: each sample includes synchronized 2D, pseudo-3D photometric-stereo fusion, TIFF, and PLY data; supported 3D formats include ASC, PLY, STL, OBJ, IGES, and TIFF.
- Spatial detail: the paper reports four point-cloud resolutions up to 16.2 million points at 5328 x 3040, 0.002 mm point precision, defect area proportions from 0.46% to 6.39%, and defective-point proportions from 0.33% to 7.34%.
- Acquisition: a unified setup captures high-resolution RGB images at 3,648 x 5,472 pixels, pseudo-3D surface normals from four directional light sources, and 3D point clouds from four-direction DLP structured light.
- Access: approval-gated research dataset on Hugging Face; the dataset card asks users to accept conditions and indicates institutional-email approval or affiliation email request.
- License: CC-BY-NC-SA-4.0 on the Hugging Face dataset card.

## Why It Matters

Real-IAD D3 provides a larger and finer-resolution multimodal benchmark than earlier RGB-D industrial anomaly datasets, especially for subtle surface defects where RGB, pseudo-3D, and point-cloud data can carry complementary evidence.

## Used In These Papers

- [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]] introduces the dataset and evaluates multimodal IAD.

## Source Anchors

- Hosting source: https://realiad4ad.github.io/Real-IAD_D3.
- Dataset files: https://huggingface.co/datasets/Real-IAD/Real-IAD_D3.
- Introducing paper: [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]].

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Real-IAD]]
- [[MVTec3D]]
- [[Photometric stereo]]
- [[Industrial anomaly detection]]
