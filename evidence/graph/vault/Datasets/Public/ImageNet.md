---
title: "ImageNet"
aliases:
  - "ImageNet"
  - "ILSVRC"
related_domain: "[[General computer vision]]"
url: "https://www.image-net.org/"
data_sources: "ImageNet project website"
introduced_by: "[ImageNet: A large-scale hierarchical image database](https://openalex.org/W2108598243)"
doi: "10.1109/CVPR.2009.5206848"
availability: "restricted to research and educational access under ImageNet terms"
licenses: "ImageNet does not own image copyrights; access is governed by ImageNet terms"
---
# ImageNet

## Definition

ImageNet is a large-scale image dataset organized according to the WordNet hierarchy. The project provides human-annotated images for synsets and is commonly used to train general-purpose visual recognition backbones.

## Why It Matters

ImageNet pretraining is used as a transfer-learning starting point when industrial defect datasets are small. Its graph-facing domain is [[General computer vision]] because the dataset is not an industrial anomaly benchmark, even when ImageNet-pretrained models are later fine-tuned for inspection tasks.

## Used In These Papers

- [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] uses an ImageNet-pretrained 18-layer ResNet before synthetic pretraining and real-world fine-tuning.
- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]] fine-tunes ImageNet-pretrained ResNet34 and ResNet50 backbones on [[NEU-DET]].

## Source Anchors

- Hosting source: [ImageNet project website](https://www.image-net.org/).
- Access: ImageNet provides access for non-commercial research and educational use under stated conditions and terms.
- Copyright note: ImageNet does not own the images; it compiles web-image lists for WordNet synsets.
- Introducing paper: [ImageNet: A large-scale hierarchical image database](https://openalex.org/W2108598243), CVPR 2009, DOI [10.1109/CVPR.2009.5206848](https://doi.org/10.1109/CVPR.2009.5206848).

## Dataset Details

- Domain: [[General computer vision]].
- Task: large-scale object recognition and image classification.
- Organization: images are organized by WordNet synsets.
- Project scale: the ImageNet site reports 14,197,122 indexed images and 21,841 indexed synsets.
- Paper-reported 2009 state: 12 subtrees, 5,247 synsets, and 3.2 million images.
- Target construction goal: populate most WordNet noun synsets with roughly 500-1,000 clean full-resolution images per synset.
- Annotation: quality-controlled and human-annotated concept images.

## Related Concepts

- [[General computer vision]]
- [[Image classification]]
- [[Transfer learning]]
