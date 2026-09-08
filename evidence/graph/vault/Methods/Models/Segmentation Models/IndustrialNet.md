---
title: "IndustrialNet"
aliases:
  - "IndustrialNet-L2"
  - "IndustrialNet-Cosine"
  - "IndustrialNet-Proto"
  - "IndustrialNet-Merge"
tags:
  - method
  - model
status: "stable"
concept_type: "method"
source_papers:
  - "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
evidence_count: 1
related_methods:
  - "[[ResNet50]]"
  - "[[U-Net]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
---

# IndustrialNet

## Definition

IndustrialNet is a few-shot industrial defect segmentation model proposed in [[2023 - Few-shot semantic segmentation for industrial defect recognition]]. It compares normal support images with an abnormal query image, uses [[ResNet50]] features to estimate defect-related distance maps, and decodes the fused features into a binary defect mask.

## Why It Matters

IndustrialNet targets defect segmentation for product categories without many labeled defect examples. On [[Industrial-5i]], the paper reports higher [[mIoU]] and [[FB-IoU]] than FSS-1000, MMNet, MSNet, and HSNet.

## Method Details

- Backbone: ImageNet-pretrained [[ResNet50]].
- Inputs: K normal support images and one abnormal query image.
- Feature comparison: query features are matched to support features by cosine similarity, then an L2 distance between original and replaced query features estimates likely defects.
- Decoder: U-Net-like multi-scale decoder.
- Loss: weighted cross-entropy.
- Primary reported variant: IndustrialNet-L2.

## Used In These Papers

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] proposes IndustrialNet for few-shot segmentation on [[Industrial-5i]].

## Related Concepts

- [[Few-shot anomaly detection]]
- [[Defect segmentation]]
- [[Industrial anomaly detection]]
- [[ResNet50]]
- [[U-Net]]
