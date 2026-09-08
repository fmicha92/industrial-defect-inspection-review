---
title: "Real-IAD"
aliases:
  - "Real-IAD"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://realiad4ad.github.io/Real-IAD"
data_sources:
  - "https://realiad4ad.github.io/Real-IAD"
  - "https://huggingface.co/datasets/Real-IAD/Real-IAD"
introduced_by: "[[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]]"
related_papers:
  - "[[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]]"
availability: "public gated"
access: "Hugging Face dataset card reports a publicly accessible repository with condition acceptance and automatically approved access request."
license: "CC-BY-NC-SA-4.0"
modalities:
  - "RGB images"
  - "pixel-level anomaly masks"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
---
# Real-IAD

## Definition

Real-IAD is a real-world multi-view industrial anomaly detection dataset with 151,050 high-resolution images from 30 object classes. The introducing paper reports 99,721 normal images and 51,329 anomalous images, five shooting angles per object, pixel-level anomaly masks, and image resolutions cropped to roughly 2,000-5,000 pixels from original 3,648 x 5,472 camera captures.

## Dataset Details

- Scope: 30 industrial products covering materials such as metal, plastic, wood, ceramics, and mixed materials.
- Defects: missing parts, dirt, deformation, pits, damage, holes, cracks, and scratches are reported in the construction procedure; the project page maps folder codes to eight defect types: pit, deformation, abrasion, scratch, damage, missing parts, foreign objects, and contamination.
- Acquisition: one top-view camera plus four approximately 45-degree symmetric side views are used to abstract multi-view visual quality inspection.
- Annotation: anomalous images have pixel-level masks created with LabelMe, then cleaned through repeated model-assisted confident-learning checks and manual inspection.
- Splits and evaluation assets: the host distributes 1024 x 1024 downsampled images, raw high-resolution images, and JSON split files.
- Access: public gated research dataset hosted on Hugging Face; users must accept conditions and share contact information, and the access request is reported as automatically approved.
- License: CC-BY-NC-SA-4.0 on the Hugging Face dataset card.

## Why It Matters

Real-IAD expands industrial anomaly benchmarks beyond single-view, small-scale datasets by combining many object categories, five views, dense anomaly labels, and fully unsupervised industrial anomaly detection settings.

## Used In These Papers

- [[2025 - Real-IAD D3 A Real-World 2D Pseudo-3D 3D Dataset for Industrial Anomaly Detection]] extends the Real-IAD dataset family.
- [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] supports few-shot anomaly generation, industrial anomaly image generation.
- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] introduces Real-IAD with 151,050 images, 30 object classes, five views per object, pixel-level masks, and UIAD/FUIAD benchmark settings.
- [[2025 - Free Lunch of Image-mask Alignment for Anomaly Image Generation and Segmentation]] evaluates image-mask aligned diffusion synthesis on Real-IAD and reports average mIoU improving from 65.13 with AnomalyDiffusion to 70.16.

## Source Anchors

- Hosting source: https://realiad4ad.github.io/Real-IAD.
- Dataset files: https://huggingface.co/datasets/Real-IAD/Real-IAD.
- Introducing paper: [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]].
- Code/example repository: https://github.com/Tencent/AnomalyDetection_Real-IAD.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
